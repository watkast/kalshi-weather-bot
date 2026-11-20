# 15-Minute 1¢ Study

*Updated Fri Nov 20, 3:53 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4607 finished bets | 1% | $207.75 | +41% | +4.51¢ | $75.90 / $131.85 |

*Expect about **86 buys a day** (~$12.88/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4350 | $107.20 | +23% |
| Volatility model ≥ 2%, hold to the close | 8614 | $59.10 | +6% |
| Momentum model ≥ 2%, hold to the close | 7149 | -$20.25 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 63440 | 63406 | 245 (0%) | 1.07% | -$4,281.65 (-56%) | Hold to the close: -$4,281.65 (-56%) |

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
| Volatility model | 37485 | 4.5% | 0.4% (157) | -633% | ❌ Worse |
| Momentum model | 37485 | 4.4% | 0.4% (157) | -658% | ❌ Worse |
| Mean-reversion model | 37485 | 7.9% | 0.4% (157) | -769% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 37485 | 157 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8614 | 78 | +6% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4607 | 51 | +41% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 2649 | 30 | +66% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 7149 | 57 | -2% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4350 | 41 | +23% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2836 | 26 | +31% | -67% | -67% | -62% |
| Mean-reversion model ≥ 2% | 15310 | 109 | -22% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10648 | 89 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7074 | 64 | +3% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 37691 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15250 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10465 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 63406 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 245 | 0% | -$4,281.65 | -56% | — |
| Sell at 2¢ | 2565 | 4% | -$6,750.75 | -88% | 47 sec |
| Sell at 3¢ | 1730 | 3% | -$6,742.95 | -87% | 48 sec |
| Sell at 5¢ | 1181 | 2% | -$6,622.00 | -86% | 63 sec |
| Sell at 10¢ | 722 | 1% | -$6,359.83 | -82% | 65 sec |
| Sell at 25¢ | 387 | 1% | -$5,870.68 | -76% | 80 sec |
| Sell at 50¢ | 251 | 0% | -$5,303.40 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3260 | 17 | 10% | 4% | -51% | -82% | -83% |
| 2–5 min | 20579 | 110 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 15846 | 55 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 23708 | 63 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4214 | 19 | 5% | 2% | -40% | -88% | -87% |
| SOL | 4210 | 19 | 4% | 2% | -42% | -86% | -86% |
| HYPE | 4205 | 14 | 4% | 2% | -57% | -89% | -88% |
| DOGE | 4194 | 11 | 4% | 2% | -67% | -90% | -89% |
| BNB | 4193 | 21 | 5% | 2% | -36% | -85% | -85% |
| ETH | 4189 | 19 | 7% | 3% | -43% | -82% | -82% |
| BTC | 4170 | 22 | 5% | 2% | -28% | -86% | -88% |
| NEAR | 4165 | 18 | 5% | 2% | -43% | -85% | -86% |
| XRP | 4151 | 16 | 3% | 2% | -51% | -89% | -88% |
| GOLD | 2265 | 8 | 5% | 2% | -57% | -82% | -84% |
| WTI | 2244 | 7 | 4% | 1% | -62% | -91% | -92% |
| SILVER | 2209 | 9 | 5% | 2% | -51% | -83% | -83% |
| PLATINUM | 2012 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 1968 | 7 | 3% | 1% | -67% | -91% | -90% |
| GBPUSD | 1900 | 8 | 2% | 1% | -61% | -96% | -95% |
| COPPER | 1895 | 6 | 2% | 1% | -70% | -77% | -77% |
| USDJPY | 1855 | 6 | 2% | 1% | -70% | -96% | -96% |
| NATGAS | 1852 | 10 | 2% | 1% | -50% | -76% | -76% |
| PALLADIUM | 1808 | 4 | 1% | 1% | -79% | -93% | -93% |
| AUDUSD | 1406 | 6 | 2% | 1% | -60% | -90% | -90% |
| USDCAD | 1340 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 965 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 499 | 2 | 3% | 1% | -63% | -76% | -74% |
| 2YRRATE | 476 | 4 | 4% | 2% | -22% | -54% | -53% |
| 30YRRATE | 462 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 451 | 2 | 4% | 2% | -59% | -94% | -95% |
| INX | 108 | 1 | 2% | 1% | -14% | -97% | -98% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 32397 | 126 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 31009 | 119 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5577 | 25 | 2% | 1% | -19% | -78% | -78% |
| 0.05–0.1% | 6080 | 24 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 9414 | 34 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 11728 | 53 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 4883 | 23 | 7% | 3% | -51% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15327 | 48 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 15289 | 81 | 4% | 2% | -40% | -85% | -85% |
| Afternoon (12–6pm) | 15494 | 66 | 4% | 2% | -50% | -87% | -87% |
| Evening (6pm–12am) | 17296 | 50 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,970 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/20 3:44:52 PM | NATGAS | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 3:44:22 PM | NEAR | DOWN | 38 sec | +0.080% | 0¢ | ❌ Lost | -$0.15 |
| 11/20 3:44:06 PM | ETH | DOWN | 54 sec | +0.167% | 0¢ | ❌ Lost | $0.00 |
| 11/20 3:44:06 PM | XRP | DOWN | 54 sec | +0.197% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 3:43:51 PM | BTC | DOWN | 68 sec | +0.163% | 0¢ | ❌ Lost | $0.00 |
| 11/20 3:43:51 PM | DOGE | DOWN | 68 sec | +0.278% | 0¢ | ❌ Lost | $0.00 |
| 11/20 3:43:51 PM | HYPE | DOWN | 68 sec | +0.242% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 3:43:35 PM | BNB | DOWN | 84 sec | +0.115% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 3:43:35 PM | BRENT | UP | 84 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 3:43:19 PM | SOL | DOWN | 1.7 min | +0.253% | 0¢ | ❌ Lost | -$0.15 |
| 11/20 3:40:29 PM | ZEC | DOWN | 4.5 min | +1.175% | 1¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
