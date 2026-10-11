# 15-Minute 1¢ Study

*Updated Sun Oct 11, 2:02 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1119 finished bets | 1% | $46.35 | +38% | +4.14¢ | $23.70 / $22.65 |

*Expect about **83 buys a day** (~$12.38/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1071 | $25.10 | +22% |
| 5+ min left, hold to the close | 402 | -$3.40 | -6% |
| Volatility model ≥ 2%, hold to the close | 1956 | -$11.35 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 14686 | 14679 | 59 (0%) | 1.07% | -$943.25 (-53%) | Hold to the close: -$943.25 (-53%) |

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
| Volatility model | 9834 | 4.5% | 0.4% (42) | -673% | ❌ Worse |
| Momentum model | 9834 | 4.5% | 0.4% (42) | -700% | ❌ Worse |
| Mean-reversion model | 9834 | 7.2% | 0.4% (42) | -777% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 9834 | 42 | -46% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1956 | 16 | -5% | -76% | -76% | -73% |
| Volatility model ≥ 5% | 1119 | 12 | +38% | -70% | -69% | -67% |
| Volatility model ≥ 10% | 705 | 8 | +64% | -60% | -59% | -56% |
| Momentum model ≥ 2% | 1721 | 13 | -8% | -78% | -79% | -77% |
| Momentum model ≥ 5% | 1071 | 10 | +22% | -74% | -75% | -71% |
| Momentum model ≥ 10% | 742 | 7 | +35% | -66% | -67% | -63% |
| Mean-reversion model ≥ 2% | 3437 | 25 | -20% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2347 | 19 | -10% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1574 | 13 | -4% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 10032 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3444 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1203 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 14679 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 59 | 0% | -$943.25 | -53% | — |
| Sell at 2¢ | 505 | 3% | -$1,595.95 | -90% | 33 sec |
| Sell at 3¢ | 333 | 2% | -$1,597.38 | -90% | 47 sec |
| Sell at 5¢ | 244 | 2% | -$1,568.65 | -89% | 50 sec |
| Sell at 10¢ | 161 | 1% | -$1,488.34 | -84% | 64 sec |
| Sell at 25¢ | 92 | 1% | -$1,366.73 | -77% | 81 sec |
| Sell at 50¢ | 60 | 0% | -$1,224.25 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 398 | 4 | 11% | 3% | -5% | -81% | -86% |
| 2–5 min | 4749 | 31 | 6% | 3% | -36% | -88% | -89% |
| 1–2 min | 3851 | 15 | 3% | 2% | -58% | -94% | -94% |
| Under 1 min | 5677 | 9 | 1% | 0% | -77% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1125 | 6 | 4% | 3% | -34% | -90% | -90% |
| HYPE | 1124 | 3 | 4% | 2% | -67% | -90% | -89% |
| DOGE | 1119 | 2 | 4% | 2% | -78% | -91% | -90% |
| BNB | 1116 | 5 | 4% | 2% | -46% | -91% | -92% |
| ETH | 1115 | 8 | 5% | 2% | -12% | -89% | -89% |
| SOL | 1113 | 2 | 3% | 1% | -77% | -93% | -92% |
| BTC | 1109 | 5 | 5% | 2% | -40% | -88% | -91% |
| XRP | 1106 | 7 | 2% | 1% | -21% | -84% | -84% |
| NEAR | 1105 | 6 | 5% | 2% | -29% | -75% | -76% |
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
| UP (bought YES) | 7376 | 31 | 3% | 2% | -51% | -89% | -89% |
| DOWN (bought NO) | 7303 | 28 | 3% | 2% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1814 | 9 | 2% | 1% | -18% | -75% | -75% |
| 0.05–0.1% | 1785 | 6 | 3% | 1% | -52% | -92% | -92% |
| 0.1–0.2% | 2564 | 8 | 4% | 2% | -61% | -91% | -92% |
| 0.2–0.5% | 2760 | 16 | 5% | 3% | -36% | -89% | -88% |
| Over 0.5% | 1106 | 5 | 6% | 2% | -53% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3699 | 20 | 4% | 2% | -37% | -85% | -86% |
| Morning (6am–12pm) | 3615 | 20 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 3374 | 9 | 3% | 1% | -68% | -90% | -90% |
| Evening (6pm–12am) | 3991 | 10 | 3% | 1% | -71% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,493 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/11 1:59:52 PM | DOGE | UP | 7 sec | -0.039% | 0¢ | ❌ Lost | $0.00 |
| 10/11 1:59:52 PM | BNB | DOWN | 7 sec | -0.012% | 0¢ | ❌ Lost | $0.00 |
| 10/11 1:59:52 PM | HYPE | UP | 7 sec | -0.024% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 1:59:37 PM | NEAR | UP | 22 sec | -0.222% | 0¢ | ❌ Lost | $0.00 |
| 10/11 1:59:37 PM | ETH | UP | 22 sec | -0.006% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 1:59:21 PM | SOL | UP | 38 sec | -0.024% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 1:58:49 PM | XRP | DOWN | 71 sec | +0.064% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 1:58:16 PM | BTC | UP | 1.7 min | -0.069% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 1:57:14 PM | ZEC | DOWN | 2.8 min | +0.299% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 1:44:40 PM | SOL | DOWN | 19 sec | +0.044% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 1:44:40 PM | XRP | DOWN | 19 sec | +0.028% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 1:44:40 PM | HYPE | UP | 19 sec | -0.030% | 0¢ | ❌ Lost | $0.00 |
| 10/11 1:44:24 PM | BTC | DOWN | 35 sec | +0.045% | 0¢ | ❌ Lost | $0.00 |
| 10/11 1:44:08 PM | NEAR | UP | 51 sec | -0.425% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 1:43:37 PM | DOGE | DOWN | 82 sec | +0.099% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 1:41:58 PM | ETH | DOWN | 3.0 min | +0.115% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 1:40:23 PM | ZEC | DOWN | 4.6 min | +0.658% | 0¢ | ❌ Lost | $0.00 |
| 10/11 1:29:36 PM | ETH | UP | 24 sec | -0.022% | 0¢ | ❌ Lost | $0.00 |
| 10/11 1:29:36 PM | SOL | UP | 24 sec | -0.065% | 0¢ | ❌ Lost | $0.00 |
| 10/11 1:29:20 PM | BTC | UP | 40 sec | -0.023% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 1:29:20 PM | NEAR | UP | 40 sec | -0.376% | 0¢ | ❌ Lost | $0.00 |
| 10/11 1:29:04 PM | BNB | DOWN | 56 sec | +0.013% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 1:29:04 PM | HYPE | DOWN | 56 sec | +0.111% | 0¢ | ❌ Lost | $0.00 |
| 10/11 1:28:15 PM | ZEC | UP | 1.8 min | -0.269% | 0¢ | ❌ Lost | $0.00 |
| 10/11 1:14:32 PM | XRP | DOWN | 28 sec | +0.050% | 0¢ | ❌ Lost | $0.00 |
| 10/11 1:14:16 PM | BTC | DOWN | 44 sec | +0.044% | 0¢ | ❌ Lost | $0.00 |
| 10/11 1:14:16 PM | DOGE | DOWN | 44 sec | +0.083% | 0¢ | ❌ Lost | $0.00 |
| 10/11 1:14:16 PM | ETH | DOWN | 44 sec | +0.053% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 1:14:16 PM | BNB | DOWN | 44 sec | +0.027% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 1:13:45 PM | SOL | UP | 74 sec | -0.108% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
