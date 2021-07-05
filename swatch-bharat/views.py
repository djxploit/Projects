# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render,redirect
from Swach_Bharat.settings import BASE_DIR
# Create your views here.
from models import user,session,Post,like,comment
from forms import signup_form,login_form,post_form,like_form,comment_form
from imgurpython import ImgurClient
def homepage_view(request):
    response = {}
    if request.method == 'GET':
        form = signup_form()
    elif request.method == 'POST':
        form = signup_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            if len(username)>=4 and len(password)>=5:
                new_user = user.objects.create(username=username, name=name, email=email, password=password)
                new_user.save()
                print "Account succesfully created"
                return redirect('/login/')
            else:
                print "Username should be atleast 4 char long and pass be 5 char long min"

    return render(request,'homepage.html',{'form':form})

def login_view(request):
    if request.method == "GET":
        form = login_form()
    elif request.method == "POST":
        form = login_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            act_usr = user.objects.filter(username=username,password=password).first()
            if act_usr:
                id = session(user=act_usr)
                id.create_token()
                id.save()
                response = redirect('/feed/')
                response.set_cookie(key='token',value=id.token)
                return response
            else:
                print "Wrong credentials"
    return render(request,'login.html',{'form':form})
def session_validator(request):
    if request.COOKIES.get('token'):
        usr = session.objects.filter(token=request.COOKIES.get('token')).first()
        if usr:
            return usr.user
        else:
            return None
    else:
        return None
def post_view(request):
    usr = session_validator(request)
    if usr:
        if request.method == "GET":
            form = post_form()
        elif request.method == "POST":
            form = post_form(request.POST,request.FILES)
            if form.is_valid():
                image = form.cleaned_data.get('image')
                caption = form.cleaned_data.get('caption')
                post_item = Post(user=usr, image=image, caption=caption)
                path = str(BASE_DIR + '/' + post_item.image.url)
                client = ImgurClient("f5b1c7a1ec081d7", "663b0b503e76b5b13b7b8209cc63fbfdc6ec7d51")
                post_item.image_url = client.upload_from_path(path,anon=True)['link']
                post_item.save()
                return redirect('/feed/')
        return render(request,'post.html',{'form':form})
    else:
        return redirect('/login/')
def feed_view(request):
    usr = session_validator(request)
    if usr:
        posts = Post.objects.all().order_by('posted_on')
        from clarifai.rest import ClarifaiApp
        app = ClarifaiApp(api_key="dae1929dd4bd4c17b7d2dba889589226")
        model = app.models.get('dirty')
        for temp in posts:
            usr_like = like.objects.filter(user=usr,post_id=temp.id).first()
            if usr_like:
                temp.has_liked=True
            response = model.predict_by_url("%s" % temp.image_url)
            for item in response['outputs'][0]['data']['concepts']:
                if item['name'] == 'dirty':
                    if (item['value']) < 0.5:
                        temp.tags = 'clean'
                    else:
                        temp.tags = 'dirty'

        return render(request,'feed.html',{'posts':posts})
    else:
        return redirect('/login/')

def like_view(request):
    usr = session_validator(request)
    if usr and request.method=="POST":
        form = like_form(request.POST)
        if form.is_valid():
            post_id = form.cleaned_data.get('post').id
            curr_usr_like = like.objects.filter(user=usr,post_id=post_id).first()
            if curr_usr_like:
                curr_usr_like.delete()
            else:
                like.objects.create(user=usr,post_id=post_id)
            return redirect('/feed/')
    else:
        return redirect('/login/')

def comment_view(request):
    usr = session_validator(request)
    if usr and request.method=="POST":
            form = comment_form(request.POST)
            if form.is_valid():
                post_id = form.cleaned_data.get('post').id
                comm_text = form.cleaned_data.get('comm_text')
                new = comment.objects.create(user=usr,post_id=post_id,comm_text=comm_text)
                new.save()
                return redirect('/feed/')
            else:
                return redirect('/login/')
    return redirect('/login/')

def logout_view(request):
    if request.COOKIES.get('token'):
        usr = session.objects.filter(token=request.COOKIES.get('token')).first()
        usr.delete()
    return render(request,'logout.html')
def myfeed_view(request):
    usr = session_validator(request)
    if usr:
        posts = Post.objects.filter(user=usr).order_by('posted_on')
        for post in posts:
            act_usr = like.objects.filter(user=usr,post_id=post.id).first()
            if act_usr:
                post.has_liked=True
        return render(request,'myfeed.html',{'posts':posts})
    else:
        return ('/login/')
