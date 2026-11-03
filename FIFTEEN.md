# 15-Minute 1¢ Study

*Updated Tue Nov 3, 1:05 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3538 finished bets | 1% | $122.60 | +31% | +3.47¢ | $69.20 / $53.40 |

*Expect about **98 buys a day** (~$14.72/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3272 | $49.75 | +14% |
| Volatility model ≥ 2%, hold to the close | 6555 | $46.20 | +6% |
| Momentum model ≥ 2%, hold to the close | 5405 | -$36.90 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 43475 | 43465 | 161 (0%) | 1.07% | -$3,038.75 (-57%) | Hold to the close: -$3,038.75 (-57%) |

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
| Volatility model | 26881 | 4.7% | 0.4% (106) | -678% | ❌ Worse |
| Momentum model | 26881 | 4.6% | 0.4% (106) | -702% | ❌ Worse |
| Mean-reversion model | 26881 | 8.1% | 0.4% (106) | -825% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26881 | 106 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6555 | 60 | +6% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3538 | 37 | +31% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 2003 | 22 | +57% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 5405 | 42 | -6% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3272 | 29 | +14% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2136 | 19 | +24% | -74% | -73% | -69% |
| Mean-reversion model ≥ 2% | 11100 | 76 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7783 | 65 | -8% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 5202 | 46 | +0% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 27084 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10265 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6116 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 43465 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 161 | 0% | -$3,038.75 | -57% | — |
| Sell at 2¢ | 1716 | 4% | -$4,608.59 | -87% | 47 sec |
| Sell at 3¢ | 1177 | 3% | -$4,595.72 | -87% | 49 sec |
| Sell at 5¢ | 815 | 2% | -$4,497.00 | -85% | 63 sec |
| Sell at 10¢ | 490 | 1% | -$4,300.85 | -81% | 65 sec |
| Sell at 25¢ | 255 | 1% | -$3,986.70 | -75% | 82 sec |
| Sell at 50¢ | 166 | 0% | -$3,626.25 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2091 | 9 | 11% | 4% | -59% | -81% | -82% |
| 2–5 min | 13967 | 75 | 7% | 4% | -47% | -87% | -86% |
| 1–2 min | 10975 | 39 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 16421 | 38 | 1% | 0% | -67% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3035 | 13 | 5% | 3% | -45% | -88% | -87% |
| SOL | 3027 | 11 | 4% | 2% | -54% | -90% | -90% |
| BNB | 3023 | 17 | 5% | 2% | -30% | -85% | -84% |
| HYPE | 3022 | 9 | 5% | 2% | -63% | -89% | -87% |
| DOGE | 3008 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 3006 | 11 | 7% | 3% | -55% | -85% | -85% |
| BTC | 2991 | 14 | 5% | 2% | -37% | -88% | -89% |
| NEAR | 2990 | 15 | 5% | 2% | -35% | -83% | -84% |
| XRP | 2982 | 12 | 3% | 1% | -50% | -89% | -88% |
| GOLD | 1593 | 5 | 5% | 2% | -62% | -81% | -83% |
| SILVER | 1554 | 7 | 5% | 2% | -47% | -82% | -82% |
| WTI | 1551 | 4 | 3% | 1% | -69% | -92% | -93% |
| PLATINUM | 1383 | 3 | 2% | 1% | -80% | -96% | -96% |
| EURUSD | 1324 | 3 | 2% | 1% | -79% | -89% | -89% |
| COPPER | 1317 | 6 | 2% | 1% | -57% | -69% | -69% |
| NATGAS | 1266 | 7 | 2% | 1% | -48% | -82% | -81% |
| GBPUSD | 1252 | 2 | 2% | 1% | -85% | -96% | -96% |
| PALLADIUM | 1247 | 3 | 1% | 1% | -78% | -90% | -91% |
| USDJPY | 1233 | 5 | 2% | 1% | -62% | -97% | -96% |
| AUDUSD | 782 | 4 | 2% | 1% | -52% | -85% | -84% |
| USDCAD | 746 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 354 | 0 | 1% | 1% | -100% | -98% | -96% |
| 10YRRATE | 211 | 1 | 5% | 2% | -56% | -47% | -45% |
| 30YRRATE | 199 | 0 | 2% | 0% | -100% | -97% | -96% |
| 2YRRATE | 192 | 2 | 4% | 1% | -3% | +4% | +5% |
| 5YRRATE | 177 | 1 | 6% | 2% | -47% | -90% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 22118 | 87 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 21347 | 74 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4403 | 21 | 2% | 1% | -17% | -82% | -82% |
| 0.05–0.1% | 4641 | 18 | 3% | 2% | -42% | -91% | -90% |
| 0.1–0.2% | 7018 | 24 | 4% | 2% | -57% | -90% | -90% |
| 0.2–0.5% | 8021 | 33 | 7% | 3% | -54% | -86% | -86% |
| Over 0.5% | 2995 | 12 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10719 | 37 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 10804 | 48 | 4% | 2% | -49% | -85% | -85% |
| Afternoon (12–6pm) | 10198 | 38 | 4% | 2% | -56% | -85% | -85% |
| Evening (6pm–12am) | 11744 | 38 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,768 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/3 12:59:48 AM | USDCAD | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 12:59:48 AM | ZEC | DOWN | 11 sec | +0.188% | 0¢ | ❌ Lost | $0.00 |
| 11/3 12:59:48 AM | EURUSD | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 12:59:48 AM | GOLD | UP | 11 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/3 12:59:32 AM | SOL | DOWN | 27 sec | +0.018% | 0¢ | ❌ Lost | -$0.15 |
| 11/3 12:59:32 AM | BTC | UP | 27 sec | -0.030% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 12:59:32 AM | AUDUSD | DOWN | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 12:59:32 AM | NEAR | UP | 27 sec | -0.172% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 12:59:16 AM | DOGE | DOWN | 43 sec | +0.003% | 0¢ | ❌ Lost | -$0.15 |
| 11/3 12:59:00 AM | HYPE | DOWN | 60 sec | +0.060% | 0¢ | ❌ Lost | $0.00 |
| 11/3 12:59:00 AM | 30YRRATE | DOWN | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 12:59:00 AM | 5YRRATE | DOWN | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 12:58:44 AM | 2YRRATE | DOWN | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 12:58:28 AM | WTI | UP | 1.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 12:58:28 AM | PALLADIUM | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 12:58:12 AM | 10YRRATE | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 12:57:56 AM | USDJPY | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 12:57:21 AM | XRP | DOWN | 2.6 min | +0.104% | 6¢ | ❌ Lost | -$0.15 |
| 11/3 12:57:05 AM | ETH | DOWN | 2.9 min | +0.099% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 12:55:46 AM | BNB | DOWN | 4.2 min | +0.162% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 12:44:45 AM | WTI | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 12:44:45 AM | USDCAD | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 12:44:29 AM | USDJPY | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 12:44:29 AM | BTC | UP | 30 sec | -0.049% | 0¢ | ❌ Lost | $0.00 |
| 11/3 12:44:29 AM | ETH | UP | 30 sec | -0.056% | 0¢ | ❌ Lost | $0.00 |
| 11/3 12:43:57 AM | ZEC | UP | 63 sec | -0.355% | 0¢ | ❌ Lost | $0.00 |
| 11/3 12:43:57 AM | GOLD | UP | 63 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/3 12:43:43 AM | NEAR | UP | 76 sec | -0.295% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 12:41:19 AM | DOGE | UP | 3.7 min | -0.208% | 0¢ | ❌ Lost | -$0.15 |
| 11/3 12:41:19 AM | SOL | UP | 3.7 min | -0.258% | 3¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
