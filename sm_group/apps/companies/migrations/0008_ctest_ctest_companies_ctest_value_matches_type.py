# Generated by Django 4.0.8 on 2022-12-08 21:10

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0007_country_country_companies_country_value_matches_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='CTest',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('type', models.IntegerField(choices=[(1, 'Points'), (2, 'Duration')])),
                ('value_points', models.IntegerField(null=True)),
                ('value_duration', models.DurationField(null=True)),
            ],
        ),
        migrations.AddConstraint(
            model_name='ctest',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('type', 1), ('value_duration__isnull', True), ('value_points__isnull', False)), models.Q(('type', 2), ('value_duration__isnull', False), ('value_points__isnull', True)), _connector='OR'), name='companies_ctest_value_matches_type'),
        ),
    ]
