# Generated by Django 3.1.6 on 2021-02-07 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Ссылка')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
