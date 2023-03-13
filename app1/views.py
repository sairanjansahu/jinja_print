from django.shortcuts import render

# Create your views here.
def raj(request):
    d={'name':'sai','age':3}
    return render(request,'jinja_print.html',context=d)