# coding=utf-8

from finance import FinancialStatus


class Player:
    def __init__(self, name):
        self.name = name  # The name of the player
        self.finance = FinancialStatus()
        self.xp = 100

    def _list_assets(self):
        if self.finance.assets.__len__() > 0:
            print('Your assets')
            print('-----------')
            for asset in self.player.finance.assets:
                print('%s - %s - %s - %s' % (asset.name, asset.description, asset.value, asset.rent))
        else:
            print('You currently have no assets.')
