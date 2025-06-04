from django.shortcuts import render
import random
from django.contrib.auth.decorators import login_required
from quiz.models import *

def index(request):
	context = {}
	return render(request,"index.html",context=context)
	

def propos(request):
  return render(request,"apropos.html")
  
@login_required 
def profile(request):
  context = {
  "profile" : request.user.profile,
  }
  return render(request,"profil.html",context=context)

    
def quiz(request):
  context = {
    "Category":Category.objects.all(),
  }
  return render(request,"quiz.html",context=context)
  

def question(request,slug):
  tag = Category.objects.get(slug=slug)
  questionnaire = tag.questionnaire_set.all()
  print(questionnaire)
  list_quiz = []
  for i in questionnaire:
  	reponse = i.response_list
  	choice = []
  	x = []
  	print(reponse)
  	while True:
  		if not len(x) == 4:
  			print(len(x))
  			print(len(x) <= 4)
  			n = random.randint(1,4)
  			print(n)
  			if not n in x:
  				print(x)
  				x.append(n)
  				choice.append(reponse[n-1])
  		else:
  			print("fin")
  			break 
  	dic = {"q" : i.Question,"r" : choice,"g" : i.good_answer}
  	print(dic)
  	list_quiz.append(dic)
  	print(list_quiz)
  context = {
    "category":tag.name,
    "quiz_data":list_quiz
  }
  return render(request,"question.html",context=context)