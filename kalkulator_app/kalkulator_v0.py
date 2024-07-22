while True:
    number1=float(input("Masukan angka pertama: "))
    operaation1=input("Masukkan operasi (+,-,*,/): ")
    number2=float(input("Masukkan angka kedua: "))

    if operaation1=="+":
        result = number1+number2
    elif operaation1=="-":
        result = number1-number2
    elif operaation1=="*":
        result = number1*number2
    elif operaation1=="/":
        result = number1/number2
    else:
        result = "Operasi tidak valid"

    print("Hasil: ", result)
