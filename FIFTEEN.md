# 15-Minute 1¢ Study

*Updated Fri Nov 20, 3:32 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4605 finished bets | 1% | $208.05 | +41% | +4.52¢ | $76.05 / $132.00 |

*Expect about **86 buys a day** (~$12.88/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4349 | $107.35 | +23% |
| Volatility model ≥ 2%, hold to the close | 8611 | $59.40 | +6% |
| Momentum model ≥ 2%, hold to the close | 7147 | -$19.95 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 63429 | 63395 | 245 (0%) | 1.07% | -$4,280.45 (-56%) | Hold to the close: -$4,280.45 (-56%) |

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
| Volatility model | 37476 | 4.5% | 0.4% (157) | -633% | ❌ Worse |
| Momentum model | 37476 | 4.4% | 0.4% (157) | -658% | ❌ Worse |
| Mean-reversion model | 37476 | 7.9% | 0.4% (157) | -769% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 37476 | 157 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8611 | 78 | +6% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4605 | 51 | +41% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 2648 | 30 | +66% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 7147 | 57 | -2% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4349 | 41 | +23% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2836 | 26 | +31% | -67% | -67% | -62% |
| Mean-reversion model ≥ 2% | 15303 | 109 | -22% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10644 | 89 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7071 | 64 | +3% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 37682 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15248 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10465 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 63395 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 245 | 0% | -$4,280.45 | -56% | — |
| Sell at 2¢ | 2565 | 4% | -$6,749.55 | -88% | 47 sec |
| Sell at 3¢ | 1730 | 3% | -$6,741.75 | -87% | 48 sec |
| Sell at 5¢ | 1181 | 2% | -$6,620.80 | -86% | 63 sec |
| Sell at 10¢ | 722 | 1% | -$6,358.63 | -82% | 65 sec |
| Sell at 25¢ | 387 | 1% | -$5,869.48 | -76% | 80 sec |
| Sell at 50¢ | 251 | 0% | -$5,302.20 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3260 | 17 | 10% | 4% | -51% | -82% | -83% |
| 2–5 min | 20578 | 110 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 15840 | 55 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 23704 | 63 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4213 | 19 | 5% | 2% | -40% | -88% | -87% |
| SOL | 4209 | 19 | 4% | 2% | -42% | -86% | -86% |
| HYPE | 4204 | 14 | 4% | 2% | -57% | -89% | -88% |
| DOGE | 4193 | 11 | 4% | 2% | -67% | -90% | -89% |
| BNB | 4192 | 21 | 5% | 2% | -36% | -85% | -85% |
| ETH | 4188 | 19 | 7% | 3% | -43% | -82% | -82% |
| BTC | 4169 | 22 | 5% | 2% | -28% | -86% | -88% |
| NEAR | 4164 | 18 | 5% | 2% | -43% | -85% | -86% |
| XRP | 4150 | 16 | 3% | 2% | -51% | -89% | -88% |
| GOLD | 2265 | 8 | 5% | 2% | -57% | -82% | -84% |
| WTI | 2244 | 7 | 4% | 1% | -62% | -91% | -92% |
| SILVER | 2209 | 9 | 5% | 2% | -51% | -83% | -83% |
| PLATINUM | 2012 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 1968 | 7 | 3% | 1% | -67% | -91% | -90% |
| GBPUSD | 1900 | 8 | 2% | 1% | -61% | -96% | -95% |
| COPPER | 1895 | 6 | 2% | 1% | -70% | -77% | -77% |
| USDJPY | 1855 | 6 | 2% | 1% | -70% | -96% | -96% |
| NATGAS | 1851 | 10 | 2% | 1% | -50% | -76% | -76% |
| PALLADIUM | 1808 | 4 | 1% | 1% | -79% | -93% | -93% |
| AUDUSD | 1406 | 6 | 2% | 1% | -60% | -90% | -90% |
| USDCAD | 1340 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 964 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 499 | 2 | 3% | 1% | -63% | -76% | -74% |
| 2YRRATE | 476 | 4 | 4% | 2% | -22% | -54% | -53% |
| 30YRRATE | 462 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 451 | 2 | 4% | 2% | -59% | -94% | -95% |
| INX | 108 | 1 | 2% | 1% | -14% | -97% | -98% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 32396 | 126 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 30999 | 119 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5577 | 25 | 2% | 1% | -19% | -78% | -78% |
| 0.05–0.1% | 6079 | 24 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 9410 | 34 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 11725 | 53 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 4882 | 23 | 7% | 3% | -51% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15327 | 48 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 15289 | 81 | 4% | 2% | -40% | -85% | -85% |
| Afternoon (12–6pm) | 15483 | 66 | 4% | 2% | -50% | -87% | -87% |
| Evening (6pm–12am) | 17296 | 50 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,968 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/20 3:29:51 PM | ETH | UP | 8 sec | -0.081% | 0¢ | ❌ Lost | $0.00 |
| 11/20 3:29:51 PM | DOGE | DOWN | 8 sec | +0.070% | 0¢ | ❌ Lost | $0.00 |
| 11/20 3:29:51 PM | NEAR | DOWN | 8 sec | -0.031% | 0¢ | ❌ Lost | $0.00 |
| 11/20 3:29:23 PM | BTC | UP | 36 sec | -0.124% | 0¢ | ❌ Lost | $0.00 |
| 11/20 3:29:23 PM | WTI | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 3:29:23 PM | HYPE | UP | 36 sec | -0.117% | 0¢ | ❌ Lost | $0.00 |
| 11/20 3:28:21 PM | XRP | DOWN | 1.6 min | +0.242% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 3:27:50 PM | BNB | UP | 2.2 min | -0.277% | 4¢ | ❌ Lost | -$0.15 |
| 11/20 3:25:04 PM | ZEC | UP | 4.9 min | -1.418% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 3:14:56 PM | BRENT | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 3:14:40 PM | NATGAS | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 3:14:24 PM | SOL | DOWN | 36 sec | +0.120% | 0¢ | ❌ Lost | $0.00 |
| 11/20 3:13:54 PM | XRP | DOWN | 66 sec | +0.253% | 0¢ | ❌ Lost | $0.00 |
| 11/20 3:13:38 PM | ETH | DOWN | 82 sec | +0.192% | 0¢ | ❌ Lost | -$0.15 |
| 11/20 3:13:38 PM | BTC | DOWN | 82 sec | +0.128% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 3:13:22 PM | BNB | DOWN | 1.6 min | +0.202% | 0¢ | ❌ Lost | $0.00 |
| 11/20 3:13:22 PM | HYPE | DOWN | 1.6 min | +0.488% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 3:12:01 PM | ZEC | DOWN | 3.0 min | +0.829% | 2¢ | ❌ Lost | -$0.15 |
| 11/20 3:12:01 PM | DOGE | DOWN | 3.0 min | +0.569% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 3:11:15 PM | NEAR | DOWN | 3.8 min | +0.790% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 2:59:46 PM | DOGE | UP | 13 sec | -0.048% | 0¢ | ❌ Lost | $0.00 |
| 11/20 2:59:46 PM | NEAR | UP | 13 sec | -0.141% | 0¢ | ❌ Lost | $0.00 |
| 11/20 2:59:15 PM | SOL | DOWN | 45 sec | +0.104% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 2:59:03 PM | XRP | UP | 57 sec | -0.220% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 2:58:47 PM | 5YRRATE | UP | 73 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/20 2:58:47 PM | AUDUSD | DOWN | 73 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 2:58:30 PM | USDJPY | UP | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 2:58:14 PM | NATGAS | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 2:58:14 PM | GBPUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 2:58:02 PM | SILVER | DOWN | 1.9 min | — | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
