from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #context={
        #'name':'Shreya',
        #'age':20,
        #'nationality':'Indian',
    #}

    return render(request, 'index.html')


def register(request):
    return render(request,'register.html')

def counter(request):
    text =request.POST['text']
    amount_of_words= len(text.split())
    return render(request,'counter.html',{'amount':amount_of_words})
