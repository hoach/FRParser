import urlparse
import urllib2
import os
import sys
from bs4 import BeautifulSoup

#Verify that BeautifulSoup is installed
try:
	from bs4 import BeautifulSoup
except ImportError:
	print "[*] Please download and install Beautiful Soup first!"
	sys.exit(0)

#Download all of the files
def fileDownload(url, download_path):
	for page in url:
		i = 0
		request = urllib2.Request(page)
		html = urllib2.urlopen(request)
		soup = BeautifulSoup(html.read(),"html.parser")
	
		for tag in soup.findAll('a', href=True):
			tag['href'] = urlparse.urljoin(page, tag['href'])
	
			if (os.path.splitext(os.path.basename(tag['href']))[1] == ".pdf") or (os.path.splitext(os.path.basename(tag['href']))[1] == ".docx") or (os.path.splitext(os.path.basename(tag['href']))[1] == ".xlsx") or (os.path.splitext(os.path.basename(tag['href']))[1] == ".pptx") or (os.path.splitext(os.path.basename(tag['href']))[1] == ".doc") or (os.path.splitext(os.path.basename(tag['href']))[1] == ".ppt") or (os.path.splitext(os.path.basename(tag['href']))[1] == ".xls"):
				current = urllib2.urlopen(tag['href'])
				print "\n[*] Downloading: %s" %(os.path.basename(tag['href']))
		
				f = open(download_path + "\\" + os.path.basename(tag['href']),'wb')		
				f.write(current.read())
				f.close()
			
				i+=1
	
		print "\n[*] Downloaded %d files from %s" %((i+1),page)
#	raw_input("[+] Press any key to exit...")