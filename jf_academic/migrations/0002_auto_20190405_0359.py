# Generated by Django 2.1.7 on 2019-04-05 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jf_academic', '0001_initial'),
        ('jf_judgment_facts', '0001_initial'),
        ('jf_account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupstudent',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jf_account.Student'),
        ),
        migrations.AddField(
            model_name='group',
            name='judgment_facts',
            field=models.ManyToManyField(to='jf_judgment_facts.JudgmentFacts'),
        ),
        migrations.AddField(
            model_name='group',
            name='student',
            field=models.ManyToManyField(to='jf_account.Student'),
        ),
        migrations.AddField(
            model_name='course',
            name='group',
            field=models.ManyToManyField(to='jf_academic.Group'),
        ),
    ]