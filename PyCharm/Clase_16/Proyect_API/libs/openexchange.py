import requests
from cachetools import cached, TTLCache


class OpenExchangeClient:
    BASE_URL = 'https://openexchangerates.org/api'

    def __init__(self, app_id):
        self.app_id = app_id

    @property
    @cached(cache=TTLCache(maxsize=2, ttl=1800)) # esto retiene el request al server y lo demora 1800 segundos, ya que el servidor actualiza 1 vez poro hpra
    def latest(self):
        return requests.get(f'{self.BASE_URL}/latest.json?app_id={self.app_id}').json()

    def convert(self, from_amount, from_currency, to_currency):
        rates = self.latest['rates']
        to_rate = rates[to_currency]

        if from_currency == 'USD':
            return from_amount * to_rate
        else:
            from_in_usd = from_amount / rates[from_currency]
            return from_in_usd * to_rate
