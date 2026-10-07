# 15-Minute 1¢ Study

*Updated Wed Oct 7, 4:17 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 724 finished bets | 1% | $34.30 | +44% | +4.74¢ | -$11.15 / $45.45 |

*Expect about **79 buys a day** (~$11.87/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 722 | $21.50 | +28% |
| 5+ min left, hold to the close | 267 | $16.40 | +41% |
| Mean-reversion model ≥ 5%, hold to the close | 1584 | $10.80 | +5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 10572 | 10566 | 48 (0%) | 1.07% | -$606.30 (-47%) | Hold to the close: -$606.30 (-47%) |

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
| Volatility model | 6846 | 4.1% | 0.5% (33) | -564% | ❌ Worse |
| Momentum model | 6846 | 4.2% | 0.5% (33) | -593% | ❌ Worse |
| Mean-reversion model | 6846 | 6.8% | 0.5% (33) | -652% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6846 | 33 | -39% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 1324 | 12 | +6% | -73% | -73% | -69% |
| Volatility model ≥ 5% | 724 | 8 | +44% | -62% | -61% | -58% |
| Volatility model ≥ 10% | 453 | 6 | +96% | -45% | -46% | -41% |
| Momentum model ≥ 2% | 1181 | 10 | +3% | -74% | -75% | -73% |
| Momentum model ≥ 5% | 722 | 7 | +28% | -66% | -68% | -66% |
| Momentum model ≥ 10% | 501 | 6 | +73% | -56% | -57% | -54% |
| Mean-reversion model ≥ 2% | 2336 | 19 | -11% | -84% | -84% | -80% |
| Mean-reversion model ≥ 5% | 1584 | 15 | +5% | -81% | -81% | -75% |
| Mean-reversion model ≥ 10% | 1048 | 11 | +22% | -79% | -79% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7043 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2658 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 865 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 10566 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 48 | 0% | -$606.30 | -47% | — |
| Sell at 2¢ | 373 | 4% | -$1,139.32 | -89% | 33 sec |
| Sell at 3¢ | 249 | 2% | -$1,139.19 | -89% | 47 sec |
| Sell at 5¢ | 186 | 2% | -$1,115.40 | -87% | 60 sec |
| Sell at 10¢ | 125 | 1% | -$1,058.55 | -83% | 65 sec |
| Sell at 25¢ | 71 | 1% | -$959.29 | -75% | 82 sec |
| Sell at 50¢ | 47 | 0% | -$835.05 | -65% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 264 | 4 | 10% | 3% | +43% | -83% | -88% |
| 2–5 min | 3395 | 25 | 7% | 3% | -28% | -88% | -88% |
| 1–2 min | 2790 | 11 | 3% | 2% | -57% | -94% | -93% |
| Under 1 min | 4114 | 8 | 1% | 0% | -71% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 793 | 6 | 5% | 3% | -10% | -90% | -89% |
| HYPE | 789 | 3 | 5% | 3% | -53% | -88% | -87% |
| DOGE | 785 | 2 | 3% | 1% | -67% | -92% | -92% |
| ETH | 783 | 7 | 5% | 3% | +12% | -88% | -88% |
| BNB | 782 | 3 | 4% | 2% | -54% | -91% | -92% |
| NEAR | 780 | 5 | 6% | 3% | -16% | -69% | -70% |
| SOL | 778 | 0 | 3% | 1% | -100% | -94% | -93% |
| BTC | 777 | 4 | 5% | 2% | -32% | -88% | -90% |
| XRP | 776 | 5 | 2% | 1% | -19% | -80% | -80% |
| GOLD | 444 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 433 | 0 | 3% | 1% | -100% | -95% | -94% |
| WTI | 411 | 3 | 3% | 1% | -20% | -95% | -96% |
| COPPER | 382 | 0 | 1% | 1% | -100% | -99% | -99% |
| PLATINUM | 340 | 0 | 0% | 0% | -100% | -99% | -99% |
| PALLADIUM | 325 | 1 | 2% | 1% | -71% | -97% | -98% |
| NATGAS | 323 | 3 | 3% | 2% | -13% | -95% | -93% |
| EURUSD | 315 | 2 | 3% | 2% | -41% | -64% | -63% |
| GBPUSD | 295 | 1 | 3% | 2% | -68% | -95% | -95% |
| USDJPY | 255 | 3 | 2% | 1% | +10% | -97% | -96% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5366 | 26 | 4% | 2% | -44% | -88% | -87% |
| DOWN (bought NO) | 5200 | 22 | 3% | 2% | -51% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1167 | 8 | 2% | 1% | +18% | -65% | -64% |
| 0.05–0.1% | 1219 | 4 | 3% | 1% | -52% | -92% | -92% |
| 0.1–0.2% | 1793 | 6 | 4% | 2% | -58% | -92% | -92% |
| 0.2–0.5% | 2049 | 12 | 6% | 3% | -36% | -88% | -87% |
| Over 0.5% | 813 | 5 | 6% | 3% | -37% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2796 | 16 | 4% | 2% | -34% | -83% | -84% |
| Morning (6am–12pm) | 2536 | 17 | 5% | 3% | -24% | -90% | -89% |
| Afternoon (12–6pm) | 2244 | 7 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 2990 | 8 | 3% | 1% | -69% | -95% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,040 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/7 4:14:45 AM | PALLADIUM | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 4:14:45 AM | COPPER | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 4:14:45 AM | BTC | DOWN | 14 sec | +0.021% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 4:14:45 AM | WTI | DOWN | 14 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/7 4:14:29 AM | USDJPY | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 4:14:13 AM | XRP | UP | 46 sec | -0.138% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 4:13:56 AM | PLATINUM | UP | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 4:13:40 AM | GOLD | UP | 79 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 4:13:40 AM | BNB | UP | 79 sec | -0.131% | 0¢ | ❌ Lost | $0.00 |
| 10/7 4:13:40 AM | SOL | UP | 79 sec | -0.168% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 4:13:24 AM | ETH | UP | 1.6 min | -0.446% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 4:13:24 AM | DOGE | UP | 1.6 min | -0.382% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 4:13:24 AM | SILVER | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 4:13:08 AM | GBPUSD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 4:13:08 AM | NEAR | DOWN | 1.9 min | +0.488% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 4:13:08 AM | EURUSD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 4:12:49 AM | HYPE | DOWN | 2.2 min | +0.380% | 0¢ | ❌ Lost | $0.00 |
| 10/7 3:59:46 AM | DOGE | DOWN | 14 sec | +0.026% | 0¢ | ❌ Lost | $0.00 |
| 10/7 3:59:46 AM | BTC | DOWN | 14 sec | +0.024% | 0¢ | ❌ Lost | $0.00 |
| 10/7 3:59:46 AM | HYPE | DOWN | 14 sec | +0.028% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 3:59:30 AM | COPPER | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 3:58:59 AM | ZEC | DOWN | 60 sec | +0.181% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 3:58:59 AM | PALLADIUM | DOWN | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 3:58:43 AM | XRP | DOWN | 76 sec | +0.138% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 3:58:43 AM | SOL | UP | 76 sec | -0.126% | 0¢ | ❌ Lost | $0.00 |
| 10/7 3:58:27 AM | ETH | UP | 1.5 min | -0.128% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 3:58:27 AM | EURUSD | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 3:57:55 AM | NATGAS | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 3:57:39 AM | BNB | UP | 2.4 min | -0.154% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 3:57:05 AM | USDJPY | DOWN | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
