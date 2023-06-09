# Generated by Django 4.2.1 on 2023-05-28 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_question_question_num_quiz_num_questions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=300)),
                ('token', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=300)),
                ('total_qn', models.IntegerField(default=0)),
                ('answered_qn', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=300)),
                ('token', models.CharField(max_length=8)),
                ('isexpired', models.BooleanField(default=False)),
            ],
        ),
    ]
