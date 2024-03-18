import matplotlib.pyplot as plt

def quadratic_bezier(t, start_point, control_point, end_point):
    """
    Menghitung titik pada kurva Bezier kuadratik pada parameter t.
    """
    x = (1 - t)**2 * start_point[0] + 2 * (1 - t) * t * control_point[0] + t**2 * end_point[0]
    y = (1 - t)**2 * start_point[1] + 2 * (1 - t) * t * control_point[1] + t**2 * end_point[1]
    return x, y

def plot_quadratic_bezier(start_point, control_point, end_point, num_points=100):
    """
    Plot kurva Bezier kuadratik dengan pendekatan brute force.
    """
    x_values, y_values = [], []
    for i in range(num_points + 1):
        t = i / num_points
        x, y = quadratic_bezier(t, start_point, control_point, end_point)
        x_values.append(x)
        y_values.append(y)

    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, label='Kurva Bezier Kuadratik')
    plt.scatter([start_point[0], control_point[0], end_point[0]], [start_point[1], control_point[1], end_point[1]], color='red', label='Titik Kontrol')
    plt.plot([start_point[0], control_point[0], end_point[0]], [start_point[1], control_point[1], end_point[1]], linestyle='--', color='grey', alpha=0.5, label='Garis Kontrol')

    plt.title('Kurva Bezier Kuadratik')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

def input_point(label):
    x = float(input(f"Masukkan koordinat x untuk {label}: "))
    y = float(input(f"Masukkan koordinat y untuk {label}: "))
    return (x, y)

def main():
    print("Masukkan koordinat untuk titik-titik Bezier:")
    start_point = input_point("titik awal")
    control_point = input_point("titik kontrol")
    end_point = input_point("titik akhir")

    plot_quadratic_bezier(start_point, control_point, end_point)

if __name__ == "__main__":
    main()
