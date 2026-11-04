# 15-Minute 1¢ Study

*Updated Wed Nov 4, 1:20 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3627 finished bets | 1% | $113.30 | +28% | +3.12¢ | $78.55 / $34.75 |

*Expect about **98 buys a day** (~$14.68/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3360 | $41.20 | +11% |
| Volatility model ≥ 2%, hold to the close | 6716 | $28.05 | +3% |
| Momentum model ≥ 2%, hold to the close | 5533 | -$50.55 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 45008 | 44998 | 167 (0%) | 1.07% | -$3,142.85 (-57%) | Hold to the close: -$3,142.85 (-57%) |

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
| Volatility model | 27592 | 4.7% | 0.4% (108) | -677% | ❌ Worse |
| Momentum model | 27592 | 4.6% | 0.4% (108) | -704% | ❌ Worse |
| Mean-reversion model | 27592 | 8.1% | 0.4% (108) | -826% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 27592 | 108 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6716 | 60 | +3% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3627 | 37 | +28% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2058 | 22 | +53% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5533 | 42 | -8% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 3360 | 29 | +11% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2191 | 19 | +22% | -74% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11422 | 78 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 8026 | 67 | -8% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 5374 | 47 | -1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 27797 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10683 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6518 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 44998 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 167 | 0% | -$3,142.85 | -57% | — |
| Sell at 2¢ | 1768 | 4% | -$4,769.17 | -87% | 47 sec |
| Sell at 3¢ | 1212 | 3% | -$4,756.17 | -87% | 49 sec |
| Sell at 5¢ | 838 | 2% | -$4,656.15 | -85% | 63 sec |
| Sell at 10¢ | 506 | 1% | -$4,453.99 | -81% | 66 sec |
| Sell at 25¢ | 266 | 1% | -$4,124.39 | -75% | 83 sec |
| Sell at 50¢ | 170 | 0% | -$3,759.35 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2202 | 10 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 14483 | 79 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 11352 | 39 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 16950 | 39 | 1% | 0% | -67% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3114 | 13 | 5% | 3% | -46% | -88% | -88% |
| SOL | 3108 | 12 | 4% | 2% | -51% | -90% | -90% |
| BNB | 3101 | 17 | 5% | 2% | -31% | -85% | -84% |
| HYPE | 3100 | 9 | 5% | 2% | -64% | -89% | -87% |
| DOGE | 3088 | 6 | 4% | 2% | -76% | -90% | -90% |
| ETH | 3082 | 12 | 7% | 3% | -52% | -85% | -85% |
| NEAR | 3071 | 15 | 5% | 2% | -37% | -84% | -84% |
| BTC | 3071 | 14 | 5% | 2% | -38% | -88% | -89% |
| XRP | 3062 | 12 | 3% | 1% | -51% | -89% | -89% |
| GOLD | 1656 | 5 | 5% | 2% | -63% | -81% | -83% |
| WTI | 1612 | 5 | 3% | 1% | -62% | -92% | -93% |
| SILVER | 1610 | 7 | 5% | 2% | -49% | -82% | -82% |
| PLATINUM | 1442 | 4 | 2% | 1% | -74% | -96% | -96% |
| EURUSD | 1384 | 3 | 3% | 1% | -80% | -89% | -89% |
| COPPER | 1360 | 6 | 2% | 1% | -59% | -70% | -69% |
| GBPUSD | 1310 | 3 | 2% | 1% | -79% | -96% | -96% |
| NATGAS | 1309 | 8 | 2% | 1% | -43% | -75% | -74% |
| USDJPY | 1292 | 5 | 2% | 1% | -64% | -97% | -97% |
| PALLADIUM | 1291 | 3 | 1% | 1% | -78% | -91% | -91% |
| AUDUSD | 842 | 4 | 2% | 1% | -56% | -86% | -86% |
| USDCAD | 808 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 403 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 241 | 1 | 5% | 2% | -61% | -53% | -50% |
| 30YRRATE | 224 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 217 | 2 | 4% | 0% | -14% | -8% | -7% |
| 5YRRATE | 200 | 1 | 5% | 2% | -53% | -91% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 22844 | 89 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 22154 | 78 | 4% | 2% | -60% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4492 | 21 | 2% | 1% | -18% | -83% | -82% |
| 0.05–0.1% | 4736 | 18 | 3% | 2% | -42% | -91% | -90% |
| 0.1–0.2% | 7191 | 25 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 8265 | 33 | 6% | 3% | -56% | -87% | -86% |
| Over 0.5% | 3105 | 13 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11143 | 40 | 4% | 2% | -59% | -87% | -87% |
| Morning (6am–12pm) | 11054 | 48 | 4% | 2% | -51% | -85% | -85% |
| Afternoon (12–6pm) | 10598 | 39 | 4% | 2% | -57% | -86% | -86% |
| Evening (6pm–12am) | 12203 | 40 | 3% | 2% | -62% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,720 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/4 1:14:52 AM | 2YRRATE | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 1:14:52 AM | EURUSD | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 1:14:20 AM | NATGAS | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 1:14:20 AM | NEAR | DOWN | 40 sec | +0.251% | 0¢ | ❌ Lost | $0.00 |
| 11/4 1:14:04 AM | PALLADIUM | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 1:12:29 AM | PLATINUM | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 1:12:13 AM | BRENT | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 1:11:57 AM | WTI | UP | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/4 1:11:41 AM | SOL | DOWN | 3.3 min | +0.331% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 1:11:41 AM | BTC | DOWN | 3.3 min | +0.298% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 1:11:41 AM | ZEC | DOWN | 3.3 min | +0.845% | 0¢ | ❌ Lost | -$0.15 |
| 11/4 1:11:25 AM | BNB | DOWN | 3.6 min | +0.191% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 1:11:25 AM | AUDUSD | DOWN | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 1:10:53 AM | ETH | DOWN | 4.1 min | +0.446% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 1:10:17 AM | DOGE | DOWN | 4.7 min | +0.408% | 0¢ | ❌ Lost | $0.00 |
| 11/4 1:10:17 AM | SILVER | DOWN | 4.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/4 1:10:01 AM | HYPE | DOWN | 5.0 min | +0.480% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 1:10:01 AM | GOLD | DOWN | 5.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/4 1:09:27 AM | XRP | DOWN | 5.5 min | +0.338% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 12:59:54 AM | ZEC | DOWN | 5 sec | +0.003% | 0¢ | ❌ Lost | $0.00 |
| 11/4 12:59:54 AM | NEAR | UP | 5 sec | -0.114% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 12:59:54 AM | EURUSD | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 12:59:54 AM | ETH | UP | 5 sec | -0.041% | 0¢ | ❌ Lost | $0.00 |
| 11/4 12:59:54 AM | PALLADIUM | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 12:59:38 AM | 30YRRATE | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 12:59:38 AM | BNB | DOWN | 21 sec | -0.006% | 0¢ | ❌ Lost | $0.00 |
| 11/4 12:59:06 AM | WTI | UP | 54 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/4 12:59:06 AM | BRENT | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 12:59:06 AM | 2YRRATE | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 12:58:48 AM | 10YRRATE | UP | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
