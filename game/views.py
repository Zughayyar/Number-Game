from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    if 'random_number' not in request.session : 
        request.session['random_number'] = random.randint(1,100)
    return render(request , 'index.html')

def guess(request):
    request.session['guessed_number'] = int(request.POST['guess'])
    return redirect('/')

def destroy_session(request):
    request.session['random_number'] = None
    request.session['guessed_number'] = None
    return redirect(index)