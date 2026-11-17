# 15-Minute 1¢ Study

*Updated Tue Nov 17, 3:30 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4479 finished bets | 1% | $219.15 | +44% | +4.89¢ | $82.95 / $136.20 |

*Expect about **88 buys a day** (~$13.27/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4217 | $119.35 | +26% |
| Volatility model ≥ 2%, hold to the close | 8352 | $87.60 | +9% |
| Momentum model ≥ 2%, hold to the close | 6924 | $4.20 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 59959 | 59918 | 235 (0%) | 1.07% | -$4,001.20 (-55%) | Hold to the close: -$4,001.20 (-55%) |

*In play or awaiting result: 13. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 35929 | 4.5% | 0.4% (154) | -622% | ❌ Worse |
| Momentum model | 35929 | 4.4% | 0.4% (154) | -647% | ❌ Worse |
| Mean-reversion model | 35929 | 7.9% | 0.4% (154) | -754% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 35929 | 154 | -45% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8352 | 78 | +9% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4479 | 51 | +44% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2572 | 30 | +69% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6924 | 57 | +1% | -79% | -78% | -74% |
| Momentum model ≥ 5% | 4217 | 41 | +26% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2748 | 26 | +34% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14728 | 108 | -20% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10252 | 89 | -4% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6808 | 64 | +7% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 36135 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14234 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9549 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 59918 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 235 | 0% | -$4,001.20 | -55% | — |
| Sell at 2¢ | 2419 | 4% | -$6,368.26 | -87% | 47 sec |
| Sell at 3¢ | 1632 | 3% | -$6,360.72 | -87% | 48 sec |
| Sell at 5¢ | 1119 | 2% | -$6,241.85 | -86% | 63 sec |
| Sell at 10¢ | 682 | 1% | -$5,991.78 | -82% | 65 sec |
| Sell at 25¢ | 365 | 1% | -$5,551.05 | -76% | 80 sec |
| Sell at 50¢ | 242 | 0% | -$4,999.70 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3022 | 17 | 11% | 4% | -47% | -81% | -83% |
| 2–5 min | 19421 | 107 | 7% | 3% | -46% | -86% | -87% |
| 1–2 min | 15034 | 51 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 22428 | 60 | 1% | 0% | -62% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4041 | 19 | 5% | 3% | -38% | -88% | -87% |
| SOL | 4040 | 19 | 4% | 2% | -40% | -86% | -86% |
| HYPE | 4031 | 12 | 5% | 2% | -62% | -89% | -88% |
| DOGE | 4021 | 11 | 4% | 2% | -65% | -90% | -89% |
| BNB | 4020 | 21 | 5% | 2% | -34% | -85% | -85% |
| ETH | 4014 | 19 | 7% | 3% | -41% | -82% | -82% |
| NEAR | 3995 | 18 | 5% | 2% | -41% | -85% | -86% |
| BTC | 3994 | 21 | 5% | 2% | -29% | -86% | -88% |
| XRP | 3979 | 16 | 3% | 2% | -49% | -89% | -88% |
| GOLD | 2131 | 5 | 5% | 2% | -71% | -83% | -84% |
| WTI | 2109 | 7 | 4% | 1% | -60% | -91% | -92% |
| SILVER | 2068 | 9 | 5% | 2% | -48% | -83% | -83% |
| PLATINUM | 1884 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1835 | 6 | 2% | 1% | -69% | -91% | -90% |
| COPPER | 1766 | 6 | 2% | 1% | -68% | -76% | -76% |
| GBPUSD | 1762 | 6 | 2% | 1% | -68% | -96% | -96% |
| NATGAS | 1741 | 10 | 2% | 1% | -46% | -75% | -75% |
| USDJPY | 1721 | 6 | 2% | 1% | -67% | -96% | -96% |
| PALLADIUM | 1695 | 4 | 1% | 0% | -78% | -93% | -93% |
| AUDUSD | 1276 | 6 | 2% | 1% | -56% | -89% | -89% |
| USDCAD | 1225 | 1 | 3% | 1% | -92% | -95% | -96% |
| BRENT | 840 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 435 | 2 | 3% | 1% | -57% | -73% | -71% |
| 2YRRATE | 420 | 4 | 4% | 2% | -11% | -49% | -48% |
| 30YRRATE | 403 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 391 | 2 | 4% | 2% | -52% | -93% | -95% |
| INX | 81 | 1 | 2% | 1% | +15% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 30501 | 121 | 4% | 2% | -54% | -88% | -88% |
| DOWN (bought NO) | 29417 | 114 | 4% | 2% | -55% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5444 | 25 | 2% | 1% | -17% | -78% | -77% |
| 0.05–0.1% | 5895 | 24 | 3% | 2% | -37% | -91% | -91% |
| 0.1–0.2% | 9054 | 34 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 11180 | 50 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 4553 | 23 | 7% | 3% | -47% | -86% | -86% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14507 | 45 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 14416 | 78 | 5% | 2% | -38% | -85% | -84% |
| Afternoon (12–6pm) | 14635 | 63 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 16360 | 49 | 4% | 2% | -66% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,061 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/17 3:29:53 PM | XRP | DOWN | 6 sec | +0.103% | 0¢ | ❌ Lost | $0.00 |
| 11/17 3:29:35 PM | BRENT | DOWN | 24 sec | — | 0¢ | In play | — |
| 11/17 3:29:03 PM | AUDUSD | DOWN | 57 sec | — | 0¢ | In play | — |
| 11/17 3:29:03 PM | NEAR | DOWN | 57 sec | +0.172% | 0¢ | ❌ Lost | -$0.15 |
| 11/17 3:28:47 PM | ETH | DOWN | 72 sec | +0.167% | 0¢ | In play | — |
| 11/17 3:28:31 PM | DOGE | DOWN | 88 sec | +0.175% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 3:28:31 PM | BNB | DOWN | 88 sec | +0.118% | 0¢ | In play | — |
| 11/17 3:28:31 PM | SOL | DOWN | 88 sec | +0.222% | 0¢ | ❌ Lost | $0.00 |
| 11/17 3:28:00 PM | HYPE | DOWN | 2.0 min | +0.245% | 1¢ | In play | — |
| 11/17 3:28:00 PM | BTC | DOWN | 2.0 min | +0.159% | 1¢ | In play | — |
| 11/17 3:26:08 PM | ZEC | DOWN | 3.9 min | +0.626% | 1¢ | In play | — |
| 11/17 11:44:45 AM | NATGAS | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 11:44:13 AM | GBPUSD | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 11:43:55 AM | BRENT | UP | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 11:43:55 AM | 30YRRATE | UP | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 11:43:39 AM | 2YRRATE | UP | 80 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 11:43:39 AM | WTI | UP | 80 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/17 11:43:09 AM | 10YRRATE | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 11:43:09 AM | COPPER | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 11:43:09 AM | 5YRRATE | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 11:43:09 AM | SILVER | UP | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/17 11:42:37 AM | EURUSD | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 11:42:21 AM | USDCAD | DOWN | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/17 11:41:34 AM | GOLD | UP | 3.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/17 11:41:34 AM | AUDUSD | UP | 3.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 11:40:46 AM | NEAR | UP | 4.2 min | -0.798% | 0¢ | ❌ Lost | -$0.15 |
| 11/17 11:40:46 AM | INX | UP | 4.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 11:40:46 AM | SOL | UP | 4.2 min | -0.579% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 11:40:30 AM | BNB | UP | 4.5 min | -0.357% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 11:40:30 AM | BTC | UP | 4.5 min | -0.376% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
