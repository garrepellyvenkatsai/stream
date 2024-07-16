import streamlit as st
import random
from datetime import datetime
import time

# Define Bootstrap CSS link
bootstrap_css = """
<link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
"""
st.set_page_config(layout="wide")

# Inject Bootstrap CSS into the Streamlit app
st.markdown(bootstrap_css, unsafe_allow_html=True)

# Define custom CSS for the chat container, chat input, and loader
custom_css = """
<style>
/* Chat container */
.chat-container {
    width: 100%;
    max-width: 1200px;
    margin: auto;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 10px;
    background-color: #f9f9f9;
    height: 500px;
    overflow-y: auto;
    margin-bottom: 20px;
    position: relative;
}

/* User message */
.user-message {
    text-align: right;
    margin: 10px 0;
}

.user-message .msg {
    display: inline-block;
    background-color: #007bff;
    color: white;
    padding: 10px;
    border-radius: 10px;
    max-width: 60%;
}

.user-message .timestamp {
    font-size: 10px;
    color: #999;
    margin-top: 2px;
}

/* Bot message */
.bot-message {
    text-align: left;
    margin: 10px 0;
}

.bot-message .msg {
    display: inline-block;
    background-color: #e9ecef;
    color: black;
    padding: 10px;
    border-radius: 10px;
    max-width: 60%;
}

.bot-message .timestamp {
    font-size: 10px;
    color: #999;
    margin-top: 2px;
}

/* Custom CSS for the chat input */
.chat-input-container {
    display: flex;
    align-items: center;
}

.stTextArea {
    flex: 1;
    padding: 10px;
    font-size: 16px;
    border-radius: 10px;
    border: 1px solid #ccc;
    margin-right: 10px;
    overflow: hidden;
}

.send-button {
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}

.send-button:hover {
    background-color: #0056b3;
}

/* Loader */
.loader {
    border: 16px solid #f3f3f3; /* Light grey */
    border-top: 16px solid #3498db; /* Blue */
    border-radius: 50%;
    width: 120px;
    height: 120px;
    animation: spin 2s linear infinite;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    opacity: 0.5; /* Adjust the transparency */
}

@keyframes spin {
    0% { transform: translate(-50%, -50%) rotate(0deg); }
    100% { transform: translate(-50%, -50%) rotate(360deg); }
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Function to display messages
def display_messages(messages, show_loader=False):
    chat_html = '<div class="chat-container">'
    for message in messages:
        timestamp = f'<div class="timestamp">{message["timestamp"].strftime("%Y-%m-%d %H:%M:%S")}</div>'
        if message["role"] == "user":
            chat_html += f'<div class="user-message"><div class="msg">{message["content"]}</div>{timestamp}</div>'
        else:
            chat_html += f'<div class="bot-message"><div class="msg">{message["content"]}</div>{timestamp}</div>'
    if show_loader:
        chat_html += '<div class="loader"></div>'
    chat_html += '</div>'
    return chat_html

# Placeholder for chat messages
if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "bot", "content": "Hello! How can I help you today?", "timestamp": datetime.now()},
        {"role": "user", "content": "Can you tell me a joke?", "timestamp": datetime.now()},
        {"role": "bot", "content": "Sure! Why don't scientists trust atoms? Because they make up everything!", "timestamp": datetime.now()},
    ]

# Predefined intents and responses
intents = {
    "joke": "Why don't scientists trust atoms? Because they make up everything!",
    "hello": "Hello! How can I help you today?",
    "bye": "Goodbye! Have a great day!",
}

def get_bot_response(user_message):
    for key in intents.keys():
        if key in user_message.lower():
            return intents[key]
    return random.choice([
        "That's interesting!",
        "Can you tell me more?",
        "I see.",
        "Let's discuss further.",
    ])

# Chat container
chat_container = st.empty()

# Display initial messages without loader
chat_container.markdown(display_messages(st.session_state['messages']), unsafe_allow_html=True)

# Chat input field and send button using st.text_input and st.button
with st.container():
    user_input = st.text_input("Your message")
    if st.button("Send"):
        if user_input:
            # Display user message
            st.session_state['messages'].append({"role": "user", "content": user_input, "timestamp": datetime.now()})
            
            # Display messages with loader
            chat_container.markdown(display_messages(st.session_state['messages'], show_loader=True), unsafe_allow_html=True)
            
            # Simulate delay and get bot response
            time.sleep(2)  # Simulate a delay for fetching the response
            bot_response = get_bot_response(user_input)
            st.session_state['messages'].append({"role": "bot", "content": bot_response, "timestamp": datetime.now()})
            
            # Display messages without loader
            chat_container.markdown(display_messages(st.session_state['messages']), unsafe_allow_html=True)
