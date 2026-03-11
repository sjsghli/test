from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import CustomUserCreationForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                messages.success(request, "Registration successful.")
                return redirect("index")
            except Exception as e:
                messages.error(request, str(e))
                
        else:
            messages.error(request, "Form is not valid.")
            
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/register.html", {"form": form})
