nano monitor_enp0s3.py <<< Buat file baru Dengan nama ini pada LINUX DEVASC-LABVM
import subprocess
import time

# --- Konfigurasi ---
INTERFACE = "enp0s3"        # Nama interface jaringan yang akan dimonitor
PING_TARGET = "8.8.8.8"     # IP tujuan untuk uji konektivitas (Google DNS)
RETRY_LIMIT = 3             # Batas jumlah gagal ping sebelum interface dinonaktifkan


def check_ping(target):
    """Cek konektivitas jaringan dengan satu kali ping."""
    result = subprocess.run(
        ["ping", "-c", "1", "-W", "2", target],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return result.returncode == 0  # True jika ping sukses, False jika gagal


def disable_network(interface):
    """Matikan interface jaringan tertentu."""
    subprocess.run(["sudo", "ip", "link", "set", interface, "down"])
    print(f"[!] Interface {interface} telah di-disable karena gagal koneksi.")


def main():
    print(f"Memantau koneksi jaringan pada interface {INTERFACE}...")
    failure_count = 0

    while True:
        if check_ping(PING_TARGET):
            print(f"[OK] {INTERFACE} aktif dan koneksi ke {PING_TARGET} sukses.")
            failure_count = 0  # Reset jika ping berhasil
        else:
            failure_count += 1
            print(f"[X] Gagal ping ke {PING_TARGET} ({failure_count}/{RETRY_LIMIT})")

        # Jika gagal melebihi batas, disable interface
        if failure_count >= RETRY_LIMIT:
            disable_network(INTERFACE)
            break  # Hentikan program setelah interface dimatikan

        time.sleep(5)  # Jeda 5 detik sebelum ping ulang


if __name__ == "__main__":
    main()
jalankan pada Terminal DEVASC-VM >>> sudo python3 monitor_enp0s3.py
