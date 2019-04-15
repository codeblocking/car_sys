from django.shortcuts import render

# Create your views here.

def show(request):
    print(111111111111111111)
    usr_id = request.GET.get('id', None)
    print(usr_id)

    return render(request, 'employee/show.html')
