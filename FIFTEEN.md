# 15-Minute 1¢ Study

*Updated Thu Nov 5, 2:49 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3720 finished bets | 1% | $132.75 | +32% | +3.57¢ | $87.30 / $45.45 |

*Expect about **96 buys a day** (~$14.44/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3459 | $60.05 | +16% |
| Volatility model ≥ 2%, hold to the close | 6883 | $38.80 | +5% |
| Momentum model ≥ 2%, hold to the close | 5682 | -$37.25 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 46985 | 46974 | 173 (0%) | 1.07% | -$3,306.95 (-58%) | Hold to the close: -$3,306.95 (-58%) |

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
| Volatility model | 28466 | 4.7% | 0.4% (111) | -685% | ❌ Worse |
| Momentum model | 28466 | 4.6% | 0.4% (111) | -712% | ❌ Worse |
| Mean-reversion model | 28466 | 8.1% | 0.4% (111) | -833% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 28466 | 111 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6883 | 62 | +5% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3720 | 39 | +32% | -77% | -75% | -71% |
| Volatility model ≥ 10% | 2127 | 24 | +62% | -71% | -70% | -66% |
| Momentum model ≥ 2% | 5682 | 44 | -6% | -82% | -81% | -78% |
| Momentum model ≥ 5% | 3459 | 31 | +16% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2261 | 20 | +24% | -75% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11769 | 80 | -25% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8256 | 69 | -7% | -82% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5531 | 49 | +1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 28671 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11263 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7040 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 46974 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 173 | 0% | -$3,306.95 | -58% | — |
| Sell at 2¢ | 1840 | 4% | -$4,998.55 | -87% | 47 sec |
| Sell at 3¢ | 1254 | 3% | -$4,987.89 | -87% | 49 sec |
| Sell at 5¢ | 866 | 2% | -$4,886.05 | -85% | 63 sec |
| Sell at 10¢ | 525 | 1% | -$4,677.20 | -82% | 65 sec |
| Sell at 25¢ | 273 | 1% | -$4,349.32 | -76% | 83 sec |
| Sell at 50¢ | 176 | 0% | -$3,966.95 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2322 | 10 | 10% | 4% | -59% | -82% | -83% |
| 2–5 min | 15130 | 81 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 11806 | 40 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 17704 | 42 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3211 | 13 | 5% | 2% | -48% | -88% | -88% |
| SOL | 3205 | 12 | 4% | 2% | -52% | -90% | -90% |
| BNB | 3201 | 17 | 5% | 2% | -33% | -85% | -84% |
| HYPE | 3200 | 10 | 5% | 2% | -61% | -89% | -87% |
| DOGE | 3186 | 6 | 4% | 2% | -76% | -90% | -90% |
| ETH | 3183 | 12 | 7% | 3% | -54% | -85% | -85% |
| NEAR | 3166 | 16 | 5% | 2% | -34% | -84% | -84% |
| BTC | 3164 | 15 | 5% | 2% | -35% | -88% | -89% |
| XRP | 3155 | 12 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1737 | 5 | 5% | 2% | -65% | -81% | -83% |
| WTI | 1688 | 5 | 4% | 1% | -64% | -92% | -92% |
| SILVER | 1683 | 8 | 5% | 2% | -44% | -82% | -81% |
| PLATINUM | 1517 | 4 | 2% | 1% | -75% | -96% | -96% |
| EURUSD | 1455 | 3 | 2% | 1% | -81% | -89% | -89% |
| COPPER | 1432 | 6 | 2% | 1% | -61% | -71% | -71% |
| GBPUSD | 1384 | 4 | 2% | 1% | -73% | -96% | -96% |
| NATGAS | 1371 | 8 | 2% | 1% | -46% | -76% | -75% |
| PALLADIUM | 1364 | 3 | 1% | 1% | -79% | -91% | -91% |
| USDJPY | 1361 | 5 | 2% | 1% | -66% | -97% | -97% |
| AUDUSD | 908 | 4 | 2% | 1% | -59% | -86% | -87% |
| USDCAD | 888 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 471 | 0 | 1% | 1% | -100% | -97% | -97% |
| 10YRRATE | 279 | 1 | 4% | 1% | -67% | -59% | -57% |
| 30YRRATE | 265 | 0 | 2% | 1% | -100% | -97% | -95% |
| 2YRRATE | 260 | 3 | 4% | 1% | +8% | -22% | -20% |
| 5YRRATE | 239 | 1 | 5% | 2% | -61% | -92% | -95% |
| INX | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 23837 | 92 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 23137 | 81 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4597 | 22 | 2% | 1% | -16% | -83% | -82% |
| 0.05–0.1% | 4871 | 18 | 3% | 2% | -44% | -91% | -90% |
| 0.1–0.2% | 7382 | 26 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 8559 | 34 | 6% | 3% | -56% | -87% | -86% |
| Over 0.5% | 3254 | 13 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11506 | 40 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11661 | 51 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 11181 | 41 | 4% | 2% | -57% | -86% | -86% |
| Evening (6pm–12am) | 12626 | 41 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,647 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/5 2:44:49 PM | 10YRRATE | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 2:44:49 PM | ETH | DOWN | 10 sec | +0.024% | 0¢ | ❌ Lost | $0.00 |
| 11/5 2:44:49 PM | 5YRRATE | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 2:44:34 PM | PALLADIUM | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 2:44:34 PM | WTI | DOWN | 25 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/5 2:44:18 PM | 2YRRATE | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 2:44:18 PM | BNB | DOWN | 41 sec | +0.078% | 0¢ | ❌ Lost | $0.00 |
| 11/5 2:44:18 PM | PLATINUM | UP | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 2:44:02 PM | XRP | DOWN | 57 sec | +0.123% | 0¢ | ❌ Lost | $0.00 |
| 11/5 2:43:46 PM | BRENT | DOWN | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 2:43:15 PM | SOL | DOWN | 1.8 min | +0.216% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 2:43:15 PM | NEAR | DOWN | 1.8 min | +0.305% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 2:42:59 PM | COPPER | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 2:42:26 PM | ZEC | DOWN | 2.6 min | +0.696% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 2:42:26 PM | USDJPY | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 2:42:10 PM | DOGE | DOWN | 2.8 min | +0.321% | 0¢ | ❌ Lost | -$0.15 |
| 11/5 2:40:52 PM | NATGAS | UP | 4.1 min | — | 2¢ | ❌ Lost | -$0.15 |
| 11/5 2:39:32 PM | HYPE | DOWN | 5.5 min | +1.355% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 2:29:55 PM | 10YRRATE | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 2:29:55 PM | XRP | DOWN | 5 sec | +0.074% | 0¢ | ❌ Lost | $0.00 |
| 11/5 2:29:39 PM | NEAR | DOWN | 21 sec | +0.043% | 0¢ | ❌ Lost | $0.00 |
| 11/5 2:29:39 PM | AUDUSD | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 2:29:23 PM | SOL | DOWN | 37 sec | +0.155% | 0¢ | ❌ Lost | $0.00 |
| 11/5 2:29:07 PM | BTC | UP | 53 sec | -0.137% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 2:29:07 PM | BRENT | DOWN | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 2:28:35 PM | ZEC | DOWN | 84 sec | +0.595% | 0¢ | ❌ Lost | $0.00 |
| 11/5 2:28:35 PM | GBPUSD | DOWN | 84 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 2:27:47 PM | WTI | DOWN | 2.2 min | — | 0¢ | ❌ Lost | $0.00 |
| 11/5 2:26:11 PM | DOGE | UP | 3.8 min | -0.569% | 2¢ | ❌ Lost | -$0.15 |
| 11/5 2:25:55 PM | 2YRRATE | UP | 4.1 min | — | 93¢ | ✅ Won | $13.85 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
