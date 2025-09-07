import matplotlib.pyplot as plt
import seaborn as sns

def plot_country_sales(df, save_path=None):
    country_sales = df.groupby("Country")["TotalPrice"].sum().sort_values(ascending=False)
    plt.figure(figsize=(12,6))
    sns.barplot(x=country_sales.index[:10], y=country_sales.values[:10])
    plt.xticks(rotation=45)
    plt.title("En Çok Satış Yapılan İlk 10 Ülke")
    if save_path:
        plt.savefig(save_path, bbox_inches="tight")
    plt.show()
