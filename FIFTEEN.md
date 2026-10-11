# 15-Minute 1¢ Study

*Updated Sun Oct 11, 4:35 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1135 finished bets | 1% | $45.00 | +37% | +3.96¢ | $23.10 / $21.90 |

*Expect about **83 buys a day** (~$12.46/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1086 | $23.75 | +20% |
| 5+ min left, hold to the close | 404 | -$3.70 | -6% |
| Volatility model ≥ 2%, hold to the close | 1983 | -$13.90 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 14786 | 14779 | 59 (0%) | 1.07% | -$954.20 (-54%) | Hold to the close: -$954.20 (-54%) |

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
| Volatility model | 9922 | 4.5% | 0.4% (42) | -678% | ❌ Worse |
| Momentum model | 9922 | 4.5% | 0.4% (42) | -706% | ❌ Worse |
| Mean-reversion model | 9922 | 7.2% | 0.4% (42) | -782% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 9922 | 42 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1983 | 16 | -6% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 1135 | 12 | +37% | -71% | -70% | -67% |
| Volatility model ≥ 10% | 717 | 8 | +62% | -60% | -60% | -56% |
| Momentum model ≥ 2% | 1748 | 13 | -9% | -78% | -79% | -77% |
| Momentum model ≥ 5% | 1086 | 10 | +20% | -74% | -75% | -72% |
| Momentum model ≥ 10% | 752 | 7 | +34% | -67% | -67% | -63% |
| Mean-reversion model ≥ 2% | 3470 | 25 | -21% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2367 | 19 | -10% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1589 | 13 | -5% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 10120 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3449 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1210 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 14779 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 59 | 0% | -$954.20 | -54% | — |
| Sell at 2¢ | 506 | 3% | -$1,606.64 | -90% | 33 sec |
| Sell at 3¢ | 333 | 2% | -$1,608.33 | -90% | 47 sec |
| Sell at 5¢ | 244 | 2% | -$1,579.60 | -89% | 50 sec |
| Sell at 10¢ | 161 | 1% | -$1,499.29 | -84% | 64 sec |
| Sell at 25¢ | 92 | 1% | -$1,377.68 | -77% | 81 sec |
| Sell at 50¢ | 60 | 0% | -$1,235.20 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 400 | 4 | 10% | 3% | -5% | -82% | -86% |
| 2–5 min | 4780 | 31 | 6% | 3% | -36% | -88% | -89% |
| 1–2 min | 3883 | 15 | 3% | 2% | -58% | -94% | -94% |
| Under 1 min | 5712 | 9 | 1% | 0% | -77% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1135 | 6 | 4% | 3% | -35% | -90% | -90% |
| HYPE | 1134 | 3 | 4% | 2% | -67% | -90% | -89% |
| DOGE | 1128 | 2 | 4% | 2% | -78% | -91% | -90% |
| BNB | 1126 | 5 | 4% | 2% | -46% | -91% | -92% |
| ETH | 1124 | 8 | 5% | 2% | -13% | -90% | -89% |
| SOL | 1123 | 2 | 3% | 1% | -78% | -93% | -92% |
| BTC | 1119 | 5 | 5% | 2% | -41% | -88% | -91% |
| XRP | 1116 | 7 | 2% | 1% | -22% | -84% | -84% |
| NEAR | 1115 | 6 | 5% | 2% | -30% | -75% | -77% |
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
| DOWN (bought NO) | 7356 | 28 | 3% | 2% | -56% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1835 | 9 | 2% | 1% | -18% | -76% | -75% |
| 0.05–0.1% | 1802 | 6 | 3% | 1% | -52% | -92% | -92% |
| 0.1–0.2% | 2585 | 8 | 4% | 2% | -62% | -91% | -92% |
| 0.2–0.5% | 2782 | 16 | 5% | 3% | -37% | -89% | -88% |
| Over 0.5% | 1113 | 5 | 6% | 2% | -54% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3699 | 20 | 4% | 2% | -37% | -85% | -86% |
| Morning (6am–12pm) | 3615 | 20 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 3474 | 9 | 3% | 1% | -69% | -90% | -91% |
| Evening (6pm–12am) | 3991 | 10 | 3% | 1% | -71% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,519 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
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
| 10/11 4:13:50 PM | HYPE | DOWN | 70 sec | +0.169% | 0¢ | ❌ Lost | $0.00 |
| 10/11 4:13:50 PM | USDCAD | UP | 70 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/11 4:13:34 PM | XRP | DOWN | 85 sec | +0.114% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 4:13:34 PM | BNB | DOWN | 85 sec | +0.048% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 4:13:34 PM | ZEC | UP | 85 sec | -0.249% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 4:13:18 PM | GBPUSD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 4:13:18 PM | NEAR | UP | 1.7 min | -0.695% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 4:12:46 PM | SOL | DOWN | 2.2 min | +0.237% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 4:12:31 PM | BTC | DOWN | 2.5 min | +0.149% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 4:12:15 PM | ETH | DOWN | 2.8 min | +0.214% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 4:12:15 PM | USDJPY | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 4:10:39 PM | NATGAS | UP | 4.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/11 4:08:17 PM | WTI | DOWN | 6.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/11 3:59:55 PM | BTC | UP | 4 sec | -0.001% | 0¢ | ❌ Lost | $0.00 |
| 10/11 3:59:40 PM | XRP | DOWN | 20 sec | +0.036% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
