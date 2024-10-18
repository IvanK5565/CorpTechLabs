from currency_converter import CurrencyConverter, SINGLE_DAY_ECB_URL

class Controller:
    c = 0

    def __init__(self):
        self.c = CurrencyConverter()

    def get_currencies(self):
        return self.c.currencies

    def input(self, value: str, from_format: str, to_format: str, callback):
        result = 0
        if str.isnumeric(value):
            int_value = float(value)
            result = self.c.convert(int_value, from_format, to_format)
            result = str(result)
        else:
            result = "error input"
        callback(result)
