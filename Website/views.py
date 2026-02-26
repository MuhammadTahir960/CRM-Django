from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

def home(request):
    if request.user.is_authenticated:
        records = Record.objects.all()
        return render(request, 'home.html', {'records':records})
    else:
        messages.error(request, "You Must Be Logged In To View This Page.")
        return redirect('login')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful!")
            return redirect('home')
        else:
            messages.error(request, "Invalid Username or Password. Please Try Again.")
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('login')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            user = authenticate(username=username, password=password)
            
            login(request, user)
            messages.success(request, "Successfully Registered!")
            return redirect('login')
        else:
            messages.error(request, "Registration Failed. Please Correct The Errors Below.")
            return render(request, 'register.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = get_object_or_404(Record, id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.error(request, "You Must Be Logged In To View Record...")
        return redirect('login')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = get_object_or_404(Record, id=pk)
        delete_it.delete()
        messages.success(request, "Record Deleted Successfully...")
        return redirect('home')
    else:
        messages.error(request, "You Must Be Logged In To Delete Record...")
        return redirect('login')
        
def add_record(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddRecordForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Record Added Successfully...")
                return redirect('home')
            else:
                messages.error(request, "Error Adding Record. Please Check The Form.")
                return render(request, 'add_record.html', {'form': form})
        else:
            form = AddRecordForm()
            return render(request, 'add_record.html', {'form': form})
    else:
        messages.error(request, "You Must Be Logged In To Add Record...")
        return redirect('login')

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = get_object_or_404(Record, id=pk)
        if request.method == 'POST':
            form = AddRecordForm(request.POST, instance=current_record)
            if form.is_valid():
                form.save()
                messages.success(request, "Record Updated Successfully...")
                return redirect('record', pk)
            else:
                messages.error(request, "Error Updating Record. Please Check The Form.")
                return render(request, 'update_record.html', {'form': form, 'id': pk})
        else:
            form = AddRecordForm(instance=current_record)
            return render(request, 'update_record.html', {'form': form, 'id': pk})
    else:
        messages.error(request, "You Must Be Logged In To Update Record...")
        return redirect('login')
