# Generated by Django 3.2.12 on 2022-02-20 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcastcontentindexpage',
            name='rss_omit_previews',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True, help_text='Should preview episodes be omitted from your RSS feed? They will still appear on the website index page. This should probably be used in conjunction with the option to omit episode numbers from your RSS feed.', verbose_name='Omit previews'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='podcastcontentindexpage',
            name='rss_preview_text',
            field=models.CharField(blank=True, help_text='Freeform. This will be prepended to episodes flagged as previews of paid content if you include previews in your feed. Ex: "PREVIEW--"', max_length=50, null=True, verbose_name='Preview prefix'),
        ),
    ]