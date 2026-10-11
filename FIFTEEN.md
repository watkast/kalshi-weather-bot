# 15-Minute 1¢ Study

*Updated Sun Oct 11, 4:45 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1137 finished bets | 1% | $44.70 | +36% | +3.93¢ | $22.95 / $21.75 |

*Expect about **83 buys a day** (~$12.48/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1087 | $23.60 | +20% |
| 5+ min left, hold to the close | 404 | -$3.70 | -6% |
| Volatility model ≥ 2%, hold to the close | 1987 | -$14.20 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 14801 | 14788 | 59 (0%) | 1.07% | -$954.95 (-54%) | Hold to the close: -$954.95 (-54%) |

*In play or awaiting result: 12. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 9931 | 4.5% | 0.4% (42) | -678% | ❌ Worse |
| Momentum model | 9931 | 4.5% | 0.4% (42) | -706% | ❌ Worse |
| Mean-reversion model | 9931 | 7.2% | 0.4% (42) | -782% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 9931 | 42 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1987 | 16 | -6% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 1137 | 12 | +36% | -71% | -70% | -67% |
| Volatility model ≥ 10% | 718 | 8 | +62% | -60% | -60% | -56% |
| Momentum model ≥ 2% | 1751 | 13 | -9% | -78% | -79% | -77% |
| Momentum model ≥ 5% | 1087 | 10 | +20% | -74% | -75% | -72% |
| Momentum model ≥ 10% | 753 | 7 | +33% | -67% | -67% | -63% |
| Mean-reversion model ≥ 2% | 3477 | 25 | -21% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2369 | 19 | -11% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1591 | 13 | -5% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 10129 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3449 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1210 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 14788 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 59 | 0% | -$954.95 | -54% | — |
| Sell at 2¢ | 506 | 3% | -$1,607.39 | -90% | 33 sec |
| Sell at 3¢ | 333 | 2% | -$1,609.08 | -90% | 47 sec |
| Sell at 5¢ | 244 | 2% | -$1,580.35 | -89% | 50 sec |
| Sell at 10¢ | 161 | 1% | -$1,500.04 | -84% | 64 sec |
| Sell at 25¢ | 92 | 1% | -$1,378.43 | -77% | 81 sec |
| Sell at 50¢ | 60 | 0% | -$1,235.95 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 400 | 4 | 10% | 3% | -5% | -82% | -86% |
| 2–5 min | 4782 | 31 | 6% | 3% | -36% | -88% | -89% |
| 1–2 min | 3887 | 15 | 3% | 2% | -58% | -94% | -94% |
| Under 1 min | 5715 | 9 | 1% | 0% | -77% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1136 | 6 | 4% | 3% | -35% | -90% | -90% |
| HYPE | 1135 | 3 | 4% | 2% | -67% | -90% | -89% |
| DOGE | 1129 | 2 | 4% | 2% | -78% | -91% | -90% |
| BNB | 1127 | 5 | 4% | 2% | -46% | -91% | -92% |
| ETH | 1125 | 8 | 5% | 2% | -13% | -90% | -89% |
| SOL | 1124 | 2 | 3% | 1% | -78% | -93% | -92% |
| BTC | 1120 | 5 | 5% | 2% | -41% | -88% | -91% |
| XRP | 1117 | 7 | 2% | 1% | -22% | -84% | -84% |
| NEAR | 1116 | 6 | 5% | 2% | -30% | -75% | -77% |
| GOLD | 568 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 556 | 1 | 3% | 1% | -79% | -94% | -94% |
| WTI | 530 | 3 | 3% | 1% | -36% | -94% | -96% |
| COPPER | 490 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 452 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 433 | 3 | 3% | 2% | -35% | -95% | -93% |
| PALLADIUM | 420 | 1 | 1% | 0% | -78% | -98% | -99% |
| EURUSD | 413 | 3 | 3% | 2% | -32% | -72% | -71% |
| GBPUSD | 391 | 1 | 3% | 2% | -76% | -96% | -95% |
| USDJPY | 356 | 3 | 1% | 1% | -21% | -98% | -97% |
| USDCAD | 25 | 0 | 0% | 0% | -100% | -100% | -100% |
| AUDUSD | 25 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 7423 | 31 | 3% | 2% | -51% | -89% | -89% |
| DOWN (bought NO) | 7365 | 28 | 3% | 2% | -56% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1837 | 9 | 2% | 1% | -19% | -76% | -75% |
| 0.05–0.1% | 1805 | 6 | 3% | 1% | -52% | -92% | -92% |
| 0.1–0.2% | 2587 | 8 | 4% | 2% | -62% | -91% | -92% |
| 0.2–0.5% | 2784 | 16 | 5% | 3% | -37% | -89% | -88% |
| Over 0.5% | 1113 | 5 | 6% | 2% | -54% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3699 | 20 | 4% | 2% | -37% | -85% | -86% |
| Morning (6am–12pm) | 3615 | 20 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 3483 | 9 | 3% | 1% | -69% | -90% | -91% |
| Evening (6pm–12am) | 3991 | 10 | 3% | 1% | -71% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,522 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/11 4:44:58 PM | AUDUSD | DOWN | 1 sec | — | 0¢ | In play | — |
| 10/11 4:44:58 PM | GOLD | UP | 1 sec | — | 0¢ | In play | — |
| 10/11 4:44:58 PM | WTI | UP | 1 sec | — | 1¢ | In play | — |
| 10/11 4:44:11 PM | XRP | DOWN | 49 sec | +0.043% | 0¢ | ❌ Lost | $0.00 |
| 10/11 4:44:11 PM | ETH | DOWN | 49 sec | +0.043% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 4:44:11 PM | USDJPY | DOWN | 49 sec | — | 0¢ | In play | — |
| 10/11 4:44:11 PM | SOL | DOWN | 49 sec | +0.084% | 0¢ | ❌ Lost | $0.00 |
| 10/11 4:43:55 PM | BTC | DOWN | 65 sec | +0.057% | 0¢ | ❌ Lost | $0.00 |
| 10/11 4:43:39 PM | GBPUSD | UP | 80 sec | — | 0¢ | In play | — |
| 10/11 4:43:23 PM | DOGE | DOWN | 1.6 min | +0.104% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 4:43:23 PM | NEAR | DOWN | 1.6 min | +0.352% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 4:43:23 PM | ZEC | DOWN | 1.6 min | +0.184% | 0¢ | ❌ Lost | $0.00 |
| 10/11 4:42:04 PM | BNB | DOWN | 2.9 min | +0.054% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 4:42:04 PM | EURUSD | UP | 2.9 min | — | 0¢ | In play | — |
| 10/11 4:40:29 PM | HYPE | DOWN | 4.5 min | +0.315% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 4:29:54 PM | GBPUSD | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 4:29:38 PM | ETH | DOWN | 21 sec | +0.007% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 4:29:38 PM | BNB | UP | 21 sec | -0.033% | 0¢ | ❌ Lost | $0.00 |
| 10/11 4:29:22 PM | ZEC | DOWN | 37 sec | +0.122% | 0¢ | ❌ Lost | $0.00 |
| 10/11 4:29:06 PM | BTC | DOWN | 53 sec | +0.029% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 4:29:06 PM | NATGAS | DOWN | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 4:28:50 PM | SILVER | DOWN | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 4:28:19 PM | DOGE | DOWN | 1.7 min | +0.089% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 4:28:19 PM | HYPE | DOWN | 1.7 min | +0.147% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 4:28:19 PM | XRP | DOWN | 1.7 min | +0.157% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 4:28:19 PM | PLATINUM | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/11 4:27:30 PM | SOL | DOWN | 2.5 min | +0.188% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 4:27:14 PM | NEAR | DOWN | 2.8 min | +0.562% | 0¢ | ❌ Lost | $0.00 |
| 10/11 4:14:22 PM | DOGE | DOWN | 38 sec | -0.016% | 0¢ | ❌ Lost | $0.00 |
| 10/11 4:14:22 PM | EURUSD | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
