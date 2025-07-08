An AI-powered Streamlit application that automatically generates tailored cold emails by scraping job listings and matching them with your portfolio. Ideal for showcasing company capabilities in response to job postings.

🔧 Features
🔍 Job Extraction: Parses a job description from a URL using LangChain and a powerful LLM.

✉️ Cold Email Generation: Crafts professional emails aligned with the job posting.

💼 Portfolio Matching: Integrates links from your past projects using a semantic search powered by ChromaDB.

🌐 Web UI: Simple and interactive interface via Streamlit.

🧩 Tech Stack
Streamlit for UI

LangChain + Groq (LLaMA3 model)

ChromaDB for vector storage and search

pandas for CSV-based portfolio input

📂 File Structure
bash
Copy
Edit
├── app.py             # Streamlit UI and main app runner
├── chain.py           # LLM-based job extraction and email generation
├── potofilo.py        # Portfolio loader and semantic query engine
├── .env               # Store your GROQ_API_KEY here
├── my_portfolio.csv   # CSV file with Techstack and Links columns
🚀 How to Run
Clone this repository:

bash
Copy
Edit
git clone https://github.com/your-username/your-repo.git
cd your-repo
Set up your environment:

Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Create a .env file:

ini
Copy
Edit
GROQ_API_KEY=your_api_key_here
Prepare your portfolio:

Create my_portfolio.csv with columns: Techstack, Links.

Run the app:

bash
Copy
Edit
streamlit run app.py
📌 Example Portfolio CSV
cs
Copy
Edit
Techstack,Links
Machine Learning,https://example.com/project1
Streamlit Web App,https://example.com/project2
🧠 Credits
Built using LangChain

Powered by Groq's LLaMA3 API

Vector search via ChromaDB

