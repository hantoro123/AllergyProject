# Generated by Django 4.1.3 on 2022-12-08 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchapp', '0004_alter_userdata_rnum'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='prdlstReportNo',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
