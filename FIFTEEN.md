# 15-Minute 1¢ Study

*Updated Tue Sep 29, 8:06 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 66 finished bets | 3% | $18.10 | +183% | +27.42¢ | $23.05 / -$4.95 |

*Expect about **45 buys a day** (~$6.70/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 244 | $10.35 | +33% |
| 5+ min left, sell at 50¢ | 66 | $3.60 | +36% |
| Volatility model ≥ 5%, sell at 25¢ | 90 | $0.48 | +5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1910 | 1904 | 8 (0%) | 1.07% | -$117.50 (-51%) | Hold to the close: -$117.50 (-51%) |

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
| Volatility model | 1009 | 2.8% | 0.4% (4) | -404% | ❌ Worse |
| Momentum model | 1009 | 2.9% | 0.4% (4) | -471% | ❌ Worse |
| Mean-reversion model | 1009 | 6.0% | 0.4% (4) | -501% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1009 | 4 | -49% | -89% | -91% | -86% |
| Volatility model ≥ 2% | 197 | 1 | -41% | -86% | -87% | -84% |
| Volatility model ≥ 5% | 90 | 0 | -100% | -72% | -71% | -66% |
| Volatility model ≥ 10% | 47 | 0 | -100% | -69% | -63% | -54% |
| Momentum model ≥ 2% | 160 | 0 | -100% | -86% | -90% | -90% |
| Momentum model ≥ 5% | 94 | 0 | -100% | -82% | -89% | -87% |
| Momentum model ≥ 10% | 59 | 0 | -100% | -86% | -79% | -77% |
| Mean-reversion model ≥ 2% | 374 | 3 | -13% | -86% | -86% | -81% |
| Mean-reversion model ≥ 5% | 244 | 3 | +33% | -83% | -83% | -75% |
| Mean-reversion model ≥ 10% | 157 | 2 | +44% | -77% | -78% | -70% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1204 | 4% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 588 | 2% | 1% | 0% | 0% | 0% | 0% |
| Financials | 112 | 4% | 3% | 2% | 2% | 2% | 2% |
| **All** | 1904 | 3% | 2% | 1% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 8 | 0% | -$117.50 | -51% | — |
| Sell at 2¢ | 66 | 3% | -$212.34 | -93% | 47 sec |
| Sell at 3¢ | 39 | 2% | -$214.29 | -93% | 47 sec |
| Sell at 5¢ | 28 | 1% | -$211.30 | -92% | 81 sec |
| Sell at 10¢ | 25 | 1% | -$196.75 | -86% | 1.9 min |
| Sell at 25¢ | 13 | 1% | -$186.47 | -81% | 2.1 min |
| Sell at 50¢ | 9 | 0% | -$168.75 | -74% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 66 | 2 | 9% | 3% | +183% | -84% | -88% |
| 2–5 min | 631 | 5 | 6% | 3% | -23% | -89% | -90% |
| 1–2 min | 529 | 1 | 3% | 1% | -80% | -95% | -95% |
| Under 1 min | 678 | 0 | 1% | 0% | -100% | -97% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 137 | 2 | 5% | 4% | +83% | -88% | -85% |
| ZEC | 136 | 1 | 6% | 2% | -9% | -87% | -92% |
| DOGE | 135 | 1 | 4% | 2% | -7% | -90% | -87% |
| NEAR | 134 | 0 | 4% | 1% | -100% | -88% | -94% |
| BTC | 134 | 0 | 9% | 3% | -100% | -78% | -86% |
| XRP | 134 | 2 | 3% | 2% | +89% | -93% | -92% |
| SOL | 133 | 0 | 2% | 2% | -100% | -94% | -91% |
| BNB | 131 | 0 | 2% | 1% | -100% | -95% | -95% |
| HYPE | 130 | 0 | 3% | 2% | -100% | -93% | -92% |
| GOLD | 101 | 0 | 2% | 0% | -100% | -96% | -100% |
| SILVER | 93 | 0 | 2% | 0% | -100% | -95% | -96% |
| WTI | 92 | 0 | 1% | 0% | -100% | -98% | -100% |
| COPPER | 85 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 80 | 0 | 4% | 1% | -100% | -94% | -90% |
| PLATINUM | 75 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 62 | 0 | 2% | 0% | -100% | -97% | -100% |
| GBPUSD | 42 | 0 | 2% | 0% | -100% | -96% | -94% |
| USDJPY | 36 | 2 | 6% | 6% | +419% | -90% | -86% |
| EURUSD | 34 | 0 | 3% | 0% | -100% | -95% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 998 | 5 | 4% | 2% | -41% | -92% | -92% |
| DOWN (bought NO) | 906 | 3 | 3% | 1% | -62% | -93% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 121 | 0 | 2% | 2% | -100% | -91% | -91% |
| 0.05–0.1% | 146 | 0 | 1% | 0% | -100% | -95% | -96% |
| 0.1–0.2% | 279 | 0 | 4% | 1% | -100% | -91% | -92% |
| 0.2–0.5% | 457 | 2 | 5% | 3% | -52% | -89% | -91% |
| Over 0.5% | 201 | 4 | 7% | 3% | +111% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 577 | 1 | 3% | 1% | -80% | -93% | -96% |
| Morning (6am–12pm) | 408 | 4 | 4% | 2% | +14% | -92% | -92% |
| Afternoon (12–6pm) | 330 | 1 | 2% | 1% | -65% | -95% | -96% |
| Evening (6pm–12am) | 589 | 2 | 4% | 2% | -60% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,695 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 45 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/29 7:59:38 AM | DOGE | DOWN | 22 sec | +0.015% | 0¢ | ❌ Lost | $0.00 |
| 9/29 7:59:38 AM | GOLD | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:59:22 AM | SOL | UP | 38 sec | -0.087% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 7:59:07 AM | BNB | DOWN | 53 sec | +0.037% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 7:59:07 AM | HYPE | UP | 53 sec | -0.154% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:59:07 AM | XRP | UP | 53 sec | -0.200% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 7:58:33 AM | SILVER | DOWN | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:56:41 AM | ZEC | DOWN | 3.3 min | +0.782% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 7:56:25 AM | ETH | DOWN | 3.6 min | +0.317% | 10¢ | ❌ Lost | -$0.15 |
| 9/29 7:56:09 AM | BTC | DOWN | 3.8 min | +0.312% | 7¢ | ❌ Lost | -$0.15 |
| 9/29 7:55:05 AM | NEAR | DOWN | 4.9 min | +2.570% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 7:44:58 AM | SOL | UP | 1 sec | -0.055% | 0¢ | ❌ Lost | $0.00 |
| 9/29 7:44:58 AM | COPPER | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:44:58 AM | SILVER | UP | 1 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/29 7:44:26 AM | PLATINUM | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:43:38 AM | XRP | DOWN | 81 sec | +0.453% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 7:43:38 AM | ZEC | DOWN | 81 sec | +0.449% | 24¢ | ❌ Lost | -$0.15 |
| 9/29 7:43:38 AM | WTI | DOWN | 81 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 7:43:38 AM | NEAR | DOWN | 81 sec | +0.760% | 0¢ | ❌ Lost | $0.00 |
| 9/29 7:43:22 AM | BNB | UP | 1.6 min | -0.177% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 7:43:22 AM | NATGAS | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:43:22 AM | DOGE | UP | 1.6 min | -0.330% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:43:06 AM | BTC | UP | 1.9 min | -0.219% | 2¢ | ❌ Lost | -$0.15 |
| 9/29 7:42:48 AM | USDJPY | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:42:01 AM | HYPE | UP | 3.0 min | -0.361% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 7:41:45 AM | ETH | UP | 3.2 min | -0.367% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 7:29:45 AM | ETH | DOWN | 15 sec | +0.068% | 0¢ | ❌ Lost | $0.00 |
| 9/29 7:29:45 AM | PLATINUM | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 7:29:29 AM | BTC | UP | 31 sec | -0.045% | 0¢ | ❌ Lost | $0.00 |
| 9/29 7:29:29 AM | ZEC | UP | 31 sec | -0.139% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
