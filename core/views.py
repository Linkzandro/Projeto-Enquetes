from django.shortcuts import render

def index(request):
    content={'title':'Index'}
    return render(request,'core/core-index.html',content)

