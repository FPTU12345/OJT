# Document loading
from langchain.document_loaders import YoutubeLoader
# Splitting
from langchain.text_splitter import RecursiveCharacterTextSplitter
# Storage and Retrieval
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
# Output
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

class Youtube_vector_store:
  def __init__(self, url):
    self.url = url
    self.transcript, self.docs, self.db = self.create_vector_db()
  
  def create_vector_db(self):
    # Document loading
    loader = YoutubeLoader.from_youtube_url(self.url)
    transcript = loader.load()

    # Splitting
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000,
                                                   chunk_overlap = 100)
    docs = text_splitter.split_documents(transcript)

    # Storage
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(docs, embeddings)
    return transcript, docs, db
  
  def ask(self, query = ' ', k = 10):
    # Retrieval
    docs = self.db.similarity_search(query, k)
    docs_page_content = " ".join([d.page_content for d in docs])

    # Output
    llm = OpenAI()
    prompt = PromptTemplate(
        input_variables = ['docs', 'question'],
        template = """
        You are a helpful assistant that that can answer questions about youtube videos
        based on the video's transcript.

        Answer the following question: {question}
        By searching the following video transcript: {docs}

        Only use the factual information from the transcript to answer the question.

        If you feel like you don't have enough information to answer the question, say "I don't know".

        Your answers should be verbose and detailed.
        """
    )
    chain = LLMChain(llm = llm,
                     prompt = prompt)
    response = chain.run(question = query,
                         docs = docs)
    response = response.replace("\n", "")
    return response, docs
