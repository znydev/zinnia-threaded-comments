# Generated by Django 2.0.7 on 2018-09-03 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zinnia-threaded-comments', '0003_auto_20180903_0240'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='threadedcomment',
            options={'ordering': ['tree_id', 'lft']},
        ),
    ]
