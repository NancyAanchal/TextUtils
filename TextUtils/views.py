from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,  'index2.html')
    

def analyze(request):
    
    djtext=request.POST.get('text',  'default')
    
    removepunc=request.POST.get('removepunc',  'off')
    capfirst=request.POST.get('capfirst', 'off')
    nlineremove=request.POST.get('nlineremove', 'off')
    extrspaceremove=request.POST.get('extrspaceremove', 'off')
    numremove=request.POST.get('numremove', 'off')

    if removepunc=='on':
        analyzed=''
        punctuations='''!()-{}[];:'"\,.<>/?@#$%^&*_~`'''
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        djtext=analyzed
        
    
    if(capfirst=="on"):
        analyzed=''
        for char in djtext:
            analyzed=analyzed+char.upper()
        djtext=analyzed
        

    if(nlineremove=="on"):
        analyzed=''
        for char in djtext:
            if char!="/n":
                analyzed=analyzed+char
        djtext=analyzed

    if(numremove=="on"):
        numbers="0123456789"
        analyzed=''
        for char in djtext:
            if char not in numbers:
                analyzed=analyzed+char
        djtext=analyzed

    if(extrspaceremove=="on"):
        analyzed=''
        for index, char in enumerate(djtext):
            if index!=0:
                if not(djtext[index]==' ' and djtext[index-1]==' '):
                    analyzed=analyzed+char
            else:
                analyzed+=char
    if not(removepunc=='on' or capfirst=="on" or nlineremove=="on" or extrspaceremove=="on"):
        analyzed=djtext
    
    params={'char_count':len(analyzed), 'analyzed_text':analyzed}
    return render(request, 'analyze2.html', params)