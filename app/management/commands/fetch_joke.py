import requests
from django.core.management.base import BaseCommand
from app.models import Joke 

class Command(BaseCommand):
    help = 'Pobiera jeden losowy żart z API i zapisuje go w bazie danych'

    def handle(self, *args, **options):
        url = "https://official-joke-api.appspot.com/random_joke"

        try:
            # Wysyłamy zapytanie do API
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Zgłosi błąd, jeśli API zwróci np. kod 404 lub 500
            
            data = response.json()

            # Wyciągamy interesujące nas dane z odpowiedzi JSON
            joke_id = data.get('id')
            setup = data.get('setup')
            punchline = data.get('punchline')

            # 'get_or_create' szuka rekordu po unikalnym 'joke_id'.
            # Jeśli go nie ma - tworzy nowy z wartościami z 'defaults'.
            # Zapobiega to powstawaniu duplikatów, gdy API wylosuje to samo.
            joke, created = Joke.objects.get_or_create(
                joke_id=joke_id,
                defaults={
                    'setup': setup,
                    'punchline': punchline
                }
            )

            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Pomyślnie dodano nowy żart o ID {joke_id}!')
                )
                self.stdout.write(f'Pytanie: "{setup}"')
                self.stdout.write(f'Odpowiedź: "{punchline}"')
            else:
                self.stdout.write(
                    self.style.WARNING(f'Żart o ID {joke_id} już istnieje w bazie. Spróbuj uruchomić komendę ponownie.')
                )

        except requests.RequestException as e:
            # Obsługa błędów sieciowych (np. brak internetu, API nie działa)
            self.stdout.write(
                self.style.ERROR(f'Wystąpił błąd podczas pobierania danych z API: {e}')
            )