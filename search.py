import requests, sys, bs4
from pymongo import MongoClient
client = MongoClient('localhost:27017')
db = client.WebData


print('Searching...')

# Download the search page
res = requests.get("https://google.co.in/search?q=" + ''.join(sys.argv[1:]))
res.raise_for_status()

# Pull data out from the html
soup = bs4.BeautifulSoup(res.text)
# Select all the search links
linkElems = soup.select('.r a')

# Store and print the top 5 google search results
for i in range(5):
    print (linkElems[i])
    link = linkElems[i].get('href')
    print ('\n')
    print (link)
    print('\n')
    db.Websites.insert_one(
        {
            'link':link
        }
    )

print('Data insertion successful\n')

# Dispalys the stored data on the database
webCol = db.Websites.find()
print("All data from the database:\n")
for web in webCol:
    print(web)
