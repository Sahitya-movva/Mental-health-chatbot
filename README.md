# AI Mental Health Support Assistant

A simple Python-based emotional support chatbot using NLP, a mini RAG concept, and safe responses.

🧠 Overview

This project is a lightweight AI-powered mental health assistant that provides empathetic, non-clinical emotional support through simple natural language conversation.

It uses:

Rule-based NLP for emotion detection

Keyword-based risk detection for safety

A mini Knowledge Base (RAG-style retrieval)

LLM-style template responses (offline, no API required)

This is a beginner-friendly project designed for AI/ML interviews, campus drives, and GitHub portfolio building.

🌼 Features
✔ Emotion Detection

Classifies user messages into:

Sad

Stressed

Anxious

Neutral

✔ High-Risk Message Detection

Catches dangerous patterns such as:

“I want to die”

“No reason to live”

“Kill myself”

If triggered → sends a safety response.

✔ Mini RAG Pipeline (Retrieval-Augmented Generation)

Retrieves helpful tips based on the detected emotion from a small knowledge base.

✔ Empathetic AI Responses

Generates friendly suggestions using safe, supportive templates.

✔ ChatGPT-style CLI Experience

User can chat naturally inside a terminal.

🔧 Tech Stack

Python 3

Regex (re)

Basic NLP (keyword-based)

Mini RAG Knowledge Base (dictionary-based)

Console interface

No external ML model or API needed.

📁 Project Structure
mental-health-chatbot/
│
├── mental_health_chatbot.py     # Main chatbot code
├── README.md                    # Project documentation
├── LICENSE                      # MIT License
└── .gitignore                   # Ignored files

▶️ How to Run

Clone the repository:

git clone https://github.com/YOUR-USERNAME/mental-health-chatbot
cd mental-health-chatbot


Run the chatbot:

python mental_health_chatbot.py


Start chatting!
Type exit anytime to quit.

💬 Sample Interaction
You: I feel stressed about exams.

AI:
It sounds like you're feeling quite stressed. 😥

Here are a few gentle suggestions:
• Break your work into smaller tasks
• Take short breaks and drink water
• Start with the easiest task first

Remember, I’m just an AI assistant, not a professional.

🗂 Future Enhancements

Replace rule-based classifier with ML/NLP model

Add Streamlit web UI

Integrate real LLM API for richer responses

Add multilingual support

Expand knowledge base

📜 License

This project is licensed under the MIT License.
You are free to use, modify, and distribute the code.

🌟 Author

Sahitya Movva
B.Tech – Computer Science & Engineering
2026 Batch
India

🖤 If you like this project

⭐ Star the repo on GitHub
and
🤍 share it in your resume or LinkedIn
