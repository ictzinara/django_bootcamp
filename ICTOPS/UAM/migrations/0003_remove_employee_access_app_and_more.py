# Generated by Django 4.1.1 on 2022-09-18 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("UAM", "0002_applications_employee_agent_employee_department_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="employee_access", name="app",),
        migrations.AddField(
            model_name="applications",
            name="employee_access",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="UAM.employee_access",
            ),
            preserve_default=False,
        ),
    ]
