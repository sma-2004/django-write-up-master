from django.shortcuts import render, redirect
from django.http import HttpResponse
from Home.form import *
from Home.models import *
import random
# Create your views here.


# def txtInput(req):
#     return render(req, "text.html")


# def txtSave(req):
#     print(req.POST)
#     txt = req.POST['txt']
#     stxt = temptext(txt=txt)
#     stxt.save()
#     return HttpResponse("Data Saved")


# def dataHelp(req):
#     if req.method == "POST":
#         email = req.POST['email']
#         try:
#             privacy = req.POST['privacy']
#         except:
#             privacy = 0
#         textarea = req.POST['textarea']

#         txt = text(email=email, privacy=privacy, text=textarea)
#         txt.save()
#         return HttpResponse("Saved")
#     else:
#         frm = Input()
#         return render(req, "test.html", {'frm': frm})


# def dataHelpDisplay(req):
#     if req.method == 'POST':
#         email = req.POST['email']
#         data = text.objects.filter(email=email, privacy=False).values()
#         for da in data:
#             print(da)
#         return HttpResponse("Look Console!")
#     else:
#         form = Email()
#         return render(req, 'filter.html', {'form': form})

# def ImgUploadTest(req):
#     if req.method == "GET" :
#         img = ImageForm()
#         return render(req,"test.html",{'frm':img})
    


def Home(req):
    if req.method == 'GET':
        title = "Home"
        if 'email' in req.session.keys():
            value = req.session['email']

            g = req.GET.get('global', "")
            if g == "g":
                data = text.objects.filter(privacy=0).order_by("-likesCount").values()
            else:
                data = text.objects.filter(email=value).values()
            # print(data)
            Len = 0
            for d in data:
                d.get("id")
                # print(d)
                Len = Len+1

            page = "loggedIn.html"
            visible = "true"
            if g == "g":
                page = "user.html"
                visible = "false"
                for d in data:
                    if len(d.get("likes")) > 0:  # type: ignore
                        likess = d.get("likes")
                        likess = likess.split(",")# type: ignore
                        add = False
                        for l in likess:
                            if l == value :
                                add=True
                                break
                        if add:
                            d.update({"liked": "1"})
                        else:
                            d.update({"liked": "0"})
                    else:
                        d.update({"liked": "0"})
            elif g == "home":
                page = "user.html"
                for d in data :
                    d.update({"liked" : "0"})
                    
            for d in data:
                xt = d.get('text')
                xt = xt.replace("\n","<br>")# type: ignore
                d.update({'text' : xt})
                print(d)
            return render(req, page, {'Title': title, 'state': req.session['email'], 'log': "logout", 'email': req.session['email'], 'data': data, 'len': (Len+1), 'visible': visible})
        else:
            da = text.objects.filter(privacy=0).order_by("-likesCount").values()
            data=da
            # c=0
            # for d in data:
            #     data.append(d)
            #     if c==4 :
            #         break
            #     c=c+1
                
            return render(req, 'loggedof.html', {'Title': title, 'state': 'Login', 'log': "/login","data" : data})
    else:
        g = req.POST.get('globe', None)
        flike = ""
        if g == "true":
            id = req.POST.get('id', None)
            likeCount = req.POST.get('likecount', 0)
            email = req.POST.get('email', None)
            liked = req.POST.get('liked', None)
            Txt = text.objects.get(id=id)
            Txt.likesCount = likeCount
            if liked == "true":
                Txt.likes = Txt.likes + "," + email
            else:
                lik = Txt.likes.split(",")
                # print(lik)
                lik.remove(str(email))
                # print(lik)
                for l in lik:
                    if len(l) > 0:
                        flike = flike + l + ","
                # print(flike)
                # if len(flike) > 2:
                #     flike = flike[len(flike)-2]
                # print(flike)
                Txt.likes = flike
            Txt.save()
        else:
            txt = req.POST.get('text', None)
            id = req.POST.get('id', None)
            email = req.POST.get('email', None)
            New = req.POST.get('New', None)
            privacy = req.POST.get('privacy', None)
        
            # print(txt, id, email, New, privacy)

            if New == "true":
                if privacy == "1":
                    pvt = 1
                else:
                    pvt = 0
                Txt = text(id=email+"_"+id, email=email, privacy=pvt, text=txt)
                Txt.save()
            else:
                Txt = text.objects.get(email=email, id=id)
                Txt.text = txt
                Txt.privacy = privacy
                Txt.save()
            # return HttpResponse(txt)
            # return HttpResponse(json.dumps("Hi"),content_type="application/json")
        return HttpResponse("Done")


def logout(req):
    if 'email' in req.session.keys():
        del req.session['email']
        return redirect('/')


def delete(req):
    print("In delete method")
    id = req.POST.get('id')
    email = id[0:id.index("_")]
    print("Id going to be deleted : "+id)
    Txt = text.objects.get(email=email, id=id)
    Txt.delete()
    return HttpResponse("Deleted")

# def getData(req):
#     if req.method == 'GET':
#         return HttpResponse("Hi")
