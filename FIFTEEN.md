# 15-Minute 1¢ Study

*Updated Sat Oct 10, 8:37 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 962 finished bets | 1% | $35.00 | +33% | +3.64¢ | -$8.85 / $43.85 |

*Expect about **78 buys a day** (~$11.70/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 936 | $11.35 | +11% |
| 5+ min left, hold to the close | 388 | -$1.30 | -2% |
| Volatility model ≥ 5%, sell at 50¢ | 962 | -$9.50 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 13768 | 13761 | 56 (0%) | 1.07% | -$882.50 (-53%) | Hold to the close: -$882.50 (-53%) |

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
| Volatility model | 8916 | 4.1% | 0.4% (39) | -584% | ❌ Worse |
| Momentum model | 8916 | 4.2% | 0.4% (39) | -616% | ❌ Worse |
| Mean-reversion model | 8916 | 6.8% | 0.4% (39) | -681% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 8916 | 39 | -45% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1726 | 14 | -6% | -76% | -76% | -72% |
| Volatility model ≥ 5% | 962 | 10 | +33% | -69% | -68% | -64% |
| Volatility model ≥ 10% | 599 | 8 | +94% | -55% | -55% | -50% |
| Momentum model ≥ 2% | 1528 | 11 | -13% | -77% | -78% | -76% |
| Momentum model ≥ 5% | 936 | 8 | +11% | -72% | -73% | -70% |
| Momentum model ≥ 10% | 643 | 6 | +33% | -63% | -64% | -60% |
| Mean-reversion model ≥ 2% | 3101 | 23 | -19% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2092 | 17 | -10% | -83% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1385 | 13 | +8% | -81% | -81% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 9114 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3444 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1203 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 13761 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 56 | 0% | -$882.50 | -53% | — |
| Sell at 2¢ | 464 | 3% | -$1,503.86 | -90% | 33 sec |
| Sell at 3¢ | 310 | 2% | -$1,503.60 | -90% | 47 sec |
| Sell at 5¢ | 227 | 2% | -$1,476.95 | -89% | 50 sec |
| Sell at 10¢ | 150 | 1% | -$1,400.00 | -84% | 64 sec |
| Sell at 25¢ | 85 | 1% | -$1,287.15 | -77% | 81 sec |
| Sell at 50¢ | 57 | 0% | -$1,141.75 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 384 | 4 | 10% | 3% | -1% | -82% | -86% |
| 2–5 min | 4454 | 28 | 6% | 3% | -38% | -89% | -89% |
| 1–2 min | 3601 | 15 | 3% | 2% | -55% | -94% | -94% |
| Under 1 min | 5318 | 9 | 1% | 0% | -75% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1021 | 6 | 4% | 3% | -29% | -90% | -90% |
| HYPE | 1018 | 3 | 4% | 2% | -63% | -90% | -88% |
| BNB | 1017 | 5 | 4% | 2% | -40% | -91% | -92% |
| DOGE | 1016 | 2 | 3% | 2% | -75% | -92% | -91% |
| ETH | 1011 | 8 | 5% | 3% | -3% | -89% | -88% |
| NEAR | 1009 | 6 | 6% | 2% | -22% | -73% | -74% |
| SOL | 1009 | 1 | 3% | 1% | -87% | -94% | -93% |
| BTC | 1007 | 4 | 5% | 2% | -48% | -88% | -91% |
| XRP | 1006 | 6 | 2% | 1% | -26% | -83% | -83% |
| GOLD | 568 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 555 | 1 | 3% | 1% | -79% | -94% | -94% |
| WTI | 529 | 3 | 3% | 1% | -35% | -94% | -96% |
| COPPER | 490 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 451 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 431 | 3 | 3% | 2% | -35% | -95% | -93% |
| PALLADIUM | 420 | 1 | 1% | 0% | -78% | -98% | -99% |
| EURUSD | 412 | 3 | 3% | 2% | -32% | -72% | -71% |
| GBPUSD | 389 | 1 | 3% | 2% | -76% | -96% | -95% |
| USDJPY | 353 | 3 | 1% | 1% | -21% | -98% | -97% |
| AUDUSD | 25 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 24 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6927 | 29 | 3% | 2% | -52% | -89% | -89% |
| DOWN (bought NO) | 6834 | 27 | 3% | 1% | -54% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1522 | 9 | 2% | 1% | +0% | -71% | -71% |
| 0.05–0.1% | 1590 | 5 | 3% | 1% | -54% | -92% | -92% |
| 0.1–0.2% | 2335 | 8 | 4% | 2% | -57% | -92% | -92% |
| 0.2–0.5% | 2602 | 14 | 5% | 3% | -41% | -89% | -88% |
| Over 0.5% | 1062 | 5 | 6% | 2% | -51% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3525 | 19 | 4% | 2% | -38% | -85% | -86% |
| Morning (6am–12pm) | 3313 | 18 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 3143 | 9 | 3% | 1% | -66% | -90% | -90% |
| Evening (6pm–12am) | 3780 | 10 | 3% | 1% | -70% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,193 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/10 8:29:32 AM | ZEC | DOWN | 28 sec | +0.112% | 0¢ | ❌ Lost | $0.00 |
| 10/10 8:29:16 AM | NEAR | UP | 44 sec | -0.293% | 0¢ | ❌ Lost | $0.00 |
| 10/10 8:26:34 AM | BNB | DOWN | 3.4 min | +0.061% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:26:34 AM | ETH | DOWN | 3.4 min | +0.121% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:26:34 AM | BTC | DOWN | 3.4 min | +0.085% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:26:18 AM | DOGE | DOWN | 3.7 min | +0.252% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:26:18 AM | SOL | DOWN | 3.7 min | +0.194% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:26:02 AM | XRP | DOWN | 4.0 min | +0.193% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:24:26 AM | HYPE | DOWN | 5.5 min | +1.206% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:13:58 AM | BNB | DOWN | 61 sec | +0.013% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 8:13:10 AM | ZEC | UP | 1.8 min | -0.301% | 0¢ | ❌ Lost | $0.00 |
| 10/10 8:13:10 AM | BTC | UP | 1.8 min | -0.045% | 0¢ | ❌ Lost | $0.00 |
| 10/10 8:12:22 AM | NEAR | DOWN | 2.6 min | +0.921% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:12:22 AM | XRP | UP | 2.6 min | -0.157% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:12:06 AM | HYPE | DOWN | 2.9 min | +0.188% | 0¢ | ❌ Lost | $0.00 |
| 10/10 8:10:46 AM | ETH | UP | 4.2 min | -0.085% | 2¢ | ❌ Lost | -$0.15 |
| 10/10 8:10:14 AM | SOL | UP | 4.8 min | -0.184% | 2¢ | ❌ Lost | -$0.15 |
| 10/10 7:59:31 AM | ZEC | DOWN | 28 sec | +0.115% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 7:59:15 AM | NEAR | DOWN | 44 sec | +0.179% | 0¢ | ❌ Lost | $0.00 |
| 10/10 7:58:43 AM | SOL | DOWN | 76 sec | +0.080% | 0¢ | ❌ Lost | $0.00 |
| 10/10 7:58:27 AM | ETH | DOWN | 1.5 min | +0.078% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 7:58:27 AM | XRP | DOWN | 1.5 min | +0.043% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 7:58:11 AM | BTC | DOWN | 1.8 min | +0.038% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 7:57:55 AM | DOGE | UP | 2.1 min | -0.126% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 7:57:06 AM | BNB | DOWN | 2.9 min | +0.032% | 2¢ | ❌ Lost | -$0.15 |
| 10/10 7:44:46 AM | HYPE | DOWN | 14 sec | +0.057% | 0¢ | ❌ Lost | $0.00 |
| 10/10 7:44:46 AM | BNB | UP | 14 sec | -0.043% | 0¢ | ❌ Lost | $0.00 |
| 10/10 7:44:14 AM | SOL | UP | 46 sec | -0.045% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 7:43:10 AM | ETH | UP | 1.8 min | -0.069% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 7:42:05 AM | NEAR | DOWN | 2.9 min | +0.329% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
