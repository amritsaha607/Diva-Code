# Generated by Django 2.1.4 on 2019-01-19 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dis_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='excercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ex_name', models.CharField(max_length=50)),
                ('anim', models.FileField(blank=True, null=True, upload_to='')),
                ('dis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choice_set', to='Excercise.disease')),
            ],
        ),
    ]
