# 15-Minute 1¢ Study

*Updated Mon Oct 12, 10:16 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1191 finished bets | 1% | $38.85 | +30% | +3.26¢ | $33.80 / $5.05 |

*Expect about **83 buys a day** (~$12.41/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1140 | $18.05 | +15% |
| 5+ min left, hold to the close | 424 | -$6.70 | -11% |
| Volatility model ≥ 2%, hold to the close | 2094 | -$13.55 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 15640 | 15633 | 62 (0%) | 1.07% | -$1,017.80 (-54%) | Hold to the close: -$1,017.80 (-54%) |

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
| Volatility model | 10403 | 4.5% | 0.4% (45) | -672% | ❌ Worse |
| Momentum model | 10403 | 4.5% | 0.4% (45) | -698% | ❌ Worse |
| Mean-reversion model | 10403 | 7.2% | 0.4% (45) | -777% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 10403 | 45 | -46% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2094 | 17 | -5% | -77% | -77% | -74% |
| Volatility model ≥ 5% | 1191 | 12 | +30% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 751 | 8 | +55% | -62% | -62% | -58% |
| Momentum model ≥ 2% | 1843 | 14 | -7% | -79% | -80% | -78% |
| Momentum model ≥ 5% | 1140 | 10 | +15% | -75% | -76% | -73% |
| Momentum model ≥ 10% | 788 | 7 | +27% | -68% | -68% | -64% |
| Mean-reversion model ≥ 2% | 3639 | 26 | -22% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2488 | 20 | -10% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1664 | 14 | -2% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 10601 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3712 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1320 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 15633 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 62 | 0% | -$1,017.80 | -54% | — |
| Sell at 2¢ | 535 | 3% | -$1,704.70 | -90% | 33 sec |
| Sell at 3¢ | 355 | 2% | -$1,705.35 | -90% | 47 sec |
| Sell at 5¢ | 260 | 2% | -$1,674.80 | -89% | 50 sec |
| Sell at 10¢ | 170 | 1% | -$1,593.10 | -84% | 64 sec |
| Sell at 25¢ | 96 | 1% | -$1,470.04 | -78% | 80 sec |
| Sell at 50¢ | 64 | 0% | -$1,313.80 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 420 | 4 | 11% | 3% | -10% | -81% | -86% |
| 2–5 min | 5030 | 32 | 6% | 3% | -38% | -88% | -88% |
| 1–2 min | 4130 | 16 | 3% | 2% | -58% | -94% | -94% |
| Under 1 min | 6049 | 10 | 1% | 0% | -76% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1190 | 7 | 4% | 3% | -28% | -90% | -90% |
| HYPE | 1188 | 4 | 4% | 2% | -58% | -90% | -89% |
| DOGE | 1181 | 2 | 4% | 2% | -79% | -91% | -90% |
| BNB | 1179 | 5 | 4% | 2% | -48% | -91% | -92% |
| ETH | 1178 | 8 | 5% | 2% | -17% | -89% | -89% |
| SOL | 1178 | 2 | 3% | 1% | -79% | -93% | -92% |
| BTC | 1173 | 5 | 5% | 2% | -43% | -88% | -91% |
| NEAR | 1168 | 7 | 5% | 2% | -21% | -76% | -77% |
| XRP | 1166 | 7 | 2% | 1% | -25% | -84% | -85% |
| GOLD | 608 | 0 | 3% | 1% | -100% | -92% | -94% |
| SILVER | 595 | 1 | 3% | 1% | -81% | -94% | -94% |
| WTI | 571 | 3 | 3% | 1% | -40% | -94% | -96% |
| COPPER | 531 | 0 | 1% | 1% | -100% | -98% | -98% |
| PLATINUM | 491 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 458 | 3 | 3% | 2% | -39% | -95% | -94% |
| PALLADIUM | 458 | 1 | 1% | 0% | -80% | -98% | -98% |
| EURUSD | 442 | 3 | 3% | 2% | -37% | -74% | -73% |
| GBPUSD | 422 | 1 | 2% | 1% | -78% | -96% | -96% |
| USDJPY | 382 | 3 | 1% | 1% | -27% | -98% | -97% |
| USDCAD | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| AUDUSD | 35 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 7867 | 34 | 3% | 2% | -50% | -90% | -89% |
| DOWN (bought NO) | 7766 | 28 | 3% | 2% | -58% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1912 | 9 | 2% | 1% | -21% | -77% | -76% |
| 0.05–0.1% | 1892 | 6 | 3% | 1% | -54% | -92% | -92% |
| 0.1–0.2% | 2719 | 9 | 4% | 2% | -59% | -91% | -92% |
| 0.2–0.5% | 2933 | 18 | 6% | 3% | -33% | -89% | -88% |
| Over 0.5% | 1142 | 5 | 6% | 2% | -55% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4019 | 20 | 4% | 2% | -43% | -86% | -86% |
| Morning (6am–12pm) | 3680 | 20 | 4% | 2% | -37% | -91% | -91% |
| Afternoon (12–6pm) | 3575 | 9 | 3% | 1% | -70% | -90% | -91% |
| Evening (6pm–12am) | 4359 | 13 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,506 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/12 10:14:32 AM | USDCAD | DOWN | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 10:14:16 AM | ETH | DOWN | 44 sec | +0.025% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 10:14:16 AM | NEAR | UP | 44 sec | -0.290% | 0¢ | ❌ Lost | $0.00 |
| 10/12 10:13:59 AM | ZEC | UP | 60 sec | -0.318% | 0¢ | ❌ Lost | $0.00 |
| 10/12 10:13:59 AM | NATGAS | UP | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 10:13:43 AM | DOGE | DOWN | 76 sec | +0.085% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 10:13:43 AM | PALLADIUM | DOWN | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 10:13:27 AM | SILVER | DOWN | 1.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 10:11:01 AM | SOL | DOWN | 4.0 min | +0.207% | 5¢ | ❌ Lost | -$0.15 |
| 10/12 10:10:28 AM | HYPE | DOWN | 4.5 min | +0.333% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 10:10:28 AM | BNB | DOWN | 4.5 min | +0.224% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 10:10:28 AM | XRP | DOWN | 4.5 min | +0.363% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 10:10:12 AM | PLATINUM | DOWN | 4.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 10:10:12 AM | BTC | DOWN | 4.8 min | +0.265% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 9:59:53 AM | USDCAD | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 9:59:53 AM | USDJPY | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 9:59:53 AM | AUDUSD | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 9:59:37 AM | ETH | DOWN | 22 sec | +0.033% | 0¢ | ❌ Lost | $0.00 |
| 10/12 9:59:37 AM | SOL | UP | 22 sec | -0.072% | 0¢ | ❌ Lost | $0.00 |
| 10/12 9:59:37 AM | HYPE | UP | 22 sec | -0.036% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 9:59:23 AM | ZEC | DOWN | 37 sec | +0.097% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 9:59:23 AM | BNB | DOWN | 37 sec | -0.035% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 9:59:06 AM | SILVER | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 9:59:06 AM | NEAR | DOWN | 54 sec | +0.081% | 0¢ | ❌ Lost | $0.00 |
| 10/12 9:58:50 AM | GOLD | UP | 70 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 9:58:34 AM | DOGE | UP | 86 sec | -0.187% | 0¢ | ❌ Lost | $0.00 |
| 10/12 9:58:34 AM | WTI | DOWN | 86 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 9:58:18 AM | EURUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 9:58:18 AM | NATGAS | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 9:44:45 AM | ETH | DOWN | 14 sec | -0.023% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
