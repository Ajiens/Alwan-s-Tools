import re
import numpy as np

def tupleRelasi(input):
    if input == "0":
        return {0}
    
    element = re.findall(r'\d+|[a-z]|[A-Z]', input)
    tup_list = set()
    
    if len(element) % 2 != 0:
        print(f"\n{element[-1]}Tidak berpasangan.")
        print("Pastikan semua himpunan relasi yang dimasukan memiliki pasangannya.\n")
        return False
    
    for i in range(0, len(element), 2):
        tup_list.add((element[i], element[i+1]))
    return tup_list

def generateMatriks(relasi, domain, kodomain):
    matriks = np.zeros((len(domain), len(kodomain)), dtype=int)
    #Element Matriks: (d,k)
    for i, dom in enumerate(domain):
        baris = []
        print("|", end=" ")
        for j, kod in enumerate(kodomain):
            if tuple(f"{dom}{kod}") in relasi:
                matriks[i][j] = 1
                relasi.remove(tuple(f"{dom}{kod}"))
                print(1, end=f" ")
            else:
                matriks[i][j]= 0
                print(0, end=" ")
        print("|")

    if len(relasi) != 0:
        print(f"\nNOTE: {relasi} tidak berada di dalam Matriks karena berada di luar Domain dan Kodomain.\n")
    
    return matriks

def isRefleksif(matriks):
    for i, baris in enumerate(matriks):
        if baris[i] != 1:
            return False
    return True

def isIrrefleksif(matriks):
    for i, baris in enumerate(matriks):
        if baris[i] != 0:
            return False
    return True

def isSimetri(matriks):
    for i in range(len(matriks)):
        for j in range(len(matriks[i])):
            if i != j: #Antidiagonal
                if matriks[i][j] != matriks[j][i]:
                    return False
    return True

def isAntisimetri(matriks):
    for i in range (len(matriks)):
        for j in range (len(matriks[i])):
            if i != j: #Antidiagonal
                if matriks[i][j] == 1 and matriks[j][i] == 1:
                    return False
    return True

def isAsimetris(matriks):
    if isIrrefleksif(matriks) and isAntisimetri(matriks):
        return True
    return False

def isTransitif(matriks):
    indeks = np.argwhere(matriks == 1) #Cari mana aja yang value == 1
    for i, j in indeks:
        for k in range(matriks.shape[1]):
            if matriks[j][k] == 1 and matriks[i][k] != 1:
                return False
    return True
        
def cekSifat(matriks):
    print(" =========== Sifat Dari Matriks ===========")
    print("    Refleksif:", "✔" if isRefleksif(matriks) else "✘", "    Antisimetri:", "✔" if isAntisimetri(matriks) else "✘")
    print("    Irrefleksif:", "✔" if isIrrefleksif(matriks) else "✘", "  Asimetris:", "✔" if isAsimetris(matriks) else "✘")
    print("    Simetri:", "✔" if isSimetri(matriks) else "✘", "      Transitif: ", "✔" if isTransitif(matriks) else "✘")
    print(" ==========================================\n")

def __main__():
    while True:
        print("Masukan AxB, dimana A adalah Domain dan B adalah Kodomain ('exit' to exit)")
        domain = str(input("Masukan A (Domain): "))
        if "exit" in domain: exit()

        kodomain = str(input("Masukan B (Kodomain): "))
        if "exit" in kodomain: exit()

        domain = set(re.findall(r'\d+|[a-z]|[A-Z]', domain)) # Make sure gaada double element
        kodomain = set(re.findall(r'\d+|[a-z]|[A-Z]', kodomain))
        if len(domain) != len(kodomain):
            print(f"Domain[{len(domain)}] dan Kodomain[{len(kodomain)}] panjangnya harus sama (Matriks Persegi). Coba Lagi!\n")
            continue
        
        while True:
            input_user = str(input("Masukan Himpunan ('reset' to ReSet Domain n Kodomain): "))
            if input_user == "reset":
                domain = set()
                kodomain = set()
                break

            himpunan = tupleRelasi(input_user)
            if himpunan != False:
                domain_sort = sorted(list(domain)) #Make sure elemnt terurut
                kodomain_sort = sorted(list(kodomain))
                print("Domain: ", domain_sort)
                print("Kodomain: ", kodomain_sort)
                print("Himpunan: ", himpunan)
                matriks = generateMatriks(himpunan, domain_sort, kodomain_sort)
                cekSifat(matriks)
        
__main__() #aowkwaok