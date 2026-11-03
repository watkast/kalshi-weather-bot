# 15-Minute 1¢ Study

*Updated Tue Nov 3, 9:23 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3562 finished bets | 1% | $119.60 | +30% | +3.36¢ | $68.15 / $51.45 |

*Expect about **98 buys a day** (~$14.68/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3295 | $47.20 | +13% |
| Volatility model ≥ 2%, hold to the close | 6587 | $42.30 | +5% |
| Momentum model ≥ 2%, hold to the close | 5431 | -$39.75 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 43822 | 43811 | 164 (0%) | 1.07% | -$3,038.75 (-57%) | Hold to the close: -$3,038.75 (-57%) |

*In play or awaiting result: 10. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 27029 | 4.7% | 0.4% (106) | -682% | ❌ Worse |
| Momentum model | 27029 | 4.6% | 0.4% (106) | -706% | ❌ Worse |
| Mean-reversion model | 27029 | 8.1% | 0.4% (106) | -830% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 27029 | 106 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6587 | 60 | +5% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3562 | 37 | +30% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2021 | 22 | +55% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5431 | 42 | -6% | -81% | -81% | -77% |
| Momentum model ≥ 5% | 3295 | 29 | +13% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2152 | 19 | +23% | -74% | -73% | -69% |
| Mean-reversion model ≥ 2% | 11170 | 76 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7836 | 65 | -8% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 5244 | 46 | -1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 27232 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10354 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6225 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 43811 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 164 | 0% | -$3,038.75 | -57% | — |
| Sell at 2¢ | 1729 | 4% | -$4,647.21 | -87% | 47 sec |
| Sell at 3¢ | 1186 | 3% | -$4,634.21 | -87% | 48 sec |
| Sell at 5¢ | 823 | 2% | -$4,533.80 | -85% | 63 sec |
| Sell at 10¢ | 496 | 1% | -$4,334.99 | -81% | 66 sec |
| Sell at 25¢ | 260 | 1% | -$4,012.15 | -75% | 83 sec |
| Sell at 50¢ | 168 | 0% | -$3,640.75 | -68% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2108 | 9 | 11% | 4% | -59% | -81% | -82% |
| 2–5 min | 14067 | 78 | 7% | 4% | -45% | -86% | -86% |
| 1–2 min | 11083 | 39 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 16542 | 38 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3052 | 13 | 5% | 3% | -45% | -88% | -88% |
| SOL | 3044 | 11 | 4% | 2% | -54% | -91% | -90% |
| BNB | 3039 | 17 | 5% | 2% | -30% | -85% | -84% |
| HYPE | 3038 | 9 | 5% | 2% | -63% | -89% | -87% |
| DOGE | 3024 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 3022 | 11 | 7% | 3% | -56% | -85% | -85% |
| NEAR | 3007 | 15 | 5% | 2% | -35% | -84% | -84% |
| BTC | 3007 | 14 | 5% | 2% | -37% | -88% | -89% |
| XRP | 2999 | 12 | 3% | 1% | -50% | -89% | -88% |
| GOLD | 1606 | 5 | 5% | 2% | -62% | -81% | -83% |
| SILVER | 1568 | 7 | 5% | 2% | -47% | -82% | -81% |
| WTI | 1564 | 5 | 3% | 1% | -61% | -92% | -93% |
| PLATINUM | 1395 | 4 | 2% | 1% | -73% | -96% | -96% |
| EURUSD | 1338 | 3 | 2% | 1% | -79% | -89% | -89% |
| COPPER | 1325 | 6 | 2% | 1% | -58% | -69% | -69% |
| NATGAS | 1276 | 7 | 2% | 1% | -49% | -82% | -81% |
| GBPUSD | 1266 | 3 | 2% | 1% | -78% | -96% | -96% |
| PALLADIUM | 1254 | 3 | 1% | 1% | -78% | -90% | -91% |
| USDJPY | 1244 | 5 | 2% | 1% | -62% | -97% | -96% |
| AUDUSD | 797 | 4 | 2% | 1% | -53% | -85% | -85% |
| USDCAD | 760 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 366 | 0 | 1% | 1% | -100% | -98% | -96% |
| 10YRRATE | 224 | 1 | 5% | 2% | -58% | -50% | -48% |
| 30YRRATE | 210 | 0 | 1% | 0% | -100% | -98% | -96% |
| 2YRRATE | 201 | 2 | 4% | 0% | -7% | -0% | +1% |
| 5YRRATE | 185 | 1 | 5% | 2% | -50% | -91% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 22263 | 88 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 21548 | 76 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4432 | 21 | 2% | 1% | -17% | -83% | -82% |
| 0.05–0.1% | 4665 | 18 | 3% | 2% | -42% | -91% | -90% |
| 0.1–0.2% | 7053 | 24 | 4% | 2% | -58% | -90% | -90% |
| 0.2–0.5% | 8067 | 33 | 7% | 3% | -55% | -87% | -86% |
| Over 0.5% | 3009 | 12 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11048 | 40 | 4% | 2% | -59% | -87% | -87% |
| Morning (6am–12pm) | 10821 | 48 | 4% | 2% | -49% | -85% | -85% |
| Afternoon (12–6pm) | 10198 | 38 | 4% | 2% | -56% | -85% | -85% |
| Evening (6pm–12am) | 11744 | 38 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,738 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/3 9:23:05 AM | NEAR | UP | 6.9 min | -1.182% | — | In play | — |
| 11/3 9:14:51 AM | SILVER | UP | 9 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/3 9:14:51 AM | 5YRRATE | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 9:14:35 AM | PALLADIUM | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 9:14:35 AM | 2YRRATE | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 9:14:20 AM | NATGAS | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 9:13:46 AM | EURUSD | UP | 73 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 9:13:30 AM | ZEC | UP | 89 sec | -0.465% | 0¢ | ❌ Lost | $0.00 |
| 11/3 9:13:30 AM | XRP | UP | 89 sec | -0.188% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 9:13:30 AM | BTC | UP | 89 sec | -0.125% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 9:13:30 AM | NEAR | UP | 89 sec | -0.516% | 0¢ | ❌ Lost | -$0.15 |
| 11/3 9:13:14 AM | BNB | UP | 1.8 min | -0.258% | 0¢ | ❌ Lost | $0.00 |
| 11/3 9:13:14 AM | SOL | UP | 1.8 min | -0.330% | 0¢ | ❌ Lost | $0.00 |
| 11/3 9:13:14 AM | DOGE | UP | 1.8 min | -0.308% | 0¢ | ❌ Lost | $0.00 |
| 11/3 9:13:14 AM | ETH | UP | 1.8 min | -0.212% | 0¢ | ❌ Lost | -$0.15 |
| 11/3 9:13:14 AM | HYPE | UP | 1.8 min | -0.886% | 0¢ | ❌ Lost | $0.00 |
| 11/3 9:13:14 AM | AUDUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 9:13:14 AM | USDCAD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 5:12:44 AM | HYPE | DOWN | 2.3 min | +0.368% | 0¢ | ❌ Lost | $0.00 |
| 11/3 5:12:28 AM | SILVER | UP | 2.5 min | — | 40¢ | ❌ Lost | -$0.15 |
| 11/3 5:11:52 AM | AUDUSD | UP | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 5:11:52 AM | WTI | DOWN | 3.1 min | — | 93¢ | ✅ Won | $14.00 |
| 11/3 5:11:20 AM | PLATINUM | UP | 3.6 min | — | 45¢ | ✅ Won | $13.85 |
| 11/3 5:11:04 AM | GOLD | UP | 3.9 min | — | 33¢ | ❌ Lost | -$0.15 |
| 11/3 5:10:32 AM | USDCAD | DOWN | 4.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 4:59:44 AM | SOL | DOWN | 16 sec | +0.019% | 0¢ | ❌ Lost | $0.00 |
| 11/3 4:59:44 AM | EURUSD | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 4:59:44 AM | ZEC | DOWN | 16 sec | +0.018% | 0¢ | ❌ Lost | -$0.15 |
| 11/3 4:59:28 AM | AUDUSD | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 4:59:28 AM | NATGAS | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
