# Generated by Django 2.1.7 on 2019-05-01 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0005_auto_20190501_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='judgment_facts',
            field=models.ManyToManyField(blank=True, to='judgment_facts.JudgmentFacts'),
        ),
    ]
