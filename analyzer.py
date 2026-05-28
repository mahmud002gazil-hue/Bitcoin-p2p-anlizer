import numpy as np

def run_grid_analysis(df, lower_price, upper_price, grid_count, leverage, investment):
    """Grid stratejisini simüle eder ve ön analiz raporu çıkarır."""
    initial_price = df['close'].iloc[0]
    grid_step = (upper_price - lower_price) / grid_count
    grids = np.linspace(lower_price, upper_price, grid_count)
    
    # Basit Likidasyon ve Risk Analizi
    # Vadeli işlemlerde kaldıraç riskini simüle etmek için:
    max_price = df['high'].max()
    min_price = df['low'].min()
    
    # Cüzdan ve Pozisyon Büyüklüğü Hesaplama
    total_position_size = investment * leverage
    position_per_grid = total_position_size / grid_count
    
    # Eğer fiyat alt bandın altına düşerse oluşacak teorik zarar (Long Grid için)
    price_drop_pct = (initial_price - min_price) / initial_price
    potential_loss = total_position_size * price_drop_pct
    
    is_liquidated = potential_loss >= investment
    
    report = {
        "Başlangıç Fiyatı": initial_price,
        "En Yüksek Fiyat": max_price,
        "En Düşük Fiyat": min_price,
        "Grid Adım Mesafesi (USDT)": grid_step,
        "Toplam Pozisyon Büyüklüğü ($)": total_position_size,
        "Izgara Başına Büyüklük ($)": position_per_grid,
        "Maksimum Olası Zarar ($)": potential_loss,
        "Likidasyon Riski Var mı?": "EVET 🚨" if is_liquidated else "HAYIR ✅"
    }
    
    return report, grids
