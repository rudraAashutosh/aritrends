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
		print("""MIT License

Copyright (c) 2022 Aritrends

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.""")
