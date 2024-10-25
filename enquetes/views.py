from django.shortcuts import render

# Create your views here.
def dashboard(request):
    content={'title':'dashboard'}
    return render(request,'enquetes/dashboard.html',content)