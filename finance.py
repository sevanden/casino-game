# coding=utf-8


class FinancialStatus():
    """
        The financial status of the player.
    """
    def __init__(self):
        self.cash   = 0                                                                                                 # Our player will initially start with no cash
        self.assets = []                                                                                                # Our player will initially start with no assets

    def income(self):
        income = 0
        for owned in self.assets:
            income = income + int(owned.rent)
        return income

    def __str__(self):
        cash_line   = 'Cash: %d' % self.cash
        income_line = 'Income: %d' % self.income()
        return '%s - %s' % (cash_line, income_line)
