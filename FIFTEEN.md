# 15-Minute 1¢ Study

*Updated Sat Oct 17, 12:51 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1721 finished bets | 1% | $75.05 | +39% | +4.36¢ | $32.70 / $42.35 |

*Expect about **91 buys a day** (~$13.58/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1585 | $38.25 | +22% |
| Momentum model ≥ 2%, hold to the close | 2679 | -$16.65 | -5% |
| Volatility model ≥ 5%, sell at 50¢ | 1721 | -$27.45 | -14% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 21622 | 21615 | 80 (0%) | 1.07% | -$1,508.75 (-57%) | Hold to the close: -$1,508.75 (-57%) |

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
| Volatility model | 13891 | 4.5% | 0.4% (54) | -667% | ❌ Worse |
| Momentum model | 13891 | 4.4% | 0.4% (54) | -690% | ❌ Worse |
| Mean-reversion model | 13891 | 7.5% | 0.4% (54) | -802% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13891 | 54 | -51% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 3132 | 24 | -11% | -79% | -78% | -75% |
| Volatility model ≥ 5% | 1721 | 19 | +39% | -74% | -73% | -69% |
| Volatility model ≥ 10% | 1005 | 11 | +56% | -66% | -66% | -63% |
| Momentum model ≥ 2% | 2679 | 21 | -5% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 1585 | 15 | +22% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1056 | 10 | +33% | -73% | -73% | -68% |
| Mean-reversion model ≥ 2% | 5285 | 34 | -30% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3649 | 27 | -18% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2403 | 16 | -24% | -80% | -80% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 14089 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5309 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 21615 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 80 | 0% | -$1,508.75 | -57% | — |
| Sell at 2¢ | 773 | 4% | -$2,329.77 | -89% | 37 sec |
| Sell at 3¢ | 517 | 2% | -$2,329.12 | -89% | 47 sec |
| Sell at 5¢ | 371 | 2% | -$2,289.60 | -87% | 50 sec |
| Sell at 10¢ | 223 | 1% | -$2,210.62 | -84% | 63 sec |
| Sell at 25¢ | 126 | 1% | -$2,043.69 | -78% | 80 sec |
| Sell at 50¢ | 83 | 0% | -$1,830.50 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 739 | 5 | 10% | 3% | -36% | -82% | -85% |
| 2–5 min | 6987 | 37 | 7% | 3% | -48% | -88% | -88% |
| 1–2 min | 5620 | 20 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 8265 | 18 | 1% | 0% | -69% | -88% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1583 | 11 | 5% | 3% | -13% | -89% | -90% |
| HYPE | 1577 | 5 | 4% | 2% | -61% | -90% | -88% |
| ETH | 1570 | 8 | 6% | 3% | -38% | -87% | -87% |
| BNB | 1568 | 6 | 5% | 2% | -53% | -89% | -89% |
| DOGE | 1567 | 2 | 4% | 2% | -84% | -90% | -90% |
| SOL | 1565 | 2 | 3% | 2% | -84% | -92% | -92% |
| XRP | 1556 | 7 | 3% | 1% | -44% | -86% | -87% |
| NEAR | 1553 | 8 | 6% | 3% | -33% | -78% | -78% |
| BTC | 1550 | 7 | 5% | 2% | -40% | -88% | -91% |
| GOLD | 864 | 1 | 3% | 1% | -86% | -92% | -94% |
| SILVER | 841 | 4 | 3% | 1% | -45% | -80% | -80% |
| WTI | 821 | 3 | 3% | 1% | -57% | -94% | -95% |
| COPPER | 735 | 2 | 2% | 1% | -75% | -84% | -84% |
| PLATINUM | 722 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 667 | 5 | 2% | 2% | -30% | -82% | -81% |
| PALLADIUM | 659 | 2 | 1% | 0% | -72% | -84% | -84% |
| EURUSD | 659 | 3 | 3% | 1% | -58% | -81% | -81% |
| GBPUSD | 615 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 574 | 3 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 200 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 169 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10901 | 40 | 4% | 2% | -58% | -89% | -89% |
| DOWN (bought NO) | 10714 | 40 | 4% | 2% | -57% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2355 | 11 | 2% | 1% | -21% | -80% | -80% |
| 0.05–0.1% | 2427 | 7 | 3% | 1% | -58% | -92% | -91% |
| 0.1–0.2% | 3551 | 11 | 4% | 2% | -62% | -90% | -90% |
| 0.2–0.5% | 4121 | 21 | 6% | 3% | -44% | -88% | -88% |
| Over 0.5% | 1632 | 6 | 6% | 3% | -62% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5384 | 20 | 4% | 2% | -58% | -87% | -88% |
| Morning (6am–12pm) | 5104 | 27 | 4% | 2% | -39% | -87% | -86% |
| Afternoon (12–6pm) | 5104 | 16 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 6023 | 17 | 3% | 2% | -68% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,493 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/17 12:44:43 AM | DOGE | DOWN | 16 sec | -0.021% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:44:43 AM | ZEC | DOWN | 16 sec | +0.059% | 0¢ | ❌ Lost | $0.00 |
| 10/17 12:44:27 AM | NEAR | DOWN | 32 sec | -0.012% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 12:44:27 AM | SOL | UP | 32 sec | -0.030% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 12:43:40 AM | ETH | DOWN | 79 sec | +0.053% | 2¢ | ❌ Lost | -$0.15 |
| 10/17 12:43:40 AM | BNB | DOWN | 79 sec | +0.013% | 0¢ | ❌ Lost | $0.00 |
| 10/17 12:43:08 AM | HYPE | DOWN | 1.9 min | +0.131% | 0¢ | ❌ Lost | $0.00 |
| 10/17 12:42:21 AM | XRP | UP | 2.6 min | -0.115% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:29:38 AM | DOGE | UP | 22 sec | -0.031% | 0¢ | ❌ Lost | $0.00 |
| 10/17 12:29:22 AM | BTC | DOWN | 38 sec | +0.026% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 12:29:22 AM | SOL | UP | 38 sec | -0.056% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 12:29:06 AM | ZEC | UP | 54 sec | -0.162% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:28:35 AM | ETH | DOWN | 85 sec | +0.059% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 12:28:35 AM | NEAR | UP | 85 sec | -0.283% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:28:35 AM | XRP | UP | 85 sec | -0.115% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:26:26 AM | BNB | UP | 3.5 min | -0.090% | 3¢ | ❌ Lost | -$0.15 |
| 10/17 12:14:41 AM | BTC | DOWN | 18 sec | +0.043% | 0¢ | ❌ Lost | $0.00 |
| 10/17 12:14:41 AM | SOL | DOWN | 18 sec | +0.046% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 12:14:09 AM | ZEC | DOWN | 50 sec | +0.131% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 12:13:53 AM | DOGE | DOWN | 67 sec | +0.056% | 0¢ | ❌ Lost | $0.00 |
| 10/17 12:13:53 AM | HYPE | DOWN | 67 sec | +0.067% | 0¢ | ❌ Lost | $0.00 |
| 10/17 12:13:38 AM | ETH | DOWN | 81 sec | +0.062% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:13:22 AM | NEAR | UP | 1.6 min | -0.334% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 12:12:50 AM | XRP | DOWN | 2.2 min | +0.069% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:12:19 AM | BNB | UP | 2.7 min | -0.105% | 0¢ | ❌ Lost | $0.00 |
| 10/16 11:59:53 PM | BTC | UP | 7 sec | -0.021% | 0¢ | ❌ Lost | $0.00 |
| 10/16 11:59:37 PM | ZEC | UP | 22 sec | +0.029% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 11:59:37 PM | XRP | DOWN | 22 sec | -0.008% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 11:59:37 PM | NEAR | DOWN | 22 sec | -0.020% | 0¢ | ❌ Lost | $0.00 |
| 10/16 11:59:05 PM | BNB | DOWN | 54 sec | +0.001% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
