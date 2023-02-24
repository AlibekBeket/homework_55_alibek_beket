# Generated by Django 4.1.6 on 2023-02-14 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list', '0002_alter_todo_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(blank=True, null=True, verbose_name='Дата выполнения'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.TextField(default=1, max_length=1000, verbose_name='Описание'),
        ),
    ]