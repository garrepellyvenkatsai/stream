import streamlit as st
import base64

# Function to load and encode the logo
def load_logo(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your logo
logo_path = "logo.png"
logo_base64 = load_logo(logo_path)

# Bootstrap CSS
bootstrap_css = """
<link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
"""

# Custom CSS for the navbar
custom_css = f"""
<style>
    .navbar {{
        background-color: red;
        display: flex;
        align-items: center;
        height: 60px; /* Adjust the height to match the logo height */
        
    }}
    .navbar .navbar-brand img {{
        max-height: 40px;
        margin-right: 10px;
    }}
    .navbar .navbar-title {{
        flex-grow: 1;
        text-align: center;
        white-space: nowrap; /* Prevents title from breaking into multiple lines */
    }}
    .navbar .navbar-subheader {{
        margin-left: auto;
        margin-top:20px;
        white-space: nowrap; /* Prevents subheader from breaking into multiple lines */
    }}
    @media (max-width: 768px) {{
        .navbar {{
            flex-wrap: nowrap; /* Prevents wrapping of navbar items */
        }}
        .navbar .navbar-brand,
        .navbar .navbar-title,
        .navbar .navbar-subheader {{
            flex-shrink: 0;
        }}
    }}
</style>
"""

# Navbar HTML
navbar_html = f"""
<nav class="navbar navbar-expand-lg navbar-light">
    <div class="navbar-brand"><img src="data:image/png;base64,{logo_base64}"></div>
    <div class="navbar-title"><h1>Chat with Doc</h1></div>
    <div class="navbar-subheader">Subheader</div>
</nav>
"""

# Streamlit application
def main():
    st.set_page_config(layout="wide")
    st.markdown(bootstrap_css, unsafe_allow_html=True)
    st.markdown(custom_css, unsafe_allow_html=True)
    st.markdown(navbar_html, unsafe_allow_html=True)

    # Your main application content
    st.title("Welcome to My Streamlit App")
    st.write("This is the main content of the app.")

if __name__ == "__main__":
    main()




autoscroll_script = """
        <script>
            var chatContainer = window.parent.document.getElementById('chat-container');
            if (chatContainer) {
                chatContainer.scrollTop = chatContainer.scrollHeight;
            }
        </script>
        """
        st.markdown(autoscroll_script, unsafe_allow_html=True)


def display_conversation(history):
    container = '<div class="chat-container">'
    
    
    # Add chat messages to the container
    for i in range(len(history["generated2"])):
        
        container += f'<div class="chat-message user-message">{history["past2"][i]}</div>'
        container += f'<div class="chat-message assistant-message">{history["generated2"][i]}</div>'
    
    # Close the chat container div
    container += '</div>'
    
    # Display the entire container with the messages
    st.markdown(container, unsafe_allow_html=True)

autoscroll_script = """
        <script>
            var chatContainer = window.parent.document.getElementById('chat-container');
            if (chatContainer) {
                chatContainer.scrollTop = chatContainer.scrollHeight;
            }
        </script>
        """
st.markdown(autoscroll_script, unsafe_allow_html=True)
