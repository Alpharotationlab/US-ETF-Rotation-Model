# US ETF Rotation Model — Simplified Research Edition

[中文版本](README_CN.md)

Open-source ETF rotation framework for the US market.

This repository provides a **simplified, research-grade implementation** of a momentum-based ETF rotation strategy combined with a 200-day moving average trend filter, designed for quantitative research, backtesting, and educational purposes.

> 📌 \*\*Disclaimer\*\*  
> Nothing herein constitutes investment advice. Past performance does not guarantee future results.

\---

## Table of Contents

* [Overview](#overview)
* [Research Philosophy](#research-philosophy)
* [Why ETF Rotation?](#why-etf-rotation)
* [Characteristics of the US ETF Market](#characteristics-of-the-us-etf-market)
* [Strategy Logic](#strategy-logic)
* [Simplified vs Extended Model](#simplified-vs-extended-model)
* [Backtest Summary](#backtest-summary)
* [Annual Performance](#annual-performance)
* [Risk Metrics](#risk-metrics)
* [ETF Universe](#etf-universe)
* [Equity Curve](#equity-curve)
* [FAQ](#faq)
* [Risk Disclosure](#risk-disclosure)
* [Open Source vs Extended Research Version](#open-source-vs-extended-research-version)
* [Public Paper Portfolio Tracking](#public-paper-portfolio-tracking)
* [Installation](#installation)
* [Requirements](#requirements)
* [Usage](#usage)
* [Data Source](#data-source)
* [License](#license)
* [Full Disclaimer](#full-disclaimer)

\---

## Overview

This repository provides a simplified research implementation of a US ETF rotation framework based on:

* Relative momentum ranking (20-day lookback)
* 200-day moving average trend filter
* Rebalancing every 5 trading days
* 0.10% one-way transaction cost assumption

The project includes:

* Historical backtesting engine
* `yfinance`-based data pipeline
* Performance evaluation metrics
* Multiple liquid US ETFs
* Simplified research implementation

The goal of this repository is to provide a transparent, reproducible, verifiable, and trustworthy framework for systematic ETF allocation research.

> This open-source repository is intended as a transparent and reproducible research framework, not a production-ready trading system.

\---

## Research Philosophy

This repository is not an attempt to provide a "magic trading strategy." Instead, it aims to build a research framework that is transparent, reproducible, educational, and understandable.

The simplified research edition intentionally emphasizes:

* **Clarity** — code written for humans rather than optimization contests
* **Reproducibility** — running `python run\_backtest.py` should produce consistent results
* **Educational value** — understanding how momentum ranking and trend filtering interact

The extended research version further incorporates:

* Multi-factor ranking
* Market environment analysis
* Risk scoring framework
* Dynamic risk management
* Weekly model observations

The open-source version itself is a genuine and functional research implementation — not merely a placeholder demo.

\---

## Why ETF Rotation?

Compared with individual stock strategies, ETF rotation offers several advantages:

* Lower single-company risk
* Reduced earnings surprise exposure
* Better suitability for systematic investing
* More stable long-term backtests
* Improved liquidity and execution

The US market consistently exhibits sector rotation, style rotation, interest-rate regime shifts, and changing risk appetite. Performance dispersion across ETFs can become substantial over time.

The purpose of ETF rotation is not to predict markets, but to systematically follow relative strength through rules-based allocation.

\---

## Characteristics of the US ETF Market

Compared with many international markets, the US ETF ecosystem features:

|Feature|US ETF Market|
|-|-|
|Institutional participation|Very high|
|Long-term trend persistence|Strong|
|ETF liquidity|Extremely high|
|Sector coverage|Comprehensive|
|Global capital influence|Significant|
|Long-term bull market tendency|Historically strong|

As a result, US ETF rotation strategies tend to focus more on trend following, asset rotation, and risk-adjusted returns rather than short-term speculative trading.

\---

## Strategy Logic

The simplified model follows these steps:

1. Build a universe of liquid US ETFs
2. Rank ETFs by trailing 20-day momentum
3. Require current price to remain above the 200-day moving average
4. Hold the top 3 ETFs satisfying the trend condition
5. Rebalance every 5 trading days

The parameters used in this repository are intentionally simple and widely accepted in momentum-rotation literature. Users are encouraged to experiment with alternative configurations.

\---

## Simplified vs Extended Model

> ⚠️ \*\*Please read this section carefully before interpreting the backtest results.\*\*

While the simplified model can outperform SPY during certain market environments, it may also experience higher volatility, concentrated exposure, rotation failures, and temporary underperformance.

|Component|Simplified (This Repo)|Extended Version|
|-|:-:|:-:|
|Momentum ranking|✅|✅|
|200-day MA trend filter|✅|✅|
|Market environment analysis|❌|✅|
|Dynamic position sizing|❌|✅|
|Risk observation framework|❌|✅|
|Defensive allocation|❌|✅|
|Volatility monitoring|❌|✅|

The extended research version introduces additional risk-control layers aimed at improving long-term risk-adjusted returns.

\---

## Backtest Summary

**Period:** 2019-01-01 – 2026-04-30 · **Benchmark:** SPY (S\&P 500 ETF) · **One-way fee:** 0.10% · **Rebalance:** Every 5 trading days

|Metric|Strategy (Simplified)|SPY|
|-|-|-|
|Total Return|+212.16%|+227.04%|
|CAGR|16.81%|17.56%|
|Max Drawdown|−23.58%|−33.72%|
|Sharpe Ratio|0.937|0.824|
|Calmar Ratio|0.713|0.521|

> ⚠️ Although the simplified model slightly underperforms SPY in total return, it demonstrates superior risk-adjusted performance as measured by Sharpe and Calmar ratios, with a meaningfully shallower max drawdown.

\---

## Annual Performance

|Year|Strategy|SPY|Excess Return|
|-|-|-|-|
|2019|+27.29%|+31.09%|−3.80%|
|2020|+30.60%|+17.24%|+13.36%|
|2021|+22.01%|+30.51%|−8.50%|
|2022|−17.78%|−18.65%|+0.87%|
|2023|+21.97%|+26.71%|−4.74%|
|2024|+5.16%|+25.59%|−20.43%|
|2025|+21.73%|+18.01%|+3.72%|
|2026 YTD|+17.99%|+7.71%|+10.28%|

\---

## Risk Metrics

|Year|Strategy Max DD|Strategy Sharpe|SPY Annual Return|
|-|-|-|-|
|2019|−7.95%|2.076|+31.09%|
|2020|−21.80%|1.256|+17.24%|
|2021|−5.45%|1.302|+30.51%|
|2022|−23.58%|−1.135|−18.65%|
|2023|−11.30%|1.364|+26.71%|
|2024|−12.40%|0.282|+25.59%|
|2025|−9.82%|1.287|+18.01%|
|2026 YTD|−7.53%|3.029|+7.71%|

\---

## ETF Universe

The model rotates among multiple liquid US ETFs, including:

|Ticker|Category|
|-|-|
|SPY|S\&P 500|
|QQQ|Nasdaq 100|
|IWM|Russell 2000|
|XLK|Technology|
|XLE|Energy|
|XLF|Financials|
|XLI|Industrials|
|XLV|Healthcare|
|GLD|Gold|
|TLT|Long-term Treasury Bonds|

The allocation dynamically shifts depending on momentum and trend conditions.

\---

## Equity Curve

Cumulative return comparison between the simplified strategy and SPY, 2019–2026.



!\[Equity Curve](https://raw.githubusercontent.com/Alpharotationlab/US-ETF-Rotation-Model/main/output/equity\_curve.png)



*Log scale · 0.10% one-way transaction cost · Rebalance every 5 trading days.*

\---

## FAQ

### Why can the model underperform SPY in some years?

Rotation strategies do not outperform continuously. During periods when mega-cap technology dominates, AI-driven rallies become highly concentrated, or broad-market momentum is extremely strong, a diversified rotation framework may lag SPY or QQQ.

The model prioritizes long-term risk-adjusted returns, drawdown control, and portfolio stability rather than maximizing short-term upside.

### Why use the 200-day moving average?

The 200-day moving average is one of the most widely used long-term trend filters in systematic investing. Its purpose is not prediction, but avoiding prolonged bear markets, improving risk-adjusted returns, and reducing catastrophic drawdowns.

### Why hold only the top 3 ETFs?

Concentrated exposure increases momentum capture and rotation efficiency, but also introduces higher volatility and deeper short-term drawdowns. The extended model mitigates this through additional risk-management layers.

### Why ETF rotation instead of stock picking?

ETF rotation generally offers better diversification, lower idiosyncratic risk, improved liquidity, and more stable systematic behavior, making it particularly suitable for quantitative research frameworks.

\---

## Risk Disclosure

ETF rotation strategies are not low-risk investments. This model may experience momentum crashes, trend reversals, macro regime shifts, liquidity shocks, concentrated sector drawdowns, and extended periods of underperformance.

Backtests also involve limitations such as survivorship bias, execution differences, and historical overfitting risk. Historical results should never be interpreted as guarantees of future returns.

\---

## Open Source vs Extended Research Version

This repository provides a **Simplified Research Edition**. The extended research version includes market environment analysis, a risk scoring framework, weekly model observations, a full historical research archive, public paper portfolio tracking, research notes and model commentary, and additional advanced research materials.

For extended research updates and live model tracking:

* **A-Share ETF Rotation Model** – [Access research materials →](https://alpharotationlab.lemonsqueezy.com/checkout/buy/ed1b2e49-e4d9-4ed9-b1e5-9d18b32a69f0)
* **US ETF Rotation Model** – [Access research materials →](https://alpharotationlab.lemonsqueezy.com/checkout/buy/694902b7-8a2b-41ea-a120-bf187d644a3c)
* **A-Share + US Bundle** – [Access research materials →](https://alpharotationlab.lemonsqueezy.com/checkout/buy/728eb9e4-1cd1-49e2-b0d7-b853a929f428)

\---

## Public Paper Portfolio Tracking

* **TradingView Paper Portfolio** – [View portfolio →](https://tw.tradingview.com/portfolios/54cb931a7c7d4524af796571b7f4a178/)
* **Xueqiu Paper Portfolio** – Portfolio ID: `ZH3624707`

These portfolios are intended for research observation and model-behavior tracking only. They do not constitute investment advice.

\---

## Installation

```bash
git clone https://github.com/AlphaRotationLab/US-ETF-Rotation-Model.git
cd US-ETF-Rotation-Model
pip install -r requirements.txt
```

\---

## Requirements

```
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
yfinance>=0.2.0
seaborn>=0.12.0
```

\---

## Usage

```python
from model import USETFRotationModel

model = USETFRotationModel(
    universe=\[
        'SPY', 'QQQ', 'IWM',
        'XLK', 'XLE', 'XLF',
        'GLD', 'TLT'
    ],
    lookback\_days=20,
    ma\_period=200,
    top\_n=3,
    rebalance\_freq=5
)

results = model.backtest(
    start='2019-01-01',
    end='2026-04-30'
)

results.plot\_equity\_curve()
results.print\_summary()
```

\---

## Data Source

Price data is retrieved through `yfinance` (Yahoo Finance). The repository uses publicly available market data and does not require paid subscriptions. Backtests are calculated using adjusted historical ETF prices.

Some ETFs may exhibit historical differences due to later inception dates, incomplete data history, or Yahoo Finance adjustments. The framework automatically uses the available historical data for each ETF.

\---

## License

MIT License. See [LICENSE](LICENSE) for details.

\---

## Full Disclaimer

This repository and all associated materials are provided strictly for educational and research purposes. Nothing contained herein constitutes investment advice, financial advice, trading advice, or asset management advice.

* Past backtest performance does not guarantee future results
* Backtests may contain survivorship bias, look-ahead bias, and overfitting risk
* Real-world trading involves slippage, market impact, liquidity constraints, and execution differences not fully captured in backtests
* The author assumes no responsibility for any financial losses resulting from the use of this repository

Always conduct your own research and consult qualified professionals before making investment decisions.

