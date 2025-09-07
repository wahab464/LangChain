from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import Annotated, TypedDict, Optional,Literal
from pydantic import BaseModel,Field

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini')

class Review(BaseModel):

    key_themes: list[str] = Field(description="Write down all the key themes discussed in the review in a list")
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal["pos", "neg"] = Field(description="Return sentiment of the review either negative, positive or neutral")
    pros: Optional[list[str]] = Field(default=None, description="Write down all the pros inside a list")
    cons: Optional[list[str]] = Field(default=None, description="Write down all the cons inside a list")
    name: Optional[str] = Field(default=None, description="Write the name of the reviewer")

structured_model = model.with_structured_output(Review)


result = structured_model.invoke("Looks good, the package is also good but the backup time is not more than 120 or 150 minutes, after using it for 75 minutes, 60 percent battery is left. ")

print (result)