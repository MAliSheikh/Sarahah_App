from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import uuid  

# REMAINING WORK 
# MESSAGES SEEN AND REPLY PAGE


def dashboard(request):
    return render(request, 'dashboard.html')

@login_required(login_url='/login/')
def index(request,user_identifier,uuid):
    if request.method == 'POST':
        if request.user.username == user_identifier and uuid == uuid:
            comment_text = request.POST.get('comment')  
            
            if comment_text:
                comment = Comment_Reply.objects.create(user=request.user, comment=comment_text)
                comment.save()
                return redirect('success', user_identifier=user_identifier, uuid=uuid)
            else:
                return redirect('index', user_identifier=user_identifier, uuid=uuid)
    else:
        return render(request, 'index.html')


@login_required(login_url='/login/')
def interface(request, user_identifier):
    if request.user.username == user_identifier:
        username = request.user.username

        user = User.objects.get(username=username)
        link = Link.objects.get(user=user)
        
        fullname = user.first_name
        uuid = link.uuid

        generated_link = f"/index/{username}/{uuid}"  # Replace with your generated lin  
        return render(request, 'interface.html', {
            'user_identifier': user_identifier,
            'generated_link': generated_link,
            'fullname': fullname,
        })
    else:
        return redirect('interface', user_identifier=request.user.username)

def comments(request, user_identifier, uuid):
    if request.user.username == user_identifier and uuid == uuid:
        user_comments = Comment_Reply.objects.filter(user=request.user, parent=None)
        link = Link.objects.get(user=request.user)
        uuid = link.uuid

        # data = request.get_json()  # Get the JSON data sent from the frontend
        # paragraph_content = data.get('content', '')
        
        return render(request, 'comments.html', {
            'user_comments': user_comments,
            'user_identifier': user_identifier,
            'uuid': uuid,
        })

def reply(request, user_identifier, uuid):
    if request.method == 'POST':
        if request.user.username == user_identifier and uuid == uuid:
            comment_no = request.POST.get('comment_no')
            reply_content = request.POST.get('reply')

            if reply_content:
                reply = Reply.objects.create(comment_no,reply_content)
                reply.save()
                user_reply = Reply.objects.filter(user=request.user)

                return render(request, 'comments.html', {
                   'user_reply': user_reply,
                   'user_identifier': user_identifier,
                   'uuid': uuid,
               })

         
         

def success(request, user_identifier, uuid):
    if request.user.username == user_identifier and uuid == uuid:
        return render(request, 'success.html', {
            'user_identifier': user_identifier,
            'uuid': uuid,
        })
   


def contact(request):
    return render(request, 'contact.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.info(request, 'Username does not exist')
            return redirect('/login_page/')
        
        user = authenticate(username = username ,password = password)
        if user is None:
            messages.info(request, 'Incorrect password')
            return redirect('/login_page/')
        else:
            messages.info(request, 'Login successful')
            login(request, user)
            return redirect('/interface/'+username+'/')
    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login_page/')

def register(request):
    if request.method == 'POST':
        fullname = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        unique_id = uuid.uuid4()

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, 'Username already exists. Please try another username')
            return redirect('/register/')

        user = User.objects.create(
            first_name=fullname,
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        link = Link.objects.create(user=user, uuid=unique_id)

        messages.info(request, 'Account created successfully')
        return redirect('/login_page/')
    return render(request, 'register.html')
 



