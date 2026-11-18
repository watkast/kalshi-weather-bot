# 15-Minute 1¢ Study

*Updated Wed Nov 18, 4:37 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4510 finished bets | 1% | $216.00 | +43% | +4.79¢ | $81.15 / $134.85 |

*Expect about **88 buys a day** (~$13.21/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4247 | $116.05 | +25% |
| Volatility model ≥ 2%, hold to the close | 8413 | $80.10 | +8% |
| Momentum model ≥ 2%, hold to the close | 6981 | -$3.00 | -0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 60666 | 60632 | 237 (0%) | 1.07% | -$4,061.85 (-55%) | Hold to the close: -$4,061.85 (-55%) |

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
| Volatility model | 36265 | 4.5% | 0.4% (154) | -623% | ❌ Worse |
| Momentum model | 36265 | 4.4% | 0.4% (154) | -649% | ❌ Worse |
| Mean-reversion model | 36265 | 7.9% | 0.4% (154) | -758% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 36265 | 154 | -45% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8413 | 78 | +8% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4510 | 51 | +43% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 2592 | 30 | +68% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6981 | 57 | -0% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4247 | 41 | +25% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2766 | 26 | +34% | -67% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14862 | 108 | -20% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10338 | 89 | -5% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6867 | 64 | +6% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 36471 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14446 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9715 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 60632 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 237 | 0% | -$4,061.85 | -55% | — |
| Sell at 2¢ | 2449 | 4% | -$6,449.11 | -87% | 47 sec |
| Sell at 3¢ | 1656 | 3% | -$6,440.01 | -87% | 48 sec |
| Sell at 5¢ | 1132 | 2% | -$6,322.05 | -86% | 63 sec |
| Sell at 10¢ | 690 | 1% | -$6,069.95 | -82% | 65 sec |
| Sell at 25¢ | 369 | 1% | -$5,612.46 | -76% | 80 sec |
| Sell at 50¢ | 244 | 0% | -$5,060.85 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3076 | 17 | 11% | 4% | -48% | -81% | -82% |
| 2–5 min | 19657 | 108 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 15194 | 51 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 22692 | 61 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4078 | 19 | 5% | 3% | -39% | -88% | -87% |
| SOL | 4076 | 19 | 4% | 2% | -40% | -86% | -86% |
| HYPE | 4069 | 12 | 4% | 2% | -63% | -89% | -88% |
| DOGE | 4058 | 11 | 4% | 2% | -66% | -90% | -89% |
| BNB | 4058 | 21 | 5% | 2% | -34% | -85% | -85% |
| ETH | 4051 | 19 | 7% | 3% | -41% | -82% | -82% |
| BTC | 4033 | 21 | 5% | 2% | -29% | -86% | -88% |
| NEAR | 4032 | 18 | 5% | 2% | -42% | -85% | -86% |
| XRP | 4016 | 16 | 3% | 2% | -50% | -89% | -88% |
| GOLD | 2159 | 6 | 5% | 2% | -66% | -82% | -84% |
| WTI | 2141 | 7 | 4% | 1% | -60% | -91% | -92% |
| SILVER | 2096 | 9 | 5% | 2% | -49% | -83% | -83% |
| PLATINUM | 1908 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1861 | 7 | 2% | 1% | -65% | -91% | -90% |
| COPPER | 1796 | 6 | 2% | 1% | -69% | -76% | -76% |
| GBPUSD | 1787 | 6 | 2% | 1% | -69% | -96% | -96% |
| NATGAS | 1760 | 10 | 2% | 1% | -47% | -75% | -75% |
| USDJPY | 1749 | 6 | 2% | 1% | -68% | -97% | -96% |
| PALLADIUM | 1715 | 4 | 1% | 0% | -78% | -93% | -93% |
| AUDUSD | 1301 | 6 | 2% | 1% | -57% | -89% | -89% |
| USDCAD | 1244 | 1 | 3% | 1% | -92% | -95% | -96% |
| BRENT | 871 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 447 | 2 | 3% | 1% | -58% | -73% | -72% |
| 2YRRATE | 428 | 4 | 4% | 2% | -13% | -50% | -48% |
| 30YRRATE | 415 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 402 | 2 | 4% | 1% | -54% | -94% | -95% |
| INX | 81 | 1 | 2% | 1% | +15% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 30905 | 121 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 29727 | 116 | 4% | 2% | -55% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5483 | 25 | 2% | 1% | -18% | -78% | -77% |
| 0.05–0.1% | 5930 | 24 | 3% | 2% | -37% | -91% | -91% |
| 0.1–0.2% | 9136 | 34 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 11318 | 50 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 4595 | 23 | 7% | 3% | -48% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14845 | 45 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 14416 | 78 | 5% | 2% | -38% | -85% | -84% |
| Afternoon (12–6pm) | 14813 | 65 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 16558 | 49 | 4% | 2% | -66% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,054 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/18 4:29:53 AM | 5YRRATE | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 4:29:37 AM | NATGAS | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 4:29:37 AM | 10YRRATE | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 4:29:21 AM | ETH | DOWN | 38 sec | +0.045% | 0¢ | ❌ Lost | $0.00 |
| 11/18 4:29:05 AM | 30YRRATE | UP | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 4:29:05 AM | BTC | DOWN | 55 sec | +0.046% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 4:29:05 AM | GBPUSD | UP | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 4:28:31 AM | GOLD | DOWN | 89 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/18 4:28:31 AM | PLATINUM | DOWN | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 4:28:31 AM | SILVER | DOWN | 89 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/18 4:28:15 AM | SOL | DOWN | 1.8 min | +0.205% | 0¢ | ❌ Lost | $0.00 |
| 11/18 4:28:00 AM | ZEC | DOWN | 2.0 min | +0.407% | 0¢ | ❌ Lost | -$0.15 |
| 11/18 4:28:00 AM | DOGE | DOWN | 2.0 min | +0.140% | 0¢ | ❌ Lost | -$0.15 |
| 11/18 4:27:11 AM | USDJPY | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 4:27:11 AM | HYPE | DOWN | 2.8 min | +0.256% | 0¢ | ❌ Lost | -$0.15 |
| 11/18 4:27:11 AM | BNB | DOWN | 2.8 min | +0.129% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 4:26:55 AM | PALLADIUM | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 4:26:37 AM | XRP | UP | 3.4 min | -0.374% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 4:25:50 AM | NEAR | DOWN | 4.2 min | +0.440% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 4:14:22 AM | EURUSD | UP | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 4:14:06 AM | USDCAD | DOWN | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 4:13:18 AM | AUDUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 4:13:18 AM | PALLADIUM | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 4:11:11 AM | BRENT | DOWN | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 4:11:11 AM | COPPER | UP | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 4:10:55 AM | SILVER | UP | 4.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/18 4:10:07 AM | NEAR | UP | 4.9 min | -0.599% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 4:10:07 AM | BTC | UP | 4.9 min | -0.267% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 4:09:51 AM | WTI | DOWN | 5.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/18 4:09:51 AM | PLATINUM | UP | 5.2 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
