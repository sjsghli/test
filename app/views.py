from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    if request.method == "POST":
        api_url = request.POST.get("api_url")
        response = requests.get(api_url)
        data = response.json()
        
       
        context = {"data": data}
        return render(request, "app/api.html", context)
        
    return render(request, "app/index.html")


def register(request):
    return render(request, "app/register.html")
