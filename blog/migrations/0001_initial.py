# Generated by Django 2.2.7 on 2019-11-21 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField(default='test')),
                ('pub_date', models.DateTimeField()),
                ('image', models.ImageField(upload_to='images/')),
                ('summary', models.CharField(max_length=250)),
            ],
        ),
    ]
