from django.shortcuts import render
#from django.http import HttpResponse
#from datetime import datetime



def index(request):
    context = {} 
    return render(request, 'index.html', context)

def aboutus(request):
    context = {} 
    return render(request, 'about-us.html', context)


# Aula 03 - For com If
# def index(request):
#     products = [
#         {"name": "banana", "price": 10},
#         {"name": "apple", "price": 20},
#         {"name": "mango", "price": 30},
#         {"name": "orange", "price": 40},
#         {"name": "lemon", "price": 50},
#     ]
#     context = {
#         "products": products ,
#         "price_thereshold": 30,
#     } 
#     return render(request, 'index.html', context)

# Aula 02 - For
#def index(request):
#    products = [
#        {"name": "banana", "price": 10},
#        {"name": "apple", "price": 20},
#        {"name": "mango", "price": 30},
#        {"name": "orange", "price": 40},
#        {"name": "lemon", "price": 50},
#    ]
#    context = {
#        "products": products ,
#    } 
#    return render(request, 'index.html', context)

# Aula 01
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