from django.db import migrations


def load_roles(apps, schema_editor):
    Role = apps.get_model("users", "Role")

    role_superadmin = Role(id=1, name='IS_SUPERADMIN')
    role_superadmin.save()

    role_admin = Role(id=2, name='IS_ADMIN')
    role_admin.save()

    role_learner = Role(id=3, name='IS_LEARNER')
    role_learner.save()

    role_instructor = Role(id=4, name='IS_INSTRUCTOR')
    role_instructor.save()


def delete_roles(apps, schema_editor):
    Role = apps.get_model("users", "Role")
    Role.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_roles, delete_roles),
    ]
