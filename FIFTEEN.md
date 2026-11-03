# 15-Minute 1¢ Study

*Updated Tue Nov 3, 3:51 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3558 finished bets | 1% | $120.20 | +30% | +3.38¢ | $68.30 / $51.90 |

*Expect about **98 buys a day** (~$14.75/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3292 | $47.50 | +13% |
| Volatility model ≥ 2%, hold to the close | 6581 | $43.05 | +5% |
| Momentum model ≥ 2%, hold to the close | 5428 | -$39.45 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 43696 | 43686 | 162 (0%) | 1.07% | -$3,052.50 (-57%) | Hold to the close: -$3,052.50 (-57%) |

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
| Volatility model | 26978 | 4.7% | 0.4% (106) | -683% | ❌ Worse |
| Momentum model | 26978 | 4.6% | 0.4% (106) | -707% | ❌ Worse |
| Mean-reversion model | 26978 | 8.1% | 0.4% (106) | -831% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26978 | 106 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6581 | 60 | +5% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3558 | 37 | +30% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2020 | 22 | +55% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5428 | 42 | -6% | -81% | -81% | -77% |
| Momentum model ≥ 5% | 3292 | 29 | +13% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2151 | 19 | +23% | -74% | -73% | -69% |
| Mean-reversion model ≥ 2% | 11154 | 76 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7825 | 65 | -8% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 5233 | 46 | -0% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 27181 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10321 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6184 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 43686 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 162 | 0% | -$3,052.50 | -57% | — |
| Sell at 2¢ | 1722 | 4% | -$4,634.78 | -87% | 47 sec |
| Sell at 3¢ | 1181 | 3% | -$4,621.91 | -87% | 48 sec |
| Sell at 5¢ | 818 | 2% | -$4,522.80 | -85% | 63 sec |
| Sell at 10¢ | 492 | 1% | -$4,325.98 | -81% | 65 sec |
| Sell at 25¢ | 256 | 1% | -$4,011.14 | -75% | 82 sec |
| Sell at 50¢ | 167 | 0% | -$3,647.25 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2102 | 9 | 11% | 4% | -59% | -81% | -82% |
| 2–5 min | 14036 | 76 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 11042 | 39 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 16495 | 38 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3046 | 13 | 5% | 3% | -45% | -88% | -88% |
| SOL | 3038 | 11 | 4% | 2% | -54% | -91% | -90% |
| BNB | 3034 | 17 | 5% | 2% | -30% | -85% | -84% |
| HYPE | 3032 | 9 | 5% | 2% | -63% | -89% | -87% |
| DOGE | 3019 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 3016 | 11 | 7% | 3% | -56% | -85% | -85% |
| BTC | 3002 | 14 | 5% | 2% | -37% | -88% | -89% |
| NEAR | 3001 | 15 | 5% | 2% | -35% | -83% | -84% |
| XRP | 2993 | 12 | 3% | 1% | -50% | -89% | -88% |
| GOLD | 1601 | 5 | 5% | 2% | -62% | -81% | -83% |
| SILVER | 1562 | 7 | 5% | 2% | -47% | -82% | -82% |
| WTI | 1559 | 4 | 3% | 1% | -69% | -92% | -93% |
| PLATINUM | 1390 | 3 | 2% | 1% | -80% | -96% | -96% |
| EURUSD | 1332 | 3 | 2% | 1% | -79% | -89% | -89% |
| COPPER | 1323 | 6 | 2% | 1% | -58% | -69% | -69% |
| NATGAS | 1273 | 7 | 2% | 1% | -49% | -82% | -81% |
| GBPUSD | 1262 | 3 | 2% | 1% | -78% | -96% | -96% |
| PALLADIUM | 1251 | 3 | 1% | 1% | -78% | -90% | -91% |
| USDJPY | 1240 | 5 | 2% | 1% | -62% | -97% | -96% |
| AUDUSD | 792 | 4 | 2% | 1% | -53% | -85% | -85% |
| USDCAD | 754 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 362 | 0 | 1% | 1% | -100% | -98% | -96% |
| 10YRRATE | 219 | 1 | 5% | 2% | -57% | -49% | -47% |
| 30YRRATE | 206 | 0 | 1% | 0% | -100% | -97% | -96% |
| 2YRRATE | 198 | 2 | 4% | 1% | -6% | +1% | +2% |
| 5YRRATE | 181 | 1 | 6% | 2% | -48% | -90% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 22205 | 87 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 21481 | 75 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4424 | 21 | 2% | 1% | -17% | -83% | -82% |
| 0.05–0.1% | 4655 | 18 | 3% | 2% | -42% | -91% | -90% |
| 0.1–0.2% | 7042 | 24 | 4% | 2% | -57% | -90% | -90% |
| 0.2–0.5% | 8050 | 33 | 7% | 3% | -55% | -86% | -86% |
| Over 0.5% | 3004 | 12 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10940 | 38 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 10804 | 48 | 4% | 2% | -49% | -85% | -85% |
| Afternoon (12–6pm) | 10198 | 38 | 4% | 2% | -56% | -85% | -85% |
| Evening (6pm–12am) | 11744 | 38 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,751 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/3 3:44:49 AM | PLATINUM | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 3:44:49 AM | BTC | DOWN | 10 sec | +0.007% | 0¢ | ❌ Lost | $0.00 |
| 11/3 3:44:33 AM | HYPE | DOWN | 26 sec | -0.036% | 0¢ | ❌ Lost | -$0.15 |
| 11/3 3:44:33 AM | EURUSD | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 3:44:17 AM | WTI | DOWN | 42 sec | — | 7¢ | ❌ Lost | $0.00 |
| 11/3 3:44:17 AM | ZEC | DOWN | 42 sec | +0.194% | 0¢ | ❌ Lost | $0.00 |
| 11/3 3:44:17 AM | SOL | UP | 42 sec | -0.058% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 3:44:17 AM | ETH | DOWN | 42 sec | +0.033% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 3:44:17 AM | NEAR | UP | 42 sec | -0.247% | 0¢ | ❌ Lost | $0.00 |
| 11/3 3:44:01 AM | BRENT | DOWN | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 3:43:51 AM | XRP | DOWN | 69 sec | +0.064% | 0¢ | ❌ Lost | $0.00 |
| 11/3 3:43:51 AM | PALLADIUM | DOWN | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 3:43:51 AM | DOGE | DOWN | 69 sec | -0.001% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 3:43:35 AM | 10YRRATE | DOWN | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 3:43:19 AM | 30YRRATE | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 3:42:15 AM | GBPUSD | DOWN | 2.8 min | — | 59¢ | ✅ Won | $13.85 |
| 11/3 3:42:15 AM | NATGAS | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 3:41:26 AM | AUDUSD | DOWN | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 3:40:13 AM | USDCAD | UP | 4.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 3:39:42 AM | BNB | UP | 5.3 min | -0.211% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 3:29:52 AM | GBPUSD | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 3:29:36 AM | BTC | DOWN | 24 sec | +0.032% | 0¢ | ❌ Lost | $0.00 |
| 11/3 3:29:36 AM | BRENT | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 3:29:05 AM | GOLD | UP | 54 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 3:28:49 AM | XRP | DOWN | 70 sec | +0.048% | 0¢ | ❌ Lost | $0.00 |
| 11/3 3:28:33 AM | WTI | DOWN | 86 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 3:28:33 AM | PLATINUM | DOWN | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 3:28:17 AM | AUDUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 3:28:01 AM | NEAR | DOWN | 2.0 min | +0.199% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 3:27:43 AM | ETH | DOWN | 2.3 min | +0.153% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
