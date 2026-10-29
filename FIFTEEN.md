# 15-Minute 1¢ Study

*Updated Thu Oct 29, 12:24 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3090 finished bets | 1% | $87.50 | +25% | +2.83¢ | $80.85 / $6.65 |

*Expect about **98 buys a day** (~$14.72/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2865 | $36.50 | +12% |
| Volatility model ≥ 2%, hold to the close | 5723 | $5.05 | +1% |
| Volatility model ≥ 5%, sell at 50¢ | 3090 | -$66.75 | -19% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 38170 | 38160 | 141 (0%) | 1.07% | -$2,684.55 (-58%) | Hold to the close: -$2,684.55 (-58%) |

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
| Volatility model | 23545 | 4.7% | 0.4% (93) | -679% | ❌ Worse |
| Momentum model | 23545 | 4.6% | 0.4% (93) | -702% | ❌ Worse |
| Mean-reversion model | 23545 | 8.0% | 0.4% (93) | -826% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 23545 | 93 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5723 | 50 | +1% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 3090 | 31 | +25% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1750 | 19 | +54% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4729 | 34 | -13% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2865 | 25 | +12% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1874 | 17 | +26% | -72% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9627 | 64 | -27% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6749 | 54 | -12% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4506 | 39 | -2% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 23745 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9162 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5253 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 38160 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 141 | 0% | -$2,684.55 | -58% | — |
| Sell at 2¢ | 1453 | 4% | -$4,084.77 | -88% | 47 sec |
| Sell at 3¢ | 1001 | 3% | -$4,072.16 | -87% | 48 sec |
| Sell at 5¢ | 697 | 2% | -$4,009.50 | -86% | 63 sec |
| Sell at 10¢ | 421 | 1% | -$3,855.04 | -83% | 65 sec |
| Sell at 25¢ | 224 | 1% | -$3,553.11 | -76% | 82 sec |
| Sell at 50¢ | 146 | 0% | -$3,225.05 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 8 | 0 | 38% | 25% | -100% | -35% | -3% |
| 5–10 min | 1748 | 8 | 11% | 4% | -56% | -80% | -81% |
| 2–5 min | 12155 | 68 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 9669 | 32 | 3% | 1% | -64% | -92% | -92% |
| Under 1 min | 14580 | 33 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2657 | 12 | 5% | 2% | -42% | -88% | -88% |
| HYPE | 2652 | 8 | 5% | 3% | -63% | -89% | -87% |
| BNB | 2651 | 15 | 4% | 2% | -29% | -85% | -84% |
| SOL | 2644 | 7 | 4% | 2% | -67% | -92% | -91% |
| DOGE | 2639 | 6 | 4% | 2% | -72% | -90% | -90% |
| ETH | 2638 | 11 | 6% | 3% | -49% | -85% | -85% |
| XRP | 2623 | 11 | 3% | 1% | -48% | -89% | -89% |
| BTC | 2621 | 13 | 5% | 2% | -34% | -88% | -89% |
| NEAR | 2620 | 12 | 5% | 2% | -40% | -82% | -82% |
| GOLD | 1440 | 5 | 4% | 2% | -58% | -82% | -83% |
| SILVER | 1410 | 6 | 4% | 2% | -50% | -82% | -81% |
| WTI | 1394 | 4 | 3% | 1% | -66% | -93% | -94% |
| PLATINUM | 1246 | 2 | 2% | 1% | -85% | -97% | -96% |
| COPPER | 1189 | 4 | 1% | 1% | -69% | -74% | -74% |
| EURUSD | 1183 | 3 | 2% | 1% | -76% | -88% | -88% |
| NATGAS | 1150 | 7 | 2% | 1% | -43% | -80% | -79% |
| GBPUSD | 1122 | 2 | 2% | 1% | -83% | -96% | -96% |
| PALLADIUM | 1113 | 2 | 1% | 0% | -83% | -90% | -90% |
| USDJPY | 1101 | 5 | 2% | 1% | -58% | -97% | -96% |
| AUDUSD | 655 | 4 | 1% | 1% | -43% | -84% | -83% |
| USDCAD | 619 | 0 | 2% | 0% | -100% | -97% | -97% |
| BRENT | 220 | 0 | 0% | 0% | -100% | -99% | -99% |
| 10YRRATE | 153 | 0 | 5% | 1% | -100% | -92% | -90% |
| 30YRRATE | 147 | 0 | 1% | 0% | -100% | -99% | -98% |
| 2YRRATE | 142 | 1 | 4% | 1% | -34% | -27% | -25% |
| 5YRRATE | 131 | 1 | 6% | 2% | -29% | -89% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 19358 | 77 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 18802 | 64 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3870 | 19 | 2% | 1% | -15% | -81% | -81% |
| 0.05–0.1% | 4079 | 14 | 3% | 2% | -49% | -92% | -92% |
| 0.1–0.2% | 6171 | 22 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 7011 | 30 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2610 | 10 | 7% | 3% | -61% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9458 | 35 | 4% | 2% | -58% | -86% | -86% |
| Morning (6am–12pm) | 9668 | 43 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 8872 | 29 | 4% | 2% | -62% | -88% | -88% |
| Evening (6pm–12am) | 10162 | 34 | 3% | 2% | -62% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,497 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/29 12:14:47 PM | USDCAD | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 12:14:47 PM | COPPER | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 12:14:31 PM | PLATINUM | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 12:14:31 PM | USDJPY | UP | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 12:14:15 PM | 2YRRATE | UP | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 12:14:00 PM | PALLADIUM | DOWN | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 12:14:00 PM | SILVER | DOWN | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 12:14:00 PM | 5YRRATE | UP | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 12:13:33 PM | XRP | UP | 86 sec | -0.232% | 0¢ | ❌ Lost | $0.00 |
| 10/29 12:13:33 PM | BTC | UP | 86 sec | -0.127% | 0¢ | ❌ Lost | $0.00 |
| 10/29 12:13:33 PM | 30YRRATE | UP | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 12:13:33 PM | GOLD | DOWN | 86 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 12:13:33 PM | SOL | UP | 86 sec | -0.149% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 12:13:33 PM | DOGE | UP | 86 sec | -0.224% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 12:13:17 PM | ETH | UP | 1.7 min | -0.146% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 12:13:02 PM | NEAR | UP | 1.9 min | -0.573% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 12:13:02 PM | BNB | UP | 1.9 min | -0.119% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 12:13:02 PM | HYPE | UP | 1.9 min | -0.392% | 0¢ | ❌ Lost | $0.00 |
| 10/29 12:12:30 PM | 10YRRATE | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 12:10:21 PM | ZEC | UP | 4.7 min | -0.971% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 11:59:56 AM | XRP | DOWN | 4 sec | +0.000% | 0¢ | ❌ Lost | $0.00 |
| 10/29 11:59:56 AM | WTI | UP | 4 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/29 11:59:56 AM | SOL | UP | 4 sec | +0.011% | 0¢ | ❌ Lost | $0.00 |
| 10/29 11:59:56 AM | GBPUSD | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 11:59:56 AM | BRENT | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 11:59:40 AM | PALLADIUM | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 11:59:40 AM | BTC | UP | 20 sec | -0.020% | 0¢ | ❌ Lost | $0.00 |
| 10/29 11:59:40 AM | SILVER | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 11:59:40 AM | NATGAS | DOWN | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 11:59:40 AM | ETH | DOWN | 20 sec | +0.037% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
