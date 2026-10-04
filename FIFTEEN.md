# 15-Minute 1¢ Study

*Updated Sun Oct 4, 8:23 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 186 finished bets | 2% | $14.55 | +53% | +7.82¢ | $14.20 / $0.35 |

*Expect about **29 buys a day** (~$4.30/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 529 | -$0.25 | -0% |
| Volatility model ≥ 5%, hold to the close | 525 | -$0.55 | -1% |
| 5+ min left, sell at 50¢ | 186 | -$7.20 | -26% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 7387 | 7381 | 32 (0%) | 1.07% | -$438.20 (-49%) | Hold to the close: -$438.20 (-49%) |

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
| Volatility model | 4845 | 4.2% | 0.4% (20) | -661% | ❌ Worse |
| Momentum model | 4845 | 4.3% | 0.4% (20) | -695% | ❌ Worse |
| Mean-reversion model | 4845 | 7.0% | 0.4% (20) | -767% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 4845 | 20 | -48% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 981 | 7 | -17% | -68% | -68% | -63% |
| Volatility model ≥ 5% | 525 | 4 | -1% | -53% | -52% | -48% |
| Volatility model ≥ 10% | 326 | 4 | +81% | -30% | -32% | -25% |
| Momentum model ≥ 2% | 860 | 5 | -30% | -68% | -71% | -68% |
| Momentum model ≥ 5% | 529 | 4 | -0% | -58% | -62% | -58% |
| Momentum model ≥ 10% | 361 | 3 | +20% | -44% | -46% | -42% |
| Mean-reversion model ≥ 2% | 1728 | 10 | -37% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1166 | 9 | -15% | -78% | -79% | -72% |
| Mean-reversion model ≥ 10% | 765 | 7 | +6% | -76% | -78% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5042 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 7381 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 32 | 0% | -$438.20 | -49% | — |
| Sell at 2¢ | 295 | 4% | -$781.50 | -88% | 34 sec |
| Sell at 3¢ | 188 | 3% | -$784.88 | -89% | 48 sec |
| Sell at 5¢ | 140 | 2% | -$767.20 | -87% | 61 sec |
| Sell at 10¢ | 94 | 1% | -$721.06 | -81% | 78 sec |
| Sell at 25¢ | 53 | 1% | -$654.77 | -74% | 1.6 min |
| Sell at 50¢ | 31 | 0% | -$578.95 | -65% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 183 | 3 | 13% | 3% | +56% | -78% | -87% |
| 2–5 min | 2388 | 16 | 8% | 4% | -35% | -86% | -86% |
| 1–2 min | 1938 | 8 | 3% | 2% | -55% | -94% | -93% |
| Under 1 min | 2869 | 5 | 1% | 0% | -74% | -87% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 568 | 4 | 5% | 3% | -17% | -88% | -88% |
| HYPE | 565 | 2 | 5% | 3% | -57% | -89% | -86% |
| DOGE | 564 | 2 | 4% | 1% | -54% | -91% | -91% |
| ETH | 563 | 4 | 6% | 3% | -10% | -86% | -86% |
| BTC | 558 | 2 | 6% | 2% | -53% | -86% | -90% |
| BNB | 558 | 2 | 4% | 2% | -57% | -90% | -92% |
| SOL | 557 | 0 | 3% | 1% | -100% | -93% | -92% |
| XRP | 556 | 4 | 2% | 1% | -8% | -73% | -73% |
| NEAR | 553 | 2 | 6% | 3% | -52% | -61% | -62% |
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
| UP (bought YES) | 3719 | 17 | 4% | 2% | -46% | -88% | -88% |
| DOWN (bought NO) | 3662 | 15 | 4% | 2% | -53% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 835 | 5 | 2% | 1% | +1% | -54% | -54% |
| 0.05–0.1% | 855 | 2 | 3% | 1% | -65% | -91% | -93% |
| 0.1–0.2% | 1233 | 4 | 4% | 2% | -58% | -90% | -91% |
| 0.2–0.5% | 1481 | 7 | 6% | 3% | -48% | -87% | -87% |
| Over 0.5% | 636 | 4 | 7% | 3% | -35% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1882 | 8 | 5% | 2% | -50% | -84% | -86% |
| Morning (6am–12pm) | 1928 | 15 | 5% | 3% | -11% | -89% | -88% |
| Afternoon (12–6pm) | 1513 | 3 | 3% | 1% | -76% | -85% | -87% |
| Evening (6pm–12am) | 2058 | 6 | 3% | 2% | -66% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,965 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/4 8:14:30 AM | SOL | UP | 29 sec | -0.046% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 8:13:55 AM | NEAR | UP | 64 sec | -0.430% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 8:13:55 AM | DOGE | UP | 64 sec | -0.092% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 8:13:55 AM | XRP | UP | 64 sec | -0.073% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 8:13:24 AM | HYPE | UP | 1.6 min | -0.073% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 8:12:04 AM | BTC | UP | 2.9 min | -0.102% | 2¢ | ❌ Lost | -$0.15 |
| 10/4 8:11:15 AM | ETH | UP | 3.7 min | -0.120% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 8:10:40 AM | BNB | UP | 4.3 min | -0.297% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 8:09:53 AM | ZEC | UP | 5.1 min | -0.567% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 7:59:33 AM | BTC | DOWN | 26 sec | +0.015% | 0¢ | ❌ Lost | $0.00 |
| 10/4 7:59:33 AM | XRP | UP | 26 sec | -0.033% | 0¢ | ❌ Lost | $0.00 |
| 10/4 7:59:17 AM | SOL | DOWN | 43 sec | +0.033% | 0¢ | ❌ Lost | $0.00 |
| 10/4 7:59:17 AM | DOGE | DOWN | 43 sec | +0.021% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 7:58:58 AM | HYPE | DOWN | 62 sec | +0.062% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 7:58:42 AM | BNB | UP | 78 sec | -0.100% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 7:58:26 AM | NEAR | UP | 1.6 min | -0.466% | 0¢ | ❌ Lost | $0.00 |
| 10/4 7:58:11 AM | ETH | DOWN | 1.8 min | +0.053% | 2¢ | ❌ Lost | -$0.15 |
| 10/4 7:56:49 AM | ZEC | DOWN | 3.2 min | +0.252% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 7:44:51 AM | BTC | DOWN | 9 sec | -0.002% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 7:44:20 AM | XRP | DOWN | 39 sec | +0.060% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 7:44:20 AM | BNB | UP | 39 sec | -0.065% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 7:44:20 AM | ETH | UP | 39 sec | -0.033% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 7:44:02 AM | ZEC | DOWN | 58 sec | +0.080% | 0¢ | ❌ Lost | $0.00 |
| 10/4 7:43:46 AM | SOL | DOWN | 74 sec | +0.074% | 2¢ | ❌ Lost | -$0.15 |
| 10/4 7:42:22 AM | HYPE | UP | 2.6 min | -0.144% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 7:42:22 AM | NEAR | DOWN | 2.6 min | +0.391% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 7:29:49 AM | NEAR | UP | 10 sec | -0.271% | 0¢ | ❌ Lost | $0.00 |
| 10/4 7:29:00 AM | DOGE | DOWN | 60 sec | +0.074% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 7:29:00 AM | SOL | DOWN | 60 sec | +0.074% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 7:28:44 AM | ETH | DOWN | 76 sec | +0.063% | 1¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
