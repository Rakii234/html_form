from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.

def Create_Topic(request):
    if request.method=='POST':
        tn=request.POST['topic']
        to=Topic.objects.get_or_create(topic_name=tn)[0]
        to.save()
        return HttpResponse('Data is inserted')
    return render(request,'Create_Topic.html')

def Create_Webpage(request):
    d={'to':Topic.objects.all()}
    if request.method=="POST":
        tn=request.POST['topic']
        to=Topic.objects.get(topic_name=tn)
        n=request.POST['name']
        u=request.POST['url']
        wo=Webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
        wo.save()
        return HttpResponse('Data is inserted')
    return render(request,'Create_Webpage.html',d)


def Create_ac(request):
    d={'wo':Webpage.objects.all()}
    if request.method=='POST':
        n=request.POST['name']
        wo=Webpage.objects.get(name=n)
        a=request.POST['author']
        d=request.POST['date']
        ao=Accessrecord.objects.get_or_create(name=wo, author=a, date=d)[0]
        ao.save()
        return HttpResponse('Data Inserted Successfully')
    return render (request,"Create_ac.html",d )
