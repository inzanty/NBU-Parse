import requests
import settings


def main():
    response = requests.get(
        "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=" + settings.currency + "&json")
    currency = response.json()[0]['txt']
    rate = response.json()[0]['rate']
    exchangeDate = response.json()[0]['exchangedate']
    print("Валюта: " + currency)
    print("Курс: " + str(rate))
    print("Дата: " + exchangeDate)


main()
