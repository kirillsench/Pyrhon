from htmlparser import HtmlParser
from logger import Logger
import datetime

try:
    logger = Logger(filename='moneylog.log')
    parser = HtmlParser("https://bank.gov.ua/")
    parser.NbuParse('div', 'index-page')
    print(parser.Result)
    digit = float(input("Enter digit: "))
    converted_amount = digit / parser.Result[3]
    print("Converted:", converted_amount)
    # Logging the conversion details
    logger.log_info('Details: Date: {}, Amount: {}'.format(datetime.datetime.now(), converted_amount))
except Exception as e:
    logger.log_error('Error: {}'.format(e))