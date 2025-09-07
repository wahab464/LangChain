from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """Linear regression is a statistical and machine learning method that models the relationship between a dependent variable and one or more independent variables by fitting a linear equation to observed data. It is used to predict the value of the dependent variable based on the independent variables by finding the "line of best fit" that minimizes the total error between the predicted and actual values. There are two main types: simple linear regression, with one independent variable, and multiple linear regression, with two or more."""

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 50,
    chunk_overlap = 5
)

chunks = splitter.split_text(text)

print(chunks)

print(len(chunks))

