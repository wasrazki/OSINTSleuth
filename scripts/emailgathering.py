import requests
from bs4 import BeautifulSoup

 


#skymem: skymem is a powerful  website that can be used to gather emails 
#web scrapping
def skymem(domain):
    url =f'https://www.skymem.info/srch?q={domain}&ss=home'
    page = requests.get(url)
    soupe= BeautifulSoup(page.text, 'html.parser')
    tab = soupe.find_all('table') [0]
    emails= ""
    rows =tab.find('tbody').find_all('tr')
    for row in rows:
        email=row.find('a').text 
        emails+= email + '\n'
    return(emails)    


#hunter.io is a powerful website that can be used to gather emails
#api 
def hunter(domain):
    emails =""
    url =f'https://api.hunter.io/v2/domain-search?domain={domain}&api_key=d4891d886562d279a92b76c313b56b183ae3e10e'
    page= requests.get(url)
    data =page.json()
    email_addresses = [email['value'] for email in data['data']['emails']]
    for em in email_addresses:
        emails += em +'\n'
    return emails    


def get_email(domain):
    emails=""
    emails += skymem(domain)
    emails += hunter(domain)
    return(emails)

"""
if __name__ == '__main__':
   domain ="aziza.tn"
   emails = get_email(domain) 
   print (emails)  
   """