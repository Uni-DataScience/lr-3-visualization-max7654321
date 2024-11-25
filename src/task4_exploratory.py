import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def perform_eda(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)

    # Step 1: Descriptive Statistics
    descriptive_stats = data.describe(include='all').T
    descriptive_stats['median'] = data.median()  # Add median
    descriptive_stats['mode'] = data.mode().iloc[0]  # Add mode
    descriptive_stats['variance'] = data.var()  # Add variance
    print("Descriptive Statistics:")
    print(descriptive_stats)

    # Step 2: Box Plot for Outlier Detection
    numerical_columns = data.select_dtypes(include=[np.number]).columns
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=data[numerical_columns], orient="h", palette="Set2")
    plt.title("Box Plot for Outlier Detection", fontsize=16)
    plt.xlabel("Value Range")
    plt.ylabel("Features")
    plt.tight_layout()
    plt.show()

    # Step 3: Correlation Analysis
    corr_matrix = data.corr()  # Compute correlation matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
    plt.title("Correlation Matrix Heatmap", fontsize=16)
    plt.tight_layout()
    plt.show()

    # Step 4: Findings
    print("\nFindings:")
    print("- Descriptive statistics provide key measures of central tendency and dispersion.")
    print("- Box plots indicate potential outliers in numerical columns.")
    print("- The correlation matrix highlights relationships between variables.\n")
    print("Key Insights:")
    print("- Highly correlated variables may suggest redundancy.")
    print("- Outliers identified in the box plot may warrant further investigation.")

# Example usage (Replace 'your_dataset.csv' with the actual dataset file path)
file_path = 'your_dataset.csv'  # Replace with your dataset file path
perform_eda(file_path)
