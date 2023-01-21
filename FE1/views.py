from django.shortcuts import render

# Create your views here.
def first(request):
    return render(request, 'FE-MainPage.html') 

def profile(request):
    context = {
        'user' : request.user
    }
    return render(request, 'profile.html', context)