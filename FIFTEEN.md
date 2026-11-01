# 15-Minute 1¢ Study

*Updated Sat Oct 31, 8:07 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3340 finished bets | 1% | $102.80 | +28% | +3.08¢ | $80.60 / $22.20 |

*Expect about **99 buys a day** (~$14.82/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3093 | $54.95 | +16% |
| Volatility model ≥ 2%, hold to the close | 6166 | $9.60 | +1% |
| Momentum model ≥ 2%, hold to the close | 5092 | -$56.75 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 40963 | 40953 | 151 (0%) | 1.07% | -$2,873.05 (-58%) | Hold to the close: -$2,873.05 (-58%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 25352 | 4.7% | 0.4% (98) | -699% | ❌ Worse |
| Momentum model | 25352 | 4.6% | 0.4% (98) | -721% | ❌ Worse |
| Mean-reversion model | 25352 | 8.1% | 0.4% (98) | -850% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 25352 | 98 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6166 | 54 | +1% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3340 | 34 | +28% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1894 | 21 | +58% | -69% | -67% | -64% |
| Momentum model ≥ 2% | 5092 | 38 | -10% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3093 | 28 | +16% | -78% | -78% | -73% |
| Momentum model ≥ 10% | 2022 | 19 | +31% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 10427 | 69 | -27% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7305 | 59 | -10% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4884 | 41 | -5% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 25554 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9712 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5687 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 40953 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 151 | 0% | -$2,873.05 | -58% | — |
| Sell at 2¢ | 1591 | 4% | -$4,349.39 | -87% | 47 sec |
| Sell at 3¢ | 1095 | 3% | -$4,336.00 | -87% | 48 sec |
| Sell at 5¢ | 757 | 2% | -$4,257.00 | -85% | 63 sec |
| Sell at 10¢ | 454 | 1% | -$4,084.31 | -82% | 65 sec |
| Sell at 25¢ | 238 | 1% | -$3,779.27 | -76% | 82 sec |
| Sell at 50¢ | 155 | 0% | -$3,436.80 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1921 | 9 | 11% | 4% | -55% | -80% | -81% |
| 2–5 min | 13063 | 70 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 10364 | 35 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 15594 | 37 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2862 | 13 | 5% | 3% | -42% | -88% | -88% |
| HYPE | 2851 | 8 | 5% | 2% | -65% | -89% | -87% |
| SOL | 2850 | 9 | 4% | 2% | -60% | -91% | -91% |
| BNB | 2849 | 16 | 5% | 2% | -30% | -85% | -84% |
| DOGE | 2841 | 6 | 4% | 2% | -73% | -90% | -89% |
| ETH | 2839 | 11 | 6% | 3% | -53% | -85% | -85% |
| NEAR | 2821 | 13 | 5% | 2% | -40% | -83% | -83% |
| BTC | 2821 | 13 | 5% | 2% | -38% | -88% | -89% |
| XRP | 2820 | 11 | 3% | 1% | -52% | -89% | -89% |
| GOLD | 1515 | 5 | 5% | 2% | -60% | -82% | -83% |
| SILVER | 1481 | 7 | 4% | 2% | -44% | -82% | -81% |
| WTI | 1476 | 4 | 3% | 1% | -67% | -93% | -93% |
| PLATINUM | 1314 | 3 | 2% | 1% | -79% | -96% | -96% |
| COPPER | 1253 | 5 | 1% | 1% | -63% | -75% | -75% |
| EURUSD | 1249 | 3 | 2% | 1% | -78% | -89% | -88% |
| NATGAS | 1212 | 7 | 2% | 1% | -46% | -81% | -80% |
| GBPUSD | 1185 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1178 | 2 | 1% | 0% | -84% | -90% | -91% |
| USDJPY | 1171 | 5 | 2% | 1% | -60% | -97% | -96% |
| AUDUSD | 705 | 4 | 2% | 1% | -47% | -84% | -83% |
| USDCAD | 685 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 283 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 188 | 1 | 5% | 2% | -50% | -41% | -39% |
| 30YRRATE | 177 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 170 | 2 | 5% | 1% | +10% | +18% | +19% |
| 5YRRATE | 157 | 1 | 6% | 3% | -41% | -89% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 20778 | 82 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 20175 | 69 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4148 | 21 | 2% | 1% | -12% | -82% | -81% |
| 0.05–0.1% | 4372 | 14 | 3% | 2% | -52% | -92% | -91% |
| 0.1–0.2% | 6579 | 22 | 4% | 2% | -58% | -90% | -89% |
| 0.2–0.5% | 7564 | 32 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2886 | 11 | 7% | 3% | -61% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10116 | 36 | 4% | 2% | -59% | -86% | -86% |
| Morning (6am–12pm) | 10310 | 46 | 4% | 2% | -49% | -85% | -84% |
| Afternoon (12–6pm) | 9655 | 34 | 4% | 2% | -59% | -87% | -87% |
| Evening (6pm–12am) | 10872 | 35 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,639 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/31 7:58:57 PM | NEAR | UP | 63 sec | -0.277% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 7:57:38 PM | BNB | UP | 2.4 min | -0.147% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 7:57:13 PM | BTC | UP | 2.8 min | -0.085% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 7:55:17 PM | ZEC | UP | 4.7 min | -0.400% | 3¢ | ❌ Lost | -$0.15 |
| 10/31 7:55:17 PM | ETH | UP | 4.7 min | -0.162% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 7:55:17 PM | HYPE | UP | 4.7 min | -0.344% | 2¢ | ❌ Lost | -$0.15 |
| 10/31 7:54:45 PM | DOGE | UP | 5.2 min | -0.273% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 7:53:57 PM | SOL | UP | 6.0 min | -0.255% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 7:53:06 PM | XRP | UP | 6.9 min | -0.303% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 7:44:19 PM | ZEC | DOWN | 40 sec | +0.156% | 0¢ | ❌ Lost | $0.00 |
| 10/31 7:44:19 PM | BNB | DOWN | 40 sec | -0.061% | 0¢ | ❌ Lost | $0.00 |
| 10/31 7:43:29 PM | DOGE | DOWN | 1.5 min | +0.092% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 7:42:26 PM | NEAR | DOWN | 2.5 min | +0.289% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 7:42:09 PM | BTC | DOWN | 2.8 min | +0.098% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 7:42:09 PM | SOL | DOWN | 2.8 min | +0.114% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 7:41:52 PM | XRP | DOWN | 3.1 min | +0.152% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 7:39:58 PM | ETH | DOWN | 5.0 min | +0.276% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 7:38:52 PM | HYPE | DOWN | 6.1 min | +0.474% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 7:29:47 PM | ETH | UP | 12 sec | -0.069% | 0¢ | ❌ Lost | $0.00 |
| 10/31 7:29:47 PM | SOL | UP | 12 sec | -0.066% | 0¢ | ❌ Lost | $0.00 |
| 10/31 7:29:47 PM | HYPE | UP | 12 sec | -0.048% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 7:29:31 PM | ZEC | UP | 28 sec | -0.055% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 7:29:31 PM | BTC | UP | 28 sec | -0.047% | 0¢ | ❌ Lost | $0.00 |
| 10/31 7:29:31 PM | DOGE | UP | 28 sec | -0.130% | 0¢ | ❌ Lost | $0.00 |
| 10/31 7:28:56 PM | XRP | UP | 63 sec | -0.088% | 0¢ | ❌ Lost | $0.00 |
| 10/31 7:26:29 PM | BNB | UP | 3.5 min | -0.230% | 0¢ | ❌ Lost | $0.00 |
| 10/31 7:24:20 PM | NEAR | DOWN | 5.7 min | +0.696% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 7:14:47 PM | BTC | DOWN | 13 sec | +0.000% | 0¢ | ❌ Lost | $0.00 |
| 10/31 7:14:47 PM | BNB | DOWN | 13 sec | -0.072% | 0¢ | ❌ Lost | $0.00 |
| 10/31 7:14:47 PM | SOL | UP | 13 sec | -0.029% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
