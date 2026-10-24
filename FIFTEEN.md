# 15-Minute 1¢ Study

*Updated Fri Oct 23, 6:22 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2509 finished bets | 1% | $93.75 | +33% | +3.74¢ | $44.45 / $49.30 |

*Expect about **97 buys a day** (~$14.62/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2317 | $51.50 | +20% |
| Volatility model ≥ 2%, hold to the close | 4651 | $4.30 | +1% |
| Momentum model ≥ 2%, hold to the close | 3872 | -$21.55 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 30434 | 30426 | 117 (0%) | 1.07% | -$2,075.25 (-56%) | Hold to the close: -$2,075.25 (-56%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 19237 | 4.6% | 0.4% (82) | -635% | ❌ Worse |
| Momentum model | 19237 | 4.5% | 0.4% (82) | -661% | ❌ Worse |
| Mean-reversion model | 19237 | 7.9% | 0.4% (82) | -765% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 19237 | 82 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4651 | 41 | +1% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2509 | 27 | +33% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 1430 | 17 | +67% | -64% | -62% | -59% |
| Momentum model ≥ 2% | 3872 | 31 | -5% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2317 | 22 | +20% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 1522 | 15 | +36% | -69% | -68% | -63% |
| Mean-reversion model ≥ 2% | 7738 | 54 | -24% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5407 | 45 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3598 | 32 | +1% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 19437 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 7334 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3655 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 30426 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 117 | 0% | -$2,075.25 | -56% | — |
| Sell at 2¢ | 1133 | 4% | -$3,250.67 | -88% | 47 sec |
| Sell at 3¢ | 777 | 3% | -$3,242.22 | -87% | 48 sec |
| Sell at 5¢ | 545 | 2% | -$3,191.00 | -86% | 61 sec |
| Sell at 10¢ | 333 | 1% | -$3,067.02 | -83% | 64 sec |
| Sell at 25¢ | 185 | 1% | -$2,820.90 | -76% | 82 sec |
| Sell at 50¢ | 119 | 0% | -$2,546.00 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1300 | 7 | 11% | 4% | -49% | -81% | -83% |
| 2–5 min | 9739 | 53 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 7743 | 29 | 3% | 1% | -59% | -91% | -91% |
| Under 1 min | 11640 | 28 | 1% | 0% | -66% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2179 | 12 | 5% | 2% | -31% | -89% | -89% |
| BNB | 2170 | 12 | 5% | 2% | -32% | -83% | -82% |
| HYPE | 2169 | 8 | 5% | 3% | -54% | -88% | -86% |
| SOL | 2162 | 5 | 4% | 2% | -71% | -92% | -92% |
| ETH | 2159 | 10 | 6% | 3% | -44% | -86% | -85% |
| DOGE | 2156 | 4 | 4% | 2% | -77% | -90% | -89% |
| XRP | 2150 | 9 | 3% | 1% | -48% | -88% | -88% |
| NEAR | 2147 | 12 | 5% | 3% | -27% | -81% | -81% |
| BTC | 2145 | 12 | 5% | 2% | -25% | -88% | -89% |
| GOLD | 1190 | 4 | 4% | 2% | -60% | -81% | -83% |
| SILVER | 1156 | 5 | 4% | 1% | -50% | -82% | -82% |
| WTI | 1132 | 3 | 3% | 1% | -69% | -94% | -95% |
| PLATINUM | 1010 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 987 | 4 | 1% | 1% | -62% | -69% | -69% |
| EURUSD | 938 | 3 | 2% | 1% | -70% | -86% | -86% |
| NATGAS | 931 | 5 | 2% | 1% | -50% | -86% | -86% |
| PALLADIUM | 897 | 2 | 1% | 0% | -79% | -88% | -88% |
| GBPUSD | 884 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 866 | 5 | 1% | 1% | -46% | -98% | -97% |
| AUDUSD | 428 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 387 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 31 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 15368 | 64 | 4% | 2% | -52% | -87% | -86% |
| DOWN (bought NO) | 15058 | 53 | 4% | 2% | -60% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3192 | 17 | 2% | 1% | -10% | -79% | -78% |
| 0.05–0.1% | 3339 | 11 | 3% | 2% | -52% | -92% | -91% |
| 0.1–0.2% | 5008 | 18 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 5702 | 28 | 6% | 3% | -46% | -87% | -86% |
| Over 0.5% | 2192 | 10 | 7% | 3% | -53% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7532 | 31 | 4% | 2% | -53% | -84% | -84% |
| Morning (6am–12pm) | 7425 | 34 | 4% | 2% | -48% | -88% | -87% |
| Afternoon (12–6pm) | 7298 | 24 | 4% | 2% | -61% | -87% | -88% |
| Evening (6pm–12am) | 8171 | 28 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,602 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/23 6:14:51 PM | NEAR | UP | 9 sec | -0.271% | 0¢ | ❌ Lost | $0.00 |
| 10/23 6:14:04 PM | DOGE | UP | 55 sec | -0.134% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 6:13:48 PM | ZEC | UP | 71 sec | -0.285% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 6:13:32 PM | XRP | UP | 87 sec | -0.201% | 0¢ | ❌ Lost | $0.00 |
| 10/23 6:13:16 PM | BNB | UP | 1.7 min | -0.110% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 6:13:16 PM | SOL | UP | 1.7 min | -0.213% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 6:13:16 PM | HYPE | UP | 1.7 min | -0.227% | 0¢ | ❌ Lost | $0.00 |
| 10/23 6:11:39 PM | ETH | UP | 3.4 min | -0.191% | 1¢ | ❌ Lost | $0.00 |
| 10/23 6:11:23 PM | BTC | UP | 3.6 min | -0.189% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 5:55:51 PM | ZEC | DOWN | 4.2 min | +0.610% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 5:55:51 PM | NEAR | DOWN | 4.2 min | +0.446% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 5:55:09 PM | HYPE | DOWN | 4.8 min | +0.342% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 5:54:53 PM | DOGE | DOWN | 5.1 min | +0.268% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 5:54:53 PM | XRP | DOWN | 5.1 min | +0.256% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 5:54:38 PM | SOL | DOWN | 5.3 min | +0.325% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 5:54:38 PM | BTC | DOWN | 5.3 min | +0.281% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 5:53:34 PM | ETH | DOWN | 6.4 min | +0.270% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 5:53:34 PM | BNB | DOWN | 6.4 min | +0.248% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 5:44:38 PM | ZEC | UP | 21 sec | -0.056% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 5:44:38 PM | BTC | UP | 21 sec | -0.023% | 0¢ | ❌ Lost | $0.00 |
| 10/23 5:44:38 PM | XRP | DOWN | 21 sec | +0.008% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 5:44:22 PM | BNB | DOWN | 37 sec | +0.033% | 0¢ | ❌ Lost | $0.00 |
| 10/23 5:44:22 PM | NEAR | UP | 37 sec | -0.344% | 0¢ | ❌ Lost | $0.00 |
| 10/23 5:44:06 PM | ETH | DOWN | 53 sec | +0.073% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 5:44:06 PM | DOGE | DOWN | 53 sec | +0.075% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 5:43:50 PM | SOL | UP | 70 sec | -0.105% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 5:43:50 PM | HYPE | UP | 70 sec | -0.110% | 13¢ | ❌ Lost | -$0.15 |
| 10/23 5:29:51 PM | BRENT | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 5:29:51 PM | WTI | UP | 9 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/23 5:29:35 PM | NATGAS | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
