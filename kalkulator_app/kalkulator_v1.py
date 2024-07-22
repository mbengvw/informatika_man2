def get_user_input():
    number1=float(input("Masukan angka pertama: "))
    operaation1=input("Masukkan operasi (+,-,*,/): ")
    number2=float(input("Masukkan angka kedua: "))
    return number1, operaation1, number2

def calculate(number1, operaation1, number2):
    if operaation1=="+":
        return number1+number2
    elif operaation1=="-":
        return number1-number2
    elif operaation1=="*":
        return number1*number2
    elif operaation1=="/":
        return number1/number2
    else:
        return "Operasi tidak valid"

def display_result(result):
    print("Hasil: ", result)


def main():
    number1, operaation1, number2=get_user_input()
    result=calculate(number1, operaation1, number2)
    

if __name__=="__main__":
    main()