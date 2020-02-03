# Quianna Mortimer
# EC500: HW 1
# this is my python code that converts Arabic numbers to Roman numerals


def arb2rom(arb):
# check if input is a number
    if not(isinstance(arb, int)):
        print("not a number")
        return ''
# check if input is less than 4000
    if  arb > 3999:
        print("this number is out of range (1-3999)")
        return ''

    ar_list = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    rom_list = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]

    rom = ''

    i = 12
    while arb > 0:
        r = arb // ar_list[i]
        arb = arb % ar_list[i]
        while r > 0:
                r -= 1
                rom += rom_list[i]
        i -= 1
    return rom
