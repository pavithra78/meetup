from django.shortcuts import render,redirect
from django.http import HttpResponse
from eventform.models import events
from eventform.models import Registration
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def home(request):
	return render(request,'home.html')

def allmeetup(request):
	user = request.user
	if (user is not None) and (not user.is_authenticated):
		return redirect("/") 

	totalmeets=events.objects.all()
	
	return render(request,"allmeetup.html",{"t":totalmeets})

def signup(request):

	if request.method=="POST":
		username=request.POST['username']
		email=request.POST['email']
		password=request.POST['password']
		present=User.objects.filter(username=username).exists()
		if not present:
			user=User.objects.create_user(username,email,password)
			return redirect('/')
		else:
			return HttpResponse("username already exists")
	return render(request,"signup.html")

def signin(request):
	user = request.user

	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(request,username=username,password=password)

		if user is not None:
			login(request,user)
			return redirect('/meetup/')

		else:
			return HttpResponse("Invalid Credentials")

	return render(request,"signin.html")

def logoutuser(request):
	user = request.user
	logout(request)
	return redirect('/')

def create_event(request):
	user=request.user
	if request.method=="POST":
		name=request.POST["name"]
		venue=request.POST["venue"]
		eventname=request.POST["eventname"]
		date=request.POST["date"]
		time=request.POST["time"]
		Amount=request.POST["Amount"]
		posts=events.objects.create(name=name,venue=venue,eventname=eventname,date=date,time=time,Amount=Amount)
		return redirect("/meetup/")
	#print(request.POST)
	return render(request,"create_event.html")

def joinevent(request,event_id):
	user=request.user
	if request.method=="POST":
		name=request.POST["name"]
		email=request.POST["email"]
		t=events.objects.get(pk=event_id)
		print(t)
		tl=Registration.objects.create(name=name,email=email,eventname=t)

		return redirect("/meetup/")

	
	eventsp=events.objects.all()
	return render(request,"joinevent.html")

def registration(request):
	totalregister=Registration.objects.all()
	return render(request,"registration.html",{"t":totalregister})

def registered(request,event_id):
	user=request.user
	et=events.objects.get(pk=event_id)
	re=Registration.objects.filter(eventname=et)

	return render(request,"registered.html",{"t":re})


		



