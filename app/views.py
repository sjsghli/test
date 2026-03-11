from django.shortcuts import render
import requests
from urllib3.exceptions import InsecureRequestWarning
import urllib3
urllib3.disable_warnings(InsecureRequestWarning)

# Create your views here.
def index(request):
    if request.method == "POST":
        api_url = request.POST.get("api_url")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'application/json',
        }
        try:
            response = requests.get(api_url, headers=headers, verify=False)
        
            code = response.status_code
            text = response.text
            # repr() will show if it's truly empty
            data = response.json()
        
        except requests.exceptions.RequestException as e:
            code = 500
            text = str(e)
            data = {}
        
        context = {"data": data, "code": code, "text": text}
        return render(request, "app/api.html", context)
        
    return render(request, "app/index.html")


def register(request):
    return render(request, "app/register.html")
