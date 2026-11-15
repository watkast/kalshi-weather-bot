# 15-Minute 1¢ Study

*Updated Sat Nov 14, 11:49 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4368 finished bets | 1% | $228.75 | +47% | +5.24¢ | $75.10 / $153.65 |

*Expect about **91 buys a day** (~$13.65/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4116 | $127.00 | +28% |
| Volatility model ≥ 2%, hold to the close | 8111 | $72.15 | +7% |
| Momentum model ≥ 2%, hold to the close | 6739 | $8.20 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 57442 | 57421 | 222 (0%) | 1.07% | -$3,884.10 (-56%) | Hold to the close: -$3,884.10 (-56%) |

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
| Volatility model | 34554 | 4.6% | 0.4% (143) | -639% | ❌ Worse |
| Momentum model | 34554 | 4.5% | 0.4% (143) | -664% | ❌ Worse |
| Mean-reversion model | 34554 | 7.9% | 0.4% (143) | -777% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 34554 | 143 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8111 | 75 | +7% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4368 | 51 | +47% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2512 | 30 | +72% | -62% | -61% | -57% |
| Momentum model ≥ 2% | 6739 | 56 | +1% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4116 | 41 | +28% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2681 | 26 | +36% | -66% | -66% | -61% |
| Mean-reversion model ≥ 2% | 14182 | 100 | -23% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 9870 | 84 | -6% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6565 | 60 | +4% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 34760 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 13651 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9010 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 57421 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 222 | 0% | -$3,884.10 | -56% | — |
| Sell at 2¢ | 2309 | 4% | -$6,097.76 | -87% | 47 sec |
| Sell at 3¢ | 1559 | 3% | -$6,090.09 | -87% | 48 sec |
| Sell at 5¢ | 1069 | 2% | -$5,975.25 | -85% | 62 sec |
| Sell at 10¢ | 650 | 1% | -$5,734.60 | -82% | 65 sec |
| Sell at 25¢ | 342 | 1% | -$5,328.08 | -76% | 80 sec |
| Sell at 50¢ | 227 | 0% | -$4,801.85 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2879 | 13 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 18527 | 100 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 14490 | 51 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 21512 | 58 | 1% | 0% | -61% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3891 | 19 | 5% | 3% | -36% | -88% | -87% |
| SOL | 3884 | 17 | 4% | 2% | -44% | -86% | -86% |
| HYPE | 3883 | 12 | 5% | 2% | -61% | -89% | -88% |
| BNB | 3868 | 20 | 5% | 2% | -35% | -85% | -85% |
| DOGE | 3867 | 10 | 4% | 2% | -67% | -90% | -89% |
| ETH | 3861 | 16 | 6% | 3% | -48% | -82% | -82% |
| BTC | 3841 | 20 | 5% | 2% | -29% | -86% | -88% |
| NEAR | 3838 | 17 | 5% | 2% | -42% | -85% | -86% |
| XRP | 3827 | 14 | 3% | 1% | -54% | -89% | -89% |
| GOLD | 2047 | 5 | 5% | 2% | -70% | -82% | -84% |
| WTI | 2031 | 7 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 1988 | 9 | 5% | 2% | -46% | -83% | -83% |
| PLATINUM | 1809 | 4 | 3% | 1% | -79% | -95% | -95% |
| EURUSD | 1754 | 6 | 3% | 1% | -68% | -90% | -90% |
| COPPER | 1699 | 6 | 2% | 1% | -67% | -75% | -75% |
| GBPUSD | 1679 | 6 | 2% | 1% | -67% | -96% | -96% |
| NATGAS | 1674 | 9 | 2% | 1% | -50% | -74% | -74% |
| USDJPY | 1646 | 6 | 2% | 1% | -66% | -97% | -96% |
| PALLADIUM | 1626 | 4 | 1% | 0% | -77% | -92% | -93% |
| AUDUSD | 1199 | 6 | 2% | 1% | -53% | -89% | -89% |
| USDCAD | 1162 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 777 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 401 | 2 | 4% | 1% | -53% | -70% | -68% |
| 2YRRATE | 384 | 4 | 4% | 2% | -3% | -45% | -43% |
| 30YRRATE | 376 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 355 | 2 | 4% | 2% | -47% | -93% | -95% |
| INX | 54 | 0 | 2% | 0% | -100% | -97% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 29221 | 112 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 28200 | 110 | 4% | 2% | -55% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5337 | 25 | 2% | 1% | -16% | -77% | -77% |
| 0.05–0.1% | 5764 | 23 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 8767 | 34 | 5% | 2% | -51% | -89% | -89% |
| 0.2–0.5% | 10630 | 44 | 6% | 3% | -53% | -86% | -86% |
| Over 0.5% | 4253 | 19 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13892 | 44 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13774 | 67 | 4% | 2% | -45% | -85% | -84% |
| Afternoon (12–6pm) | 13991 | 62 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 15764 | 49 | 4% | 2% | -64% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,026 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/14 11:44:32 PM | ZEC | DOWN | 27 sec | +0.292% | 0¢ | ❌ Lost | $0.00 |
| 11/14 11:44:16 PM | XRP | DOWN | 43 sec | +0.198% | 0¢ | ❌ Lost | $0.00 |
| 11/14 11:44:00 PM | NEAR | UP | 59 sec | -0.362% | 3¢ | ❌ Lost | -$0.15 |
| 11/14 11:43:29 PM | BTC | UP | 1.5 min | -0.171% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 11:43:29 PM | DOGE | UP | 1.5 min | -0.231% | 9¢ | ❌ Lost | -$0.15 |
| 11/14 11:43:29 PM | BNB | UP | 1.5 min | -0.209% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 11:43:13 PM | HYPE | UP | 1.8 min | -0.301% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 11:43:13 PM | ETH | UP | 1.8 min | -0.276% | 0¢ | ❌ Lost | $0.00 |
| 11/14 11:40:49 PM | SOL | UP | 4.2 min | -0.583% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 11:26:58 PM | HYPE | DOWN | 3.0 min | +0.397% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 11:26:42 PM | DOGE | DOWN | 3.3 min | +0.533% | 0¢ | ❌ Lost | -$0.15 |
| 11/14 11:26:42 PM | ETH | DOWN | 3.3 min | +0.374% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 11:26:26 PM | BTC | DOWN | 3.6 min | +0.364% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 11:26:10 PM | ZEC | DOWN | 3.8 min | +0.897% | 0¢ | ❌ Lost | $0.00 |
| 11/14 11:26:10 PM | BNB | DOWN | 3.8 min | +0.325% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 11:26:10 PM | XRP | DOWN | 3.8 min | +0.662% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 11:25:38 PM | SOL | DOWN | 4.3 min | +0.639% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 11:23:47 PM | NEAR | DOWN | 6.2 min | +0.981% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 11:11:30 PM | BTC | UP | 3.5 min | -0.437% | 3¢ | ❌ Lost | -$0.15 |
| 11/14 11:10:25 PM | XRP | UP | 4.6 min | -0.751% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 11:10:10 PM | NEAR | UP | 4.8 min | -0.973% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 11:10:10 PM | HYPE | UP | 4.8 min | -0.782% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 11:09:53 PM | ETH | UP | 5.1 min | -0.825% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 11:09:53 PM | DOGE | UP | 5.1 min | -0.685% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 11:09:37 PM | BNB | UP | 5.4 min | -0.652% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 11:09:37 PM | SOL | UP | 5.4 min | -0.943% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 11:09:06 PM | ZEC | UP | 5.9 min | -1.149% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 10:59:31 PM | NEAR | UP | 28 sec | -0.262% | 0¢ | ❌ Lost | $0.00 |
| 11/14 10:58:44 PM | XRP | UP | 76 sec | -0.291% | 0¢ | ❌ Lost | $0.00 |
| 11/14 10:57:40 PM | ETH | UP | 2.3 min | -0.265% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
