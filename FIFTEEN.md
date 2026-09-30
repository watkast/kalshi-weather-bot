# 15-Minute 1¢ Study

*Updated Tue Sep 29, 9:04 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 79 finished bets | 3% | $16.15 | +136% | +20.44¢ | $22.15 / -$6.00 |

*Expect about **39 buys a day** (~$5.87/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 79 | $1.65 | +14% |
| Mean-reversion model ≥ 5%, hold to the close | 343 | -$3.00 | -7% |
| Volatility model ≥ 5%, sell at 25¢ | 125 | -$3.12 | -24% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 2589 | 2583 | 10 (0%) | 1.07% | -$173.80 (-55%) | Hold to the close: -$173.80 (-55%) |

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
| Volatility model | 1421 | 2.9% | 0.3% (4) | -497% | ❌ Worse |
| Momentum model | 1421 | 3.0% | 0.3% (4) | -559% | ❌ Worse |
| Mean-reversion model | 1421 | 5.7% | 0.3% (4) | -604% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1421 | 4 | -64% | -91% | -92% | -89% |
| Volatility model ≥ 2% | 274 | 1 | -58% | -86% | -88% | -86% |
| Volatility model ≥ 5% | 125 | 0 | -100% | -76% | -76% | -70% |
| Volatility model ≥ 10% | 69 | 0 | -100% | -75% | -75% | -69% |
| Momentum model ≥ 2% | 239 | 0 | -100% | -87% | -90% | -91% |
| Momentum model ≥ 5% | 137 | 0 | -100% | -85% | -90% | -87% |
| Momentum model ≥ 10% | 88 | 0 | -100% | -88% | -86% | -85% |
| Mean-reversion model ≥ 2% | 522 | 3 | -38% | -86% | -87% | -84% |
| Mean-reversion model ≥ 5% | 343 | 3 | -7% | -84% | -84% | -78% |
| Mean-reversion model ≥ 10% | 212 | 2 | +5% | -79% | -82% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1617 | 4% | 2% | 2% | 2% | 1% | 0% |
| Commodities | 788 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 178 | 4% | 3% | 2% | 2% | 2% | 1% |
| **All** | 2583 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 10 | 0% | -$173.80 | -55% | — |
| Sell at 2¢ | 91 | 4% | -$290.14 | -92% | 34 sec |
| Sell at 3¢ | 56 | 2% | -$291.96 | -93% | 47 sec |
| Sell at 5¢ | 39 | 2% | -$288.45 | -92% | 64 sec |
| Sell at 10¢ | 32 | 1% | -$257.88 | -82% | 1.6 min |
| Sell at 25¢ | 17 | 1% | -$243.53 | -78% | 1.6 min |
| Sell at 50¢ | 9 | 0% | -$225.05 | -72% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 79 | 2 | 11% | 3% | +136% | -80% | -87% |
| 2–5 min | 852 | 5 | 6% | 3% | -43% | -89% | -90% |
| 1–2 min | 694 | 2 | 3% | 1% | -69% | -94% | -94% |
| Under 1 min | 958 | 1 | 1% | 0% | -84% | -97% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 183 | 1 | 4% | 2% | -28% | -91% | -90% |
| ZEC | 182 | 1 | 5% | 2% | -35% | -89% | -93% |
| ETH | 181 | 2 | 4% | 3% | +36% | -90% | -87% |
| NEAR | 180 | 0 | 6% | 1% | -100% | -87% | -90% |
| BTC | 179 | 0 | 7% | 2% | -100% | -84% | -90% |
| XRP | 179 | 2 | 2% | 2% | +44% | -95% | -94% |
| SOL | 179 | 0 | 3% | 2% | -100% | -91% | -89% |
| HYPE | 177 | 0 | 3% | 2% | -100% | -92% | -92% |
| BNB | 177 | 0 | 2% | 1% | -100% | -96% | -96% |
| GOLD | 141 | 0 | 5% | 1% | -100% | -89% | -90% |
| WTI | 125 | 0 | 2% | 1% | -100% | -95% | -98% |
| SILVER | 124 | 0 | 2% | 1% | -100% | -95% | -95% |
| COPPER | 116 | 0 | 1% | 1% | -100% | -99% | -98% |
| NATGAS | 107 | 0 | 3% | 1% | -100% | -95% | -93% |
| PLATINUM | 90 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 85 | 0 | 1% | 0% | -100% | -98% | -100% |
| GBPUSD | 66 | 1 | 5% | 2% | +41% | -92% | -92% |
| EURUSD | 59 | 1 | 5% | 2% | +58% | -91% | -96% |
| USDJPY | 53 | 2 | 4% | 4% | +252% | -93% | -90% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1352 | 7 | 4% | 2% | -41% | -92% | -92% |
| DOWN (bought NO) | 1231 | 3 | 3% | 1% | -72% | -92% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 171 | 0 | 2% | 1% | -100% | -93% | -93% |
| 0.05–0.1% | 210 | 0 | 1% | 0% | -100% | -97% | -98% |
| 0.1–0.2% | 378 | 0 | 3% | 1% | -100% | -91% | -93% |
| 0.2–0.5% | 590 | 2 | 5% | 3% | -63% | -90% | -91% |
| Over 0.5% | 267 | 4 | 6% | 3% | +56% | -88% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 577 | 1 | 3% | 1% | -80% | -93% | -96% |
| Morning (6am–12pm) | 647 | 6 | 4% | 2% | +7% | -91% | -90% |
| Afternoon (12–6pm) | 583 | 1 | 3% | 1% | -81% | -94% | -97% |
| Evening (6pm–12am) | 776 | 2 | 4% | 2% | -70% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,650 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/29 8:59:43 PM | SOL | DOWN | 17 sec | +0.084% | 0¢ | ❌ Lost | $0.00 |
| 9/29 8:59:43 PM | BTC | UP | 17 sec | -0.013% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 8:59:27 PM | NATGAS | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 8:59:27 PM | COPPER | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 8:59:11 PM | BNB | DOWN | 49 sec | +0.018% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 8:59:11 PM | DOGE | UP | 49 sec | -0.135% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 8:59:11 PM | HYPE | UP | 49 sec | -0.101% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 8:58:56 PM | GOLD | DOWN | 63 sec | — | 46¢ | ❌ Lost | -$0.15 |
| 9/29 8:58:56 PM | ETH | DOWN | 63 sec | +0.062% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 8:58:56 PM | NEAR | DOWN | 63 sec | +0.162% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 8:58:08 PM | USDJPY | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 8:58:08 PM | ZEC | UP | 1.9 min | -0.257% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 8:58:08 PM | WTI | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 8:44:44 PM | SILVER | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 8:44:44 PM | EURUSD | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 8:44:44 PM | USDJPY | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 8:44:44 PM | GOLD | DOWN | 15 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/29 8:44:44 PM | NATGAS | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 8:44:28 PM | HYPE | DOWN | 31 sec | +0.030% | 0¢ | ❌ Lost | $0.00 |
| 9/29 8:44:28 PM | WTI | DOWN | 31 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/29 8:44:12 PM | SOL | DOWN | 47 sec | +0.093% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 8:44:12 PM | COPPER | DOWN | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 8:44:12 PM | NEAR | DOWN | 47 sec | +0.237% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 8:44:12 PM | ETH | DOWN | 47 sec | +0.073% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 8:43:56 PM | BTC | UP | 63 sec | -0.073% | 0¢ | ❌ Lost | $0.00 |
| 9/29 8:43:56 PM | DOGE | DOWN | 63 sec | +0.191% | 0¢ | ❌ Lost | $0.00 |
| 9/29 8:43:56 PM | XRP | DOWN | 63 sec | +0.174% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 8:42:22 PM | ZEC | DOWN | 2.6 min | +0.287% | 2¢ | ❌ Lost | -$0.15 |
| 9/29 8:42:06 PM | BNB | DOWN | 2.9 min | +0.112% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 8:29:58 PM | COPPER | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
