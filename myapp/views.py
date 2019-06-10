# 클라이언트의 요청을 처리하는 파일 (MTV에서 V(View)는 Controller 역할을 함.)

from django.shortcuts import render
from django.http.response import HttpResponse

def index(request):
    return HttpResponse("인덱스 요청 처리")

def hello(request):
    msg = "장고 만세"
    ss = "<html><body> 장고 프로젝트 연습 %s</body></html>"%(msg,)
    return HttpResponse(ss)

def hello_tem(request):
    msg2 = "구조를 파악하자"
    return render(request, 'hi.html', {'key':msg2})