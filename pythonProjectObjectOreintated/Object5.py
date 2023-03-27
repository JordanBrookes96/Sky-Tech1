class One:
    A = 20
    B = 30

    def message(self):
        print("Jordan Is The Greatest!!")


class Two(One):
    C = 56
    D = 97


class Three(Two):
    E = 89


ref = Three()
print(ref.A)
print(ref.B)
print(ref.C)
print(ref.D)
print(ref.E)
ref.message()
