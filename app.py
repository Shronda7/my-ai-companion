import streamlit as st
import google.generativeai as genai

# 1. Configuration
st.set_page_config(page_title="My AI Companion", page_icon="🤖")
st.title("🤖 Your Personal AI Assistant")
st.caption("Here to help with work, home, and life.")

# 2. Sidebar for API Key (Secure)
with st.sidebar:
    api_key = st.text_input("AQ.
    st.markdown("Get your key [here](https://google.com)")

# 3. Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 5. Handle User Input
if prompt := st.chat_input("What can I help you with today?"):
    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Generate Response
    if api_key:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-1.5-flash") # The free, fast model
            
            # Create a simple chat session with history
            chat = model.start_chat(history=[
                {"role": m["role"], "parts": [m["content"]]} 
                for m in st.session_state.messages if m["role"] != "system"
            ])
            
            response = chat.send_message(prompt)
            
            with st.chat_message("assistant"):
                st.write(response.text)
            
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter your API Key in the sidebar to start chatting!")
