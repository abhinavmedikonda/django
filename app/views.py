from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

PASSWORD = "mytestpassword123" 

def authenticate(username, password):
    test = str()
    l = list()
    d = dict()
    if username == "admin" and password == PASSWORD:
        return True
    return False