# 15-Minute 1¢ Study

*Updated Mon Oct 5, 6:45 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 589 finished bets | 1% | $34.70 | +55% | +5.89¢ | -$18.25 / $52.95 |

*Expect about **81 buys a day** (~$12.18/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 2%, hold to the close | 1094 | $22.30 | +17% |
| Momentum model ≥ 5%, hold to the close | 588 | $21.45 | +34% |
| 5+ min left, hold to the close | 215 | $10.20 | +32% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 8476 | 8461 | 37 (0%) | 1.07% | -$498.70 (-49%) | Hold to the close: -$498.70 (-49%) |

*In play or awaiting result: 15. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 5593 | 4.1% | 0.4% (25) | -598% | ❌ Worse |
| Momentum model | 5593 | 4.2% | 0.4% (25) | -623% | ❌ Worse |
| Mean-reversion model | 5593 | 6.8% | 0.4% (25) | -699% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5593 | 25 | -44% | -85% | -85% | -82% |
| Volatility model ≥ 2% | 1094 | 11 | +17% | -69% | -69% | -64% |
| Volatility model ≥ 5% | 589 | 7 | +55% | -56% | -54% | -50% |
| Volatility model ≥ 10% | 366 | 5 | +102% | -36% | -37% | -31% |
| Momentum model ≥ 2% | 961 | 8 | +1% | -70% | -72% | -69% |
| Momentum model ≥ 5% | 588 | 6 | +34% | -61% | -63% | -60% |
| Momentum model ≥ 10% | 409 | 5 | +75% | -48% | -48% | -45% |
| Mean-reversion model ≥ 2% | 1940 | 14 | -21% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1302 | 12 | +2% | -79% | -79% | -72% |
| Mean-reversion model ≥ 10% | 863 | 9 | +20% | -78% | -78% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5790 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 2022 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 649 | 4% | 3% | 2% | 2% | 1% | 0% |
| **All** | 8461 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 37 | 0% | -$498.70 | -49% | — |
| Sell at 2¢ | 328 | 4% | -$903.42 | -89% | 33 sec |
| Sell at 3¢ | 213 | 3% | -$905.63 | -89% | 47 sec |
| Sell at 5¢ | 158 | 2% | -$886.00 | -87% | 61 sec |
| Sell at 10¢ | 106 | 1% | -$835.84 | -82% | 66 sec |
| Sell at 25¢ | 59 | 1% | -$751.41 | -74% | 1.5 min |
| Sell at 50¢ | 36 | 0% | -$661.70 | -65% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 212 | 3 | 11% | 3% | +34% | -80% | -88% |
| 2–5 min | 2746 | 20 | 7% | 4% | -29% | -87% | -87% |
| 1–2 min | 2227 | 9 | 3% | 2% | -56% | -93% | -93% |
| Under 1 min | 3273 | 5 | 1% | 0% | -77% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 654 | 5 | 5% | 3% | -9% | -89% | -89% |
| ETH | 647 | 5 | 6% | 3% | -3% | -87% | -86% |
| DOGE | 647 | 2 | 4% | 2% | -60% | -90% | -90% |
| HYPE | 646 | 3 | 5% | 3% | -43% | -88% | -86% |
| BNB | 642 | 2 | 4% | 2% | -63% | -91% | -93% |
| XRP | 640 | 4 | 2% | 1% | -20% | -76% | -77% |
| SOL | 640 | 0 | 3% | 1% | -100% | -92% | -91% |
| BTC | 638 | 3 | 5% | 2% | -38% | -87% | -90% |
| NEAR | 636 | 3 | 6% | 3% | -38% | -64% | -65% |
| GOLD | 341 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 328 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 311 | 2 | 3% | 1% | -31% | -95% | -96% |
| COPPER | 287 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 255 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 253 | 2 | 4% | 2% | -26% | -94% | -92% |
| PALLADIUM | 247 | 1 | 2% | 1% | -62% | -96% | -98% |
| EURUSD | 232 | 1 | 5% | 3% | -60% | -92% | -90% |
| GBPUSD | 222 | 1 | 4% | 2% | -58% | -94% | -94% |
| USDJPY | 195 | 3 | 2% | 2% | +44% | -96% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4267 | 20 | 4% | 2% | -45% | -89% | -88% |
| DOWN (bought NO) | 4194 | 17 | 4% | 2% | -53% | -89% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 958 | 7 | 2% | 1% | +24% | -58% | -58% |
| 0.05–0.1% | 975 | 2 | 3% | 1% | -69% | -91% | -92% |
| 0.1–0.2% | 1447 | 6 | 4% | 2% | -47% | -91% | -91% |
| 0.2–0.5% | 1706 | 8 | 6% | 3% | -48% | -88% | -87% |
| Over 0.5% | 702 | 4 | 7% | 3% | -42% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2228 | 9 | 4% | 2% | -53% | -86% | -87% |
| Morning (6am–12pm) | 2088 | 17 | 5% | 3% | -7% | -89% | -88% |
| Afternoon (12–6pm) | 1751 | 4 | 3% | 1% | -73% | -86% | -87% |
| Evening (6pm–12am) | 2394 | 7 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,134 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/5 6:44:59 AM | PLATINUM | DOWN | 1 sec | — | 0¢ | In play | — |
| 10/5 6:44:43 AM | SILVER | UP | 17 sec | — | 0¢ | In play | — |
| 10/5 6:44:02 AM | GBPUSD | UP | 58 sec | — | 0¢ | In play | — |
| 10/5 6:43:13 AM | NEAR | DOWN | 1.8 min | +0.242% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 6:43:09 AM | ZEC | UP | 1.9 min | -0.272% | 0¢ | In play | — |
| 10/5 6:43:05 AM | SOL | UP | 1.9 min | -0.200% | 1¢ | In play | — |
| 10/5 6:42:39 AM | DOGE | UP | 2.3 min | -0.225% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 6:42:23 AM | PALLADIUM | UP | 2.6 min | — | 0¢ | In play | — |
| 10/5 6:42:23 AM | ETH | UP | 2.6 min | -0.188% | 0¢ | ❌ Lost | $0.00 |
| 10/5 6:42:17 AM | BNB | UP | 2.7 min | -0.191% | 0¢ | In play | — |
| 10/5 6:41:33 AM | XRP | UP | 3.4 min | -0.258% | 1¢ | In play | — |
| 10/5 6:41:33 AM | BTC | UP | 3.4 min | -0.193% | 1¢ | In play | — |
| 10/5 6:39:57 AM | HYPE | UP | 5.0 min | -0.665% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 6:29:56 AM | SILVER | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 6:29:48 AM | HYPE | DOWN | 11 sec | +0.059% | 0¢ | ❌ Lost | $0.00 |
| 10/5 6:29:48 AM | SOL | DOWN | 11 sec | +0.043% | 0¢ | ❌ Lost | $0.00 |
| 10/5 6:29:44 AM | ZEC | UP | 15 sec | -0.226% | 0¢ | ❌ Lost | $0.00 |
| 10/5 6:29:22 AM | NEAR | UP | 37 sec | -0.214% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 6:29:08 AM | ETH | UP | 51 sec | -0.062% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 6:28:47 AM | BTC | UP | 73 sec | -0.071% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 6:28:43 AM | GOLD | DOWN | 77 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 6:28:29 AM | EURUSD | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 6:27:19 AM | DOGE | UP | 2.7 min | -0.244% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 6:27:17 AM | XRP | UP | 2.7 min | -0.145% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 6:26:29 AM | WTI | DOWN | 3.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 6:26:01 AM | BNB | UP | 4.0 min | -0.143% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 6:14:47 AM | GBPUSD | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 6:14:35 AM | NATGAS | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 6:14:31 AM | EURUSD | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 6:14:17 AM | BTC | UP | 42 sec | -0.081% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
