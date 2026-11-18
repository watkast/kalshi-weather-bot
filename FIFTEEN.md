# 15-Minute 1¢ Study

*Updated Wed Nov 18, 3:36 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4507 finished bets | 1% | $216.15 | +43% | +4.80¢ | $81.45 / $134.70 |

*Expect about **88 buys a day** (~$13.22/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4245 | $116.20 | +25% |
| Volatility model ≥ 2%, hold to the close | 8406 | $80.85 | +8% |
| Momentum model ≥ 2%, hold to the close | 6978 | -$2.70 | -0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 60590 | 60556 | 237 (0%) | 1.07% | -$4,053.00 (-55%) | Hold to the close: -$4,053.00 (-55%) |

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
| Volatility model | 36230 | 4.5% | 0.4% (154) | -623% | ❌ Worse |
| Momentum model | 36230 | 4.4% | 0.4% (154) | -649% | ❌ Worse |
| Mean-reversion model | 36230 | 7.9% | 0.4% (154) | -757% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 36230 | 154 | -45% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8406 | 78 | +8% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4507 | 51 | +43% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2590 | 30 | +68% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6978 | 57 | -0% | -79% | -78% | -74% |
| Momentum model ≥ 5% | 4245 | 41 | +25% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2765 | 26 | +34% | -67% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14846 | 108 | -20% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10326 | 89 | -4% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6860 | 64 | +6% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 36436 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14422 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9698 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 60556 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 237 | 0% | -$4,053.00 | -55% | — |
| Sell at 2¢ | 2446 | 4% | -$6,441.04 | -87% | 47 sec |
| Sell at 3¢ | 1653 | 3% | -$6,432.33 | -87% | 48 sec |
| Sell at 5¢ | 1129 | 2% | -$6,315.15 | -86% | 63 sec |
| Sell at 10¢ | 688 | 1% | -$6,063.72 | -82% | 65 sec |
| Sell at 25¢ | 368 | 1% | -$5,606.92 | -76% | 80 sec |
| Sell at 50¢ | 244 | 0% | -$5,052.00 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3064 | 17 | 11% | 4% | -47% | -81% | -82% |
| 2–5 min | 19639 | 108 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 15175 | 51 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 22665 | 61 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4074 | 19 | 5% | 3% | -39% | -88% | -87% |
| SOL | 4072 | 19 | 4% | 2% | -40% | -86% | -86% |
| HYPE | 4065 | 12 | 5% | 2% | -63% | -89% | -88% |
| DOGE | 4055 | 11 | 4% | 2% | -66% | -90% | -89% |
| BNB | 4054 | 21 | 5% | 2% | -34% | -85% | -85% |
| ETH | 4047 | 19 | 7% | 3% | -41% | -82% | -82% |
| BTC | 4029 | 21 | 5% | 2% | -29% | -86% | -88% |
| NEAR | 4028 | 18 | 5% | 2% | -42% | -85% | -86% |
| XRP | 4012 | 16 | 3% | 2% | -50% | -89% | -88% |
| GOLD | 2156 | 6 | 5% | 2% | -66% | -82% | -84% |
| WTI | 2138 | 7 | 4% | 1% | -60% | -91% | -92% |
| SILVER | 2092 | 9 | 5% | 2% | -49% | -83% | -83% |
| PLATINUM | 1905 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1859 | 7 | 2% | 1% | -65% | -91% | -90% |
| COPPER | 1793 | 6 | 2% | 1% | -69% | -76% | -76% |
| GBPUSD | 1786 | 6 | 2% | 1% | -69% | -96% | -96% |
| NATGAS | 1757 | 10 | 2% | 1% | -47% | -75% | -75% |
| USDJPY | 1746 | 6 | 2% | 1% | -68% | -97% | -96% |
| PALLADIUM | 1712 | 4 | 1% | 0% | -78% | -93% | -93% |
| AUDUSD | 1299 | 6 | 2% | 1% | -57% | -89% | -89% |
| USDCAD | 1242 | 1 | 3% | 1% | -92% | -95% | -96% |
| BRENT | 869 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 445 | 2 | 3% | 1% | -58% | -73% | -71% |
| 2YRRATE | 427 | 4 | 4% | 2% | -13% | -50% | -48% |
| 30YRRATE | 413 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 400 | 2 | 4% | 2% | -53% | -94% | -95% |
| INX | 81 | 1 | 2% | 1% | +15% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 30871 | 121 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 29685 | 116 | 4% | 2% | -55% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5475 | 25 | 2% | 1% | -18% | -78% | -77% |
| 0.05–0.1% | 5926 | 24 | 3% | 2% | -37% | -91% | -91% |
| 0.1–0.2% | 9132 | 34 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 11303 | 50 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 4591 | 23 | 7% | 3% | -48% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14769 | 45 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 14416 | 78 | 5% | 2% | -38% | -85% | -84% |
| Afternoon (12–6pm) | 14813 | 65 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 16558 | 49 | 4% | 2% | -66% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,056 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/18 3:29:50 AM | USDJPY | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 3:29:34 AM | NEAR | UP | 26 sec | -0.157% | 0¢ | ❌ Lost | $0.00 |
| 11/18 3:29:34 AM | NATGAS | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 3:29:34 AM | GBPUSD | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 3:29:03 AM | HYPE | UP | 56 sec | -0.189% | 0¢ | ❌ Lost | $0.00 |
| 11/18 3:28:29 AM | 30YRRATE | UP | 1.5 min | — | 3¢ | ❌ Lost | -$0.15 |
| 11/18 3:28:29 AM | BRENT | UP | 1.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/18 3:28:13 AM | 2YRRATE | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 3:27:59 AM | 5YRRATE | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 3:27:43 AM | EURUSD | UP | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/18 3:27:43 AM | WTI | UP | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/18 3:27:11 AM | GOLD | UP | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/18 3:26:55 AM | SILVER | UP | 3.1 min | — | 15¢ | ❌ Lost | -$0.15 |
| 11/18 3:26:22 AM | DOGE | UP | 3.6 min | -0.259% | 0¢ | ❌ Lost | -$0.15 |
| 11/18 3:25:18 AM | ETH | UP | 4.7 min | -0.268% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 3:25:18 AM | SOL | UP | 4.7 min | -0.356% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 3:25:02 AM | BTC | UP | 5.0 min | -0.236% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 3:25:02 AM | PLATINUM | UP | 5.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 3:24:30 AM | BNB | UP | 5.5 min | -0.261% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 3:24:30 AM | ZEC | UP | 5.5 min | -0.880% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 3:24:30 AM | XRP | UP | 5.5 min | -0.459% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 3:22:37 AM | 10YRRATE | UP | 7.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/18 3:14:57 AM | 2YRRATE | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 3:14:57 AM | 5YRRATE | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 3:14:25 AM | BTC | UP | 35 sec | -0.060% | 0¢ | ❌ Lost | $0.00 |
| 11/18 3:13:38 AM | PLATINUM | UP | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 3:13:38 AM | DOGE | UP | 81 sec | -0.146% | 3¢ | ❌ Lost | -$0.15 |
| 11/18 3:13:38 AM | HYPE | UP | 81 sec | -0.217% | 0¢ | ❌ Lost | $0.00 |
| 11/18 3:13:22 AM | BNB | UP | 1.6 min | -0.162% | 0¢ | ❌ Lost | $0.00 |
| 11/18 3:13:22 AM | 10YRRATE | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
