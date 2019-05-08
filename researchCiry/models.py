from django.db import models
from tinymce.models import HTMLField


# Create your models here.

# https://www.cnblogs.com/hwtmhj/p/6995379.html
#自关联
class AreaInfo(models.Model):
    title = models.CharField(max_length=20)
    parea = models.ForeignKey('self','on_delete=models.CASCADE()',null=True,blank=True)



class MyModel(models.Model):
     content = HTMLField('正文')



# """
# class AreaInfo(models.Model):
#     title = models.CharField(max_length=20)
#     lng = models.DecimalField(max_digits=12, decimal_places=8)
#     lat = models.DecimalField(max_digits=12, decimal_places=8)
#     level = models.CharField(max_length=10)
#     parent_adcode = models.CharField(max_length=10)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#     parea = models.ForeignKey('self','on_delete=models.CASCADE()',null=True,blank=True)
#
# """


"""
# CREATE TABLE `researchciry_areainfo` (
#   `parea_id` char(6) COLLATE utf8_unicode_ci NOT NULL,
#   `title` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
#   `lng` decimal(12,8) unsigned NOT NULL,
#   `lat` decimal(12,8) unsigned NOT NULL,
#   `level` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
#   `parent_adcode` char(6) COLLATE utf8_unicode_ci NOT NULL,
#   `created_at` timestamp NULL DEFAULT NULL,
#   `updated_at` timestamp NULL DEFAULT NULL,
#   PRIMARY KEY (`adcode`),
#   KEY `tbl_districts_parent_adcode_index` (`parent_adcode`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
# 
# 
# SELECT * FROM `researchciry_areainfo`;
# 
# 
# alter TABLE researchciry_areainfo ADD PRIMARY KEY(id)
# 
# SELECT adcode,name,parent_adcode FROM areainfo
# SELECT adcode,name ,parent_adcode FROM areainfo WHERE parent_adcode != 0
# SELECT p.adcode,p.name ,p.parent_adcode FROM areainfo  as p WHERE parent_adcode != 0
# create table researchciry_areainfo2(
# id int PRIMARY KEY,
# title VARCHAR(20),
# parea_id int,
# FOREIGN KEY(parea_id) REFERENCES researchciry_areainfo(id)
# )
# 
# alter table researchciry_areainfo MODIFY parea_id   FOREIGN KEY(parea_id) REFERENCES researchciry_areainfo(id)
# 
# DROP table researchciry_areainfo
# create table researchciry_areainfo(
# id int PRIMARY KEY,
# title VARCHAR(20),
# parea_id int
# )
# 
# INSERT INTO researchciry_areainfo(id,title,parea_id)SELECT p.adcode,p.name ,p.parent_adcode FROM areainfo  as p WHERE parent_adcode != 0
# INSERT INTO researchciry_areainfo(id,title)SELECT p.adcode,p.name  FROM areainfo  as p WHERE parent_adcode = 0
# 
# INSERT INTO researchciry_areainfo(id,title,parea_id)SELECT adcode,name,parent_adcode FROM areainfo
# 
# show create table researchciry_areainfo
# show create table researchciry_areainfo2
# 
# CREATE TABLE `researchciry_areainfo` (
#   `id` int(11) NOT NULL,
#   `title` varchar(20) DEFAULT NULL,
#   `parea_id` int(11) DEFAULT NULL,
#   PRIMARY KEY (`id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8
# 
# CREATE TABLE `researchciry_areainfo2` (
#   `id` int(11) NOT NULL,
#   `title` varchar(20) DEFAULT NULL,
#   `parea_id` int(11) DEFAULT NULL,
#   PRIMARY KEY (`id`),
#   KEY `parea_id` (`parea_id`),
#   CONSTRAINT `researchciry_areainfo2_ibfk_1` FOREIGN KEY (`parea_id`) REFERENCES `researchciry_areainfo2` (`id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8
"""