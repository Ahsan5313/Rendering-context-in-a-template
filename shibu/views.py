from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    
    text = {
        
       "name" : "Ahsanul Huq",
       "age" :24,
       "phone": "01753138080"
    }
    return render(request,'index.html',text)


def about(request):
    return render(request, 'about.html')

def contact(request):
    
    address = {
        
        'email' : 'ahsanulhuq17@gmail.com',
        'email2' :'ahsantheigomon@gamil.com'
    }
    return render(request, 'contact.html' , address)