# 15-Minute 1¢ Study

*Updated Mon Oct 19, 11:47 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2085 finished bets | 1% | $88.45 | +38% | +4.24¢ | $25.85 / $62.60 |

*Expect about **95 buys a day** (~$14.24/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1918 | $69.55 | +33% |
| Momentum model ≥ 2%, hold to the close | 3199 | -$10.85 | -3% |
| Volatility model ≥ 5%, sell at 50¢ | 2085 | -$28.55 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 24635 | 24628 | 90 (0%) | 1.07% | -$1,731.30 (-58%) | Hold to the close: -$1,731.30 (-58%) |

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
| Volatility model | 16157 | 4.6% | 0.4% (64) | -678% | ❌ Worse |
| Momentum model | 16157 | 4.6% | 0.4% (64) | -700% | ❌ Worse |
| Mean-reversion model | 16157 | 7.7% | 0.4% (64) | -816% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16157 | 64 | -51% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3770 | 30 | -9% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2085 | 23 | +38% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 1217 | 15 | +73% | -59% | -58% | -55% |
| Momentum model ≥ 2% | 3199 | 26 | -3% | -78% | -78% | -75% |
| Momentum model ≥ 5% | 1918 | 20 | +33% | -73% | -73% | -69% |
| Momentum model ≥ 10% | 1274 | 13 | +40% | -66% | -65% | -60% |
| Mean-reversion model ≥ 2% | 6297 | 41 | -29% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 4383 | 33 | -17% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2900 | 22 | -13% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16355 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5775 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2498 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 24628 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 90 | 0% | -$1,731.30 | -58% | — |
| Sell at 2¢ | 888 | 4% | -$2,648.42 | -89% | 46 sec |
| Sell at 3¢ | 600 | 2% | -$2,645.30 | -88% | 47 sec |
| Sell at 5¢ | 428 | 2% | -$2,601.10 | -87% | 50 sec |
| Sell at 10¢ | 260 | 1% | -$2,510.70 | -84% | 64 sec |
| Sell at 25¢ | 143 | 1% | -$2,321.97 | -78% | 79 sec |
| Sell at 50¢ | 93 | 0% | -$2,097.55 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 948 | 5 | 10% | 3% | -50% | -82% | -84% |
| 2–5 min | 7986 | 40 | 7% | 3% | -51% | -88% | -88% |
| 1–2 min | 6283 | 24 | 3% | 2% | -58% | -92% | -92% |
| Under 1 min | 9407 | 21 | 1% | 0% | -68% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1839 | 11 | 4% | 2% | -25% | -90% | -90% |
| HYPE | 1828 | 6 | 5% | 2% | -60% | -89% | -88% |
| BNB | 1827 | 9 | 5% | 2% | -39% | -82% | -81% |
| ETH | 1817 | 9 | 6% | 3% | -40% | -87% | -86% |
| DOGE | 1817 | 3 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1813 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1807 | 7 | 3% | 1% | -52% | -87% | -88% |
| NEAR | 1804 | 9 | 6% | 3% | -36% | -79% | -80% |
| BTC | 1803 | 10 | 5% | 2% | -26% | -88% | -90% |
| GOLD | 948 | 1 | 3% | 1% | -87% | -93% | -94% |
| SILVER | 917 | 4 | 3% | 1% | -50% | -81% | -81% |
| WTI | 890 | 3 | 3% | 1% | -60% | -94% | -96% |
| COPPER | 793 | 2 | 2% | 1% | -76% | -85% | -85% |
| PLATINUM | 784 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 729 | 5 | 2% | 2% | -36% | -84% | -83% |
| EURUSD | 724 | 3 | 2% | 1% | -61% | -83% | -83% |
| PALLADIUM | 714 | 2 | 1% | 0% | -74% | -85% | -85% |
| GBPUSD | 678 | 1 | 2% | 1% | -86% | -97% | -97% |
| USDJPY | 632 | 3 | 1% | 1% | -56% | -99% | -98% |
| AUDUSD | 259 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 205 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12415 | 43 | 4% | 2% | -60% | -89% | -88% |
| DOWN (bought NO) | 12213 | 47 | 3% | 1% | -56% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2780 | 15 | 2% | 1% | -10% | -77% | -76% |
| 0.05–0.1% | 2846 | 10 | 3% | 2% | -49% | -92% | -91% |
| 0.1–0.2% | 4109 | 13 | 5% | 2% | -61% | -89% | -89% |
| 0.2–0.5% | 4764 | 22 | 6% | 3% | -49% | -88% | -88% |
| Over 0.5% | 1853 | 6 | 6% | 3% | -67% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6064 | 24 | 4% | 2% | -55% | -86% | -86% |
| Morning (6am–12pm) | 5814 | 29 | 4% | 2% | -43% | -87% | -86% |
| Afternoon (12–6pm) | 5807 | 19 | 3% | 1% | -61% | -89% | -89% |
| Evening (6pm–12am) | 6943 | 18 | 3% | 2% | -70% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,816 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/19 11:44:55 PM | XRP | DOWN | 5 sec | +0.008% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 11:44:55 PM | EURUSD | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 11:44:39 PM | WTI | DOWN | 20 sec | — | 1¢ | ❌ Lost | $0.00 |
| 10/19 11:44:39 PM | GOLD | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 11:44:23 PM | USDJPY | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 11:44:23 PM | HYPE | UP | 36 sec | -0.147% | 0¢ | ❌ Lost | $0.00 |
| 10/19 11:44:07 PM | ZEC | UP | 52 sec | -0.247% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 11:44:07 PM | DOGE | UP | 52 sec | -0.073% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 11:44:07 PM | SOL | UP | 52 sec | -0.090% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 11:42:33 PM | PLATINUM | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 11:42:17 PM | SILVER | DOWN | 2.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 11:42:01 PM | BTC | UP | 3.0 min | -0.120% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 11:40:10 PM | NATGAS | UP | 4.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 11:39:54 PM | ETH | UP | 5.1 min | -0.225% | 4¢ | ❌ Lost | -$0.15 |
| 10/19 11:39:54 PM | BNB | UP | 5.1 min | -0.183% | 2¢ | ❌ Lost | -$0.15 |
| 10/19 11:29:44 PM | USDJPY | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 11:29:44 PM | USDCAD | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 11:29:12 PM | EURUSD | DOWN | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 11:28:56 PM | NATGAS | UP | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 11:28:56 PM | WTI | UP | 64 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 11:28:41 PM | BTC | UP | 78 sec | -0.064% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 11:28:41 PM | XRP | UP | 78 sec | -0.107% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 11:28:41 PM | BNB | UP | 78 sec | -0.074% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 11:28:41 PM | GBPUSD | DOWN | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 11:28:25 PM | ETH | UP | 1.6 min | -0.092% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 11:27:38 PM | SILVER | UP | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 11:27:22 PM | HYPE | UP | 2.6 min | -0.279% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 11:27:22 PM | PLATINUM | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 11:27:22 PM | DOGE | UP | 2.6 min | -0.170% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 11:27:22 PM | ZEC | UP | 2.6 min | -0.589% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
