# 15-Minute 1¢ Study

*Updated Sun Nov 15, 7:01 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4386 finished bets | 1% | $226.65 | +47% | +5.17¢ | $74.05 / $152.60 |

*Expect about **91 buys a day** (~$13.62/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4136 | $124.90 | +28% |
| Volatility model ≥ 2%, hold to the close | 8156 | $66.90 | +7% |
| Momentum model ≥ 2%, hold to the close | 6780 | $3.55 | +0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 57638 | 57612 | 222 (0%) | 1.07% | -$3,900.60 (-56%) | Hold to the close: -$3,900.60 (-56%) |

*In play or awaiting result: 14. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 34745 | 4.6% | 0.4% (143) | -640% | ❌ Worse |
| Momentum model | 34745 | 4.5% | 0.4% (143) | -666% | ❌ Worse |
| Mean-reversion model | 34745 | 7.9% | 0.4% (143) | -779% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 34745 | 143 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8156 | 75 | +7% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4386 | 51 | +47% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2519 | 30 | +71% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6780 | 56 | +0% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4136 | 41 | +28% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2691 | 26 | +36% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14261 | 100 | -23% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 9922 | 84 | -6% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6588 | 60 | +3% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 34951 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 13651 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9010 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 57612 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 222 | 0% | -$3,900.60 | -56% | — |
| Sell at 2¢ | 2315 | 4% | -$6,112.70 | -87% | 47 sec |
| Sell at 3¢ | 1562 | 3% | -$6,105.42 | -87% | 48 sec |
| Sell at 5¢ | 1071 | 2% | -$5,990.45 | -85% | 62 sec |
| Sell at 10¢ | 652 | 1% | -$5,748.48 | -82% | 65 sec |
| Sell at 25¢ | 343 | 1% | -$5,341.27 | -76% | 80 sec |
| Sell at 50¢ | 228 | 0% | -$4,811.60 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2883 | 13 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 18600 | 100 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 14532 | 51 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 21584 | 58 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3913 | 19 | 5% | 3% | -36% | -88% | -87% |
| SOL | 3907 | 17 | 4% | 2% | -44% | -86% | -86% |
| HYPE | 3905 | 12 | 5% | 2% | -61% | -89% | -88% |
| DOGE | 3889 | 10 | 4% | 2% | -68% | -90% | -89% |
| BNB | 3888 | 20 | 5% | 2% | -35% | -85% | -85% |
| ETH | 3879 | 16 | 6% | 3% | -49% | -82% | -82% |
| BTC | 3861 | 20 | 5% | 2% | -30% | -86% | -88% |
| NEAR | 3859 | 17 | 5% | 2% | -43% | -85% | -86% |
| XRP | 3850 | 14 | 3% | 1% | -54% | -89% | -89% |
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
| UP (bought YES) | 29328 | 112 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 28284 | 110 | 4% | 2% | -55% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5348 | 25 | 2% | 1% | -17% | -77% | -77% |
| 0.05–0.1% | 5786 | 23 | 3% | 2% | -39% | -91% | -91% |
| 0.1–0.2% | 8807 | 34 | 5% | 2% | -51% | -89% | -89% |
| 0.2–0.5% | 10715 | 44 | 6% | 3% | -54% | -86% | -86% |
| Over 0.5% | 4286 | 19 | 7% | 3% | -54% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14049 | 44 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13800 | 67 | 4% | 2% | -45% | -85% | -84% |
| Afternoon (12–6pm) | 13991 | 62 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 15772 | 49 | 4% | 2% | -64% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,052 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/15 6:59:49 AM | ETH | UP | 11 sec | -0.112% | 0¢ | In play | — |
| 11/15 6:59:43 AM | SOL | UP | 17 sec | -0.137% | 0¢ | ❌ Lost | $0.00 |
| 11/15 6:59:33 AM | BNB | DOWN | 27 sec | +0.002% | 0¢ | In play | — |
| 11/15 6:59:23 AM | ZEC | UP | 37 sec | -0.122% | 0¢ | In play | — |
| 11/15 6:59:19 AM | DOGE | UP | 41 sec | -0.145% | 0¢ | In play | — |
| 11/15 6:58:36 AM | XRP | UP | 83 sec | -0.195% | 0¢ | ❌ Lost | -$0.15 |
| 11/15 6:58:24 AM | NEAR | UP | 1.6 min | -0.487% | 0¢ | In play | — |
| 11/15 6:44:45 AM | BNB | UP | 14 sec | -0.054% | 0¢ | ❌ Lost | -$0.15 |
| 11/15 6:44:39 AM | BTC | UP | 20 sec | -0.068% | 0¢ | ❌ Lost | $0.00 |
| 11/15 6:44:31 AM | ZEC | UP | 28 sec | -0.393% | 0¢ | ❌ Lost | $0.00 |
| 11/15 6:44:01 AM | ETH | UP | 59 sec | -0.134% | 0¢ | ❌ Lost | -$0.15 |
| 11/15 6:43:13 AM | NEAR | UP | 1.8 min | -0.417% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 6:42:41 AM | DOGE | UP | 2.3 min | -0.283% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 6:42:39 AM | HYPE | UP | 2.3 min | -0.356% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 6:42:33 AM | SOL | UP | 2.4 min | -0.349% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 6:42:25 AM | XRP | UP | 2.6 min | -0.349% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 6:29:22 AM | HYPE | DOWN | 38 sec | +0.190% | 0¢ | ❌ Lost | $0.00 |
| 11/15 6:29:10 AM | SOL | UP | 50 sec | -0.183% | 0¢ | ❌ Lost | -$0.15 |
| 11/15 6:28:56 AM | BNB | UP | 64 sec | -0.309% | 0¢ | ❌ Lost | $0.00 |
| 11/15 6:28:56 AM | ZEC | UP | 64 sec | -0.558% | 0¢ | ❌ Lost | $0.00 |
| 11/15 6:28:11 AM | DOGE | DOWN | 1.8 min | +0.271% | 22¢ | ❌ Lost | $0.00 |
| 11/15 6:28:09 AM | BTC | DOWN | 1.9 min | +0.235% | 60¢ | ❌ Lost | $0.00 |
| 11/15 6:24:46 AM | XRP | DOWN | 5.2 min | +0.566% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 6:14:43 AM | ETH | UP | 16 sec | -0.137% | 0¢ | ❌ Lost | $0.00 |
| 11/15 6:14:31 AM | DOGE | DOWN | 28 sec | +0.034% | 0¢ | ❌ Lost | $0.00 |
| 11/15 6:14:10 AM | BTC | DOWN | 49 sec | +0.076% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 6:14:00 AM | HYPE | UP | 60 sec | -0.295% | 0¢ | ❌ Lost | $0.00 |
| 11/15 6:13:50 AM | SOL | DOWN | 70 sec | +0.174% | 0¢ | ❌ Lost | $0.00 |
| 11/15 6:13:30 AM | ZEC | UP | 1.5 min | -0.475% | 0¢ | ❌ Lost | $0.00 |
| 11/15 6:13:14 AM | NEAR | UP | 1.8 min | -0.544% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
