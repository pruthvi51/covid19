import requests 
file_url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"

r = requests.get(file_url, stream = True) 

with open("data.txt","wb") as f: 
	for chunk in r.iter_content(chunk_size=1024): 
		if chunk: 
			f.write(chunk) 
