# SmartGuard-dashboard

# Submission_SmartGuard-Analytics_CC26-PSU072
## SmartGuard Analytics Dashboard

* **Tim:** CC26-PSU072
* **Topik:** Bank Transaction Fraud Detection

---

## Deskripsi Proyek

Dashboard ini merupakan aplikasi analisis data interaktif yang dibuat menggunakan Python dan Streamlit. Dashboard ini digunakan untuk mengeksplorasi dan memahami pola fraud pada transaksi perbankan berdasarkan berbagai dimensi seperti waktu transaksi, nominal, lokasi geografis, jenis merchant & device, kondisi finansial, serta kekuatan fitur dalam mendeteksi fraud. Melalui visualisasi yang disediakan, pengguna dapat melihat bagaimana pola fraud berubah dalam berbagai kondisi, sehingga dapat memberikan insight yang berguna untuk pengambilan keputusan dan perancangan sistem deteksi fraud.

---

## Fitur Utama

* **Overview Dataset:** Ringkasan distribusi kelas (Fraud vs Normal), distribusi nominal transaksi, dan statistik dasar fitur numerik utama (Transaction Amount, Account Balance, Age).
* **Analisis Temporal:** Visualisasi fraud rate per jam, per hari, heatmap jam × hari, kategori waktu (Morning/Afternoon/Evening/Night), serta Skor Dominansi faktor pemicu fraud.
* **Analisis Nominal:** Distribusi nominal transaksi fraud vs normal, binning interval nominal, dan rekomendasi skema verifikasi berjenjang.
* **Analisis Geografis:** Sebaran fraud berdasarkan wilayah/lokasi transaksi.
* **Merchant & Device:** Fraud rate per jenis merchant, tipe device, dan kombinasi faktor risiko tinggi.
* **Analisis Finansial:** Korelasi rasio Amount/Balance terhadap fraud, deteksi card testing (nominal kecil), distribusi saldo kritis, dan estimasi total kerugian.
* **Evaluasi Fitur:** Korelasi absolut seluruh fitur numerik terhadap target `Is_Fraud`, heatmap korelasi top-10 fitur, serta validasi hasil feature engineering (engineered flags vs fitur asli).

---

## Teknologi yang Digunakan

* **Python:** Bahasa pemrograman utama
* **Pandas:** Manipulasi dan agregasi data
* **NumPy:** Komputasi numerik
* **Plotly Express & Plotly Graph Objects:** Visualisasi interaktif (bar chart, scatter, heatmap, pie, box plot, histogram)
* **Streamlit:** Pembuatan dashboard interaktif berbasis web

---

## Deskripsi Data

Dataset terdiri dari satu file utama yang berisi data transaksi perbankan dengan label fraud, sebagai berikut:

* **`main_data.csv`** (separator `;`): Data transaksi perbankan yang telah melalui proses feature engineering

### Kolom Utama

| Kolom | Deskripsi |
|---|---|
| `Is_Fraud` | Label target — 1 = Fraud, 0 = Normal |
| `Transaction_Amount` | Nominal transaksi (INR) |
| `Account_Balance` | Saldo akun nasabah (INR) |
| `Balance_After_Transaction` | Saldo setelah transaksi |
| `Transaction_Hour` | Jam transaksi (0–23) |
| `Transaction_DayOfWeek` | Hari transaksi (0 = Senin … 6 = Minggu) |
| `Transaction_Weekend` | Flag akhir pekan (1 = Ya) |
| `Device_Type` | Tipe perangkat (Mobile, Desktop, Tablet) |
| `Account_Type` | Tipe akun (Personal, Business) |
| `Age` | Usia nasabah (tahun) |
| `Is_Night_Transaction` | Flag transaksi malam 00:00–05:59 |
| `Is_High_Risk_Combination` | Flag kombinasi malam + mobile |
| `Is_Weekend_Small_Amount` | Flag weekend + nominal < 10.000 |
| `Is_Small_Amount_High_Risk` | Flag nominal kecil berisiko (< 10.000) |
| `Is_High_Risk_Merchant` | Flag merchant berisiko tinggi |
| `Is_High_Risk_Device` | Flag device berisiko tinggi |
| `Is_Balance_Critical` | Flag saldo kritis (< 10% saldo awal) |
| `Amount_to_Balance_Ratio` | Rasio nominal terhadap saldo akun |
| `Amount_to_Age_Ratio` | Rasio nominal terhadap usia nasabah |
| `Transaction_Amount_zscore` | Z-score nominal transaksi |
| `Time_Category` | Kategori waktu: Morning / Afternoon / Evening / Night |

---

## Cara Menjalankan Dashboard

### 1. Pastikan semua file berikut ada dalam satu folder:

```
- dashboard.py
- main_data.csv
- requirements.txt
```

### 2. Membuat Virtual Environment

Untuk menghindari konflik antar library, sebaiknya gunakan virtual environment. Buka terminal atau command prompt di folder proyek, lalu pilih salah satu cara berikut:

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Anaconda:**
```bash
conda create --name main-ds python=3.9
conda activate main-ds
```

### 3. Instalasi Library

Setelah environment aktif, install semua library yang dibutuhkan menggunakan file `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Menjalankan Aplikasi Streamlit

Setelah semua sudah siap, jalankan aplikasi dengan perintah berikut. Dashboard akan otomatis terbuka di browser.

```bash
streamlit run dashboard.py
```

---

## Navigasi Halaman

| Halaman | Pertanyaan Riset | Deskripsi |
|---|---|---|
| Overview Dataset | — | Gambaran umum distribusi kelas dan fitur |
| Analisis Temporal | Q1, Q3 | Pola waktu dan device pemicu fraud |
| Analisis Nominal | Q2 | Interval nominal dan skema verifikasi |
| Analisis Geografis | Q4 | Sebaran fraud berdasarkan lokasi |
| Merchant & Device | Q5 | Fraud rate per merchant dan perangkat |
| Analisis Finansial | Q6 | Rasio finansial dan estimasi kerugian |
| Evaluasi Fitur | Q7 | Korelasi fitur dan validasi feature engineering |

---

## Catatan

> ⚠️ **Indikasi Data Sintetis:** Distribusi Uniform (skewness ≈ 0) pada seluruh fitur numerik mengonfirmasi dataset ini bersifat sintetis. Hal ini menyebabkan fraud rate yang homogen (~5%) di semua kategori, sehingga model perlu menangkap **kombinasi fitur non-linear** untuk deteksi yang efektif.
