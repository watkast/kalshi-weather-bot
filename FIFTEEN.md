# 15-Minute 1¢ Study

*Updated Tue Sep 29, 9:45 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 80 finished bets | 2% | $16.00 | +133% | +20.00¢ | $22.00 / -$6.00 |

*Expect about **40 buys a day** (~$5.94/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 80 | $1.50 | +12% |
| Volatility model ≥ 5%, sell at 25¢ | 127 | -$3.42 | -26% |
| Mean-reversion model ≥ 5%, hold to the close | 348 | -$3.75 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 2637 | 2618 | 10 (0%) | 1.07% | -$177.85 (-56%) | Hold to the close: -$177.85 (-56%) |

*In play or awaiting result: 19. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 1444 | 2.9% | 0.3% (4) | -493% | ❌ Worse |
| Momentum model | 1444 | 3.0% | 0.3% (4) | -556% | ❌ Worse |
| Mean-reversion model | 1444 | 5.7% | 0.3% (4) | -602% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1444 | 4 | -65% | -91% | -92% | -89% |
| Volatility model ≥ 2% | 277 | 1 | -59% | -86% | -88% | -87% |
| Volatility model ≥ 5% | 127 | 0 | -100% | -77% | -77% | -71% |
| Volatility model ≥ 10% | 69 | 0 | -100% | -75% | -75% | -69% |
| Momentum model ≥ 2% | 242 | 0 | -100% | -87% | -91% | -91% |
| Momentum model ≥ 5% | 139 | 0 | -100% | -85% | -90% | -88% |
| Momentum model ≥ 10% | 89 | 0 | -100% | -88% | -87% | -85% |
| Mean-reversion model ≥ 2% | 528 | 3 | -39% | -86% | -88% | -84% |
| Mean-reversion model ≥ 5% | 348 | 3 | -8% | -84% | -85% | -79% |
| Mean-reversion model ≥ 10% | 214 | 2 | +4% | -80% | -83% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1640 | 4% | 2% | 2% | 2% | 1% | 0% |
| Commodities | 797 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 181 | 5% | 3% | 3% | 2% | 2% | 1% |
| **All** | 2618 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 10 | 0% | -$177.85 | -56% | — |
| Sell at 2¢ | 92 | 4% | -$293.93 | -92% | 34 sec |
| Sell at 3¢ | 57 | 2% | -$295.62 | -93% | 47 sec |
| Sell at 5¢ | 40 | 2% | -$291.85 | -92% | 64 sec |
| Sell at 10¢ | 33 | 1% | -$260.62 | -82% | 1.6 min |
| Sell at 25¢ | 17 | 1% | -$247.58 | -78% | 1.6 min |
| Sell at 50¢ | 9 | 0% | -$229.10 | -72% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 80 | 2 | 11% | 2% | +133% | -80% | -87% |
| 2–5 min | 857 | 5 | 6% | 3% | -43% | -89% | -90% |
| 1–2 min | 704 | 2 | 3% | 2% | -69% | -94% | -93% |
| Under 1 min | 977 | 1 | 1% | 0% | -85% | -97% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 185 | 1 | 4% | 2% | -29% | -91% | -90% |
| ZEC | 184 | 1 | 5% | 2% | -35% | -89% | -93% |
| ETH | 183 | 2 | 4% | 3% | +34% | -90% | -87% |
| NEAR | 182 | 0 | 5% | 1% | -100% | -87% | -90% |
| BTC | 182 | 0 | 7% | 2% | -100% | -84% | -90% |
| XRP | 182 | 2 | 2% | 2% | +41% | -95% | -94% |
| SOL | 182 | 0 | 3% | 2% | -100% | -92% | -89% |
| HYPE | 180 | 0 | 3% | 2% | -100% | -92% | -92% |
| BNB | 180 | 0 | 2% | 1% | -100% | -96% | -96% |
| GOLD | 142 | 0 | 5% | 1% | -100% | -89% | -91% |
| WTI | 126 | 0 | 2% | 1% | -100% | -95% | -98% |
| SILVER | 125 | 0 | 2% | 1% | -100% | -95% | -95% |
| COPPER | 117 | 0 | 1% | 1% | -100% | -99% | -98% |
| NATGAS | 108 | 0 | 3% | 1% | -100% | -95% | -93% |
| PLATINUM | 92 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 87 | 0 | 1% | 0% | -100% | -98% | -100% |
| GBPUSD | 67 | 1 | 6% | 3% | +39% | -90% | -88% |
| EURUSD | 60 | 1 | 5% | 2% | +56% | -91% | -96% |
| USDJPY | 54 | 2 | 4% | 4% | +246% | -94% | -90% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1374 | 7 | 4% | 2% | -42% | -92% | -92% |
| DOWN (bought NO) | 1244 | 3 | 3% | 1% | -72% | -93% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 175 | 0 | 2% | 1% | -100% | -94% | -94% |
| 0.05–0.1% | 212 | 0 | 1% | 0% | -100% | -97% | -98% |
| 0.1–0.2% | 387 | 0 | 3% | 1% | -100% | -91% | -93% |
| 0.2–0.5% | 597 | 2 | 5% | 3% | -64% | -90% | -91% |
| Over 0.5% | 268 | 4 | 6% | 3% | +55% | -88% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 577 | 1 | 3% | 1% | -80% | -93% | -96% |
| Morning (6am–12pm) | 647 | 6 | 4% | 2% | +7% | -91% | -90% |
| Afternoon (12–6pm) | 583 | 1 | 3% | 1% | -81% | -94% | -97% |
| Evening (6pm–12am) | 811 | 2 | 4% | 2% | -71% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,650 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/29 9:44:45 PM | HYPE | UP | 15 sec | -0.102% | 0¢ | ❌ Lost | $0.00 |
| 9/29 9:44:45 PM | COPPER | UP | 15 sec | — | 0¢ | In play | — |
| 9/29 9:44:29 PM | NEAR | UP | 31 sec | -0.302% | 0¢ | In play | — |
| 9/29 9:43:57 PM | NATGAS | DOWN | 63 sec | — | 0¢ | In play | — |
| 9/29 9:43:57 PM | WTI | DOWN | 63 sec | — | 1¢ | In play | — |
| 9/29 9:43:24 PM | SOL | DOWN | 1.6 min | +0.180% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 9:43:24 PM | BTC | DOWN | 1.6 min | +0.107% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 9:43:08 PM | XRP | DOWN | 1.9 min | +0.234% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 9:43:08 PM | GBPUSD | UP | 1.9 min | — | 0¢ | In play | — |
| 9/29 9:42:53 PM | SILVER | UP | 2.1 min | — | 1¢ | In play | — |
| 9/29 9:42:37 PM | PLATINUM | UP | 2.4 min | — | 0¢ | In play | — |
| 9/29 9:42:21 PM | GOLD | UP | 2.6 min | — | 1¢ | In play | — |
| 9/29 9:42:05 PM | ETH | DOWN | 2.9 min | +0.163% | 1¢ | In play | — |
| 9/29 9:41:35 PM | USDJPY | DOWN | 3.4 min | — | 0¢ | In play | — |
| 9/29 9:41:35 PM | DOGE | DOWN | 3.4 min | +0.365% | 1¢ | In play | — |
| 9/29 9:41:19 PM | ZEC | DOWN | 3.7 min | +0.392% | 13¢ | In play | — |
| 9/29 9:39:57 PM | BNB | DOWN | 5.0 min | +0.182% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 9:36:18 PM | EURUSD | UP | 8.7 min | — | 0¢ | In play | — |
| 9/29 9:29:59 PM | PLATINUM | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 9:29:59 PM | PALLADIUM | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 9:29:59 PM | EURUSD | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 9:29:43 PM | GOLD | DOWN | 16 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 9:29:43 PM | SILVER | DOWN | 16 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/29 9:29:43 PM | NATGAS | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 9:29:43 PM | BTC | UP | 16 sec | -0.016% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 9:29:27 PM | WTI | UP | 32 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/29 9:29:11 PM | USDJPY | UP | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 9:29:11 PM | DOGE | UP | 48 sec | -0.180% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 9:29:11 PM | ETH | UP | 48 sec | -0.089% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 9:28:55 PM | XRP | UP | 65 sec | -0.161% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
