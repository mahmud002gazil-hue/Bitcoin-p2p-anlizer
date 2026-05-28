from src.data_loader import fetch_futures_data
from src.analyzer import run_grid_analysis

def main():
    # --- Kullanıcı Parametreleri ---
    SYMBOL = "BTC/USDT"
    TIMEFRAME = "1h"
    INVESTMENT = 1000       # Ana para (Marjin)
    LEVERAGE = 5            # Kaldıraç oranı
    LOWER_PRICE = 60000     # Grid alt bant
    UPPER_PRICE = 70000     # Grid üst bant
    GRID_COUNT = 20         # Izgara sayısı
    
    # 1. Veriyi Yükle
    df = fetch_futures_data(symbol=SYMBOL, timeframe=TIMEFRAME, limit=500)
    
    # 2. Analiz Et
    report, grids = run_grid_analysis(df, LOWER_PRICE, UPPER_PRICE, GRID_COUNT, LEVERAGE, INVESTMENT)
    
    # 3. Sonuçları Raporla
    print("\n" + "="*40)
    print(f"📊 BITCOIN FUTURES GRID ÖN ANALİZ RAPORU ({SYMBOL})")
    print("="*40)
    for key, value in report.items():
        if isinstance(value, float):
            print(f"{key}: {value:.2f}")
        else:
            print(f"{key}: {value}")
    print("="*40)

if __name__ == "__main__":
    main()
