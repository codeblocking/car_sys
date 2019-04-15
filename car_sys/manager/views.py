from django.shortcuts import render, redirect
from app.models import User
# Create your views here.



def show(request):
    # 查询数据
    users = User.objects.exclude(type=1)
    user_list = []
    for user in users:
        user_dic = {}
        user_dic['id'] = user.id
        user_dic['name'] = user.usr
        user_dic['entry_time'] = user.entry_time
        user_dic['total_count'] = 0
        user_dic['total_money'] = 0
        user_list.append(user_dic)

    return render(request, 'manager/show.html', {'list': user_list})


def add(request):
    if request.method == "GET":
        return render(request, 'manager/add.html')
    if request.method == "POST":
        usr = request.POST.get('usr', None)
        pwd = request.POST.get('pwd', None)
        user = User.objects.filter(usr=usr).first()
        if not user:
            User.objects.create(usr=usr, pwd=pwd)
        return redirect('/manager/show/')


def delete(request, id):
    User.objects.filter(id=id).delete()
    return redirect('/manager/show/')


def reset(request, id):
    User.objects.filter(id=id).update(pwd='123456')
    return redirect('/manager/show/')