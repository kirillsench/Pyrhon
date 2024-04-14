import sqlite3
from htmlparser import HtmlParser
from logger import Logger
from bs4 import BeautifulSoup
from datetime import datetime
import requests

logger = Logger(filename='loger.log')


def create_tables_if_not_exist():
    try:
        conn = sqlite3.connect('weatherandmoney.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS WeatherKyiv
                     (id INTEGER PRIMARY KEY,
                      date_time TEXT,
                      temperature TEXT)''')

        c.execute('''CREATE TABLE IF NOT EXISTS CurrencyExchange
                     (id INTEGER PRIMARY KEY,
                      date_time TEXT,
                      exchange_rate REAL)''')

        conn.commit()
        conn.close()
        logger.log_info('The tables have been successfully created or already exist')
    except Exception as e:
        logger.log_error(f'Error creating tables: {e}')
        raise


def get_temperature():
    try:
        url = "https://sinoptik.ua/погода-киев"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        temperature = soup.find(class_="temperature").get_text().strip()
        return temperature
    except Exception as e:
        logger.log_error('Error getting weather data: {}'.format(e))
        raise


def insert_data(table_name, *data):
    try:
        conn = sqlite3.connect('weatherandmoney.db')
        c = conn.cursor()
        placeholders = ','.join(['?'] * len(data))
        c.execute(f"INSERT INTO {table_name} VALUES ({placeholders})", data)
        conn.commit()
        conn.close()
        logger.log_info(f'Success {table_name}: {data}')
    except Exception as e:
        logger.log_error(f'Error entering data into the table {table_name}: {e}')
        raise


def main():
    try:
        create_tables_if_not_exist()

        print("Choose option:")
        print("1. Дізнатись погоду у Києві")
        print("2. Конвертація валют")

        option = int(input("Choose (1/2): "))

        if option == 1:
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            temperature = get_temperature()
            insert_data('WeatherKyiv', None, current_datetime, temperature)
            print("Weather data entered successfully.")

        elif option == 2:
            parser = HtmlParser("https://bank.gov.ua/")
            parser.NbuParse('div', 'index-page')
            print(parser.Result)
            digit = float(input("Enter the amount to convert: "))
            converted_amount = digit / parser.Result[3]
            print("Converted:", converted_amount)
            print("Succesfully , check the database")
            insert_data('CurrencyExchange', None, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), converted_amount)
            logger.log_info('Currency conversion: {}, {}'.format(datetime.now(), converted_amount))

        else:
            print("Wrong choice. Choose 1 or 2.")

    except ValueError:
        logger.log_error('Invalid input. Please choose the correct option.')
    except Exception as e:
        logger.log_error('Error: {}'.format(e))


if __name__ == "__main__":
    main()