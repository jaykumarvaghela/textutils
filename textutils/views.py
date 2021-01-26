###########################################################################################
'''
File created by Jay.
'''
###########################################################################################
from django.http import HttpResponse
from django.shortcuts import render
from . import functions
import string

def index(request):
    return render(request, 'index.html')

def removepunc(strr):
    strr = strr
    p = string.punctuation
    text = ""
    for char in strr:
        if char not in p:
            text = text+char
    
    return text


def analyze(request):
    #Grab text
    djtext = request.POST.get('text','default')
    # All functionality
    removePunc = request.POST.get('removePunc','off')
    allcaps = request.POST.get('allCaps', 'off')
    capfirst = request.POST.get('capfirst', 'off')
    newline = request.POST.get('newlineremove', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')
    parms={}
    analyzed = ''
    # Return text
    if removePunc == 'on':
        analyzed = functions.removepunc(djtext)
        djtext = analyzed
    if allcaps == 'on':
        analyzed = djtext.upper()
        djtext = analyzed

    if capfirst == 'on':
        analyzed = djtext.capitalize()
        djtext = analyzed
    
    if newline == 'on':
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        djtext = analyzed
    
    if spaceremove == 'on':
        for char in djtext:
            if char != " ":
                analyzed = analyzed+char
        djtext = analyzed

    if charcount == 'on':
        analyzed = len(djtext)
        djtext = analyzed
        
    if removePunc != ' on' and allcaps != 'on' and capfirst != 'on' and newline != 'on' and spaceremove != 'on' and charcount != 'on':
        analyzed = "Error"

    parms = {'purpose':'Analysed', 'analyzed_text':analyzed}
    # final Return
    return render(request, 'analyze.html', parms)

# def removePunc(request):
#     djtext = request.GET.get('text','default')
#     return HttpResponse(djtext"<br> <p><a href='../'>back</a>")

# def capfirst(request):
#     return HttpResponse("Capitalize First<br> <p><a href='../'>back</a>")

# def newlineremove(request):
#     return HttpResponse("New line remover<br> <p><a href='../'>back</a>")

# def spaceremove(request):
#     return HttpResponse("Space remover<br> <p><a href='../'>back</a>")

# def charcount(request):
#     return HttpResponse("Character Counter<br> <p><a href='../'>back</a>")