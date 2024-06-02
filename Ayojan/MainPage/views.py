from django.shortcuts import render

#below function loads the landingpage html

def landing_view(request):
    return render(request,"MainPage/landingpage.html")

