# Generated by Django 3.2.7 on 2021-11-04 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_executor_id_task_executor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='tag',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='users.tag'),
        ),
    ]
