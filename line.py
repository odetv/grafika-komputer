# pip install matplotlib
import matplotlib.pyplot as plt

def draw_line_DDA(x1, y1, x2, y2): # Fungsi Algoritma DDA
    
    # Menentukan nilai dx dan dy (Menghitung perubahan koordinat)
    # Delta x = dx dan Delta y = dy
    dx = x2 - x1
    dy = y2 - y1

    # Menentukan steps/jumlah langkah
    # Jika nilai dx > dy maka gunakan steps=dx dan Jika nilai dy > dx maka gunakan steps=dy
    # steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    steps = max(abs(dx), abs(dy))
    
    # Menghitung nilai increment x dan y
    x_increment = dx / steps
    y_increment = dy / steps
    
    # Menginisialisasi koordinat awal paling pertama
    x, y = x1, y1
    
    # Menyimpan titik awal dalam list points
    points = [(x, y)] 
    
    # Iterasi sebanyak steps yang diperlukan
    for _ in range(steps): 
        x += x_increment                    # Menambah nilai x dengan increment x
        y += y_increment                    # Menambah nilai y dengan increment y
        points.append((round(x), round(y))) # Menambahkan titik terbaru ke dalam list points setelah dibulatkan menggunakan round
    return points

# Input titik awal (x1, y1) dan titik akhir (x2, y2) dari pengguna dipisah dengan split spasi
print("Program Pembentukan Garis Menggunakan Algoritma DDA")
x1, y1 = map(int, input("Masukkan Koordinat x1 y1: ").split())
x2, y2 = map(int, input("Masukkan Koordinat x2 y2: ").split())

# Memanggil fungsi draw_line_DDA untuk menggambar garis
line_points = draw_line_DDA(x1, y1, x2, y2)

# Menampilkan koordinat piksel sepanjang garis
print("Koordinat (x, y) piksel yang membentuk sepanjang garis:")
count = 1
for x, y in line_points:
    print(f"{count}. ({x}, {y})")
    count += 1

# Membagi kumpulan titik menjadi dua list terpisah (x dan y)
x_points, y_points = zip(*line_points)
# x_points = [point[0] for point in line_points]
# y_points = [point[1] for point in line_points]

# Membuat plot garis dengan menggunakan titik-titik
plt.plot(x_points, y_points, marker='o')
plt.title('Membuat Garis Menggunakan Algoritma DDA')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.grid(True)
for i in range(len(x_points)):
    plt.text(x_points[i], y_points[i], f'({x_points[i]}, {y_points[i]})')
plt.show()
