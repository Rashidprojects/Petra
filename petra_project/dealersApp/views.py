from django.shortcuts import render

def findDealer(request):
    return render(request, 'findNeardealers.html')

def becomeDealer(request):
    return render(request, 'becomeAdealers.html')