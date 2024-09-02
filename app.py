from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
LANGCHAIN_API_KEY = os.environ["LANGCHAIN_API_KEY"]

# Langchain tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Create the prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries."),
        ("user", "Question:{question}")
    ]
)

# Initialize conversation history
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []

# Streamlit framework
st.set_page_config(page_title="VedDarpan Chatbot", page_icon="🤖", layout="centered")

# Header with Tabs
st.title('VedDarpan Chatbot 💬')
tabs = st.tabs(["🏠 Home", "ℹ️ About VedDarpan", "📬 Contact ME"])

with tabs[0]:
    st.header("Welcome to VedDarpan Chatbot")
    st.write("**Search any topic and get quick responses!**")
    input_text = st.text_input("🔍 Search the topic you want:")

    # OpenAI LLM 
    llm = ChatOpenAI(model="llama-3.1-70b-instruct", base_url="https://api.perplexity.ai")
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

    if input_text:
        st.session_state.conversation_history.append(("user", input_text))
        with st.spinner('Generating response...'):
            response = chain.invoke({'question': input_text, 'history': st.session_state.conversation_history})
            st.session_state.conversation_history.append(("assistant", response))
            st.success("Here's the answer:")
            st.write(response)

        # Follow-up chat loop
        follow_up_text = st.text_area("💬 Ask a follow-up question:", key="initial_follow_up")
        while follow_up_text:
            st.session_state.conversation_history.append(("user", follow_up_text))
            with st.spinner('Generating follow-up response...'):
                follow_up_response = chain.invoke({'question': follow_up_text, 'history': st.session_state.conversation_history})
                st.session_state.conversation_history.append(("assistant", follow_up_response))
                st.success("Here's the follow-up answer:")
                st.write(follow_up_response)
                follow_up_text = st.text_area("💬 Ask another follow-up question:", key=f"follow_up_{follow_up_text}")

with tabs[1]:
    st.header("About VedDarpan 🤖")
    st.write("""
        **VedDarpan** is an open-source chatbot designed to provide the latest online results using advanced AI models. 
        Built with Streamlit and Langchain, VedDarpan leverages the power of the **llama-3.1-sonar-large-128k-chat** model 
        and Perplexity integration with OpenAI. The chatbot is available for public use free of cost.
    """)

with tabs[2]:
    st.header("Contact ME 📞")
    st.write("For any queries, feel free to reach out via [LinkedIn](https://www.linkedin.com/in/theshivam7/) or check out my [GitHub](https://github.com/theshivam7/) for cool projects.")
    st.write("I'm **Shivam Sharma**, an undergraduate student at IIT Madras. I'm a web developer, Android and iOS app developer, and I'm enthusiastic about AI and ML.")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: gray;">
        Made with ❤️ by <a href="https://www.linkedin.com/in/theshivam7/" target="_blank" style="color: #FF4B4B;">Shivam 🍁</a>
    </div>
    """, 
    unsafe_allow_html=True
)
