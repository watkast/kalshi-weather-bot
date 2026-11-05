# 15-Minute 1¢ Study

*Updated Thu Nov 5, 1:05 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3715 finished bets | 1% | $133.05 | +32% | +3.58¢ | $87.75 / $45.30 |

*Expect about **96 buys a day** (~$14.45/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3455 | $60.20 | +16% |
| Volatility model ≥ 2%, hold to the close | 6873 | $39.70 | +5% |
| Momentum model ≥ 2%, hold to the close | 5673 | -$36.50 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 46849 | 46838 | 172 (0%) | 1.07% | -$3,304.90 (-58%) | Hold to the close: -$3,304.90 (-58%) |

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
| Volatility model | 28405 | 4.7% | 0.4% (111) | -684% | ❌ Worse |
| Momentum model | 28405 | 4.6% | 0.4% (111) | -711% | ❌ Worse |
| Mean-reversion model | 28405 | 8.1% | 0.4% (111) | -831% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 28405 | 111 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6873 | 62 | +5% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3715 | 39 | +32% | -77% | -75% | -71% |
| Volatility model ≥ 10% | 2124 | 24 | +62% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5673 | 44 | -6% | -82% | -81% | -78% |
| Momentum model ≥ 5% | 3455 | 31 | +16% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2258 | 20 | +24% | -75% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11745 | 80 | -25% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8239 | 69 | -7% | -82% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5521 | 49 | +1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 28610 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11223 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7005 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 46838 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 172 | 0% | -$3,304.90 | -58% | — |
| Sell at 2¢ | 1834 | 4% | -$4,984.06 | -87% | 47 sec |
| Sell at 3¢ | 1252 | 3% | -$4,972.62 | -87% | 48 sec |
| Sell at 5¢ | 865 | 2% | -$4,870.65 | -85% | 63 sec |
| Sell at 10¢ | 524 | 1% | -$4,662.46 | -82% | 65 sec |
| Sell at 25¢ | 272 | 1% | -$4,336.58 | -76% | 82 sec |
| Sell at 50¢ | 175 | 0% | -$3,957.65 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2317 | 10 | 10% | 4% | -59% | -82% | -83% |
| 2–5 min | 15083 | 80 | 7% | 3% | -48% | -87% | -86% |
| 1–2 min | 11779 | 40 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 17647 | 42 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3204 | 13 | 5% | 2% | -48% | -88% | -88% |
| SOL | 3198 | 12 | 4% | 2% | -52% | -90% | -90% |
| HYPE | 3194 | 10 | 5% | 2% | -61% | -89% | -87% |
| BNB | 3194 | 17 | 5% | 2% | -33% | -85% | -84% |
| DOGE | 3179 | 6 | 4% | 2% | -76% | -90% | -90% |
| ETH | 3176 | 12 | 7% | 3% | -54% | -85% | -85% |
| NEAR | 3159 | 16 | 5% | 2% | -34% | -84% | -84% |
| BTC | 3158 | 15 | 5% | 2% | -35% | -88% | -89% |
| XRP | 3148 | 12 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1732 | 5 | 5% | 2% | -65% | -81% | -83% |
| WTI | 1681 | 5 | 4% | 1% | -64% | -92% | -92% |
| SILVER | 1678 | 8 | 5% | 2% | -44% | -82% | -81% |
| PLATINUM | 1513 | 4 | 2% | 1% | -75% | -96% | -96% |
| EURUSD | 1451 | 3 | 2% | 1% | -81% | -89% | -89% |
| COPPER | 1427 | 6 | 2% | 1% | -61% | -71% | -71% |
| GBPUSD | 1380 | 4 | 2% | 1% | -73% | -96% | -96% |
| NATGAS | 1367 | 8 | 2% | 1% | -45% | -76% | -75% |
| PALLADIUM | 1359 | 3 | 1% | 1% | -79% | -91% | -91% |
| USDJPY | 1358 | 5 | 2% | 1% | -66% | -97% | -97% |
| AUDUSD | 903 | 4 | 2% | 1% | -59% | -86% | -86% |
| USDCAD | 884 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 466 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 275 | 1 | 4% | 1% | -66% | -58% | -57% |
| 30YRRATE | 261 | 0 | 2% | 1% | -100% | -97% | -95% |
| 2YRRATE | 256 | 2 | 4% | 1% | -27% | -21% | -20% |
| 5YRRATE | 236 | 1 | 5% | 2% | -60% | -92% | -94% |
| INX | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 23748 | 91 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 23090 | 81 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4592 | 22 | 2% | 1% | -16% | -83% | -82% |
| 0.05–0.1% | 4864 | 18 | 3% | 2% | -44% | -91% | -90% |
| 0.1–0.2% | 7372 | 26 | 5% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 8535 | 34 | 6% | 3% | -56% | -87% | -86% |
| Over 0.5% | 3239 | 13 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11506 | 40 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11661 | 51 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 11045 | 40 | 4% | 2% | -58% | -86% | -86% |
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
| 11/5 12:59:52 PM | 2YRRATE | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 12:59:52 PM | GOLD | DOWN | 7 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/5 12:59:52 PM | DOGE | UP | 7 sec | -0.048% | 0¢ | ❌ Lost | $0.00 |
| 11/5 12:59:52 PM | AUDUSD | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 12:59:52 PM | PLATINUM | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 12:59:37 PM | BTC | UP | 22 sec | -0.044% | 0¢ | ❌ Lost | $0.00 |
| 11/5 12:59:37 PM | NATGAS | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 12:59:37 PM | ETH | UP | 22 sec | -0.066% | 0¢ | ❌ Lost | $0.00 |
| 11/5 12:59:37 PM | XRP | DOWN | 22 sec | +0.016% | 0¢ | ❌ Lost | $0.00 |
| 11/5 12:59:37 PM | WTI | UP | 22 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/5 12:59:05 PM | USDCAD | DOWN | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 12:59:05 PM | BNB | DOWN | 54 sec | +0.033% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 12:58:49 PM | SOL | DOWN | 71 sec | +0.153% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 12:58:32 PM | NEAR | DOWN | 88 sec | +0.282% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 12:58:32 PM | HYPE | UP | 88 sec | -0.383% | 0¢ | ❌ Lost | -$0.15 |
| 11/5 12:57:14 PM | GBPUSD | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 12:55:21 PM | EURUSD | DOWN | 4.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 12:44:55 PM | USDCAD | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 12:44:55 PM | GBPUSD | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 12:44:24 PM | INX | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 12:43:37 PM | HYPE | DOWN | 83 sec | +0.477% | 0¢ | ❌ Lost | -$0.15 |
| 11/5 12:43:37 PM | 30YRRATE | DOWN | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 12:43:21 PM | GOLD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | $0.00 |
| 11/5 12:43:21 PM | COPPER | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 12:43:05 PM | USDJPY | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 12:43:05 PM | SILVER | DOWN | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/5 12:43:05 PM | EURUSD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 12:42:50 PM | BNB | DOWN | 2.2 min | +0.135% | 0¢ | ❌ Lost | $0.00 |
| 11/5 12:42:50 PM | 10YRRATE | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 12:42:01 PM | 5YRRATE | DOWN | 3.0 min | — | 2¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
