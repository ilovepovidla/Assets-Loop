import os
from typing import Optional, List, Dict, Any

from crypto_exchanges.crypto_exchanges_registration.binance import \
    BinanceP2PParser

from core.parsers import BankParser

BANK_NAME = os.path.basename(__file__).split('.')[0].capitalize()

RAIFFEISEN_CURRENCIES = (
    'USD', 'EUR', 'RUB', 'GBP'
)


class RaiffeisenParser(BankParser):
    bank_name: str = BANK_NAME
    endpoint: str = ('https://www.raiffeisen.ru/oapi/currency_rate/get'
                     '/?source=RCONNECT&currencies=USD,EUR,GBP')
    all_values: bool = True

    def extract_all_values_from_json(self, json_data: dict
                                     ) -> Optional[List[Dict[str, Any]]]:
        if not json_data:
            return
        value_lst = []
        data = json_data['data']
        rates = data['rates'][0]
        main_currency = rates['code']
        exchanges = rates['exchange']
        for exchange in exchanges:
            second_currency = exchange['code']
            buy = exchange['rates']['buy']['value']
            sell = exchange['rates']['sell']['value']
            value_lst.append(
                {
                    'from_fiat': main_currency,
                    'to_fiat': second_currency,
                    'price': 1 / sell
                }
            )
            value_lst.append(
                {
                    'from_fiat': second_currency,
                    'to_fiat': main_currency,
                    'price': buy
                }
            )
        return value_lst

    def get_all_api_answers(self) -> None:
        values = self.choice_buy_and_sell_or_price()
        if not values:
            return
        for value_dict in values:
            price = value_dict.pop('price')
            self.add_to_bulk_update_or_create(value_dict, price)


class RaiffeisenBinanceP2PParser(BinanceP2PParser):
    bank_name: str = BANK_NAME