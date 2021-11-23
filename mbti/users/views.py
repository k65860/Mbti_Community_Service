from django.shortcuts import render

# Create your views here.
def login_view(request):
    if request.method == "POST":
        print(request.POST)

    return render(request,"app/Templates/login.html")