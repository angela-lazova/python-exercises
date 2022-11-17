# -*- coding: utf-8 -*-
"""
Programming Assignment: The internet: mind-and-brain.de

Description: 
The ‘Doctoral alumni’ page at the website for the Berlin School of Mind and 
Brain lists the school’s former PhD students: 
http://www.mind-and-brain.de/people/doctoral-alumni/. 

The following Python program retrieves the details of these alumni from the 
current version of the web page and saves their information into a spreadsheet 
file. The spreadsheet contains the following information from the alumni's 
detail view: title of their doctoral project, description of their doctoral 
project, list of supervisors, cohort year, and URLs of any websites they have 
listed.

Author: Angela Lazova
Student ID: xxxxxx (School of Mind and Brain, Track Brain, Cohort 8)

"""

import requests
import pandas as pd
from bs4 import BeautifulSoup


def retrieve_data(url):
  """
    This function retrieves information from an URL passed as a parameter. 
    It returns a HTML text.
  """
  r  = requests.get(url)
  data = r.text
  return data


def extract_alumni_data(data):
  """
    This function takes a HTML text as an input variable and retrieves relevant 
    information from that text. 
    
    It formats the information and returns a table with the following columns:
        names
        doc_projects
        descriptions
        supervisors
        cohort
        Links

  """
  soup = BeautifulSoup(data)

  # Extracting the alumni's names from the file
  names = []

  for div in soup.findAll('div', attrs={'class':'students-list-item-full-name'}):
      names.append(div.findAll('a')[0].text.strip())
      
  # Extracting information from the tables
  all_tables = []
  doc_projects = []
  descriptions = []
  supervisors = []
  cohort = []
  urls = []

  maindiv = soup.find('div', attrs={'class': 'students-list-container'}) # defining the main div where information is stored

  for div in maindiv.findAll('div', attrs={'class':'col col-2'}): 
      t = div.findAll('table')  # <--- contains divs classified as tables but are empty
      if len(t) == 1:   # this is why I filter the list to include only the tables that contain information 
          all_tables.append(t[0]) # create list of all tables

  for a in all_tables:  # go through each table
      allrows = a.findAll("tr")  # find all rows for each table at a time
      
      for b in allrows: # go through all rows 
      
      # Check if the row is something we need and add it to the list
          if 'Doctoral project</th>' in str(b):
              doc_projects.append(b.findAll('td')[0].text.strip())
          elif 'Description</th>' in str(b):
              descriptions.append(b.findAll('td')[0].text.strip()) 
          elif 'Supervisors</th>' in str(b):
              supervisors.append(b.findAll('td')[0].text.strip())
          elif 'Cohort</th>' in str(b):
              cohort.append(b.findAll('td')[0].text.strip())
      
      # Check if the table is missing these rows and fill 'no info' in our list.       
      if 'Description</th>' not in str(a):
          descriptions.append('no info.')
          
      if 'Cohort</th>' not in str(a):
          cohort.append('no info.')
      
      # Find if the table has links and add it to the list (without emails)
      url = a.findAll('a', attrs ={'target': "_blank"})

      if len(url) == 0:
          urls.append('No links.')
      else:
          to_add = []
          for u in url:
              to_add.append(u.text.strip())
          urls.append(to_add)

  alumni = pd.DataFrame({
    "names": names,
    "doc_projects": doc_projects,
    "descriptions":  descriptions,
    "supervisors": supervisors,
    "cohort": cohort,
    "Links": urls
  })

  return alumni


def save(data, filename):
  """
    This function takes a table as an input variable and saves the information
    in a spreadsheet file.

  """
  data.to_excel(filename)
    

    
# Define Url
url_alumni = "http://www.mind-and-brain.de/people/doctoral-alumni/"

# Retrieve The HTML
html = retrieve_data(url_alumni)

# Extract Data
alumni_data = extract_alumni_data(html)

# Save Data
filename = "MindandBrain_alumni_data.xlsx"
save(alumni_data, filename)
