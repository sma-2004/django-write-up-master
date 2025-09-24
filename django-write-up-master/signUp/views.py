from datetime import datetime
from pickle import TRUE
import random
from django.shortcuts import render, redirect
from django.http import HttpResponse
from signUp.SignUpForm import *
from signUp.models import *
from django.core.mail import send_mail
# Create your views here.

OTPs = {}


def SignUp(req):
    if req.method == 'GET':
        obj = SignUpForm()
        return render(req, 'signUp.html', {'Title': "SignUp", 'obj': obj, 'path': "otp"})
    else:
        try:
            OTPg = int(req.POST['OTP'])
            email = req.POST['email']
            li = OTPs.get(email)
            ntime = datetime.now()
            diff = str(ntime - li[1])
            print("Time on made", li[1])
            print("Time on checked", ntime)
            print("Time on Difference", diff)
            Otp=None
            diff = diff.split(':')
            if (len(diff) == 3):
                # hours
                if (len(diff[0]) == 1 and int(diff[0]) == 0):
                    # minutes
                    if (int(diff[1]) < 10):
                        Otp = int(li[0])
                    elif int(diff[1]) == 10:
                        diff = diff[2].split('.')
                        # seconds
                        if (int(diff[0]) == 0):
                            Otp = int(li[0])

            # for otp in OTPs:
            #     Otp = otp.getOTP(False)
            #         print("Otp which is removed : "+otp.id)
            #         OTPs.remove(otp)
            if (Otp == None):
                OTPs.pop(email)
                d = req.POST['New_password']
                e = req.POST['Confirm_password']
                obj = SignUpForm(req.POST)
                return render(req, 'signUp.html', {'Np': d, 'Cp': e, 'Title': "SignUp", 'obj': obj, 'path': "otp", 'err': "OTP Expired.Sign Up again"})

            cond = OTPg == Otp

            if (cond):
                fullname = req.POST['First_Name']+" " + req.POST['Last_Name']
                user = User(FullName=fullname,
                            email=req.POST['email'], password=req.POST['Confirm_password'])
                user.save()
                return redirect('/home')
        except Exception as e:
            print(e)
        d = req.POST['New_password']
        e = req.POST['Confirm_password']
        obj = SignUpForm(req.POST)
        return render(req, 'signUp.html', {'Np': d, 'Cp': e, 'Title': "SignUp", 'obj': obj, 'path': "./", 'err': "Wrong OTP.Valid for 10 minutes only"})

def getOTP():
        ran = random.randrange(100000, 999999)
        return ran

def getOtp(req):
    if req.method == 'POST':
        email = req.POST['email']
        d = req.POST['New_password']
        e = req.POST['Confirm_password']
        obj = SignUpForm(req.POST)
        # otp = OTP()
        # print(otp)
        otpG = str(getOTP())
        print(otpG)
        OTPs.update({email: [otpG, datetime.now()]})

        print("OTP added")
        # print("OTP already their")
        # print("len : ", len(OTPs))
        # for o in OTPs:
        #     # print("In loop")
        #     print(o)

        send_mail(
            'OTP',
            otpG,
            'asdigitalserver@gmail.com',
            [email]
        )

        print(email)
        print(otpG)

        print(OTPs)

        return render(req, 'signUp.html', {'Msg': "OTP Sent", 'Np': d, 'Cp': e, 'Title': "SignUp", 'obj': obj, 'path': "./"})
        # return HttpResponse(obj)
    else:
        pass


# def email(request):
#     send_mail(
#             'Hi',
#             'Hello are you  ?',
#             'asdigitalserver@gmail.com',
#             ['mishrashaurya445@gmail.com']
#         )
#     return HttpResponse("Message sent")


# class OTP:
    
    # id = 0
    # tm = datetime.now()

    # def __init__(self, id):
    #     self.id = id

    # def getOTP():
    #     ran = random.randrange(100000, 999999)
    #     return ran

    # def isValid(self):
    #     ntime = datetime.now()
    #     diff = str(ntime - self.tm)
    #     print("Time on made", self.tm)
    #     print("Time on checked", ntime)
    #     print("Time on Difference", diff)
    #     diff = diff.split(':')
    #     if (len(diff) == 3):
    #         # hours
    #         if (len(diff[0]) == 1 and int(diff[0]) == 0):
    #             # minutes
    #             if (int(diff[1]) < 10):
    #                 return True
    #             elif int(diff[1]) == 10:
    #                 diff = diff[2].split('.')
    #                 # seconds
    #                 if (int(diff[0]) == 0):
    #                     return True

    #     return False
