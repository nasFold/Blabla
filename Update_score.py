import requests

def update_score(skor, waktu, pencetak_gol):
    url = "http://your_username.000webhostapp.com/update-score"  # Ganti dengan alamat web Flask Anda
    payload = {"skor": skor, "waktu": waktu, "pencetakGol": pencetak_gol}
    response = requests.post(url, json=payload)
    return response.json()

# Contoh penggunaan
skor_baru = "1-0"
waktu_baru = "30:00"
pencetak_gol_baru = "Player A"

result = update_score(skor_baru, waktu_baru, pencetak_gol_baru)
print(result)
