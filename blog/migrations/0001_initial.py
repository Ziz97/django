# Generated by Django 2.1 on 2019-03-09 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastName', models.CharField(max_length=20)),
                ('firstName', models.CharField(max_length=20)),
                ('phoneNumber', models.CharField(max_length=10)),
                ('firm', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('startDate', models.DateTimeField()),
                ('endDate', models.DateTimeField()),
                ('client', models.ManyToManyField(to='blog.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abstract', models.TextField()),
                ('duration', models.IntegerField()),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Client')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Project')),
            ],
        ),
    ]