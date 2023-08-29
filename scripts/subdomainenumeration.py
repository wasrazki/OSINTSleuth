import requests
import urllib3.exceptions

list = open ("./wordlists/subdomain.txt").read()
sublist= list.splitlines()


def subdomain(domain):
    lst=[]
    for sub in sublist:
        sub_domain = f"http://{sub}.{domain}" 
        try:
            requests.get(sub_domain)
        except requests.ConnectionError :
             pass
        except requests.exceptions.InvalidURL:
            pass
        except urllib3.exceptions.LocationParseError :
            pass
        except KeyboardInterrupt:
            print("interrupted!!!!!!!!")
            quit()
        else: 
             #print (f"{sub}.{domain}")
             lst.append(f"{sub}.{domain}")
    return(lst)

"""
if __name__ == "__main__":
    domain= "facebook.com"
    subdomain(domain)  """