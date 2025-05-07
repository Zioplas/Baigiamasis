class Payout:
    def __init__(self, payouts):
        self.payouts = payouts

    def check_for_payout(self, bet, symbols):
        if symbols[0] == symbols[1] == symbols[2]:
            return bet * self.payouts.get(symbols[0])

        elif symbols[0] == symbols[1] or symbols[0] == symbols[2]:
            return bet * (self.payouts.get(symbols[0]) / 2)

        elif symbols[1] == symbols[2]:
            return bet * (self.payouts.get(symbols[1]) / 2)

        else:
            return 0

