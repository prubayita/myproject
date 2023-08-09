from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User
from .decorators import *
from django.contrib import messages
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')  # Redirect to the desired page after successful login
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    return render(request, 'cred/login.html')

def logout_view(request):
    logout(request)
    return redirect('login') 

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        # role = request.POST['role']  # Get the selected role from the dropdown
        
        # Create a new user in the database
        
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
            
        user.save()

            # Redirect to the desired page after successful signup (e.g., login page)
        return redirect('login')
       

    return render(request, 'cred/signup.html')

@login_required
def dashboard(request):
    tasks = Task.objects.all().values()
    context = {'tasks': tasks}  
    return render(request, 'index.html', context)


@login_required
def newTask(request):
    users = User.objects.all()
    projects = Project.objects.all()
    error_message = None  # Initialize error_message as None

    if request.method == 'POST':
        name = request.POST.get('name')
        startDate = request.POST.get('startDate')
        endDate = request.POST.get('endDate')
        assignee_username = request.POST.get('assignee')
        project_name = request.POST.get('project')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        attach_file = request.FILES.get('attach_file')

        try:
            assignee_user = User.objects.get(username=assignee_username)
            project_instance = Project.objects.get(name__iexact=project_name)
            
            task = Task(
                name=name,
                startDate=startDate,
                endDate=endDate,
                assignee=assignee_user,
                project=project_instance,
                description=description,
                priority=priority,
                attach_file=attach_file
            )
            task.save()

            return redirect('dashboard')
        
        except User.DoesNotExist:
            error_message = 'Assignee user does not exist.'
        except Project.DoesNotExist:
            error_message = 'Project does not exist.'

        messages.success(request, 'Task created successfully.')
    context = {'users': users, 'projects': projects, 'error_message': error_message}
    return render(request, 'test1.html', context)




@login_required
def recordProject(request):    
    if request.method == 'POST':
        # Get the form data
        name = request.POST.get('name')
        description = request.POST.get('description')
                
        project = Project(
            name=name,
            description=description
        )
        # Save the Visitor instance
        project.save()

    return render(request, 'projects.html')