from django.db import models

# Create your models here.
"""
1.模型类 需要继承models.Model
2.定义属性
    id 默认会生成
    属性名=models.类型（选项）
    2.1属性名对应就是字段名
        不要使用python和mysql的关键字
        不要使用连续的下划线（__）
    2.2 类型 mysql的类型
    2.3 选项 是否有默认值，是否唯一，是否为null
            CharField 必须设置max_length
            verbose_name 主要是admin站点使用
3. 改变表的名称
    默认表名称是：子应用名_类名 都是小写
    修改表的名字 
create table `qq_user`(
    id int,
    name varchar(20) not nul default ''
)
"""


class BookInfo(models.Model):
    name = models.CharField(max_length=10, unique=True)
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'bookinfo'
        verbose_name = 'book'

    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    # 定义一个有序字典
    GENDER_CHOICE = (
        (1, 'male'),
        (2, 'female')
    )

    name = models.CharField(max_length=10, unique=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=1)
    description = models.CharField(max_length=100, null=True)
    is_delete = models.BooleanField(default=False)

    # 外键
    # 系统会自动为外键添加_id
    # 外键的级联操作
    # 主表和从表
    # 1对多 书籍对人物
    # 主表的数据删除了，从表的数据该怎么办呢
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物'
