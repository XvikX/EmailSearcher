import PyPDF2
import string
import re
import io
import flight

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
        matches = []
        matches.append(re.match(r"([0-9]{2})( {1})([a-z]{3})( {1})([0-9]{4})", line, re.I))
        matches.append(re.match(r"([0-9]{2})([a-z]{3})", line, re.I))
        for match in matches:
            if match:
                print("[+] - We find the following flight date :", line)
                isfound = True
    if not isfound:
        print("[+] - ERROR: No flight date was found")

def extractFlightDestinationDeparture(text):
    textSplitted = text.split("\n")
    isfound = False
    matchedCodeTemplate = []
    matches = []
    for line in textSplitted:
        # matches.append(re.match(r"([A-Z]+)( {1})([A-Z]{3}$)", line, re.I))
        matches += re.findall(r"( {1}[A-Z]{3}$)", line)
    stripped_matches = [str.strip(element) for element in matches]
    airportCodes = flight.GetAirportCode()
    airportNames = flight.GetAirportName()
    for match in stripped_matches:
        if match in airportCodes:
            print("[+] - We find the following flight Departure/Destination :", match, airportNames[airportCodes.index(match)])
            isfound = True
    if not isfound:
        print("[+] - ERROR: No flight info was found")

with open(FILE_PATH, mode='rb') as f:
    reader = PyPDF2.PdfFileReader(f)
    field = reader.getOutlines()
    print("number of page : ",reader.numPages)
    for page in reader.pages:
        print("\n\n\nNew page :")
        text = page.extractText()
        print(text)
    
extractFlightNum(text)
extractFlightDate(text)
extractFlightDestinationDeparture(text)
# extractImageFromPDF(FILE_PATH)

# pdf = pdftotext.PDF(FILE_PATH)
# # Iterate over all the pages
# for page in pdf:
#     print(page)
