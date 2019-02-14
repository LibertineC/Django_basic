# -*- coding: UTF-8 -*-
from django.http import HttpResponse            #用于给用户响应信息。

def index(request):
    return HttpResponse("your lord todd ?")