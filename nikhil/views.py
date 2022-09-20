from string import punctuation
from django.shortcuts import render
from django.urls import include,path
from django.http import HttpResponse


# Create your views here.
def index2(request):
    return render(request, 'index2.html')


def index(request):
    # return HttpResponse('''hello <a href='https://www.youtube.com/'> youtube</a>''')
    params = {'name':'Nikhil' , 'place':'Mars'}
    return render(request, 'index.html',params)

def nextpage(request):
    djtext = request.GET.get('name', 'default')
    remove_punc = request.GET.get('removepunc', 'off')
    uppercase = request.GET.get('Uppercase', 'off')
    # print(djtext)
    # print(remove_punc)
    # print(uppercase)
    punctuations = '''!()-{}[]:;'"/,.<>|\?!@#$%^&*_-~`=+-'''
    new_string = ""
    if remove_punc == 'on':
        for char in djtext:
            if char not in punctuations:
                new_string += char
                
        if uppercase == "on":
            new_string = new_string.upper
            return render(request, 'nextpage.html',{"string": new_string})
        
        else:
            return render(request, 'nextpage.html',{"string": new_string})
                
    else:
        if uppercase == "on":
                    
            new_string = djtext.upper
            return render(request, 'nextpage.html',{"string": new_string})
        
        else:
            return render(request, 'nextpage.html',{"string": djtext})
    # return render(request, 'nextpage.html',{"string": new_string})
        