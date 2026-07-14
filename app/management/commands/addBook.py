from django.core.management.base import BaseCommand
from django.db.models import F
from app.models import Book 

class Command(BaseCommand):
    help = 'Zwiększa ilość (quantity) wszystkich książek o 1'

    def handle(self, *args, **options):
        # Aktualizujemy wszystkie książki jednym zapytaniem SQL
        updated_rows = Book.objects.update(quantity=F('quantity') + 1)

        self.stdout.write(
            self.style.SUCCESS(f'Pomyślnie zwiększono ilość dla {updated_rows} książek!')
        )