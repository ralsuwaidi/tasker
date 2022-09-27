# Generated by Django 3.2.15 on 2022-09-27 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_alter_task_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_private',
            field=models.BooleanField(default=False, help_text='Hide the task so only the owner and the assignee can view it', verbose_name='private task'),
        ),
    ]