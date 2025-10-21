Pastikan kamu sudah di terminal DEVASC LabVM, lalu buat file baru: nano nslookup_tool.py

import socket

def forward_lookup(domain):
    """Mencari alamat IP dari nama domain"""
    try:
        ip = socket.gethostbyname(domain)
        print(f"[+] Domain: {domain}")
        print(f"    IP Address: {ip}\n")
    except socket.gaierror:
        print(f"[X] Tidak dapat menemukan IP untuk domain: {domain}\n")

def reverse_lookup(ip_address):
    """Mencari nama domain dari alamat IP"""
    try:
        host = socket.gethostbyaddr(ip_address)
        print(f"[+] IP Address: {ip_address}")
        print(f"    Domain Name: {host[0]}\n")
    except socket.herror:
        print(f"[X] Tidak dapat menemukan domain untuk IP: {ip_address}\n")

def main():
    print("=== NSLOOKUP TOOL SEDERHANA ===")
    print("1. Lookup domain → IP")
    print("2. Lookup IP → domain")
    pilihan = input("Pilih (1/2): ")

    if pilihan == "1":
        domain = input("Masukkan nama domain (contoh: mahasiswa.pcr.ac.id): ")
        forward_lookup(domain)
    elif pilihan == "2":
        ip = input("Masukkan IP address (contoh: 8.8.8.8): ")
        reverse_lookup(ip)
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()

Ketik di terminal: python3 nslookup_tool.py

Hasil output yang didapat akan berbentuk seperti ini

=== NSLOOKUP TOOL SEDERHANA ===
1. Lookup domain → IP
2. Lookup IP → domain
Pilih (1/2): 1
Masukkan nama domain (contoh: mahasiswa.pcr.ac.id): mahasiswa.pcr.ac.id
[+] Domain: mahasiswa.pcr.ac.id
    IP Address: 103.102.xxx.xxx
    
Dan kalau kita pili 2 hasilnya >

Pilih (1/2): 2
Masukkan IP address (contoh: 8.8.8.8): 8.8.8.8
[+] IP Address: 8.8.8.8
    Domain Name: dns.google
