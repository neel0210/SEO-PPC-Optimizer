import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_seo_ppc_overlap(df):
    """Generates a scatter plot of Position vs Cost."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        data=df, 
        x='Position', 
        y='Cost', 
        size='Impressions', 
        hue='Cost', 
        palette='viridis',
        sizes=(50, 500)
    )
    
    plt.title('SEO Rank vs PPC Cost')
    plt.xlabel('Organic Search Position')
    plt.ylabel('PPC Cost ($)')
    plt.axvline(x=3, color='r', linestyle='--', label='Top 3 Threshold')
    plt.legend()
    plt.tight_layout()
    
    # Save the visualization
    plt.savefig('overlap_analysis.png')
    print("Visualization saved as overlap_analysis.png")

# 
