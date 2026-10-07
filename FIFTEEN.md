# 15-Minute 1¢ Study

*Updated Wed Oct 7, 12:05 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 736 finished bets | 1% | $33.10 | +42% | +4.50¢ | -$11.45 / $44.55 |

*Expect about **78 buys a day** (~$11.65/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 735 | $20.00 | +26% |
| 5+ min left, hold to the close | 282 | $14.15 | +34% |
| Volatility model ≥ 2%, hold to the close | 1347 | $6.30 | +4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 10836 | 10830 | 49 (0%) | 1.07% | -$625.90 (-48%) | Hold to the close: -$625.90 (-48%) |

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
| Volatility model | 7004 | 4.1% | 0.5% (33) | -561% | ❌ Worse |
| Momentum model | 7004 | 4.1% | 0.5% (33) | -590% | ❌ Worse |
| Mean-reversion model | 7004 | 6.8% | 0.5% (33) | -653% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7004 | 33 | -41% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 1347 | 12 | +4% | -73% | -73% | -69% |
| Volatility model ≥ 5% | 736 | 8 | +42% | -62% | -61% | -58% |
| Volatility model ≥ 10% | 458 | 6 | +94% | -46% | -47% | -42% |
| Momentum model ≥ 2% | 1201 | 10 | +1% | -74% | -76% | -74% |
| Momentum model ≥ 5% | 735 | 7 | +26% | -67% | -69% | -66% |
| Momentum model ≥ 10% | 506 | 6 | +72% | -56% | -57% | -54% |
| Mean-reversion model ≥ 2% | 2391 | 19 | -14% | -84% | -84% | -80% |
| Mean-reversion model ≥ 5% | 1619 | 15 | +3% | -81% | -81% | -75% |
| Mean-reversion model ≥ 10% | 1077 | 11 | +18% | -80% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7201 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2731 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 898 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 10830 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 49 | 0% | -$625.90 | -48% | — |
| Sell at 2¢ | 380 | 4% | -$1,171.10 | -89% | 34 sec |
| Sell at 3¢ | 253 | 2% | -$1,171.23 | -89% | 47 sec |
| Sell at 5¢ | 189 | 2% | -$1,147.05 | -87% | 61 sec |
| Sell at 10¢ | 127 | 1% | -$1,089.53 | -83% | 65 sec |
| Sell at 25¢ | 73 | 1% | -$986.27 | -75% | 82 sec |
| Sell at 50¢ | 48 | 0% | -$861.90 | -66% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 279 | 4 | 10% | 4% | +35% | -82% | -88% |
| 2–5 min | 3492 | 25 | 7% | 3% | -30% | -88% | -88% |
| 1–2 min | 2867 | 12 | 3% | 2% | -55% | -94% | -93% |
| Under 1 min | 4189 | 8 | 1% | 0% | -72% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 809 | 6 | 5% | 3% | -11% | -90% | -89% |
| HYPE | 807 | 3 | 5% | 3% | -55% | -89% | -87% |
| DOGE | 803 | 2 | 3% | 1% | -68% | -92% | -92% |
| ETH | 801 | 7 | 5% | 2% | +9% | -88% | -88% |
| BNB | 800 | 3 | 4% | 2% | -55% | -91% | -92% |
| NEAR | 797 | 5 | 6% | 3% | -18% | -69% | -71% |
| SOL | 796 | 0 | 3% | 1% | -100% | -94% | -93% |
| BTC | 795 | 4 | 5% | 2% | -34% | -88% | -90% |
| XRP | 793 | 5 | 2% | 1% | -21% | -80% | -80% |
| GOLD | 455 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 446 | 0 | 2% | 1% | -100% | -95% | -94% |
| WTI | 422 | 3 | 3% | 1% | -22% | -95% | -96% |
| COPPER | 390 | 0 | 1% | 1% | -100% | -99% | -99% |
| PLATINUM | 349 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 337 | 3 | 3% | 2% | -17% | -94% | -92% |
| PALLADIUM | 332 | 1 | 2% | 1% | -72% | -97% | -98% |
| EURUSD | 327 | 3 | 4% | 2% | -14% | -65% | -64% |
| GBPUSD | 307 | 1 | 3% | 2% | -70% | -95% | -95% |
| USDJPY | 264 | 3 | 2% | 1% | +6% | -97% | -96% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5516 | 26 | 4% | 2% | -45% | -88% | -88% |
| DOWN (bought NO) | 5314 | 23 | 3% | 2% | -50% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1182 | 8 | 2% | 1% | +17% | -65% | -65% |
| 0.05–0.1% | 1240 | 4 | 3% | 1% | -53% | -92% | -92% |
| 0.1–0.2% | 1830 | 6 | 3% | 2% | -59% | -92% | -92% |
| 0.2–0.5% | 2110 | 12 | 6% | 3% | -38% | -88% | -87% |
| Over 0.5% | 837 | 5 | 6% | 3% | -39% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2890 | 17 | 4% | 2% | -32% | -84% | -84% |
| Morning (6am–12pm) | 2706 | 17 | 4% | 2% | -28% | -91% | -90% |
| Afternoon (12–6pm) | 2244 | 7 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 2990 | 8 | 3% | 1% | -69% | -95% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,025 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/7 11:59:53 AM | ZEC | DOWN | 7 sec | +0.108% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 11:59:38 AM | WTI | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 11:59:22 AM | XRP | DOWN | 38 sec | +0.042% | 0¢ | ❌ Lost | $0.00 |
| 10/7 11:59:22 AM | USDJPY | UP | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 11:59:06 AM | HYPE | UP | 54 sec | -0.188% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 11:58:35 AM | DOGE | DOWN | 85 sec | +0.200% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 11:58:35 AM | EURUSD | DOWN | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 11:58:35 AM | NATGAS | UP | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 11:58:35 AM | GBPUSD | DOWN | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 11:58:03 AM | BNB | DOWN | 1.9 min | +0.152% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 11:57:47 AM | ETH | DOWN | 2.2 min | +0.258% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 11:57:47 AM | BTC | DOWN | 2.2 min | +0.109% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 11:57:31 AM | NEAR | DOWN | 2.5 min | +0.850% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 11:57:31 AM | SOL | DOWN | 2.5 min | +0.185% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 11:44:35 AM | GOLD | UP | 25 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/7 11:44:35 AM | ZEC | UP | 25 sec | -0.352% | 0¢ | ❌ Lost | $0.00 |
| 10/7 11:44:19 AM | DOGE | UP | 41 sec | -0.180% | 0¢ | ❌ Lost | $0.00 |
| 10/7 11:44:19 AM | XRP | UP | 41 sec | -0.148% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 11:44:19 AM | NEAR | UP | 41 sec | -0.397% | 0¢ | ❌ Lost | $0.00 |
| 10/7 11:44:19 AM | SILVER | UP | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 11:43:48 AM | PALLADIUM | UP | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 11:43:16 AM | WTI | UP | 1.7 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/7 11:43:16 AM | BTC | UP | 1.7 min | -0.175% | 0¢ | ❌ Lost | $0.00 |
| 10/7 11:43:16 AM | SOL | UP | 1.7 min | -0.195% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 11:43:00 AM | BNB | UP | 2.0 min | -0.164% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 11:42:45 AM | PLATINUM | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 11:42:45 AM | HYPE | UP | 2.2 min | -0.414% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 11:42:30 AM | COPPER | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 11:42:14 AM | ETH | UP | 2.8 min | -0.492% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 11:29:41 AM | EURUSD | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
