import pyttsx3
import PyPDF2

file=open(file = open("C:/Users/hp/Desktop/python/python/climate_change.pdf", mode="rb")
,mode="rb")
pdf_reader=PyPDF2.PdfFileReader(file)
pages=pdf_reader.numRages
print(pages)
mole=pyttsx3.init()
page=pdf_reader.getPage(3)
text=page.extractText()
mole.say(text)
mole.runAndWait()