from http import HTTPStatus
from itertools import combinations
from typing import List

import requests


class BankParser(object):
    FIATS = None
    ENDPOINT = None
    MODEL = None

    def generate_unique_params(self) -> List[dict[str]]:
        fiats = [fiat[0] for fiat in self.FIATS]  # repackaging choices into a list
        fiats_combinations = tuple(combinations(fiats, 2))  # 2: currency pair
        params_list = [dict([('from', params[0]), ('to', params[-1])])
                       for params in fiats_combinations]
        # repackaging a list with tuples into a list with dicts
        return params_list


    def get_api_answer(self, params):
        """Делает запрос к единственному эндпоинту API.
        Яндекс.Практикума.
        """
        try:
            response = requests.get(self.ENDPOINT, params)
        except Exception as error:
            message = f'Ошибка при запросе к основному API: {error}'
            raise Exception(message)
        if response.status_code != HTTPStatus.OK:
            message = f'Ошибка {response.status_code}'
            raise Exception(message)
        return response.json()

    def extract_buy_and_sell_from_json(self, json_data):
        pass

    def get_all_api_answers(self):
        for params in self.generate_unique_params():
            print(self.extract_buy_and_sell_from_json(self.get_api_answer(params)))


