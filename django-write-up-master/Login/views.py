from django.shortcuts import render, redirect
from django.http import HttpResponse
from Login.LoginForm import *
from signUp.models import *
# Create your views here.


def logIn(req):
    if req.method == 'GET':
        if 'email' in req.session.keys():
            return redirect('/home')
        else :
            form = LoginForm()
            return render(req, "Login.html", {'Title': "Login", 'frm': form})
    else:
        try:
            user = User.objects.get(email=req.POST['email'])
            if user.password == req.POST['password']:
                req.session['email'] = req.POST['email']
                return redirect('/')
            else:
                form = LoginForm(req.POST)
                return render(req, "Login.html", {'Title': "Login", 'frm': form, 'msg': "Wrong Password", 'posL': "27%"})
        except:
            form = LoginForm()
            return render(req, "Login.html", {'Title': "Login", 'frm': form, 'msg': "Unable to find the user : "+req.POST['email'], 'posL': "10%"})
        # form = LoginForm(req.POST)
        # return render(req,"Login.html",{'Title':"Login" , 'frm' : form,'msg':"Hi their"})
        # return HttpResponse('Hi')
