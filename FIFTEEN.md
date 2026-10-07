# 15-Minute 1¢ Study

*Updated Wed Oct 7, 7:40 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 736 finished bets | 1% | $33.10 | +42% | +4.50¢ | -$11.45 / $44.55 |

*Expect about **79 buys a day** (~$11.88/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 734 | $20.15 | +26% |
| 5+ min left, hold to the close | 279 | $14.60 | +35% |
| Mean-reversion model ≥ 5%, hold to the close | 1608 | $7.50 | +4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 10758 | 10752 | 49 (0%) | 1.07% | -$615.55 (-47%) | Hold to the close: -$615.55 (-47%) |

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
| Volatility model | 6960 | 4.1% | 0.5% (33) | -562% | ❌ Worse |
| Momentum model | 6960 | 4.2% | 0.5% (33) | -592% | ❌ Worse |
| Mean-reversion model | 6960 | 6.7% | 0.5% (33) | -652% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6960 | 33 | -40% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 1345 | 12 | +4% | -73% | -73% | -69% |
| Volatility model ≥ 5% | 736 | 8 | +42% | -62% | -61% | -58% |
| Volatility model ≥ 10% | 458 | 6 | +94% | -46% | -47% | -42% |
| Momentum model ≥ 2% | 1199 | 10 | +1% | -74% | -76% | -74% |
| Momentum model ≥ 5% | 734 | 7 | +26% | -67% | -68% | -66% |
| Momentum model ≥ 10% | 506 | 6 | +72% | -56% | -57% | -54% |
| Mean-reversion model ≥ 2% | 2375 | 19 | -13% | -84% | -84% | -80% |
| Mean-reversion model ≥ 5% | 1608 | 15 | +4% | -81% | -81% | -75% |
| Mean-reversion model ≥ 10% | 1068 | 11 | +19% | -79% | -79% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7157 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2706 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 889 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 10752 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 49 | 0% | -$615.55 | -47% | — |
| Sell at 2¢ | 379 | 4% | -$1,161.01 | -89% | 34 sec |
| Sell at 3¢ | 253 | 2% | -$1,160.88 | -89% | 47 sec |
| Sell at 5¢ | 189 | 2% | -$1,136.70 | -87% | 61 sec |
| Sell at 10¢ | 127 | 1% | -$1,079.18 | -83% | 65 sec |
| Sell at 25¢ | 73 | 1% | -$975.92 | -75% | 82 sec |
| Sell at 50¢ | 48 | 0% | -$851.55 | -65% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 276 | 4 | 10% | 4% | +37% | -82% | -88% |
| 2–5 min | 3460 | 25 | 7% | 3% | -30% | -88% | -88% |
| 1–2 min | 2843 | 12 | 3% | 2% | -54% | -94% | -93% |
| Under 1 min | 4170 | 8 | 1% | 0% | -72% | -88% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 804 | 6 | 5% | 3% | -11% | -90% | -89% |
| HYPE | 802 | 3 | 5% | 3% | -54% | -89% | -87% |
| DOGE | 798 | 2 | 3% | 1% | -68% | -92% | -92% |
| ETH | 796 | 7 | 5% | 3% | +10% | -88% | -88% |
| BNB | 795 | 3 | 4% | 2% | -54% | -91% | -92% |
| NEAR | 793 | 5 | 6% | 3% | -17% | -69% | -71% |
| SOL | 791 | 0 | 3% | 1% | -100% | -94% | -93% |
| BTC | 790 | 4 | 5% | 2% | -33% | -88% | -90% |
| XRP | 788 | 5 | 2% | 1% | -20% | -80% | -80% |
| GOLD | 452 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 442 | 0 | 2% | 1% | -100% | -95% | -94% |
| WTI | 417 | 3 | 3% | 1% | -21% | -95% | -96% |
| COPPER | 386 | 0 | 1% | 1% | -100% | -99% | -99% |
| PLATINUM | 346 | 0 | 0% | 0% | -100% | -99% | -99% |
| NATGAS | 333 | 3 | 3% | 2% | -16% | -94% | -92% |
| PALLADIUM | 330 | 1 | 2% | 1% | -72% | -97% | -98% |
| EURUSD | 324 | 3 | 4% | 2% | -14% | -65% | -63% |
| GBPUSD | 304 | 1 | 3% | 2% | -69% | -95% | -95% |
| USDJPY | 261 | 3 | 2% | 1% | +7% | -97% | -96% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5465 | 26 | 4% | 2% | -45% | -88% | -87% |
| DOWN (bought NO) | 5287 | 23 | 3% | 2% | -50% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1181 | 8 | 2% | 1% | +17% | -65% | -65% |
| 0.05–0.1% | 1240 | 4 | 3% | 1% | -53% | -92% | -92% |
| 0.1–0.2% | 1818 | 6 | 3% | 2% | -58% | -92% | -92% |
| 0.2–0.5% | 2090 | 12 | 6% | 3% | -37% | -88% | -87% |
| Over 0.5% | 826 | 5 | 7% | 3% | -38% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2890 | 17 | 4% | 2% | -32% | -84% | -84% |
| Morning (6am–12pm) | 2628 | 17 | 4% | 2% | -26% | -90% | -89% |
| Afternoon (12–6pm) | 2244 | 7 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 2990 | 8 | 3% | 1% | -69% | -95% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,004 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/7 7:29:45 AM | SOL | DOWN | 14 sec | +0.009% | 0¢ | ❌ Lost | $0.00 |
| 10/7 7:29:45 AM | NEAR | DOWN | 14 sec | +0.061% | 0¢ | ❌ Lost | $0.00 |
| 10/7 7:29:45 AM | SILVER | UP | 14 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 7:29:45 AM | BNB | DOWN | 14 sec | +0.018% | 0¢ | ❌ Lost | $0.00 |
| 10/7 7:29:45 AM | ETH | DOWN | 14 sec | +0.015% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:29:45 AM | DOGE | UP | 14 sec | -0.081% | 0¢ | ❌ Lost | $0.00 |
| 10/7 7:29:13 AM | NATGAS | DOWN | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:28:56 AM | BTC | UP | 63 sec | -0.111% | 1¢ | ❌ Lost | $0.00 |
| 10/7 7:28:40 AM | HYPE | UP | 79 sec | -0.149% | 0¢ | ❌ Lost | $0.00 |
| 10/7 7:28:40 AM | XRP | UP | 79 sec | -0.201% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 7:28:08 AM | PALLADIUM | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:25:57 AM | WTI | DOWN | 4.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 7:25:25 AM | USDJPY | DOWN | 4.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:25:25 AM | GBPUSD | UP | 4.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:14:44 AM | WTI | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:14:28 AM | SILVER | DOWN | 32 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/7 7:14:28 AM | GBPUSD | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:14:13 AM | GOLD | DOWN | 46 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/7 7:14:13 AM | HYPE | UP | 46 sec | -0.090% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:13:56 AM | SOL | UP | 63 sec | -0.232% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:13:56 AM | BTC | UP | 63 sec | -0.139% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:13:56 AM | NATGAS | UP | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:13:40 AM | EURUSD | DOWN | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:13:24 AM | XRP | UP | 1.6 min | -0.263% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:13:08 AM | BNB | UP | 1.9 min | -0.198% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 7:13:08 AM | DOGE | UP | 1.9 min | -0.294% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 7:12:51 AM | NEAR | UP | 2.1 min | -0.759% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 7:12:51 AM | ETH | UP | 2.1 min | -0.500% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:12:51 AM | PLATINUM | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:11:46 AM | USDJPY | DOWN | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
