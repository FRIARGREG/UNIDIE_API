import pytest
import dice


def test_dice_result_class():
    """
    result.d_type = d_type
    result.rolls = rolls
    result.mods = mods
    """
    test_result = dice.result([5, 2, 3])
    assert test_result.d_type == 'd6'
    assert type(test_result.mods) is list
    assert max(test_result.rolls) <= 6


def test_dice_result_max_values():

    with pytest.raises(ValueError) as excinfo:
        test_result = dice.result([5, 2, 3], d_type="d4")
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "Die result too high for this die type"

    with pytest.raises(ValueError) as excinfo:
        test_result = dice.result([5, 7, 3], d_type="d6")
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "Die result too high for this die type"

    with pytest.raises(ValueError) as excinfo:
        test_result = dice.result([5, 2, 9], d_type="d8")
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "Die result too high for this die type"

    with pytest.raises(ValueError) as excinfo:
        test_result = dice.result([5, 2, 19], d_type="d12")
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "Die result too high for this die type"


def test_dice_result_min_values():
    with pytest.raises(ValueError) as excinfo:
        test_result = dice.result([-1, 2, 10], d_type="d12")
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "Die result <= 0 not acceptable."

    with pytest.raises(ValueError) as excinfo:
        test_result = dice.result([0, 2, 19], d_type="d20")
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "Die result <= 0 not acceptable."


def test_dice_result_sums():
    test_result = dice.result([5, 2, 3])
    assert test_result.sums is 10

    test_result = dice.result([1, 3])
    assert test_result.sums is 4


def test_dice_result_sums_with_mods():
    test_result = dice.result([5, 2, 3], mods=[2])
    assert test_result.sums is 12

    test_result = dice.result([5, 2, 3], mods=[2, -4])
    assert test_result.sums is 8


def test_dice_result_successes_d4():
    test_result = dice.result([1, 2, 3], d_type="d4")
    assert test_result.successes == 0
    test_result = dice.result([4, 2, 3, 1, 4], d_type="d4")
    assert test_result.successes == 2


def test_dice_result_successes_d6():
    test_result = dice.result([5, 2, 3])  # default to d6
    assert test_result.successes == 0
    test_result = dice.result([5, 6, 2, 3, 6, 6])  # default to d6
    assert test_result.successes == 3


def test_dice_result_successes_d8():
    test_result = dice.result([5, 2, 3], d_type="d8")
    assert test_result.successes == 0
    test_result = dice.result([8, 3, 2], d_type="d8")
    assert test_result.successes == 1


def test_dice_result_successes_d10():
    test_result = dice.result([5, 2, 3], d_type="d10")
    assert test_result.successes == 0
    test_result = dice.result([10, 10, 10, 3], d_type="d10")
    assert test_result.successes == 3


def test_dice_result_successes_d12():
    test_result = dice.result([5, 2, 3], d_type="d12")
    assert test_result.successes == 0
    test_result = dice.result([5, 8, 2, 10, 3, 12], d_type="d12")
    assert test_result.successes == 1


def test_dice_result_successes_d20():
    test_result = dice.result([5, 2, 3], d_type="d20")
    assert test_result.successes == 0
    test_result = dice.result([5, 20, 2, 20, 19, 12], d_type="d20")
    assert test_result.successes == 2


def test_dice_result_failures():
    test_result = dice.result([4, 2, 3], d_type="d4")
    assert test_result.failures == 0
    test_result = dice.result([4, 1, 2, 3, 3, 1], d_type="d4")
    assert test_result.failures == 2


def test_dice_universal_roller_base():
    test_uni = dice.Unidie("d4")
    for x in range(50):
        test_result = test_uni.die_roll()
        assert test_result.sums <= 4

    test_uni = dice.Unidie("d8")
    for x in range(50):
        test_result = test_uni.die_roll()
        assert test_result.sums <= 8

    test_uni = dice.Unidie("d12")
    for x in range(50):
        test_result = test_uni.die_roll()
        assert test_result.sums <= 12

    test_uni = dice.Unidie("d100")
    for x in range(50):
        test_result = test_uni.die_roll()
        assert test_result.sums <= 100


def test_dice_universal_roller_base_with_mods():
    test_mods_single = [1]  # +1
    test_mods_multi = [1, 2, 3]  # +6
    test_mods_mixed = [1, 2, -3, -1]  # -1

    test_uni = dice.Unidie("d4", mods=test_mods_single)
    for x in range(20):
        test_result = test_uni.die_roll()
        assert 2 <= test_result.sums <= 5

    test_uni = dice.Unidie("d6", mods=test_mods_multi)
    for x in range(20):
        test_result = test_uni.die_roll()
        assert 7 <= test_result.sums <= 12

    test_uni = dice.Unidie("d8", mods=test_mods_single)
    for x in range(20):
        test_result = test_uni.die_roll()
        assert 2 <= test_result.sums <= 9

    test_uni = dice.Unidie("d10", mods=test_mods_mixed)
    for x in range(20):
        test_result = test_uni.die_roll()
        assert 0 <= test_result.sums <= 9

    test_uni = dice.Unidie("d12", mods=test_mods_single)
    for x in range(20):
        test_result = test_uni.die_roll()
        assert 2 <= test_result.sums <= 13

    test_uni = dice.Unidie("d20", mods=test_mods_mixed)
    for x in range(20):
        test_result = test_uni.die_roll()
        assert 0 <= test_result.sums <= 19

    test_uni = dice.Unidie("d100", mods=test_mods_single)
    for x in range(20):
        test_result = test_uni.die_roll()
        assert 2 <= test_result.sums <= 101


def test_dice_universal_roller_multiple_rolls():
    test_uni = dice.Unidie("d4", qty=3)
    for x in range(50):
        test_result = test_uni.die_roll()
        assert max(test_result.rolls) <= 4

    test_uni = dice.Unidie("d6", qty=3)
    for x in range(50):
        test_result = test_uni.die_roll()
        assert max(test_result.rolls) <= 6

    test_uni = dice.Unidie("d8", qty=3)
    for x in range(50):
        test_result = test_uni.die_roll()
        assert max(test_result.rolls) <= 8

    test_uni = dice.Unidie("d10", qty=3)
    for x in range(50):
        test_result = test_uni.die_roll()
        assert max(test_result.rolls) <= 10

    test_uni = dice.Unidie("d12", qty=3)
    for x in range(50):
        test_result = test_uni.die_roll()
        assert max(test_result.rolls) <= 12

    test_uni = dice.Unidie("d100", qty=3)
    for x in range(50):
        test_result = test_uni.die_roll()
        assert max(test_result.rolls) <= 100


def test_dice_universal_roller_multiple_rolls_mods():
    test_mods = [1, 2, -3]  # = 0

    test_uni = dice.Unidie("d4", qty=3, mods=test_mods)
    for x in range(50):
        test_result = test_uni.die_roll()
        assert max(test_result.rolls) <= 4

    test_uni = dice.Unidie("d6", qty=3, mods=test_mods)
    for x in range(50):
        test_result = test_uni.die_roll()
        assert max(test_result.rolls) <= 6

    test_uni = dice.Unidie("d8", qty=3, mods=test_mods)
    for x in range(50):
        test_result = test_uni.die_roll()
        assert max(test_result.rolls) <= 8

    test_uni = dice.Unidie("d10", qty=3, mods=test_mods)
    for x in range(50):
        test_result = test_uni.die_roll()
        assert max(test_result.rolls) <= 10

    test_uni = dice.Unidie("d12", qty=3, mods=test_mods)
    for x in range(50):
        test_result = test_uni.die_roll()
        assert max(test_result.rolls) <= 12

    test_uni = dice.Unidie("d100", qty=3, mods=test_mods)
    for x in range(50):
        test_result = test_uni.die_roll()
        assert max(test_result.rolls) <= 100


def test_dice_universal_Savage_exploder():
    # Savage Worlds uses the standard dice roller but includes an interesting
    # mechanic called EXPLODING where if the die roll is MAXED ie a 6 on d6,
    # you can keep that result and roll again, appending the new roll to your
    # result. EXPLODING has no cap. a 1d6 roll could result in scores of 50+.
    #
    # we've already tested the UNI roller so we're just going to
    # check the exploding mechanic
    DICE = {"d4", "d6", "d8", "d10", "d12"}

    for d_code in DICE:
        test_die = dice.Savage(d_code)
        m_val = int(d_code.replace('d', ''))

        for x in range(50):
            test_rolls = test_die.die_roll()
            assert len(test_rolls.rolls) == 1 + test_rolls.rolls.count(m_val)


def test_dice_pool_roller():
    # Dice pools are where you roll multiple dice of one type and count how many
    # MAXED and how many rolled 1's or FAILED. the more dice you roll, the higher
    # the chance of either happening.
    DICE = {"d4", "d6", "d8", "d10", "d12", "d20"}

    for d_code in DICE:
        m_val = int(d_code.replace('d', ''))
        test_pool = dice.Pool_die(d_code, 5)

        for x in range(20):
            test_roll = test_pool.die_roll()
            assert test_roll.successes == test_roll.rolls.count(m_val)
            assert test_roll.failures == test_roll.rolls.count(1)


def test_dice_pool_forbidden_d66():
    '''
    Forbidden Lands uses a simple dice pool roller that we already made,
    but this game has a special die called the d66 which only uses digits
    from 1 to 6 for both 10's and 1's column. Like a percentile but weird.
    '''

    test_dice = dice.Forbidden()
    for x in range(50):
        test_roll = test_dice.d66()
        str_result = str(test_roll.rolls.pop())
        assert 1 <= int(str_result[0]) <= 6
        assert 1 <= int(str_result[1]) <= 6
