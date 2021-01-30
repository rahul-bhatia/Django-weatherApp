from django.shortcuts import render
import requests

# Create your views here.
def home(request):
	if request.method=="POST":

		src=request.POST.get('src')
		print(src)
		try:
			a1="https://newsapi.org/v2/top-headlines"
			a2="?sources=" + src
			a3="&apikey=" + "097b0dbf475f4ad083ff1a0c55c7c4b2"
			wa=a1+a2+a3
			res=requests.get(wa)

			data=res.json()
			x=str(data['articles'])

			return render(request,'home.html',{'msg':x})
		except Exception as e:
			print("Issue : ",e)
	return render(request,'home.html')