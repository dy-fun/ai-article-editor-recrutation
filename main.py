from openai import OpenAI
from tkinter import filedialog
import tkinter as tk


def ReadFile():
    root = tk.Tk()
    root.withdraw()  
    filePath = filedialog.askopenfilename(title="Wybierz plik tekstowy", filetypes=[("Text files", "*.txt")])  
    
    if filePath: 
        with open(filePath, "r") as file:
            content = file.read()
        return CreateArticle(content)

    else:
        print("Nie wybrano pliku.")
        return None

def CreateArticle(fileContent):
    with open("artykul.html", "w") as article:  
        article.write(fileContent) 


ReadFile()
