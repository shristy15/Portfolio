from django.shortcuts import render

# Create your views here.
def HomePage(request):
    if request.method=='POST':
        pass
    else:
        return render(request,"home.html",{})      


def Aayush(request):
   if request.method=='POST':
        pass
   else:
        return render(request,"Aayush.html",{})      

def Aryan(request):
   if request.method=='POST':
        pass
   else:
        return render(request,"Aryan.html",{}) 

def Shristy(request):
   if request.method=='POST':
        pass
   else:
        return render(request,"Shristy.html",{})        