

class WhiteListError(Exception):
    def __init__(self, bad = 0):
        if bad:
            self.message = f'{bad} is not currently in our list of allowed functions! Please contact the dev team to have it added'
        else:
            self.message = 'This function is not currently allowed! Please contact the dev team to have it added'

class BlackListError(Exception):
    def __init__(self, bad = 0):
        if bad:
            self.message = f'\'{bad}\' is a banned keyword/function for WolfBot. Contact my dev team if you think this is a mistake'
        else:
            self.message = 'You\ve typed a banned phrase, so we cannot evaluate this code right now!'
