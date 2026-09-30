# 15-Minute 1¢ Study

*Updated Tue Sep 29, 11:06 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 82 finished bets | 2% | $15.70 | +128% | +19.15¢ | $21.85 / -$6.15 |

*Expect about **39 buys a day** (~$5.85/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 82 | $1.20 | +10% |
| Momentum model ≥ 5%, hold to the close | 142 | -$1.75 | -11% |
| Volatility model ≥ 5%, sell at 25¢ | 130 | -$3.72 | -27% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 2714 | 2708 | 11 (0%) | 1.07% | -$175.40 (-53%) | Hold to the close: -$175.40 (-53%) |

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
| Volatility model | 1492 | 2.9% | 0.3% (5) | -450% | ❌ Worse |
| Momentum model | 1492 | 3.0% | 0.3% (5) | -500% | ❌ Worse |
| Mean-reversion model | 1492 | 5.7% | 0.3% (5) | -554% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1492 | 5 | -58% | -91% | -91% | -89% |
| Volatility model ≥ 2% | 284 | 2 | -18% | -86% | -88% | -85% |
| Volatility model ≥ 5% | 130 | 0 | -100% | -77% | -77% | -71% |
| Volatility model ≥ 10% | 70 | 0 | -100% | -75% | -75% | -69% |
| Momentum model ≥ 2% | 249 | 1 | -52% | -87% | -89% | -89% |
| Momentum model ≥ 5% | 142 | 1 | -11% | -83% | -88% | -83% |
| Momentum model ≥ 10% | 90 | 0 | -100% | -88% | -87% | -85% |
| Mean-reversion model ≥ 2% | 548 | 3 | -41% | -87% | -87% | -84% |
| Mean-reversion model ≥ 5% | 360 | 3 | -11% | -84% | -84% | -78% |
| Mean-reversion model ≥ 10% | 221 | 2 | +1% | -79% | -82% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1688 | 4% | 2% | 2% | 2% | 1% | 0% |
| Commodities | 827 | 2% | 1% | 1% | 0% | 0% | 0% |
| Financials | 193 | 5% | 3% | 3% | 2% | 2% | 1% |
| **All** | 2708 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 11 | 0% | -$175.40 | -53% | — |
| Sell at 2¢ | 95 | 4% | -$304.70 | -93% | 34 sec |
| Sell at 3¢ | 60 | 2% | -$306.00 | -93% | 47 sec |
| Sell at 5¢ | 42 | 2% | -$302.10 | -92% | 65 sec |
| Sell at 10¢ | 35 | 1% | -$269.55 | -82% | 1.6 min |
| Sell at 25¢ | 18 | 1% | -$255.82 | -78% | 1.7 min |
| Sell at 50¢ | 10 | 0% | -$233.90 | -71% | 2.3 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 82 | 2 | 11% | 2% | +128% | -81% | -87% |
| 2–5 min | 893 | 6 | 6% | 3% | -35% | -89% | -90% |
| 1–2 min | 725 | 2 | 3% | 2% | -70% | -94% | -93% |
| Under 1 min | 1008 | 1 | 1% | 0% | -85% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 191 | 1 | 4% | 2% | -32% | -91% | -91% |
| ZEC | 190 | 1 | 5% | 3% | -37% | -88% | -91% |
| NEAR | 188 | 0 | 5% | 1% | -100% | -87% | -90% |
| ETH | 188 | 2 | 4% | 3% | +30% | -90% | -87% |
| BTC | 187 | 0 | 6% | 2% | -100% | -85% | -91% |
| XRP | 187 | 2 | 2% | 2% | +38% | -95% | -94% |
| SOL | 187 | 0 | 3% | 2% | -100% | -92% | -90% |
| HYPE | 185 | 1 | 4% | 2% | -32% | -91% | -91% |
| BNB | 185 | 0 | 2% | 1% | -100% | -97% | -97% |
| GOLD | 147 | 0 | 5% | 1% | -100% | -89% | -91% |
| WTI | 131 | 0 | 3% | 1% | -100% | -94% | -95% |
| SILVER | 130 | 0 | 2% | 1% | -100% | -95% | -95% |
| COPPER | 120 | 0 | 1% | 1% | -100% | -99% | -98% |
| NATGAS | 112 | 0 | 3% | 1% | -100% | -95% | -93% |
| PLATINUM | 97 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 90 | 0 | 1% | 0% | -100% | -98% | -100% |
| GBPUSD | 70 | 1 | 6% | 3% | +33% | -90% | -89% |
| EURUSD | 65 | 1 | 5% | 2% | +44% | -92% | -96% |
| USDJPY | 58 | 2 | 3% | 3% | +222% | -94% | -91% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1426 | 8 | 4% | 2% | -36% | -93% | -92% |
| DOWN (bought NO) | 1282 | 3 | 4% | 1% | -73% | -92% | -93% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 177 | 0 | 2% | 1% | -100% | -94% | -94% |
| 0.05–0.1% | 225 | 0 | 1% | 0% | -100% | -97% | -98% |
| 0.1–0.2% | 402 | 1 | 3% | 1% | -66% | -91% | -92% |
| 0.2–0.5% | 611 | 2 | 5% | 3% | -64% | -90% | -91% |
| Over 0.5% | 272 | 4 | 6% | 3% | +52% | -88% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 577 | 1 | 3% | 1% | -80% | -93% | -96% |
| Morning (6am–12pm) | 647 | 6 | 4% | 2% | +7% | -91% | -90% |
| Afternoon (12–6pm) | 583 | 1 | 3% | 1% | -81% | -94% | -97% |
| Evening (6pm–12am) | 901 | 3 | 4% | 2% | -61% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,653 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/29 10:59:57 PM | WTI | DOWN | 2 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/29 10:59:41 PM | ZEC | UP | 19 sec | -0.091% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 10:59:09 PM | SILVER | UP | 51 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/29 10:59:09 PM | GOLD | UP | 51 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 10:59:09 PM | EURUSD | DOWN | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 10:58:54 PM | GBPUSD | DOWN | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 10:58:39 PM | PALLADIUM | UP | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 10:58:39 PM | ETH | UP | 81 sec | -0.105% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 10:58:39 PM | XRP | UP | 81 sec | -0.140% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 10:58:39 PM | PLATINUM | UP | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 10:57:34 PM | BTC | UP | 2.4 min | -0.118% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 10:57:18 PM | NATGAS | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 10:57:18 PM | BNB | UP | 2.7 min | -0.130% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 10:57:18 PM | NEAR | UP | 2.7 min | -0.759% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 10:57:18 PM | HYPE | UP | 2.7 min | -0.283% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 10:57:18 PM | SOL | UP | 2.7 min | -0.218% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 10:56:47 PM | DOGE | UP | 3.2 min | -0.313% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 10:44:45 PM | XRP | UP | 14 sec | -0.073% | 0¢ | ❌ Lost | $0.00 |
| 9/29 10:44:29 PM | DOGE | UP | 30 sec | -0.063% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 10:44:29 PM | COPPER | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 10:44:29 PM | HYPE | UP | 30 sec | -0.077% | 0¢ | ❌ Lost | $0.00 |
| 9/29 10:44:29 PM | NEAR | DOWN | 30 sec | +0.070% | 0¢ | ❌ Lost | $0.00 |
| 9/29 10:44:29 PM | EURUSD | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 10:44:13 PM | BTC | UP | 46 sec | -0.069% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 10:44:13 PM | PALLADIUM | DOWN | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 10:43:26 PM | BNB | UP | 1.6 min | -0.122% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 10:43:26 PM | NATGAS | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 10:43:26 PM | SOL | UP | 1.6 min | -0.176% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 10:43:26 PM | ZEC | UP | 1.6 min | -0.304% | 0¢ | ❌ Lost | $0.00 |
| 9/29 10:42:23 PM | PLATINUM | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
