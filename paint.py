import cv2

# Membuat fungsi untuk menangani event mouse
def draw_shapes(event, x, y, flags, param):
    global drawing, mode, ix, iy

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == 'line':
            cv2.line(img, (ix, iy), (x, y), (255, 0, 0), 2)
        elif mode == 'circle':
            radius = int(((x - ix) ** 2 + (y - iy) ** 2) ** 0.5)
            cv2.circle(img, (ix, iy), radius, (0, 255, 0), 2)

# Membuat canvas kosong dengan OpenCV
img = cv2.imread('blank_canvas.jpg')  # Ubah 'blank_canvas.jpg' sesuai dengan nama file kosong Anda
cv2.namedWindow('Canvas')
cv2.setMouseCallback('Canvas', draw_shapes)

drawing = False
mode = 'line'  # Mode default: garis
ix, iy = -1, -1

while True:
    cv2.imshow('Canvas', img)
    k = cv2.waitKey(1) & 0xFF

    # Pilih mode untuk menggambar
    if k == ord('l'):
        mode = 'line'
    elif k == ord('c'):
        mode = 'circle'
    elif k == 27:  # Tekan 'Esc' untuk keluar
        break

cv2.destroyAllWindows()
