# 15-Minute 1¢ Study

*Updated Tue Sep 29, 1:43 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 73 finished bets | 3% | $17.05 | +156% | +23.36¢ | $22.60 / -$5.55 |

*Expect about **43 buys a day** (~$6.40/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 292 | $3.90 | +10% |
| 5+ min left, sell at 50¢ | 73 | $2.55 | +23% |
| Volatility model ≥ 5%, sell at 25¢ | 105 | -$0.87 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 2184 | 2173 | 10 (0%) | 1.07% | -$122.80 (-47%) | Hold to the close: -$122.80 (-47%) |

*In play or awaiting result: 11. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 1165 | 2.9% | 0.3% (4) | -451% | ❌ Worse |
| Momentum model | 1165 | 3.1% | 0.3% (4) | -531% | ❌ Worse |
| Mean-reversion model | 1165 | 6.0% | 0.3% (4) | -538% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1165 | 4 | -56% | -90% | -91% | -87% |
| Volatility model ≥ 2% | 230 | 1 | -49% | -85% | -86% | -84% |
| Volatility model ≥ 5% | 105 | 0 | -100% | -74% | -71% | -64% |
| Volatility model ≥ 10% | 54 | 0 | -100% | -72% | -66% | -58% |
| Momentum model ≥ 2% | 191 | 0 | -100% | -86% | -88% | -88% |
| Momentum model ≥ 5% | 110 | 0 | -100% | -83% | -87% | -84% |
| Momentum model ≥ 10% | 69 | 0 | -100% | -88% | -81% | -79% |
| Mean-reversion model ≥ 2% | 447 | 3 | -28% | -86% | -87% | -83% |
| Mean-reversion model ≥ 5% | 292 | 3 | +10% | -84% | -84% | -78% |
| Mean-reversion model ≥ 10% | 179 | 2 | +26% | -78% | -79% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1360 | 4% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 672 | 2% | 1% | 0% | 0% | 0% | 0% |
| Financials | 141 | 5% | 4% | 3% | 2% | 2% | 1% |
| **All** | 2173 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 10 | 0% | -$122.80 | -47% | — |
| Sell at 2¢ | 79 | 4% | -$242.26 | -92% | 47 sec |
| Sell at 3¢ | 49 | 2% | -$243.69 | -93% | 47 sec |
| Sell at 5¢ | 34 | 2% | -$240.70 | -92% | 72 sec |
| Sell at 10¢ | 29 | 1% | -$210.81 | -80% | 1.6 min |
| Sell at 25¢ | 15 | 1% | -$199.15 | -76% | 2.1 min |
| Sell at 50¢ | 9 | 0% | -$174.05 | -66% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 73 | 2 | 12% | 3% | +156% | -79% | -86% |
| 2–5 min | 733 | 5 | 6% | 3% | -34% | -89% | -90% |
| 1–2 min | 587 | 2 | 3% | 1% | -64% | -94% | -93% |
| Under 1 min | 780 | 1 | 1% | 0% | -80% | -97% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 155 | 2 | 5% | 4% | +60% | -88% | -84% |
| DOGE | 153 | 1 | 4% | 2% | -17% | -91% | -88% |
| ZEC | 153 | 1 | 5% | 2% | -20% | -88% | -93% |
| XRP | 152 | 2 | 3% | 2% | +67% | -94% | -93% |
| BTC | 151 | 0 | 8% | 3% | -100% | -81% | -88% |
| NEAR | 150 | 0 | 5% | 1% | -100% | -86% | -90% |
| SOL | 150 | 0 | 4% | 2% | -100% | -89% | -87% |
| BNB | 149 | 0 | 2% | 1% | -100% | -96% | -96% |
| HYPE | 147 | 0 | 3% | 1% | -100% | -94% | -93% |
| GOLD | 118 | 0 | 3% | 0% | -100% | -94% | -97% |
| WTI | 106 | 0 | 2% | 0% | -100% | -96% | -100% |
| SILVER | 105 | 0 | 3% | 1% | -100% | -94% | -94% |
| COPPER | 98 | 0 | 1% | 1% | -100% | -98% | -97% |
| NATGAS | 92 | 0 | 3% | 1% | -100% | -94% | -92% |
| PLATINUM | 82 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 71 | 0 | 1% | 0% | -100% | -98% | -100% |
| GBPUSD | 54 | 1 | 6% | 2% | +73% | -90% | -90% |
| EURUSD | 46 | 1 | 4% | 2% | +103% | -92% | -94% |
| USDJPY | 41 | 2 | 5% | 5% | +355% | -92% | -87% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1152 | 7 | 4% | 2% | -30% | -92% | -92% |
| DOWN (bought NO) | 1021 | 3 | 4% | 1% | -66% | -92% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 133 | 0 | 2% | 2% | -100% | -91% | -91% |
| 0.05–0.1% | 163 | 0 | 1% | 0% | -100% | -96% | -97% |
| 0.1–0.2% | 307 | 0 | 4% | 1% | -100% | -91% | -92% |
| 0.2–0.5% | 515 | 2 | 5% | 3% | -57% | -89% | -90% |
| Over 0.5% | 242 | 4 | 7% | 3% | +74% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 577 | 1 | 3% | 1% | -80% | -93% | -96% |
| Morning (6am–12pm) | 647 | 6 | 4% | 2% | +7% | -91% | -90% |
| Afternoon (12–6pm) | 360 | 1 | 2% | 1% | -68% | -95% | -96% |
| Evening (6pm–12am) | 589 | 2 | 4% | 2% | -60% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,764 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 45 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/29 1:43:24 PM | XRP | UP | 1.6 min | -0.227% | — | In play | — |
| 9/29 1:43:24 PM | SOL | UP | 1.6 min | -0.127% | — | In play | — |
| 9/29 1:42:51 PM | BNB | UP | 2.1 min | -0.159% | — | In play | — |
| 9/29 1:41:32 PM | ZEC | UP | 3.5 min | -0.551% | — | In play | — |
| 9/29 1:40:44 PM | HYPE | UP | 4.3 min | -0.462% | — | In play | — |
| 9/29 1:29:48 PM | XRP | DOWN | 11 sec | +0.013% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:29:48 PM | BNB | DOWN | 11 sec | -0.001% | 0¢ | ❌ Lost | $0.00 |
| 9/29 1:29:48 PM | DOGE | UP | 11 sec | +0.003% | 0¢ | ❌ Lost | $0.00 |
| 9/29 1:29:48 PM | GOLD | DOWN | 11 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/29 1:29:15 PM | ETH | UP | 45 sec | -0.083% | 0¢ | ❌ Lost | $0.00 |
| 9/29 1:29:15 PM | SOL | UP | 45 sec | -0.101% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:28:59 PM | ZEC | UP | 61 sec | -0.193% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 1:28:44 PM | HYPE | UP | 76 sec | -0.149% | 1¢ | ❌ Lost | $0.00 |
| 9/29 1:28:44 PM | BTC | UP | 76 sec | -0.065% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:27:56 PM | GBPUSD | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 1:26:51 PM | NEAR | UP | 3.1 min | -0.877% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:13:24 PM | PLATINUM | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 12:13:09 PM | HYPE | DOWN | 1.8 min | +0.329% | 0¢ | ❌ Lost | $0.00 |
| 9/29 12:12:51 PM | NATGAS | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 12:12:51 PM | WTI | UP | 2.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:12:35 PM | DOGE | DOWN | 2.4 min | +0.381% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:12:35 PM | EURUSD | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 12:12:04 PM | COPPER | DOWN | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:12:04 PM | GOLD | DOWN | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:11:46 PM | ETH | DOWN | 3.2 min | +0.333% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 12:11:46 PM | NEAR | DOWN | 3.2 min | +1.082% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:11:30 PM | XRP | DOWN | 3.5 min | +0.527% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:10:37 PM | BTC | DOWN | 4.4 min | +0.311% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:10:37 PM | PALLADIUM | DOWN | 4.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 12:10:37 PM | USDJPY | UP | 4.4 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
