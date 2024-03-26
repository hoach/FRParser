import urlparse
import urllib2
import os
import sys
from bs4 import BeautifulSoup
import filecmp
from filedownload import fileDownload
from filecompare import fileCompare

#URLs with documentation to download
webpage = ('https://www.fedramp.gov/documents/', 'https://www.fedramp.gov/templates/')

#Create folder to download comparison documentation
newpath = '//mnt/c/Users/Matthew\ Houy/Documents/Python/FedRAMPParser/FedRAMPAuthoritative'
if not os.path.exists(newpath):
	os.makedirs(newpath)
	
#Get the user's email address
mailaddr = ('matthouy@gmail.com')

#File location where the documentation will be downloaded locally
download_pwd = '//mnt/c/Users/Matthew\ Houy/Documents/Python/FedRAMPParser/FedRAMPAuthoritative'

#Download all of the files
fileDownload(webpage,download_pwd)

#Run file comparison/alerting/archiving process
fileCompare(mailaddr)
