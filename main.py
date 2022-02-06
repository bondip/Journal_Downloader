# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 14:43:58 2022

@author: Parker
"""

# Import libraries
import re
import requests
from bs4 import BeautifulSoup

months = ['01','02','03','04','05','06','07','08','09','10','11','12']
years = ['2011','2010','2009','2008','2007','2006','2005','2004','2003','2002']

# URL from which pdfs to be downloaded
url  = "http://X.com/"

for year in years:
    for month in months:
        actual_url = url + '/' + year + '/' + month
        print(actual_url)
        # Requests URL and get response object
        response = requests.get(actual_url)
          
        # Parse text obtained
        soup = BeautifulSoup(response.text, 'html.parser')
          
        # Find all hyperlinks present on webpage
        links = soup.find_all('a')
          
        i = 0
          
        # From all links check for pdf link and
        # if present download file
        for link in links:
            if ('.pdf' in link.get('href', [])):
                slink = str(link)
                namelocend = slink.index('.pdf')
                slinkrev = slink[0:namelocend]
                slinkrev = slinkrev[::-1]
                namelocstart = slinkrev.index('/')
                name = slink[namelocend-namelocstart:namelocend]
        #        namelocstart = slink[:namelocend:-1].index('/')
                
        #        name = re.split(".pdf", str(link))
        #        for n in name:
        #            print(n)
                
        #        name = link.split("//.")
                i += 1
                print("Downloading file: ", name)
          
                # Get response object for link
                response = requests.get(link.get('href'))
          
                # Write content in pdf file
                pdf = open(name+".pdf", 'wb')
                pdf.write(response.content)
                pdf.close()
                print("File ", i, " downloaded")
          
        print("All PDF files downloaded")