from htmlparser import HtmlParser
parser = HtmlParser("https://bank.gov.ua/")
parser.NbuParse('div', 'index-page')
print(parser.Result)
digit = float(input("Enter digit: "))
print(digit / parser.Result[3])