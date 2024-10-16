from django.shortcuts import render
import random

# Create your views here.
def index(request):
    # 메인페이지를 응답 
    context = {
        'name': '도경원',
    }
    return render(request, 'articles/index.html', context)

def dinner(request):
    foods = ['짜장면', '짬뽕', '탕수육', '양장피', '깐풍기']
    picked = random.choice(foods)
    context = {
        'foods': foods,
        'picked': picked,
    }
    return render(request, 'articles/dinner.html', context)

def search(request):
    return render(request, 'articles/search.html')

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    message = request.GET.get('message')
    context = {
        'message': message,
    }
    return render(request, 'articles/catch.html', context)

def greeting(request, name):
    context = {
        'name': name,
    }
    return render(request, 'articles/greeting.html', context)

def detail(request, num):
    context = {
        'num': num,
    }
    return render(request, 'articles/detail.html', context)
