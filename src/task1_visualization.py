import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def generate_data_and_plot():
    # Step 1: Generate random categorical data
    np.random.seed(42)  # For reproducibility
    categories = np.random.choice(['A', 'B', 'C'], size=100, p=[0.5, 0.3, 0.2])
    
    # Step 2: Calculate frequency of each category
    category_counts = pd.Series(categories).value_counts()

    # Step 3: Create a bar chart
    plt.figure(figsize=(8, 5))
    colors = ['skyblue', 'lightgreen', 'salmon']
    plt.bar(category_counts.index, category_counts.values, color=colors)

    # Step 4: Customize the plot
    plt.title('Frequency of Categories', fontsize=16)
    plt.xlabel('Category', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Step 5: Display the chart
    plt.tight_layout()
    plt.show()

# Run the function
generate_data_and_plot()
