import nest_asyncio
from llama_index.llms.openai import OpenAI
from llama_index.core import VectorStoreIndex
from llama_parse import LlamaParse
from llama_index.core.node_parser import MarkdownElementNodeParser

##https://github.com/tayaln/RAG-on-an-excel-sheet-using-GPT4-o-mini/blob/main/RAG_on_excel_using_GPT4_o.ipynb
##https://www.youtube.com/watch?v=eSH8UCmgosE