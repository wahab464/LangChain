from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model= 'gpt-4', temperature=0.5, max_completion_tokens=30)

result = model.invoke("Tell me about Gujrat city in punjab pakistan")

print(result.content)
