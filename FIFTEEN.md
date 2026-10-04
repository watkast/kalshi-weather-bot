# 15-Minute 1¢ Study

*Updated Sun Oct 4, 7:43 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 185 finished bets | 2% | $14.70 | +54% | +7.95¢ | $14.35 / $0.35 |

*Expect about **29 buys a day** (~$4.30/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 527 | -$0.10 | -0% |
| Volatility model ≥ 5%, hold to the close | 523 | -$0.25 | -0% |
| 5+ min left, sell at 50¢ | 185 | -$7.05 | -26% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 7363 | 7355 | 32 (0%) | 1.07% | -$435.05 (-49%) | Hold to the close: -$435.05 (-49%) |

*In play or awaiting result: 8. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 4819 | 4.2% | 0.4% (20) | -656% | ❌ Worse |
| Momentum model | 4819 | 4.3% | 0.4% (20) | -690% | ❌ Worse |
| Mean-reversion model | 4819 | 7.0% | 0.4% (20) | -767% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 4819 | 20 | -47% | -84% | -84% | -82% |
| Volatility model ≥ 2% | 977 | 7 | -17% | -68% | -68% | -63% |
| Volatility model ≥ 5% | 523 | 4 | -0% | -52% | -52% | -47% |
| Volatility model ≥ 10% | 325 | 4 | +82% | -30% | -32% | -25% |
| Momentum model ≥ 2% | 855 | 5 | -29% | -68% | -71% | -67% |
| Momentum model ≥ 5% | 527 | 4 | -0% | -58% | -62% | -58% |
| Momentum model ≥ 10% | 359 | 3 | +20% | -44% | -45% | -41% |
| Mean-reversion model ≥ 2% | 1722 | 10 | -37% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1162 | 9 | -14% | -78% | -79% | -72% |
| Mean-reversion model ≥ 10% | 763 | 7 | +6% | -76% | -78% | -70% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5016 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 7355 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 32 | 0% | -$435.05 | -49% | — |
| Sell at 2¢ | 293 | 4% | -$778.87 | -88% | 34 sec |
| Sell at 3¢ | 188 | 3% | -$781.73 | -89% | 48 sec |
| Sell at 5¢ | 140 | 2% | -$764.05 | -87% | 61 sec |
| Sell at 10¢ | 94 | 1% | -$717.91 | -81% | 78 sec |
| Sell at 25¢ | 53 | 1% | -$651.62 | -74% | 1.6 min |
| Sell at 50¢ | 31 | 0% | -$575.80 | -65% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 182 | 3 | 13% | 3% | +56% | -78% | -87% |
| 2–5 min | 2382 | 16 | 8% | 4% | -35% | -86% | -86% |
| 1–2 min | 1929 | 8 | 3% | 2% | -55% | -94% | -93% |
| Under 1 min | 2859 | 5 | 1% | 0% | -74% | -87% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 565 | 4 | 5% | 3% | -17% | -88% | -88% |
| DOGE | 562 | 2 | 4% | 1% | -54% | -91% | -91% |
| HYPE | 562 | 2 | 5% | 3% | -57% | -89% | -86% |
| ETH | 560 | 4 | 6% | 3% | -10% | -87% | -86% |
| BTC | 555 | 2 | 5% | 2% | -53% | -87% | -89% |
| BNB | 555 | 2 | 5% | 2% | -57% | -90% | -92% |
| SOL | 554 | 0 | 3% | 1% | -100% | -93% | -92% |
| XRP | 553 | 4 | 2% | 1% | -7% | -72% | -73% |
| NEAR | 550 | 2 | 6% | 3% | -52% | -60% | -62% |
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
| UP (bought YES) | 3704 | 17 | 4% | 2% | -46% | -88% | -88% |
| DOWN (bought NO) | 3651 | 15 | 4% | 2% | -53% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 828 | 5 | 2% | 1% | +1% | -54% | -54% |
| 0.05–0.1% | 846 | 2 | 3% | 1% | -65% | -91% | -93% |
| 0.1–0.2% | 1229 | 4 | 4% | 2% | -58% | -90% | -91% |
| 0.2–0.5% | 1476 | 7 | 6% | 3% | -47% | -87% | -87% |
| Over 0.5% | 635 | 4 | 7% | 3% | -35% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1882 | 8 | 5% | 2% | -50% | -84% | -86% |
| Morning (6am–12pm) | 1902 | 15 | 5% | 3% | -10% | -89% | -88% |
| Afternoon (12–6pm) | 1513 | 3 | 3% | 1% | -76% | -85% | -87% |
| Evening (6pm–12am) | 2058 | 6 | 3% | 2% | -66% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,959 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/4 7:42:22 AM | HYPE | UP | 2.6 min | -0.144% | — | In play | — |
| 10/4 7:42:22 AM | NEAR | DOWN | 2.6 min | +0.391% | — | In play | — |
| 10/4 7:29:49 AM | NEAR | UP | 10 sec | -0.271% | 0¢ | ❌ Lost | $0.00 |
| 10/4 7:29:00 AM | DOGE | DOWN | 60 sec | +0.074% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 7:29:00 AM | SOL | DOWN | 60 sec | +0.074% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 7:28:44 AM | ETH | DOWN | 76 sec | +0.063% | 1¢ | ❌ Lost | $0.00 |
| 10/4 7:28:28 AM | BTC | DOWN | 1.5 min | +0.059% | 0¢ | ❌ Lost | $0.00 |
| 10/4 7:28:28 AM | XRP | DOWN | 1.5 min | +0.133% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 7:27:06 AM | ZEC | UP | 2.9 min | -0.290% | 7¢ | ❌ Lost | -$0.15 |
| 10/4 7:27:06 AM | HYPE | UP | 2.9 min | -0.127% | 3¢ | ❌ Lost | -$0.15 |
| 10/4 7:14:30 AM | NEAR | DOWN | 30 sec | -0.092% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 7:14:15 AM | BTC | DOWN | 44 sec | +0.035% | 0¢ | ❌ Lost | $0.00 |
| 10/4 7:13:56 AM | DOGE | DOWN | 64 sec | +0.075% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 7:13:56 AM | ZEC | DOWN | 64 sec | +0.150% | 0¢ | ❌ Lost | $0.00 |
| 10/4 7:13:56 AM | ETH | DOWN | 64 sec | +0.071% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 7:13:40 AM | SOL | DOWN | 80 sec | +0.075% | 0¢ | ❌ Lost | $0.00 |
| 10/4 7:13:09 AM | XRP | DOWN | 1.8 min | +0.140% | 0¢ | ❌ Lost | $0.00 |
| 10/4 7:13:09 AM | BNB | DOWN | 1.8 min | +0.046% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 7:12:50 AM | HYPE | DOWN | 2.1 min | +0.129% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 6:58:56 AM | NEAR | UP | 64 sec | -0.248% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 6:58:40 AM | DOGE | UP | 80 sec | -0.103% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 6:58:40 AM | SOL | UP | 80 sec | -0.102% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 6:58:24 AM | BNB | DOWN | 1.6 min | +0.017% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 6:57:36 AM | ZEC | UP | 2.4 min | -0.283% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 6:57:20 AM | BTC | UP | 2.6 min | -0.116% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 6:57:04 AM | XRP | UP | 2.9 min | -0.113% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 6:56:13 AM | HYPE | UP | 3.8 min | -0.196% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 6:55:58 AM | ETH | UP | 4.0 min | -0.165% | 2¢ | ❌ Lost | -$0.15 |
| 10/4 6:44:33 AM | HYPE | UP | 27 sec | -0.172% | 0¢ | ❌ Lost | $0.00 |
| 10/4 6:44:33 AM | DOGE | UP | 27 sec | -0.058% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
