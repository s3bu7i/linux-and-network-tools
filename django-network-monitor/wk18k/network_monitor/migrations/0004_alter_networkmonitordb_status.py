# Generated by Django 4.2.5 on 2023-09-07 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network_monitor', '0003_alter_networkmonitordb_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networkmonitordb',
            name='status',
            field=models.CharField(auto_created=True, default='400', max_length=100),
        ),
    ]