import matplotlib.pyplot as plt
import pandas as pd
from data.fetch import download_prices
from backtest.engine import run_backtest
from config import SAVE_CHART, CHART_PATH, BENCHMARK

def main():
    print("Downloading data...")
    prices = download_prices()
    print("Running backtest...")
    nav, bench_nav, ret, stats = run_backtest(prices)
    
    print("\n=== Performance Metrics ===")
    for k, v in stats.items():
        print(f"{k}: {v}")
    
    # 绘制净值曲线
    plt.figure(figsize=(12, 6))
    plt.plot(nav.index, nav, label='Strategy (Simplified)', linewidth=2)
    plt.plot(bench_nav.index, bench_nav, label=f'Benchmark ({BENCHMARK})', linewidth=1.5, alpha=0.7)
    plt.title('US ETF Rotation Strategy vs Benchmark')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Return')
    plt.legend()
    plt.grid(alpha=0.3)
    if SAVE_CHART:
        plt.savefig(CHART_PATH, dpi=150)
        print(f"Chart saved to {CHART_PATH}")
    plt.show()
    
    # 年度收益表
    yearly_ret = ret.resample('Y').apply(lambda x: (1+x).prod() - 1)
    yearly_ret.index = yearly_ret.index.year
    print("\n=== Annual Returns (Strategy) ===")
    print(yearly_ret.to_string())

if __name__ == '__main__':
    main()