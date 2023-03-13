from django.shortcuts import render

# Create your views here.
def virat(request):
    d={'name':'virat'}
    return render(request,'kholi.html',context=d)