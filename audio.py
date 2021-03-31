import pyttsx3, PyPDF2
import sys
sys.setrecursionlimit(50000)

pdfReader = PyPDF2.PdfFileReader(open(
    '/root/Desktop/intelligence_technology_Trainner/practices_on_Python/pytho_mini_projects/Lec0_Python.pdf', 'rb'))
speaker=pyttsx3.init()
for page_num in range(pdfReader.numPages):
  text = pdfReader.getPage(page_num).extractText()
  speaker.say(text)
  speaker.runAndWait()
speaker.stop()
