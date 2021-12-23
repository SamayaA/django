import sys

import csv

from django.core.management.base import BaseCommand
from django.db import IntegrityError
from phones.models import Phone



class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        '''
        import data from csv file to DB
        '''
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            try:
                p = Phone.objects.create(id=phone['id'], name=phone['name'],\
                    image=phone['image'], price=phone['price'],\
                        release_date=phone['release_date'], \
                            lte_exists=phone['lte_exists'],\
                                slug=phone['name'].replace(' ','-'))
            except IntegrityError:
                print(f"Value id={phone['id']} exist")

