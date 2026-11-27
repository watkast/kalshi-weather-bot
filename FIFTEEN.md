# 15-Minute 1¢ Study

*Updated Fri Nov 27, 2:17 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 5000 finished bets | 1% | $199.75 | +37% | +3.99¢ | $95.10 / $104.65 |

*Expect about **83 buys a day** (~$12.48/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4743 | $99.50 | +20% |
| Volatility model ≥ 2%, hold to the close | 9325 | $25.95 | +2% |
| Momentum model ≥ 2%, hold to the close | 7763 | -$52.10 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 69274 | 69240 | 257 (0%) | 1.07% | -$4,784.75 (-57%) | Hold to the close: -$4,784.75 (-57%) |

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
| Volatility model | 40867 | 4.5% | 0.4% (165) | -661% | ❌ Worse |
| Momentum model | 40867 | 4.5% | 0.4% (165) | -684% | ❌ Worse |
| Mean-reversion model | 40867 | 7.9% | 0.4% (165) | -802% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 40867 | 165 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 9325 | 81 | +2% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 5000 | 53 | +37% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 2903 | 32 | +64% | -65% | -64% | -60% |
| Momentum model ≥ 2% | 7763 | 59 | -6% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 4743 | 43 | +20% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 3093 | 28 | +32% | -68% | -68% | -64% |
| Mean-reversion model ≥ 2% | 16676 | 113 | -25% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11612 | 93 | -11% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7702 | 66 | -2% | -78% | -78% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 41073 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 16564 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 11603 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 69240 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 257 | 0% | -$4,784.75 | -57% | — |
| Sell at 2¢ | 2836 | 4% | -$7,337.39 | -88% | 47 sec |
| Sell at 3¢ | 1903 | 3% | -$7,332.58 | -87% | 48 sec |
| Sell at 5¢ | 1287 | 2% | -$7,210.20 | -86% | 62 sec |
| Sell at 10¢ | 786 | 1% | -$6,933.09 | -83% | 65 sec |
| Sell at 25¢ | 425 | 1% | -$6,402.00 | -76% | 80 sec |
| Sell at 50¢ | 271 | 0% | -$5,797.50 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3601 | 17 | 10% | 4% | -55% | -82% | -83% |
| 2–5 min | 22449 | 116 | 7% | 3% | -49% | -86% | -86% |
| 1–2 min | 17224 | 58 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 25953 | 66 | 1% | 0% | -63% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4595 | 20 | 5% | 2% | -42% | -88% | -87% |
| HYPE | 4584 | 16 | 4% | 2% | -55% | -89% | -88% |
| SOL | 4578 | 20 | 4% | 2% | -43% | -86% | -86% |
| BNB | 4572 | 22 | 5% | 2% | -39% | -86% | -85% |
| DOGE | 4570 | 12 | 4% | 2% | -66% | -89% | -89% |
| ETH | 4564 | 19 | 7% | 3% | -48% | -82% | -82% |
| BTC | 4542 | 24 | 5% | 2% | -27% | -86% | -88% |
| NEAR | 4538 | 18 | 5% | 2% | -48% | -85% | -86% |
| XRP | 4530 | 16 | 4% | 2% | -55% | -88% | -88% |
| GOLD | 2446 | 8 | 5% | 2% | -60% | -83% | -84% |
| WTI | 2429 | 9 | 4% | 2% | -55% | -86% | -87% |
| SILVER | 2395 | 9 | 5% | 2% | -55% | -83% | -84% |
| PLATINUM | 2166 | 5 | 3% | 1% | -78% | -95% | -95% |
| EURUSD | 2122 | 7 | 2% | 1% | -69% | -91% | -91% |
| GBPUSD | 2066 | 8 | 2% | 1% | -64% | -96% | -96% |
| COPPER | 2052 | 6 | 2% | 1% | -73% | -79% | -79% |
| USDJPY | 2018 | 6 | 2% | 1% | -72% | -97% | -96% |
| NATGAS | 2007 | 10 | 2% | 1% | -53% | -77% | -77% |
| PALLADIUM | 1954 | 4 | 1% | 1% | -81% | -93% | -93% |
| AUDUSD | 1593 | 7 | 2% | 1% | -59% | -90% | -90% |
| USDCAD | 1498 | 1 | 3% | 1% | -94% | -95% | -95% |
| BRENT | 1115 | 1 | 2% | 1% | -92% | -96% | -97% |
| 10YRRATE | 559 | 2 | 3% | 1% | -67% | -78% | -76% |
| 30YRRATE | 519 | 0 | 3% | 1% | -100% | -95% | -93% |
| 2YRRATE | 518 | 4 | 4% | 2% | -28% | -58% | -57% |
| 5YRRATE | 509 | 2 | 4% | 2% | -63% | -94% | -95% |
| INX | 139 | 1 | 2% | 1% | -33% | -96% | -96% |
| USDMXN | 62 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 35250 | 133 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 33990 | 124 | 4% | 2% | -58% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5950 | 25 | 2% | 1% | -22% | -79% | -78% |
| 0.05–0.1% | 6520 | 26 | 3% | 2% | -36% | -91% | -91% |
| 0.1–0.2% | 10173 | 36 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 12949 | 56 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 5472 | 24 | 7% | 3% | -54% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16675 | 51 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 16354 | 82 | 4% | 2% | -43% | -86% | -85% |
| Afternoon (12–6pm) | 16940 | 73 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 19271 | 51 | 4% | 2% | -69% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,072 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/27 2:14:57 AM | DOGE | UP | 2 sec | -0.088% | 0¢ | ❌ Lost | $0.00 |
| 11/27 2:14:57 AM | BTC | UP | 2 sec | -0.051% | 0¢ | ❌ Lost | $0.00 |
| 11/27 2:14:41 AM | SILVER | DOWN | 19 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/27 2:14:41 AM | AUDUSD | DOWN | 19 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 11/27 2:14:41 AM | EURUSD | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 2:14:41 AM | ETH | UP | 19 sec | -0.106% | 0¢ | ❌ Lost | $0.00 |
| 11/27 2:14:41 AM | BNB | UP | 19 sec | -0.112% | 0¢ | ❌ Lost | $0.00 |
| 11/27 2:14:21 AM | NEAR | DOWN | 39 sec | +0.022% | 0¢ | ❌ Lost | $0.00 |
| 11/27 2:14:21 AM | USDCAD | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 2:14:05 AM | USDJPY | DOWN | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 2:14:05 AM | USDMXN | UP | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 2:13:34 AM | XRP | DOWN | 86 sec | +0.154% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 2:13:34 AM | HYPE | DOWN | 86 sec | +0.122% | 0¢ | ❌ Lost | -$0.15 |
| 11/27 2:13:34 AM | ZEC | DOWN | 86 sec | +0.393% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 2:13:15 AM | BRENT | UP | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/27 2:12:43 AM | PALLADIUM | UP | 2.3 min | — | 2¢ | ❌ Lost | -$0.15 |
| 11/27 2:12:27 AM | SOL | DOWN | 2.5 min | +0.291% | 0¢ | ❌ Lost | -$0.15 |
| 11/27 2:11:20 AM | GOLD | DOWN | 3.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/27 2:09:52 AM | NATGAS | UP | 5.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 1:59:44 AM | USDJPY | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 1:59:44 AM | ETH | DOWN | 15 sec | -0.002% | 0¢ | ❌ Lost | $0.00 |
| 11/27 1:59:24 AM | NATGAS | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 1:59:24 AM | GBPUSD | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 1:59:24 AM | PALLADIUM | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 1:59:24 AM | GOLD | DOWN | 36 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/27 1:59:24 AM | BNB | UP | 36 sec | -0.090% | 0¢ | ❌ Lost | -$0.15 |
| 11/27 1:58:52 AM | 2YRRATE | DOWN | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 1:58:37 AM | AUDUSD | DOWN | 82 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 1:58:37 AM | DOGE | DOWN | 82 sec | +0.112% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 1:58:37 AM | BTC | UP | 82 sec | -0.113% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
