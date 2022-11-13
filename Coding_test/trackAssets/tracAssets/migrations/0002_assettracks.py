# Generated by Django 4.1.3 on 2022-11-13 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracAssets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetTracks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('take_out_time', models.DateField()),
                ('return_time', models.DateField()),
                ('return_condition', models.CharField(max_length=20)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracAssets.assettype')),
                ('taken_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracAssets.employee')),
            ],
            options={
                'verbose_name_plural': 'Asset_Track',
                'db_table': 'asset_track',
                'managed': True,
            },
        ),
    ]