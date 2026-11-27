# 15-Minute 1¢ Study

*Updated Fri Nov 27, 12:34 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 5018 finished bets | 1% | $197.80 | +36% | +3.94¢ | $93.75 / $104.05 |

*Expect about **83 buys a day** (~$12.44/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4757 | $98.15 | +19% |
| Volatility model ≥ 2%, hold to the close | 9369 | $21.30 | +2% |
| Momentum model ≥ 2%, hold to the close | 7793 | -$55.10 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 69525 | 69489 | 257 (0%) | 1.07% | -$4,814.00 (-57%) | Hold to the close: -$4,814.00 (-57%) |

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
| Volatility model | 40981 | 4.5% | 0.4% (165) | -662% | ❌ Worse |
| Momentum model | 40981 | 4.5% | 0.4% (165) | -685% | ❌ Worse |
| Mean-reversion model | 40981 | 7.9% | 0.4% (165) | -803% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 40981 | 165 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 9369 | 81 | +2% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 5018 | 53 | +36% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 2913 | 32 | +64% | -65% | -64% | -60% |
| Momentum model ≥ 2% | 7793 | 59 | -6% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 4757 | 43 | +19% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 3104 | 28 | +31% | -68% | -68% | -64% |
| Mean-reversion model ≥ 2% | 16734 | 113 | -25% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11657 | 93 | -11% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 7732 | 66 | -2% | -78% | -78% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 41187 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 16629 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 11673 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 69489 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 257 | 0% | -$4,814.00 | -57% | — |
| Sell at 2¢ | 2846 | 4% | -$7,364.04 | -88% | 47 sec |
| Sell at 3¢ | 1911 | 3% | -$7,358.71 | -87% | 48 sec |
| Sell at 5¢ | 1292 | 2% | -$7,236.20 | -86% | 62 sec |
| Sell at 10¢ | 791 | 1% | -$6,955.79 | -83% | 65 sec |
| Sell at 25¢ | 427 | 1% | -$6,424.63 | -76% | 80 sec |
| Sell at 50¢ | 271 | 0% | -$5,826.75 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3608 | 17 | 10% | 4% | -55% | -82% | -83% |
| 2–5 min | 22534 | 116 | 7% | 3% | -49% | -86% | -86% |
| 1–2 min | 17280 | 58 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 26054 | 66 | 1% | 0% | -63% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4608 | 20 | 5% | 2% | -42% | -88% | -87% |
| HYPE | 4597 | 16 | 5% | 2% | -55% | -89% | -88% |
| SOL | 4591 | 20 | 4% | 2% | -43% | -86% | -86% |
| BNB | 4585 | 22 | 5% | 2% | -39% | -86% | -85% |
| DOGE | 4582 | 12 | 4% | 2% | -66% | -89% | -89% |
| ETH | 4576 | 19 | 7% | 3% | -48% | -82% | -82% |
| BTC | 4555 | 24 | 5% | 2% | -27% | -86% | -88% |
| NEAR | 4550 | 18 | 5% | 2% | -48% | -85% | -86% |
| XRP | 4543 | 16 | 4% | 2% | -55% | -89% | -88% |
| GOLD | 2455 | 8 | 5% | 2% | -60% | -83% | -84% |
| WTI | 2438 | 9 | 4% | 2% | -55% | -86% | -87% |
| SILVER | 2405 | 9 | 5% | 2% | -55% | -83% | -84% |
| PLATINUM | 2172 | 5 | 3% | 1% | -79% | -95% | -95% |
| EURUSD | 2129 | 7 | 2% | 1% | -69% | -91% | -90% |
| GBPUSD | 2076 | 8 | 2% | 1% | -64% | -96% | -95% |
| COPPER | 2060 | 6 | 2% | 1% | -73% | -79% | -79% |
| USDJPY | 2025 | 6 | 2% | 1% | -72% | -97% | -96% |
| NATGAS | 2014 | 10 | 2% | 1% | -54% | -77% | -77% |
| PALLADIUM | 1962 | 4 | 1% | 1% | -81% | -93% | -93% |
| AUDUSD | 1602 | 7 | 2% | 1% | -59% | -90% | -90% |
| USDCAD | 1503 | 1 | 3% | 1% | -94% | -96% | -96% |
| BRENT | 1123 | 1 | 2% | 1% | -92% | -96% | -97% |
| 10YRRATE | 564 | 2 | 3% | 1% | -67% | -78% | -76% |
| 30YRRATE | 526 | 0 | 3% | 1% | -100% | -95% | -93% |
| 2YRRATE | 523 | 4 | 4% | 2% | -29% | -58% | -57% |
| 5YRRATE | 514 | 2 | 4% | 2% | -64% | -94% | -95% |
| INX | 142 | 1 | 2% | 1% | -34% | -96% | -96% |
| USDMXN | 69 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 35351 | 133 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 34138 | 124 | 4% | 2% | -58% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5963 | 25 | 2% | 1% | -22% | -79% | -78% |
| 0.05–0.1% | 6530 | 26 | 3% | 2% | -36% | -91% | -91% |
| 0.1–0.2% | 10201 | 36 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 12991 | 56 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 5493 | 24 | 7% | 3% | -54% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16692 | 51 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 16558 | 82 | 4% | 2% | -43% | -86% | -85% |
| Afternoon (12–6pm) | 16968 | 73 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 19271 | 51 | 4% | 2% | -69% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,066 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/27 12:29:53 PM | SILVER | DOWN | 6 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/27 12:29:35 PM | DOGE | DOWN | 24 sec | -0.029% | 0¢ | ❌ Lost | $0.00 |
| 11/27 12:29:35 PM | EURUSD | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 12:29:35 PM | ZEC | DOWN | 24 sec | +0.049% | 0¢ | ❌ Lost | $0.00 |
| 11/27 12:28:47 PM | BRENT | DOWN | 73 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 12:28:47 PM | USDJPY | DOWN | 73 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 12:28:13 PM | XRP | DOWN | 1.8 min | +0.126% | 0¢ | ❌ Lost | -$0.15 |
| 11/27 12:27:41 PM | ETH | DOWN | 2.3 min | +0.145% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 12:27:21 PM | SOL | DOWN | 2.6 min | +0.164% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 12:27:21 PM | NEAR | DOWN | 2.6 min | +0.121% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 12:26:16 PM | BNB | DOWN | 3.7 min | +0.087% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 12:26:16 PM | HYPE | DOWN | 3.7 min | +0.290% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 12:26:16 PM | BTC | DOWN | 3.7 min | +0.173% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 12:14:51 PM | PLATINUM | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 12:14:35 PM | WTI | DOWN | 24 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/27 12:14:35 PM | XRP | DOWN | 24 sec | +0.021% | 0¢ | ❌ Lost | $0.00 |
| 11/27 12:14:19 PM | USDCAD | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 12:14:19 PM | ETH | UP | 41 sec | -0.066% | 0¢ | ❌ Lost | $0.00 |
| 11/27 12:14:19 PM | GOLD | DOWN | 41 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/27 12:14:19 PM | BRENT | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 12:14:03 PM | COPPER | DOWN | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 12:13:47 PM | HYPE | DOWN | 73 sec | +0.114% | 0¢ | ❌ Lost | $0.00 |
| 11/27 12:13:47 PM | SOL | DOWN | 73 sec | +0.130% | 0¢ | ❌ Lost | $0.00 |
| 11/27 12:13:47 PM | ZEC | DOWN | 73 sec | +0.242% | 0¢ | ❌ Lost | -$0.15 |
| 11/27 12:13:25 PM | BNB | UP | 1.6 min | -0.125% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 12:13:25 PM | NEAR | DOWN | 1.6 min | +0.145% | 0¢ | ❌ Lost | $0.00 |
| 11/27 12:13:07 PM | BTC | UP | 1.9 min | -0.148% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 12:12:35 PM | DOGE | DOWN | 2.4 min | +0.209% | 0¢ | ❌ Lost | $0.00 |
| 11/27 11:59:57 AM | WTI | UP | 2 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/27 11:59:57 AM | PALLADIUM | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
