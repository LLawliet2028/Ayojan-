from django.shortcuts import render

#below funciton loads up profile_view html
def profile_view(request):
    return render(request, 'Accounts/profile_view.html')

#below funciton loads up login_page html
def login_view(request):
    return render(request, 'Accounts/login_page.html')


#below funciton loads up signup_page html
def signup_view(request):
    return render(request, 'Accounts/signup_page.html')
