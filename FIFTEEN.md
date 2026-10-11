# 15-Minute 1¢ Study

*Updated Sat Oct 10, 9:47 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1033 finished bets | 1% | $26.90 | +24% | +2.60¢ | $0.65 / $26.25 |

*Expect about **80 buys a day** (~$12.03/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 998 | $3.70 | +3% |
| 5+ min left, hold to the close | 394 | -$2.20 | -4% |
| Volatility model ≥ 5%, sell at 50¢ | 1033 | -$17.60 | -16% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 14200 | 14193 | 56 (0%) | 1.07% | -$933.05 (-54%) | Hold to the close: -$933.05 (-54%) |

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
| Volatility model | 9348 | 4.3% | 0.4% (39) | -635% | ❌ Worse |
| Momentum model | 9348 | 4.3% | 0.4% (39) | -664% | ❌ Worse |
| Mean-reversion model | 9348 | 7.0% | 0.4% (39) | -739% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 9348 | 39 | -48% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1829 | 14 | -11% | -76% | -76% | -73% |
| Volatility model ≥ 5% | 1033 | 10 | +24% | -69% | -68% | -65% |
| Volatility model ≥ 10% | 648 | 8 | +77% | -57% | -57% | -52% |
| Momentum model ≥ 2% | 1615 | 11 | -18% | -77% | -79% | -77% |
| Momentum model ≥ 5% | 998 | 8 | +3% | -73% | -74% | -71% |
| Momentum model ≥ 10% | 691 | 6 | +22% | -65% | -66% | -62% |
| Mean-reversion model ≥ 2% | 3250 | 23 | -23% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2208 | 17 | -15% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1469 | 13 | +2% | -80% | -80% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 9546 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3444 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1203 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 14193 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 56 | 0% | -$933.05 | -54% | — |
| Sell at 2¢ | 483 | 3% | -$1,549.47 | -90% | 33 sec |
| Sell at 3¢ | 319 | 2% | -$1,550.64 | -90% | 47 sec |
| Sell at 5¢ | 233 | 2% | -$1,523.60 | -89% | 50 sec |
| Sell at 10¢ | 152 | 1% | -$1,447.93 | -84% | 64 sec |
| Sell at 25¢ | 87 | 1% | -$1,331.08 | -78% | 81 sec |
| Sell at 50¢ | 57 | 0% | -$1,192.30 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 390 | 4 | 11% | 3% | -3% | -81% | -86% |
| 2–5 min | 4589 | 28 | 6% | 3% | -40% | -89% | -89% |
| 1–2 min | 3723 | 15 | 3% | 2% | -56% | -94% | -93% |
| Under 1 min | 5487 | 9 | 1% | 0% | -76% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1069 | 6 | 4% | 3% | -32% | -90% | -90% |
| HYPE | 1068 | 3 | 4% | 2% | -65% | -90% | -89% |
| DOGE | 1066 | 2 | 4% | 2% | -76% | -91% | -91% |
| BNB | 1064 | 5 | 4% | 2% | -43% | -91% | -92% |
| ETH | 1059 | 8 | 5% | 3% | -8% | -89% | -88% |
| SOL | 1058 | 1 | 3% | 1% | -88% | -94% | -93% |
| BTC | 1056 | 4 | 5% | 2% | -50% | -88% | -91% |
| NEAR | 1054 | 6 | 6% | 2% | -26% | -74% | -75% |
| XRP | 1052 | 6 | 2% | 1% | -29% | -84% | -84% |
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
| UP (bought YES) | 7148 | 29 | 3% | 2% | -53% | -89% | -89% |
| DOWN (bought NO) | 7045 | 27 | 3% | 1% | -56% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1673 | 9 | 2% | 1% | -10% | -73% | -73% |
| 0.05–0.1% | 1693 | 5 | 3% | 1% | -58% | -92% | -92% |
| 0.1–0.2% | 2434 | 8 | 4% | 2% | -59% | -91% | -92% |
| 0.2–0.5% | 2666 | 14 | 5% | 3% | -42% | -89% | -88% |
| Over 0.5% | 1077 | 5 | 6% | 2% | -52% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3525 | 19 | 4% | 2% | -38% | -85% | -86% |
| Morning (6am–12pm) | 3425 | 18 | 4% | 2% | -40% | -91% | -91% |
| Afternoon (12–6pm) | 3332 | 9 | 3% | 1% | -68% | -90% | -90% |
| Evening (6pm–12am) | 3911 | 10 | 3% | 1% | -71% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,375 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/10 9:44:01 PM | XRP | UP | 58 sec | -0.101% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 9:43:47 PM | NEAR | DOWN | 72 sec | +0.243% | 0¢ | ❌ Lost | $0.00 |
| 10/10 9:43:16 PM | HYPE | DOWN | 1.7 min | +0.072% | 4¢ | ❌ Lost | -$0.15 |
| 10/10 9:43:00 PM | SOL | DOWN | 2.0 min | +0.118% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 9:42:44 PM | BTC | DOWN | 2.3 min | +0.062% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 9:42:29 PM | DOGE | DOWN | 2.5 min | +0.154% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 9:41:57 PM | ZEC | DOWN | 3.0 min | +0.257% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 9:41:40 PM | BNB | DOWN | 3.3 min | +0.110% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 9:39:03 PM | ETH | DOWN | 5.9 min | +0.186% | 3¢ | ❌ Lost | -$0.15 |
| 10/10 9:28:19 PM | ETH | UP | 1.7 min | -0.037% | 3¢ | ❌ Lost | -$0.15 |
| 10/10 9:28:03 PM | BTC | UP | 1.9 min | -0.062% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 9:28:03 PM | BNB | UP | 1.9 min | -0.086% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 9:27:47 PM | SOL | UP | 2.2 min | -0.124% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 9:27:32 PM | ZEC | UP | 2.5 min | -0.340% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 9:27:32 PM | DOGE | UP | 2.5 min | -0.373% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 9:27:16 PM | XRP | UP | 2.7 min | -0.201% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 9:25:05 PM | HYPE | UP | 4.9 min | -0.297% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 9:24:34 PM | NEAR | UP | 5.4 min | -1.155% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 9:11:43 PM | HYPE | UP | 3.3 min | -0.234% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 9:11:43 PM | XRP | UP | 3.3 min | -0.286% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 9:11:11 PM | BTC | UP | 3.8 min | -0.134% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 9:10:55 PM | ETH | UP | 4.1 min | -0.146% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 9:10:55 PM | DOGE | UP | 4.1 min | -0.232% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 9:10:08 PM | SOL | UP | 4.8 min | -0.193% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 9:10:08 PM | ZEC | UP | 4.8 min | -0.578% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 9:10:08 PM | BNB | UP | 4.8 min | -0.112% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 9:09:36 PM | NEAR | UP | 5.4 min | -0.910% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:58:48 PM | NEAR | UP | 72 sec | -0.303% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:58:48 PM | BTC | UP | 72 sec | -0.043% | 0¢ | ❌ Lost | $0.00 |
| 10/10 8:58:33 PM | ZEC | DOWN | 87 sec | +0.273% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
