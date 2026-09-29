# 15-Minute 1¢ Study

*Updated Tue Sep 29, 5:36 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 76 finished bets | 3% | $16.60 | +146% | +21.84¢ | $22.30 / -$5.70 |

*Expect about **41 buys a day** (~$6.09/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 76 | $2.10 | +18% |
| Mean-reversion model ≥ 5%, hold to the close | 322 | -$0.45 | -1% |
| Volatility model ≥ 5%, sell at 25¢ | 115 | -$2.07 | -17% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 2379 | 2373 | 10 (0%) | 1.07% | -$148.60 (-51%) | Hold to the close: -$148.60 (-51%) |

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
| Volatility model | 1300 | 2.8% | 0.3% (4) | -435% | ❌ Worse |
| Momentum model | 1300 | 2.9% | 0.3% (4) | -512% | ❌ Worse |
| Mean-reversion model | 1300 | 5.8% | 0.3% (4) | -532% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1300 | 4 | -61% | -90% | -91% | -88% |
| Volatility model ≥ 2% | 255 | 1 | -55% | -85% | -87% | -85% |
| Volatility model ≥ 5% | 115 | 0 | -100% | -74% | -74% | -68% |
| Volatility model ≥ 10% | 61 | 0 | -100% | -72% | -72% | -65% |
| Momentum model ≥ 2% | 214 | 0 | -100% | -86% | -89% | -90% |
| Momentum model ≥ 5% | 122 | 0 | -100% | -83% | -89% | -86% |
| Momentum model ≥ 10% | 78 | 0 | -100% | -86% | -84% | -83% |
| Mean-reversion model ≥ 2% | 491 | 3 | -35% | -86% | -87% | -84% |
| Mean-reversion model ≥ 5% | 322 | 3 | -1% | -83% | -84% | -79% |
| Mean-reversion model ≥ 10% | 199 | 2 | +12% | -78% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1496 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 726 | 2% | 1% | 1% | 0% | 0% | 0% |
| Financials | 151 | 5% | 3% | 3% | 2% | 2% | 1% |
| **All** | 2373 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 10 | 0% | -$148.60 | -51% | — |
| Sell at 2¢ | 86 | 4% | -$266.24 | -92% | 40 sec |
| Sell at 3¢ | 51 | 2% | -$268.71 | -93% | 47 sec |
| Sell at 5¢ | 36 | 2% | -$265.20 | -92% | 66 sec |
| Sell at 10¢ | 30 | 1% | -$235.30 | -82% | 1.6 min |
| Sell at 25¢ | 15 | 1% | -$224.95 | -78% | 2.1 min |
| Sell at 50¢ | 9 | 0% | -$199.85 | -69% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 76 | 2 | 12% | 3% | +146% | -79% | -86% |
| 2–5 min | 808 | 5 | 6% | 3% | -40% | -89% | -90% |
| 1–2 min | 637 | 2 | 3% | 1% | -66% | -94% | -94% |
| Under 1 min | 852 | 1 | 1% | 0% | -82% | -97% | -97% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 170 | 2 | 5% | 4% | +44% | -89% | -86% |
| DOGE | 169 | 1 | 4% | 2% | -22% | -90% | -89% |
| ZEC | 169 | 1 | 5% | 2% | -29% | -89% | -94% |
| NEAR | 166 | 0 | 5% | 1% | -100% | -87% | -91% |
| XRP | 166 | 2 | 2% | 2% | +53% | -94% | -94% |
| BTC | 165 | 0 | 7% | 2% | -100% | -83% | -89% |
| SOL | 165 | 0 | 4% | 2% | -100% | -91% | -88% |
| HYPE | 163 | 0 | 4% | 2% | -100% | -92% | -92% |
| BNB | 163 | 0 | 2% | 1% | -100% | -96% | -96% |
| GOLD | 130 | 0 | 3% | 0% | -100% | -93% | -97% |
| SILVER | 116 | 0 | 3% | 1% | -100% | -94% | -94% |
| WTI | 114 | 0 | 3% | 1% | -100% | -95% | -97% |
| COPPER | 107 | 0 | 1% | 1% | -100% | -98% | -98% |
| NATGAS | 98 | 0 | 3% | 1% | -100% | -95% | -92% |
| PLATINUM | 85 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 76 | 0 | 1% | 0% | -100% | -98% | -100% |
| GBPUSD | 58 | 1 | 5% | 2% | +61% | -91% | -91% |
| EURUSD | 50 | 1 | 6% | 2% | +87% | -90% | -95% |
| USDJPY | 43 | 2 | 5% | 5% | +334% | -92% | -88% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1243 | 7 | 4% | 2% | -35% | -92% | -92% |
| DOWN (bought NO) | 1130 | 3 | 4% | 1% | -69% | -92% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 150 | 0 | 2% | 1% | -100% | -93% | -93% |
| 0.05–0.1% | 184 | 0 | 1% | 0% | -100% | -96% | -97% |
| 0.1–0.2% | 346 | 0 | 4% | 1% | -100% | -90% | -92% |
| 0.2–0.5% | 557 | 2 | 5% | 3% | -61% | -90% | -91% |
| Over 0.5% | 258 | 4 | 6% | 3% | +62% | -88% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 577 | 1 | 3% | 1% | -80% | -93% | -96% |
| Morning (6am–12pm) | 647 | 6 | 4% | 2% | +7% | -91% | -90% |
| Afternoon (12–6pm) | 560 | 1 | 3% | 1% | -80% | -94% | -97% |
| Evening (6pm–12am) | 589 | 2 | 4% | 2% | -60% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,808 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 45 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/29 5:29:50 PM | SILVER | UP | 9 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/29 5:29:50 PM | GOLD | UP | 9 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/29 5:28:44 PM | COPPER | DOWN | 75 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:27:58 PM | XRP | UP | 2.0 min | -0.160% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:27:58 PM | SOL | UP | 2.0 min | -0.122% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:27:42 PM | BTC | UP | 2.3 min | -0.098% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:26:22 PM | ZEC | UP | 3.6 min | -0.436% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:26:06 PM | ETH | UP | 3.9 min | -0.213% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:25:50 PM | BNB | UP | 4.2 min | -0.243% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:25:18 PM | HYPE | UP | 4.7 min | -0.434% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:25:18 PM | NEAR | UP | 4.7 min | -0.823% | 2¢ | ❌ Lost | -$0.15 |
| 9/29 5:25:18 PM | DOGE | UP | 4.7 min | -0.304% | 2¢ | ❌ Lost | -$0.15 |
| 9/29 5:14:47 PM | GBPUSD | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 5:14:31 PM | PALLADIUM | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 5:13:43 PM | ZEC | DOWN | 77 sec | +0.101% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 5:13:27 PM | COPPER | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:12:55 PM | HYPE | DOWN | 2.1 min | +0.134% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:12:39 PM | ETH | DOWN | 2.3 min | +0.164% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:12:39 PM | GOLD | DOWN | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:12:39 PM | XRP | DOWN | 2.3 min | +0.268% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:12:07 PM | NEAR | DOWN | 2.9 min | +0.553% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:12:07 PM | SILVER | DOWN | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:11:35 PM | DOGE | DOWN | 3.4 min | +0.334% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:11:35 PM | SOL | DOWN | 3.4 min | +0.360% | 0¢ | ❌ Lost | $0.00 |
| 9/29 5:11:19 PM | BNB | DOWN | 3.7 min | +0.248% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:10:47 PM | BTC | DOWN | 4.2 min | +0.241% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:59:48 PM | ETH | DOWN | 11 sec | +0.010% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:59:32 PM | GOLD | DOWN | 27 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 4:59:32 PM | XRP | UP | 27 sec | -0.054% | 0¢ | ❌ Lost | $0.00 |
| 9/29 4:59:32 PM | WTI | UP | 27 sec | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
