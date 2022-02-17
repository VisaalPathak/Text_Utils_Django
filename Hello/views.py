# Self Created
import readline
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.GET.get('text', 'default')
    rmpunc = request.GET.get('removepunc', 'off')
    extraspacerm = request.GET.get('extraspacerm','off')
    Uppercase = request.GET.get('Uppercase', 'off')
    punctuations = '''.,'":;[]{}()/|\<>!-_?*&@+'''
    analyzed_txt = ""
    if rmpunc == "on":
        for char in djtext:
            if char not in punctuations:
                analyzed_txt += char
        params = {"your_analyzer":"Removed Punctuations", "analyzed_txt": analyzed_txt}
        return render(request, 'analyze.html', params)
    
    elif extraspacerm == "on":
        for i, char in enumerate(djtext):
            if not(djtext[i] == " " and djtext[i+1] == " "):
                analyzed_txt = analyzed_txt + char
        params = {"your_analyzer":"Remove Extra Space", "analyzed_txt": analyzed_txt}
        return render(request, "analyze.html", params)

    elif Uppercase == "on":
        for char in djtext:
            analyzed_txt += char.upper()
        params = {"your_analyzer":"UPPER CASE CONVERTER", "analyzed_txt": analyzed_txt}
        return render(request, "analyze.html", params)
    
    else:
        return HttpResponse("Error")



