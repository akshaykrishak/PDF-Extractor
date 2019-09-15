import PyPDF2
from gtts import gTTS
import pytesseract
from PIL import Image
from fpdf import FPDF
import os 

def pdfextraction():
	fileName = input("Enter filename\n")
	try:
		pdfFile = open(fileName,'rb')	
		pdfReader = PyPDF2.PdfFileReader(pdfFile)
		page = pdfReader.numPages
		pageobj= pdfReader.getPage(page-1)
		text = pageobj.extractText()
		file = open(r"D:\pro\python\New folder\\testextract.txt",'a')
		file.writelines(text)
		file.close()
		file1=open(r"D:\pro\python\New folder\\testextract.txt",'r')
		print(file1.read())
		file1.close()
	except FileNotFoundError:
		print("File does not exist")

def textToSpeech():
	fileName = input("Enter filename\n")
	try:
		f=open(fileName)
		x=f.read()
		language='en'
		audio=gTTS(text=x,lang=language,slow=False)
		audio.save("samp.wav")
		os.system("samp.wav")
	except FileNotFoundError:
		print("File does not exist")	

def imgextract():
	pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
	fileName=input("Enter filename\n")
	try:
		img =Image.open(fileName)
		text=pytesseract.image_to_string(img)
		print(text)
	except FileNotFoundError:
		print("File does not exist")

def txttopdf():
	fileName=input("Enter filename\n")
	try:
		with open(fileName) as f:
			txtFile = f.read()
		pdf=FPDF()
		pdf.add_page()
		pdf.set_font("Arial",size=12)
		pdf.multi_cell(0,5,txtFile,align="C")
		pdf.output("test1.pdf",'F')
	except FileNotFoundError:
		print("File does not exist")

while  True:
	print("Menu\n1.PDF text Extraction\n2.Text to speech\n3.Image Extraction\n4.Text to PDF\n5.Exit\n")
	choice=input()
	if choice=='1':
		pdfextraction()
	elif choice=='2':
		textToSpeech()
	elif choice=='3':
		imgextract()
	elif choice=='4':
		txttopdf()	
	elif choice=='5':
		break
	else:
		print("Invalid Choice!!!\n")



