# Generated by Django 4.0.8 on 2022-12-08 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0016_company_type_company_value_duration_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='company',
            name='companies_company_value_matches_type',
        ),
        migrations.RemoveConstraint(
            model_name='company',
            name='companies_company_CompanyType_valid',
        ),
        migrations.RemoveField(
            model_name='company',
            name='type',
        ),
        migrations.RemoveField(
            model_name='company',
            name='value_duration',
        ),
        migrations.RemoveField(
            model_name='company',
            name='value_points',
        ),
    ]
