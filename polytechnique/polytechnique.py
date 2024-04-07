import requests
from bs4 import BeautifulSoup
import re
import helper

def deadline_ahead_list(data):
  tbody = data.find('tbody')
  rows = tbody.find_all('tr')
  conference_array = []
  if len(rows) == 0: return conference_array
  for row in rows:
      cells = row.find_all('td')
      name = cells[0].find('a').text.strip() 
      conference_link = cells[0].find('a')['href']
      description = cells[0].find('span', class_='tooltiptext').text.strip() if cells[0].find('span', class_='tooltiptext') is not None else ""
      location = cells[1].text.strip()
      deadline = cells[2].text.strip()
      date = cells[3].text.strip()
      notification = cells[4].text.strip()
      subformat_details =re.sub(r'\s+', ' ',  cells[5].text.strip().replace("\n", "").replace("\t", ""))
      conference_array.append({'name':name, 'conference_link':conference_link,'description':description, 'location':location, 'deadline':deadline, 'date':date, 'notification':notification,'subformat_details':subformat_details})
  return conference_array

def running_list(data):
  tbody = data.find('tbody')
  rows = tbody.find_all('tr')
  conference_array = []
  if len(rows) == 0: return conference_array
  for row in rows:
      cells = row.find_all('td')
      name = cells[0].find('a').text.strip()
      conference_link = cells[0].find('a')['href']
      location = cells[1].text.strip()
      date = cells[2].text.strip()
      remark =re.sub(r'\s+', ' ',  cells[3].text.strip().replace("\n", "").replace("\t", ""))
      conference_array.append({'name':name, 'conference_link':conference_link,  'location':location, 'date':date, 'remark':remark})
  return conference_array

def deadline_over_list(data):
  tbody = data.find('tbody')
  rows = tbody.find_all('tr')
  conference_array = []
  if len(rows) == 0: return conference_array
  for row in rows:
    cells = row.find_all('td')
    name = cells[0].find('a').text.strip()
    conference_link = cells[0].find('a')['href']
    location = cells[1].text.strip()
    date = cells[2].text.strip()
    notification = cells[3].text.strip()
    final_version = cells[4].text.strip()
    early_registration = cells[5].text.strip()
    remarks = re.sub(r'\s+', ' ',  cells[6].text.strip().replace("\n", "").replace("\t", ""))
    conference_array.append({'name':name,'conference_link':conference_link,'location':location,'date':date,'notification':notification,'final_version':final_version,'early_registration':early_registration,'remarks':remarks})
  return conference_array

def planning_conference_list(data):
  tbody = data.find('tbody')
  rows = tbody.find_all('tr')
  conference_array = []
  if len(rows) == 0: return conference_array
  for row in rows:
    cells = row.find_all('td')
    name = cells[0].find('a').text.strip()
    conference_link = cells[0].find('a')['href']
    year = cells[1].text.strip()
    location = cells[2].text.strip()
    starting_date = cells[3].text.strip()
    ending_date = cells[4].text.strip()
    remarks = re.sub(r'\s+', ' ',  cells[5].text.strip().replace("\n", "").replace("\t", ""))
    conference_array.append({'name':name,'conference_link':conference_link,'year':year,'location':location,'starting_date':starting_date,'ending_date':ending_date,'remarks':remarks})
  return conference_array



if __name__ == "__main__":
  url = "https://www.lix.polytechnique.fr/~hermann/conf.php"
  response = requests.get(url)
  deadline_ahead_conference_arr = []
  running_conference_arr = []
  deadline_over_future_conference_arr = []
  planning_conference_arr = []
  if(response.status_code == 200):
    soup = BeautifulSoup(response.content,'html.parser')
    tables = soup.find_all('table', class_="conference")
    deadline_ahead = tables[0]
    running = tables[1]
    deadline_over_future = tables[2] 
    planning_conference = tables[3]
    deadline_ahead_conference_arr = deadline_ahead_list(deadline_ahead)
    running_conference_arr = running_list(running)
    deadline_over_future_conference_arr = deadline_over_list(deadline_over_future)
    planning_conference_arr = planning_conference_list(planning_conference)
    helper.write_json(deadline_ahead_conference_arr,"deadline_over_future_conference_conference.json")
    helper.write_csv(deadline_over_future_conference_arr,"deadline_over_future_conference_conference.csv")
    helper.write_json(running_conference_arr,"running_conference_arr.json")
    helper.write_csv(running_conference_arr,"running_conference_arr.csv")
    helper.write_json(deadline_over_future_conference_arr,"deadline_over_future_conference_arr.json")
    helper.write_csv(deadline_over_future_conference_arr,"deadline_over_future_conference_arr.csv")
    helper.write_json(planning_conference_arr,"planning_conference_arr.json")
    helper.write_csv(planning_conference_arr,"planning_conference_arr.csv")
  