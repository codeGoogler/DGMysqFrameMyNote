# Generated by Django 2.2 on 2019-04-16 09:31

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btitle', models.CharField(max_length=20)),
                ('bpub_date', models.DateTimeField(db_column='pub_date')),
                ('breadnum', models.IntegerField(default=0)),
                ('bcomment', models.IntegerField()),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'djbookinfo',
            },
            managers=[
                ('bookManager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=10)),
                ('hgender', models.BooleanField(default=False)),
                ('hcontent', models.CharField(max_length=1000)),
                ('isDelete', models.BooleanField(default=False)),
                ('book', models.ForeignKey(on_delete='on_delete=models.CASCADE()', to='BookApp.BookInfo')),
            ],
            options={
                'db_table': 'djheroinfo',
            },
        ),
    ]