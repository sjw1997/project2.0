from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def signin(request):
    return render(request,"SignIn.html")

def signup(request):
    return render(request,"SignUp.html")

def problemset(request):
    return render(request,"ProblemSet.html")

def answerset(request):
    return render(request,"AnswerSet.html")

def ask(request):
    return render(request,"Ask.html")

def answer(request):
    return render(request,"Answer.html")

def logout(request):
    logout(request)
    return HttpResponseRedirect("/")
