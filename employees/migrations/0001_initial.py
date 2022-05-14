# Generated by Django 4.0.4 on 2022-05-09 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('patronymic', models.CharField(max_length=20)),
                ('position', models.TextField(max_length=100)),
                ('employment_date', models.DateField()),
                ('salary', models.IntegerField()),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.employee')),
            ],
        ),
    ]
