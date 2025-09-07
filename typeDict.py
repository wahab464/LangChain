from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import Annotated, TypedDict, Optional

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini')

class Review(TypedDict):

    key_themes: Annotated[list[str], "Write down all key themes in review"]
    summary: Annotated[str, "A brief summary reivew"]
    sentiment: Annotated[str, "Give Sentiment in positive, negtive and netural"]
    pros: Annotated[Optional[list[str]],"write down all pros "]
    cons: Annotated[Optional[list[str]],"write down all cons "]

structured_model = model.with_structured_output(Review)


result = structured_model.invoke("Looks good, the package is also good but the backup time is not more than 120 or 150 minutes, after using it for 75 minutes, 60 percent battery is left. ")

print (result)
print (result['summary'])
print (result['sentiment'])