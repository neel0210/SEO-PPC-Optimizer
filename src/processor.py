import pandas as pd

def load_and_merge(seo_csv, ppc_csv):
    """Loads CSVs and merges them on the Keyword column."""
    seo = pd.read_csv(seo_csv)
    ppc = pd.read_csv(ppc_csv)
    
    # Ensure column names are standardized
    # Assuming columns: ['Keyword', 'Position'] for SEO and ['Keyword', 'Cost', 'Impressions'] for PPC
    merged = pd.merge(seo, ppc, on='Keyword', how='inner')
    return merged

def get_optimization_candidates(df, pos_threshold=3):
    """
    Identifies keywords where organic rank is high (<= threshold) 
    but we are still spending on PPC.
    """
    candidates = df[(df['Position'] <= pos_threshold) & (df['Cost'] > 0)]
    return candidates.sort_values(by='Cost', ascending=False)
