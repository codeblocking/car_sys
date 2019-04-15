from django.shortcuts import render, redirect, reverse, HttpResponse
from django.views import View
from app.models import User

# Create your views here.

def home(request):
    return render(request, 'index.html')


def index(request):
    url = reverse('home')
    return redirect(url)


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        usr = request.POST.get('usr', None)
        pwd = request.POST.get('pwd', None)
        print(usr, pwd)
        user = User.objects.filter(usr=usr, pwd=pwd).first()
        if user:
            if user.type:  # 值1为经理
                return redirect('/manager/show/')
            else: # 值0职工，要将登录的员工id携带
                return redirect('/employee/show/?id=%s' % user.id)

        # 登录失败
        return render(request, 'failed.html')

# def error(request):
#     return render(request, 'error.html')


class Error(View):
    def get(self, request):
        return render(request, 'error.html')
