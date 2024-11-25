import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def generate_data_and_plot_scatter():
    # Step 1: Generate a dataset
    np.random.seed(42)  # For reproducibility
    x = np.random.uniform(0, 50, 100)  # Generate 100 random points for 'x'
    y = 2 * x + np.random.normal(0, 10, 100)  # Create 'y' as a linear function of 'x' with some noise
    
    # Create a DataFrame for ease of use with Seaborn
    data = pd.DataFrame({'x': x, 'y': y})

    # Step 2: Set Seaborn style for simplicity
    sns.set(style="whitegrid")

    # Step 3: Create the scatter plot
    plt.figure(figsize=(8, 5))
    scatter_plot = sns.scatterplot(x='x', y='y', data=data, color="royalblue", alpha=0.7)

    # Step 4: Customize the plot for clarity
    plt.title("Scatter Plot of X vs. Y", fontsize=16, fontweight='bold')
    plt.xlabel("X Variable", fontsize=12)
    plt.ylabel("Y Variable", fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)

    # Step 5: Show the plot
    plt.tight_layout()
    plt.show()

# Run the function
generate_data_and_plot_scatter()
