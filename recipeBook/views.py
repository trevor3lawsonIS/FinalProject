from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(request) :
    sOutput = '<html><head><title>My Title</title></head><body><p style="color:red;"><b>one</b></p><p style="color:blue;">two</p><p style="font-size:50px;">three</p><ul><li>A</li><li>B</li><li>C</li></ul></body></html>'
    return HttpResponse(sOutput) 

def createPageView(request) :
    sOutput = '<html><head><title>My Title</title></head><body><p>Welcome to create page</p></body></html>'
    return HttpResponse(sOutput) 

def updatePageView(request) :
    sOutput = '<html><head><title>My Title</title></head><body><p>Welcome to update page</p></body></html>'
    return HttpResponse(sOutput)

def readPageView(request) :
    sOutput = '<html><head><title>My Title</title></head><body><p>Welcome to read page</p></body></html>'
    return HttpResponse(sOutput) 