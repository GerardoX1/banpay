from langchain.chains import RetrievalQAWithSourcesChain
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI

llm_default = ChatOpenAI(model_name="gpt-4o", temperature=0.1)


class ChatbotQA:
    def __init__(
        self,
        chroma_vectorstore: Chroma,
        llm: ChatOpenAI = llm_default,
    ):
        self._chroma_vectorstore = chroma_vectorstore
        self._llm = llm

    def qa_chain(self):
        self.qa_chain = RetrievalQAWithSourcesChain.from_chain_type(
            llm=self._llm,
            retriever=self._chroma_vectorstore.as_retriever(search_kwargs={"k": 3}),
            chain_type="stuff",
        )

    def response_qa_chain(self, question_text):
        return self.qa_chain({"question": question_text})
