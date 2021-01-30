import requests

try:
	a1="https://newsapi.org/v2/top-headlines"
	a2="?sources=" + "the-hindu"
	a3="&apikey=" + "097b0dbf475f4ad083ff1a0c55c7c4b2"
	wa=a1+a2+a3
	res=requests.get(wa)

	data=res.json()
	x=(data['articles'])

	for i in x:
		print("*" *20)
		print(i['title'])
		print(i['url'])
	
except Exception as e:
	print("Issue : ",e)