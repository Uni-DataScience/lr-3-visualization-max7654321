import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def visualize_1D_2D_3D_data():
    # 1D Line Plot
    x_1d = np.linspace(0, 10, 100)  # 1D sequence of values
    y_1d = np.sin(x_1d)  # Sine wave
    
    plt.figure(figsize=(8, 4))
    plt.plot(x_1d, y_1d, label='Sine Wave', color='blue')
    plt.title("1D Line Plot: Sine Wave", fontsize=14)
    plt.xlabel("X-axis", fontsize=12)
    plt.ylabel("Y-axis (sin(x))", fontsize=12)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # 2D Scatter Plot
    np.random.seed(42)
    x_2d = np.random.uniform(0, 50, 100)
    y_2d = 2 * x_2d + np.random.normal(0, 10, 100)
    
    plt.figure(figsize=(8, 5))
    plt.scatter(x_2d, y_2d, color='green', alpha=0.6)
    plt.title("2D Scatter Plot: Relationship Between X and Y", fontsize=14)
    plt.xlabel("X-axis", fontsize=12)
    plt.ylabel("Y-axis", fontsize=12)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # 3D Scatter Plot
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    z_3d = np.random.uniform(0, 50, 100)
    ax.scatter(x_2d, y_2d, z_3d, c=z_3d, cmap='viridis', alpha=0.8)
    ax.set_title("3D Scatter Plot: X, Y, Z Relationships", fontsize=14)
    ax.set_xlabel("X-axis", fontsize=12)
    ax.set_ylabel("Y-axis", fontsize=12)
    ax.set_zlabel("Z-axis", fontsize=12)
    plt.tight_layout()
    plt.show()

# Run the function
visualize_1D_2D_3D_data()
