from django.shortcuts import render
#from django.http import HttpResponse
#from datetime import datetime



def index(request):
    context = {

        
    } 

    return render(request, 'index.html', context)


#def index(request):
#    context={
#        "title": "Home Page",
#        "a_date": datetime.now(),
#        "course_title": "Aulas de Django",
#        "user":{
#            "name":"A",
#            "email":"cancerina_virginiana@email.com"
#        },
#        "product_price": 146842600.2446,
#        "random_text": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore"
#    }
#    return render(request, 'index.html', context)