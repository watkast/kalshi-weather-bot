# 15-Minute 1¢ Study

*Updated Wed Sep 30, 6:08 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 119 finished bets | 2% | $10.45 | +60% | +8.78¢ | $19.15 / -$8.70 |

*Expect about **41 buys a day** (~$6.17/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 205 | $5.50 | +24% |
| Volatility model ≥ 5%, sell at 25¢ | 202 | $1.73 | +8% |
| Volatility model ≥ 5%, sell at 10¢ | 202 | $0.97 | +4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 3659 | 3653 | 14 (0%) | 1.07% | -$250.55 (-56%) | Hold to the close: -$250.55 (-56%) |

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
| Volatility model | 2089 | 3.2% | 0.3% (6) | -519% | ❌ Worse |
| Momentum model | 2089 | 3.3% | 0.3% (6) | -562% | ❌ Worse |
| Mean-reversion model | 2089 | 6.3% | 0.3% (6) | -681% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2089 | 6 | -64% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 414 | 3 | -18% | -58% | -59% | -55% |
| Volatility model ≥ 5% | 202 | 1 | -37% | -17% | -16% | -11% |
| Volatility model ≥ 10% | 112 | 1 | +33% | +51% | +52% | +58% |
| Momentum model ≥ 2% | 366 | 2 | -35% | -53% | -54% | -51% |
| Momentum model ≥ 5% | 205 | 2 | +24% | -23% | -26% | -20% |
| Momentum model ≥ 10% | 135 | 1 | +7% | +17% | +19% | +22% |
| Mean-reversion model ≥ 2% | 792 | 3 | -60% | -86% | -88% | -83% |
| Mean-reversion model ≥ 5% | 520 | 3 | -39% | -84% | -85% | -78% |
| Mean-reversion model ≥ 10% | 329 | 2 | -33% | -78% | -80% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2285 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 1086 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 282 | 4% | 2% | 2% | 1% | 1% | 1% |
| **All** | 3653 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 14 | 0% | -$250.55 | -56% | — |
| Sell at 2¢ | 138 | 4% | -$396.67 | -89% | 47 sec |
| Sell at 3¢ | 85 | 2% | -$399.40 | -89% | 50 sec |
| Sell at 5¢ | 63 | 2% | -$391.60 | -88% | 64 sec |
| Sell at 10¢ | 48 | 1% | -$355.67 | -80% | 80 sec |
| Sell at 25¢ | 24 | 1% | -$339.11 | -76% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$309.55 | -69% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 119 | 2 | 12% | 3% | +60% | -79% | -87% |
| 2–5 min | 1200 | 6 | 7% | 3% | -52% | -88% | -89% |
| 1–2 min | 945 | 4 | 3% | 2% | -55% | -93% | -92% |
| Under 1 min | 1389 | 2 | 1% | 0% | -79% | -87% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 259 | 1 | 4% | 2% | -51% | -91% | -90% |
| ZEC | 256 | 1 | 5% | 2% | -53% | -88% | -92% |
| NEAR | 254 | 0 | 5% | 2% | -100% | -88% | -90% |
| ETH | 254 | 2 | 5% | 4% | -4% | -88% | -85% |
| BNB | 254 | 0 | 3% | 1% | -100% | -93% | -95% |
| XRP | 253 | 3 | 2% | 2% | +56% | -43% | -42% |
| HYPE | 253 | 1 | 4% | 3% | -52% | -90% | -88% |
| BTC | 251 | 0 | 6% | 3% | -100% | -85% | -89% |
| SOL | 251 | 0 | 3% | 1% | -100% | -92% | -92% |
| GOLD | 189 | 0 | 5% | 2% | -100% | -88% | -91% |
| SILVER | 172 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 168 | 1 | 4% | 1% | -37% | -93% | -95% |
| COPPER | 153 | 0 | 1% | 1% | -100% | -98% | -98% |
| NATGAS | 148 | 1 | 4% | 3% | -37% | -93% | -89% |
| PLATINUM | 133 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 123 | 0 | 2% | 1% | -100% | -96% | -98% |
| GBPUSD | 102 | 1 | 5% | 2% | -8% | -92% | -92% |
| EURUSD | 95 | 1 | 3% | 1% | -2% | -95% | -97% |
| USDJPY | 85 | 2 | 2% | 2% | +120% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1887 | 8 | 4% | 2% | -51% | -92% | -92% |
| DOWN (bought NO) | 1766 | 6 | 4% | 2% | -61% | -85% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 248 | 1 | 2% | 1% | -23% | -17% | -16% |
| 0.05–0.1% | 301 | 0 | 1% | 0% | -100% | -97% | -98% |
| 0.1–0.2% | 542 | 1 | 4% | 1% | -76% | -91% | -93% |
| 0.2–0.5% | 797 | 2 | 6% | 3% | -72% | -88% | -88% |
| Over 0.5% | 396 | 4 | 7% | 3% | +5% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 888 | 2 | 4% | 2% | -74% | -91% | -93% |
| Morning (6am–12pm) | 960 | 6 | 4% | 2% | -29% | -91% | -90% |
| Afternoon (12–6pm) | 841 | 2 | 3% | 1% | -73% | -80% | -84% |
| Evening (6pm–12am) | 964 | 4 | 4% | 2% | -52% | -92% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,379 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 5:59:51 PM | SILVER | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 5:59:51 PM | USDJPY | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 5:59:51 PM | PALLADIUM | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 5:59:35 PM | GOLD | DOWN | 24 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/30 5:59:03 PM | ZEC | UP | 56 sec | -0.117% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 5:58:47 PM | HYPE | DOWN | 72 sec | +0.047% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 5:58:33 PM | NATGAS | UP | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 5:58:33 PM | DOGE | UP | 87 sec | -0.095% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 5:58:18 PM | SOL | UP | 1.7 min | -0.113% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 5:58:18 PM | PLATINUM | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 5:58:18 PM | EURUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 5:57:13 PM | NEAR | UP | 2.8 min | -0.600% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 5:56:09 PM | ETH | UP | 3.9 min | -0.188% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 5:55:38 PM | BNB | UP | 4.3 min | -0.306% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 5:44:48 PM | SOL | DOWN | 11 sec | +0.037% | 0¢ | ❌ Lost | $0.00 |
| 9/30 5:44:48 PM | PLATINUM | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 5:44:48 PM | GOLD | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 5:44:32 PM | COPPER | DOWN | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 5:44:32 PM | DOGE | DOWN | 27 sec | +0.056% | 0¢ | ❌ Lost | $0.00 |
| 9/30 5:44:16 PM | ZEC | UP | 43 sec | -0.101% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 5:44:16 PM | EURUSD | UP | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 5:44:16 PM | WTI | UP | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 5:43:43 PM | BTC | UP | 76 sec | -0.087% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 5:43:43 PM | BNB | DOWN | 76 sec | +0.034% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 5:43:27 PM | USDJPY | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 5:43:11 PM | XRP | DOWN | 1.8 min | +0.141% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 5:43:11 PM | HYPE | DOWN | 1.8 min | +0.144% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 5:29:53 PM | DOGE | DOWN | 7 sec | +0.043% | 0¢ | ❌ Lost | $0.00 |
| 9/30 5:29:53 PM | EURUSD | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 5:29:38 PM | ETH | DOWN | 22 sec | +0.000% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
