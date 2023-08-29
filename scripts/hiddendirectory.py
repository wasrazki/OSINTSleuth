import requests



def request(url):
	try:
		return requests.get("http://" + url)
	except requests.exceptions.ConnectionError:
		pass
def hidden_directory(target_url):
	output=""
	try:
		file = open("./wordlists/dir.txt", 'r')
		for line in file:
			directory = line.strip()
			full_url = target_url + '/' + directory
			response = request(full_url)
			if response:
				
				output+= '[*] Discovered Directory At This Path: ' + full_url
	except KeyboardInterrupt:
	
		quit()	
	return output 
"""
if __name__ == '__main__':
	target_url = "parapharmacie.tn"
	print("123")
	hidden_directory(target_url)
	#res = hidden_directory(target_url)
	#print(res)  """

		