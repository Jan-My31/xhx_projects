# Generated by Django 2.2.2 on 2021-02-25 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fileslist',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Id')),
                ('uid', models.CharField(max_length=50, verbose_name='uid')),
                ('file_id', models.CharField(max_length=500, verbose_name='文件id')),
                ('file_name', models.CharField(max_length=500, verbose_name='文件名称')),
                ('info_text', models.CharField(max_length=500, verbose_name='公告名称')),
                ('info_url', models.CharField(max_length=500, verbose_name='公告url')),
            ],
            options={
                'verbose_name_plural': '文件信息',
                'db_table': 'files_list',
            },
        ),
        migrations.CreateModel(
            name='Infolist',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Id')),
                ('info_text', models.CharField(max_length=100, verbose_name='公告名称')),
                ('info_id', models.CharField(max_length=100, verbose_name='查询ID')),
                ('info_type', models.CharField(max_length=100, verbose_name='公告类型')),
                ('info_market', models.CharField(max_length=100, verbose_name='所属市场')),
                ('info_date', models.DateField(max_length=50, verbose_name='发布时间')),
                ('info_link', models.URLField(unique=True, verbose_name='公告链接')),
                ('info_detail', models.TextField(verbose_name='公告详情')),
                ('update_time', models.CharField(max_length=50, verbose_name='更新日期')),
                ('create_time', models.CharField(max_length=50, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '公告列表',
                'verbose_name_plural': '公告列表',
                'db_table': 'infos_list',
                'ordering': ['-info_date'],
            },
        ),
    ]
