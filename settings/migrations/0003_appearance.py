# Generated by Django 3.0.5 on 2020-05-19 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_biomodel_currentuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='appearance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currentuser', models.CharField(max_length=50)),
                ('colortheme', models.CharField(max_length=50)),
            ],
        ),
    ]
