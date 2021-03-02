from random import choice


DICE = {
    "d4": [x for x in range(1, 4 + 1)],
    "d6": [x for x in range(1, 6 + 1)],
    "d8": [x for x in range(1, 8 + 1)],
    "d10": [x for x in range(1, 10 + 1)],
    "d12": [x for x in range(1, 12 + 1)],
    "d20": [x for x in range(1, 20 + 1)],
    "d100": [x for x in range(1, 100+1)]
}


# UNIVERSAL RESULT OBJECT
class result:
    """ represents the final result with many options for output """

    def __init__(self, rolls, mods=[], d_type="d6"):
        self.d_type = d_type
        if max(rolls) > int(d_type.replace('d', '')):
            raise ValueError("Die result too high for this die type")
        elif min(rolls) < 1:
            raise ValueError("Die result <= 0 not acceptable.")
        self.rolls = rolls
        self.mods = mods

    @property
    def sums(self):
        return sum(self.rolls) + sum(self.mods)

    @property
    def successes(self):
        # don't use mods
        m_val = int(self.d_type.replace("d", ""))
        return self.rolls.count(m_val)

    @property
    def failures(self):
        # don't use mods
        return self.rolls.count(1)

    def __repr__(self):
        return str(self.rolls)


# STANDARD DIE ROLLER
class Unidie:
    """ This is the object for making standard die casts """
    # calls simple die calls like d4 or 12d6+5

    def __init__(self, code, qty=1, mods=[]):
        self.code = code
        self.qty = qty
        self.mods = mods

    def die_roll(self):
        """ rolls simple codes with any qty of 1 die type and a list of mods """
        if self.code in DICE:
            return result([int(choice(DICE[self.code])) for x in range(self.qty)], self.mods, self.code)
        else:
            print("Fucked")


# FORBIDDEN LANDS DIE POOL ROLLER
class Pool_die:
    """ this is the object for rolling die pools for some systems """
    # outputs are based on successess from a dice pool

    def __init__(self, code, qty=1):
        self.code = code
        self.qty = qty

    def die_roll(self):
        """ rolls dice pools of 1 die type and returns counts of successes """
        if self.code in DICE:
            return result([int(choice(DICE[self.code])) for x in range(self.qty)], d_type=self.code)
        else:
            print("Fucked")


class Forbidden(Pool_die):
    """ rolls dice pools of d6 only and returns counts of successes """

    def __init__(self, qty=1):
        # only use d6's in this game system.
        self.code = "d6"
        self.qty = qty

    def d66(self):
        """ a specific type of roll to Forbidden Lands called a d66 like a d% but only with digits up to 6 """
        l_digit = int(choice(DICE['d6']))
        r_digit = int(choice(DICE['d6']))
        s_result = f"{l_digit}{r_digit}"
        i_result = int(s_result)
        return result([i_result], d_type="d66")


class Savage(Unidie):
    def __init__(self, d_code, qty=1, mods=[]):
        self.code = d_code
        self.qty = qty
        self.mods = mods

    def die_roll(self):
        """ rolls simple codes with any qty of 1 die type and a list of mods """
        if self.code in DICE:
            x = result([int(choice(DICE[self.code]))
                        for x in range(self.qty)], self.mods, self.code)
            for i in x.rolls:
                # this is for exploding dice. if any rolls turned up max, then
                # roll again and add to total.
                d_max = self.code.replace("d", "")

                if i == int(d_max):
                    x.rolls.append(int(choice(DICE[self.code])))
            return x
        else:
            print("Fucked")


if __name__ == '__main__':
    pass
# TEST_DICE = {"d4", "d6", "d8", "d10", "d12", "d20"}
#
# for d_code in TEST_DICE:
#     m_val = int(d_code.replace('d', ''))
#     test_pool = Pool_die(d_code, 5)
#
#     for x in range(5):
#         test_roll = test_pool.die_roll()
#         print("\n", d_code, test_roll)
#         print(
#             f"successes: {test_roll.successes} == counts {test_roll.rolls.count(m_val)}. <--- {test_roll.successes == test_roll.rolls.count(m_val)}")
#         print(
#             f"fails    : {test_roll.failures} == counts {test_roll.rolls.count(m_val)}.")
