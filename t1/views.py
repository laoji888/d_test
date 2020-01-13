from django.shortcuts import render

# Create your views here.
def login(request):  # 子路由调用时返回login.html
    return render(request,'login.html')