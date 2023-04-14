# a,b,c dimana a^b mod c

# Algoritma :
# b dijadiin biner
# tentukan awalan, x = =, dan power = a mod c
# diproses 
# terus sampe biner abis

def destobin(desimal, biner = ""):
    '''Mengubah bilangan desimal (int) ke bentuk biner (str)'''
    # byte = desimal % 2 #sisa bagi
    sisa_bagi = str(desimal%2)

    if desimal == 0:
        return biner[::-1]

    hasil_bagi = desimal // 2
    return destobin(hasil_bagi, biner+sisa_bagi)

def modexp(a,b,c):
    '''Input berupa 3 buah int (a, b, dan c) dimana return berupa hasil a^b mod c'''
    biner = list(destobin(b))

    power = a % c # a mod c
    x = 1 
    print(f" Bin |           POWER           |  X  ")
    print("-----|---------------------------|------")
    for index, bin in enumerate(biner[::-1]): # biner dibalik, mulai enumerasi dari yg kecil
        calc_power = f"{power}^2"
        if int(bin) != 0: # x berubah
            x = (x*power) % c
        # else: x tetap
        power = (power ** 2) % c

        str_pow = f"({calc_power}) mod {c} = {power} "
        if index == len(biner)-1:
            str_pow = "STOP"
        print(f"{bin:^5s}|{str_pow:^27s}|{x:^5d}")
        
    return x

print("100% handmade yang dibuat dengan cinta ❤️\n")
while True:
    a,b,c = input("Masukan a, b, dan c, dimana a^b mod c: ").split()
    try:
        print("Hasil =", modexp(int(a), int(b), int(c)))
    except:
        print("Ouch Salah. Coba Lagi")