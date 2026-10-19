# 15-Minute 1¢ Study

*Updated Sun Oct 18, 10:07 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1981 finished bets | 1% | $86.75 | +39% | +4.38¢ | $31.85 / $54.90 |

*Expect about **95 buys a day** (~$14.22/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1820 | $66.65 | +33% |
| Momentum model ≥ 2%, hold to the close | 3033 | -$4.15 | -1% |
| Volatility model ≥ 2%, hold to the close | 3577 | -$28.70 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 23267 | 23260 | 88 (0%) | 1.07% | -$1,588.15 (-56%) | Hold to the close: -$1,588.15 (-56%) |

*In play or awaiting result: 6. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 15401 | 4.6% | 0.4% (62) | -671% | ❌ Worse |
| Momentum model | 15401 | 4.6% | 0.4% (62) | -694% | ❌ Worse |
| Mean-reversion model | 15401 | 7.7% | 0.4% (62) | -805% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 15401 | 62 | -50% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 3577 | 29 | -7% | -80% | -79% | -75% |
| Volatility model ≥ 5% | 1981 | 22 | +39% | -76% | -75% | -72% |
| Volatility model ≥ 10% | 1165 | 14 | +69% | -70% | -68% | -66% |
| Momentum model ≥ 2% | 3033 | 25 | -1% | -82% | -82% | -78% |
| Momentum model ≥ 5% | 1820 | 19 | +33% | -80% | -79% | -75% |
| Momentum model ≥ 10% | 1213 | 12 | +37% | -76% | -75% | -70% |
| Mean-reversion model ≥ 2% | 5981 | 40 | -27% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 4155 | 32 | -15% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 2751 | 21 | -13% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 15599 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5394 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2267 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 23260 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 88 | 0% | -$1,588.15 | -56% | — |
| Sell at 2¢ | 840 | 4% | -$2,503.75 | -89% | 44 sec |
| Sell at 3¢ | 569 | 2% | -$2,500.24 | -89% | 47 sec |
| Sell at 5¢ | 408 | 2% | -$2,456.95 | -87% | 50 sec |
| Sell at 10¢ | 247 | 1% | -$2,370.58 | -84% | 63 sec |
| Sell at 25¢ | 137 | 1% | -$2,184.68 | -77% | 77 sec |
| Sell at 50¢ | 91 | 0% | -$1,953.90 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 853 | 5 | 10% | 3% | -44% | -82% | -84% |
| 2–5 min | 7587 | 39 | 7% | 3% | -49% | -88% | -88% |
| 1–2 min | 5966 | 24 | 3% | 2% | -56% | -92% | -92% |
| Under 1 min | 8850 | 20 | 1% | 0% | -67% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1752 | 11 | 4% | 2% | -22% | -90% | -90% |
| BNB | 1743 | 8 | 5% | 2% | -44% | -89% | -88% |
| HYPE | 1742 | 6 | 5% | 2% | -58% | -90% | -88% |
| DOGE | 1737 | 3 | 4% | 2% | -78% | -91% | -90% |
| ETH | 1732 | 9 | 6% | 3% | -37% | -87% | -87% |
| SOL | 1730 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1724 | 7 | 3% | 1% | -50% | -87% | -87% |
| NEAR | 1720 | 9 | 6% | 3% | -32% | -79% | -79% |
| BTC | 1719 | 9 | 5% | 2% | -30% | -89% | -90% |
| GOLD | 880 | 1 | 4% | 1% | -87% | -92% | -94% |
| SILVER | 855 | 4 | 3% | 1% | -46% | -80% | -80% |
| WTI | 834 | 3 | 3% | 1% | -58% | -94% | -95% |
| COPPER | 746 | 2 | 2% | 1% | -75% | -84% | -84% |
| PLATINUM | 731 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 679 | 5 | 2% | 2% | -31% | -82% | -81% |
| EURUSD | 674 | 3 | 3% | 1% | -58% | -82% | -82% |
| PALLADIUM | 669 | 2 | 1% | 0% | -72% | -84% | -84% |
| GBPUSD | 625 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 586 | 3 | 1% | 1% | -52% | -99% | -98% |
| AUDUSD | 212 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 170 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 11686 | 42 | 4% | 2% | -59% | -89% | -88% |
| DOWN (bought NO) | 11574 | 46 | 3% | 2% | -54% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2668 | 14 | 2% | 1% | -13% | -82% | -81% |
| 0.05–0.1% | 2711 | 10 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 3909 | 13 | 4% | 2% | -59% | -90% | -89% |
| 0.2–0.5% | 4540 | 21 | 6% | 3% | -49% | -88% | -88% |
| Over 0.5% | 1768 | 6 | 6% | 3% | -65% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5767 | 23 | 4% | 2% | -55% | -87% | -88% |
| Morning (6am–12pm) | 5489 | 28 | 4% | 2% | -41% | -87% | -86% |
| Afternoon (12–6pm) | 5549 | 19 | 3% | 1% | -59% | -88% | -89% |
| Evening (6pm–12am) | 6455 | 18 | 3% | 2% | -68% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,862 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/18 9:59:58 PM | HYPE | UP | 2 sec | -0.053% | 0¢ | ❌ Lost | $0.00 |
| 10/18 9:59:58 PM | USDJPY | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 9:59:58 PM | ZEC | DOWN | 2 sec | +0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/18 9:59:58 PM | XRP | UP | 2 sec | -0.031% | 0¢ | ❌ Lost | $0.00 |
| 10/18 9:59:44 PM | PALLADIUM | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 9:59:40 PM | ETH | DOWN | 20 sec | +0.033% | 0¢ | ❌ Lost | $0.00 |
| 10/18 9:59:38 PM | SOL | UP | 22 sec | -0.027% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 9:59:36 PM | EURUSD | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 9:59:28 PM | NATGAS | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 9:59:11 PM | BTC | UP | 48 sec | -0.030% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 9:59:11 PM | GOLD | DOWN | 48 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/18 9:59:01 PM | BNB | DOWN | 58 sec | +0.000% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 9:58:39 PM | NEAR | DOWN | 81 sec | +0.211% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 9:58:39 PM | COPPER | DOWN | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 9:58:37 PM | SILVER | DOWN | 83 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/18 9:57:39 PM | DOGE | UP | 2.4 min | -0.211% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 9:44:53 PM | XRP | UP | 6 sec | -0.053% | 0¢ | ❌ Lost | $0.00 |
| 10/18 9:44:49 PM | BNB | UP | 10 sec | -0.058% | 0¢ | ❌ Lost | $0.00 |
| 10/18 9:44:43 PM | USDJPY | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 9:44:41 PM | SOL | UP | 18 sec | -0.072% | 0¢ | ❌ Lost | $0.00 |
| 10/18 9:44:23 PM | HYPE | DOWN | 36 sec | -0.016% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 9:44:23 PM | PLATINUM | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 9:44:19 PM | ZEC | DOWN | 40 sec | +0.129% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 9:44:14 PM | DOGE | UP | 46 sec | -0.134% | 0¢ | ❌ Lost | $0.00 |
| 10/18 9:43:38 PM | BTC | UP | 82 sec | -0.086% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 9:43:30 PM | COPPER | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 9:43:14 PM | WTI | UP | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/18 9:43:08 PM | ETH | UP | 1.9 min | -0.120% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 9:43:04 PM | EURUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 9:41:40 PM | NEAR | DOWN | 3.3 min | +0.434% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
