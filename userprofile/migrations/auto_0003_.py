from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20190826_1127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='avatar',
            new_name='profile_image',
        ),
        migrations.AddField(
            model_name='profile',
            name='cover_image',
            field=models.ImageField(default='avatars/cover.png', upload_to='avatars'),
        ),
    ]
