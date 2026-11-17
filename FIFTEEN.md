# 15-Minute 1¢ Study

*Updated Tue Nov 17, 10:16 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4473 finished bets | 1% | $219.90 | +45% | +4.92¢ | $83.40 / $136.50 |

*Expect about **89 buys a day** (~$13.30/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4212 | $119.65 | +26% |
| Volatility model ≥ 2%, hold to the close | 8337 | $89.40 | +9% |
| Momentum model ≥ 2%, hold to the close | 6913 | $5.40 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 59823 | 59789 | 235 (0%) | 1.07% | -$3,985.15 (-55%) | Hold to the close: -$3,985.15 (-55%) |

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
| Volatility model | 35873 | 4.5% | 0.4% (154) | -622% | ❌ Worse |
| Momentum model | 35873 | 4.4% | 0.4% (154) | -648% | ❌ Worse |
| Mean-reversion model | 35873 | 7.9% | 0.4% (154) | -755% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 35873 | 154 | -45% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8337 | 78 | +9% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4473 | 51 | +45% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2571 | 30 | +69% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6913 | 57 | +1% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4212 | 41 | +26% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2744 | 26 | +35% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14703 | 108 | -19% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10234 | 89 | -4% | -79% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6799 | 64 | +7% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 36079 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14198 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9512 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 59789 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 235 | 0% | -$3,985.15 | -55% | — |
| Sell at 2¢ | 2418 | 4% | -$6,352.47 | -87% | 47 sec |
| Sell at 3¢ | 1631 | 3% | -$6,345.06 | -87% | 48 sec |
| Sell at 5¢ | 1118 | 2% | -$6,226.45 | -86% | 63 sec |
| Sell at 10¢ | 681 | 1% | -$5,977.04 | -82% | 65 sec |
| Sell at 25¢ | 365 | 1% | -$5,535.00 | -76% | 80 sec |
| Sell at 50¢ | 242 | 0% | -$4,983.65 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3018 | 17 | 11% | 4% | -47% | -81% | -82% |
| 2–5 min | 19372 | 107 | 7% | 3% | -46% | -86% | -86% |
| 1–2 min | 15006 | 51 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 22380 | 60 | 1% | 0% | -62% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4035 | 19 | 5% | 3% | -38% | -88% | -87% |
| SOL | 4034 | 19 | 4% | 2% | -40% | -86% | -86% |
| HYPE | 4025 | 12 | 5% | 2% | -62% | -89% | -88% |
| BNB | 4015 | 21 | 5% | 2% | -34% | -85% | -85% |
| DOGE | 4014 | 11 | 4% | 2% | -65% | -90% | -89% |
| ETH | 4008 | 19 | 7% | 3% | -41% | -82% | -82% |
| NEAR | 3988 | 18 | 5% | 2% | -41% | -85% | -86% |
| BTC | 3988 | 21 | 5% | 2% | -29% | -86% | -88% |
| XRP | 3972 | 16 | 3% | 2% | -49% | -89% | -88% |
| GOLD | 2126 | 5 | 5% | 2% | -71% | -83% | -84% |
| WTI | 2104 | 7 | 4% | 1% | -60% | -91% | -92% |
| SILVER | 2063 | 9 | 5% | 2% | -48% | -83% | -83% |
| PLATINUM | 1880 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1832 | 6 | 2% | 1% | -69% | -91% | -90% |
| COPPER | 1761 | 6 | 2% | 1% | -68% | -76% | -76% |
| GBPUSD | 1757 | 6 | 2% | 1% | -68% | -96% | -96% |
| NATGAS | 1736 | 10 | 2% | 1% | -46% | -75% | -74% |
| USDJPY | 1719 | 6 | 2% | 1% | -67% | -96% | -96% |
| PALLADIUM | 1692 | 4 | 1% | 0% | -78% | -93% | -93% |
| AUDUSD | 1272 | 6 | 2% | 1% | -56% | -89% | -89% |
| USDCAD | 1221 | 1 | 3% | 1% | -92% | -95% | -96% |
| BRENT | 836 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 432 | 2 | 3% | 1% | -57% | -72% | -71% |
| 2YRRATE | 417 | 4 | 4% | 2% | -10% | -49% | -48% |
| 30YRRATE | 400 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 387 | 2 | 4% | 2% | -52% | -93% | -95% |
| INX | 75 | 1 | 3% | 1% | +24% | -95% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 30427 | 121 | 4% | 2% | -54% | -88% | -88% |
| DOWN (bought NO) | 29362 | 114 | 4% | 2% | -55% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5440 | 25 | 2% | 1% | -17% | -78% | -77% |
| 0.05–0.1% | 5888 | 24 | 3% | 2% | -37% | -91% | -91% |
| 0.1–0.2% | 9046 | 34 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 11158 | 50 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 4538 | 23 | 7% | 3% | -47% | -86% | -86% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14507 | 45 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 14291 | 78 | 5% | 2% | -38% | -85% | -84% |
| Afternoon (12–6pm) | 14631 | 63 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 16360 | 49 | 4% | 2% | -66% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,066 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/17 10:14:57 AM | USDJPY | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 10:14:41 AM | 10YRRATE | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 10:14:41 AM | EURUSD | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 10:14:25 AM | GBPUSD | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 10:14:25 AM | 30YRRATE | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 10:14:09 AM | USDCAD | DOWN | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 10:13:36 AM | PLATINUM | DOWN | 84 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 10:13:36 AM | ETH | DOWN | 84 sec | +0.375% | 0¢ | ❌ Lost | $0.00 |
| 11/17 10:13:36 AM | INX | DOWN | 84 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 10:13:36 AM | XRP | DOWN | 84 sec | +0.230% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 10:13:36 AM | BTC | DOWN | 84 sec | +0.202% | 0¢ | ❌ Lost | $0.00 |
| 11/17 10:13:36 AM | ZEC | DOWN | 84 sec | +0.498% | 0¢ | ❌ Lost | $0.00 |
| 11/17 10:13:36 AM | SILVER | DOWN | 84 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/17 10:13:20 AM | BRENT | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 10:13:20 AM | GOLD | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/17 10:12:34 AM | DOGE | DOWN | 2.4 min | +0.503% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 10:12:34 AM | BNB | DOWN | 2.4 min | +0.311% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 10:12:18 AM | WTI | UP | 2.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/17 10:11:30 AM | PALLADIUM | DOWN | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 10:11:14 AM | SOL | DOWN | 3.8 min | +0.801% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 10:11:14 AM | NEAR | DOWN | 3.8 min | +1.236% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 10:10:58 AM | HYPE | DOWN | 4.0 min | +0.899% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 9:59:49 AM | USDJPY | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 9:59:49 AM | GBPUSD | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 9:59:49 AM | ETH | DOWN | 10 sec | -0.034% | 0¢ | ❌ Lost | $0.00 |
| 11/17 9:59:49 AM | INX | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 9:59:33 AM | 10YRRATE | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 9:59:33 AM | GOLD | UP | 26 sec | — | 1¢ | ❌ Lost | $0.00 |
| 11/17 9:59:33 AM | NEAR | DOWN | 26 sec | +0.165% | 0¢ | ❌ Lost | $0.00 |
| 11/17 9:59:33 AM | ZEC | UP | 26 sec | -0.267% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
