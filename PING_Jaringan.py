nano ping_dashboard1.py < File baru di Linux Devasc-Labvm dan isi dengan codingan dibawah ini
from flask import Flask, render_template_string, jsonify
import os
import platform
import time
from datetime import datetime
import threading

app = Flask(__name__)

TARGET = "mahasiswa.pcr.ac.id"
PING_RESULT = {"status": "Menunggu...", "latency": "-", "time": "-"}

# Template HTML langsung di dalam kode
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Monitoring Jaringan - mahasiswa.pcr.ac.id</title>
    <meta http-equiv="refresh" content="5">
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; background-color: #f5f5f5; }
        h1 { color: #2c3e50; }
        .card { background: white; display: inline-block; padding: 30px; border-radius: 15px; box-shadow: 0 2px 8px rgba(0,0,0,0.2); }
        .status-ok { color: green; font-weight: bold; }
        .status-fail { color: red; font-weight: bold; }
        .akun { font-size: 20px; font-weight: bold; color: #0077cc; margin-bottom: 10px; }
    </style>
</head>
<body>
    <h1>Monitoring Koneksi ke mahasiswa.pcr.ac.id</h1>
    <div class="card">
        <p class="akun">AKUN MAHASISWA PCR CHRISTIAN</p>
        <p><strong>Waktu:</strong> {{time}}</p>
        <p><strong>Status:</strong> 
            {% if status == 'OK' %}
                <span class="status-ok">Terhubung</span>
            {% else %}
                <span class="status-fail">Gagal Terhubung</span>
            {% endif %}
        </p>
        <p><strong>Latency:</strong> {{latency}}</p>
    </div>
    <p style="margin-top: 20px; color: gray;">Halaman akan diperbarui otomatis setiap 5 detik</p>
</body>
</html>
"""

def ping_host():
    """Melakukan ping dan update hasil ke variabel global"""
    global PING_RESULT
    while True:
        param = "-n 1" if platform.system().lower() == "windows" else "-c 1"
        command = f"ping {param} {TARGET}"
        response = os.popen(command).read()

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if "time=" in response.lower() or "ttl=" in response.lower():
            # Ambil waktu ping (latency)
            try:
                latency = response.split("time=")[1].split(" ")[0]
            except:
                latency = "N/A"
            PING_RESULT = {"status": "OK", "latency": latency, "time": now}
        else:
            PING_RESULT = {"status": "FAIL", "latency": "-", "time": now}

        time.sleep(3)  # jeda 3 detik antar ping

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE, **PING_RESULT)

@app.route("/data")
def data():
    return jsonify(PING_RESULT)

if __name__ == "__main__":
    # Jalankan thread ping di latar belakang
    threading.Thread(target=ping_host, daemon=True).start()
    print(f"Server berjalan di http://localhost:5000")
    app.run(host="0.0.0.0", port=5000)
setelah itu save CTRL X + CTRL O Dan jalankan codingan menggunakan >
python3 ping_dashboard1.py
buka pada CHROME LINUX DEVASC-LABVM >>> http://localhost:5000
