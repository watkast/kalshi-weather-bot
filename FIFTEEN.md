# 15-Minute 1¢ Study

*Updated Wed Oct 7, 8:00 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 736 finished bets | 1% | $33.10 | +42% | +4.50¢ | -$11.45 / $44.55 |

*Expect about **79 buys a day** (~$11.87/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 734 | $20.15 | +26% |
| 5+ min left, hold to the close | 280 | $14.45 | +35% |
| Mean-reversion model ≥ 5%, hold to the close | 1613 | $6.75 | +3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 10789 | 10770 | 49 (0%) | 1.07% | -$618.10 (-47%) | Hold to the close: -$618.10 (-47%) |

*In play or awaiting result: 19. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 6973 | 4.1% | 0.5% (33) | -562% | ❌ Worse |
| Momentum model | 6973 | 4.2% | 0.5% (33) | -591% | ❌ Worse |
| Mean-reversion model | 6973 | 6.8% | 0.5% (33) | -653% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6973 | 33 | -41% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 1345 | 12 | +4% | -73% | -73% | -69% |
| Volatility model ≥ 5% | 736 | 8 | +42% | -62% | -61% | -58% |
| Volatility model ≥ 10% | 458 | 6 | +94% | -46% | -47% | -42% |
| Momentum model ≥ 2% | 1199 | 10 | +1% | -74% | -76% | -74% |
| Momentum model ≥ 5% | 734 | 7 | +26% | -67% | -68% | -66% |
| Momentum model ≥ 10% | 506 | 6 | +72% | -56% | -57% | -54% |
| Mean-reversion model ≥ 2% | 2382 | 19 | -13% | -84% | -84% | -80% |
| Mean-reversion model ≥ 5% | 1613 | 15 | +3% | -81% | -81% | -75% |
| Mean-reversion model ≥ 10% | 1073 | 11 | +18% | -80% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7170 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2710 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 890 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 10770 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 49 | 0% | -$618.10 | -47% | — |
| Sell at 2¢ | 379 | 4% | -$1,163.56 | -89% | 34 sec |
| Sell at 3¢ | 253 | 2% | -$1,163.43 | -89% | 47 sec |
| Sell at 5¢ | 189 | 2% | -$1,139.25 | -87% | 61 sec |
| Sell at 10¢ | 127 | 1% | -$1,081.73 | -83% | 65 sec |
| Sell at 25¢ | 73 | 1% | -$978.47 | -75% | 82 sec |
| Sell at 50¢ | 48 | 0% | -$854.10 | -65% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 277 | 4 | 10% | 4% | +36% | -82% | -88% |
| 2–5 min | 3467 | 25 | 7% | 3% | -30% | -88% | -88% |
| 1–2 min | 2852 | 12 | 3% | 2% | -55% | -94% | -93% |
| Under 1 min | 4171 | 8 | 1% | 0% | -72% | -88% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 806 | 6 | 5% | 3% | -11% | -90% | -89% |
| HYPE | 803 | 3 | 5% | 3% | -54% | -89% | -87% |
| DOGE | 799 | 2 | 3% | 1% | -68% | -92% | -92% |
| ETH | 797 | 7 | 5% | 3% | +10% | -88% | -88% |
| BNB | 797 | 3 | 4% | 2% | -55% | -91% | -92% |
| NEAR | 794 | 5 | 6% | 3% | -17% | -69% | -71% |
| BTC | 792 | 4 | 5% | 2% | -33% | -88% | -90% |
| SOL | 792 | 0 | 3% | 1% | -100% | -94% | -93% |
| XRP | 790 | 5 | 2% | 1% | -21% | -80% | -80% |
| GOLD | 452 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 443 | 0 | 2% | 1% | -100% | -95% | -94% |
| WTI | 418 | 3 | 3% | 1% | -21% | -95% | -96% |
| COPPER | 387 | 0 | 1% | 1% | -100% | -99% | -99% |
| PLATINUM | 346 | 0 | 0% | 0% | -100% | -99% | -99% |
| NATGAS | 334 | 3 | 3% | 2% | -16% | -94% | -92% |
| PALLADIUM | 330 | 1 | 2% | 1% | -72% | -97% | -98% |
| EURUSD | 324 | 3 | 4% | 2% | -14% | -65% | -63% |
| GBPUSD | 304 | 1 | 3% | 2% | -69% | -95% | -95% |
| USDJPY | 262 | 3 | 2% | 1% | +7% | -97% | -96% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5477 | 26 | 4% | 2% | -45% | -88% | -87% |
| DOWN (bought NO) | 5293 | 23 | 3% | 2% | -50% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1181 | 8 | 2% | 1% | +17% | -65% | -65% |
| 0.05–0.1% | 1240 | 4 | 3% | 1% | -53% | -92% | -92% |
| 0.1–0.2% | 1819 | 6 | 3% | 2% | -59% | -92% | -92% |
| 0.2–0.5% | 2097 | 12 | 6% | 3% | -37% | -88% | -87% |
| Over 0.5% | 831 | 5 | 6% | 3% | -38% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2890 | 17 | 4% | 2% | -32% | -84% | -84% |
| Morning (6am–12pm) | 2646 | 17 | 4% | 2% | -27% | -91% | -89% |
| Afternoon (12–6pm) | 2244 | 7 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 2990 | 8 | 3% | 1% | -69% | -95% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,014 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/7 7:59:47 AM | COPPER | DOWN | 13 sec | — | 0¢ | In play | — |
| 10/7 7:59:14 AM | PLATINUM | DOWN | 45 sec | — | 0¢ | In play | — |
| 10/7 7:59:14 AM | GOLD | DOWN | 45 sec | — | 0¢ | In play | — |
| 10/7 7:59:14 AM | SILVER | DOWN | 45 sec | — | 1¢ | In play | — |
| 10/7 7:59:14 AM | EURUSD | DOWN | 45 sec | — | 0¢ | In play | — |
| 10/7 7:58:57 AM | NATGAS | UP | 62 sec | — | 0¢ | In play | — |
| 10/7 7:58:25 AM | GBPUSD | DOWN | 1.6 min | — | 0¢ | In play | — |
| 10/7 7:57:52 AM | USDJPY | UP | 2.1 min | — | 0¢ | In play | — |
| 10/7 7:57:04 AM | BTC | DOWN | 2.9 min | +0.297% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 7:56:13 AM | ETH | DOWN | 3.8 min | +0.718% | 1¢ | In play | — |
| 10/7 7:55:58 AM | BNB | DOWN | 4.0 min | +0.444% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 7:55:41 AM | DOGE | DOWN | 4.3 min | +0.628% | 1¢ | In play | — |
| 10/7 7:55:25 AM | XRP | DOWN | 4.6 min | +0.574% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 7:55:25 AM | NEAR | DOWN | 4.6 min | +1.210% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 7:55:25 AM | HYPE | DOWN | 4.6 min | +0.881% | 1¢ | In play | — |
| 10/7 7:54:53 AM | SOL | DOWN | 5.1 min | +0.581% | 1¢ | In play | — |
| 10/7 7:54:35 AM | WTI | UP | 5.4 min | — | 1¢ | In play | — |
| 10/7 7:54:03 AM | ZEC | DOWN | 6.0 min | +1.863% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 7:44:11 AM | NATGAS | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:43:52 AM | DOGE | UP | 67 sec | -0.166% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 7:43:52 AM | ETH | UP | 67 sec | -0.239% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:43:20 AM | USDJPY | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:43:20 AM | SOL | UP | 1.6 min | -0.274% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 7:43:20 AM | BNB | UP | 1.6 min | -0.215% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 7:43:05 AM | SILVER | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 7:43:05 AM | HYPE | UP | 1.9 min | -0.371% | 0¢ | ❌ Lost | $0.00 |
| 10/7 7:43:05 AM | WTI | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:43:05 AM | BTC | UP | 1.9 min | -0.297% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:42:14 AM | ZEC | UP | 2.8 min | -0.674% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:41:41 AM | COPPER | UP | 3.3 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
