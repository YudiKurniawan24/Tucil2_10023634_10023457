import numpy as np
import matplotlib.pyplot as plt

def bezier_kuadratik(t, p0, p1, p2):
    x = (1 - t)**2 * p0[0] + 2 * (1 - t) * t * p1[0] + t**2 * p2[0]
    y = (1 - t)**2 * p0[1] + 2 * (1 - t) * t * p1[1] + t**2 * p2[1]
    return x, y

def plot_bezier_kuadratik(p0, p1, p2, iterasi=5, num_points=100, t=0.5):
    # Hitung koordinat Q0 dan Q1
    q0 = ((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2)
    q1 = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
    
    # Hitung koordinat titik pada kurva Bezier
    t_values = np.linspace(0, 1, num_points)
    curve_points = [bezier_kuadratik(t, p0, p1, p2) for t in t_values]
    x_values, y_values = zip(*curve_points)
    
    # Hitung koordinat T0, R0, dan T1
    t0 = ((p0[0] + q0[0]) / 2, (p0[1] + q0[1]) / 2)
    r0 = ((q0[0] + q1[0]) / 2, (q0[1] + q1[1]) / 2)
    t1 = ((q1[0] + p2[0]) / 2, (q1[1] + p2[1]) / 2)
    
    # Hitung titik-titik aproksimasi garis baru
    line_points = [p0, t0, r0, t1, p2]
    
    # Plot kurva Bezier, titik kontrol, dan garis baru
    plt.plot(x_values, y_values, label='Kurva Bezier Kuadratik')
    plt.scatter([p0[0], p1[0], p2[0], q0[0], q1[0], t0[0], r0[0], t1[0]], 
                [p0[1], p1[1], p2[1], q0[1], q1[1], t0[1], r0[1], t1[1]], 
                color='red', label='Titik Kontrol, Q0/Q1, T0/R0/T1')
    plt.plot([point[0] for point in line_points], [point[1] for point in line_points], linestyle='--', color='blue', label='Garis P0-T0-R0-T1-P2 (Aproksimasi)')
    
    # Plot kurva Bezier, titik kontrol, dan garis baru Q0-Q1
    plt.plot([q0[0], q1[0]], [q0[1], q1[1]], linestyle='--', color='green', label='Garis Q0-Q1')
    
    plt.title('Kurva Bezier Kuadratik dengan Titik Kontrol Tambahan')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

def input_titik(label):
    x = float(input(f"Masukkan koordinat x untuk {label}: "))
    y = float(input(f"Masukkan koordinat y untuk {label}: "))
    return (x, y)

def input_parameter_t():
    t = float(input("Masukkan nilai parameter t (0 <= t <= 1): "))
    if 0 <= t <= 1:
        return t
    else:
        print("Nilai parameter t harus berada dalam rentang 0 hingga 1.")
        return input_parameter_t()

def input_iterasi():
    iterasi = int(input("Masukkan jumlah iterasi: "))
    if iterasi >= 0:
        return iterasi
    else:
        print("Jumlah iterasi harus merupakan bilangan bulat non-negatif.")
        return input_iterasi()

def utama():
    t = input_parameter_t()
    p0 = input_titik("titik awal")
    p1 = input_titik("titik kontrol")
    p2 = input_titik("titik akhir")
    iterasi = input_iterasi()

    plot_bezier_kuadratik(p0, p1, p2, iterasi=iterasi, num_points=100, t=t)

if __name__ == "__main__":
    utama()
