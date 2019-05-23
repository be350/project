from django.shortcuts import render
from .models import Login

# Create your views here.

def login(request):
    return render(request, "login/index.html")

def check(request):
    user_id = request.GET.get('uid') #index.html에 name 해놓은 것이랑 일치시켜야 함
    user_pwd = request.GET.get('pwd')
    user_infos = Login.objects.all()

    for user_info in user_infos:
        if(user_info.Uid == user_id and user_info.PWD == user_pwd):
            text = "로그인 성공"
            break
        else:
            text = "로그인 실패"

    context = {'text' : text}
    return render(request, "login/check.html", context)