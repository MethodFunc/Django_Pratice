class YearConverter:
    regex = r'\d{3,4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return "%04d" % value


class MonthConverter(YearConverter):
    regex = r'\d{1,2}'


class DayConverter(YearConverter):
    regex = r'[0123]\d'
