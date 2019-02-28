def can_string_be_float(user_value):

    dozvoljeni_karakteri = ['0','1','2','3','4','5','6','7','8','9','.']

    for ch in user_value:

        if ch not in dozvoljeni_karakteri:
            return False

        broj_tacaka = 0

        for ch in user_value:
            if ch == '.':
                broj_tacaka = broj_tacaka + 1

        if broj_tacaka > 1:
            return False

    return True

def main():

    user_value= (input("Unesite duzinu u kilometrima: "))

    if can_string_be_float(user_value):
        print("Duzina u miljama je: ", float(user_value) * 0.6214)
    else:
        print("Vas unos nije validan.")

main()