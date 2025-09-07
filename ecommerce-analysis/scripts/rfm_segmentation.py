# scripts/rfm_segmentation.py
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


def kmeans_segmentation(rfm_df, n_clusters=4):
    scaler = StandardScaler()
    rfm_scaled = scaler.fit_transform(rfm_df)

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    rfm_df['Segment'] = kmeans.fit_predict(rfm_scaled)

    return rfm_df
