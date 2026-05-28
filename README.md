# Bitcoin-p2p-anlizer
Bitcoin analiz işlemler

bitcoin-futures-grid-analyzer/
│
├── data/                  # Geçmiş fiyat verilerinin (CSV) saklanacağı klasör
├── src/
│   ├── __init__.py
│   ├── data_loader.py     # Binance API'den veri çekme ve işleme
│   ├── analyzer.py        # Grid stratejisi, kâr/zarar ve likidasyon hesabı
│   └── visualizer.py      # Grafik çizdirme (Matplotlib / Plotly)
│
├── main.py                # Programı çalıştıracak ana script
├── requirements.txt       # Gerekli kütüphaneler
└── README.md              # Proje açıklaması ve kullanım kılavuzu
