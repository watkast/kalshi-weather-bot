# 15-Minute 1¢ Study

*Updated Tue Oct 13, 11:28 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1273 finished bets | 1% | $42.65 | +31% | +3.35¢ | $29.90 / $12.75 |

*Expect about **82 buys a day** (~$12.36/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1219 | $22.75 | +17% |
| 5+ min left, hold to the close | 475 | -$14.35 | -20% |
| Volatility model ≥ 5%, sell at 50¢ | 1273 | -$16.35 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 16702 | 16692 | 63 (0%) | 1.07% | -$1,139.25 (-56%) | Hold to the close: -$1,139.25 (-56%) |

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
| Volatility model | 10999 | 4.5% | 0.4% (46) | -658% | ❌ Worse |
| Momentum model | 10999 | 4.4% | 0.4% (46) | -686% | ❌ Worse |
| Mean-reversion model | 10999 | 7.2% | 0.4% (46) | -770% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 10999 | 46 | -48% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2269 | 18 | -8% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1273 | 13 | +31% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 787 | 9 | +64% | -63% | -63% | -59% |
| Momentum model ≥ 2% | 1994 | 15 | -9% | -79% | -80% | -78% |
| Momentum model ≥ 5% | 1219 | 11 | +17% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 830 | 8 | +36% | -69% | -69% | -64% |
| Mean-reversion model ≥ 2% | 3944 | 27 | -25% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2693 | 20 | -18% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 1772 | 14 | -9% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 11197 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4028 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1467 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 16692 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 63 | 0% | -$1,139.25 | -56% | — |
| Sell at 2¢ | 568 | 3% | -$1,831.57 | -91% | 33 sec |
| Sell at 3¢ | 376 | 2% | -$1,832.61 | -91% | 46 sec |
| Sell at 5¢ | 271 | 2% | -$1,803.10 | -89% | 49 sec |
| Sell at 10¢ | 174 | 1% | -$1,723.31 | -85% | 63 sec |
| Sell at 25¢ | 99 | 1% | -$1,595.56 | -79% | 79 sec |
| Sell at 50¢ | 64 | 0% | -$1,435.25 | -71% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 471 | 4 | 11% | 3% | -20% | -80% | -86% |
| 2–5 min | 5387 | 32 | 6% | 3% | -42% | -88% | -89% |
| 1–2 min | 4406 | 16 | 3% | 2% | -61% | -94% | -94% |
| Under 1 min | 6424 | 11 | 1% | 0% | -75% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1256 | 7 | 4% | 2% | -31% | -90% | -90% |
| HYPE | 1253 | 4 | 4% | 2% | -61% | -90% | -89% |
| DOGE | 1248 | 2 | 4% | 2% | -80% | -91% | -90% |
| ETH | 1246 | 8 | 4% | 2% | -22% | -90% | -89% |
| BNB | 1246 | 5 | 4% | 2% | -51% | -91% | -91% |
| SOL | 1244 | 2 | 3% | 1% | -80% | -93% | -92% |
| BTC | 1238 | 6 | 5% | 2% | -36% | -88% | -90% |
| NEAR | 1233 | 7 | 5% | 2% | -26% | -77% | -78% |
| XRP | 1233 | 7 | 2% | 1% | -30% | -85% | -85% |
| GOLD | 662 | 0 | 3% | 1% | -100% | -93% | -94% |
| SILVER | 643 | 1 | 3% | 1% | -82% | -94% | -94% |
| WTI | 617 | 3 | 3% | 1% | -44% | -94% | -96% |
| COPPER | 573 | 0 | 1% | 1% | -100% | -98% | -97% |
| PLATINUM | 536 | 0 | 0% | 0% | -100% | -99% | -99% |
| PALLADIUM | 503 | 1 | 1% | 0% | -81% | -98% | -98% |
| NATGAS | 494 | 3 | 3% | 2% | -43% | -95% | -94% |
| EURUSD | 481 | 3 | 3% | 2% | -42% | -76% | -75% |
| GBPUSD | 456 | 1 | 2% | 1% | -80% | -96% | -96% |
| USDJPY | 415 | 3 | 1% | 1% | -33% | -98% | -97% |
| AUDUSD | 60 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 55 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8427 | 34 | 3% | 2% | -53% | -90% | -90% |
| DOWN (bought NO) | 8265 | 29 | 3% | 2% | -59% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1965 | 10 | 2% | 1% | -15% | -77% | -76% |
| 0.05–0.1% | 1986 | 6 | 3% | 1% | -56% | -92% | -92% |
| 0.1–0.2% | 2845 | 9 | 4% | 2% | -61% | -91% | -92% |
| 0.2–0.5% | 3161 | 18 | 5% | 3% | -38% | -89% | -89% |
| Over 0.5% | 1237 | 5 | 6% | 2% | -58% | -89% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4344 | 20 | 4% | 2% | -47% | -87% | -87% |
| Morning (6am–12pm) | 3880 | 20 | 4% | 2% | -40% | -91% | -91% |
| Afternoon (12–6pm) | 3818 | 9 | 3% | 1% | -72% | -91% | -91% |
| Evening (6pm–12am) | 4650 | 14 | 3% | 1% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,486 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/13 11:27:50 AM | ETH | DOWN | 2.2 min | +0.132% | — | In play | — |
| 10/13 11:27:50 AM | ZEC | DOWN | 2.2 min | +0.483% | — | In play | — |
| 10/13 11:27:50 AM | XRP | DOWN | 2.2 min | +0.212% | — | In play | — |
| 10/13 11:14:33 AM | ZEC | UP | 27 sec | -0.038% | 0¢ | ❌ Lost | $0.00 |
| 10/13 11:14:17 AM | PLATINUM | DOWN | 43 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 11:14:17 AM | EURUSD | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 11:13:45 AM | GBPUSD | DOWN | 75 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 11:13:45 AM | PALLADIUM | DOWN | 75 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 11:13:45 AM | XRP | UP | 75 sec | -0.175% | 0¢ | ❌ Lost | $0.00 |
| 10/13 11:13:13 AM | GOLD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/13 11:13:13 AM | WTI | UP | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 11:12:58 AM | NEAR | DOWN | 2.0 min | +0.493% | 0¢ | ❌ Lost | $0.00 |
| 10/13 11:12:43 AM | SILVER | DOWN | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 11:11:54 AM | SOL | UP | 3.1 min | -0.318% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 11:11:39 AM | DOGE | UP | 3.3 min | -0.247% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 11:10:34 AM | BTC | UP | 4.4 min | -0.233% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 11:10:18 AM | ETH | UP | 4.7 min | -0.257% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 11:09:31 AM | BNB | UP | 5.5 min | -0.269% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:59:45 AM | BNB | UP | 14 sec | -0.066% | 0¢ | ❌ Lost | $0.00 |
| 10/13 10:59:45 AM | NATGAS | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:59:29 AM | DOGE | DOWN | 30 sec | +0.042% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:59:13 AM | NEAR | DOWN | 46 sec | +0.082% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:59:13 AM | SILVER | UP | 46 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:59:13 AM | AUDUSD | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:58:57 AM | COPPER | UP | 62 sec | — | 5¢ | ❌ Lost | -$0.15 |
| 10/13 10:58:57 AM | BTC | UP | 62 sec | -0.054% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:58:42 AM | GOLD | UP | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:58:42 AM | WTI | DOWN | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:58:26 AM | PLATINUM | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:58:10 AM | HYPE | UP | 1.8 min | -0.207% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
