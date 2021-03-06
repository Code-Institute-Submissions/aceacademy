# Generated by Django 2.2.14 on 2020-08-27 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0024_auto_20200828_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='education_level',
            field=models.CharField(choices=[('lower_primary', 'Lower Primary'), ('upper_primary', 'Upper Primary'), ('lower_secondary', 'Lower Secondary'), ('upper_secondary', 'Upper Secondary'), ('junior_college', 'JC')], default='Junior College', max_length=100),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='syllabus',
            field=models.CharField(choices=[('psle', 'PSLE'), ('o_level', 'GCSE O Level'), ('a_level', 'GCSE A Level')], default='A Level', max_length=100),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='tags',
            field=models.CharField(choices=[('primary_math', 'Primary Mathematics'), ('a_math', 'Additional Mathematics'), ('e_math', 'Elementary Mathematics'), ('h1_math', 'H1 Mathematics'), ('h2_math', 'H2 Mathematics')], default='H2_math', max_length=100),
        ),
    ]
