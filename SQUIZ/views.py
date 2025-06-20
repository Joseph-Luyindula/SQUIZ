from django.shortcuts import render
import random
from django.contrib.auth.decorators import login_required
from quiz.models import *

def index(request):
	context = {
	"top_categories":Category.objects.all().order_by("-total_game")[:10],
	"top_players": Profile.objects.all().order_by("-xp")[:10]
	}
	return render(request,"index.html",context=context)
	

def propos(request):
  return render(request,"apropos.html")
  
@login_required 
def profile(request):
  context = {
  "profile" : request.user.profile,
  }
  return render(request,"profil.html",context=context)

    
def thecategory(request,slug):
  context = {
    "category":Category.objects.get(slug=slug),
  }
  return render(request,"thecategory.html",context=context)
  

def quiz(request,slug):
  tag = Category.objects.get(slug=slug)
  questionnaire = tag.questionnaire_set.all()[:10]
  list_quiz = []
  for i in questionnaire:
  	dic = {"question" : i.Question,"answers" : i.response_list,"correct" : i.good_answer}
  	list_quiz.append(dic)
  context = {
    "category":tag.name,
    "quiz_data":list_quiz
  }
  return render(request,"quiz.html",context=context)
  
  
def categories(request):
	context = {
	"categories":Category.objects.all()
	}
	return render(request,"categories.html",context=context)
	
	
def singin(request):
	context = {}
	return render(request,"singin.html",context=context)
	
	
def logout(request):
	context = {}
	return render(request,"logout.html",context=context)
	
	
def login(request):
	context = {}
	return render(request,"login.html",context=context)
	
	
def faq(request):
	context = {}
	return render(request,"faq.html",context=context)
	
	
def badges(request):
	context = {}
	return render(request,"badges.html",context=context)
	
	
def classement(request):
	context = {}
	return render(request,"classement.html",context=context)