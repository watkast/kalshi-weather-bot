# 15-Minute 1¢ Study

*Updated Sat Nov 14, 12:16 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4326 finished bets | 1% | $177.40 | +37% | +4.10¢ | $77.95 / $99.45 |

*Expect about **92 buys a day** (~$13.80/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4068 | $104.40 | +24% |
| Volatility model ≥ 2%, hold to the close | 8000 | $30.10 | +3% |
| Momentum model ≥ 2%, hold to the close | 6647 | -$22.70 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 56750 | 56729 | 216 (0%) | 1.07% | -$3,895.35 (-56%) | Hold to the close: -$3,895.35 (-56%) |

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
| Volatility model | 33863 | 4.6% | 0.4% (137) | -656% | ❌ Worse |
| Momentum model | 33863 | 4.5% | 0.4% (137) | -682% | ❌ Worse |
| Mean-reversion model | 33863 | 8.0% | 0.4% (137) | -796% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 33863 | 137 | -48% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8000 | 71 | +3% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4326 | 47 | +37% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2495 | 29 | +67% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6647 | 53 | -3% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4068 | 39 | +24% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2658 | 25 | +32% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 13915 | 96 | -24% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 9705 | 80 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6465 | 57 | +0% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 34068 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 13651 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9010 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 56729 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 216 | 0% | -$3,895.35 | -56% | — |
| Sell at 2¢ | 2261 | 4% | -$6,037.49 | -87% | 47 sec |
| Sell at 3¢ | 1528 | 3% | -$6,029.43 | -87% | 48 sec |
| Sell at 5¢ | 1048 | 2% | -$5,916.15 | -86% | 63 sec |
| Sell at 10¢ | 638 | 1% | -$5,677.57 | -82% | 65 sec |
| Sell at 25¢ | 334 | 1% | -$5,281.81 | -76% | 82 sec |
| Sell at 50¢ | 221 | 0% | -$4,783.60 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2819 | 13 | 11% | 4% | -56% | -81% | -82% |
| 2–5 min | 18288 | 99 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 14304 | 48 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 21305 | 56 | 1% | 0% | -63% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3812 | 17 | 5% | 2% | -42% | -88% | -87% |
| SOL | 3811 | 17 | 4% | 2% | -43% | -86% | -87% |
| HYPE | 3803 | 11 | 5% | 2% | -64% | -89% | -88% |
| DOGE | 3791 | 9 | 4% | 2% | -70% | -90% | -90% |
| BNB | 3787 | 19 | 5% | 2% | -37% | -86% | -85% |
| ETH | 3785 | 16 | 7% | 3% | -47% | -82% | -82% |
| BTC | 3765 | 19 | 5% | 2% | -31% | -87% | -88% |
| NEAR | 3763 | 17 | 5% | 2% | -41% | -85% | -86% |
| XRP | 3751 | 14 | 3% | 1% | -53% | -89% | -89% |
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
| UP (bought YES) | 28836 | 110 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 27893 | 106 | 4% | 2% | -56% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5309 | 25 | 2% | 1% | -16% | -77% | -77% |
| 0.05–0.1% | 5719 | 21 | 3% | 2% | -43% | -91% | -91% |
| 0.1–0.2% | 8671 | 33 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 10375 | 42 | 6% | 3% | -55% | -87% | -87% |
| Over 0.5% | 3986 | 18 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13742 | 44 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13638 | 63 | 4% | 2% | -48% | -85% | -85% |
| Afternoon (12–6pm) | 13785 | 61 | 4% | 2% | -48% | -86% | -87% |
| Evening (6pm–12am) | 15564 | 48 | 4% | 2% | -65% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,876 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/14 12:14:26 AM | BTC | UP | 34 sec | -0.025% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 12:13:41 AM | NEAR | UP | 79 sec | -0.386% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 12:13:41 AM | DOGE | UP | 79 sec | -0.167% | 0¢ | ❌ Lost | $0.00 |
| 11/14 12:13:41 AM | BNB | UP | 79 sec | -0.184% | 0¢ | ❌ Lost | -$0.15 |
| 11/14 12:13:09 AM | XRP | UP | 1.9 min | -0.232% | 0¢ | ❌ Lost | $0.00 |
| 11/14 12:12:54 AM | HYPE | UP | 2.1 min | -0.290% | 0¢ | ❌ Lost | $0.00 |
| 11/14 12:12:08 AM | ETH | UP | 2.9 min | -0.204% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 12:11:56 AM | SOL | UP | 3.1 min | -0.309% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 12:11:56 AM | ZEC | UP | 3.1 min | -0.475% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 11:59:24 PM | XRP | DOWN | 35 sec | +0.091% | 0¢ | ❌ Lost | $0.00 |
| 11/13 11:59:10 PM | ZEC | DOWN | 50 sec | +0.263% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 11:58:09 PM | NEAR | DOWN | 1.8 min | +0.203% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 11:58:09 PM | DOGE | DOWN | 1.8 min | +0.151% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 11:57:39 PM | ETH | DOWN | 2.4 min | +0.180% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 11:57:39 PM | BTC | DOWN | 2.4 min | +0.174% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 11:57:23 PM | BNB | DOWN | 2.6 min | +0.227% | 0¢ | ❌ Lost | $0.00 |
| 11/13 11:57:07 PM | SOL | DOWN | 2.9 min | +0.270% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 11:56:06 PM | HYPE | DOWN | 3.9 min | +0.441% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 11:44:08 PM | BTC | UP | 52 sec | -0.111% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 11:43:37 PM | HYPE | UP | 83 sec | -0.505% | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:43:23 PM | ETH | UP | 1.6 min | -0.181% | 0¢ | ❌ Lost | $0.00 |
| 11/13 11:43:23 PM | SOL | UP | 1.6 min | -0.249% | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:42:06 PM | NEAR | UP | 2.9 min | -0.555% | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:41:21 PM | XRP | UP | 3.6 min | -0.261% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 11:41:05 PM | ZEC | UP | 3.9 min | -0.722% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 11:40:19 PM | DOGE | UP | 4.7 min | -0.331% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 11:40:19 PM | BNB | UP | 4.7 min | -0.440% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 11:29:56 PM | HYPE | UP | 4 sec | -0.095% | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:29:56 PM | ZEC | DOWN | 4 sec | +0.005% | 0¢ | ❌ Lost | $0.00 |
| 11/13 11:29:42 PM | XRP | DOWN | 18 sec | -0.010% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
