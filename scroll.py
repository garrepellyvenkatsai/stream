import streamlit as st
from streamlit.components.v1 import html
import random
from datetime import datetime

# Define custom HTML, CSS, and JavaScript for the chat interface
custom_html = """
<style>
/* Chat container */
.chat-container {
    width: 100%;
    max-width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 10px;
    background-color: #f9f9f9;
    height: 500px;
    overflow-y: scroll; /* Ensure scrollbar always appears */
    position: relative;
    box-sizing: border-box; /* Include padding and border in the element's total width and height */
}

/* Custom scrollbar */
.chat-container::-webkit-scrollbar {
    width: 5px;
}

.chat-container::-webkit-scrollbar-thumb {
    background-color: #007bff;
    border-radius: 10px;
}

.chat-container::-webkit-scrollbar-track {
    background-color: #f1f1f1;
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

/* Scroll to bottom button */
.scroll-to-bottom {
    position: absolute;
    bottom: 10px; /* Distance from the bottom */
    right: 10px;  /* Distance from the right */
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px;
    cursor: pointer;
    font-size: 16px;
    z-index: 1000;
    display: none;
}

.scroll-to-bottom.show {
    display: block;
}
</style>

<div class="chat-container">
    <!-- Chat messages will be injected here -->
</div>
<button class="scroll-to-bottom">↓</button>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const chatContainer = document.querySelector('.chat-container');
    const scrollToBottomBtn = document.querySelector('.scroll-to-bottom');

    function scrollToBottom() {
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }

    function checkScroll() {
        if (chatContainer.scrollTop + chatContainer.clientHeight < chatContainer.scrollHeight - 20) {
            scrollToBottomBtn.classList.add('show');
        } else {
            scrollToBottomBtn.classList.remove('show');
        }
    }

    scrollToBottom();  // Scroll to bottom on load
    chatContainer.addEventListener('scroll', checkScroll);
    scrollToBottomBtn.addEventListener('click', scrollToBottom);
});
</script>
"""

# Initialize chat messages if not already present
if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "bot", "content": "Hello! How can I help you today?", "timestamp": datetime.now()},
        {"role": "user", "content": "Can you tell me a joke?", "timestamp": datetime.now()},
        {"role": "bot", "content": "Sure! Why don't scientists trust atoms? Because they make up everything!", "timestamp": datetime.now()},
    ]

# Generate HTML for chat messages
messages_html = ""
for message in st.session_state['messages']:
    timestamp = message["timestamp"].strftime("%Y-%m-%d %H:%M:%S")
    if message["role"] == "user":
        messages_html += f'<div class="user-message"><div class="msg">{message["content"]}</div><div class="timestamp">{timestamp}</div></div>'
    else:
        messages_html += f'<div class="bot-message"><div class="msg">{message["content"]}</div><div class="timestamp">{timestamp}</div></div>'

# Combine HTML content with messages
full_html = custom_html.replace('<!-- Chat messages will be injected here -->', messages_html)

# Display the HTML content
html(full_html, height=600)

# Function to generate bot response
def get_bot_response(user_message):
    intents = {
        "joke": "Why don't scientists trust atoms? Because they make up everything!",
        "hello": "Hello! How can I help you today?",
        "bye": "Goodbye! Have a great day!",
    }
    for key in intents.keys():
        if key in user_message.lower():
            return intents[key]
    return random.choice([
        "That's interesting!",
        "Can you tell me more?",
        "I see.",
        "Let's discuss further.",
    ])

# Chat input field and send button
user_input = st.chat_input("Your message")
if user_input:
    # Add user message to session state
    st.session_state['messages'].append({"role": "user", "content": user_input, "timestamp": datetime.now()})

    # Generate and add bot response
    bot_response = get_bot_response(user_input)
    st.session_state['messages'].append({"role": "bot", "content": bot_response, "timestamp": datetime.now()})
    
    # Trigger rerun to update the chat display
    st.experimental_rerun()
