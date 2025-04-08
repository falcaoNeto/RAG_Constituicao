from dataclasses import dataclass
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
load_dotenv()
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

OPENAI_KEY = os.getenv("OPENAI_KEY")

GOOGLE_KEY = os.getenv("GOOGLE_KEY")

@dataclass
class BotAI:
    collection_name: str = "constituicao"
    llm = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_KEY)
    
    vectorStore = Chroma(
    embedding_function=OpenAIEmbeddings(model="text-embedding-3-small", api_key=OPENAI_KEY),
    persist_directory="EmbConstituicao/arquivos/dados",
    collection_name="constituicao",

)
    prompt: str  =  """
        Você é um assistente jurídico especializado. Com base nos documentos fornecidos, responda a seguinte pergunta de forma objetiva.

        Pergunta: {pergunta_do_usuário}

        Documentos: {trechos_recuperados}

        Sempre tente respoder com as informações fornecidas e não faça perguntas que não estejam relacionadas ao contexto.
        NUNCA informe que esta faltando informação que não esteja no contexto.
        Nunca diga que esta se baseando em documentos
        """

    def assistente_RAG(self, question):
        numRetrival = 3

        result = self.vectorStore.similarity_search(question, k=numRetrival)
        
        textRetrival = [result.page_content for result in result]

       

        prompt_template = PromptTemplate(
            input_variables=["pergunta_do_usuário", "trechos_recuperados"],
            template=self.prompt
        )

        chain = prompt_template | self.llm

        respostaFinal = chain.invoke({"pergunta_do_usuário": question, "trechos_recuperados": textRetrival})

        return respostaFinal.content

if __name__ == "__main__":
    bot = BotAI()
    print(bot.assistente_RAG("qual o artigo me garante o direito de ir e vir?"))

