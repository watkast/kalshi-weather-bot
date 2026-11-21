# 15-Minute 1¢ Study

*Updated Sat Nov 21, 12:43 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4639 finished bets | 1% | $204.45 | +40% | +4.41¢ | $74.25 / $130.20 |

*Expect about **86 buys a day** (~$12.88/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4393 | $102.55 | +22% |
| Volatility model ≥ 2%, hold to the close | 8672 | $52.80 | +5% |
| Momentum model ≥ 2%, hold to the close | 7208 | -$26.55 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 63764 | 63729 | 245 (0%) | 1.07% | -$4,312.40 (-56%) | Hold to the close: -$4,312.40 (-56%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 37785 | 4.5% | 0.4% (157) | -638% | ❌ Worse |
| Momentum model | 37785 | 4.4% | 0.4% (157) | -662% | ❌ Worse |
| Mean-reversion model | 37785 | 7.8% | 0.4% (157) | -774% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 37785 | 157 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8672 | 78 | +5% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4639 | 51 | +40% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 2671 | 30 | +65% | -64% | -62% | -59% |
| Momentum model ≥ 2% | 7208 | 57 | -3% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4393 | 41 | +22% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2860 | 26 | +30% | -67% | -67% | -63% |
| Mean-reversion model ≥ 2% | 15412 | 109 | -22% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10709 | 89 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7115 | 64 | +3% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 37991 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15273 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10465 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 63729 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 245 | 0% | -$4,312.40 | -56% | — |
| Sell at 2¢ | 2574 | 4% | -$6,779.16 | -88% | 47 sec |
| Sell at 3¢ | 1733 | 3% | -$6,772.53 | -87% | 48 sec |
| Sell at 5¢ | 1181 | 2% | -$6,652.75 | -86% | 63 sec |
| Sell at 10¢ | 722 | 1% | -$6,390.58 | -83% | 65 sec |
| Sell at 25¢ | 387 | 1% | -$5,901.43 | -76% | 80 sec |
| Sell at 50¢ | 251 | 0% | -$5,334.15 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3292 | 17 | 10% | 4% | -51% | -82% | -83% |
| 2–5 min | 20661 | 110 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 15918 | 55 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 23845 | 63 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4248 | 19 | 5% | 2% | -41% | -88% | -87% |
| SOL | 4241 | 19 | 4% | 2% | -42% | -86% | -86% |
| HYPE | 4239 | 14 | 5% | 2% | -58% | -89% | -88% |
| DOGE | 4228 | 11 | 4% | 2% | -67% | -90% | -89% |
| BNB | 4228 | 21 | 5% | 2% | -37% | -86% | -85% |
| ETH | 4223 | 19 | 7% | 3% | -44% | -82% | -82% |
| BTC | 4201 | 22 | 5% | 2% | -28% | -86% | -88% |
| NEAR | 4199 | 18 | 5% | 2% | -44% | -85% | -86% |
| XRP | 4184 | 16 | 3% | 2% | -51% | -89% | -88% |
| GOLD | 2265 | 8 | 5% | 2% | -57% | -82% | -84% |
| WTI | 2257 | 7 | 4% | 1% | -62% | -91% | -92% |
| SILVER | 2209 | 9 | 5% | 2% | -51% | -83% | -83% |
| PLATINUM | 2012 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 1968 | 7 | 3% | 1% | -67% | -91% | -90% |
| GBPUSD | 1900 | 8 | 2% | 1% | -61% | -96% | -95% |
| COPPER | 1895 | 6 | 2% | 1% | -70% | -77% | -77% |
| NATGAS | 1858 | 10 | 2% | 1% | -50% | -76% | -76% |
| USDJPY | 1855 | 6 | 2% | 1% | -70% | -96% | -96% |
| PALLADIUM | 1808 | 4 | 1% | 1% | -79% | -93% | -93% |
| AUDUSD | 1406 | 6 | 2% | 1% | -60% | -90% | -90% |
| USDCAD | 1340 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 969 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 499 | 2 | 3% | 1% | -63% | -76% | -74% |
| 2YRRATE | 476 | 4 | 4% | 2% | -22% | -54% | -53% |
| 30YRRATE | 462 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 451 | 2 | 4% | 2% | -59% | -94% | -95% |
| INX | 108 | 1 | 2% | 1% | -14% | -97% | -98% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 32574 | 126 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 31155 | 119 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5603 | 25 | 2% | 1% | -19% | -78% | -78% |
| 0.05–0.1% | 6108 | 24 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 9466 | 34 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 11819 | 53 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 4986 | 23 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15343 | 48 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 15289 | 81 | 4% | 2% | -40% | -85% | -85% |
| Afternoon (12–6pm) | 15576 | 66 | 4% | 2% | -50% | -87% | -87% |
| Evening (6pm–12am) | 17521 | 50 | 4% | 2% | -67% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,029 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/21 12:43:09 AM | HYPE | UP | 1.8 min | -0.559% | — | In play | — |
| 11/21 12:29:37 AM | BTC | UP | 23 sec | -0.105% | 0¢ | ❌ Lost | $0.00 |
| 11/21 12:29:37 AM | DOGE | UP | 23 sec | -0.144% | 0¢ | ❌ Lost | $0.00 |
| 11/21 12:29:37 AM | BNB | UP | 23 sec | -0.146% | 0¢ | ❌ Lost | $0.00 |
| 11/21 12:29:37 AM | ZEC | DOWN | 23 sec | -0.002% | 0¢ | ❌ Lost | $0.00 |
| 11/21 12:29:21 AM | NEAR | UP | 39 sec | -0.297% | 0¢ | ❌ Lost | $0.00 |
| 11/21 12:29:06 AM | HYPE | DOWN | 53 sec | +0.375% | 0¢ | ❌ Lost | $0.00 |
| 11/21 12:28:50 AM | XRP | UP | 69 sec | -0.234% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 12:14:44 AM | HYPE | DOWN | 16 sec | +0.056% | 0¢ | ❌ Lost | $0.00 |
| 11/21 12:14:28 AM | XRP | UP | 32 sec | -0.145% | 0¢ | ❌ Lost | -$0.15 |
| 11/21 12:14:28 AM | BTC | DOWN | 32 sec | +0.311% | 0¢ | ❌ Lost | $0.00 |
| 11/21 12:14:28 AM | BNB | DOWN | 32 sec | +0.129% | 0¢ | ❌ Lost | $0.00 |
| 11/21 12:14:13 AM | ETH | UP | 46 sec | -0.440% | 0¢ | ❌ Lost | $0.00 |
| 11/21 12:14:13 AM | ZEC | UP | 46 sec | -0.479% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 12:13:23 AM | DOGE | UP | 1.6 min | -0.621% | 0¢ | ❌ Lost | $0.00 |
| 11/21 12:13:23 AM | NEAR | UP | 1.6 min | -0.869% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 12:13:08 AM | SOL | UP | 1.9 min | -0.695% | 0¢ | ❌ Lost | -$0.15 |
| 11/20 11:58:51 PM | HYPE | DOWN | 69 sec | +0.707% | 0¢ | ❌ Lost | -$0.15 |
| 11/20 11:57:00 PM | ZEC | DOWN | 3.0 min | +1.654% | 0¢ | ❌ Lost | -$0.15 |
| 11/20 11:55:53 PM | SOL | DOWN | 4.1 min | +0.950% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 11:55:19 PM | BTC | DOWN | 4.7 min | +0.990% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 11:55:19 PM | BNB | DOWN | 4.7 min | +1.128% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 11:54:48 PM | NEAR | DOWN | 5.2 min | +1.786% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 11:52:40 PM | ETH | DOWN | 7.3 min | +2.285% | 2¢ | ❌ Lost | -$0.15 |
| 11/20 11:52:09 PM | XRP | DOWN | 7.8 min | +1.570% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 11:51:18 PM | DOGE | DOWN | 8.7 min | +1.978% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 11:40:41 PM | ZEC | DOWN | 4.3 min | +2.450% | 0¢ | ❌ Lost | -$0.15 |
| 11/20 11:40:09 PM | XRP | DOWN | 4.8 min | +1.046% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 11:39:54 PM | ETH | DOWN | 5.1 min | +0.921% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 11:39:54 PM | DOGE | DOWN | 5.1 min | +1.193% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
