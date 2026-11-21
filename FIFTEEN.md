# 15-Minute 1¢ Study

*Updated Fri Nov 20, 9:57 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4631 finished bets | 1% | $205.50 | +40% | +4.44¢ | $74.40 / $131.10 |

*Expect about **86 buys a day** (~$12.89/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4382 | $103.75 | +22% |
| Volatility model ≥ 2%, hold to the close | 8652 | $55.35 | +5% |
| Momentum model ≥ 2%, hold to the close | 7187 | -$24.15 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 63674 | 63635 | 245 (0%) | 1.07% | -$4,303.10 (-56%) | Hold to the close: -$4,303.10 (-56%) |

*In play or awaiting result: 11. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 37693 | 4.5% | 0.4% (157) | -637% | ❌ Worse |
| Momentum model | 37693 | 4.4% | 0.4% (157) | -662% | ❌ Worse |
| Mean-reversion model | 37693 | 7.8% | 0.4% (157) | -773% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 37693 | 157 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8652 | 78 | +5% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4631 | 51 | +40% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 2667 | 30 | +65% | -64% | -62% | -59% |
| Momentum model ≥ 2% | 7187 | 57 | -3% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4382 | 41 | +22% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2854 | 26 | +30% | -67% | -67% | -63% |
| Mean-reversion model ≥ 2% | 15369 | 109 | -22% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10682 | 89 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7097 | 64 | +3% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 37899 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15271 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10465 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 63635 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 245 | 0% | -$4,303.10 | -56% | — |
| Sell at 2¢ | 2573 | 4% | -$6,770.12 | -88% | 47 sec |
| Sell at 3¢ | 1733 | 3% | -$6,763.23 | -87% | 48 sec |
| Sell at 5¢ | 1181 | 2% | -$6,643.45 | -86% | 63 sec |
| Sell at 10¢ | 722 | 1% | -$6,381.28 | -83% | 65 sec |
| Sell at 25¢ | 387 | 1% | -$5,892.13 | -76% | 80 sec |
| Sell at 50¢ | 251 | 0% | -$5,324.85 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3279 | 17 | 10% | 4% | -51% | -82% | -83% |
| 2–5 min | 20630 | 110 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 15898 | 55 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 23815 | 63 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4237 | 19 | 5% | 2% | -40% | -88% | -87% |
| SOL | 4233 | 19 | 4% | 2% | -42% | -86% | -86% |
| HYPE | 4229 | 14 | 5% | 2% | -58% | -89% | -88% |
| DOGE | 4217 | 11 | 4% | 2% | -67% | -90% | -89% |
| BNB | 4217 | 21 | 5% | 2% | -37% | -86% | -85% |
| ETH | 4213 | 19 | 7% | 3% | -44% | -82% | -82% |
| BTC | 4191 | 22 | 5% | 2% | -28% | -86% | -88% |
| NEAR | 4188 | 18 | 5% | 2% | -44% | -85% | -86% |
| XRP | 4174 | 16 | 3% | 2% | -51% | -89% | -88% |
| GOLD | 2265 | 8 | 5% | 2% | -57% | -82% | -84% |
| WTI | 2256 | 7 | 4% | 1% | -62% | -91% | -92% |
| SILVER | 2209 | 9 | 5% | 2% | -51% | -83% | -83% |
| PLATINUM | 2012 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 1968 | 7 | 3% | 1% | -67% | -91% | -90% |
| GBPUSD | 1900 | 8 | 2% | 1% | -61% | -96% | -95% |
| COPPER | 1895 | 6 | 2% | 1% | -70% | -77% | -77% |
| NATGAS | 1857 | 10 | 2% | 1% | -50% | -76% | -76% |
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
| UP (bought YES) | 32536 | 126 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 31099 | 119 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5598 | 25 | 2% | 1% | -19% | -78% | -78% |
| 0.05–0.1% | 6104 | 24 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 9457 | 34 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 11794 | 53 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 4937 | 23 | 7% | 3% | -51% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15327 | 48 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 15289 | 81 | 4% | 2% | -40% | -85% | -85% |
| Afternoon (12–6pm) | 15576 | 66 | 4% | 2% | -50% | -87% | -87% |
| Evening (6pm–12am) | 17443 | 50 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,011 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/20 9:57:31 PM | NEAR | UP | 2.5 min | -1.326% | — | In play | — |
| 11/20 9:57:00 PM | BTC | DOWN | 3.0 min | +0.680% | — | In play | — |
| 11/20 9:57:00 PM | HYPE | DOWN | 3.0 min | +0.962% | — | In play | — |
| 11/20 9:56:43 PM | ETH | DOWN | 3.3 min | +0.621% | — | In play | — |
| 11/20 9:54:50 PM | SOL | DOWN | 5.2 min | +0.926% | — | In play | — |
| 11/20 9:44:56 PM | BNB | UP | 4 sec | -0.014% | 0¢ | ❌ Lost | $0.00 |
| 11/20 9:44:40 PM | ETH | DOWN | 20 sec | +0.096% | 0¢ | ❌ Lost | $0.00 |
| 11/20 9:44:24 PM | BTC | DOWN | 36 sec | +0.245% | 0¢ | ❌ Lost | $0.00 |
| 11/20 9:44:24 PM | WTI | UP | 36 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/20 9:44:24 PM | HYPE | DOWN | 36 sec | +0.319% | 0¢ | ❌ Lost | $0.00 |
| 11/20 9:43:35 PM | SOL | DOWN | 84 sec | +0.380% | 4¢ | ❌ Lost | -$0.15 |
| 11/20 9:43:35 PM | ZEC | DOWN | 84 sec | +0.472% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 9:43:03 PM | NEAR | DOWN | 1.9 min | +0.622% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 9:42:16 PM | DOGE | DOWN | 2.7 min | +0.549% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 9:42:00 PM | XRP | DOWN | 3.0 min | +0.885% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 9:29:56 PM | WTI | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 9:29:56 PM | BRENT | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 9:28:53 PM | BNB | UP | 67 sec | -0.466% | 0¢ | ❌ Lost | $0.00 |
| 11/20 9:28:37 PM | BTC | UP | 83 sec | -0.465% | 0¢ | ❌ Lost | $0.00 |
| 11/20 9:28:37 PM | DOGE | UP | 83 sec | -0.784% | 0¢ | ❌ Lost | $0.00 |
| 11/20 9:28:21 PM | ETH | UP | 1.6 min | -0.605% | 0¢ | ❌ Lost | $0.00 |
| 11/20 9:28:21 PM | NEAR | UP | 1.6 min | -1.177% | 0¢ | ❌ Lost | -$0.15 |
| 11/20 9:28:21 PM | XRP | UP | 1.6 min | -0.901% | 0¢ | ❌ Lost | $0.00 |
| 11/20 9:27:48 PM | SOL | UP | 2.2 min | -0.659% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 9:27:48 PM | HYPE | UP | 2.2 min | -0.885% | 0¢ | ❌ Lost | -$0.15 |
| 11/20 9:27:16 PM | ZEC | UP | 2.7 min | -1.305% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 9:14:40 PM | HYPE | UP | 20 sec | -0.398% | 0¢ | ❌ Lost | -$0.15 |
| 11/20 9:14:24 PM | WTI | UP | 36 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/20 9:14:24 PM | BRENT | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 9:14:24 PM | XRP | UP | 36 sec | -0.455% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
