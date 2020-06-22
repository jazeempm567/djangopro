from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.generic import View
# Create your views here.
import datetime
from myapp.models import *
from myapp.forms import *
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

def hello(request):
    return HttpResponse("hello world")

def view1(request,num=0,num2=0):
    today=datetime.datetime.now()
    print(num)
    print(num2)

    a="changed data"
    lst=[1,2,3,4]
    students=[{"name":"sam","age":20,"img":'Desert.jpg'},
              {"name":"john","age":21,"img":'Koala.jpg'},
              {"name":"zara","age":22,"img":'Tulips.jpg'}]
    all_students=Student.objects.all()


    return render(request,'page1.html',{'data1':lst,'data2':all_students,'today':today,'num':num})

def view2(request):
    today=datetime.datetime.now()

    a="changed data"
    lst=[1,2,3,4]
    students=[{"name":"sam","age":20,"img":'Desert.jpg'},
              {"name":"john","age":21,"img":'Koala.jpg'},
              {"name":"zara","age":22,"img":'Tulips.jpg'}]

    return render(request,'page2.html',{'data1':lst,'data2':students,'today':today})

def view3(request):

    s1=Student(name="sam",age=21,height=165)
    s1.save()

    return HttpResponse("done")

def view4(request):
    students=Student.objects.filter(name="sam",height=165)
    print(students)
    s=""
    for student in students:
        s+=student.name+' '+str(student.age)+'<br>'
    return HttpResponse(s)

def view5(request):
    student=Student.objects.get(id=1)
    student.name="john"
    student.age = 22
    student.height = 170
    student.save()
    #
    #
    #
    students=Student.objects.all()
    # student.name="zara"
    # student.age=22
    # student.height=160
    # student.save()

    # student.delete()

    # if Student.objects.filter(namee='jon',height=170).exists()
    for student in students:

        student.height = 175
        student.save()
    # #
    # score=Score(student=student,sub="maths",score=60)
    # score.save()
    # scores= Score.objects.all()
    # s=""
    # for score in scores:
    #     s+=score.sub+' '+str(score.score)+' '+str(score.student.height)+'<br>'
    return redirect(view1,12,23)


class MyView(View):
    def get(self,request):
        return render(request,'page4.html',{})
    def post(self,request):

       nm=request.POST['name']
       age=request.POST['age']
       height=request.POST['height']

       a=Student(name=nm,age=age,height=height)
       a.save()
       return HttpResponse(nm+' '+age)

def view6(request):
    if request.method == 'POST':
        uname=request.POST['username']
        pwd=request.POST['password']

        return HttpResponse(uname+' '+pwd)

    return render(request,'page4.html',{})

def getFormData(request):
    uname=request.POST['username']
    pwd=request.POST['password']
    return HttpResponse(uname+' '+pwd)

class MyView2(View):
    def get(self,request):
        myform=MyForm()
        return render(request,'page5.html',{'myform':myform})

    def post(self,request):
        myform=MyForm(request.POST)

        uname="none"
        pwd="none"
        if myform.is_valid():
            myform.save()


        else:
            return HttpResponse("not valid")
        data=request.POST
        uname=data['username']
        pwd=data['password']
        return HttpResponse(uname+' '+pwd)



def view7(request):
    if request.method == 'POST':
        data=request.POST
        name=data['name']
        uname=data['username']
        pwd=data['password']
        return HttpResponse(name+' '+uname+' '+pwd)

    return render(request,'page5.html',{})

def view8(request):
    return redirect(view1,12,43)

    # data=request.POST
    # name=data['name']
    # uname=data['username']
    # pwd=data['password']
    # return HttpResponse(name+' '+uname+' '+pwd)

class UploadView(View):
    def get(self,request):
        a=Files.objects.all()

        return render(request,'page6.html',{'all_images':a})
    def post(self,request):

        myform=UploadForm(request.POST,request.FILES)
        if myform.is_valid():
            name=myform.cleaned_data['name']
            file=myform.cleaned_data['image']
        # name=request.POST['name']
        # file=request.FILES['image']

            a=Files(name=name,file=file)
            a.save()
        return HttpResponse("done")



def page7(request):
    if request.method == "POST":
        data=request.POST
        name=data['name']
        pwd=data['password']
        return HttpResponse(name+' '+pwd)


    return render(request,'page7.html',{})


def getData(request):
    data=request.POST
    name=data['name']
    pwd=data['password']
    return HttpResponse(name+' '+pwd)

# class FormView(View):
#     def get(self,request):
#         myform=LoginForm()
#         return render(request,'page7.html',{'myform':myform})
#     def post(self,request):
#         myform=LoginForm(request.POST)
#         if myform.is_valid():
#             name=myform.cleaned_data['name']
#             uname=myform.cleaned_data['username']
#             pwd=myform.cleaned_data['password']
#
#
#             return HttpResponse(name+" "+uname+' '+pwd)
#         # data=request.POST
#         # uname=data['username']
#         # name=data['name']
#         # pwd=data['password']
#
#         return HttpResponse("form is not valid")


# def logout(request):
#     del request.session['uname']
#     return redirect()


# class FileUpload(View):
#     def get(self,request):
#         all_rows=Files.objects.all()
#         return render(request,'page6.html',{'all_rows':all_rows})
#     def post(self,request):
#         name=request.POST['name']
#         img=request.FILES['image']
#         ob=Files(name=name,file=img)
#         ob.save()
#         return HttpResponse("done")


# class Register(View):
#     def get(self,request):
#         user = User.objects.create_user(username='john',password= 'johnpassword',)
#         user.is_staff=True
#         user.first_name="jon"
#
#         user.save()
#         return HttpResponse("done")
#
#
#         # request.user.is_authenticated()
#
#     def post(self,request):
#
#         pass
        # user = User.objects.create_user(username='john',password= 'johnpassword',)
        # user.is_staff=True
        # user.first_name="jon"
        #
        # user.save()

class FileUpload(View):
    def get(self,request):
        all_rows=Files.objects.all()
        return render(request,'page6.html',{'all_rows':all_rows})
    def post(self,request):
        name=request.POST['name']
        file=request.FILES['file']

        ob=Files(name=name,file=file)
        ob.save()
        return HttpResponse("done")



def page3(request):
    return render(request,'page3.html')

import json
def getdata(request):
    data=request.GET['data']
    data=json.loads(data)
    print(data[0])
    d={"name":"sam","age":20}
    return HttpResponse(json.dumps(d))

def home(request):
    user=""

    if request.session.has_key('uname'):
        username=request.session['uname']
        user=Users.objects.get(username=username)
        return render(request,'home.html',{'user':user})
    else:
        return redirect(login)

def secondpage(request):
    if request.session.has_key('uname'):
        username=request.session['uname']
        user=Users.objects.get(username=username)

        return render(request,'secondpage.html',{'user':user})
    else:
        return redirect(login)
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        pwd=request.POST['password']

        if Users.objects.filter(username=username,password=pwd).exists():
            request.session['uname']=username
            return redirect(home)
        else:
            return HttpResponse("invalid username or password")
    return render(request,'loginform.html')

def logout(request):
    if request.session.has_key('uname'):
        del request.session['uname']
    return redirect(login)

def new(request):
    a = "<h1>hello</h1>"
    l=["text1", "text2", "text3","text4",'text5']
    return render(request, 'new.html', {'a': a, "some_list": l})


