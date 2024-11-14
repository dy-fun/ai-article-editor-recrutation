from dotenv import load_dotenv
from openai import OpenAI
import tkinter as tk
import os
from tkinter import filedialog

def Configure():
    load_dotenv()
    return os.getenv("OPENAI_API_KEY")

def ReadFile():
    root = tk.Tk()
    root.withdraw()  
    filePath = filedialog.askopenfilename(title="Wybierz plik tekstowy", filetypes=[("Text files", "*.txt")])  
    
    if filePath: 
        with open(filePath, "r") as file:
            content = file.read()
        return content

def ConnectToAi(promptText, fileContent, apiKey):
    client = OpenAI(api_key=apiKey)
    
    gptModel="gpt-4" 
    messages=[
        {"role": "system", "content": "Jesteś asystentem, który pomaga konwertować tekst na HTML."},
        {"role": "user", "content": f"{promptText}\n\n{fileContent}"}
    ]
      
    response = client.chat.completions.create(
        model=gptModel,
        messages=messages,
        temperature=0,
        max_tokens=3000,  
    )
    response_message = response.choices[0].message.content
    return response_message

def CreateArticle(fileContent):
    with open("artykul.html", "w") as article:  
        article.write(fileContent) 

def Main():
    apiKey = Configure()
    fileContent = ReadFile()
    
    promptText = (
        "Przekształć poniższy artykuł na kod HTML, używając odpowiednich tagów. "
        "Kod ma zawierać wyłącznie część kodu znajdującą się między znacznikami <body>, bez znaczników <html>, <body>, <head>"
        "Dodaj tagi <h1>, <h2>, <p> do strukturyzacji treści. "
        "Tam, gdzie warto wstawić grafikę, dodaj tag <img src='image_placeholder.jpg' alt='[opis obrazu]'> "
        "oraz <figcaption> z krótkim opisem. Nie używaj CSS ani JavaScript."
    )
    
    htmlContent = ConnectToAi(promptText, fileContent, apiKey)
    CreateArticle(htmlContent)
    print("Artykuł zapisano jako artykul.html")

if __name__ == "__main__":
    Main()