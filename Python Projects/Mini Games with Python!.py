import random

def guess(x):
    nomorAcak = random.randint(1, x)
    tebakan = 0

    while tebakan != nomorAcak:
        try:
            tebakan = int(input(f'Tebak Angka di antara angka 1 dan {x}: '))
            if tebakan < nomorAcak:
                print('Salah, naikin dikit :(')
            elif tebakan > nomorAcak:
                print('Salah, rendahin angkanya :P')
        except ValueError:
            print("Masukkan angka yang valid!")

    print(f'Yay, bener! nomornya {nomorAcak}.')
    again(guess, x)

def computerTebak(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            tebakan = random.randint(low, high)
        else:
            tebakan = low

        feedback = input(f'Aku tebak... {tebakan}!\nGimana? Angkanya.. (h) ketinggian, (l) kerendahan, (c) benar: ').lower()
        if feedback == 'h':
            high = tebakan - 1
        elif feedback == 'l':
            low = tebakan + 1
        elif feedback != 'c':
            print("Input tidak valid. Gunakan 'h', 'l', atau 'c'.")

    print(f'Yay, {tebakan} bener!')
    again(computerTebak, x)

def again(fungsi_game, x):
    while True:
        pilih = input('Mau ganti game? [y/n]: ').lower()
        if pilih == 'y':
            main()
            break
        elif pilih == 'n':
            fungsi_game(x)
            break
        else:
            print('Input tidak dikenali. Coba lagi.')

def main():
    while True:
        print("=" * 38)
        print("| Welcome to my Mini Games Projects! |")
        print("| 1. Guess UR Number                 |")
        print("| 2. Guess MY Number                 |")
        print("| 3. Keluar                          |")
        print("|         (\\__/)                     |")
        print("|        ( •ㅅ• )                    |")
        print("|        /_____\\                     |")
        print("=" * 38)

        try:
            opsi = int(input('Masukkan opsi (1/2/3): '))
            if opsi == 1:
                guess(20)
            elif opsi == 2:
                computerTebak(20)
            elif opsi == 3:
                print("Terima kasih telah bermain, byebye! ❤️")
                exit()
            else:
                print("Opsi tidak tersedia.")
        except ValueError:
            print("Masukkan angka 1, 2, atau 3!")

main()
