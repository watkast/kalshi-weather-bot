# 15-Minute 1¢ Study

*Updated Thu Nov 5, 2:38 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3720 finished bets | 1% | $132.75 | +32% | +3.57¢ | $87.30 / $45.45 |

*Expect about **96 buys a day** (~$14.45/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3459 | $60.05 | +16% |
| Volatility model ≥ 2%, hold to the close | 6882 | $38.95 | +5% |
| Momentum model ≥ 2%, hold to the close | 5680 | -$37.10 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 46967 | 46956 | 173 (0%) | 1.07% | -$3,304.85 (-58%) | Hold to the close: -$3,304.85 (-58%) |

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
| Volatility model | 28458 | 4.7% | 0.4% (111) | -685% | ❌ Worse |
| Momentum model | 28458 | 4.6% | 0.4% (111) | -712% | ❌ Worse |
| Mean-reversion model | 28458 | 8.1% | 0.4% (111) | -834% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 28458 | 111 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6882 | 62 | +5% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3720 | 39 | +32% | -77% | -75% | -71% |
| Volatility model ≥ 10% | 2127 | 24 | +62% | -71% | -70% | -66% |
| Momentum model ≥ 2% | 5680 | 44 | -6% | -82% | -81% | -78% |
| Momentum model ≥ 5% | 3459 | 31 | +16% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2261 | 20 | +24% | -75% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11765 | 80 | -25% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8255 | 69 | -7% | -82% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5530 | 49 | +1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 28663 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11257 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7036 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 46956 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 173 | 0% | -$3,304.85 | -58% | — |
| Sell at 2¢ | 1839 | 4% | -$4,996.71 | -87% | 47 sec |
| Sell at 3¢ | 1254 | 3% | -$4,985.79 | -87% | 49 sec |
| Sell at 5¢ | 866 | 2% | -$4,883.95 | -85% | 63 sec |
| Sell at 10¢ | 525 | 1% | -$4,675.10 | -82% | 65 sec |
| Sell at 25¢ | 273 | 1% | -$4,347.22 | -76% | 83 sec |
| Sell at 50¢ | 176 | 0% | -$3,964.85 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2321 | 10 | 10% | 4% | -59% | -82% | -83% |
| 2–5 min | 15125 | 81 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 11803 | 40 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 17695 | 42 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3210 | 13 | 5% | 2% | -48% | -88% | -88% |
| SOL | 3204 | 12 | 4% | 2% | -52% | -90% | -90% |
| BNB | 3200 | 17 | 5% | 2% | -33% | -85% | -84% |
| HYPE | 3199 | 10 | 5% | 2% | -61% | -89% | -87% |
| DOGE | 3185 | 6 | 4% | 2% | -76% | -90% | -90% |
| ETH | 3182 | 12 | 7% | 3% | -54% | -85% | -85% |
| NEAR | 3165 | 16 | 5% | 2% | -34% | -84% | -84% |
| BTC | 3164 | 15 | 5% | 2% | -35% | -88% | -89% |
| XRP | 3154 | 12 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1737 | 5 | 5% | 2% | -65% | -81% | -83% |
| WTI | 1687 | 5 | 4% | 1% | -64% | -92% | -92% |
| SILVER | 1683 | 8 | 5% | 2% | -44% | -82% | -81% |
| PLATINUM | 1516 | 4 | 2% | 1% | -75% | -96% | -96% |
| EURUSD | 1455 | 3 | 2% | 1% | -81% | -89% | -89% |
| COPPER | 1431 | 6 | 2% | 1% | -61% | -71% | -71% |
| GBPUSD | 1384 | 4 | 2% | 1% | -73% | -96% | -96% |
| NATGAS | 1370 | 8 | 2% | 1% | -45% | -76% | -75% |
| PALLADIUM | 1363 | 3 | 1% | 1% | -79% | -91% | -91% |
| USDJPY | 1360 | 5 | 2% | 1% | -66% | -97% | -97% |
| AUDUSD | 908 | 4 | 2% | 1% | -59% | -86% | -87% |
| USDCAD | 888 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 470 | 0 | 1% | 1% | -100% | -97% | -97% |
| 10YRRATE | 278 | 1 | 4% | 1% | -66% | -59% | -57% |
| 30YRRATE | 265 | 0 | 2% | 1% | -100% | -97% | -95% |
| 2YRRATE | 259 | 3 | 4% | 1% | +8% | -21% | -20% |
| 5YRRATE | 238 | 1 | 5% | 2% | -61% | -92% | -95% |
| INX | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 23832 | 92 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 23124 | 81 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4596 | 22 | 2% | 1% | -16% | -83% | -82% |
| 0.05–0.1% | 4870 | 18 | 3% | 2% | -44% | -91% | -90% |
| 0.1–0.2% | 7381 | 26 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 8556 | 34 | 6% | 3% | -56% | -87% | -86% |
| Over 0.5% | 3252 | 13 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11506 | 40 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11661 | 51 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 11163 | 41 | 4% | 2% | -57% | -86% | -86% |
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
| 11/5 2:25:55 PM | ETH | UP | 4.1 min | -0.747% | 3¢ | ❌ Lost | -$0.15 |
| 11/5 2:25:55 PM | BNB | UP | 4.1 min | -0.379% | 3¢ | ❌ Lost | -$0.15 |
| 11/5 2:23:17 PM | USDJPY | UP | 6.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 2:14:29 PM | 30YRRATE | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 2:14:29 PM | ZEC | UP | 30 sec | -0.284% | 0¢ | ❌ Lost | $0.00 |
| 11/5 2:14:29 PM | NEAR | UP | 30 sec | -0.216% | 0¢ | ❌ Lost | -$0.15 |
| 11/5 2:14:13 PM | WTI | UP | 46 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/5 2:13:57 PM | BTC | UP | 62 sec | -0.143% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 2:13:42 PM | SOL | UP | 78 sec | -0.299% | 0¢ | ❌ Lost | $0.00 |
| 11/5 2:13:10 PM | ETH | UP | 1.8 min | -0.316% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 2:12:54 PM | GBPUSD | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 2:12:39 PM | DOGE | UP | 2.4 min | -0.313% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 2:12:39 PM | AUDUSD | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 2:12:23 PM | BNB | UP | 2.6 min | -0.307% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 2:12:07 PM | PLATINUM | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 2:11:35 PM | EURUSD | UP | 3.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/5 2:10:47 PM | HYPE | UP | 4.2 min | -0.881% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 2:10:32 PM | XRP | UP | 4.5 min | -0.732% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
