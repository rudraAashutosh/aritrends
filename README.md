# <img src="http://aritrends.tech/folder.png" height="35vh"> [Aritrends](http://aritrends.tech)

Open source python lib from file processing work. Instead of writing old multiline codes, just write one line code and complete your work quickly and efficently.

##  Installation

Install git command and python3.10 in your system.

Enter the following code in your terminal.

```
git clone https://github.com/aritrendstech/aritrends
cd aritrends
pip3 install -r requirements.txt
```

## Command execution guide

### Convert Word file into pdf

```
import aritrends as w
w.convert("/path/to/folder/filename.docx")
```

### Convert multiple images to pdf

```
import aritrends as w
list = ["/path/to/folder/image1.png","/path/to/folder/image2.png","/path/to/folder/image3.png"]
w.image2pdf(list)
```

### Generate qrcode

```
import aritrends as w
w.qrcode("Hello world !")
```

### Convert multiple files into zip

```
import aritrends as w
list = ["/path/to/folder/filename.exe","/path/to/folder/filename2.png","/path/to/folder/filename3.dart"]
w.zip()
```

## Authors

[@aritrends](https://github.com/aritrends.tech)

[@abhineetraj](https://github.com/abhineetraj1)
