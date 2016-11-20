from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html

class Student(models.Model):
    class Meta:
        verbose_name = '学生信息'
        verbose_name_plural = '学生信息'

    GENDER_CHOICE = (
        ('u', u'保密'),
        ('m', u'男'),
        ('f', u'女'),
    )

    name = models.CharField(u'姓名', max_length=50)
    age = models.IntegerField(u'年龄', blank=True, null=True)
    gender = models.CharField(u'性别', max_length=10, choices=GENDER_CHOICE, blank=True, null=True)
    birthdate = models.DateField(u'出生日期', blank=True, null=True)
    studentID = models.CharField(u'学号', max_length=50, unique=True)
    add_time = models.DateTimeField(u'添加时间', auto_now_add=True)
    edit_time = models.DateTimeField(u'最后编辑时间', auto_now=True)
    add_user = models.ForeignKey(User, verbose_name=u'添加者')
    friends = models.ManyToManyField('self', verbose_name=u'好友', blank=True)
    school = models.CharField(u'在读学校', max_length=100, blank=True, null=True)
    major = models.CharField(u'在读专业', max_length=100, blank=True, null=True)
    admission = models.DateField(u'入学时间', blank=True, null=True)
    gpa = models.FloatField(u'成绩', blank=True, null=True)
    mobile = models.IntegerField(u'联系电话')
    email = models.EmailField(u'电子邮箱')
    color_code = models.CharField(u'名字颜色', max_length=6, default='FF0000')

    def colored_name(self):
        return format_html('<span style="color: #{};">{}</span>',
                           self.color_code,
                           self.name)
    colored_name.short_description = '姓名状态'
    colored_name.admin_order_field = 'name'
    colored_name.allow_tags = True

    def __str__(self):
        return '%s (%s)' % (self.name, self.studentID)


class Parent(models.Model):
    class Meta:
        verbose_name = '家庭成员'
        verbose_name_plural = '家庭成员'
    RELATION_CHOICE= (
        ('f', u'父亲'),
        ('m', u'母亲'),
        ('o', u'其他'),
    )
    name = models.CharField(u'姓名', max_length=50)
    add_time = models.DateTimeField(u'添加时间', auto_now_add=True)
    mobile = models.IntegerField(u'联系电话', blank=True, null=True)
    relation = models.CharField(u'关系', choices=RELATION_CHOICE, max_length=10, blank=True, null=True)
    student = models.ForeignKey(Student, verbose_name='办理学生')
# Create your models here.
