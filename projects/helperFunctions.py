# imports
from bs4 import BeautifulSoup
import requests
import csv
from urllib import parse

# use as library
def main():
    print("This is a library, not a script")

if __name__ == "__main__":
    main()

# Accenture Scrape
class Job:
    def __init__(self, title, link, country, language):
        self.title = title
        self.href = link
        self.country = country
        self.language = language
    def __str__(self):
        return self.title

class Country:
    def __init__(self, name, language):
        self.name = name
        self.language = language
        self.jobs = []
    def addJob(self, job):
        self.jobs.append( job )

def getCountryName():
    # Parse specific website to get all conutry codes (accenture website for different regions)
    accentureWeb = 'https://www.accenture.com/de-de/careers/jobsearch?'
    # We parse the html with beautifulsoup
    source = requests.get( accentureWeb ).text
    soup = BeautifulSoup(source, 'lxml')
    countrylist = soup.find('ul', class_="countrylist")
    countryCodes = {}
    countryNameList = []
    try:
        for country in countrylist.find_all(class_='list-group-item'):
            name = country['value']
            if name not in countryCodes:
                countryCodes[name] = True
                countryNameList.append( name )
    except Exception:
        pass
    return countryNameList

def getLanguageName():
    # Parse specific website to get all conutry codes (accenture website for different regions)
    accentureWeb = 'https://www.accenture.com/de-de/careers/jobsearch?'
    # We parse the html with beautifulsoup
    source = requests.get( accentureWeb ).text
    soup = BeautifulSoup(source, 'lxml')
    countrylist = soup.find('ul', class_="countrylist")
    languageCodes = {}
    languageNameList = []
    try:
        for country in countrylist.find_all(class_='list-group-item'):
            textlist = country.text.split()
            indexl = 1
            indexr = 4
            for i in range(2,len(textlist)):
                if textlist[i] == "(":
                    indexl = i
                elif textlist[i] == ")":
                    indexr = i
                    break
            name = ' '.join(textlist[indexl+1:indexr])
            if name not in languageCodes:
                languageCodes[name] = True
                languageNameList.append( name )
    except Exception:
        pass
    return languageNameList

def getAccentureJobs():
    # Parse specific website to get all conutry codes (accenture website for different regions)
    accentureWeb = 'https://www.accenture.com/de-de/careers/jobsearch?'
    # We parse the html with beautifulsoup
    source = requests.get( accentureWeb ).text
    soup = BeautifulSoup(source, 'lxml')
    countrylist = soup.find('ul', class_="countrylist")
    countryCodes = {}
    try:
        for country in countrylist.find_all(class_='list-group-item'):
            cc = country['data-country-site']
            textlist = country.text.split()
            indexl = 1
            indexr = 4
            for i in range(2,len(textlist)):
                if textlist[i] == "(":
                    indexl = i
                elif textlist[i] == ")":
                    indexr = i
                    break
            language = ' '.join(textlist[indexl+1:indexr])
            countryCodes[cc] = [ cc[3:5] , country['value'], language ]
    except Exception:
        pass
    # Use accenture API to collect all jobs for every region
    accentureAPI = "https://www.accenture.com/api/sitecore/JobSearch/FindJobs"
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
        "content-type": "application/json; charset=UTF-8",
        "sec-ch-ua": "\"Google Chrome\";v=\"93\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"93\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-requested-with": "XMLHttpRequest"
        }
    jobList = []
    for cc in countryCodes:
        payload = "{\"f\":1,\"s\":9,\"k\":\"\",\"lang\":\"" + countryCodes[cc][0] + "\",\"cs\":\"" + cc + "\",\"df\":\"[{\\\"metadatafieldname\\\":\\\"skill\\\",\\\"items\\\":[]},{\\\"metadatafieldname\\\":\\\"location\\\",\\\"items\\\":[]},{\\\"metadatafieldname\\\":\\\"postedDate\\\",\\\"items\\\":[]},{\\\"metadatafieldname\\\":\\\"travelPercentage\\\",\\\"items\\\":[]},{\\\"metadatafieldname\\\":\\\"jobTypeDescription\\\",\\\"items\\\":[{\\\"term\\\":\\\"entry-level job\\\",\\\"selected\\\":true}]},{\\\"metadatafieldname\\\":\\\"businessArea\\\",\\\"items\\\":[]},{\\\"metadatafieldname\\\":\\\"specialization\\\",\\\"items\\\":[]},{\\\"metadatafieldname\\\":\\\"workforceEntity\\\",\\\"items\\\":[]}]\",\"c\":\"" + countryCodes[cc][1] + "\",\"sf\":0,\"syn\":false,\"isPk\":false,\"wordDistance\":0,\"userId\":\"\"}"
        #                 ?       ?   searchTerm              Language (en)                         countryCode (us-en)                                   Name of the field: Selections                               Name of the field: Selections                                 Name of the field:   Selections                                     Name of the field:     Selections                                      Name of the field: Selections                     Entry-Level Job is selected                                                      Name of the field: Selections                                     Name of the field:   Selections                                    Name of the field:     Selections                     countryName (Deutschland)       ?           ?               ?                   ?             ?
        try:
            response = requests.request("POST", accentureAPI, data=payload, headers=headers)
            dict = response.json()
            jobs = dict['documents']
            for job in jobs:
                jobUrl = job['jobDetailUrl'].split('/')
                jobUrl[3] = cc
                jobList.append( Job( job['title'], '/'.join(jobUrl), countryCodes[cc][1], countryCodes[cc][2] ) )
        except Exception:
            pass
    return jobList

    # ?