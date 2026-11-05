# 15-Minute 1¢ Study

*Updated Thu Nov 5, 4:59 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3727 finished bets | 1% | $132.00 | +32% | +3.54¢ | $87.00 / $45.00 |

*Expect about **96 buys a day** (~$14.44/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3466 | $59.30 | +16% |
| Volatility model ≥ 2%, hold to the close | 6895 | $37.45 | +5% |
| Momentum model ≥ 2%, hold to the close | 5692 | -$38.45 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 47078 | 47053 | 173 (0%) | 1.07% | -$3,315.20 (-58%) | Hold to the close: -$3,315.20 (-58%) |

*In play or awaiting result: 17. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 28517 | 4.7% | 0.4% (111) | -685% | ❌ Worse |
| Momentum model | 28517 | 4.6% | 0.4% (111) | -712% | ❌ Worse |
| Mean-reversion model | 28517 | 8.1% | 0.4% (111) | -834% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 28517 | 111 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6895 | 62 | +5% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3727 | 39 | +32% | -77% | -75% | -71% |
| Volatility model ≥ 10% | 2129 | 24 | +62% | -71% | -70% | -66% |
| Momentum model ≥ 2% | 5692 | 44 | -6% | -82% | -81% | -78% |
| Momentum model ≥ 5% | 3466 | 31 | +16% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2266 | 20 | +24% | -75% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11789 | 80 | -25% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8270 | 69 | -7% | -82% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5538 | 49 | +1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 28722 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11276 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7055 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 47053 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 173 | 0% | -$3,315.20 | -58% | — |
| Sell at 2¢ | 1843 | 4% | -$5,006.02 | -87% | 47 sec |
| Sell at 3¢ | 1257 | 3% | -$4,994.97 | -87% | 49 sec |
| Sell at 5¢ | 868 | 2% | -$4,893.00 | -85% | 63 sec |
| Sell at 10¢ | 526 | 1% | -$4,684.14 | -82% | 65 sec |
| Sell at 25¢ | 274 | 1% | -$4,354.26 | -76% | 83 sec |
| Sell at 50¢ | 177 | 0% | -$3,968.45 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2323 | 10 | 10% | 4% | -59% | -82% | -83% |
| 2–5 min | 15150 | 81 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 11838 | 40 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 17730 | 42 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3217 | 13 | 5% | 2% | -48% | -88% | -88% |
| SOL | 3211 | 12 | 4% | 2% | -53% | -90% | -90% |
| BNB | 3207 | 17 | 5% | 2% | -33% | -85% | -84% |
| HYPE | 3204 | 10 | 5% | 2% | -61% | -89% | -88% |
| DOGE | 3191 | 6 | 4% | 2% | -76% | -90% | -90% |
| ETH | 3189 | 12 | 7% | 3% | -54% | -85% | -85% |
| NEAR | 3172 | 16 | 5% | 2% | -35% | -84% | -84% |
| BTC | 3170 | 15 | 5% | 2% | -36% | -88% | -89% |
| XRP | 3161 | 12 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1738 | 5 | 5% | 2% | -65% | -81% | -82% |
| WTI | 1691 | 5 | 4% | 1% | -64% | -92% | -92% |
| SILVER | 1684 | 8 | 5% | 2% | -44% | -82% | -81% |
| PLATINUM | 1517 | 4 | 2% | 1% | -75% | -96% | -96% |
| EURUSD | 1457 | 3 | 2% | 1% | -81% | -89% | -89% |
| COPPER | 1434 | 6 | 2% | 1% | -61% | -71% | -71% |
| GBPUSD | 1388 | 4 | 2% | 1% | -73% | -96% | -96% |
| NATGAS | 1375 | 8 | 2% | 1% | -46% | -76% | -75% |
| PALLADIUM | 1364 | 3 | 1% | 1% | -79% | -91% | -91% |
| USDJPY | 1363 | 5 | 2% | 1% | -66% | -97% | -97% |
| AUDUSD | 911 | 4 | 2% | 1% | -59% | -87% | -87% |
| USDCAD | 889 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 473 | 0 | 1% | 1% | -100% | -97% | -97% |
| 10YRRATE | 280 | 1 | 4% | 1% | -67% | -59% | -57% |
| 30YRRATE | 265 | 0 | 2% | 1% | -100% | -97% | -95% |
| 2YRRATE | 261 | 3 | 4% | 1% | +7% | -22% | -21% |
| 5YRRATE | 240 | 1 | 5% | 2% | -61% | -92% | -95% |
| INX | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 23888 | 92 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 23165 | 81 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4599 | 22 | 2% | 1% | -16% | -83% | -82% |
| 0.05–0.1% | 4872 | 18 | 3% | 2% | -44% | -91% | -90% |
| 0.1–0.2% | 7402 | 26 | 4% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 8583 | 34 | 6% | 3% | -56% | -87% | -86% |
| Over 0.5% | 3258 | 13 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11506 | 40 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11661 | 51 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 11260 | 41 | 4% | 2% | -57% | -86% | -86% |
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
| 11/5 4:58:53 PM | USDCAD | DOWN | 66 sec | — | — | In play | — |
| 11/5 4:58:37 PM | HYPE | UP | 82 sec | -0.331% | — | In play | — |
| 11/5 4:58:37 PM | PALLADIUM | UP | 82 sec | — | — | In play | — |
| 11/5 4:58:21 PM | SILVER | UP | 1.6 min | — | — | In play | — |
| 11/5 4:58:05 PM | NATGAS | UP | 1.9 min | — | — | In play | — |
| 11/5 4:57:00 PM | XRP | UP | 3.0 min | -0.339% | — | In play | — |
| 11/5 4:56:42 PM | GOLD | UP | 3.3 min | — | — | In play | — |
| 11/5 4:55:39 PM | PLATINUM | UP | 4.3 min | — | — | In play | — |
| 11/5 4:44:45 PM | SILVER | DOWN | 14 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/5 4:44:45 PM | XRP | UP | 14 sec | -0.058% | 0¢ | ❌ Lost | $0.00 |
| 11/5 4:44:45 PM | NEAR | UP | 14 sec | -0.156% | 0¢ | ❌ Lost | $0.00 |
| 11/5 4:44:45 PM | BNB | DOWN | 14 sec | -0.015% | 0¢ | ❌ Lost | $0.00 |
| 11/5 4:44:29 PM | WTI | UP | 31 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/5 4:44:29 PM | SOL | DOWN | 31 sec | +0.030% | 0¢ | ❌ Lost | -$0.15 |
| 11/5 4:44:29 PM | AUDUSD | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 4:44:11 PM | BRENT | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 4:43:55 PM | DOGE | DOWN | 65 sec | +0.176% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 4:43:39 PM | BTC | DOWN | 81 sec | +0.167% | 0¢ | ❌ Lost | $0.00 |
| 11/5 4:43:24 PM | ZEC | DOWN | 1.6 min | +0.384% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 4:43:24 PM | ETH | DOWN | 1.6 min | +0.207% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 4:43:06 PM | EURUSD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 4:43:06 PM | COPPER | UP | 1.9 min | — | 6¢ | ❌ Lost | -$0.15 |
| 11/5 4:42:34 PM | GBPUSD | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 4:42:01 PM | GOLD | UP | 3.0 min | — | 63¢ | ❌ Lost | -$0.15 |
| 11/5 4:41:45 PM | USDJPY | DOWN | 3.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/5 4:41:29 PM | USDCAD | DOWN | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 4:11:11 PM | GBPUSD | DOWN | 3.8 min | — | — | ❌ Lost | -$0.15 |
| 11/5 4:10:55 PM | ETH | UP | 4.1 min | -0.975% | — | ❌ Lost | -$0.15 |
| 11/5 4:10:24 PM | SOL | UP | 4.6 min | -1.028% | — | ❌ Lost | -$0.15 |
| 11/5 4:10:08 PM | XRP | UP | 4.8 min | -1.267% | — | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
