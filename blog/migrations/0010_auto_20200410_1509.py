# Generated by Django 2.2.7 on 2020-04-10 15:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='active',
            new_name='approved_comment',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.CharField(default='viewer', max_length=200),
        ),
        migrations.AddField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
