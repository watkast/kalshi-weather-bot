# 15-Minute 1¢ Study

*Updated Mon Nov 9, 3:25 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4078 finished bets | 1% | $190.85 | +42% | +4.68¢ | $93.10 / $97.75 |

*Expect about **97 buys a day** (~$14.51/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3785 | $108.50 | +26% |
| Volatility model ≥ 2%, hold to the close | 7472 | $80.90 | +9% |
| Momentum model ≥ 2%, hold to the close | 6162 | $6.45 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 50680 | 50661 | 187 (0%) | 1.07% | -$3,545.35 (-58%) | Hold to the close: -$3,545.35 (-58%) |

*In play or awaiting result: 11. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 30949 | 4.8% | 0.4% (122) | -689% | ❌ Worse |
| Momentum model | 30949 | 4.6% | 0.4% (122) | -715% | ❌ Worse |
| Mean-reversion model | 30949 | 8.1% | 0.4% (122) | -833% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 30949 | 122 | -50% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7472 | 70 | +9% | -76% | -75% | -71% |
| Volatility model ≥ 5% | 4078 | 46 | +42% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2349 | 28 | +71% | -61% | -59% | -55% |
| Momentum model ≥ 2% | 6162 | 51 | +1% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3785 | 37 | +26% | -73% | -72% | -68% |
| Momentum model ≥ 10% | 2483 | 25 | +42% | -64% | -64% | -59% |
| Mean-reversion model ≥ 2% | 12797 | 90 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 8975 | 77 | -5% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 5998 | 56 | +6% | -76% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31154 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11941 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7566 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 50661 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 187 | 0% | -$3,545.35 | -58% | — |
| Sell at 2¢ | 1996 | 4% | -$5,364.39 | -87% | 47 sec |
| Sell at 3¢ | 1356 | 3% | -$5,354.51 | -87% | 48 sec |
| Sell at 5¢ | 947 | 2% | -$5,239.80 | -85% | 62 sec |
| Sell at 10¢ | 571 | 1% | -$5,023.34 | -82% | 65 sec |
| Sell at 25¢ | 298 | 1% | -$4,672.97 | -76% | 83 sec |
| Sell at 50¢ | 192 | 0% | -$4,265.35 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2507 | 12 | 11% | 4% | -55% | -81% | -82% |
| 2–5 min | 16366 | 88 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 12796 | 41 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 18980 | 46 | 1% | 0% | -65% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3492 | 14 | 5% | 2% | -48% | -88% | -88% |
| SOL | 3484 | 15 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3475 | 11 | 5% | 2% | -60% | -89% | -88% |
| BNB | 3469 | 18 | 5% | 2% | -34% | -86% | -85% |
| DOGE | 3467 | 7 | 4% | 2% | -75% | -90% | -90% |
| ETH | 3461 | 14 | 7% | 3% | -50% | -81% | -81% |
| NEAR | 3440 | 16 | 5% | 2% | -40% | -85% | -85% |
| BTC | 3438 | 16 | 5% | 2% | -36% | -87% | -89% |
| XRP | 3428 | 13 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1819 | 5 | 6% | 2% | -66% | -81% | -82% |
| WTI | 1789 | 6 | 4% | 1% | -60% | -92% | -92% |
| SILVER | 1770 | 8 | 5% | 2% | -47% | -82% | -82% |
| PLATINUM | 1603 | 4 | 2% | 1% | -77% | -96% | -96% |
| EURUSD | 1534 | 4 | 2% | 1% | -76% | -90% | -89% |
| COPPER | 1501 | 6 | 2% | 1% | -63% | -72% | -72% |
| NATGAS | 1462 | 8 | 2% | 1% | -49% | -77% | -77% |
| GBPUSD | 1456 | 4 | 2% | 1% | -74% | -96% | -96% |
| USDJPY | 1443 | 5 | 2% | 1% | -68% | -97% | -96% |
| PALLADIUM | 1438 | 3 | 1% | 0% | -81% | -92% | -92% |
| AUDUSD | 997 | 5 | 2% | 1% | -53% | -87% | -87% |
| USDCAD | 962 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 559 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 312 | 1 | 4% | 1% | -70% | -63% | -61% |
| 2YRRATE | 294 | 3 | 4% | 1% | -5% | -29% | -29% |
| 30YRRATE | 291 | 0 | 2% | 1% | -100% | -96% | -95% |
| 5YRRATE | 270 | 1 | 4% | 1% | -65% | -93% | -95% |
| INX | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 25692 | 96 | 4% | 2% | -57% | -88% | -87% |
| DOWN (bought NO) | 24969 | 91 | 4% | 2% | -58% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5048 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5329 | 19 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 8020 | 27 | 5% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 9267 | 39 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 3482 | 14 | 7% | 3% | -58% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12436 | 43 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 12223 | 54 | 4% | 2% | -50% | -84% | -84% |
| Afternoon (12–6pm) | 12200 | 47 | 4% | 2% | -55% | -86% | -86% |
| Evening (6pm–12am) | 13802 | 43 | 4% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,940 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/9 3:25:17 AM | BRENT | UP | 4.7 min | — | — | In play | — |
| 11/9 3:23:56 AM | WTI | UP | 6.1 min | — | — | In play | — |
| 11/9 3:14:59 AM | SILVER | DOWN | 0 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/9 3:14:59 AM | GBPUSD | DOWN | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 3:14:59 AM | AUDUSD | DOWN | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 3:14:59 AM | WTI | DOWN | 0 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/9 3:14:59 AM | XRP | DOWN | 0 sec | +0.064% | 0¢ | ❌ Lost | $0.00 |
| 11/9 3:14:43 AM | USDCAD | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 3:14:43 AM | 5YRRATE | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 3:14:26 AM | GOLD | DOWN | 33 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/9 3:14:07 AM | BRENT | DOWN | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 3:13:51 AM | EURUSD | DOWN | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 3:13:51 AM | USDJPY | UP | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 3:13:35 AM | PLATINUM | DOWN | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 3:13:35 AM | 10YRRATE | DOWN | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 3:13:35 AM | 30YRRATE | DOWN | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 3:13:20 AM | BTC | UP | 1.6 min | -0.162% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 3:12:13 AM | BNB | UP | 2.8 min | -0.157% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 3:12:13 AM | NATGAS | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 3:11:56 AM | NEAR | UP | 3.0 min | -0.676% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 3:11:56 AM | HYPE | UP | 3.0 min | -0.438% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 3:11:40 AM | SOL | UP | 3.3 min | -0.394% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 3:11:40 AM | DOGE | UP | 3.3 min | -0.313% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 3:11:40 AM | ETH | UP | 3.3 min | -0.334% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 3:10:01 AM | ZEC | UP | 5.0 min | -0.926% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 2:59:52 AM | 30YRRATE | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 2:59:52 AM | ZEC | UP | 8 sec | -0.075% | 0¢ | ❌ Lost | -$0.15 |
| 11/9 2:59:52 AM | 5YRRATE | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 2:59:52 AM | 10YRRATE | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 2:59:37 AM | PALLADIUM | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
