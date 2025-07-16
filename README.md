🧠📈 Financial Stock Analysis using LlamaIndex & OpenAI

This project provides a lightweight AI-powered **financial stock analysis** assistant. It uses **LlamaIndex**, **OpenAI (GPT-3.5-Turbo)**, and **Streamlit** to analyze articles and generate intelligent stock reports.

---

🚀 Features

- 📄 Index financial news articles from the `articles/` folder
- 🔍 Query insights using OpenAI's GPT
- 🧠 LlamaIndex for vector-based document retrieval
- 🖥️ Interactive UI with Streamlit
- 🔐 Secure environment using `.env` file for API keys
- 🧾 Report generation:
  - Single Stock Outlook
  - Competitor Analysis

---

🗂️ Project Structure
```plaintext
Financial-Stock-Analysis/
│
├── articles/                  # Folder for financial news documents (.txt/.pdf/.docx)
├── src/
│   ├── 01_fetch_data.py       #  Script for fetching articles 
│   ├── 02_index_news.py       # Index documents using LlamaIndex
│   └── 03_query_news.py       # Query indexed documents (backend logic)
│
├── storage/                   # Auto-generated vector index files (ignored in Git)
├── app.py                     # Streamlit UI for querying
├── .env                       # Contains OpenAI API key (not pushed to Git)
├── requirements.txt           # Python dependencies
└── README.md                  # Project overview
```


---

🧪 Setup Instructions

1️⃣ Clone the repo

```bash
git clone https://github.com/your-username/financial-stock-analysis.git
cd financial-stock-analysis
```

2️⃣ Create and activate a virtual environment
```bash
conda create -n Myenv python=3.8 -y
conda activate Myenv
```

3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

4️⃣ Set your OpenAI API Key

Create a .env file in the root directory:
```bash
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
5️⃣ Prepare the data

Place your .docx, .pdf, or .txt news articles in the articles/ folder.

6️⃣ Run the indexer
```bash
python src/02_index_news.py
```
This will create the vector index and persist it in the storage/ folder.

7️⃣ Launch the Streamlit app
```bash
streamlit run app.py
```

📋 Usage

📌 Single Stock Outlook

Enter a stock ticker (e.g., AAPL) and receive a report on its outlook for 2023–2027, including risks.

📌 Competitor Analysis

Enter two tickers (e.g., GOOGL vs MSFT) to compare their performance, strategy, and outlook.


📦 Dependencies
	•	LlamaIndex
	•	OpenAI API
	•	Streamlit
	•	Python-dotenv

📎 Notes
	•	storage/ is ignored by Git to avoid pushing vector data.
	•	.env file is also excluded for security.
	•	The app is compatible with Python 3.8–3.11 (avoid 3.13+ due to LlamaIndex issues).


