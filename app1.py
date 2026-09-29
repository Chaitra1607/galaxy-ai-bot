import streamlit as st
import ollama

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@400;500;600;700;800&display=swap');

.stApp {
    background: radial-gradient(circle at top, #1b1745 0%, #09071a 45%, #03030b 100%);
    color: #f5f3ff;
}

/* Main title */
h1 {
    text-align: center;
    color: #e8ddff;
    font-size: 52px;
    font-weight: 800;
    font-family: 'Baloo 2', 'Trebuchet MS', cursive;
    letter-spacing: 1px;
    text-shadow: 0 0 10px #9d7cff, 0 0 25px #6c4cff;
    margin-bottom: 30px;
}

/* Chat messages */
[data-testid="stChatMessage"] {
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(180, 150, 255, 0.25);
    border-radius: 18px;
    padding: 12px 18px;
    margin-bottom: 12px;
    box-shadow: 0 0 15px rgba(100, 70, 200, 0.15);
    backdrop-filter: blur(10px);
}

/* Chat input box */
[data-testid="stChatInput"] {
    border-radius: 20px;
}

/* Input styling */
[data-testid="stChatInput"] textarea {
    background: rgba(20, 15, 45, 0.9);
    color: white;
    border: 1px solid #8066d9;
    border-radius: 18px;
}

/* Input glow when clicked */
[data-testid="stChatInput"] textarea:focus {
    border: 1px solid #b59cff;
    box-shadow: 0 0 15px rgba(150, 120, 255, 0.5);
}

/* Sidebar if you add one later */
section[data-testid="stSidebar"] {
    background: #080617;
}

/* Make normal text softer */
p {
    color: #ddd7f5;
}

</style>
""", unsafe_allow_html=True)


st.title(" Galaxy")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Ask me anything... ✨")

if user_input:

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    response = ollama.chat(
        model="llama3.2",
        messages=st.session_state.messages
    )

    bot_response = response["message"]["content"]

    st.session_state.messages.append(
        {"role": "assistant", "content": bot_response}
    )

    with st.chat_message("assistant"):
        st.markdown(bot_response)