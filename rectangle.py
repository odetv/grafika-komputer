# pip install matplotlib
import matplotlib.pyplot as plt

def draw_line_DDA(x1, y1, x2, y2): # Fungsi menggambar garis Algoritma DDA
    
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

def draw_rectangle_DDA(x, y, lebar, tinggi): # Fungsi menggambar persegi panjang Algoritma DDA
    # Mengatur koordinat titik sudut persegi panjang berdasarkan x, y, lebar, dan tinggi
    x1, y1 = x, y                   # Titik sudut atas kiri
    x2, y2 = x + lebar, y           # Titik sudut atas kanan
    x3, y3 = x + lebar, y - tinggi  # Titik sudut bawah kanan
    x4, y4 = x, y - tinggi          # Titik sudut bawah kiri
    
    # Menyimpan titik-titik dalam list rectangle_points
    rectangle_points = []
    
    # Menambahkan titik-titik dengan menggunakan fungsi draw_line_DDA
    rectangle_points.extend(draw_line_DDA(x1, y1, x2, y2)) # Menggambar sisi atas
    rectangle_points.extend(draw_line_DDA(x2, y2, x3, y3)) # Menggambar sisi kanan
    rectangle_points.extend(draw_line_DDA(x3, y3, x4, y4)) # Menggambar sisi bawah
    rectangle_points.extend(draw_line_DDA(x4, y4, x1, y1)) # Menggambar sisi kiri
    return rectangle_points

# Input titik awal (x, y) dan panjang sisi persegi
print("Program Pembentukan Persegi Panjang Menggunakan Algoritma DDA")
x, y = map(int, input("Masukkan Koordinat x y untuk Sudut Kiri Atas: ").split())
lebar = int(input("Masukkan Lebar Persegi Panjang: "))
tinggi = int(input("Masukkan Tinggi Persegi Panjang: "))

# Memanggil fungsi draw_rectangle_DDA untuk menggambar persegi panjang
rectangle_points = draw_rectangle_DDA(x, y, lebar, tinggi)

# Membagi kumpulan titik menjadi dua list terpisah (x dan y)
x_points, y_points = zip(*rectangle_points)

# Membuat plot persegi panjang dengan menggunakan titik-titik
plt.plot(x_points, y_points, marker='o')
plt.title('Membuat Persegi Panjang Menggunakan Algoritma DDA')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.grid(True)
plt.show()
