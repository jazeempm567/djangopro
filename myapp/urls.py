from django.urls import path
from myapp.views import *
from django.views.generic import TemplateView,ListView
from myapp.models import *
urlpatterns = [
    path('hel/',hello,name="hel"),

    path('view1/',view1,name="view1"),
    path('view1/<int:num>/<int:num2>/',view1), #view1(req,num=234,num2=45)
    path('view2/',view2,name="view2"),
    path('view3/',view3,name="view3"),
    path('view4/',view4,name="view4"),
    path('view5/',view5,name="view5"),

    path('static/',TemplateView.as_view(template_name='page3.html'),name="static"),

    path('list/',ListView.as_view(model=Student,template_name='page1.html')),

    path('demo/',MyView.as_view(),name='myview'),
    path('view6/',view6,name="view6"),
    path('getform/',getFormData,name="getform"),

    # path('getform/',getFormData,name="getform"),

    path('myview2/',MyView2.as_view(),name="myview2"),
    path('view7/',view7,name="view7"),
    path('view8/',view8,name="view8"),
    path('upload/',UploadView.as_view(),name="upload"),
    path('page7/',page7,name="page7"),
    # path('getdata/',getData,name="getdata"),
    # path('formview/',FormView.as_view(),name="formview"),
    path('fileupload/',FileUpload.as_view(),name="fileupload"),
    # path('register/',Register.as_view()),
    path('page3/',page3,name="page3"),
    path('getdata/',getdata,name="getdata"),


    path('login/',login,name="login"),
    path('home/',home,name="home"),
    path('second/',secondpage,name="second"),
    path('logout/',logout,name="logout"),
    path('new/',new,name="new"),



]
