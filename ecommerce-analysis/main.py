# main.py
import os
from scripts.data_cleaning import load_and_clean_data
from scripts.eda import plot_country_sales
from scripts.rfm_analysis import calculate_rfm
from scripts.rfm_segmentation import kmeans_segmentation

# 1️⃣ Dosya yollarını güvenli oluştur
current_dir = os.path.dirname(os.path.abspath(__file__))  # main.py'nin bulunduğu klasör
data_path = os.path.join(current_dir, "data", "e_commerce_uk.csv")
results_dir = os.path.join(current_dir, "results")

# results klasörü yoksa oluştur
os.makedirs(results_dir, exist_ok=True)

# 2️⃣ Veri yükle
df = load_and_clean_data(data_path)

# 3️⃣ Ülkelere göre satış grafiği
plot_country_sales(df, save_path=os.path.join(results_dir, "country_sales.png"))

# 4️⃣ RFM Analizi
rfm = calculate_rfm(df)

# 5️⃣ K-Means Segmentasyonu
rfm_segmented = kmeans_segmentation(rfm, n_clusters=4)

# 6️⃣ Sonuçları kaydet
rfm_segmented.to_csv(os.path.join(results_dir, "rfm_segmented.csv"))
print(rfm_segmented.head())
