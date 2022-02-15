# Self Created
import readline
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.GET.get('text', 'default')
    rmpunc = request.GET.get('removepunc', 'off')
    punctuations = '''.,'":;[]{}()/|\<>!-_?*&@+'''
    analyzed_txt = ""
    if rmpunc == "on":
        for char in djtext:
            if char not in punctuations:
                analyzed_txt += char
        params = {"your_analyzer":"Removed Punctuations", "analyzed_txt": analyzed_txt}
        print(params)
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")


# def removepunc(request):
#     text = request.GET.get('text', 'default')

#     return HttpResponse("Puntuation Remover")

# def spaceremover(request):
#     return HttpResponse("Space Remover")

# def capitalizeletter(request):
#     return HttpResponse("Capitalize Letters")

# def newlineremove(request):
#     return HttpResponse("Newline remover")

# def char_count(request):
#     return HttpResponse("Character Counter")


