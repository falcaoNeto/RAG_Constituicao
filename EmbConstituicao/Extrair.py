from dataclasses import dataclass
from docling.document_converter  import DocumentConverter
from langchain.text_splitter import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv
load_dotenv()
import os
OPENAI_KEY = os.getenv("OPENAI_KEY")



@dataclass
class Extrair:
    pdf_path: str
    embed_model: str = "text-embedding-3-small"
    collection_name: str = "constituicao"

    def ExtrairMarkdown(self):
        converter = DocumentConverter()
        result = converter.convert(self.pdf_path)
        textoresult = result.document.export_to_markdown()
        return textoresult
    
    def SpliterMarkdown(self, conteudo_markdown):
        spplit = [
            ("##",  "Header")
        ]
        splitter = MarkdownHeaderTextSplitter(headers_to_split_on=spplit)
        textos = splitter.split_text(conteudo_markdown)

        dic_constituicao = []

        for texto in textos:
            dic = {"metadatos": texto.metadata, "conteudo":  texto.page_content, "length": len(texto.page_content)}
            dic_constituicao.append(dic)
        
        return dic_constituicao
    

    def Redivisao(self, dic_constituicao):

        final = []
        flag_pular = False
        

        for i, texto in enumerate(dic_constituicao):
            if i == len(dic_constituicao) - 1 and flag_pular:
                break

            if i == len(dic_constituicao) - 1:
                final.append(texto)
                break
                

            if flag_pular:
                flag_pular = False
                continue


            if texto["length"] > 500  and texto["length"] < 2000:
                final.append(texto)
                continue

            if texto["length"] > 2000:
                spliter = RecursiveCharacterTextSplitter(
                    chunk_size=1100,  
                    chunk_overlap=100,    
                    length_function=len,  
                    separators=[
                        "\n\n",  
                        "\n",    
                        ".",  
                        " ",
                        ""       
                    ],
                    keep_separator=True  # Mantém os separadores no texto
                )
                textos = spliter.split_text(texto["conteudo"])
                listaDic = []
                for textoSTR in textos:
                    listaDic.append({"metadatos": texto["metadatos"], "conteudo":  textoSTR, "length": len(textoSTR)})

                final.extend(listaDic)
            
            if len(texto["metadatos"]) == 0:
                continue

            if texto["length"] < 500:
                header = f"{texto['metadatos']["Header"]} - {dic_constituicao[i+1]['metadatos']["Header"]}"
                conteudo = f"{texto['conteudo']}\n\n{dic_constituicao[i+1]['conteudo']}"
                final.append({"metadatos": {"Header": header}, "conteudo": conteudo, "length": len(conteudo)})
                flag_pular = True

        return final
    
    def CriarChunks(self, dic_constituicao):
        textos = [t["conteudo"] for t in dic_constituicao]
    
        emb  = OpenAIEmbeddings(model="text-embedding-3-small", api_key=OPENAI_KEY)

        local  = "EmbConstituicao/arquivos/dados"

        store = Chroma.from_texts(persist_directory=local, embedding=emb ,texts=textos, collection_name="constituicao")
        
        num = store._collection.count()
        return num


    def main(self):
        
        textoDoc = self.ExtrairMarkdown()
        textosDoc = self.SpliterMarkdown(textoDoc)

        textos = self.Redivisao(textosDoc)
        textos2 = self.Redivisao(textos)

        num = self.CriarChunks(textos2)

        print(f"Número de documentos na coleção: {num}")


if __name__ == "__main__":
    pdf_path = "EmbConstituicao/dfd.pdf"
    extrair = Extrair(pdf_path)
    extrair.main()



