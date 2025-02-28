## Chatbot-CDP

This project is a chatbot designed to answer questions related to **Customer Data Platforms (CDPs)**, including **Segment, mParticle, Lytics, and Zeotap**. The chatbot ensures relevance by filtering out unrelated queries and provides real-time streaming responses.

## Features

- **Handles CDP-related questions**: Answers queries about Segment, mParticle, Lytics, and Zeotap.
- **Real-time Streaming Responses**: Generates and displays responses dynamically as they are generated.
- **Question Relevance Filtering**: Filters out irrelevant questions (e.g., movies, sports, etc.).
- **Handles Long Questions**: Truncates extremely long questions (over 500 characters) and notifies the user.
- **Chat History Persistence**: Maintains a session-based conversation history.

## Tech Stack

- **Python**
- **Streamlit** (for UI)
- **LangChain OllamaLLM** (for LLM processing)
- **Sentence Transformers** (for relevance checking)

## Installation

### Prerequisites

Make sure you have Python 3.8+ installed.

### Setup Virtual Environment

```sh
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

### Install Dependencies

```sh
pip install streamlit langchain_ollama sentence-transformers
```

### Download and Setup Ollama

You need to install **Ollama** to run the LLM model.

1. Download Ollama from [ollama.ai](https://ollama.ai)
2. Install it following the instructions for your OS.
3. Open your terminal and run:
   ```sh
   ollama pull llama3.1
   ```
   This will download the necessary model for processing queries.

## How to Run

```sh
streamlit run main.py
```

## Usage

1. **Ask a question about CDPs** (e.g., *"How does mParticle handle identity resolution?"*)
2. If the question is **too long**, it will be truncated, and you will be notified.
3. If the question is **not related to CDPs**, the bot will reject it with an appropriate message.
4. If the question is valid, the assistant will generate and stream the response in real time.

## Example Interactions

### **Valid Question**

**User:** "How does Segment track user events?"

**Bot:** (Generates a detailed response dynamically)

### **Irrelevant Question**

**User:** "Which movie is releasing this week?"

**Bot:** "I can only answer questions related to Customer Data Platforms (Segment, mParticle, Lytics, Zeotap)."

## Future Enhancements

- Improve question filtering using advanced NLP techniques.
- Add multi-turn conversation support.
- Enhance UI with additional features (e.g., dropdowns for quick queries).

## License

This project is licensed under the **MIT License**.

## Author

Developed by **K.S. Appanna**

