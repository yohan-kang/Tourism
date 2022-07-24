from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

# Create your views here.
def list(request):
    # 로그인 상태 표시 : ㄴis_authenticated
    print(request.user.is_authenticated) 
    return render(request,'tourism/list.html')
