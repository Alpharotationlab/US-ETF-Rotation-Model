# A-Share ETF Rotation Model – Simplified

This repository provides a **simplified, research-grade implementation** of a momentum-based ETF rotation strategy combined with a 200-day moving average trend filter for the A-Share market. Designed for quantitative research, backtesting, and educational purposes.

> 📌 **Disclaimer** – Nothing herein constitutes investment advice. Past performance does not guarantee future results.

---

## Table of Contents

- [Overview](#overview)
- [Research Philosophy](#research-philosophy)
- [Strategy Logic](#strategy-logic)
- [Simplified vs Full Model](#simplified-vs-full-model--key-differences)
- [Backtest Summary](#backtest-summary)
- [Annual Performance Breakdown](#annual-performance-breakdown)
- [Risk Metrics](#risk-metrics)
- [ETF Universe](#etf-universe)
- [Equity Curve](#equity-curve)
- [Limitations](#limitations)
- [Open Source vs Extended Research](#-open-source-vs-extended-research)
- [Installation](#installation)
- [Requirements](#requirements)
- [Usage](#usage)
- [Data Source](#data-source)
- [License](#license)
- [Full Disclaimer](#full-disclaimer)

---

## Overview

This repository contains a **simplified research edition** of an A-Share ETF rotation framework based on:

- Relative momentum ranking (20-day lookback)
- 200-day moving average trend filter
- Weekly rebalancing (every 5 trading days)
- 0.15% one-way transaction cost assumption

The code includes:

- Historical backtesting engine
- `efinance`-based data pipeline (no token required)
- Performance evaluation metrics
- ETF universe of 14 liquid A-Share broad-market and sector ETFs
- Simplified research implementation

The goal is to provide a transparent, reproducible, and **trustworthy** baseline for systematic A-Share ETF allocation research.

> **Note on data availability** – Three ETFs in the universe were listed after 2019:  
> `512760` (Semiconductor ETF, listed June 2019), `515220` (Coal ETF, listed March 2020),  
> and `515790` (Solar ETF, listed December 2020).  
> The backtest automatically uses only the available price history for each fund.  
> Reported results reflect real tradable history.

---

## Research Philosophy

This repository is **not** an attempt to ship a "magic" trading strategy. It serves as an **educational and transparent research framework** for ETF rotation strategies built on momentum and trend-following.

The simplified implementation intentionally emphasizes:

- **Clarity** – Code is written for humans, not machines.
- **Reproducibility** – Run `python run_backtest.py` and obtain the exact same results.
- **Educational value** – Understand how momentum ranking and trend filtering interact.

The extended research version (available separately) builds on this foundation with:

- Multi-factor ranking (not just momentum)
- Dynamic risk management and regime detection
- Adaptive position sizing
- Weekly model updates with full transparency

The open-source version alone is a **solid, correct, and useful** starting point for anyone interested in systematic A-Share ETF allocation. It is not "crippled" — it is a genuine research implementation you can trust, with well-understood limitations.

---

## Strategy Logic

The simplified model follows these steps:

1. Select a universe of 14 liquid A-Share ETFs (see `config.py`)
2. Rank ETFs by momentum over the last **20 trading days**
3. Apply trend filter: current price must be above its **200-day simple moving average**
4. Hold the **top 3** ETFs that satisfy the trend condition
5. Rebalance every **5 trading days** (roughly weekly)

This open-source version uses **default parameters** that are reasonable and widely accepted in the momentum-rotation literature. Users are encouraged to experiment with different settings.

---

## Simplified vs Full Model — Key Differences

> ⚠️ **Read this section before interpreting the backtest results.**

The simplified model achieves meaningfully higher returns than the CSI 300 benchmark over the 2019–2026 period. This comes with a real trade-off: the model also carries higher annual volatility (24.26% vs benchmark 18.9%) and does not include any regime-based defensive mechanism.

| Component | Simplified (this repo) | Full Model |
|---|:---:|:---:|
| Momentum ranking | ✅ | ✅ |
| 200-day MA trend filter | ✅ | ✅ |
| Market regime detection | ❌ | ✅ |
| Risk budget & position sizing | ❌ | ✅ |
| Drawdown circuit breaker | ❌ | ✅ |
| Defensive allocation (money market / short bond) | ❌ | ✅ |

**Why this matters for A-Share specifically:**

A-Share markets exhibit high retail participation, policy-driven volatility, and rapid sector rotations that differ structurally from US markets. During the 2021–2022 sector correction (e.g., new energy, education, internet regulations), momentum strategies without regime filters experienced sharp drawdowns before signals could rotate out.

The simplified model's max drawdown reaches **-36.25%** — shallower than the CSI 300's **-42.13%**, but still significant. The full model's regime detection is specifically designed for these A-Share characteristics, reducing drawdown while maintaining positive excess returns.

---

## Backtest Summary

**Period:** 2019-01-02 – 2026-04-30 · **Benchmark:** CSI 300 ETF (510300) · **One-way fee:** 0.15% · **Rebalance:** Every 5 trading days

| Metric | Strategy (Simplified) | CSI 300 (510300) |
|---|---|---|
| Total Return | +199.70% | +100.6% |
| CAGR | 16.85% | 9.15% |
| Max Drawdown | −36.25% | −42.13% |
| Sharpe Ratio | 0.61 | 0.45 |
| Annual Volatility | 24.26% | 18.9% |

> ⚠️ **Note:** The strategy outperforms the benchmark on both raw return and Sharpe ratio, but carries **significantly higher volatility** than the CSI 300. This is a direct consequence of concentrated sector rotation without defensive position management. The full model addresses this through adaptive position sizing.

---

## Annual Performance Breakdown

| Year | Strategy | CSI 300 (510300) | Excess Return |
|---|---|---|---|
| 2019 | +14.36% | +49.9% | −35.54% ⚠️ |
| 2020 | +42.49% | +31.1% | +11.39% |
| 2021 | +36.45% | −5.2% | +41.65% |
| 2022 | −27.69% | −21.4% | −6.29% |
| 2023 | +2.04% | −10.7% | +12.74% |
| 2024 | −0.63% | +20.1% | −20.73% |
| 2025 | +45.88% | +25.2% | +20.68% |
| 2026 YTD | +26.00% | +2.2% | +23.80% |

**Year-by-year interpretation:**

- **2019 (−35.54% excess):** The model's momentum filter was slow to capture the broad-based rebound after the 2018 bear market. The CSI 300 rallied sharply, while the simplified model — holding only 3 ETFs above the 200-day MA — had limited candidates to rotate into early in the year. This is the strategy's most notable underperformance year.
- **2021 (+41.65% excess):** Strong momentum dispersion across sectors (semiconductors, defense, non-ferrous metals) created ideal conditions for rotation. This was the strategy's best year.
- **2023 (+12.74% excess):** The CSI 300 declined while select themes (gold, non-ferrous metals) offered positive momentum. The trend filter successfully avoided the broad market decline.
- **2024 (−20.73% excess):** Broad market recovery driven by policy stimulus benefited buy-and-hold CSI 300 holders. The rotation model's selective exposure lagged the index-wide rebound — a pattern similar to the US model's 2024 underperformance.

---

## Risk Metrics

| Year | Strategy Max DD | Strategy Sharpe |  CSI 300 Annual Return |
|---|---|---|---|
| 2019 | -10.2% | 0.95 | +49.9% |
| 2020 | -9.5% | 1.70 | +31.1% |
| 2021 | -12.1% | 1.15 | −5.2% |
| 2022 | -24.3% | -0.82 | −21.4% |
| 2023 | -14.0% | 0.92| −10.7% |
| 2024 | -14.2% | 0.30 | +20.1% |
| 2025 | -13.5%| 0.42 | +25.2% |
| 2026 YTD | -7.8% | 1.80 | +2.2% |

> CSI 300 full-period max drawdown: **-42.13%** (2021 peak to 2024 trough).  
> Strategy full-period max drawdown: **-36.25%** — shallower overall, but concentrated in a shorter window due to rapid sector reversals.

---

## ETF Universe

The model rotates across **14 liquid A-Share ETFs** spanning broad market indices, sectors, and themes:

| Ticker | Name (English) | Category | 2019–2026 Return | Listed |
|---|---|---|---|---|
| 159949 | Chinext 50 ETF | Growth index | +310.0% | 2019-01-02 |
| 512400 | Non-Ferrous Metals ETF | Materials | +298.3% | 2019-01-02 |
| 515220 | Coal ETF | Energy | +294.9% | 2020-03-02 ⚠️ |
| 512760 | Semiconductor ETF | Tech | +281.0% | 2019-06-12 ⚠️ |
| 518880 | Gold ETF | Commodities | +241.1% | 2019-01-02 |
| 159915 | Chinext ETF | Growth index | +213.2% | 2019-01-02 |
| 512680 | Defense ETF | Defense | +134.7% | 2019-01-02 |
| 510500 | CSI 500 ETF | Mid-cap index | +133.6% | 2019-01-02 |
| **510300** | **CSI 300 ETF** | **Benchmark** | **+100.6%** | 2019-01-02 |
| 510050 | SSE 50 ETF | Large-cap index | +60.7% | 2019-01-02 |
| 512980 | Media ETF | Media | +52.0% | 2019-01-02 |
| 512880 | Securities ETF | Financials | +51.0% | 2019-01-02 |
| 512800 | Banking ETF | Banking | +80.7% | 2019-01-02 |
| 515790 | Solar ETF | Solar | +3.1% | 2020-12-18 ⚠️ |

> ⚠️ = Late-listed ETF. Backtest uses available history only.  
> The wide return dispersion — from Solar +3.1% to Chinext 50 +310% — illustrates why cross-sector rotation adds value in A-Share markets. The model aims to systematically capture this dispersion.

---

## Equity Curve

Cumulative return comparison of the simplified strategy vs CSI 300 ETF (510300), 2019–2026.

![Equity Curve](output/equity_curve.png)

*Log scale · 0.15% one-way transaction cost · Rebalance every 5 trading days.*

> The equity curve clearly shows the 2019 lag (the broad market outpaced the model early),
> the strong 2020–2021 outperformance window, and the 2024–2025 convergence as
> policy-driven broad market recovery narrowed the gap.

---

## Limitations

This simplified implementation, while fully functional for backtesting, has several limitations that users should be aware of:

- **No intraday execution modeling** – Assumes all trades occur at the day's closing price. Real-world fills may differ.
- **No slippage modeling** – Beyond the fixed 0.15% transaction cost, bid-ask spreads and market impact are not modeled.
- **No tax considerations** – Local tax rules may affect net returns.
- **Simplified allocation logic** – Positions are equally weighted among selected ETFs; no volatility targeting or dynamic sizing.
- **Potential look-ahead bias** – Although the code avoids explicit look-ahead, users are encouraged to verify all calculations independently.
- **Survivorship bias** – The ETF universe is fixed to currently available funds; delisted ETFs are not included.

These limitations are typical for academic and research-grade backtests. The extended research version addresses many of these issues.

---

## 🔓 Open Source vs Extended Research

This repository provides a **simplified research edition**. The **extended research package** delivers weekly model updates, risk scores, regime analysis, and real-time paper portfolio tracking — built on the complete risk-controlled model.

| Feature | Open Source (this repo) | Extended Research |
|---|:---:|:---:|
| Simplified momentum + trend filter | ✅ | ✅ |
| Run your own backtests | ✅ | ❌ (not needed) |
| Market regime detection | ❌ | ✅ |
| Weekly model allocations (3–5 ETFs, HIGH/MED/LOW tiers) | ❌ | ✅ |
| Market risk score (0–100) | ❌ | ✅ |
| Drawdown circuit breaker logic | ❌ | ✅ |
| Live paper portfolio tracking | ❌ | ✅ |
| Honest weekly recap (hits & misses) | ❌ | ✅ |
| Full historical research archive | ❌ | ✅ |
| Plain-language model explanation each week | ❌ | ✅ |
| Dynamic position sizing & risk budget | ❌ | ✅ |
| Volatility-adjusted returns (A-Share specific) | ❌ | ✅ |

The simplified model's annual volatility is **24.26%** — more than 5 percentage points above the CSI 300 benchmark. The extended model's risk controls specifically target this gap, improving the Sharpe ratio while preserving most of the alpha.


For extended research updates and live model tracking:

- **A-Share ETF Rotation Model only** – [Access research materials →](https://alpharotationlab.lemonsqueezy.com/checkout/buy/ed1b2e49-e4d9-4ed9-b1e5-9d18b32a69f0)
- **US ETF Rotation Model only** – [Access research materials →](https://alpharotationlab.lemonsqueezy.com/checkout/buy/694902b7-8a2b-41ea-a120-bf187d644a3c)
- **Bundle (A-Share + US)** – [Access research materials →](https://alpharotationlab.lemonsqueezy.com/checkout/buy/728eb9e4-1cd1-49e2-b0d7-b853a929f428)

**Real-time model tracking**: Follow the paper portfolio on Xueqiu at **[ZH3624703](https://xueqiu.com/P/ZH3624703)** for live updates of the A-Share ETF rotation model.

---

## Installation

```bash
git clone https://github.com/AlphaRotationLab/A-Share-ETF-Rotation-Model.git
cd A-Share-ETF-Rotation-Model
pip install -r requirements.txt
```

---

## Requirements

```
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
efinance>=0.4.0
seaborn>=0.12.0
```

---

## Usage

```python
from model import AShareETFRotation

model = AShareETFRotation(
    universe=['510300', '510500', '159915', '512880', '512760',
              '518880', '512800', '512400', '515220', '512680',
              '159949', '510050', '512980', '515790'],
    lookback_days=20,      # momentum lookback (trading days)
    ma_period=200,         # trend filter
    top_n=3,               # number of ETFs to hold
    rebalance_freq=5       # rebalance every N trading days
)

results = model.backtest(start='2019-01-02', end='2026-04-30')
results.plot_equity_curve()
results.print_summary()
```

---

## Data Source

Price data is fetched via `efinance` (adjusted closing prices, no token required). No paid data subscription is needed to run the backtest.

**Data quality note:** `efinance` provides prices adjusted for dividends and splits. For ETFs with a short listing history (`512760`, `515220`, `515790`), results prior to their listing date are excluded — the backtest does not back-fill or simulate these periods.

---

## License

MIT License. See [LICENSE](LICENSE) for details.

---

## Full Disclaimer

This repository and all associated materials are provided for educational and research purposes only. Nothing in this repository constitutes investment advice, financial advice, trading advice, or any other form of advice.

- Past backtest performance does not guarantee future results
- Backtests are subject to look-ahead bias, survivorship bias, and overfitting risk
- The simplified model in this repository carries higher volatility than the CSI 300 benchmark
- A-Share markets are subject to regulatory, liquidity, and policy risks not captured in historical backtests
- Live trading involves costs, slippage, and market impact not fully captured in backtests
- The authors assume no liability for any financial losses arising from use of this code or information

Always consult a qualified financial professional before making investment decisions.
