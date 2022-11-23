print("Hello CodeSandbox!")


def verifyPerfectNumbers(number):
    value = 0
    for x in range(1, number):
        if x % 2 == 0:
            value += x

    print(f'Number {number} is {"" if number == value else "not"} perfect')


print(verifyPerfectNumbers(7))


def verifyNumbersAreFriends(a, b):
    divA, divB = 0, 0
    for i in range(1, a):
        if a % i == 0:
            divA += i
    for j in range(1, b):
        if b % j == 0:
            divB += j
    print(
        f'Numbers {a} and {b} are {"" if divA == b and a == divB else "not"} friends')


verifyNumbersAreFriends(1184, 1211)


def verifyIfNumberIsCool(number):
    value = 0
    isCool = False
    for x in range(1, number):
        value += x
        if number == value:
            isCool = True
            break
    print(f'This number {number} is {"" if isCool else "not"} cool')


verifyIfNumberIsCool(15)
