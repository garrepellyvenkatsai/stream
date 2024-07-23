import streamlit as st
import streamlit.components.v1 as components

# HTML code for the Bootstrap header with image and title
header_html = """
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">

<style>
  .navbar {
    background-color:#551E6F;
   height:100px;
    color: white;
    border-radius:20px;
  }
  .navbar-brand {
    color: white;
  }
  .navbar-brand:hover {
    color: #d4d4d4;
    
  }
  .title
  {
  align:center;
  margin-bottom:10px;
  margin-left:300px;
  margin-bottom:10px;
  font-size:25px;
  font-weight:bold;
  }
  .a
  {
  margin-left:300px;
  margin-top:20px;
  }
  
</style>

<nav class="navbar navbar-expand-lg navbar-light">
 
    <img src="data:image/jpeg;base64,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"  width="90" class="d-inline-block align-top" alt="">
    <div class="title">IPF Chat Assistant</div>
    <div class="a" >-powered by payments technology</div>
  
</nav>
"""

# HTML and CSS code for the Bootstrap accordion with custom styles and icons
accordion_html = """
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">

<style>
  .card-header {
    cursor: pointer;
   
    
  }
  .card-header .btn {
    width: 100%;
    text-align: left;
  }
  .card-header .btn .fas {
    float: right;
  }
  .accordion .button:hover
  {
 
  text-decoration:none;
  }
  .card-body
  {
  border-bottom:1px solid black;
  border-left:1px solid black;
  border-right:1px solid black;
  border-top:none;
  }

.btn
{
color:red;
 text-decoration: none;}


.accordion .btn:hover {
    text-decoration: none;
}
.card
{
 text-decoration: none;
 border-radius:10px;
 }
.card-header{
height:80px;
border:1px solid black;
border-bottom:2px solid black;
 text-decoration: none;
 }
 .mb-0
 {
  text-decoration: none;}

</style>

<div class="accordion" id="accordionExample">

  <div class="card">
    <div class="card-header" id="headingThree">
      <h2 class="mb-0">
        <button class="btn btn-link collapsed" type="button" data-toggle="collapse" data-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
          Accordion Item #3 <i class="fas fa-chevron-down"></i>
        </button>
      </h2>
    </div>
    <div id="collapseThree" class="collapse" aria-labelledby="headingThree" data-parent="#accordionExample">
      <div class="card-body">
        Content for the third accordion item goes here.
           Content for the third accordion item goes here.
              Content for the third accordion item goes here.
                 Content for the third accordion item goes here.
                    Content for the third accordion item goes here.
                       Content for the third accordion item goes here.
                          Content for the third accordion item goes here.
      </div>
    </div>
  </div>
</div>

<script>
  $('#accordionExample .collapse').on('shown.bs.collapse', function () {
    $(this).parent().find(".fas").removeClass("fa-chevron-down").addClass("fa-chevron-up");
  }).on('hidden.bs.collapse', function () {
    $(this).parent().find(".fas").removeClass("fa-chevron-up").addClass("fa-chevron-down");
  });
</script>
"""

st.set_page_config(page_title="Streamlit App with Bootstrap", layout="wide")

# Display the header
components.html(header_html, height=80)

# Display the accordion

components.html(accordion_html, height=200)




import streamlit as st
import random
from datetime import datetime

# Define Bootstrap CSS link
bootstrap_css = """
<link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
"""

# Inject Bootstrap CSS into the Streamlit app
st.markdown(bootstrap_css, unsafe_allow_html=True)

# Define custom CSS for the chat container and chat input
custom_css = """
<style>
/* Chat container */
.chat-container {
    width: 100%;
    max-width: 1800px;
   
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 10px;
    background-color: #f9f9f9;
    height: 500px;
    overflow-y: auto;
    margin-bottom: 20px;
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
    width:1800px;
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
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Inject JavaScript to handle "Enter" key behavior in the chat input


# Function to display messages
def display_messages(messages):
    chat_html = '<div class="chat-container">'
    for message in messages:
        timestamp = f'<div class="timestamp">{message["timestamp"].strftime("%Y-%m-%d %H:%M:%S")}</div>'
        if message["role"] == "user":
            chat_html += f'<div class="user-message"><div class="msg">{message["content"]}</div>{timestamp}</div>'
        else:
            chat_html += f'<div class="bot-message"><div class="msg">{message["content"]}</div>{timestamp}</div>'
    chat_html += '</div>'
    st.markdown(chat_html, unsafe_allow_html=True)

# Placeholder for chat messages
if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "bot", "content": "Hello! How can I help you today?", "timestamp": datetime.now()},
        {"role": "user", "content": "Can you tell me a joke?", "timestamp": datetime.now()},
        {"role": "bot", "content": "Sure! Why don't scientists trust atoms? Because they make up everything!", "timestamp": datetime.now()},
    ]

# Display initial messages
display_messages(st.session_state['messages'])

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

# Chat input field and send button using st.chat_input
st.markdown("""
            <style>
.stChatInput{
border-radius: 50px; !important;
border: 2px solid red; !important;

            width:1325px;

}
.stChatInput > input{
border-radius: 50px; !important;
border: 2px solid red !important;
background: red; !important;
}
div[data-testid=“stChatInput”] {
border-radius: 50px; !important;
border: 20px solid red; !important;
background: #000080; !important;
}
            </style>
""",unsafe_allow_html=True)
with st.container():
    user_input = st.chat_input("Your message")
    if user_input:
        # Display user message
        st.session_state['messages'].append({"role": "user", "content": user_input, "timestamp": datetime.now()})

        # Bot response
        bot_response = get_bot_response(user_input)
        st.session_state['messages'].append({"role": "bot", "content": bot_response, "timestamp": datetime.now()})
        
        # Rerun the script to update the chat
        st.rerun()




def display_conversation(history):
    container = '<div id="messages" class="chat-container" >'
    
    
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

    st.markdown(autoscroll_script, unsafe_allow_html=True)
    


st.markdown(
    """
    
    <style>
    /* CSS for chat_input container inbuilt streamlit widget classes*/
    .st-emotion-cache-1ch8vux:hover {
    background-color:#99c9ff;
    border: 1px solid black;
    color: rgb(255, 255, 255);
    
    }
    
    .st-emotion-cache-klqnuk { /* RUNNING TEXT*/
        font-size: 14px;
        color: rgb(163, 168, 184);
        text-transform: uppercase;
        margin-top: 1000px; 
        margin-right: 550px;
        white-space: nowrap;
        max-width: 20rem;
        transition: opacity 200ms ease-out 0s, clip 200ms ease-out 0s, min-width 200ms ease-out 0s, max-width 200ms ease-out 0s, padding 200ms ease-out 0s;
    }
    .st-emotion-cache-1j15ncu { /* RUNNING ICON*/
        opacity: 0.4;
        width: 1.6rem;
        height: 1.6rem;
        margin-right: -0.5rem;
        margin-top: 1000px; 
        #margin-right: 102px;
    }
   
    .st-cy {
        border-left-color: black;
    }
    .st-cz {
        border-right-color: black;
    }
    .st-d0 {
        border-top-color: black;
    }
    .st-d1 {
        border-bottom-color: black;
    }
    .st-bn {
        background-color: #F9F9F9;
    }
    .st-emotion-cache-1ch8vux {
    border: none;
    background-color: black;
    border-top-right-radius: 0.5rem;
    border-top-left-radius: 0px;
    border-bottom-right-radius: 0.5rem;
    display: inline-flex;
    -webkit-box-align: center;
    align-items: center;
    -webkit-box-pack: center;
    justify-content: center;
    line-height: 1;
    margin: 0px;
    padding: 0.5rem;
    color: #e6feff;
    pointer-events: auto;

    }

    </style>
    """,
    unsafe_allow_html=True
)

def save_uploadedfile(uploadedfile):
    with open(os.path.join(r"X:\Technology\CoPilot\chatWithDocUserFiles",uploadedfile.name),"wb") as f:
        f.write(uploadedfile.getbuffer())
   
    success_message = st.success("Saved file!")
    time.sleep(2)  
    success_message.empty()
    

@st.cache_resource
def declare():
    if "globalFiles" not in st.session_state:
        st.session_state.globalFiles= {}
    return st.session_state.globalFiles

# this is for sessioned(private files)
if "files_dic" not in st.session_state:
    st.session_state.files_dic= {}

# this is for docVisiblity
# values: local, global
if "docVisibility" not in st.session_state:
    st.session_state.docVisibility= ""

# original input container function here->
def chatInterface(qa):

    input_container = st.container()
    with input_container:
        
        user_input = st.chat_input(placeholder="Enter your prompt here")
        
    # print("user_input: " + user_input)
    input_container.float("bottom: 0.5px;")
    # input_container.markdown("""<style> padding-top: 50px; </style>""", unsafe_allow_html=True)

    # to maintain the chat history
    chat_history = []

    # Initialize session state for generated2 responses and past2 messages
    if "past2" not in st.session_state:
        st.session_state["past2"] = ["Hey there!"]
        
    if "generated2" not in st.session_state:
        print("generated2 not in session state")
        st.session_state["generated2"] = ["Ask away any questions you have about the Document. "] #Below is a summary of your file to get you started.
        summary = qa({"query": "Say 'Here is a summary of your document' and then summarise in a short paragraph and give 3-5 salient points", "chat_history": chat_history})
        # chat_history.append(("", summary['result']))       
        summary_response = str(summary["result"])
        st.session_state.past2.append("Let's start with the summary")
        st.session_state.generated2.append(summary_response)
    
    


    
        
    # Search the database for a response based on user input and update session state
    if user_input:
       
        # output = qa({"question": user_input, "chat_history": chat_history})
        output = qa({"query": user_input, "chat_history": chat_history})
        # update chat history by adding this query and answer
        chat_history.append((user_input, output['result']))        
        
        #adding the current query and response to appropriate lists
        st.session_state.past2.append(user_input)

        # Display messages with loader
        
        response = str(output["result"])
        # response = str(output["answer"])
        st.session_state.generated2.append(response)
    
    
 
        

    # Display conversation history using Streamlit messages
    if st.session_state["generated2"]:
        display_conversation(st.session_state)
