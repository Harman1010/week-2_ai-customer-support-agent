from core.template import prompt

from core.config import llm

from pathlib import Path

from langchain_core.output_parsers import StrOutputParser

FAQ_PATH = Path("ShopZone.md")

parser = StrOutputParser()

chain = prompt | llm | parser

def load_faq()->str:

    return FAQ_PATH.read_text(encoding="utf-8")

def get_answer(query:str)->str:

    faq = load_faq()

    response = chain.invoke(
        {
            "faq" : faq,
            "query" : query
        }
    )
    
    return response