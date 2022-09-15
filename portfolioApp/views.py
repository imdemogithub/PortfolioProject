from django.shortcuts import render
from django.http import HttpResponse

default_data = {
    'app_name': 'Portflio',
    'technologies': ['python', 'django', 'html', 'css', 'javascript']
}

for t in default_data['technologies']:
    print(t)

def index(request):
    return render(request, "index.html", default_data)
    # return HttpResponse("<h1>first response</h1>")