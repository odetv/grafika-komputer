# pip install matplotlib
import matplotlib.pyplot as plt

def draw_circle_Bresenham(radius): # Fungsi Algoritma Bresenham
    x = 0               # Menginisialisasi nilai x pada titik awal
    y = radius          # Menginisialisasi nilai y pada titik awal
    d = 3 - 2 * radius  # Menghitung nilai awal dari parameter d pada algoritma Bresenham (Bisa juga d = 1 - radius)
    
    # Mmebuat list kosong untuk menyimpan semua titik pada lingkaran
    points = []
    while x <= y: # Melakukan loop sampai titik lengkung lingkaran tergambar penuh
        # Menambahkan titik-titik lingkaran pada semua 8 kuadran dengan simetri ke list points
        points.append((x, y))   # Kuadran I
        points.append((-x, y))  # Kuadran II
        points.append((x, -y))  # Kuadran III
        points.append((-x, -y)) # Kuadran IV
        points.append((y, x))   # Kuadran I, simetris terhadap x=y
        points.append((-y, x))  # Kuadran I, simetris terhadap -x=y
        points.append((y, -x))  # Kuadran II, simetris terhadap x=-y
        points.append((-y, -x)) # Kuadran II, simetris terhadap -x=-y

        # Memeriksa apakah nilai parameter d kurang dari atau sama dengan 0
        # Menghitung nilai berikutnya dari parameter d sesuai aturan algoritma Bresenham
        if d <= 0:
            d = d + 4 * x + 6
        # Menghitung nilai berikutnya dari parameter d sesuai aturan algoritma Bresenham
        # Mengurangi nilai y untuk menyesuaikan langkah selanjutnya dalam menggambar lingkaran
        else:
            d = d + 4 * (x - y) + 10
            y -= 1
        # Menambahkan nilai x untuk memperbarui langkah selanjutnya dalam menggambar lingkaran
        x += 1
    return points

# Input radius lingkaran dari pengguna dengan validasi
# Membuat loop yang terus berjalan sampai input yang valid diberikan
while True:
    # Handle radius kurang dari atau sama dengan 0
    try:
        print("Program Pembentukan Lingkaran Menggunakan Algoritma Bresenham")
        radius = int(input("Masukkan Radius Lingkaran: "))
        if radius <= 0:
            print("Radius harus lebih besar dari 0. Silakan masukkan nilai yang valid!")
            continue
        break
    # Handle kemungkinan pengguna memasukkan inputan selain yang sudah di validasi
    except ValueError:
        print("Input yang Anda masukkan bukan angka bulat atau tidak valid. Silakan coba lagi!")

# Memanggil fungsi untuk menggambar lingkaran
circle_points = draw_circle_Bresenham(radius)

# Membagi kumpulan titik menjadi dua list terpisah (x dan y)
x_points, y_points = zip(*circle_points)

# Membuat plot lingkaran dengan menggunakan titik-titik
plt.scatter(x_points, y_points)
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Membuat Lingkaran Menggunakan Algoritma Bresenham')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.grid(True)
plt.show()