from langchain_community.document_loaders import WebBaseLoader

url = 'https://alaqsa.com.pk/product/lenovo-thinkpad-t560-core-i5-6th-gen/'
loader = WebBaseLoader(url)

docs = loader.load()

print(docs)

print(docs[0].page_content)