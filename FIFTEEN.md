# 15-Minute 1¢ Study

*Updated Sat Oct 31, 8:03 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3293 finished bets | 1% | $93.45 | +25% | +2.84¢ | $83.30 / $10.15 |

*Expect about **99 buys a day** (~$14.83/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3051 | $44.85 | +13% |
| Volatility model ≥ 2%, hold to the close | 6083 | $4.75 | +1% |
| Momentum model ≥ 2%, hold to the close | 5022 | -$63.55 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 40574 | 40564 | 150 (0%) | 1.07% | -$2,847.30 (-58%) | Hold to the close: -$2,847.30 (-58%) |

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
| Volatility model | 24964 | 4.7% | 0.4% (97) | -695% | ❌ Worse |
| Momentum model | 24964 | 4.6% | 0.4% (97) | -718% | ❌ Worse |
| Mean-reversion model | 24964 | 8.1% | 0.4% (97) | -844% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 24964 | 97 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6083 | 53 | +1% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3293 | 33 | +25% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1865 | 20 | +53% | -69% | -67% | -64% |
| Momentum model ≥ 2% | 5022 | 37 | -11% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3051 | 27 | +13% | -78% | -78% | -73% |
| Momentum model ≥ 10% | 1991 | 18 | +25% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 10272 | 68 | -27% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7195 | 58 | -11% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4810 | 40 | -6% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 25165 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9712 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5687 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 40564 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 150 | 0% | -$2,847.30 | -58% | — |
| Sell at 2¢ | 1570 | 4% | -$4,315.10 | -87% | 47 sec |
| Sell at 3¢ | 1080 | 3% | -$4,302.10 | -87% | 48 sec |
| Sell at 5¢ | 749 | 2% | -$4,222.45 | -85% | 63 sec |
| Sell at 10¢ | 449 | 1% | -$4,051.11 | -82% | 65 sec |
| Sell at 25¢ | 235 | 1% | -$3,749.45 | -76% | 83 sec |
| Sell at 50¢ | 154 | 0% | -$3,403.80 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1898 | 9 | 11% | 4% | -55% | -80% | -81% |
| 2–5 min | 12942 | 70 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 10262 | 35 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 15451 | 36 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2817 | 13 | 5% | 3% | -41% | -88% | -88% |
| HYPE | 2809 | 8 | 5% | 2% | -65% | -89% | -87% |
| BNB | 2807 | 16 | 5% | 2% | -28% | -85% | -84% |
| SOL | 2804 | 8 | 4% | 2% | -64% | -91% | -91% |
| DOGE | 2797 | 6 | 4% | 2% | -73% | -90% | -89% |
| ETH | 2795 | 11 | 6% | 3% | -52% | -85% | -85% |
| NEAR | 2780 | 13 | 5% | 2% | -39% | -83% | -83% |
| BTC | 2779 | 13 | 5% | 2% | -37% | -88% | -89% |
| XRP | 2777 | 11 | 3% | 1% | -51% | -89% | -89% |
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
| UP (bought YES) | 20585 | 82 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 19979 | 68 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4044 | 20 | 2% | 1% | -14% | -82% | -81% |
| 0.05–0.1% | 4283 | 14 | 3% | 2% | -51% | -92% | -91% |
| 0.1–0.2% | 6465 | 22 | 4% | 2% | -58% | -90% | -89% |
| 0.2–0.5% | 7495 | 32 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2874 | 11 | 7% | 3% | -61% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10116 | 36 | 4% | 2% | -59% | -86% | -86% |
| Morning (6am–12pm) | 10183 | 46 | 4% | 2% | -49% | -85% | -84% |
| Afternoon (12–6pm) | 9463 | 33 | 4% | 2% | -59% | -87% | -87% |
| Evening (6pm–12am) | 10802 | 35 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,556 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/31 7:59:22 AM | BTC | UP | 38 sec | -0.049% | 0¢ | ❌ Lost | $0.00 |
| 10/31 7:59:22 AM | ZEC | DOWN | 38 sec | +0.104% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 7:59:22 AM | ETH | DOWN | 38 sec | -0.004% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 7:58:02 AM | NEAR | UP | 2.0 min | -0.353% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 7:57:14 AM | HYPE | UP | 2.8 min | -0.350% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 7:56:58 AM | BNB | UP | 3.0 min | -0.199% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 7:56:58 AM | XRP | UP | 3.0 min | -0.136% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 7:56:42 AM | DOGE | UP | 3.3 min | -0.155% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 7:55:54 AM | SOL | UP | 4.1 min | -0.312% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 7:44:26 AM | BNB | UP | 34 sec | -0.045% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 7:44:26 AM | HYPE | DOWN | 34 sec | +0.052% | 0¢ | ❌ Lost | $0.00 |
| 10/31 7:42:51 AM | BTC | DOWN | 2.1 min | +0.056% | 3¢ | ❌ Lost | -$0.15 |
| 10/31 7:42:15 AM | DOGE | DOWN | 2.8 min | +0.098% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 7:42:15 AM | XRP | DOWN | 2.8 min | +0.080% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 7:41:43 AM | ETH | DOWN | 3.3 min | +0.093% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 7:41:27 AM | ZEC | DOWN | 3.5 min | +0.515% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 7:40:39 AM | NEAR | DOWN | 4.3 min | +0.526% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 7:40:23 AM | SOL | DOWN | 4.6 min | +0.247% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 7:29:55 AM | SOL | UP | 4 sec | -0.032% | 0¢ | ❌ Lost | $0.00 |
| 10/31 7:29:39 AM | BTC | UP | 20 sec | -0.026% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 7:29:39 AM | BNB | UP | 20 sec | -0.072% | 0¢ | ❌ Lost | $0.00 |
| 10/31 7:29:07 AM | DOGE | DOWN | 52 sec | +0.049% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 7:28:51 AM | ETH | DOWN | 68 sec | +0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/31 7:28:35 AM | HYPE | DOWN | 84 sec | +0.179% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 7:28:19 AM | ZEC | UP | 1.7 min | -0.269% | 0¢ | ❌ Lost | $0.00 |
| 10/31 7:26:59 AM | XRP | DOWN | 3.0 min | +0.064% | 4¢ | ❌ Lost | -$0.15 |
| 10/31 7:25:55 AM | NEAR | UP | 4.1 min | -0.599% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 7:14:13 AM | ZEC | DOWN | 46 sec | +0.186% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 7:14:13 AM | BNB | UP | 46 sec | -0.091% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 7:13:43 AM | NEAR | UP | 76 sec | -0.354% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
