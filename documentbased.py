from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

text = """age = 20

if age >= 18:
    print("You are old enough to vote.")
else:
    print("You are not yet old enough to vote.")"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language= Language.PYTHON,
    chunk_size = 20,
    chunk_overlap = 0

)

chunk = splitter.split_text(text)

print(len(chunk))
print (chunk)

