from docx2pdf import convert
import qrcode
import zipfile
import datetime
from PIL import Image
import webbrowser
print("http://aritrends.tech\nType 'aritrends.credits()', 'aritrends.license()' or 'aritrends.github()' for more information")

def rnm():
	return str(datetime.datetime.now()).replace("-","").replace(".","").replace(":","").replace(" ","")

class aritrends:
	def docx2pdf(filename):
		try:
			convert(filename, rnm()+".pdf")
		except Exception as e:
			print(e)
	def zip(list):
		n= rnm()
		var = zipfile.ZipFile(n+".zip","w")
		try:
			for i in list:
				var.write(i)
		except Exception as e:
			print(e)
	def image2pdf(list):
		n = rnm()
		t=[]
		try:
			for i in list:
				t.append(Image.open(i).convert("RGB"))
			k = t[0]
			t.remove(t[0])
			k.save(str(n)+".pdf", save_all=True, append_images=t)
		except Exception as e:
			print(e)
	def qrcode(text):
		qrcode.make(text).save(rnm()+".png")
	def github():
		webbrowser.open("http://github.com/aritrendstech")
	def credits():
		print("This project is developed by Abhineet Raj (github-> @abhineetraj1).")
	def license():
		print("""""")