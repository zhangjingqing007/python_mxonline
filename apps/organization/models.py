# -*- encodeing:utf-8 -*-
from datetime import datetime

from django.db import models

# Create your models here.
#课程机构
class CityDict(models.Model):
    name = models.CharField(max_length = 20, verbose_name = u"城市")
    desc = models.TextField(max_length = 200,verbose_name = u"描述")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"城市"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.name
    


class CouresOrg(models.Model):
    name = models.CharField(max_length = 50, verbose_name = u"机构名称")
    desc = models.TextField(verbose_name = u"机构描述")
    category = models.CharField(default="pxjg", verbose_name=u"机构类别", max_length=20, choices=(("pxjg","培训机构"),("gr","个人"),("gx","高校")))
    click_num = models.IntegerField(default=0,verbose_name=u"点击数")
    fav_num = models.IntegerField(default=0, verbose_name=u"收藏人数")
    students = models.IntegerField(default=0, verbose_name=u"学习人数")
    course_num = models.IntegerField(default=0, verbose_name=u"课程数")
    image = models.ImageField(upload_to="org/%y/%m", verbose_name=u"封面")
    address = models.CharField(max_length = 50, verbose_name = u"机构地址")
    city = models.ForeignKey(CityDict,verbose_name =u"所在城市")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程机构"
        verbose_name_plural = verbose_name    
    
    def get_teacher_nums(self):
        #获取课程机构的教师数量
        return self.teacher_set.all().count()

    def get_coures_nums(self):
        #获取课程数量
        return self.coures_set.all().count()        
    
    def __str__(self):
        return self.name
    

class Teacher(models.Model):
    org = models.ForeignKey(CouresOrg,verbose_name=u"所属机构")
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name=u"logo", max_length=100,null=True, blank=True)
    name = models.CharField(max_length = 50, verbose_name = u"教师名")
    work_years = models.IntegerField(default=0,verbose_name=u"工作年限")
    work_company = models.CharField(max_length = 50, verbose_name = u"就职公司")
    work_position = models.CharField(max_length = 50, verbose_name = u"公司职位")
    points = models.CharField(max_length = 100, verbose_name = u"教学特点")
    click_num = models.IntegerField(default=0,verbose_name=u"点击数")
    fav_num = models.IntegerField(default=0, verbose_name=u"收藏人数")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"教师"
        verbose_name_plural = verbose_name

    def get_coures_num(self):
        return self.coures_set.all().count()

    def __str__(self):
        return self.name