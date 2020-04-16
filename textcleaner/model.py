from django.shortcuts import render 
from django.http import HttpResponse,HttpRequest    

def logic(request): 
    return render(request,'index.html')
def result(request):
    txt=request.POST['data']
    if request.POST.get('capital','off')=="on":
        clean = txt.upper()
        
        dict={"clean":clean}
        txt=clean
        #return render(request,'result.html',{'purpose':"capital",'clean':cleantxt})

    if request.POST.get('punc','off')=="on":
        punc = '''!()-[]{};:'",<>./?@#$%^&*_~'''
        clean=""
        for ch in txt:
            if ch not in punc:
                clean+=ch 
        
        dict={"clean":clean}
        txt=clean
       # return render(request,'result.html',{'purpose':"punc",'clean':clean})
    
    if request.POST.get('space','off')=='on':
        clean=" ".join(txt.split())
        dict={"clean":clean}
        txt=clean
       # return render(request,'result.html',{'purpose':"punc",'clean':clean})

    if request.POST.get("line",'off')=='on':
        clean = ""
        for char in txt:
            if char != "\n" and char!="\r":
                clean = clean + char
        dict={"clean":clean}
    

    if request.POST.get("line",'off')=='off' and request.POST.get('space','off')=='off' and request.POST.get('punc','off')=="off" and request.POST.get('capital','off')=="off":
        return HttpResponse("<h2>You haven't selected any field please try selecting atlaest one field</h2>")
    
    return render(request,'result.html',dict)