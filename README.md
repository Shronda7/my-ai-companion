# 📘 User & Customization Manual: AI Companion

Thank you for deploying your Personal AI Companion! This guide covers operating instructions and custom optimization paths for daily life management.

## 🎯 How to Interact with Your Companion
Your companion understands cross-functional context natively. You don't need distinct rooms for work or home notes—simply voice your tasks organically:
* *"Draft an agenda for my 2 PM sync, remind me to defrost chicken at 5 PM, and write a quick evening text to my partner."*

## ✏️ How to Modify Your AI's Personality
If you want to alter how your AI companion sounds, acts, or thinks, you can tweak its core operational rules:

1. Open `app.py` inside GitHub.
2. Find the `system_instruction=` text boundary block.
3. Replace the text inside the parentheses with custom operational behaviors:
   * **Corporate Executive Filter:** *"Focus exclusively on spreadsheet outputs, markdown schedules, and professional language."*
   * **Family Household Focus:** *"Prioritize visual charts, kid-friendly meal options, and enthusiastic, supportive tones."*
4. Save (Commit) changes to update your app globally.

## 🛠️ Setup & Installation

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)

### Installation Steps

```bash
# Clone the repository
git clone https://github.com/Shronda7/my-ai-companion.git
cd my-ai-companion

# Install dependencies
pip install -r requirements.txt
```

### Environment Configuration

1. **Create a `.streamlit/secrets.toml` file** in the project root:

```toml
GEMINI_API_KEY = "your-api-key-here"
```

2. **Get your API key** from [Google AI Studio](https://makersuite.google.com/app/apikey)

## 🚀 Running the Application

### Streamlit Web App

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

### Standalone HTML Interface

Open `index.html` directly in your browser for a local-storage powered alternative.

## 📁 Project Structure

```
my-ai-companion/
├── app.py              # Streamlit web app entry point
├── index.html          # Standalone single-page app (browser-based)
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## ⚙️ Tech Stack

- **Backend**: Python 3.11+, Streamlit
- **AI**: Google Generative AI (Gemini)
- **Frontend**: Streamlit UI, HTML/CSS/JavaScript
- **Storage**: Session state (Streamlit) or localStorage (HTML)

## 🔒 Security Notes

- **Never hardcode API keys** directly in source files
- Python: Use `st.secrets["GEMINI_API_KEY"]` for secure key access
- JavaScript: Use `localStorage.getItem()` for client-side storage
- Keep `.streamlit/secrets.toml` in `.gitignore`

## 🤝 Contributing

Feel free to fork, modify, and improve this project. When contributing:

1. Keep security practices intact
2. Maintain beginner-friendly code with comments
3. Test thoroughly before submitting changes

## 📄 License

This project is open source. Feel free to use and modify as needed.

## 🆘 Troubleshooting

**Issue**: "API key not found"
- **Solution**: Ensure `GEMINI_API_KEY` is set in `.streamlit/secrets.toml`

**Issue**: Import errors
- **Solution**: Run `pip install -r requirements.txt` to install all dependencies

---

**Questions?** Open an issue on GitHub or check the inline code comments for implementation details.
