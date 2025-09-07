from langchain_huggingface import HuggingFacePipeline,ChatHuggingFace


llm = HuggingFacePipeline.from_model_id(
    model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
     task = "text generation",
     pipeline_kwargs=dict(
         temperature = 1,
         max_new_tokens = 100
     )
)

model = ChatHuggingFace(llm = llm )

result = model.invoke("Tell me about Gujrat city in punjab pakistan")

print(result)