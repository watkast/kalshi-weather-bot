# 15-Minute 1¢ Study

*Updated Wed Oct 7, 3:06 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 723 finished bets | 1% | $34.45 | +44% | +4.76¢ | -$11.00 / $45.45 |

*Expect about **79 buys a day** (~$11.92/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 720 | $21.80 | +29% |
| 5+ min left, hold to the close | 266 | $16.55 | +42% |
| Mean-reversion model ≥ 5%, hold to the close | 1579 | $11.55 | +6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 10494 | 10488 | 47 (0%) | 1.07% | -$611.00 (-48%) | Hold to the close: -$611.00 (-48%) |

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
| Volatility model | 6804 | 4.2% | 0.5% (33) | -566% | ❌ Worse |
| Momentum model | 6804 | 4.2% | 0.5% (33) | -594% | ❌ Worse |
| Mean-reversion model | 6804 | 6.8% | 0.5% (33) | -654% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6804 | 33 | -39% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 1323 | 12 | +6% | -73% | -73% | -69% |
| Volatility model ≥ 5% | 723 | 8 | +44% | -62% | -61% | -58% |
| Volatility model ≥ 10% | 453 | 6 | +96% | -45% | -46% | -41% |
| Momentum model ≥ 2% | 1179 | 10 | +3% | -73% | -75% | -73% |
| Momentum model ≥ 5% | 720 | 7 | +29% | -66% | -68% | -65% |
| Momentum model ≥ 10% | 501 | 6 | +73% | -56% | -57% | -54% |
| Mean-reversion model ≥ 2% | 2328 | 19 | -11% | -84% | -84% | -80% |
| Mean-reversion model ≥ 5% | 1579 | 15 | +6% | -81% | -81% | -75% |
| Mean-reversion model ≥ 10% | 1047 | 11 | +22% | -79% | -79% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7001 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2635 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 852 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 10488 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 47 | 0% | -$611.00 | -48% | — |
| Sell at 2¢ | 371 | 4% | -$1,144.54 | -90% | 33 sec |
| Sell at 3¢ | 247 | 2% | -$1,144.67 | -90% | 47 sec |
| Sell at 5¢ | 185 | 2% | -$1,120.75 | -88% | 60 sec |
| Sell at 10¢ | 124 | 1% | -$1,064.56 | -84% | 65 sec |
| Sell at 25¢ | 71 | 1% | -$963.99 | -76% | 82 sec |
| Sell at 50¢ | 47 | 0% | -$839.75 | -66% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 263 | 4 | 10% | 3% | +44% | -83% | -88% |
| 2–5 min | 3374 | 25 | 7% | 3% | -28% | -88% | -88% |
| 1–2 min | 2763 | 11 | 3% | 2% | -57% | -94% | -93% |
| Under 1 min | 4085 | 7 | 1% | 0% | -75% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 790 | 6 | 5% | 3% | -9% | -90% | -89% |
| HYPE | 784 | 3 | 5% | 3% | -53% | -88% | -87% |
| DOGE | 780 | 2 | 3% | 1% | -67% | -92% | -92% |
| ETH | 778 | 7 | 5% | 3% | +12% | -88% | -87% |
| BNB | 777 | 3 | 4% | 2% | -53% | -91% | -93% |
| NEAR | 775 | 5 | 6% | 3% | -15% | -69% | -70% |
| SOL | 774 | 0 | 3% | 1% | -100% | -94% | -93% |
| BTC | 772 | 4 | 5% | 2% | -31% | -88% | -90% |
| XRP | 771 | 5 | 2% | 1% | -18% | -80% | -80% |
| GOLD | 442 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 429 | 0 | 2% | 1% | -100% | -95% | -95% |
| WTI | 407 | 3 | 3% | 1% | -20% | -95% | -96% |
| COPPER | 380 | 0 | 1% | 1% | -100% | -99% | -99% |
| PLATINUM | 336 | 0 | 0% | 0% | -100% | -99% | -99% |
| NATGAS | 321 | 3 | 3% | 2% | -13% | -95% | -93% |
| PALLADIUM | 320 | 1 | 2% | 1% | -71% | -97% | -98% |
| EURUSD | 310 | 1 | 4% | 2% | -70% | -94% | -92% |
| GBPUSD | 291 | 1 | 3% | 2% | -68% | -95% | -95% |
| USDJPY | 251 | 3 | 2% | 1% | +12% | -97% | -96% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5308 | 25 | 4% | 2% | -45% | -90% | -89% |
| DOWN (bought NO) | 5180 | 22 | 3% | 2% | -51% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1160 | 8 | 2% | 1% | +18% | -65% | -64% |
| 0.05–0.1% | 1215 | 4 | 3% | 1% | -52% | -92% | -92% |
| 0.1–0.2% | 1780 | 6 | 4% | 2% | -58% | -92% | -92% |
| 0.2–0.5% | 2036 | 12 | 6% | 3% | -35% | -88% | -87% |
| Over 0.5% | 808 | 5 | 6% | 3% | -37% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2718 | 15 | 4% | 2% | -37% | -87% | -88% |
| Morning (6am–12pm) | 2536 | 17 | 5% | 3% | -24% | -90% | -89% |
| Afternoon (12–6pm) | 2244 | 7 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 2990 | 8 | 3% | 1% | -69% | -95% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,052 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/7 2:59:53 AM | WTI | DOWN | 7 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 2:59:53 AM | GBPUSD | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 2:59:21 AM | USDJPY | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 2:59:21 AM | BTC | UP | 39 sec | -0.052% | 0¢ | ❌ Lost | $0.00 |
| 10/7 2:58:33 AM | SOL | UP | 87 sec | -0.152% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 2:58:33 AM | SILVER | UP | 87 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/7 2:58:33 AM | GOLD | UP | 87 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 2:58:33 AM | ETH | UP | 87 sec | -0.111% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 2:58:17 AM | PLATINUM | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 2:58:17 AM | BNB | UP | 1.7 min | -0.112% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 2:58:17 AM | PALLADIUM | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 2:58:17 AM | COPPER | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 2:57:45 AM | XRP | UP | 2.2 min | -0.171% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 2:57:13 AM | HYPE | UP | 2.8 min | -0.199% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 2:56:38 AM | NEAR | UP | 3.4 min | -0.818% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 2:56:23 AM | ZEC | UP | 3.6 min | -0.529% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 2:56:07 AM | DOGE | UP | 3.9 min | -0.321% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 2:44:44 AM | NEAR | DOWN | 16 sec | -0.023% | 0¢ | ❌ Lost | $0.00 |
| 10/7 2:44:44 AM | COPPER | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 2:44:28 AM | DOGE | UP | 32 sec | -0.048% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 2:44:28 AM | SILVER | DOWN | 32 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 2:44:12 AM | EURUSD | DOWN | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 2:44:12 AM | XRP | UP | 48 sec | -0.102% | 0¢ | ❌ Lost | $0.00 |
| 10/7 2:44:12 AM | BTC | UP | 48 sec | -0.090% | 0¢ | ❌ Lost | $0.00 |
| 10/7 2:43:55 AM | WTI | UP | 64 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 2:43:55 AM | SOL | UP | 64 sec | -0.102% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 2:43:39 AM | ZEC | DOWN | 80 sec | +0.170% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 2:42:51 AM | HYPE | DOWN | 2.1 min | +0.176% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 2:42:18 AM | ETH | UP | 2.7 min | -0.160% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 2:42:02 AM | BNB | UP | 3.0 min | -0.233% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
