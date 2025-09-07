from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model= 'gemini-1.5-pro')

result = model.invoke("What is the captial city of divison Gujrat Pakistan")

print(result)