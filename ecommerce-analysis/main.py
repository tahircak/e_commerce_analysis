from scripts.data_cleaning import load_and_clean_data
from scripts.eda import plot_country_sales
from scripts.rfm_analysis import calculate_rfm
from scripts.rfm_segmentation import kmeans_segmentation

# 1️⃣ Veri yükle
df = load_and_clean_data("ecommerce-analysis/data/e_commerce_uk.csv")

# 2️⃣ Ülkelere göre satış grafiği
plot_country_sales(df, save_path="results/country_sales.png")

# 3️⃣ RFM Analizi
rfm = calculate_rfm(df)

# 4️⃣ K-Means Segmentasyonu
rfm_segmented = kmeans_segmentation(rfm, n_clusters=4)

# 5️⃣ Sonuçları kaydet
rfm_segmented.to_csv("results/rfm_segmented.csv")
print(rfm_segmented.head())
