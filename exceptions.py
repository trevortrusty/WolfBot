

class WhiteListError(Exception):
    def __init__(self, bad = 0):
        if bad:
            self.message = f'{bad} is not currently in our list of allowed functions! Please contact the dev team to have it added by joining our support server: https://discord.gg/eyd376A'
        else:
            self.message = 'This function is not currently allowed! Please contact the dev team to have it added'

class BlackListError(Exception):
    def __init__(self, bad = 0):
        if bad:
            self.message = f'\'{bad}\' is a banned keyword/function for WolfBot. Contact the dev team at https://discord.gg/eyd376A if you think this is a mistake'
        else:
            self.message = 'You\ve typed a banned phrase, so we cannot evaluate this code right now!'

class BadQuery(Exception):
    pass