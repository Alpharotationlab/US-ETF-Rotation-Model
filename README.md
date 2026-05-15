# \# US ETF Rotation Model – Simplified

# 

# Open-source ETF rotation model for the US market.  

# This repository provides a \*\*simplified, research-grade implementation\*\* of a momentum-based ETF rotation strategy combined with a 200-day moving average trend filter. Designed for quantitative research, backtesting, and educational purposes.

# 

# > 📌 \*\*Disclaimer\*\* – Nothing herein constitutes investment advice. Past performance does not guarantee future results.

# 

# \---

# 

# \## Table of Contents

# 

# \- \[Overview](#overview)

# \- \[Research Philosophy](#research-philosophy)

# \- \[Strategy Logic](#strategy-logic)

# \- \[Simplified vs Full Model](#simplified-vs-full-model--key-differences)

# \- \[Backtest Summary](#backtest-summary)

# \- \[Annual Performance](#annual-performance-breakdown)

# \- \[Risk Metrics](#risk-metrics)

# \- \[ETF Universe](#etf-universe)

# \- \[Equity Curve](#equity-curve)

# \- \[Limitations](#limitations)

# \- \[Open Source vs Extended Research](#-open-source-vs-extended-research)

# \- \[Installation](#installation)

# \- \[Usage](#usage)

# \- \[Data Source](#data-source)

# \- \[License](#license)

# \- \[Full Disclaimer](#full-disclaimer)

# 

# \---

# 

# \## Overview

# 

# This repository contains a \*\*simplified research edition\*\* of a US ETF rotation framework based on:

# 

# \- Relative momentum ranking (multi-period, default \~6 months)

# \- 200-day moving average trend filter

# \- Weekly rebalancing

# \- 0.15% one-way transaction cost assumption

# 

# The code includes:

# 

# \- Historical backtesting engine

# \- `yfinance`-based data pipeline (no token required)

# \- Performance evaluation metrics

# \- ETF universe of 20 liquid US sector and thematic ETFs

# \- Simplified research implementation

# 

# The goal is to provide a transparent, reproducible, and \*\*trustworthy\*\* baseline for systematic US ETF allocation research.

# 

# \---

# 

# \## Research Philosophy

# 

# This repository is \*\*not\*\* an attempt to ship a "magic" trading strategy. It serves as an \*\*educational and transparent research framework\*\* for ETF rotation strategies built on momentum and trend-following.

# 

# The simplified implementation intentionally emphasizes:

# 

# \- \*\*Clarity\*\* – Code is written for humans, not machines.

# \- \*\*Reproducibility\*\* – Run `python run\_backtest.py` and obtain the exact same results.

# \- \*\*Educational value\*\* – Understand how momentum ranking + trend filter interact.

# 

# The extended research version (available separately) builds on this foundation with:

# 

# \- Multi-factor ranking (not just momentum)

# \- Dynamic risk management and regime detection

# \- Adaptive position sizing

# \- Weekly model updates with full transparency

# 

# The open-source version alone is a \*\*solid, correct, and useful\*\* starting point for anyone interested in systematic US ETF allocation. It is not "crippled" — it is a genuine research implementation you can trust, with well-understood limitations.

# 

# \---

# 

# \## Strategy Logic

# 

# The simplified model follows these steps:

# 

# 1\. Select a universe of 20 liquid US ETFs (see `config.py`)

# 2\. Rank ETFs by momentum over a \*\*126-day lookback\*\* (\~6 months)

# 3\. Apply trend filter: current price must be above its \*\*200-day simple moving average\*\*

# 4\. Hold the \*\*top 3\*\* ETFs that satisfy the trend condition

# 5\. Rebalance \*\*weekly\*\*

# 

# This open-source version uses \*\*default parameters\*\* that are reasonable and widely accepted in the momentum-rotation literature. Users are encouraged to experiment with different settings.

# 

# \---

# 

# \## Simplified vs Full Model — Key Differences

# 

# > ⚠️ \*\*Read this section before interpreting the backtest results.\*\*

# 

# The simplified model achieves meaningfully higher raw returns than the S\&P 500 benchmark over the 2019–2026 period. This comes with a real trade-off: the model also carries \*\*higher drawdown risk\*\* (max drawdown \~−38% to −42% vs benchmark −33.7%) and does not include any regime-based defensive mechanism.

# 

# | Component | Simplified (this repo) | Full Model |

# |---|:---:|:---:|

# | Momentum ranking | ✅ | ✅ |

# | 200-day MA trend filter | ✅ | ✅ |

# | Market regime detection | ❌ | ✅ |

# | Risk budget \& position sizing | ❌ | ✅ |

# | Drawdown circuit breaker | ❌ | ✅ |

# | Defensive allocation (short-term bonds) | ❌ | ✅ |

# 

# \*\*Why this matters in practice:\*\*

# 

# The 2019–2026 period was dominated by a strong AI/tech-driven bull market. In this environment, the simplified model's lack of defensive filters allowed it to maintain full exposure to high-momentum ETFs such as SOXX (+815% over the period), QTUM (+588%), and QQQ (+347%), which inflated its raw return.

# 

# However, this same absence of risk controls produced \*\*two drawdown episodes significantly deeper than the S\&P 500\*\* — most visibly in 2020 and 2022. The full model explicitly trades \~0.75% per year in CAGR for materially better Sharpe, Calmar, and a maximum drawdown roughly 30% shallower than the benchmark. For real capital management, those risk metrics matter far more than peak backtest CAGR.

# 

# \---

# 

# \## Backtest Summary

# 

# \*\*Period:\*\* 2019-01-01 – 2026-04-30 · \*\*Benchmark:\*\* S\&P 500 (SPY) · \*\*One-way fee:\*\* 0.15% · \*\*Rebalance:\*\* Weekly

# 

# \### Simplified Model (this repository)

# 

# | Metric | Simplified Model | S\&P 500 |

# |---|---|---|

# | Total Return | \~+290% | +227% |

# | CAGR | \~20% | 17.56% |

# | Max Drawdown | \~−38% to −42% | −33.72% |

# | Sharpe Ratio | \~0.80–0.90 | 0.824 |

# | Calmar Ratio | \~0.45–0.55 | 0.521 |

# 

# > ⚠️ The simplified model \*\*exceeds the benchmark's maximum drawdown\*\* in at least two periods. Higher raw returns reflect greater risk exposure, not superior risk-adjusted performance.

# 

# \### Full Model (reference, not included in this repo)

# 

# | Metric | Full Model | S\&P 500 |

# |---|---|---|

# | Total Return | +212.16% | +227.04% |

# | CAGR | 16.81% | 17.56% |

# | Max Drawdown | \*\*−23.58%\*\* | −33.72% |

# | Sharpe Ratio | \*\*0.937\*\* | 0.824 |

# | Calmar Ratio | \*\*0.713\*\* | 0.521 |

# 

# The full model sacrifices \~75 bps of annual return in exchange for a 30% shallower max drawdown and the highest Sharpe and Calmar ratios of the three. This is the intended design goal.

# 

# \---

# 

# \## Annual Performance Breakdown

# 

# \### Simplified Model vs S\&P 500

# 

# | Year | Simplified Model | S\&P 500 | Excess |

# |---|---|---|---|

# | 2019 | \~+28% | +31.09% | \~−3% |

# | 2020 | \~+38% | +17.24% | \~+21% |

# | 2021 | \~+35% | +30.51% | \~+5% |

# | 2022 | \~−25% | −18.65% | \~−6% ⚠️ |

# | 2023 | \~+28% | +26.71% | \~+1% |

# | 2024 | \~+22% | +25.59% | \~−4% |

# | 2025 | \~+24% | +18.01% | \~+6% |

# 

# > Simplified model annual figures are estimates derived from the equity curve. Run the code for exact values.

# 

# \### Full Model vs S\&P 500 (reference)

# 

# | Year | Full Model | S\&P 500 | Excess |

# |---|---|---|---|

# | 2019 | +27.29% | +31.09% | −3.80% |

# | 2020 | +30.60% | +17.24% | +13.36% |

# | 2021 | +22.01% | +30.51% | −8.50% |

# | 2022 | −17.78% | −18.65% | +0.87% |

# | 2023 | +21.97% | +26.71% | −4.74% |

# | 2024 | +5.16% | +25.59% | −20.43% |

# | 2025 | +21.73% | +18.01% | +3.72% |

# | 2026 YTD | +17.99% | +7.71% | +10.28% |

# 

# \*\*Interpretation:\*\* The full model's worst single-year miss was 2024 (−20.43% excess), when an unprecedented concentration of mega-cap AI stocks drove S\&P 500 returns. The model's regime filters correctly identified elevated risk, reducing exposure — this cost returns in 2024 but was the same mechanism that limited drawdown to −23.58% during the 2020 crash and −17.78% during the 2022 bear market.

# 

# \---

# 

# \## Risk Metrics

# 

# \### Full Model by Year (reference)

# 

# | Year | Max Drawdown | Sharpe | Calmar |

# |---|---|---|---|

# | 2019 | −7.95% | 2.076 | 3.43 |

# | 2020 | −21.80% | 1.256 | 1.40 |

# | 2021 | −5.45% | 1.302 | 4.04 |

# | 2022 | −23.58% | −1.135 | −0.76 |

# | 2023 | −11.30% | 1.364 | 1.96 |

# | 2024 | −12.40% | 0.282 | 0.42 |

# | 2025 | −9.82% | 1.287 | 2.23 |

# | 2026 YTD | −7.53% | 3.029 | 8.28 |

# 

# Notable risk events:

# \- \*\*2020 COVID crash:\*\* Full model −21.80% vs S\&P 500 −33.72% — defensive rotation protected 11.9 percentage points at the most critical moment

# \- \*\*2022 bear market:\*\* Full model −17.78% vs S\&P 500 −18.65% — short-duration bond rotation flipped excess return positive

# 

# \---

# 

# \## ETF Universe

# 

# The model rotates across \*\*20 liquid US sector and thematic ETFs\*\*:

# 

# | Ticker | Description | 2019–2026 Return |

# |---|---|---|

# | SOXX | Semiconductor | +815% |

# | QTUM | Quantum / Next-gen tech | +588% |

# | QQQ | Nasdaq 100 | +347% |

# | PAVE | Infrastructure | +328% |

# | COPX | Copper miners | +394% |

# | TAN | Solar energy | +202% |

# | XHB | Homebuilders | +238% |

# | XLI | Industrials | +196% |

# | SPY | S\&P 500 (benchmark) | +217% |

# | IGV | Software | +146% |

# | DBC | Commodities | +150% |

# | XLF | Financials | +148% |

# | XLE | Energy | +179% |

# | REMX | Rare earth / materials | +182% |

# | XLB | Materials | +132% |

# | BOTZ | Robotics \& AI | +128% |

# | KBE | Banking | +105% |

# | ITA | Aerospace \& defense | +164% |

# | XBI | Biotech | +78% |

# | CLOU | Cloud computing | +35% |

# 

# > Returns calculated from 2019-01-02 to 2026-04-29 using adjusted closing prices. High dispersion across the universe (SOXX +815% vs CLOU +35%) is precisely what momentum-based rotation is designed to exploit — but also what makes risk control critical when momentum reverses.

# 

# \---

# 

# \## Equity Curve

# 

# Cumulative return comparison of the simplified strategy vs S\&P 500 (SPY), 2019–2026.

# 

# !\[Equity Curve](images/equity\_curve.png)

# 

# \*Log scale · 0.15% one-way transaction cost · Weekly rebalance.\*

# 

# > The equity curve shows the 2019 lag, the strong 2020–2021 outperformance, and the two drawdown episodes where the simplified model temporarily falls below or significantly underperforms SPY — reflecting the absence of defensive risk controls in this edition.

# 

# \---

# 

# \## Limitations

# 

# This simplified implementation, while fully functional for backtesting, has several limitations that users should be aware of:

# 

# \- \*\*No intraday execution modeling\*\* – Assumes all trades occur at the day's close. Real-world fills may differ.

# \- \*\*No slippage modeling\*\* – Beyond the fixed 0.15% transaction cost, we do not model bid-ask spreads or market impact.

# \- \*\*No tax considerations\*\* – Local tax rules may affect net returns.

# \- \*\*Simplified allocation logic\*\* – Positions are equally weighted among selected ETFs; no volatility targeting or dynamic sizing.

# \- \*\*Look-ahead bias\*\* – Although the code avoids explicit look-ahead, users should verify all calculations.

# \- \*\*Survivorship bias\*\* – The ETF universe is fixed to currently available funds; delisted ETFs are not included.

# 

# These limitations are typical for academic and research-grade backtests. The extended research version addresses many of these issues.

# 

# \---

# 

# \## 🔓 Open Source vs Extended Research

# 

# This repository provides a \*\*simplified research edition\*\*. The \*\*extended research package\*\* delivers weekly model updates, risk scores, regime analysis, and real-time paper portfolio tracking — built on the complete risk-controlled model.

# 

# | Feature | Open Source (this repo) | Extended Research |

# |---|:---:|:---:|

# | Simplified momentum + trend filter | ✅ | ✅ |

# | Run your own backtests | ✅ | ❌ (not needed) |

# | Market regime detection | ❌ | ✅ |

# | Weekly model allocations (3–5 ETFs, HIGH/MED/LOW tiers) | ❌ | ✅ |

# | Market risk score (0–100) | ❌ | ✅ |

# | Drawdown circuit breaker logic | ❌ | ✅ |

# | Live paper portfolio tracking | ❌ | ✅ |

# | Honest weekly recap (hits \& misses) | ❌ | ✅ |

# | Full historical research archive | ❌ | ✅ |

# | Plain-language model explanation each week | ❌ | ✅ |

# | Dynamic position sizing \& risk budget | ❌ | ✅ |

# | Risk-adjusted return (Sharpe/Calmar) | Lower ⚠️ | Higher ✅ |

# 

# The simplified model's drawdown risk is \*\*significantly higher\*\* than the S\&P 500 benchmark. The extended model's risk controls specifically target this gap, improving the Sharpe and Calmar ratios while preserving most of the alpha.

# 

# For extended research updates and live model tracking:

# 

# \- \*\*US ETF Rotation Model only\*\* – \[Access research materials →](https://alpharotationlab.lemonsqueezy.com/checkout/buy/694902b7-8a2b-41ea-a120-bf187d644a3c)  

# \- \*\*A-Share ETF Rotation Model only\*\* – \[Access research materials →](https://alpharotationlab.lemonsqueezy.com/checkout/buy/ed1b2e49-e4d9-4ed9-b1e5-9d18b32a69f0)  

# \- \*\*Bundle (US + A-Share)\*\* – \[Access research materials →](https://alpharotationlab.lemonsqueezy.com/checkout/buy/728eb9e4-1cd1-49e2-b0d7-b853a929f428)  

# 

# \---

# 

# \## Installation

# 

# ```bash

# git clone https://github.com/AlphaRotationLab/US-ETF-Rotation-Model.git

# cd US-ETF-Rotation-Model

# pip install -r requirements.txt

# Requirements

# text

# yfinance>=0.2.0

# pandas>=2.0.0

# numpy>=1.24.0

# matplotlib>=3.7.0

# Usage

# python

# from model import USETFRotation

# 

# model = USETFRotation(

# &#x20;   universe=\['QQQ', 'SOXX', 'XLF', 'XLE', 'XLI', 'XLB', 'TAN', 'PAVE',

# &#x20;             'COPX', 'XHB', 'IGV', 'DBC', 'REMX', 'BOTZ', 'KBE', 'ITA', 'XBI', 'CLOU'],

# &#x20;   lookback\_days=126,      # momentum lookback (trading days)

# &#x20;   ma\_period=200,          # trend filter

# &#x20;   top\_n=3,                # number of ETFs to hold

# &#x20;   rebalance\_freq=5        # rebalance every N trading days (weekly)

# )

# 

# results = model.backtest(start='2019-01-01', end='2026-04-30')

# results.plot\_equity\_curve()

# results.print\_summary()

# Data Source

# Price data is fetched via yfinance (adjusted closing prices). No paid data subscription is needed to run the backtest.

# 

# Data quality note: yfinance provides adjusted prices that account for dividends and splits. For ETFs with shorter listing histories, results prior to their listing date are simply excluded — the backtest does not back-fill or simulate these periods.

# 

# License

# MIT License. See LICENSE for details.

# 

# Full Disclaimer

# This repository and all associated materials are provided for educational and research purposes only. Nothing in this repository constitutes investment advice, financial advice, trading advice, or any other form of advice.

# 

# Past backtest performance does not guarantee future results

# 

# Backtests are subject to look-ahead bias, survivorship bias, and overfitting risk

# 

# The simplified model in this repository carries higher drawdown risk than the S\&P 500 benchmark in certain market conditions

# 

# US markets are subject to regulatory, liquidity, and macroeconomic risks not captured in historical backtests

# 

# Live trading involves costs, slippage, and market impact not fully captured in backtests

# 

# The authors assume no liability for any financial losses arising from use of this code or information

# 

# Always consult a qualified financial professional before making investment decisions.

