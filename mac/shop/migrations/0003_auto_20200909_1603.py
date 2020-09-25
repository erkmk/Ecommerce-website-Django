# Generated by Django 3.1 on 2020-09-09 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200904_1247'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=70)),
                ('phone', models.CharField(default='', max_length=70)),
                ('desc', models.CharField(default='', max_length=700)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=2000),
        ),
    ]
