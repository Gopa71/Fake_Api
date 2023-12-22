from django.shortcuts import render
import requests
# Create your views here.

app_name='api'
def home(req):
    url='https://dummyjson.com/products'
    res=requests.get(url)
    data=res.json()
    print(data)
    return render(req,'index.html',{'data':data})


def details(req,id):
    url='https://dummyjson.com/products/'+id
    res=requests.get(url)
    data=res.json()

    return render(req,'details.html',{'data':data})

def cart(req):

  return render(req,'cart.html')

def message(req):
   
   return render(req,'message.html')