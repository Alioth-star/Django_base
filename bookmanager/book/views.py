from django.shortcuts import render

# Create your views here.
"""
视图
所谓的视图 其实就是python函数
视图函数有两个要求
1.视图函数的第一个参数就是接受请求 之恶个请求其实就是HttpRequest的类对象

"""
# request
from django.http import HttpRequest
from django.http import HttpResponse


# 我们期望用户输入 Http://127.0.0.1:8000/index 访问主页
# 来访问视图函数
def index(request):
    # return HttpResponse("ok")
    # rander 渲染模板
    # 参数:request, template_name, context = None
    # 请求,模板名字,context=None

    # 模拟数据查询
    # 将视图中的数据传给HTML模板
    # HTML（模板）采用{{字典的key}}形式
    context = {
        'name': '马上双十一点击有惊喜'
    }

    return render(request, 'book/index.html', context)
