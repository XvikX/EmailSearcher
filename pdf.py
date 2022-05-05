import PyPDF2
import string
import re

FILE_PATH = "boarding_pass.pdf"

def extractFlightNum(text):
    textSplitted = text.split("\n")
    isfound = False
    for line in textSplitted:
        match = re.match(r"([a-z]{2})([0-9]{3})", line, re.I)
        if match:
            print("[+] - We find the following flight number :", line)
            isfound = True
    if not isfound:
        print("[+] - ERROR: No flight number was found")

def extractFlightDate(text):
    textSplitted = text.split("\n")
    isfound = False
    for line in textSplitted:
        match = re.match(r"([0-9]{2})([a-z]{3})", line, re.I)
        if match:
            print("[+] - We find the following flight date :", line)
            isfound = True
    if not isfound:
        print("[+] - ERROR: No flight date was found")

with open(FILE_PATH, mode='rb') as f:
    reader = PyPDF2.PdfFileReader(f)
    page = reader.getPage(0)
    text = page.extractText()
    print(text)
    
extractFlightNum(text)
extractFlightDate(text)