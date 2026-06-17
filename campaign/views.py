from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import VolunteerForm

def home(request):
    return render(request, 'campaign/home.html')

def about(request):
    return render(request, 'campaign/about.html')

def register(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save() # Saves data safely to SQLite database
            messages.success(request, 'Thank you for registering! Together we can save the planet.')
            return redirect('register')
    else:
        form = VolunteerForm()
    
    return render(request, 'campaign/register.html', {'form': form})

# Create your views here.
