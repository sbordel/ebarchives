# Generated by Django 2.1.4 on 2019-01-06 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebarchivesweb', '0004_event_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='email',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='last_name',
        ),
        migrations.AddField(
            model_name='event',
            name='description_fr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='title_fr',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='recurringevent',
            name='description_fr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recurringevent',
            name='title_fr',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]