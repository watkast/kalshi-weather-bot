# 15-Minute 1¢ Study

*Updated Thu Nov 5, 5:50 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3735 finished bets | 1% | $131.10 | +32% | +3.51¢ | $86.55 / $44.55 |

*Expect about **96 buys a day** (~$14.46/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3473 | $58.70 | +16% |
| Volatility model ≥ 2%, hold to the close | 6910 | $35.65 | +4% |
| Momentum model ≥ 2%, hold to the close | 5702 | -$39.35 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 47144 | 47127 | 173 (0%) | 1.07% | -$3,324.65 (-58%) | Hold to the close: -$3,324.65 (-58%) |

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
| Volatility model | 28552 | 4.7% | 0.4% (111) | -685% | ❌ Worse |
| Momentum model | 28552 | 4.6% | 0.4% (111) | -712% | ❌ Worse |
| Mean-reversion model | 28552 | 8.1% | 0.4% (111) | -834% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 28552 | 111 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6910 | 62 | +4% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3735 | 39 | +32% | -77% | -75% | -71% |
| Volatility model ≥ 10% | 2134 | 24 | +62% | -71% | -70% | -66% |
| Momentum model ≥ 2% | 5702 | 44 | -6% | -82% | -81% | -78% |
| Momentum model ≥ 5% | 3473 | 31 | +16% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2271 | 20 | +24% | -75% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11812 | 80 | -26% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8280 | 69 | -7% | -82% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5546 | 49 | +1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 28757 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11298 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7072 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 47127 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 173 | 0% | -$3,324.65 | -58% | — |
| Sell at 2¢ | 1846 | 4% | -$5,014.69 | -87% | 47 sec |
| Sell at 3¢ | 1259 | 3% | -$5,003.64 | -87% | 49 sec |
| Sell at 5¢ | 870 | 2% | -$4,901.15 | -85% | 63 sec |
| Sell at 10¢ | 527 | 1% | -$4,692.28 | -82% | 65 sec |
| Sell at 25¢ | 275 | 1% | -$4,360.40 | -76% | 83 sec |
| Sell at 50¢ | 177 | 0% | -$3,977.90 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2328 | 10 | 10% | 4% | -59% | -82% | -83% |
| 2–5 min | 15184 | 81 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 11851 | 40 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 17752 | 42 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3221 | 13 | 5% | 2% | -48% | -88% | -88% |
| SOL | 3215 | 12 | 4% | 2% | -53% | -90% | -90% |
| BNB | 3211 | 17 | 5% | 2% | -33% | -85% | -84% |
| HYPE | 3208 | 10 | 5% | 2% | -61% | -89% | -88% |
| DOGE | 3195 | 6 | 4% | 2% | -76% | -90% | -90% |
| ETH | 3193 | 12 | 7% | 3% | -54% | -85% | -85% |
| NEAR | 3175 | 16 | 5% | 2% | -35% | -84% | -84% |
| BTC | 3174 | 15 | 5% | 2% | -36% | -88% | -89% |
| XRP | 3165 | 12 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1742 | 5 | 5% | 2% | -65% | -81% | -82% |
| WTI | 1692 | 5 | 4% | 1% | -64% | -92% | -92% |
| SILVER | 1688 | 8 | 5% | 2% | -44% | -82% | -82% |
| PLATINUM | 1521 | 4 | 2% | 1% | -75% | -96% | -96% |
| EURUSD | 1461 | 3 | 2% | 1% | -81% | -89% | -89% |
| COPPER | 1437 | 6 | 2% | 1% | -61% | -71% | -71% |
| GBPUSD | 1390 | 4 | 2% | 1% | -73% | -96% | -96% |
| NATGAS | 1378 | 8 | 2% | 1% | -46% | -76% | -75% |
| PALLADIUM | 1366 | 3 | 1% | 1% | -80% | -91% | -91% |
| USDJPY | 1366 | 5 | 2% | 1% | -66% | -97% | -97% |
| AUDUSD | 915 | 4 | 2% | 1% | -59% | -87% | -87% |
| USDCAD | 893 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 474 | 0 | 1% | 1% | -100% | -97% | -97% |
| 10YRRATE | 280 | 1 | 4% | 1% | -67% | -59% | -57% |
| 30YRRATE | 265 | 0 | 2% | 1% | -100% | -97% | -95% |
| 2YRRATE | 261 | 3 | 4% | 1% | +7% | -22% | -21% |
| 5YRRATE | 240 | 1 | 5% | 2% | -61% | -92% | -95% |
| INX | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 23906 | 92 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 23221 | 81 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4605 | 22 | 2% | 1% | -16% | -83% | -82% |
| 0.05–0.1% | 4874 | 18 | 3% | 2% | -44% | -91% | -90% |
| 0.1–0.2% | 7404 | 26 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 8600 | 34 | 6% | 3% | -56% | -87% | -86% |
| Over 0.5% | 3266 | 13 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11506 | 40 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11661 | 51 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 11334 | 41 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 12626 | 41 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,650 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/5 5:44:58 PM | NATGAS | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:44:58 PM | GOLD | UP | 1 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/5 5:44:42 PM | SILVER | DOWN | 17 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/5 5:44:26 PM | EURUSD | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:44:10 PM | USDJPY | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:43:55 PM | AUDUSD | DOWN | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:43:55 PM | PLATINUM | DOWN | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:43:23 PM | USDCAD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:43:23 PM | COPPER | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:42:35 PM | BTC | DOWN | 2.4 min | +0.214% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 5:42:19 PM | ETH | DOWN | 2.7 min | +0.240% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 5:42:03 PM | HYPE | DOWN | 3.0 min | +0.354% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 5:41:48 PM | SOL | DOWN | 3.2 min | +0.368% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 5:41:32 PM | BNB | DOWN | 3.5 min | +0.185% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 5:40:03 PM | XRP | DOWN | 5.0 min | +0.411% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 5:40:03 PM | NEAR | DOWN | 5.0 min | +1.169% | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:39:30 PM | DOGE | DOWN | 5.5 min | +0.465% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 5:38:58 PM | ZEC | DOWN | 6.0 min | +1.610% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 5:29:56 PM | USDCAD | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:29:09 PM | GOLD | DOWN | 50 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/5 5:28:53 PM | BTC | DOWN | 66 sec | +0.092% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 5:28:05 PM | GBPUSD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:27:46 PM | EURUSD | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:27:46 PM | SILVER | DOWN | 2.2 min | — | 0¢ | ❌ Lost | $0.00 |
| 11/5 5:27:30 PM | ETH | DOWN | 2.5 min | +0.272% | 0¢ | ❌ Lost | $0.00 |
| 11/5 5:27:14 PM | COPPER | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:27:14 PM | NATGAS | UP | 2.8 min | — | 38¢ | ❌ Lost | -$0.15 |
| 11/5 5:27:14 PM | AUDUSD | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:27:00 PM | USDJPY | DOWN | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 5:27:00 PM | PALLADIUM | DOWN | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
