# 15-Minute 1¢ Study

*Updated Wed Sep 30, 3:05 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 91 finished bets | 2% | $14.50 | +107% | +15.93¢ | $21.25 / -$6.75 |

*Expect about **40 buys a day** (~$6.02/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 91 | -$0.00 | -0% |
| Momentum model ≥ 5%, hold to the close | 153 | -$3.10 | -18% |
| Volatility model ≥ 5%, sell at 25¢ | 141 | -$5.07 | -34% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 2938 | 2932 | 13 (0%) | 1.07% | -$176.50 (-49%) | Hold to the close: -$176.50 (-49%) |

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
| Volatility model | 1631 | 2.8% | 0.3% (5) | -460% | ❌ Worse |
| Momentum model | 1631 | 2.9% | 0.3% (5) | -507% | ❌ Worse |
| Mean-reversion model | 1631 | 5.7% | 0.3% (5) | -577% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1631 | 5 | -62% | -90% | -91% | -88% |
| Volatility model ≥ 2% | 304 | 2 | -24% | -86% | -87% | -84% |
| Volatility model ≥ 5% | 141 | 0 | -100% | -77% | -77% | -70% |
| Volatility model ≥ 10% | 77 | 0 | -100% | -74% | -72% | -63% |
| Momentum model ≥ 2% | 271 | 1 | -56% | -86% | -89% | -88% |
| Momentum model ≥ 5% | 153 | 1 | -18% | -82% | -86% | -81% |
| Momentum model ≥ 10% | 95 | 0 | -100% | -86% | -83% | -79% |
| Mean-reversion model ≥ 2% | 602 | 3 | -47% | -87% | -87% | -83% |
| Mean-reversion model ≥ 5% | 388 | 3 | -17% | -84% | -83% | -76% |
| Mean-reversion model ≥ 10% | 237 | 2 | -6% | -78% | -79% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1827 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 890 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 215 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 2932 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 13 | 0% | -$176.50 | -49% | — |
| Sell at 2¢ | 107 | 4% | -$330.68 | -92% | 47 sec |
| Sell at 3¢ | 68 | 2% | -$331.98 | -93% | 48 sec |
| Sell at 5¢ | 49 | 2% | -$326.65 | -91% | 64 sec |
| Sell at 10¢ | 40 | 1% | -$292.10 | -81% | 82 sec |
| Sell at 25¢ | 20 | 1% | -$278.30 | -78% | 1.7 min |
| Sell at 50¢ | 11 | 0% | -$242.25 | -68% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 91 | 2 | 10% | 2% | +107% | -83% | -88% |
| 2–5 min | 970 | 6 | 6% | 3% | -40% | -89% | -90% |
| 1–2 min | 788 | 4 | 4% | 2% | -46% | -93% | -92% |
| Under 1 min | 1083 | 1 | 1% | 0% | -86% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 206 | 1 | 4% | 1% | -37% | -91% | -91% |
| ZEC | 205 | 1 | 5% | 3% | -42% | -88% | -90% |
| ETH | 204 | 2 | 5% | 3% | +17% | -89% | -87% |
| NEAR | 203 | 0 | 5% | 1% | -100% | -88% | -91% |
| XRP | 203 | 2 | 2% | 2% | +27% | -94% | -93% |
| SOL | 203 | 0 | 3% | 1% | -100% | -93% | -91% |
| BTC | 201 | 0 | 6% | 2% | -100% | -86% | -91% |
| HYPE | 201 | 1 | 5% | 3% | -38% | -89% | -86% |
| BNB | 201 | 0 | 2% | 0% | -100% | -96% | -97% |
| GOLD | 158 | 0 | 5% | 1% | -100% | -89% | -91% |
| SILVER | 140 | 0 | 2% | 1% | -100% | -95% | -95% |
| WTI | 138 | 1 | 4% | 1% | -23% | -93% | -94% |
| COPPER | 130 | 0 | 1% | 1% | -100% | -99% | -98% |
| NATGAS | 120 | 1 | 3% | 2% | -22% | -94% | -91% |
| PLATINUM | 103 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 101 | 0 | 1% | 0% | -100% | -98% | -100% |
| GBPUSD | 78 | 1 | 5% | 3% | +20% | -91% | -90% |
| EURUSD | 72 | 1 | 4% | 1% | +30% | -93% | -96% |
| USDJPY | 65 | 2 | 3% | 3% | +187% | -95% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1536 | 8 | 4% | 2% | -41% | -92% | -92% |
| DOWN (bought NO) | 1396 | 5 | 4% | 2% | -59% | -92% | -93% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 185 | 0 | 2% | 2% | -100% | -92% | -91% |
| 0.05–0.1% | 246 | 0 | 1% | 0% | -100% | -96% | -98% |
| 0.1–0.2% | 437 | 1 | 3% | 1% | -69% | -92% | -93% |
| 0.2–0.5% | 669 | 2 | 6% | 3% | -67% | -88% | -89% |
| Over 0.5% | 289 | 4 | 6% | 2% | +44% | -89% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 738 | 2 | 4% | 1% | -69% | -92% | -94% |
| Morning (6am–12pm) | 647 | 6 | 4% | 2% | +7% | -91% | -90% |
| Afternoon (12–6pm) | 583 | 1 | 3% | 1% | -81% | -94% | -97% |
| Evening (6pm–12am) | 964 | 4 | 4% | 2% | -52% | -92% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,615 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 2:59:58 AM | NATGAS | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:59:58 AM | BTC | DOWN | 1 sec | -0.016% | 0¢ | ❌ Lost | $0.00 |
| 9/30 2:59:41 AM | USDJPY | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:59:25 AM | COPPER | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:58:23 AM | DOGE | DOWN | 1.6 min | +0.186% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:58:23 AM | GBPUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:58:23 AM | PALLADIUM | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:58:23 AM | ETH | DOWN | 1.6 min | +0.120% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:58:07 AM | EURUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:58:07 AM | WTI | DOWN | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:57:51 AM | XRP | DOWN | 2.1 min | +0.207% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:57:35 AM | GOLD | UP | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:57:19 AM | SILVER | UP | 2.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:57:19 AM | HYPE | DOWN | 2.7 min | +0.186% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:57:03 AM | BNB | DOWN | 2.9 min | +0.072% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:57:03 AM | SOL | DOWN | 2.9 min | +0.273% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:56:47 AM | ZEC | DOWN | 3.2 min | +0.416% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:56:31 AM | NEAR | DOWN | 3.5 min | +0.625% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:44:46 AM | NEAR | UP | 14 sec | -0.164% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:44:46 AM | PLATINUM | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:44:30 AM | COPPER | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:44:30 AM | PALLADIUM | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:44:14 AM | BNB | UP | 46 sec | -0.075% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:44:14 AM | SILVER | UP | 46 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:44:14 AM | ZEC | UP | 46 sec | -0.183% | 0¢ | ❌ Lost | $0.00 |
| 9/30 2:44:14 AM | ETH | UP | 46 sec | -0.069% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:43:59 AM | XRP | UP | 60 sec | -0.147% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:43:59 AM | HYPE | DOWN | 60 sec | +0.057% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:43:28 AM | BTC | UP | 1.5 min | -0.112% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:43:12 AM | SOL | UP | 1.8 min | -0.243% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
