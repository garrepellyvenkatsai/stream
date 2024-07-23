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


def main():
    st.markdown(bootstrap_css, unsafe_allow_html=True)
    st.markdown(custom_css, unsafe_allow_html=True)
    st.markdown(navbar_html, unsafe_allow_html=True)
    st.session_state.globalFiles= declare()
    globalFiles_dic= st.session_state.globalFiles

    optionsSelectBox= []
    sessionOptions= st.session_state.files_dic.keys()
    globalOPtions= globalFiles_dic.keys()
    if len(sessionOptions)>0: optionsSelectBox.extend(sessionOptions)
    optionsSelectBox.extend(globalOPtions)
    

    # display files for download in the sidebar
    with st.sidebar:
        downloadOption = st.selectbox(
            "Select The Files Available Globally For Download",
            optionsSelectBox,
            index= None)

        # st.button("Download", on_click= downloadFiles, args= [downloadOptions])
        if downloadOption:
            with open(os.path.join(r"X:\Technology\CoPilot\chatWithDocUserFiles", downloadOption),"rb") as file:
                    btn = st.download_button(
                            label= downloadOption,
                            data= file,
                            file_name= downloadOption
                        )

    if 'is_expanded' not in st.session_state:
        st.session_state['is_expanded']=True
    with st.expander("Upload and Select Documents", expanded=st.session_state['is_expanded']):
        # optionsSelectBox = ["doc1", "doc2", "doc3"]  # Replace with your dynamic list of options

        options = st.multiselect(
            "Pick documents to chat with!",
            optionsSelectBox,
            default=None
        )


        uploaded_file = st.file_uploader(
            "Choose a file", 
            type=['txt', 'docx', 'pdf', 'html', 'xml', 'bpmn'], 
            key="uploader"
        )
        if uploaded_file is not None:
       
            col1, col2 = st.columns([2, 4])
        
            with col1:
                st.write("How would you like the visibility of the doc? 🚨")
        
            with col2:
                visOption = st.radio(
                "",
                ["Visible only to me", "Visible to others"],
                index=None,
                horizontal=True
            )
            st.session_state['is_expanded']=False
            
                
            try:
                if visOption:
                    if visOption== "Visible only to me": 
                        st.session_state.files_dic[st.session_state.uploader.name]= st.session_state.uploader.file_id
                    else:
                        st.session_state.globalFiles[st.session_state.uploader.name]= st.session_state.uploader.file_id
            except valueError:
                st.error('Please select the visibility of the doc above to proceed', icon="🚨")

            if visOption:
            
                base_dir= "X:\Technology\CoPilot\Embeddings\chatWithDoc"
                # base_dir=r"C:\Users\venkagv\Documents\chatwithdoc-main\chatBot\DBS"
                
                persist_dir= os.path.join(base_dir, st.session_state.uploader.file_id)

                
                if st.session_state.generateEmbs=='True':
                    texts = doc_preprocessing(uploaded_file)
                    generateEmbeddings(texts, persist_dir)
                    
                    st.session_state.generateEmbs= 'False'
                    # upload the file if a global file
                    if visOption!= "Visible only to me":
                        save_uploadedfile(uploaded_file)

        
        
    #view_doc = st.sidebar.checkbox("View Document")

    # state variable to capture file id, later used to delete the corresponding embeddings
    if "holdFileId" not in st.session_state:
        st.session_state.holdFileId= ""

    # state variable to decide to generate embeddigns or not
    if "generateEmbs" not in st.session_state:
        st.session_state.generateEmbs= 'True'

    def add_collection(_db_name):   #the var db_name is unhashable- so telling streamlit to not hash it by adding a '_' before the var name
        db_name_data=_db_name._collection.get(include=['documents','metadatas','embeddings'])
        db._collection.add(
            embeddings=db_name_data['embeddings'],
            metadatas=db_name_data['metadatas'],
            documents=db_name_data['documents'],
            ids=db_name_data['ids']
        )
        print('completed adding collection')

    # displaying the chat interface
    if (options or (uploaded_file and visOption)):
        if options:
            base_dir= "X:\Technology\CoPilot\Embeddings\chatWithDoc"
            first_option= options[0]
            if first_option in st.session_state.files_dic: persist_dir= os.path.join(base_dir, st.session_state.files_dic[first_option])
            else: persist_dir= os.path.join(base_dir, globalFiles_dic[first_option])
        
            db = Chroma(persist_directory=persist_dir, embedding_function=embeddings)
           
            for option in options[1:]:
                if option in st.session_state.files_dic: persist_dir= os.path.join(base_dir, st.session_state.files_dic[option])
                else: persist_dir= os.path.join(base_dir, globalFiles_dic[option])
          
                tmp_db= Chroma(persist_directory=persist_dir, embedding_function=embeddings)
                
                tmp_db_data= tmp_db._collection.get(include=['documents','metadatas','embeddings'])
                db._collection.add(
                    embeddings=tmp_db_data['embeddings'],
                    metadatas=tmp_db_data['metadatas'],
                    documents=tmp_db_data['documents'],
                    ids=tmp_db_data['ids']
                )
                print('Added collections for', option)

        else:
            db = Chroma(persist_directory=persist_dir, embedding_function=embeddings)
        qa = search_pdf(db, secret1)

        

        col1, col2 = st.columns([5, 1])
        view_doc=True

        with col1:
            if options:
                option_names = ', '.join(options)
                st.write("You are chatting with " + option_names)
            else:
                st.write("You are chatting with " + st.session_state.uploader.name)

        tab1,tab2=st.tabs(['Chat','Document'])
        with tab1:
            chatInterface(qa)
            if st.button("Reset Chat"):
                    st.session_state.past2 = ["Hey there!"]
                    st.session_state.generated2 = ["Ask away any questions you have about the Document."]
                    st.session_state.chat_history = []
   
        with tab2:
            

            if  uploaded_file is not None:
                f_name = uploaded_file.name
                file_extension = os.path.splitext(f_name)[1].lower()
                
                with open(f_name, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                if file_extension == ".pdf":
                    show_pdf(f_name)
                elif file_extension == ".docx":
                    show_docx(f_name)
                elif file_extension == ".txt":
                    show_txt(f_name)
                elif file_extension == ".xml":
                    show_xml(f_name)
                elif file_extension == ".html":
                    show_html(f_name)
                elif file_extension == ".bpmn":
                    show_bpmn(f_name)
                st.sidebar.success(f"File uploaded: {f_name}")
                
if __name__ == "__main__":
    main()
