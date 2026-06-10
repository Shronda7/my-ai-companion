# 🤖 Coding Agent Guidelines & Repository Context

This file contains behavioral boundaries, design styles, and requirements for AI agents editing this codebase.

## 📋 Project Architecture
* `app.py`: Entry point for the Streamlit web app interface.
* `index.html`: Client-side single-page alternative using local storage memory configurations.
* No local servers or complex databases are allowed; state must stay inside `st.session_state` or browser `localStorage`.

## ⚙️ Dependencies & Environment
* Python 3.11+
* Packages: `streamlit`, `google-generativeai`

## 🔒 Security Constraints & Guardrails
* **CRITICAL:** Do NOT hardcode API keys or credentials directly into Python or Javascript strings.
* Python keys MUST pass securely via `st.secrets["GEMINI_API_KEY"]`.
* Javascript alternative keys MUST strictly pass via browser memory storage using `localStorage.getItem()`.

## 🎨 Style Preferences
* Keep code snippets accessible to non-technical individuals.
* Comment heavily inside logic blocks to explain *why* something works to a beginner.
