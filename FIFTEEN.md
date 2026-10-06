# 15-Minute 1¢ Study

*Updated Tue Oct 6, 11:18 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 663 finished bets | 1% | $26.90 | +38% | +4.06¢ | -$8.00 / $34.90 |

*Expect about **79 buys a day** (~$11.78/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 245 | $19.70 | +54% |
| Momentum model ≥ 5%, hold to the close | 662 | $13.65 | +19% |
| Mean-reversion model ≥ 5%, hold to the close | 1457 | $13.00 | +7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 9647 | 9641 | 45 (0%) | 1.07% | -$531.00 (-46%) | Hold to the close: -$531.00 (-46%) |

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
| Volatility model | 6293 | 4.1% | 0.5% (32) | -545% | ❌ Worse |
| Momentum model | 6293 | 4.1% | 0.5% (32) | -575% | ❌ Worse |
| Mean-reversion model | 6293 | 6.7% | 0.5% (32) | -627% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6293 | 32 | -36% | -86% | -86% | -83% |
| Volatility model ≥ 2% | 1226 | 11 | +4% | -72% | -72% | -68% |
| Volatility model ≥ 5% | 663 | 7 | +38% | -60% | -59% | -56% |
| Volatility model ≥ 10% | 407 | 5 | +85% | -41% | -42% | -37% |
| Momentum model ≥ 2% | 1089 | 9 | -0% | -73% | -74% | -72% |
| Momentum model ≥ 5% | 662 | 6 | +19% | -65% | -67% | -64% |
| Momentum model ≥ 10% | 458 | 5 | +58% | -53% | -54% | -51% |
| Mean-reversion model ≥ 2% | 2161 | 18 | -9% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1457 | 14 | +7% | -80% | -80% | -74% |
| Mean-reversion model ≥ 10% | 958 | 10 | +21% | -78% | -79% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6490 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2381 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 770 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 9641 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 45 | 0% | -$531.00 | -46% | — |
| Sell at 2¢ | 355 | 4% | -$1,040.70 | -90% | 33 sec |
| Sell at 3¢ | 234 | 2% | -$1,041.74 | -90% | 47 sec |
| Sell at 5¢ | 174 | 2% | -$1,019.90 | -88% | 50 sec |
| Sell at 10¢ | 119 | 1% | -$963.11 | -83% | 65 sec |
| Sell at 25¢ | 68 | 1% | -$865.92 | -75% | 82 sec |
| Sell at 50¢ | 44 | 0% | -$752.00 | -65% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 242 | 4 | 10% | 3% | +56% | -82% | -88% |
| 2–5 min | 3108 | 24 | 7% | 3% | -25% | -87% | -87% |
| 1–2 min | 2545 | 11 | 3% | 2% | -53% | -94% | -93% |
| Under 1 min | 3743 | 6 | 1% | 0% | -76% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 735 | 6 | 5% | 3% | -2% | -89% | -89% |
| HYPE | 725 | 3 | 5% | 3% | -49% | -89% | -87% |
| DOGE | 724 | 2 | 4% | 1% | -64% | -91% | -91% |
| ETH | 722 | 7 | 6% | 3% | +22% | -87% | -86% |
| BNB | 719 | 3 | 4% | 2% | -49% | -91% | -92% |
| BTC | 717 | 4 | 5% | 3% | -27% | -87% | -89% |
| SOL | 717 | 0 | 3% | 1% | -100% | -93% | -92% |
| XRP | 716 | 5 | 2% | 1% | -12% | -79% | -79% |
| NEAR | 715 | 4 | 6% | 3% | -27% | -67% | -68% |
| GOLD | 402 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 384 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 364 | 2 | 2% | 1% | -40% | -95% | -97% |
| COPPER | 342 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 305 | 0 | 0% | 0% | -100% | -99% | -99% |
| NATGAS | 294 | 3 | 3% | 2% | -5% | -94% | -92% |
| PALLADIUM | 290 | 1 | 2% | 1% | -68% | -97% | -98% |
| EURUSD | 278 | 1 | 4% | 3% | -66% | -93% | -92% |
| GBPUSD | 267 | 1 | 3% | 2% | -65% | -94% | -94% |
| USDJPY | 225 | 3 | 2% | 1% | +24% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4861 | 23 | 4% | 2% | -44% | -89% | -89% |
| DOWN (bought NO) | 4780 | 22 | 4% | 2% | -47% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1065 | 7 | 2% | 1% | +13% | -62% | -61% |
| 0.05–0.1% | 1115 | 4 | 3% | 1% | -47% | -91% | -92% |
| 0.1–0.2% | 1627 | 6 | 4% | 2% | -53% | -91% | -91% |
| 0.2–0.5% | 1907 | 12 | 6% | 3% | -31% | -88% | -87% |
| Over 0.5% | 774 | 5 | 7% | 3% | -34% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2570 | 15 | 4% | 2% | -32% | -87% | -88% |
| Morning (6am–12pm) | 2492 | 17 | 5% | 3% | -22% | -90% | -89% |
| Afternoon (12–6pm) | 1943 | 6 | 3% | 1% | -63% | -86% | -88% |
| Evening (6pm–12am) | 2636 | 7 | 3% | 1% | -69% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,032 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/6 11:14:50 AM | COPPER | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 11:14:03 AM | XRP | UP | 56 sec | -0.140% | 0¢ | ❌ Lost | $0.00 |
| 10/6 11:14:03 AM | SOL | UP | 56 sec | -0.083% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 11:13:47 AM | BTC | UP | 72 sec | -0.093% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 11:13:47 AM | ETH | UP | 72 sec | -0.059% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 11:13:31 AM | WTI | DOWN | 88 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 11:13:31 AM | NATGAS | DOWN | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 11:13:15 AM | HYPE | UP | 1.7 min | -0.275% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 11:12:27 AM | DOGE | UP | 2.5 min | -0.336% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 11:11:39 AM | NEAR | UP | 3.3 min | -0.741% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 11:11:39 AM | SILVER | DOWN | 3.3 min | — | 3¢ | ❌ Lost | -$0.15 |
| 10/6 11:11:07 AM | BNB | UP | 3.9 min | -0.336% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 11:10:51 AM | ZEC | UP | 4.2 min | -0.683% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 11:10:03 AM | GOLD | DOWN | 5.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 10:59:45 AM | NATGAS | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 10:59:29 AM | ZEC | UP | 30 sec | -0.092% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 10:59:29 AM | COPPER | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 10:59:13 AM | HYPE | UP | 46 sec | -0.126% | 0¢ | ❌ Lost | $0.00 |
| 10/6 10:59:13 AM | XRP | DOWN | 46 sec | +0.033% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 10:59:03 AM | DOGE | UP | 57 sec | -0.131% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 10:58:47 AM | SOL | UP | 72 sec | -0.137% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 10:58:31 AM | BNB | UP | 89 sec | -0.078% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 10:58:31 AM | USDJPY | DOWN | 89 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 10:58:15 AM | BTC | UP | 1.8 min | -0.132% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 10:58:15 AM | ETH | UP | 1.8 min | -0.114% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 10:57:58 AM | NEAR | UP | 2.0 min | -0.435% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 10:55:50 AM | GOLD | UP | 4.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 10:44:50 AM | WTI | UP | 10 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/6 10:44:34 AM | NEAR | UP | 26 sec | -0.125% | 0¢ | ❌ Lost | $0.00 |
| 10/6 10:44:18 AM | BNB | UP | 42 sec | -0.077% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
