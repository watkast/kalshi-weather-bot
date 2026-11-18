# 15-Minute 1¢ Study

*Updated Wed Nov 18, 5:18 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4515 finished bets | 1% | $216.00 | +43% | +4.78¢ | $80.85 / $135.15 |

*Expect about **88 buys a day** (~$13.22/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4252 | $116.05 | +25% |
| Volatility model ≥ 2%, hold to the close | 8421 | $79.80 | +8% |
| Momentum model ≥ 2%, hold to the close | 6987 | -$3.15 | -0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 60733 | 60699 | 237 (0%) | 1.07% | -$4,069.05 (-55%) | Hold to the close: -$4,069.05 (-55%) |

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
| Volatility model | 36290 | 4.5% | 0.4% (154) | -626% | ❌ Worse |
| Momentum model | 36290 | 4.4% | 0.4% (154) | -652% | ❌ Worse |
| Mean-reversion model | 36290 | 7.9% | 0.4% (154) | -761% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 36290 | 154 | -45% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8421 | 78 | +8% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4515 | 51 | +43% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 2597 | 30 | +68% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6987 | 57 | -0% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4252 | 41 | +25% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2771 | 26 | +34% | -67% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14871 | 108 | -20% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10345 | 89 | -5% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6873 | 64 | +6% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 36496 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14464 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9739 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 60699 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 237 | 0% | -$4,069.05 | -55% | — |
| Sell at 2¢ | 2452 | 4% | -$6,455.53 | -87% | 47 sec |
| Sell at 3¢ | 1657 | 3% | -$6,446.82 | -87% | 48 sec |
| Sell at 5¢ | 1132 | 2% | -$6,329.25 | -86% | 63 sec |
| Sell at 10¢ | 690 | 1% | -$6,077.15 | -82% | 65 sec |
| Sell at 25¢ | 369 | 1% | -$5,619.66 | -76% | 80 sec |
| Sell at 50¢ | 244 | 0% | -$5,068.05 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3082 | 17 | 11% | 4% | -48% | -81% | -82% |
| 2–5 min | 19675 | 108 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 15208 | 51 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 22721 | 61 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4081 | 19 | 5% | 2% | -39% | -88% | -87% |
| SOL | 4079 | 19 | 4% | 2% | -40% | -86% | -86% |
| HYPE | 4072 | 12 | 4% | 2% | -63% | -89% | -88% |
| DOGE | 4061 | 11 | 4% | 2% | -66% | -90% | -89% |
| BNB | 4061 | 21 | 5% | 2% | -34% | -85% | -85% |
| ETH | 4053 | 19 | 7% | 3% | -41% | -82% | -82% |
| NEAR | 4035 | 18 | 5% | 2% | -42% | -85% | -86% |
| BTC | 4035 | 21 | 5% | 2% | -29% | -86% | -88% |
| XRP | 4019 | 16 | 3% | 2% | -50% | -89% | -88% |
| GOLD | 2162 | 6 | 5% | 2% | -66% | -82% | -84% |
| WTI | 2142 | 7 | 4% | 1% | -60% | -91% | -92% |
| SILVER | 2099 | 9 | 5% | 2% | -49% | -83% | -83% |
| PLATINUM | 1911 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1864 | 7 | 2% | 1% | -65% | -91% | -90% |
| COPPER | 1798 | 6 | 2% | 1% | -69% | -76% | -76% |
| GBPUSD | 1790 | 6 | 2% | 1% | -69% | -96% | -96% |
| NATGAS | 1763 | 10 | 2% | 1% | -47% | -75% | -75% |
| USDJPY | 1752 | 6 | 2% | 1% | -68% | -97% | -96% |
| PALLADIUM | 1717 | 4 | 1% | 0% | -78% | -93% | -93% |
| AUDUSD | 1302 | 6 | 2% | 1% | -57% | -89% | -89% |
| USDCAD | 1247 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 872 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 450 | 2 | 3% | 1% | -59% | -73% | -72% |
| 2YRRATE | 431 | 4 | 4% | 2% | -13% | -50% | -49% |
| 30YRRATE | 417 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 405 | 2 | 4% | 1% | -54% | -94% | -96% |
| INX | 81 | 1 | 2% | 1% | +15% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 30934 | 121 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 29765 | 116 | 4% | 2% | -55% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5489 | 25 | 2% | 1% | -18% | -78% | -77% |
| 0.05–0.1% | 5939 | 24 | 3% | 2% | -37% | -91% | -91% |
| 0.1–0.2% | 9142 | 34 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 11322 | 50 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 4595 | 23 | 7% | 3% | -48% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14912 | 45 | 4% | 2% | -66% | -88% | -88% |
| Morning (6am–12pm) | 14416 | 78 | 5% | 2% | -38% | -85% | -84% |
| Afternoon (12–6pm) | 14813 | 65 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 16558 | 49 | 4% | 2% | -66% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,045 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/18 5:14:46 AM | USDJPY | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 5:14:46 AM | HYPE | DOWN | 14 sec | -0.012% | 0¢ | ❌ Lost | $0.00 |
| 11/18 5:14:46 AM | BNB | DOWN | 14 sec | -0.049% | 0¢ | ❌ Lost | $0.00 |
| 11/18 5:14:30 AM | NEAR | UP | 30 sec | -0.224% | 0¢ | ❌ Lost | $0.00 |
| 11/18 5:14:30 AM | DOGE | DOWN | 30 sec | +0.088% | 0¢ | ❌ Lost | $0.00 |
| 11/18 5:14:30 AM | COPPER | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 5:14:15 AM | SOL | DOWN | 44 sec | +0.144% | 0¢ | ❌ Lost | $0.00 |
| 11/18 5:13:59 AM | ZEC | UP | 60 sec | -0.230% | 0¢ | ❌ Lost | $0.00 |
| 11/18 5:13:59 AM | PALLADIUM | DOWN | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 5:13:59 AM | PLATINUM | DOWN | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 5:13:43 AM | USDCAD | UP | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 5:13:27 AM | EURUSD | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 5:12:39 AM | 10YRRATE | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 5:12:23 AM | NATGAS | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 5:12:23 AM | 5YRRATE | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 5:12:23 AM | 2YRRATE | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 5:11:48 AM | XRP | UP | 3.2 min | -0.274% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 5:10:46 AM | AUDUSD | DOWN | 4.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 5:10:30 AM | SILVER | DOWN | 4.5 min | — | 2¢ | ❌ Lost | -$0.15 |
| 11/18 5:10:30 AM | GBPUSD | DOWN | 4.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/18 5:09:10 AM | GOLD | DOWN | 5.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/18 4:59:55 AM | PALLADIUM | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 4:59:55 AM | SOL | UP | 5 sec | -0.086% | 0¢ | ❌ Lost | $0.00 |
| 11/18 4:59:55 AM | GOLD | DOWN | 5 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/18 4:59:55 AM | EURUSD | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 4:59:39 AM | HYPE | UP | 21 sec | -0.086% | 0¢ | ❌ Lost | -$0.15 |
| 11/18 4:59:39 AM | BNB | DOWN | 21 sec | -0.027% | 0¢ | ❌ Lost | $0.00 |
| 11/18 4:59:23 AM | XRP | UP | 37 sec | -0.081% | 0¢ | ❌ Lost | $0.00 |
| 11/18 4:59:23 AM | NEAR | DOWN | 37 sec | +0.039% | 0¢ | ❌ Lost | $0.00 |
| 11/18 4:59:23 AM | BTC | DOWN | 37 sec | +0.055% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
