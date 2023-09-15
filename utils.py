
class utils():
    def reversed(self, x: int) -> int:
        assert isinstance(x, int)
        ret = 0
        while x != 0:
            digit = x % 10
            ret = 10 * ret + digit
            x = int(x / 10)
        return ret

    def formatter(self, x: int) -> tuple[int, int]:
        assert isinstance(x, int)
        biny = 0
        octal = 0

        # compute binary
        x_bin = x
        digit_mult = 1
        while x_bin != 0:
            digit = x_bin % 2
            x_bin = int(x_bin / 2)
            biny += digit_mult * digit
            digit_mult *= 10

        # compute octal
        x_octal = x
        digit_mult = 1
        while x_octal != 0:
            digit = x_octal % 8
            x_octal = int(x_octal / 8)
            octal += digit_mult * digit
            digit_mult *= 10

        return biny, octal
