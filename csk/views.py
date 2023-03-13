from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dhoni(request):
    d={'name':'Dhoni'}
    return render(request,'csk.html',context=d)