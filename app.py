# Versi Clean Code
INVENTARIS_TOKO = {
    "Buku": 50,
    "Pena": 10,
    "Penghapus": 3,
    "Penggaris": 15
}

BATAS_STOK_MINIMUM = 5

def ambil_data_stok(nama_item: str) -> int:
    """Mengambil jumlah stok berdasarkan nama item (Case-insensitive)."""
    return INVENTARIS_TOKO.get(nama_item.capitalize())

def tampilkan_laporan_stok(nama_item: str):
    """Menampilkan informasi stok ke layar dengan peringatan jika kritis."""
    jumlah = ambil_data_stok(nama_item)

    if jumlah is None:
        print(f"\n[!] Barang '{nama_item}' tidak ditemukan.")
        return

    print(f"\n--- LAPORAN STOK: {nama_item.upper()} ---")
    print(f"Status: Tersedia ({jumlah} unit)")
    
    if jumlah < BATAS_STOK_MINIMUM:
        print("⚠️ PERINGATAN: Stok berada di bawah batas minimum!")

# Alur Utama
if __name__ == "__main__":
    print("=== SISTEM MANAJEMEN INVENTARIS ===")
    input_user = input("Cek Nama Barang: ")
    tampilkan_laporan_stok(input_user)