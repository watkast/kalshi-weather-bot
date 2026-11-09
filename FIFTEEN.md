# 15-Minute 1¢ Study

*Updated Mon Nov 9, 6:22 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4100 finished bets | 1% | $188.15 | +41% | +4.59¢ | $92.05 / $96.10 |

*Expect about **97 buys a day** (~$14.55/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3804 | $106.25 | +26% |
| Volatility model ≥ 2%, hold to the close | 7505 | $76.55 | +8% |
| Momentum model ≥ 2%, hold to the close | 6194 | $2.55 | +0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 50937 | 50920 | 187 (0%) | 1.07% | -$3,579.25 (-58%) | Hold to the close: -$3,579.25 (-58%) |

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
| Volatility model | 31057 | 4.8% | 0.4% (122) | -692% | ❌ Worse |
| Momentum model | 31057 | 4.6% | 0.4% (122) | -717% | ❌ Worse |
| Mean-reversion model | 31057 | 8.1% | 0.4% (122) | -836% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 31057 | 122 | -50% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7505 | 70 | +8% | -77% | -75% | -71% |
| Volatility model ≥ 5% | 4100 | 46 | +41% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2359 | 28 | +70% | -61% | -59% | -56% |
| Momentum model ≥ 2% | 6194 | 51 | +0% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3804 | 37 | +26% | -73% | -73% | -68% |
| Momentum model ≥ 10% | 2495 | 25 | +41% | -65% | -64% | -59% |
| Mean-reversion model ≥ 2% | 12851 | 90 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9012 | 77 | -5% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6024 | 56 | +6% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31262 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12015 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7643 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 50920 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 187 | 0% | -$3,579.25 | -58% | — |
| Sell at 2¢ | 2008 | 4% | -$5,395.17 | -87% | 47 sec |
| Sell at 3¢ | 1365 | 3% | -$5,384.90 | -87% | 48 sec |
| Sell at 5¢ | 951 | 2% | -$5,271.10 | -85% | 62 sec |
| Sell at 10¢ | 573 | 1% | -$5,054.62 | -82% | 65 sec |
| Sell at 25¢ | 298 | 1% | -$4,706.87 | -76% | 83 sec |
| Sell at 50¢ | 192 | 0% | -$4,299.25 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2525 | 12 | 11% | 4% | -55% | -81% | -82% |
| 2–5 min | 16451 | 88 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 12880 | 41 | 3% | 2% | -65% | -92% | -92% |
| Under 1 min | 19052 | 46 | 1% | 0% | -65% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3504 | 14 | 5% | 2% | -48% | -88% | -88% |
| SOL | 3496 | 15 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3487 | 11 | 5% | 2% | -60% | -89% | -88% |
| BNB | 3481 | 18 | 5% | 2% | -35% | -86% | -85% |
| DOGE | 3479 | 7 | 4% | 2% | -75% | -90% | -90% |
| ETH | 3473 | 14 | 7% | 3% | -50% | -81% | -81% |
| NEAR | 3452 | 16 | 5% | 2% | -40% | -85% | -85% |
| BTC | 3450 | 16 | 5% | 2% | -36% | -87% | -89% |
| XRP | 3440 | 13 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1829 | 5 | 6% | 2% | -67% | -81% | -83% |
| WTI | 1801 | 6 | 4% | 1% | -60% | -92% | -92% |
| SILVER | 1778 | 8 | 5% | 2% | -47% | -82% | -82% |
| PLATINUM | 1611 | 4 | 2% | 1% | -77% | -96% | -95% |
| EURUSD | 1545 | 4 | 2% | 1% | -76% | -90% | -89% |
| COPPER | 1509 | 6 | 2% | 1% | -63% | -72% | -72% |
| NATGAS | 1470 | 8 | 2% | 1% | -49% | -77% | -77% |
| GBPUSD | 1464 | 4 | 2% | 1% | -74% | -96% | -96% |
| USDJPY | 1449 | 5 | 2% | 1% | -68% | -97% | -96% |
| PALLADIUM | 1446 | 3 | 1% | 0% | -81% | -92% | -92% |
| AUDUSD | 1006 | 5 | 2% | 1% | -54% | -87% | -87% |
| USDCAD | 972 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 571 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 321 | 1 | 4% | 2% | -71% | -63% | -61% |
| 2YRRATE | 302 | 3 | 4% | 1% | -7% | -31% | -30% |
| 30YRRATE | 299 | 0 | 2% | 1% | -100% | -97% | -95% |
| 5YRRATE | 278 | 1 | 4% | 1% | -66% | -93% | -95% |
| INX | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 25824 | 96 | 4% | 2% | -57% | -88% | -87% |
| DOWN (bought NO) | 25096 | 91 | 4% | 2% | -58% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5055 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5346 | 19 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 8041 | 27 | 5% | 2% | -58% | -89% | -89% |
| 0.2–0.5% | 9308 | 39 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 3504 | 14 | 7% | 3% | -59% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12671 | 43 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12247 | 54 | 4% | 2% | -50% | -84% | -84% |
| Afternoon (12–6pm) | 12200 | 47 | 4% | 2% | -55% | -86% | -86% |
| Evening (6pm–12am) | 13802 | 43 | 4% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,924 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/9 6:14:56 AM | EURUSD | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 6:14:25 AM | PALLADIUM | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 6:14:25 AM | ETH | UP | 34 sec | -0.060% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 6:14:10 AM | DOGE | UP | 50 sec | -0.120% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 6:14:10 AM | PLATINUM | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 6:14:10 AM | WTI | DOWN | 50 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 6:13:54 AM | SOL | UP | 66 sec | -0.162% | 0¢ | ❌ Lost | $0.00 |
| 11/9 6:13:54 AM | BRENT | DOWN | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 6:13:54 AM | GOLD | UP | 66 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 6:13:54 AM | 2YRRATE | UP | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 6:13:38 AM | NATGAS | DOWN | 82 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 6:13:22 AM | COPPER | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 6:13:07 AM | 30YRRATE | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 6:13:07 AM | 5YRRATE | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 6:12:51 AM | 10YRRATE | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 6:12:35 AM | BTC | UP | 2.4 min | -0.200% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 6:12:03 AM | HYPE | UP | 2.9 min | -0.493% | 0¢ | ❌ Lost | -$0.15 |
| 11/9 6:12:03 AM | SILVER | UP | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 6:11:38 AM | NEAR | UP | 3.4 min | -0.863% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 6:11:38 AM | BNB | UP | 3.4 min | -0.243% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 6:11:38 AM | ZEC | UP | 3.4 min | -0.708% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 6:11:07 AM | USDCAD | DOWN | 3.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 6:10:47 AM | AUDUSD | UP | 4.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 6:10:15 AM | XRP | UP | 4.7 min | -0.643% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 5:59:57 AM | USDCAD | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:59:57 AM | PALLADIUM | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:59:57 AM | NATGAS | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:59:41 AM | SOL | UP | 19 sec | -0.070% | 0¢ | ❌ Lost | $0.00 |
| 11/9 5:59:41 AM | 30YRRATE | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:59:26 AM | NEAR | DOWN | 34 sec | +0.138% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
