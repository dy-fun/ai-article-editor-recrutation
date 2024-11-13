from openai import OpenAI

def ReadFile():
    with open("tresc.txt", "r") as file:  
        content = file.read() 
    return content  

def CreateArticle(fileContent):
    with open("artykul.html", "w") as article:  
        article.write(fileContent) 


fileContent = ReadFile()  
CreateArticle(fileContent)  