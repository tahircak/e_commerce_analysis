# scripts/rfm_analysis.py
import pandas as pd

def calculate_rfm(df, reference_date=None):
    """
    RFM tablosunu oluşturur.
    Recency = Son alışverişten geçen gün sayısı
    Frequency = Toplam alışveriş sayısı
    Monetary = Toplam harcama
    """
    if reference_date is None:
        reference_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)

    rfm = df.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (reference_date - x.max()).days,
        'InvoiceNo': 'nunique',
        'TotalPrice': 'sum'
    }).rename(columns={
        'InvoiceDate': 'Recency',
        'InvoiceNo': 'Frequency',
        'TotalPrice': 'Monetary'
    })

    return rfm
