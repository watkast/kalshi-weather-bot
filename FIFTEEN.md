# 15-Minute 1¢ Study

*Updated Tue Sep 29, 1:39 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 57 finished bets | 4% | $19.45 | +227% | +34.12¢ | $23.80 / -$4.35 |

*Expect about **47 buys a day** (~$7.08/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 208 | $15.30 | +57% |
| 5+ min left, sell at 50¢ | 57 | $4.95 | +58% |
| Volatility model ≥ 5%, sell at 25¢ | 76 | $2.13 | +27% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1653 | 1647 | 8 (0%) | 1.07% | -$86.30 (-44%) | Hold to the close: -$86.30 (-44%) |

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
| Volatility model | 844 | 2.9% | 0.5% (4) | -390% | ❌ Worse |
| Momentum model | 844 | 3.1% | 0.5% (4) | -464% | ❌ Worse |
| Mean-reversion model | 844 | 6.1% | 0.5% (4) | -463% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 844 | 4 | -39% | -89% | -91% | -86% |
| Volatility model ≥ 2% | 164 | 1 | -27% | -84% | -86% | -80% |
| Volatility model ≥ 5% | 76 | 0 | -100% | -70% | -70% | -58% |
| Volatility model ≥ 10% | 41 | 0 | -100% | -71% | -68% | -46% |
| Momentum model ≥ 2% | 138 | 0 | -100% | -85% | -90% | -88% |
| Momentum model ≥ 5% | 81 | 0 | -100% | -82% | -91% | -85% |
| Momentum model ≥ 10% | 55 | 0 | -100% | -90% | -85% | -75% |
| Mean-reversion model ≥ 2% | 317 | 3 | +4% | -85% | -86% | -79% |
| Mean-reversion model ≥ 5% | 208 | 3 | +57% | -82% | -82% | -73% |
| Mean-reversion model ≥ 10% | 133 | 2 | +73% | -78% | -78% | -68% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1039 | 4% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 511 | 1% | 1% | 0% | 0% | 0% | 0% |
| Financials | 97 | 3% | 3% | 2% | 2% | 2% | 2% |
| **All** | 1647 | 3% | 2% | 2% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 8 | 0% | -$86.30 | -44% | — |
| Sell at 2¢ | 54 | 3% | -$184.26 | -93% | 47 sec |
| Sell at 3¢ | 34 | 2% | -$185.04 | -93% | 47 sec |
| Sell at 5¢ | 25 | 2% | -$182.05 | -92% | 81 sec |
| Sell at 10¢ | 23 | 1% | -$168.17 | -85% | 1.9 min |
| Sell at 25¢ | 13 | 1% | -$155.27 | -78% | 2.1 min |
| Sell at 50¢ | 9 | 1% | -$137.55 | -69% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 57 | 2 | 7% | 4% | +227% | -88% | -86% |
| 2–5 min | 551 | 5 | 7% | 3% | -12% | -88% | -89% |
| 1–2 min | 457 | 1 | 2% | 1% | -76% | -96% | -96% |
| Under 1 min | 582 | 0 | 1% | 0% | -100% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 119 | 2 | 5% | 3% | +110% | -88% | -85% |
| ZEC | 118 | 1 | 6% | 2% | +4% | -87% | -94% |
| NEAR | 116 | 0 | 4% | 2% | -100% | -89% | -93% |
| DOGE | 116 | 1 | 4% | 3% | +7% | -90% | -85% |
| XRP | 116 | 2 | 3% | 3% | +117% | -92% | -91% |
| BTC | 115 | 0 | 8% | 3% | -100% | -80% | -87% |
| SOL | 115 | 0 | 3% | 2% | -100% | -93% | -89% |
| BNB | 113 | 0 | 3% | 1% | -100% | -94% | -94% |
| HYPE | 111 | 0 | 3% | 2% | -100% | -94% | -94% |
| GOLD | 90 | 0 | 2% | 0% | -100% | -95% | -100% |
| WTI | 81 | 0 | 1% | 0% | -100% | -98% | -100% |
| SILVER | 80 | 0 | 1% | 0% | -100% | -97% | -96% |
| COPPER | 73 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 69 | 0 | 3% | 1% | -100% | -95% | -92% |
| PLATINUM | 68 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 50 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 37 | 0 | 3% | 0% | -100% | -95% | -93% |
| USDJPY | 30 | 2 | 7% | 7% | +522% | -88% | -83% |
| EURUSD | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 871 | 5 | 4% | 2% | -33% | -92% | -92% |
| DOWN (bought NO) | 776 | 3 | 3% | 1% | -55% | -94% | -95% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 107 | 0 | 3% | 2% | -100% | -89% | -89% |
| 0.05–0.1% | 119 | 0 | 1% | 0% | -100% | -97% | -100% |
| 0.1–0.2% | 231 | 0 | 4% | 1% | -100% | -90% | -90% |
| 0.2–0.5% | 396 | 2 | 5% | 3% | -44% | -90% | -91% |
| Over 0.5% | 186 | 4 | 7% | 4% | +128% | -86% | -86% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 390 | 1 | 3% | 1% | -70% | -93% | -94% |
| Morning (6am–12pm) | 338 | 4 | 3% | 1% | +36% | -94% | -94% |
| Afternoon (12–6pm) | 330 | 1 | 2% | 1% | -65% | -95% | -96% |
| Evening (6pm–12am) | 589 | 2 | 4% | 2% | -60% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,992 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 45 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/29 1:29:53 AM | GBPUSD | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 1:29:53 AM | BTC | DOWN | 6 sec | +0.001% | 0¢ | ❌ Lost | $0.00 |
| 9/29 1:29:53 AM | BNB | DOWN | 6 sec | -0.018% | 0¢ | ❌ Lost | $0.00 |
| 9/29 1:29:35 AM | PLATINUM | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 1:29:35 AM | SOL | UP | 24 sec | -0.025% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:29:19 AM | ZEC | UP | 40 sec | -0.287% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:29:19 AM | USDJPY | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 1:29:19 AM | XRP | DOWN | 40 sec | +0.067% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:29:03 AM | HYPE | DOWN | 57 sec | +0.055% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:29:03 AM | SILVER | DOWN | 57 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:29:03 AM | PALLADIUM | DOWN | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 1:28:45 AM | NEAR | UP | 75 sec | -0.614% | 0¢ | ❌ Lost | $0.00 |
| 9/29 1:28:29 AM | WTI | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 1:28:13 AM | NATGAS | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 1:27:58 AM | GOLD | DOWN | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:27:26 AM | ETH | DOWN | 2.5 min | +0.258% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:26:54 AM | COPPER | UP | 3.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:14:52 AM | USDJPY | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 1:14:52 AM | NEAR | DOWN | 8 sec | +0.006% | 0¢ | ❌ Lost | $0.00 |
| 9/29 1:14:36 AM | COPPER | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 1:14:36 AM | BTC | UP | 24 sec | -0.024% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:14:20 AM | PLATINUM | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 1:14:05 AM | GOLD | DOWN | 54 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:14:05 AM | DOGE | DOWN | 54 sec | +0.108% | 0¢ | ❌ Lost | $0.00 |
| 9/29 1:14:05 AM | GBPUSD | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 1:14:05 AM | XRP | UP | 54 sec | -0.093% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:14:05 AM | ETH | DOWN | 54 sec | +0.093% | 0¢ | ❌ Lost | $0.00 |
| 9/29 1:13:01 AM | SOL | DOWN | 2.0 min | +0.269% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:11:56 AM | HYPE | DOWN | 3.1 min | +0.322% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:10:00 AM | BNB | DOWN | 5.0 min | +0.277% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
