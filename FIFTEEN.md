# 15-Minute 1¢ Study

*Updated Wed Sep 30, 2:35 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 91 finished bets | 2% | $14.50 | +107% | +15.93¢ | $21.25 / -$6.75 |

*Expect about **40 buys a day** (~$6.07/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 91 | -$0.00 | -0% |
| Momentum model ≥ 5%, hold to the close | 150 | -$2.80 | -17% |
| Volatility model ≥ 5%, sell at 25¢ | 136 | -$4.47 | -31% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 2907 | 2901 | 13 (0%) | 1.07% | -$172.15 (-49%) | Hold to the close: -$172.15 (-49%) |

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
| Volatility model | 1613 | 2.8% | 0.3% (5) | -438% | ❌ Worse |
| Momentum model | 1613 | 2.9% | 0.3% (5) | -485% | ❌ Worse |
| Mean-reversion model | 1613 | 5.7% | 0.3% (5) | -552% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1613 | 5 | -61% | -90% | -91% | -88% |
| Volatility model ≥ 2% | 299 | 2 | -23% | -86% | -87% | -84% |
| Volatility model ≥ 5% | 136 | 0 | -100% | -77% | -76% | -68% |
| Volatility model ≥ 10% | 74 | 0 | -100% | -73% | -71% | -61% |
| Momentum model ≥ 2% | 265 | 1 | -55% | -86% | -89% | -88% |
| Momentum model ≥ 5% | 150 | 1 | -17% | -81% | -86% | -81% |
| Momentum model ≥ 10% | 93 | 0 | -100% | -86% | -83% | -78% |
| Mean-reversion model ≥ 2% | 598 | 3 | -46% | -87% | -87% | -83% |
| Mean-reversion model ≥ 5% | 385 | 3 | -17% | -83% | -83% | -75% |
| Mean-reversion model ≥ 10% | 234 | 2 | -5% | -78% | -79% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1809 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 880 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 212 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 2901 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 13 | 0% | -$172.15 | -49% | — |
| Sell at 2¢ | 107 | 4% | -$326.33 | -92% | 47 sec |
| Sell at 3¢ | 68 | 2% | -$327.63 | -93% | 48 sec |
| Sell at 5¢ | 49 | 2% | -$322.30 | -91% | 64 sec |
| Sell at 10¢ | 40 | 1% | -$287.75 | -81% | 82 sec |
| Sell at 25¢ | 20 | 1% | -$273.95 | -77% | 1.7 min |
| Sell at 50¢ | 11 | 0% | -$237.90 | -67% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 91 | 2 | 10% | 2% | +107% | -83% | -88% |
| 2–5 min | 961 | 6 | 6% | 3% | -39% | -89% | -90% |
| 1–2 min | 778 | 4 | 4% | 2% | -45% | -93% | -92% |
| Under 1 min | 1071 | 1 | 1% | 0% | -86% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 204 | 1 | 4% | 1% | -37% | -91% | -91% |
| ZEC | 203 | 1 | 5% | 3% | -41% | -88% | -90% |
| ETH | 202 | 2 | 5% | 3% | +19% | -89% | -87% |
| NEAR | 201 | 0 | 5% | 1% | -100% | -88% | -91% |
| XRP | 201 | 2 | 2% | 2% | +29% | -94% | -93% |
| SOL | 201 | 0 | 3% | 1% | -100% | -92% | -91% |
| BTC | 199 | 0 | 6% | 2% | -100% | -86% | -91% |
| HYPE | 199 | 1 | 5% | 3% | -37% | -88% | -86% |
| BNB | 199 | 0 | 2% | 1% | -100% | -96% | -97% |
| GOLD | 157 | 0 | 5% | 1% | -100% | -89% | -91% |
| SILVER | 138 | 0 | 2% | 1% | -100% | -95% | -95% |
| WTI | 137 | 1 | 4% | 1% | -22% | -93% | -94% |
| COPPER | 128 | 0 | 1% | 1% | -100% | -99% | -98% |
| NATGAS | 119 | 1 | 3% | 2% | -22% | -94% | -91% |
| PLATINUM | 102 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 99 | 0 | 1% | 0% | -100% | -98% | -100% |
| GBPUSD | 77 | 1 | 5% | 3% | +21% | -91% | -90% |
| EURUSD | 71 | 1 | 4% | 1% | +31% | -93% | -96% |
| USDJPY | 64 | 2 | 3% | 3% | +192% | -95% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1519 | 8 | 4% | 2% | -40% | -92% | -92% |
| DOWN (bought NO) | 1382 | 5 | 4% | 2% | -58% | -92% | -93% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 184 | 0 | 2% | 2% | -100% | -92% | -91% |
| 0.05–0.1% | 242 | 0 | 1% | 0% | -100% | -96% | -98% |
| 0.1–0.2% | 430 | 1 | 3% | 1% | -69% | -92% | -93% |
| 0.2–0.5% | 664 | 2 | 6% | 3% | -67% | -88% | -89% |
| Over 0.5% | 288 | 4 | 6% | 2% | +44% | -89% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 707 | 2 | 4% | 1% | -68% | -91% | -94% |
| Morning (6am–12pm) | 647 | 6 | 4% | 2% | +7% | -91% | -90% |
| Afternoon (12–6pm) | 583 | 1 | 3% | 1% | -81% | -94% | -97% |
| Evening (6pm–12am) | 964 | 4 | 4% | 2% | -52% | -92% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,623 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 2:29:56 AM | COPPER | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:29:39 AM | ZEC | UP | 21 sec | -0.115% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:29:23 AM | EURUSD | DOWN | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:29:23 AM | BTC | DOWN | 37 sec | +0.022% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:28:52 AM | HYPE | DOWN | 67 sec | +0.107% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:28:35 AM | GOLD | DOWN | 85 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:28:19 AM | NATGAS | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:28:19 AM | PLATINUM | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:28:03 AM | SOL | DOWN | 1.9 min | +0.235% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:27:48 AM | XRP | DOWN | 2.2 min | +0.322% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:27:48 AM | ETH | DOWN | 2.2 min | +0.094% | 2¢ | ❌ Lost | -$0.15 |
| 9/30 2:27:33 AM | BNB | DOWN | 2.4 min | +0.062% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:27:33 AM | PALLADIUM | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:27:01 AM | DOGE | DOWN | 3.0 min | +0.315% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:27:01 AM | GBPUSD | DOWN | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:25:10 AM | NEAR | DOWN | 4.8 min | +1.444% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:14:47 AM | USDJPY | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:13:58 AM | GBPUSD | UP | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:13:27 AM | COPPER | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:13:27 AM | HYPE | UP | 1.5 min | -0.205% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:12:23 AM | PALLADIUM | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:12:23 AM | NEAR | UP | 2.6 min | -1.008% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:11:51 AM | XRP | UP | 3.1 min | -0.400% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:11:51 AM | BTC | UP | 3.1 min | -0.195% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:11:35 AM | DOGE | UP | 3.4 min | -0.359% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:11:35 AM | SOL | UP | 3.4 min | -0.331% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:11:03 AM | ETH | UP | 3.9 min | -0.272% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:10:15 AM | BNB | UP | 4.7 min | -0.179% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:09:26 AM | ZEC | UP | 5.6 min | -0.682% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 1:59:46 AM | NEAR | UP | 14 sec | -0.233% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
