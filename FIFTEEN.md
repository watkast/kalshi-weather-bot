# 15-Minute 1¢ Study

*Updated Thu Oct 1, 3:11 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 142 finished bets | 1% | $7.15 | +34% | +5.04¢ | $17.35 / -$10.20 |

*Expect about **38 buys a day** (~$5.65/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 286 | -$3.35 | -11% |
| Volatility model ≥ 5%, sell at 25¢ | 277 | -$6.52 | -21% |
| Volatility model ≥ 5%, sell at 10¢ | 277 | -$7.28 | -24% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 4675 | 4669 | 15 (0%) | 1.07% | -$362.85 (-63%) | Hold to the close: -$362.85 (-63%) |

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
| Volatility model | 2666 | 3.5% | 0.2% (6) | -667% | ❌ Worse |
| Momentum model | 2666 | 3.7% | 0.2% (6) | -724% | ❌ Worse |
| Mean-reversion model | 2666 | 6.6% | 0.2% (6) | -852% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2666 | 6 | -72% | -85% | -86% | -84% |
| Volatility model ≥ 2% | 548 | 3 | -38% | -63% | -65% | -61% |
| Volatility model ≥ 5% | 277 | 1 | -54% | -35% | -36% | -33% |
| Volatility model ≥ 10% | 156 | 1 | -6% | +12% | +10% | +16% |
| Momentum model ≥ 2% | 491 | 2 | -52% | -61% | -64% | -61% |
| Momentum model ≥ 5% | 286 | 2 | -11% | -41% | -44% | -39% |
| Momentum model ≥ 10% | 191 | 1 | -26% | -16% | -16% | -12% |
| Mean-reversion model ≥ 2% | 1013 | 3 | -68% | -85% | -88% | -84% |
| Mean-reversion model ≥ 5% | 668 | 3 | -52% | -83% | -85% | -79% |
| Mean-reversion model ≥ 10% | 422 | 2 | -47% | -78% | -80% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2862 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1386 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 421 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 4669 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 15 | 0% | -$362.85 | -63% | — |
| Sell at 2¢ | 174 | 4% | -$513.61 | -90% | 46 sec |
| Sell at 3¢ | 105 | 2% | -$517.90 | -90% | 49 sec |
| Sell at 5¢ | 77 | 2% | -$508.80 | -89% | 66 sec |
| Sell at 10¢ | 56 | 1% | -$471.49 | -82% | 81 sec |
| Sell at 25¢ | 26 | 1% | -$444.79 | -78% | 1.6 min |
| Sell at 50¢ | 13 | 0% | -$415.10 | -72% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 139 | 2 | 13% | 3% | +37% | -77% | -89% |
| 2–5 min | 1544 | 7 | 7% | 3% | -56% | -88% | -89% |
| 1–2 min | 1212 | 4 | 3% | 2% | -65% | -94% | -93% |
| Under 1 min | 1771 | 2 | 1% | 0% | -84% | -90% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 324 | 1 | 4% | 1% | -60% | -90% | -92% |
| ETH | 320 | 2 | 5% | 3% | -23% | -89% | -86% |
| ZEC | 318 | 1 | 5% | 2% | -63% | -89% | -94% |
| BNB | 318 | 0 | 4% | 1% | -100% | -91% | -94% |
| NEAR | 317 | 0 | 5% | 2% | -100% | -88% | -91% |
| BTC | 317 | 0 | 7% | 3% | -100% | -84% | -88% |
| HYPE | 317 | 1 | 5% | 3% | -62% | -89% | -87% |
| XRP | 316 | 3 | 2% | 1% | +22% | -55% | -55% |
| SOL | 315 | 0 | 3% | 1% | -100% | -92% | -92% |
| GOLD | 238 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 221 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 211 | 1 | 3% | 1% | -50% | -94% | -96% |
| COPPER | 197 | 0 | 1% | 1% | -100% | -98% | -99% |
| NATGAS | 181 | 1 | 4% | 2% | -48% | -93% | -91% |
| PLATINUM | 173 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 165 | 0 | 2% | 1% | -100% | -97% | -98% |
| GBPUSD | 149 | 1 | 5% | 2% | -37% | -92% | -93% |
| EURUSD | 148 | 1 | 4% | 2% | -37% | -93% | -93% |
| USDJPY | 124 | 3 | 3% | 2% | +126% | -94% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2377 | 9 | 4% | 2% | -57% | -92% | -92% |
| DOWN (bought NO) | 2292 | 6 | 4% | 1% | -70% | -87% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 334 | 1 | 1% | 1% | -44% | -40% | -40% |
| 0.05–0.1% | 401 | 0 | 2% | 0% | -100% | -94% | -97% |
| 0.1–0.2% | 686 | 1 | 4% | 1% | -81% | -91% | -92% |
| 0.2–0.5% | 968 | 2 | 6% | 3% | -77% | -88% | -89% |
| Over 0.5% | 472 | 4 | 7% | 2% | -12% | -87% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1116 | 2 | 4% | 1% | -80% | -92% | -94% |
| Morning (6am–12pm) | 1285 | 7 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 955 | 2 | 3% | 1% | -76% | -81% | -84% |
| Evening (6pm–12am) | 1313 | 4 | 4% | 2% | -65% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,169 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/1 2:59:52 PM | BTC | DOWN | 8 sec | +0.023% | 0¢ | ❌ Lost | $0.00 |
| 10/1 2:59:50 PM | XRP | UP | 10 sec | -0.053% | 0¢ | ❌ Lost | $0.00 |
| 10/1 2:59:28 PM | DOGE | UP | 32 sec | -0.080% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 2:59:22 PM | SILVER | DOWN | 38 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 2:59:10 PM | ETH | DOWN | 50 sec | +0.027% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 2:59:08 PM | PALLADIUM | UP | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 2:58:27 PM | PLATINUM | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 2:58:25 PM | GOLD | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 2:58:09 PM | ZEC | DOWN | 1.9 min | +0.444% | 0¢ | ❌ Lost | $0.00 |
| 10/1 2:57:59 PM | BNB | DOWN | 2.0 min | +0.057% | 0¢ | ❌ Lost | $0.00 |
| 10/1 2:57:40 PM | SOL | DOWN | 2.3 min | +0.119% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 2:57:16 PM | USDJPY | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 2:56:54 PM | EURUSD | UP | 3.1 min | — | 83¢ | ❌ Lost | -$0.15 |
| 10/1 2:56:45 PM | GBPUSD | UP | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 2:55:40 PM | HYPE | DOWN | 4.3 min | +0.437% | 27¢ | ❌ Lost | -$0.15 |
| 10/1 2:44:52 PM | COPPER | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 2:44:52 PM | WTI | DOWN | 8 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/1 2:44:20 PM | USDJPY | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 2:44:20 PM | PLATINUM | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 2:44:20 PM | GBPUSD | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 2:43:48 PM | EURUSD | UP | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 2:43:32 PM | GOLD | UP | 88 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 2:43:16 PM | HYPE | UP | 1.7 min | -0.161% | 1¢ | ❌ Lost | $0.00 |
| 10/1 2:42:28 PM | NEAR | UP | 2.5 min | -0.621% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 2:42:12 PM | BNB | UP | 2.8 min | -0.144% | 0¢ | ❌ Lost | $0.00 |
| 10/1 2:42:12 PM | ETH | UP | 2.8 min | -0.186% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 2:41:38 PM | DOGE | UP | 3.4 min | -0.291% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 2:41:38 PM | BTC | UP | 3.4 min | -0.155% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 2:41:38 PM | ZEC | UP | 3.4 min | -0.634% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 2:41:22 PM | XRP | UP | 3.6 min | -0.306% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
