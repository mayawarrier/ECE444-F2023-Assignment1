import utils

util = utils.utils()

def test_util(func, inp, desc):
    try:
        print(desc + ":", func(inp))
    except:
        print("Failed to compute " + desc)


test_util(util.reversed, "hello", "reversed('hello')")
test_util(util.reversed, 0.25, "reversed(0.25)")
test_util(util.reversed, 1234, "reversed(1234)")

test_util(util.formatter, "hello", "formatter('hello')")
test_util(util.formatter, 0.25, "formatter(0.25)")
test_util(util.formatter, 1234, "formatter(1234)")
