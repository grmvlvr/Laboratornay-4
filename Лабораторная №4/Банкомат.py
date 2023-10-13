from num2words import num2words

def name_valuta(summa):
    if 10 < summa % 100 < 20:
        return "рублей"
    elif summa % 10 == 1:
        return "рубль"
    elif 2 <= summa % 10 <= 4:
        return "рубля"
    else:
        return "рублей"
    
def proverka (summa):
    try:
        summa = int(summa)
        if summa < 1 or summa > 100000:
            raise ValueError
        return True
    except ValueError:
        return False

def perevod_v_slova(summa):
    words = num2words(summa, lang='ru')
    name2_valuta = name_valuta(summa)
    return f"{words} {name2_valuta}"
    
def main():
    while True:
        summa = input("Введите сумму выдачи в банкомате (от 1 до 100000): ")
        if proverka(summa):
            summa = int(summa)
            break
        else:
            print("Некорректный ввод. Пожалуйста, введите число от 1 до 100000.")

    perevod_summa = perevod_v_slova(summa)
    print(perevod_summa)

if __name__ == "__main__":
    main()
