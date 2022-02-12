from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from book.models import BookInfo


def index(request):
    # books = BookInfo.objects.all()  # 查询数据库全部信息
    return HttpResponse('hello index')


# **********************增加数据**********************
from book.models import BookInfo

# 方法1 必须要调用的对象的save方法才能将数据保存到数据库
book = BookInfo(
    name='Django',
    pub_date='2020-02-01',
    readcount=1
)
book.save()

# 方法二
# object 相当于一个代理 可以用于增删改查
BookInfo.objects.create(
    name='年少不知愁滋味',
    pub_date='2022-02-12',
    readcount=1
)

# ****************************修改数据**********************
# 方式1
book = BookInfo.objects.get(id=6)
book.name = '运维开发'
book.save()
# 想要保存数据 需要调用对象save方法
# 方法二
# filter 过滤
BookInfo.objects.filter(id=6).update(name='下一个学爬虫', commentcount=666)
# ************************删除数据********************
# 方式一
book = BookInfo.objects.get(id=6)
# 两种删除 物理删除 逻辑删除(is_delete)
book.delete()
# 方式二
BookInfo.objects.get(id=5).delete()
BookInfo.objects.filter(id=5).delete()

# **********************查询**************************
# get查询单一结果 没有查到会出现异常
try:
    book = BookInfo.objects.get(id=6)
except BookInfo.DoesNotExist:
    print('查询失败，没有查询到')
# all查询多个结果
books = BookInfo.objects.all()
# count 查询结果数量
BookInfo.objects.all().count()
BookInfo.objects.count()

# 过滤查询
# 实现SQL中的where功能，包括
#
# filter过滤出多个结果
# exclude排除掉符合条件剩下的结果
# get过滤单一结果
# 模型类名.objects.filter（属性名___运算符=值）   获取n个结果
# 模型类名.objects.exclude（属性名___运算符=值）   获取n个结果
# 模型类名.objects.get（属性名___运算符=值）   获取1个结果 或者异常

# 查询编号为1的图书
book = BookInfo.objects.get(id=1)  # 简写形式 （属性名=值）
book = BookInfo.objects.get(id__exact=1)  # 完整形式 (id__exact=1)

BookInfo.objects.get(pk=1)  # primary key == pk
BookInfo.objects.get(id=1)  # 对象
BookInfo.objects.filter(id=1)  # 列表[对象，]
# 查询书名包含'湖'的图书
# 查询书名以'部'结尾的图书
# 查询书名为空的图书
# 查询编号为1或3或5的图书
# 查询编号大于3的图书
# 查询1980年发表的图书
# 查询1990年1月1日后发表的图书
