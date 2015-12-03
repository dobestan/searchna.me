import os

from django.conf import settings
from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand

from items.models import Item

import pandas


class Command(BaseCommand):
    help = "Install Item fixture(s) in the database."

    def add_arguments(self, parser):
        parser.add_argument(
            '--src',
            type=str,
        )

    def handle(self, *args, **options):

        items_dir = os.path.join(
            settings.PROJECT_ROOT,
            'data',
            'items',
        )
        src_files = []

        if options['src']:
            src_file = os.path.join(
                items_dir,
                options['src'],
            )

            src_files.append(src_file)

        else:
            src_files = [
                os.path.join(items_dir, filename)
                for filename
                in os.listdir(items_dir)
            ]

        for src_file in src_files:
            slug = src_file.split('/')[-1].split('.')[0]
            site = Site.objects.get(name=slug)

            self.stdout.write("Start loading items of <Site: {site_domain}> from {src_file}.".format(
                site_domain=site.domain,
                src_file=src_file,
            ))

            df = pandas.read_csv(src_file)

        for index, row in df.iterrows():
            item, item_created = site.item_set.get_or_create(
                name=row['name'],
            )
            site.slug = row['slug']
            site.save()

        self.stdout.write("Successfully Loaded {items_count} items of <Site: {site_domain}>.".format(
            items_count=site.item_set.count(),
            site_domain=site.domain,
        ))
