# 15-Minute 1¢ Study

*Updated Mon Nov 16, 8:38 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4446 finished bets | 1% | $222.60 | +45% | +5.01¢ | $84.90 / $137.70 |

*Expect about **89 buys a day** (~$13.38/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4196 | $120.85 | +27% |
| Volatility model ≥ 2%, hold to the close | 8277 | $82.75 | +8% |
| Momentum model ≥ 2%, hold to the close | 6881 | $8.70 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 59124 | 59090 | 227 (0%) | 1.07% | -$4,008.35 (-56%) | Hold to the close: -$4,008.35 (-56%) |

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
| Volatility model | 35560 | 4.6% | 0.4% (148) | -635% | ❌ Worse |
| Momentum model | 35560 | 4.5% | 0.4% (148) | -661% | ❌ Worse |
| Mean-reversion model | 35560 | 7.9% | 0.4% (148) | -773% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 35560 | 148 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8277 | 77 | +8% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4446 | 51 | +45% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2559 | 30 | +70% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6881 | 57 | +1% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4196 | 41 | +27% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2733 | 26 | +35% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14558 | 103 | -22% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10131 | 85 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6726 | 61 | +3% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 35766 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14003 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9321 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 59090 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 227 | 0% | -$4,008.35 | -56% | — |
| Sell at 2¢ | 2372 | 4% | -$6,275.63 | -87% | 47 sec |
| Sell at 3¢ | 1600 | 3% | -$6,268.35 | -87% | 48 sec |
| Sell at 5¢ | 1095 | 2% | -$6,152.60 | -86% | 62 sec |
| Sell at 10¢ | 669 | 1% | -$5,903.96 | -82% | 65 sec |
| Sell at 25¢ | 355 | 1% | -$5,479.30 | -76% | 80 sec |
| Sell at 50¢ | 234 | 0% | -$4,948.85 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2961 | 13 | 11% | 4% | -58% | -81% | -83% |
| 2–5 min | 19115 | 104 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 14868 | 51 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 22133 | 59 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4003 | 19 | 5% | 2% | -38% | -88% | -87% |
| SOL | 3998 | 18 | 4% | 2% | -42% | -87% | -87% |
| HYPE | 3990 | 12 | 4% | 2% | -62% | -89% | -88% |
| BNB | 3980 | 20 | 5% | 2% | -36% | -86% | -85% |
| DOGE | 3979 | 11 | 4% | 2% | -65% | -90% | -89% |
| ETH | 3971 | 17 | 6% | 3% | -47% | -82% | -82% |
| BTC | 3954 | 21 | 5% | 2% | -28% | -86% | -88% |
| NEAR | 3952 | 17 | 5% | 2% | -44% | -85% | -86% |
| XRP | 3939 | 15 | 3% | 2% | -52% | -89% | -88% |
| GOLD | 2095 | 5 | 5% | 2% | -71% | -82% | -84% |
| WTI | 2077 | 7 | 4% | 1% | -59% | -91% | -92% |
| SILVER | 2035 | 9 | 5% | 2% | -47% | -83% | -83% |
| PLATINUM | 1859 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1806 | 6 | 2% | 1% | -69% | -91% | -90% |
| COPPER | 1737 | 6 | 2% | 1% | -68% | -75% | -75% |
| GBPUSD | 1732 | 6 | 2% | 1% | -68% | -96% | -96% |
| NATGAS | 1716 | 9 | 2% | 1% | -51% | -75% | -74% |
| USDJPY | 1692 | 6 | 2% | 1% | -67% | -97% | -96% |
| PALLADIUM | 1669 | 4 | 1% | 0% | -78% | -92% | -93% |
| AUDUSD | 1249 | 6 | 2% | 1% | -55% | -89% | -89% |
| USDCAD | 1194 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 815 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 418 | 2 | 4% | 1% | -55% | -71% | -70% |
| 2YRRATE | 403 | 4 | 4% | 2% | -7% | -47% | -46% |
| 30YRRATE | 388 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 375 | 2 | 4% | 2% | -50% | -94% | -95% |
| INX | 64 | 0 | 2% | 0% | -100% | -97% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 30041 | 113 | 4% | 2% | -57% | -88% | -88% |
| DOWN (bought NO) | 29049 | 114 | 4% | 2% | -55% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5422 | 25 | 2% | 1% | -17% | -78% | -77% |
| 0.05–0.1% | 5866 | 24 | 3% | 2% | -36% | -91% | -90% |
| 0.1–0.2% | 8974 | 34 | 5% | 2% | -51% | -89% | -89% |
| 0.2–0.5% | 11044 | 48 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4451 | 19 | 7% | 3% | -55% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14411 | 45 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13940 | 70 | 4% | 2% | -43% | -85% | -84% |
| Afternoon (12–6pm) | 14631 | 63 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 16108 | 49 | 4% | 2% | -65% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,080 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/16 8:29:51 PM | WTI | UP | 8 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/16 8:29:36 PM | PALLADIUM | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 8:29:36 PM | GOLD | DOWN | 24 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/16 8:29:36 PM | NATGAS | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 8:29:20 PM | COPPER | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 8:29:04 PM | PLATINUM | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 8:28:48 PM | USDJPY | DOWN | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 8:28:30 PM | GBPUSD | DOWN | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 8:28:30 PM | ZEC | DOWN | 89 sec | +0.951% | 0¢ | ❌ Lost | $0.00 |
| 11/16 8:28:30 PM | AUDUSD | DOWN | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 8:26:52 PM | NEAR | DOWN | 3.1 min | +0.453% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 8:26:36 PM | BNB | DOWN | 3.4 min | +0.172% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 8:26:36 PM | HYPE | DOWN | 3.4 min | +0.468% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 8:26:36 PM | XRP | DOWN | 3.4 min | +0.365% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 8:26:36 PM | SOL | DOWN | 3.4 min | +0.310% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 8:26:36 PM | DOGE | DOWN | 3.4 min | +0.409% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 8:26:36 PM | BTC | DOWN | 3.4 min | +0.274% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 8:25:33 PM | ETH | DOWN | 4.4 min | +0.324% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 8:14:53 PM | PLATINUM | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 8:14:38 PM | USDJPY | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 8:14:38 PM | GOLD | DOWN | 22 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/16 8:14:38 PM | AUDUSD | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 8:14:22 PM | GBPUSD | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 8:14:22 PM | PALLADIUM | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 8:13:50 PM | EURUSD | DOWN | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 8:11:43 PM | ETH | DOWN | 3.3 min | +0.232% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 8:11:28 PM | BNB | DOWN | 3.5 min | +0.200% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 8:11:28 PM | BTC | DOWN | 3.5 min | +0.255% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 8:10:09 PM | ZEC | DOWN | 4.8 min | +0.663% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 8:09:53 PM | HYPE | DOWN | 5.1 min | +0.604% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
