# Generated by Django 3.0.5 on 2020-07-31 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_content_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='tags',
            field=models.ManyToManyField(blank=True, to='Main.Tag'),
        ),
    ]
