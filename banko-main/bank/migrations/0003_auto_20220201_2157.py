# Generated by Django 3.2.5 on 2022-02-01 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_alter_customerdetails_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_data', models.CharField(default='none', max_length=50)),
                ('receiver_data', models.CharField(default='none', max_length=50)),
                ('amount_data', models.IntegerField(default='none')),
            ],
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='email',
            field=models.EmailField(default='none', max_length=254, unique=True),
        ),
    ]