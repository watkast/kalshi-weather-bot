# 15-Minute 1¢ Study

*Updated Wed Nov 4, 8:21 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3641 finished bets | 1% | $111.65 | +27% | +3.07¢ | $78.10 / $33.55 |

*Expect about **97 buys a day** (~$14.62/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3376 | $39.25 | +11% |
| Volatility model ≥ 2%, hold to the close | 6739 | $25.20 | +3% |
| Momentum model ≥ 2%, hold to the close | 5557 | -$53.25 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 45341 | 45331 | 168 (0%) | 1.07% | -$3,172.05 (-57%) | Hold to the close: -$3,172.05 (-57%) |

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
| Volatility model | 27723 | 4.7% | 0.4% (108) | -680% | ❌ Worse |
| Momentum model | 27723 | 4.6% | 0.4% (108) | -707% | ❌ Worse |
| Mean-reversion model | 27723 | 8.1% | 0.4% (108) | -829% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 27723 | 108 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6739 | 60 | +3% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3641 | 37 | +27% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2069 | 22 | +52% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5557 | 42 | -8% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 3376 | 29 | +11% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2202 | 19 | +21% | -74% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11467 | 78 | -25% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8060 | 67 | -8% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 5400 | 47 | -1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 27928 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10770 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6633 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 45331 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 168 | 0% | -$3,172.05 | -57% | — |
| Sell at 2¢ | 1779 | 4% | -$4,809.51 | -87% | 47 sec |
| Sell at 3¢ | 1219 | 3% | -$4,796.64 | -87% | 49 sec |
| Sell at 5¢ | 843 | 2% | -$4,696.10 | -85% | 63 sec |
| Sell at 10¢ | 510 | 1% | -$4,491.95 | -81% | 65 sec |
| Sell at 25¢ | 267 | 1% | -$4,164.28 | -75% | 83 sec |
| Sell at 50¢ | 171 | 0% | -$3,795.80 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2235 | 10 | 11% | 4% | -57% | -81% | -83% |
| 2–5 min | 14582 | 79 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 11427 | 39 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 17076 | 40 | 1% | 0% | -67% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3129 | 13 | 5% | 2% | -46% | -88% | -88% |
| SOL | 3123 | 12 | 4% | 2% | -51% | -90% | -90% |
| HYPE | 3115 | 9 | 5% | 2% | -64% | -89% | -87% |
| BNB | 3115 | 17 | 5% | 2% | -31% | -85% | -85% |
| DOGE | 3103 | 6 | 4% | 2% | -76% | -90% | -90% |
| ETH | 3097 | 12 | 7% | 3% | -53% | -85% | -85% |
| BTC | 3086 | 14 | 5% | 2% | -38% | -88% | -89% |
| NEAR | 3084 | 15 | 5% | 2% | -37% | -84% | -84% |
| XRP | 3076 | 12 | 3% | 1% | -51% | -89% | -89% |
| GOLD | 1669 | 5 | 5% | 2% | -64% | -81% | -83% |
| WTI | 1624 | 5 | 4% | 1% | -63% | -92% | -93% |
| SILVER | 1622 | 8 | 5% | 2% | -42% | -82% | -81% |
| PLATINUM | 1452 | 4 | 2% | 1% | -74% | -96% | -96% |
| EURUSD | 1397 | 3 | 3% | 1% | -80% | -89% | -89% |
| COPPER | 1370 | 6 | 2% | 1% | -59% | -70% | -70% |
| GBPUSD | 1322 | 3 | 2% | 1% | -79% | -96% | -96% |
| NATGAS | 1318 | 8 | 2% | 1% | -43% | -75% | -74% |
| USDJPY | 1305 | 5 | 2% | 1% | -64% | -97% | -97% |
| PALLADIUM | 1301 | 3 | 1% | 1% | -78% | -91% | -91% |
| AUDUSD | 853 | 4 | 2% | 1% | -56% | -86% | -86% |
| USDCAD | 821 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 414 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 254 | 1 | 5% | 2% | -63% | -55% | -53% |
| 30YRRATE | 234 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 232 | 2 | 3% | 0% | -20% | -14% | -13% |
| 5YRRATE | 215 | 1 | 5% | 2% | -57% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 23003 | 89 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 22328 | 79 | 4% | 2% | -59% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4510 | 21 | 2% | 1% | -19% | -83% | -82% |
| 0.05–0.1% | 4761 | 18 | 3% | 2% | -43% | -91% | -90% |
| 0.1–0.2% | 7206 | 25 | 4% | 2% | -57% | -90% | -89% |
| 0.2–0.5% | 8305 | 33 | 6% | 3% | -56% | -87% | -86% |
| Over 0.5% | 3138 | 13 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11276 | 40 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11254 | 49 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 10598 | 39 | 4% | 2% | -57% | -86% | -86% |
| Evening (6pm–12am) | 12203 | 40 | 3% | 2% | -62% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,690 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/4 8:14:57 AM | AUDUSD | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 8:14:57 AM | GOLD | UP | 2 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/4 8:14:25 AM | NATGAS | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 8:14:25 AM | GBPUSD | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 8:14:09 AM | 30YRRATE | UP | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 8:14:09 AM | SILVER | DOWN | 51 sec | — | 84¢ | ✅ Won | $13.85 |
| 11/4 8:13:20 AM | COPPER | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 8:13:05 AM | USDJPY | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 8:12:50 AM | USDCAD | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 8:12:34 AM | EURUSD | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 8:12:34 AM | 2YRRATE | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 8:12:18 AM | BRENT | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 8:12:02 AM | PALLADIUM | DOWN | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 8:12:02 AM | 10YRRATE | DOWN | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 8:12:02 AM | 5YRRATE | DOWN | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 8:11:43 AM | PLATINUM | DOWN | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 8:10:43 AM | WTI | DOWN | 4.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/4 8:10:11 AM | ZEC | DOWN | 4.8 min | +1.930% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 8:10:11 AM | NEAR | DOWN | 4.8 min | +2.091% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 8:09:22 AM | DOGE | DOWN | 5.6 min | +1.780% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 8:08:51 AM | ETH | DOWN | 6.1 min | +2.532% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 8:08:51 AM | XRP | DOWN | 6.1 min | +1.720% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 8:08:36 AM | HYPE | DOWN | 6.4 min | +1.914% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 8:08:20 AM | BTC | DOWN | 6.7 min | +1.376% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 8:06:59 AM | SOL | DOWN | 8.0 min | +2.466% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 8:06:13 AM | BNB | DOWN | 8.8 min | +1.068% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 7:59:57 AM | USDJPY | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 7:59:57 AM | GBPUSD | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 7:59:57 AM | BRENT | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 7:59:57 AM | COPPER | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
