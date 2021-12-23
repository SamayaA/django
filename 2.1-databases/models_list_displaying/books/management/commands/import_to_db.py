import json

from django.core.management.base import BaseCommand
from django.db import IntegrityError
from books.models import Book



class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        '''
        import data from json file to DB
        '''
        with open('fixtures/books.json', 'r', encoding='UTF-8') as file:
            books = json.load(file)

        for book in books:
            try:
                p = Book.objects.create(name=book["fields"]["name"],\
                     author=book["fields"]["author"], pub_date=book["fields"]["pub_date"])
            except IntegrityError:
                print(f"Book already in the list")

