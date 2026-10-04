# 15-Minute 1¢ Study

*Updated Sun Oct 4, 10:41 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 186 finished bets | 2% | $14.55 | +53% | +7.82¢ | $14.20 / $0.35 |

*Expect about **28 buys a day** (~$4.26/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 532 | -$1.60 | -3% |
| Momentum model ≥ 5%, hold to the close | 540 | -$1.90 | -3% |
| 5+ min left, sell at 50¢ | 186 | -$7.20 | -26% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 7465 | 7456 | 32 (0%) | 1.07% | -$446.90 (-50%) | Hold to the close: -$446.90 (-50%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 4920 | 4.2% | 0.4% (20) | -672% | ❌ Worse |
| Momentum model | 4920 | 4.3% | 0.4% (20) | -706% | ❌ Worse |
| Mean-reversion model | 4920 | 7.0% | 0.4% (20) | -778% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 4920 | 20 | -49% | -84% | -84% | -82% |
| Volatility model ≥ 2% | 992 | 7 | -18% | -68% | -69% | -63% |
| Volatility model ≥ 5% | 532 | 4 | -3% | -54% | -53% | -49% |
| Volatility model ≥ 10% | 332 | 4 | +76% | -32% | -34% | -27% |
| Momentum model ≥ 2% | 875 | 5 | -31% | -69% | -71% | -68% |
| Momentum model ≥ 5% | 540 | 4 | -3% | -60% | -63% | -59% |
| Momentum model ≥ 10% | 371 | 3 | +15% | -46% | -48% | -44% |
| Mean-reversion model ≥ 2% | 1748 | 10 | -38% | -82% | -84% | -78% |
| Mean-reversion model ≥ 5% | 1178 | 9 | -15% | -78% | -79% | -72% |
| Mean-reversion model ≥ 10% | 775 | 7 | +4% | -76% | -77% | -70% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5117 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 7456 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 32 | 0% | -$446.90 | -50% | — |
| Sell at 2¢ | 303 | 4% | -$788.12 | -88% | 34 sec |
| Sell at 3¢ | 194 | 3% | -$791.24 | -88% | 48 sec |
| Sell at 5¢ | 143 | 2% | -$773.95 | -86% | 61 sec |
| Sell at 10¢ | 97 | 1% | -$725.83 | -81% | 78 sec |
| Sell at 25¢ | 53 | 1% | -$663.47 | -74% | 1.6 min |
| Sell at 50¢ | 31 | 0% | -$587.65 | -66% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 183 | 3 | 13% | 3% | +56% | -78% | -87% |
| 2–5 min | 2407 | 16 | 8% | 4% | -35% | -85% | -86% |
| 1–2 min | 1959 | 8 | 3% | 2% | -55% | -94% | -93% |
| Under 1 min | 2904 | 5 | 1% | 0% | -74% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 577 | 4 | 5% | 3% | -18% | -88% | -89% |
| DOGE | 573 | 2 | 4% | 2% | -55% | -90% | -91% |
| HYPE | 572 | 2 | 5% | 3% | -58% | -89% | -86% |
| ETH | 571 | 4 | 6% | 3% | -12% | -86% | -86% |
| BNB | 567 | 2 | 5% | 2% | -58% | -90% | -92% |
| SOL | 566 | 0 | 3% | 1% | -100% | -92% | -91% |
| BTC | 565 | 2 | 6% | 2% | -54% | -86% | -90% |
| XRP | 564 | 4 | 2% | 1% | -9% | -73% | -73% |
| NEAR | 562 | 2 | 6% | 3% | -53% | -61% | -62% |
| GOLD | 304 | 0 | 5% | 1% | -100% | -90% | -92% |
| SILVER | 285 | 0 | 2% | 1% | -100% | -95% | -95% |
| WTI | 274 | 2 | 3% | 1% | -23% | -94% | -96% |
| COPPER | 254 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 226 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 225 | 2 | 4% | 2% | -17% | -94% | -92% |
| PALLADIUM | 216 | 1 | 2% | 1% | -57% | -96% | -98% |
| GBPUSD | 195 | 1 | 4% | 2% | -52% | -93% | -93% |
| EURUSD | 195 | 1 | 5% | 3% | -52% | -91% | -89% |
| USDJPY | 165 | 3 | 2% | 2% | +70% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 3759 | 17 | 4% | 2% | -47% | -88% | -87% |
| DOWN (bought NO) | 3697 | 15 | 4% | 2% | -53% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 851 | 5 | 2% | 1% | -1% | -55% | -54% |
| 0.05–0.1% | 872 | 2 | 3% | 1% | -66% | -91% | -93% |
| 0.1–0.2% | 1259 | 4 | 4% | 2% | -59% | -90% | -91% |
| 0.2–0.5% | 1495 | 7 | 6% | 4% | -48% | -87% | -86% |
| Over 0.5% | 638 | 4 | 7% | 3% | -36% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1882 | 8 | 5% | 2% | -50% | -84% | -86% |
| Morning (6am–12pm) | 2003 | 15 | 5% | 3% | -14% | -89% | -88% |
| Afternoon (12–6pm) | 1513 | 3 | 3% | 1% | -76% | -85% | -87% |
| Evening (6pm–12am) | 2058 | 6 | 3% | 2% | -66% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,992 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/4 10:41:26 AM | HYPE | DOWN | 3.6 min | +0.242% | — | In play | — |
| 10/4 10:40:23 AM | ZEC | DOWN | 4.6 min | +0.447% | — | In play | — |
| 10/4 10:39:34 AM | ETH | DOWN | 5.4 min | +0.170% | — | In play | — |
| 10/4 10:29:34 AM | NEAR | UP | 25 sec | -0.216% | 0¢ | ❌ Lost | $0.00 |
| 10/4 10:29:18 AM | DOGE | UP | 41 sec | -0.102% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 10:29:02 AM | BNB | DOWN | 58 sec | +0.005% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 10:29:02 AM | SOL | UP | 58 sec | -0.082% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 10:27:59 AM | BTC | UP | 2.0 min | -0.063% | 3¢ | ❌ Lost | -$0.15 |
| 10/4 10:27:59 AM | ETH | UP | 2.0 min | -0.080% | 3¢ | ❌ Lost | -$0.15 |
| 10/4 10:27:44 AM | XRP | UP | 2.3 min | -0.193% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 10:27:12 AM | HYPE | UP | 2.8 min | -0.244% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 10:27:12 AM | ZEC | DOWN | 2.8 min | +0.388% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 10:14:36 AM | ZEC | UP | 24 sec | -0.108% | 0¢ | ❌ Lost | $0.00 |
| 10/4 10:14:20 AM | SOL | DOWN | 40 sec | +0.035% | 13¢ | ❌ Lost | -$0.15 |
| 10/4 10:13:51 AM | HYPE | UP | 68 sec | -0.147% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 10:13:51 AM | XRP | UP | 68 sec | -0.100% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 10:13:34 AM | DOGE | DOWN | 85 sec | +0.131% | 0¢ | ❌ Lost | $0.00 |
| 10/4 10:13:18 AM | BNB | DOWN | 1.7 min | +0.051% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 10:13:02 AM | NEAR | DOWN | 1.9 min | +0.284% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:59:50 AM | HYPE | UP | 9 sec | -0.035% | 0¢ | ❌ Lost | $0.00 |
| 10/4 9:59:34 AM | ZEC | UP | 25 sec | -0.116% | 0¢ | ❌ Lost | $0.00 |
| 10/4 9:59:18 AM | DOGE | UP | 41 sec | -0.083% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:59:18 AM | BNB | DOWN | 41 sec | -0.034% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:59:18 AM | ETH | DOWN | 41 sec | +0.030% | 0¢ | ❌ Lost | $0.00 |
| 10/4 9:58:46 AM | BTC | UP | 73 sec | -0.052% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:58:30 AM | NEAR | UP | 89 sec | -0.407% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:58:30 AM | SOL | UP | 89 sec | -0.103% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:58:14 AM | XRP | DOWN | 1.8 min | +0.133% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:44:54 AM | HYPE | DOWN | 5 sec | +0.035% | 0¢ | ❌ Lost | $0.00 |
| 10/4 9:44:39 AM | BTC | DOWN | 20 sec | +0.025% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
