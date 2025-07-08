import pandas as pd
import chromadb
import uuid


class Portfolio:
    def __init__(self, file_path=r"C:\Users\msdho\Downloads\my_portfolio.csv"):
        """
        Initializes the Portfolio with a CSV file path.
        It loads the data, sets up a persistent ChromaDB client,
        and gets or creates a collection named "portfolio".

        Args:
            file_path (str): The path to the CSV file containing portfolio data.
                             Expected columns: "Techstack" and "Links".
        """
        self.file_path = file_path
        try:
            self.data = pd.read_csv(file_path)
        except FileNotFoundError:
            print(f"Error: my_portfolio.csv not found at {file_path}. Please ensure the file exists.")
            # Create an empty DataFrame to avoid further errors if file is missing
            self.data = pd.DataFrame(columns=["Techstack", "Links"])
            
        self.chroma_client = chromadb.PersistentClient('vectorstore')
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):
        """
        Loads the portfolio data into the ChromaDB collection.
        This method only adds data if the collection is currently empty,
        preventing duplicate entries on successive runs.
        """
        if not self.collection.count():
            print("Loading portfolio into ChromaDB...")
            for index, row in self.data.iterrows():
                # Ensure 'Techstack' and 'Links' columns exist before accessing
                if "Techstack" in row and "Links" in row:
                    self.collection.add(
                        documents=row["Techstack"],
                        metadatas={"links": row["Links"]},
                        ids=[str(uuid.uuid4())]
                    )
                else:
                    print(f"Warning: Row {index} missing 'Techstack' or 'Links' column. Skipping.")
            print("Portfolio loading complete.")
        else:
            print("Portfolio already loaded in ChromaDB (collection is not empty).")

    def query_links(self, skills):
        """
        Queries the ChromaDB collection for links relevant to the given skills.

        Args:
            skills (list or str): A list of strings representing skills to query,
                                  or a single string.

        Returns:
            list: A list of metadata dictionaries, each containing a 'links' key,
                  or an empty list if no relevant links are found or skills list is empty.
        """
        # Ensure skills is a list of strings
        if isinstance(skills, str):
            skills = [skills]
        elif not isinstance(skills, list):
            print(f"Warning: 'skills' input is not a list or string. Received type: {type(skills)}. Returning empty list.")
            return [] # Return empty if not a valid type

        # IMPORTANT: Check if the skills list is empty before querying ChromaDB
        if not skills:
            print("No skills provided for query. Returning empty list.")
            return []

        try:
            results = self.collection.query(
                query_texts=skills,
                n_results=2 # Retrieve top 2 most relevant results
            )
            return results.get('metadatas', [])
        except Exception as e:
            print(f"Error querying ChromaDB: {e}")
            return []
