class absentyException(Exception):
    pass


def tax(salary, absent):
    if absent >= 10:
        raise absentyException
    t = salary * 21 / 100
    n = salary - t
    print("TAX", t)
    print("SALARY", n)


try:
    tax(1000, 5)
except absentyException:
    print("Too many absences")
