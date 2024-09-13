import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")

# Langchain tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Header with Tabs
st.set_page_config(page_title="VedDarpan Chatbot", page_icon="💬")
st.title('VedDarpan Chatbot 💬')
tabs = st.tabs(["🏠 Home", "ℹ️ About VedDarpan", "📬 Contact ME"])

with tabs[0]:
    st.header("Welcome to VedDarpan Chatbot")

    # Custom CSS for better UI and moving text
    st.markdown("""
    <style>
    .moving-text {
        white-space: nowrap;
        overflow: hidden;
        position: relative;
        animation: moveText 20s linear infinite;
    }
    @keyframes moveText {
        0% { transform: translateX(100%); }
        100% { transform: translateX(-100%); }
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: rgba(0, 0, 0, 0);
        color: white;
        text-align: center;
        padding: 10px 0;
        z-index: 999;
    }
    </style>
    <div class="moving-text">Search any topic and get quick responses!</div>
    """, unsafe_allow_html=True)

    # Initialize session state
    if 'conversation' not in st.session_state:
        st.session_state['conversation'] = None
    if 'messages' not in st.session_state:
        st.session_state['messages'] = []

    # Function for generating LLM response
    def generate_response(prompt):
        if st.session_state['conversation'] is None:
            llm = ChatOpenAI(model="llama-3.1-70b-instruct", base_url="https://api.perplexity.ai", api_key=OPENAI_API_KEY)
            memory = ConversationBufferMemory(return_messages=True)
            st.session_state['conversation'] = ConversationChain(
                llm=llm,
                memory=memory,
                prompt=PromptTemplate(
                    input_variables=["history", "input"],
                    template="Current conversation:\n{history}\nHuman: {input}\nAI: "
                ),
            )
        response = st.session_state['conversation'].predict(input=prompt)
        return response

    # Display chat messages from history
    for message in st.session_state['messages']:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Create a placeholder for the response
    response_placeholder = st.empty()

    # Add the small text above the chatbox
    st.markdown("🔎 Search the topic you want:")

    # Accept user input
    prompt = st.chat_input("What is your question?")

    if prompt:
        # Add user message to chat history
        st.session_state['messages'].append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate response
        response = generate_response(prompt)
        # Add assistant response to chat history
        st.session_state['messages'].append({"role": "assistant", "content": response})
        # Display assistant response in chat message container
        with response_placeholder.chat_message("assistant"):
            st.markdown(response)

with tabs[1]:
    
    st.header("About VedDarpan 🤖")
    st.write("""
    **VedDarpan** is an open-source chatbot designed to provide the latest online results using advanced AI models. Built with Streamlit and Langchain, VedDarpan leverages the power of the **llama-3.1-sonar-large-128k-chat** model and Perplexity integration with OpenAI. The chatbot is available for public use free of cost.
    """)

with tabs[2]:
    st.header("Contact ME 📞")
    st.write("For any queries, feel free to reach out via [LinkedIn](https://www.linkedin.com/in/theshivam7/) or check out my [GitHub](https://github.com/theshivam7/) for cool projects.")
    st.write("I'm **Shivam Sharma**, an undergraduate student at IIT Madras. I'm a web developer, Android and iOS app developer, and I'm enthusiastic about AI and ML.")

# Footer
st.markdown(
    """
    <div class="footer">Made with ❤️ by Shivam 🍁</div>
    """,
    unsafe_allow_html=True
)