from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def main(request, *args, **kwargs):
    return HttpResponse('hello')

@login_required
def test(request, *args, **kwargs):
    return render(request, 'main/test.html')