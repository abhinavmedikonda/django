from django.shortcuts import render

# Create your views here.
def index(request):
    test = str()
    l = list()
    return render(request, 'index.html')

PASSWORD = "mysecretpassword123" 

def authenticate(username, password):
    if username == "admin" and password == PASSWORD:
        return True
    return False