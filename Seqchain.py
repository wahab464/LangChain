from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template= 'generate 5 interesting lines about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='generate a 5 line summary from following text \n {text}',
    input_variables= ['text']
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic':'Unemployment in pakistan'})

print(result)

chain.get_graph().print_ascii()
