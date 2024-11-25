import pandas as pd
import numpy as np
import plotly.express as px

def create_interactive_scatter_plot():
    # Generate sample data
    np.random.seed(42)
    num_points = 200
    data = {
        'X': np.random.uniform(0, 50, num_points),
        'Y': np.random.uniform(0, 100, num_points),
        'Category': np.random.choice(['A', 'B', 'C'], num_points)
    }
    df = pd.DataFrame(data)

    # Create the interactive scatter plot
    fig = px.scatter(
        df,
        x='X',
        y='Y',
        color='Category',
        hover_data=['X', 'Y', 'Category'],
        title="Interactive Scatter Plot: Explore Data Dynamically",
        labels={'X': 'X-Axis Label', 'Y': 'Y-Axis Label'},
        template='plotly'
    )

    # Customize layout for better readability
    fig.update_layout(
        title_font_size=20,
        xaxis_title_font_size=14,
        yaxis_title_font_size=14,
        legend_title="Categories",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )

    # Show the plot
    fig.show()

# Run the function to display the plot
create_interactive_scatter_plot()
