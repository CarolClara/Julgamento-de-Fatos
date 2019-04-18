# Generated by Django 2.1.8 on 2019-04-08 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='GroupStudent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jf_academic.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('course', models.ManyToManyField(to='jf_academic.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60, unique=True)),
                ('program', models.ManyToManyField(to='jf_academic.Program')),
            ],
        ),
    ]
