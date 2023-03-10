# Generated by Django 2.2.27 on 2022-07-20 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20220226_2004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newname', models.CharField(max_length=150, unique=True)),
                ('img_1', models.ImageField(upload_to='picture_2')),
                ('desc_2', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
