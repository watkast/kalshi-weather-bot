# 15-Minute 1¢ Study

*Updated Wed Oct 7, 3:57 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 724 finished bets | 1% | $34.30 | +44% | +4.74¢ | -$11.15 / $45.45 |

*Expect about **79 buys a day** (~$11.89/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 722 | $21.50 | +28% |
| 5+ min left, hold to the close | 267 | $16.40 | +41% |
| Mean-reversion model ≥ 5%, hold to the close | 1583 | $10.95 | +6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 10543 | 10534 | 48 (0%) | 1.07% | -$602.40 (-47%) | Hold to the close: -$602.40 (-47%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 6829 | 4.2% | 0.5% (33) | -565% | ❌ Worse |
| Momentum model | 6829 | 4.2% | 0.5% (33) | -594% | ❌ Worse |
| Mean-reversion model | 6829 | 6.8% | 0.5% (33) | -653% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6829 | 33 | -39% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 1324 | 12 | +6% | -73% | -73% | -69% |
| Volatility model ≥ 5% | 724 | 8 | +44% | -62% | -61% | -58% |
| Volatility model ≥ 10% | 453 | 6 | +96% | -45% | -46% | -41% |
| Momentum model ≥ 2% | 1181 | 10 | +3% | -74% | -75% | -73% |
| Momentum model ≥ 5% | 722 | 7 | +28% | -66% | -68% | -66% |
| Momentum model ≥ 10% | 501 | 6 | +73% | -56% | -57% | -54% |
| Mean-reversion model ≥ 2% | 2334 | 19 | -11% | -84% | -84% | -80% |
| Mean-reversion model ≥ 5% | 1583 | 15 | +6% | -81% | -81% | -75% |
| Mean-reversion model ≥ 10% | 1048 | 11 | +22% | -79% | -79% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7026 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2648 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 860 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 10534 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 48 | 0% | -$602.40 | -47% | — |
| Sell at 2¢ | 373 | 4% | -$1,135.42 | -89% | 33 sec |
| Sell at 3¢ | 249 | 2% | -$1,135.29 | -89% | 47 sec |
| Sell at 5¢ | 186 | 2% | -$1,111.50 | -87% | 60 sec |
| Sell at 10¢ | 125 | 1% | -$1,054.65 | -83% | 65 sec |
| Sell at 25¢ | 71 | 1% | -$955.39 | -75% | 82 sec |
| Sell at 50¢ | 47 | 0% | -$831.15 | -65% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 264 | 4 | 10% | 3% | +43% | -83% | -88% |
| 2–5 min | 3389 | 25 | 7% | 3% | -28% | -88% | -88% |
| 1–2 min | 2774 | 11 | 3% | 2% | -57% | -94% | -93% |
| Under 1 min | 4104 | 8 | 1% | 0% | -71% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 792 | 6 | 5% | 3% | -9% | -90% | -89% |
| HYPE | 787 | 3 | 5% | 3% | -53% | -88% | -87% |
| DOGE | 783 | 2 | 3% | 1% | -67% | -92% | -92% |
| ETH | 781 | 7 | 5% | 3% | +12% | -88% | -88% |
| BNB | 780 | 3 | 4% | 2% | -53% | -91% | -92% |
| NEAR | 778 | 5 | 6% | 3% | -15% | -69% | -70% |
| SOL | 776 | 0 | 3% | 1% | -100% | -94% | -93% |
| BTC | 775 | 4 | 5% | 2% | -32% | -88% | -90% |
| XRP | 774 | 5 | 2% | 1% | -19% | -80% | -80% |
| GOLD | 443 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 432 | 0 | 3% | 1% | -100% | -95% | -94% |
| WTI | 409 | 3 | 3% | 1% | -20% | -95% | -96% |
| COPPER | 380 | 0 | 1% | 1% | -100% | -99% | -99% |
| PLATINUM | 339 | 0 | 0% | 0% | -100% | -99% | -99% |
| PALLADIUM | 323 | 1 | 2% | 1% | -71% | -97% | -98% |
| NATGAS | 322 | 3 | 3% | 2% | -13% | -95% | -93% |
| EURUSD | 313 | 2 | 4% | 2% | -40% | -64% | -63% |
| GBPUSD | 294 | 1 | 3% | 2% | -68% | -95% | -95% |
| USDJPY | 253 | 3 | 2% | 1% | +11% | -97% | -96% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5349 | 26 | 4% | 2% | -43% | -88% | -87% |
| DOWN (bought NO) | 5185 | 22 | 3% | 2% | -51% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1163 | 8 | 2% | 1% | +18% | -65% | -64% |
| 0.05–0.1% | 1219 | 4 | 3% | 1% | -52% | -92% | -92% |
| 0.1–0.2% | 1785 | 6 | 4% | 2% | -58% | -92% | -92% |
| 0.2–0.5% | 2045 | 12 | 6% | 3% | -36% | -88% | -87% |
| Over 0.5% | 812 | 5 | 6% | 3% | -37% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2764 | 16 | 4% | 2% | -33% | -83% | -84% |
| Morning (6am–12pm) | 2536 | 17 | 5% | 3% | -24% | -90% | -89% |
| Afternoon (12–6pm) | 2244 | 7 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 2990 | 8 | 3% | 1% | -69% | -95% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,046 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/7 3:57:05 AM | USDJPY | DOWN | 2.9 min | — | — | In play | — |
| 10/7 3:55:44 AM | NEAR | UP | 4.2 min | -1.115% | — | In play | — |
| 10/7 3:55:28 AM | WTI | DOWN | 4.5 min | — | — | In play | — |
| 10/7 3:44:56 AM | USDJPY | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 3:44:56 AM | PLATINUM | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 3:44:56 AM | EURUSD | UP | 4 sec | — | 0¢ | ✅ Won | $13.85 |
| 10/7 3:44:56 AM | SILVER | UP | 4 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/7 3:44:24 AM | ZEC | UP | 36 sec | -0.170% | 0¢ | ❌ Lost | $0.00 |
| 10/7 3:44:24 AM | BTC | UP | 36 sec | -0.058% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 3:43:50 AM | PALLADIUM | UP | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 3:43:04 AM | NATGAS | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 3:42:46 AM | GBPUSD | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 3:41:11 AM | XRP | UP | 3.8 min | -0.665% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 3:41:11 AM | BNB | UP | 3.8 min | -0.244% | 19¢ | ❌ Lost | -$0.15 |
| 10/7 3:40:37 AM | NEAR | UP | 4.4 min | -0.902% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 3:40:21 AM | ETH | UP | 4.6 min | -0.358% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 3:40:21 AM | DOGE | UP | 4.6 min | -0.402% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 3:40:21 AM | SOL | UP | 4.6 min | -0.336% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 3:39:32 AM | HYPE | UP | 5.5 min | -0.538% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 3:29:45 AM | EURUSD | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 3:29:45 AM | GOLD | UP | 14 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/7 3:29:29 AM | BNB | UP | 30 sec | -0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/7 3:29:29 AM | GBPUSD | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 3:29:13 AM | XRP | UP | 47 sec | -0.089% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 3:29:13 AM | PALLADIUM | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 3:28:55 AM | SOL | UP | 65 sec | -0.084% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 3:28:55 AM | NEAR | DOWN | 65 sec | +0.256% | 0¢ | ❌ Lost | $0.00 |
| 10/7 3:28:39 AM | ETH | UP | 81 sec | -0.114% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 3:28:08 AM | WTI | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 3:28:08 AM | BTC | UP | 1.9 min | -0.129% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
