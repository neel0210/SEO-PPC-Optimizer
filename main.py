from src.processor import load_and_merge, get_optimization_candidates
from src.visualizer import plot_seo_ppc_overlap

df = load_and_merge('data/gsc_report.csv', 'data/google_ads_report.csv')

candidates = get_optimization_candidates(df)
candidates.to_csv('data/optimization_report.csv', index=False)
plot_seo_ppc_overlap(df)

print(f"Analysis complete. {len(candidates)} keywords identified for potential budget reallocation.")
