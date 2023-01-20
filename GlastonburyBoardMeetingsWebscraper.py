#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests
from bs4 import BeautifulSoup


# In[170]:


raw_data = requests.get('https://meetings.boardbook.org/Public/Organization/2417')
data = BeautifulSoup(raw_data.text, 'html5lib')
for row in data.find_all('tr', attrs={'class': "row-for-board"}):
    time = str(row.find('div').text).strip().split(' - ')[0]
    meeting_type = str(row.find('div').text).strip().split(' - ')[1]
    print(f"{time}, {meeting_type}")
    


# In[236]:


locations = []
meeting_locations = []
for row in data.find_all('tr', attrs={'class': "row-for-board"}):
    for index, info in enumerate(row.find_all('div')):
        if index != 0 and index % 2 == 0:
            location = str(info.text).strip().split()
            if 'map' in location:
                {i: location.remove(location[-1]) for i in range(3)}
            if "Hall2155" in location:
                location = ['Town', 'Council' ,'Chambers' ,'Glastonbury', 'Town', 'Hall' ,'2155', 'Main', 'Street', 'Glastobury', 'CT','06033']
            
            locations.append(location)

while locations.count(["Agenda"]) != 0:
    locations.remove(['Agenda'])
while locations.count(['Minutes']) != 0:
    locations.remove(['Minutes'])
while locations.count(['Supplemental Resources']) != 0:
    locations.remove(['Supplemental Resources'])
    
for places in locations:
    meeting_location = " ".join(map(str, places))
    meeting_locations.append(meeting_location)


# In[294]:


for row in data.find_all('tr', attrs={'class': 'row-for-board'}):
    try:
        lo = str(row.find('a', href=True)).split("?q=")[1].split('target')[0].split('"')
        print(lo[0].strip())
    except IndexError:
        oh = str(row.find('a', href=True)).split("?q=")[0].split('\n')
        try:
            print(oh[1].strip())
        except IndexError:
            pass


# In[310]:


for row in data.find_all('tr', attrs={'class': 'row-for-board'}):
    try:
        print(str(row.find_all('a', href=True)[1]).split('<a href="')[1].split('">')[0])
    except IndexError:
        pass


# In[ ]:




