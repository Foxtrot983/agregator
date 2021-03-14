import requests
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from agreg_app.models import Values


class Command(BaseCommand):
    help = "collect values"

    def handle(self, *args, **options):
        url = 'https://myfin.by/currency/minsk'
        site = requests.get(url, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}).text
        soup = BeautifulSoup(site, 'html.parser')
        postings = soup.find('div', class_='table-responsive').find('tbody').find_all('tr')
        for p in postings:
            # time.sleep(8)
            name = p.find('a').text
            value_buy = p.find('td').next_sibling.next_sibling.text
            value_sell = p.find('td').next_sibling.next_sibling.next_sibling.next_sibling.text
            value_nb = p.find('td').next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text
            try:
                Values.objects.create(
                    name=name,
                    value_buy=value_buy,
                    value_sell=value_sell,
                    value_nb=value_nb)
                print(name, ' added')
            except:
                print(name, 'already exists')

        self.stdout.write('Job done')
