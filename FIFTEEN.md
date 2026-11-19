# 15-Minute 1¢ Study

*Updated Thu Nov 19, 4:08 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4556 finished bets | 1% | $212.25 | +42% | +4.66¢ | $78.45 / $133.80 |

*Expect about **87 buys a day** (~$13.10/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4291 | $112.60 | +24% |
| Volatility model ≥ 2%, hold to the close | 8499 | $71.25 | +7% |
| Momentum model ≥ 2%, hold to the close | 7044 | -$9.00 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 61686 | 61652 | 238 (0%) | 1.07% | -$4,168.00 (-56%) | Hold to the close: -$4,168.00 (-56%) |

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
| Volatility model | 36706 | 4.5% | 0.4% (154) | -635% | ❌ Worse |
| Momentum model | 36706 | 4.4% | 0.4% (154) | -660% | ❌ Worse |
| Mean-reversion model | 36706 | 7.9% | 0.4% (154) | -770% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 36706 | 154 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8499 | 78 | +7% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4556 | 51 | +42% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 2620 | 30 | +67% | -63% | -62% | -58% |
| Momentum model ≥ 2% | 7044 | 57 | -1% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4291 | 41 | +24% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2798 | 26 | +33% | -67% | -66% | -62% |
| Mean-reversion model ≥ 2% | 15014 | 108 | -21% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10451 | 89 | -6% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6946 | 64 | +5% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 36912 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14753 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9987 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 61652 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 238 | 0% | -$4,168.00 | -56% | — |
| Sell at 2¢ | 2497 | 4% | -$6,556.78 | -87% | 47 sec |
| Sell at 3¢ | 1684 | 3% | -$6,549.24 | -87% | 48 sec |
| Sell at 5¢ | 1149 | 2% | -$6,431.15 | -86% | 63 sec |
| Sell at 10¢ | 702 | 1% | -$6,174.38 | -82% | 65 sec |
| Sell at 25¢ | 376 | 1% | -$5,709.44 | -76% | 80 sec |
| Sell at 50¢ | 245 | 0% | -$5,160.25 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3135 | 17 | 10% | 4% | -49% | -82% | -83% |
| 2–5 min | 19988 | 108 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 15433 | 51 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 23083 | 62 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4128 | 19 | 5% | 2% | -39% | -88% | -87% |
| SOL | 4125 | 19 | 4% | 2% | -41% | -86% | -86% |
| HYPE | 4117 | 12 | 4% | 2% | -63% | -89% | -88% |
| DOGE | 4108 | 11 | 4% | 2% | -66% | -89% | -89% |
| BNB | 4107 | 21 | 5% | 2% | -35% | -85% | -85% |
| ETH | 4101 | 19 | 7% | 3% | -42% | -82% | -82% |
| BTC | 4082 | 21 | 5% | 2% | -30% | -86% | -88% |
| NEAR | 4080 | 18 | 5% | 2% | -42% | -85% | -86% |
| XRP | 4064 | 16 | 3% | 2% | -50% | -89% | -88% |
| GOLD | 2201 | 6 | 5% | 2% | -67% | -82% | -84% |
| WTI | 2179 | 7 | 4% | 1% | -61% | -91% | -92% |
| SILVER | 2137 | 9 | 5% | 2% | -50% | -83% | -83% |
| PLATINUM | 1949 | 4 | 3% | 1% | -81% | -95% | -95% |
| EURUSD | 1904 | 7 | 2% | 1% | -66% | -91% | -90% |
| COPPER | 1834 | 6 | 2% | 1% | -69% | -76% | -76% |
| GBPUSD | 1830 | 7 | 2% | 1% | -64% | -96% | -96% |
| NATGAS | 1794 | 10 | 2% | 1% | -48% | -76% | -75% |
| USDJPY | 1788 | 6 | 2% | 1% | -69% | -96% | -96% |
| PALLADIUM | 1752 | 4 | 1% | 0% | -79% | -92% | -93% |
| AUDUSD | 1339 | 6 | 2% | 1% | -58% | -90% | -90% |
| USDCAD | 1281 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 907 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 465 | 2 | 3% | 1% | -60% | -74% | -73% |
| 2YRRATE | 444 | 4 | 4% | 2% | -16% | -52% | -50% |
| 30YRRATE | 426 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 418 | 2 | 4% | 1% | -55% | -94% | -96% |
| INX | 92 | 1 | 2% | 1% | +1% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 31403 | 122 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 30249 | 116 | 4% | 2% | -56% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5527 | 25 | 2% | 1% | -18% | -78% | -77% |
| 0.05–0.1% | 6005 | 24 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 9245 | 34 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 11469 | 50 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4657 | 23 | 7% | 3% | -48% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15020 | 46 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 14575 | 78 | 4% | 2% | -39% | -85% | -85% |
| Afternoon (12–6pm) | 15130 | 65 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 16927 | 49 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,017 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/19 3:59:47 AM | NEAR | UP | 13 sec | -0.265% | 0¢ | ❌ Lost | -$0.15 |
| 11/19 3:59:47 AM | NATGAS | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 3:59:47 AM | ZEC | DOWN | 13 sec | +0.004% | 0¢ | ❌ Lost | $0.00 |
| 11/19 3:59:31 AM | AUDUSD | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 3:59:31 AM | GBPUSD | UP | 29 sec | — | 29¢ | ✅ Won | $13.85 |
| 11/19 3:59:31 AM | HYPE | UP | 29 sec | -0.056% | 0¢ | ❌ Lost | $0.00 |
| 11/19 3:59:15 AM | DOGE | UP | 45 sec | -0.074% | 0¢ | ❌ Lost | $0.00 |
| 11/19 3:59:15 AM | SOL | UP | 45 sec | -0.096% | 0¢ | ❌ Lost | $0.00 |
| 11/19 3:58:59 AM | BTC | UP | 61 sec | -0.075% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 3:58:59 AM | USDJPY | DOWN | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 3:58:59 AM | PALLADIUM | DOWN | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 3:58:43 AM | USDCAD | DOWN | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 3:58:27 AM | ETH | UP | 1.5 min | -0.126% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 3:58:11 AM | SILVER | DOWN | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/19 3:56:03 AM | BNB | DOWN | 3.9 min | +0.163% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 3:56:03 AM | PLATINUM | DOWN | 3.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 3:55:16 AM | WTI | UP | 4.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/19 3:55:16 AM | BRENT | UP | 4.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 3:54:44 AM | COPPER | DOWN | 5.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/19 3:44:47 AM | SILVER | DOWN | 12 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/19 3:44:47 AM | HYPE | DOWN | 12 sec | +0.098% | 0¢ | ❌ Lost | $0.00 |
| 11/19 3:44:47 AM | XRP | DOWN | 12 sec | +0.061% | 0¢ | ❌ Lost | $0.00 |
| 11/19 3:44:31 AM | NEAR | DOWN | 28 sec | -0.006% | 0¢ | ❌ Lost | $0.00 |
| 11/19 3:44:31 AM | BTC | DOWN | 28 sec | +0.072% | 0¢ | ❌ Lost | $0.00 |
| 11/19 3:44:15 AM | WTI | DOWN | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 3:44:15 AM | ETH | DOWN | 44 sec | +0.051% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 3:43:59 AM | AUDUSD | DOWN | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 3:43:42 AM | BNB | DOWN | 78 sec | +0.027% | 0¢ | ❌ Lost | -$0.15 |
| 11/19 3:43:42 AM | SOL | DOWN | 78 sec | +0.120% | 1¢ | ❌ Lost | $0.00 |
| 11/19 3:43:10 AM | DOGE | DOWN | 1.8 min | +0.089% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
