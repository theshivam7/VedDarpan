# VedDarpan: An Open-Source Chatbot

VedDarpan is an open-source chatbot designed to provide the latest online results using advanced AI models. Built with Streamlit and Langchain, VedDarpan leverages the power of the Llama-3-Sonar-Large-32k-Chat model and Perplexity integration with OpenAI. The chatbot is available for public use free of cost.

You can try VedDarpan here: [VedDarpan Chatbot](https://veddarpan.streamlit.app/)

## Features

- **Latest Online Results**: Provides up-to-date information by integrating with Perplexity and OpenAI.
- **User-Friendly Interface**: Built with Streamlit for a simple and intuitive user experience.
- **Advanced AI Models**: Utilizes the Llama-3-Sonar-Large-32k-Chat model for accurate and relevant responses.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.7 or higher
- `pip` (Python package installer)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/VedDarpan.git
    cd VedDarpan
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:

    Create a `.env` file in the project directory and add your OpenAI API key and Langchain API key:

    ```env
    OPENAI_API_KEY=your_openai_api_key
    LANGCHAIN_API_KEY=your_langchain_api_key
    ```

### Running the App

To start the Streamlit app, run:

```bash
streamlit run app.py 
```
## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [Langchain](https://www.langchain.com/)
- Uses models from [OpenAI](https://www.openai.com/) and [Perplexity](https://www.perplexity.ai/)

## Author

Made by [Shivam Sharma](https://www.linkedin.com/in/theshivam7/)


## Contributors

Contributors are welcome to contribute to this chatbot. Please feel free to submit pull requests or open issues.
