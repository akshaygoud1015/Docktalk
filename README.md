# DocTalk

DocTalk is a Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions about their content. The application leverages AI-powered semantic search and text generation to provide accurate, context-aware answers.

## Features

- **PDF Support**: Upload and process PDF documents
- **Semantic Search**: Find relevant content from documents using embeddings
- **AI-Powered Responses**: Generate natural language answers using Google's Generative AI
- **Vector Database**: Efficient document storage and retrieval using ChromaDB
- **User-Friendly Interface**: Built with Streamlit for easy interaction

## Project Structure

```
docTalk/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── rag/                  # RAG module (core functionality)
    ├── __init__.py
    ├── loader.py         # PDF text extraction
    ├── chunker.py        # Text chunking for processing
    ├── embeddings.py     # Embedding generation
    ├── retriever.py      # Vector database operations
    └── generator.py      # AI response generation
```

## Installation

1. **Clone or navigate to the project directory**
   ```
   cd docTalk
   ```

2. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory and add your Google API credentials:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## Usage

1. **Run the application**
   ```
   streamlit run app.py
   ```

2. **Upload a PDF**
   - Click "Upload PDF" and select a PDF file from your computer
   - The application will process the document and display a success message

3. **Ask Questions**
   - Enter your question in the text input field
   - The system will search the document and generate an answer using AI

## Dependencies

- **streamlit**: Web framework for building the UI
- **pypdf**: PDF text extraction
- **chromadb**: Vector database for semantic search
- **google-genai**: Google's generative AI models
- **google-generativeai**: Alternative Google AI library
- **python-dotenv**: Environment variable management
- **requests**: HTTP library for API calls

## How It Works

1. **Document Loading**: PDFs are uploaded and text is extracted using PyPDF
2. **Text Chunking**: Extracted text is split into manageable chunks with overlap
3. **Embedding**: Chunks are converted to vector embeddings for semantic search
4. **Storage**: Embeddings are stored in ChromaDB for efficient retrieval
5. **Query & Retrieval**: User queries are embedded and matched against stored chunks
6. **Generation**: Retrieved context is sent to Google's Generative AI for answer generation

## Configuration

- **Chunk Size**: Default 500 characters (configurable in `chunker.py`)
- **Chunk Overlap**: Default 100 characters to maintain context
- **Retrieval k**: Top 5 most relevant chunks retrieved by default

## Requirements

- Python 3.8 or higher
- Google API key for generative AI access
- Internet connection for API calls

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve the application.
