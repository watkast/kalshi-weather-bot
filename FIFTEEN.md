# 15-Minute 1¢ Study

*Updated Mon Sep 28, 7:52 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 66 finished bets | 2% | $5.45 | +64% | +8.26¢ | $9.80 / -$4.35 |

*Expect **66 buys in the first 7 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 2%, hold to the close | 110 | -$0.55 | -4% |
| Mean-reversion model ≥ 5%, sell at 50¢ | 66 | -$1.80 | -21% |
| Momentum model ≥ 2%, sell at 5¢ | 41 | -$4.15 | -86% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 689 | 683 | 3 (0%) | 1.07% | -$40.65 (-49%) | Hold to the close: -$40.65 (-49%) |

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
| Volatility model | 255 | 3.7% | 0.4% (1) | -638% | ❌ Worse |
| Momentum model | 255 | 4.1% | 0.4% (1) | -755% | ❌ Worse |
| Mean-reversion model | 255 | 6.7% | 0.4% (1) | -680% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 255 | 1 | -51% | -90% | -92% | -89% |
| Volatility model ≥ 2% | 42 | 0 | -100% | -90% | -92% | -87% |
| Volatility model ≥ 5% | 24 | 0 | -100% | -81% | -86% | -76% |
| Volatility model ≥ 10% | 13 | 0 | -100% | -81% | -71% | -52% |
| Momentum model ≥ 2% | 41 | 0 | -100% | -89% | -92% | -86% |
| Momentum model ≥ 5% | 27 | 0 | -100% | -83% | -87% | -78% |
| Momentum model ≥ 10% | 20 | 0 | -100% | -88% | -81% | -69% |
| Mean-reversion model ≥ 2% | 110 | 1 | -4% | -86% | -89% | -87% |
| Mean-reversion model ≥ 5% | 66 | 1 | +64% | -85% | -86% | -77% |
| Mean-reversion model ≥ 10% | 44 | 1 | +146% | -82% | -86% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 450 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 208 | 2% | 1% | 0% | 0% | 0% | 0% |
| Financials | 25 | 0% | 0% | 0% | 0% | 0% | 0% |
| **All** | 683 | 3% | 2% | 1% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 3 | 0% | -$40.65 | -49% | — |
| Sell at 2¢ | 23 | 3% | -$76.67 | -93% | 63 sec |
| Sell at 3¢ | 14 | 2% | -$77.19 | -93% | 74 sec |
| Sell at 5¢ | 8 | 1% | -$77.45 | -94% | 2.3 min |
| Sell at 10¢ | 7 | 1% | -$73.48 | -89% | 2.9 min |
| Sell at 25¢ | 4 | 1% | -$69.41 | -84% | 3.5 min |
| Sell at 50¢ | 3 | 0% | -$62.40 | -75% | 4.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 22 | 2 | 14% | 9% | +748% | -76% | -65% |
| 2–5 min | 238 | 1 | 6% | 2% | -59% | -88% | -91% |
| 1–2 min | 205 | 0 | 2% | 0% | -100% | -96% | -97% |
| Under 1 min | 218 | 0 | 0% | 0% | -100% | -99% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| XRP | 52 | 2 | 6% | 4% | +334% | -88% | -88% |
| ZEC | 52 | 0 | 6% | 0% | -100% | -87% | -100% |
| ETH | 51 | 1 | 2% | 2% | +152% | -95% | -93% |
| DOGE | 51 | 0 | 6% | 2% | -100% | -88% | -82% |
| NEAR | 50 | 0 | 0% | 0% | -100% | -100% | -100% |
| BTC | 50 | 0 | 10% | 4% | -100% | -75% | -78% |
| SOL | 50 | 0 | 4% | 2% | -100% | -90% | -85% |
| BNB | 49 | 0 | 2% | 0% | -100% | -95% | -93% |
| HYPE | 45 | 0 | 2% | 0% | -100% | -95% | -100% |
| GOLD | 38 | 0 | 3% | 0% | -100% | -94% | -100% |
| WTI | 34 | 0 | 3% | 0% | -100% | -94% | -100% |
| SILVER | 33 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 30 | 0 | 7% | 3% | -100% | -88% | -83% |
| PLATINUM | 26 | 0 | 0% | 0% | -100% | -100% | -100% |
| COPPER | 25 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 22 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 11 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 9 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 5 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 355 | 3 | 4% | 2% | +1% | -92% | -91% |
| DOWN (bought NO) | 328 | 0 | 3% | 1% | -100% | -94% | -96% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 42 | 0 | 2% | 2% | -100% | -90% | -86% |
| 0.05–0.1% | 47 | 0 | 2% | 0% | -100% | -94% | -100% |
| 0.1–0.2% | 106 | 0 | 3% | 0% | -100% | -93% | -93% |
| 0.2–0.5% | 192 | 1 | 5% | 2% | -44% | -91% | -92% |
| Over 0.5% | 63 | 2 | 8% | 3% | +239% | -84% | -81% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 99 | 0 | 2% | 0% | -100% | -96% | -100% |
| Evening (6pm–12am) | 276 | 2 | 3% | 1% | -16% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,974 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 47 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 7:44:39 AM | NEAR | DOWN | 20 sec | +0.011% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:44:23 AM | SOL | DOWN | 36 sec | +0.064% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:44:23 AM | ZEC | UP | 36 sec | -0.253% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:43:49 AM | PLATINUM | DOWN | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:43:49 AM | HYPE | DOWN | 71 sec | +0.166% | 0¢ | ❌ Lost | $0.00 |
| 9/28 7:43:33 AM | GOLD | DOWN | 87 sec | — | 3¢ | ❌ Lost | -$0.15 |
| 9/28 7:43:33 AM | DOGE | DOWN | 87 sec | +0.426% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 7:43:17 AM | XRP | DOWN | 1.7 min | +0.295% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 7:43:02 AM | ETH | DOWN | 1.9 min | +0.309% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 7:43:02 AM | BNB | DOWN | 1.9 min | +0.235% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:42:28 AM | SILVER | DOWN | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 7:42:12 AM | BTC | DOWN | 2.8 min | +0.251% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 7:29:54 AM | DOGE | DOWN | 6 sec | +0.039% | 0¢ | ❌ Lost | $0.00 |
| 9/28 7:29:54 AM | BNB | UP | 6 sec | -0.027% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:29:38 AM | HYPE | UP | 22 sec | -0.097% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:29:38 AM | ZEC | UP | 22 sec | -0.106% | 0¢ | ❌ Lost | $0.00 |
| 9/28 7:29:22 AM | GOLD | UP | 38 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 7:29:07 AM | NEAR | DOWN | 52 sec | +0.735% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 7:28:35 AM | NATGAS | DOWN | 84 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:28:19 AM | SOL | DOWN | 1.7 min | +0.202% | 1¢ | ❌ Lost | $0.00 |
| 9/28 7:28:19 AM | PALLADIUM | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:28:19 AM | ETH | DOWN | 1.7 min | +0.142% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 7:28:03 AM | EURUSD | DOWN | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 7:27:47 AM | BTC | DOWN | 2.2 min | +0.124% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 7:27:31 AM | XRP | DOWN | 2.5 min | +0.408% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 7:14:55 AM | SILVER | UP | 4 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/28 7:14:39 AM | ZEC | DOWN | 20 sec | +0.167% | 0¢ | ❌ Lost | $0.00 |
| 9/28 7:14:07 AM | PLATINUM | UP | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:13:02 AM | PALLADIUM | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:12:30 AM | GOLD | UP | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
