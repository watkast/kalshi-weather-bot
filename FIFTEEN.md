# 15-Minute 1¢ Study

*Updated Mon Oct 5, 12:44 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 576 finished bets | 1% | $35.90 | +58% | +6.23¢ | -$17.80 / $53.70 |

*Expect about **82 buys a day** (~$12.34/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 2%, hold to the close | 1059 | $26.35 | +21% |
| Momentum model ≥ 5%, hold to the close | 580 | $22.20 | +36% |
| 5+ min left, hold to the close | 196 | $13.05 | +45% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 8131 | 8117 | 37 (0%) | 1.07% | -$455.95 (-47%) | Hold to the close: -$455.95 (-47%) |

*In play or awaiting result: 14. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 5385 | 4.2% | 0.5% (25) | -592% | ❌ Worse |
| Momentum model | 5385 | 4.3% | 0.5% (25) | -621% | ❌ Worse |
| Mean-reversion model | 5385 | 6.9% | 0.5% (25) | -688% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5385 | 25 | -41% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 1059 | 11 | +21% | -68% | -68% | -63% |
| Volatility model ≥ 5% | 576 | 7 | +58% | -55% | -54% | -49% |
| Volatility model ≥ 10% | 359 | 5 | +105% | -35% | -36% | -31% |
| Momentum model ≥ 2% | 936 | 8 | +4% | -69% | -71% | -68% |
| Momentum model ≥ 5% | 580 | 6 | +36% | -61% | -63% | -59% |
| Momentum model ≥ 10% | 403 | 5 | +77% | -47% | -48% | -45% |
| Mean-reversion model ≥ 2% | 1872 | 14 | -18% | -82% | -83% | -78% |
| Mean-reversion model ≥ 5% | 1254 | 12 | +6% | -79% | -79% | -72% |
| Mean-reversion model ≥ 10% | 830 | 9 | +26% | -77% | -77% | -70% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5582 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 1923 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 612 | 4% | 3% | 2% | 2% | 1% | 0% |
| **All** | 8117 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 37 | 0% | -$455.95 | -47% | — |
| Sell at 2¢ | 324 | 4% | -$861.71 | -88% | 33 sec |
| Sell at 3¢ | 210 | 3% | -$864.05 | -89% | 47 sec |
| Sell at 5¢ | 155 | 2% | -$845.20 | -87% | 61 sec |
| Sell at 10¢ | 105 | 1% | -$794.40 | -82% | 66 sec |
| Sell at 25¢ | 58 | 1% | -$711.97 | -73% | 1.5 min |
| Sell at 50¢ | 36 | 0% | -$618.95 | -64% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 193 | 3 | 12% | 3% | +47% | -79% | -88% |
| 2–5 min | 2617 | 20 | 8% | 4% | -25% | -86% | -86% |
| 1–2 min | 2146 | 9 | 3% | 2% | -54% | -93% | -93% |
| Under 1 min | 3158 | 5 | 1% | 0% | -76% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 631 | 5 | 5% | 3% | -6% | -89% | -89% |
| ETH | 624 | 5 | 6% | 3% | +1% | -86% | -86% |
| DOGE | 624 | 2 | 4% | 1% | -59% | -90% | -90% |
| HYPE | 621 | 3 | 5% | 3% | -41% | -88% | -86% |
| BNB | 620 | 2 | 4% | 2% | -61% | -90% | -92% |
| SOL | 618 | 0 | 3% | 1% | -100% | -92% | -91% |
| XRP | 617 | 4 | 2% | 1% | -17% | -75% | -76% |
| BTC | 615 | 3 | 6% | 2% | -36% | -86% | -89% |
| NEAR | 612 | 3 | 7% | 3% | -35% | -62% | -63% |
| GOLD | 327 | 0 | 4% | 1% | -100% | -90% | -93% |
| SILVER | 312 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 298 | 2 | 3% | 1% | -29% | -95% | -96% |
| COPPER | 274 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 240 | 2 | 3% | 2% | -22% | -94% | -92% |
| PLATINUM | 240 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 232 | 1 | 2% | 1% | -60% | -96% | -98% |
| EURUSD | 221 | 1 | 5% | 3% | -58% | -92% | -91% |
| GBPUSD | 208 | 1 | 4% | 2% | -55% | -93% | -94% |
| USDJPY | 183 | 3 | 2% | 2% | +53% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4095 | 20 | 4% | 2% | -43% | -88% | -88% |
| DOWN (bought NO) | 4022 | 17 | 4% | 2% | -51% | -89% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 941 | 7 | 2% | 1% | +26% | -58% | -57% |
| 0.05–0.1% | 941 | 2 | 4% | 1% | -69% | -90% | -92% |
| 0.1–0.2% | 1383 | 6 | 4% | 2% | -45% | -90% | -90% |
| 0.2–0.5% | 1638 | 8 | 6% | 3% | -46% | -87% | -87% |
| Over 0.5% | 677 | 4 | 7% | 3% | -39% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1914 | 9 | 5% | 2% | -45% | -84% | -85% |
| Morning (6am–12pm) | 2058 | 17 | 5% | 3% | -5% | -89% | -87% |
| Afternoon (12–6pm) | 1751 | 4 | 3% | 1% | -73% | -86% | -87% |
| Evening (6pm–12am) | 2394 | 7 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,199 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/5 12:44:01 AM | HYPE | DOWN | 59 sec | +0.103% | — | In play | — |
| 10/5 12:43:43 AM | DOGE | UP | 77 sec | -0.175% | — | In play | — |
| 10/5 12:43:43 AM | ZEC | UP | 77 sec | -0.209% | — | In play | — |
| 10/5 12:43:27 AM | XRP | UP | 1.6 min | -0.165% | — | In play | — |
| 10/5 12:42:40 AM | BNB | UP | 2.3 min | -0.151% | — | In play | — |
| 10/5 12:42:40 AM | USDJPY | UP | 2.3 min | — | — | In play | — |
| 10/5 12:42:24 AM | EURUSD | UP | 2.6 min | — | — | In play | — |
| 10/5 12:42:08 AM | NATGAS | UP | 2.9 min | — | — | In play | — |
| 10/5 12:29:36 AM | SILVER | DOWN | 24 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 12:29:20 AM | PALLADIUM | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 12:29:20 AM | COPPER | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 12:29:20 AM | EURUSD | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 12:29:20 AM | XRP | UP | 40 sec | -0.159% | 0¢ | ❌ Lost | $0.00 |
| 10/5 12:29:04 AM | ETH | DOWN | 56 sec | +0.033% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 12:29:04 AM | DOGE | DOWN | 56 sec | -0.002% | 3¢ | ❌ Lost | $0.00 |
| 10/5 12:29:04 AM | GOLD | DOWN | 56 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 12:28:33 AM | BNB | UP | 86 sec | -0.118% | 0¢ | ❌ Lost | $0.00 |
| 10/5 12:28:01 AM | ZEC | DOWN | 2.0 min | +0.284% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 12:27:45 AM | WTI | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 12:27:29 AM | NATGAS | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 12:27:13 AM | HYPE | UP | 2.8 min | -0.364% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 12:27:13 AM | NEAR | UP | 2.8 min | -0.693% | 7¢ | ❌ Lost | -$0.15 |
| 10/5 12:14:24 AM | BNB | DOWN | 35 sec | +0.029% | 0¢ | ❌ Lost | $0.00 |
| 10/5 12:14:24 AM | WTI | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 12:13:17 AM | NATGAS | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 12:13:17 AM | ZEC | DOWN | 1.7 min | +0.251% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 12:12:45 AM | GBPUSD | DOWN | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 12:12:45 AM | USDJPY | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 12:12:29 AM | HYPE | DOWN | 2.5 min | +0.245% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 12:12:13 AM | BTC | DOWN | 2.8 min | +0.164% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
