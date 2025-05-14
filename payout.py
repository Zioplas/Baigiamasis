import os
class Payout:
    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.payouts = {
            os.path.join(base_dir, "pictures", "dollar.png"): 10,
            os.path.join(base_dir, "pictures", "bar.png"): 8,
            os.path.join(base_dir, "pictures", "cherries.png"): 6,
            os.path.join(base_dir, "pictures", "lemon.png"): 5,
            os.path.join(base_dir, "pictures", "seven.png"): 20,
            os.path.join(base_dir, "pictures", "watermelon.png"): 4,
        }

    def check_for_payout(self, bet, symbols):
        if symbols[0] == symbols[1] == symbols[2]:
            return bet * self.payouts.get(symbols[0])

        elif symbols[0] == symbols[1] or symbols[0] == symbols[2]:
            return bet * (self.payouts.get(symbols[0]) / 2)

        elif symbols[1] == symbols[2]:
            return bet * (self.payouts.get(symbols[1]) / 2)

        else:
            return 0

