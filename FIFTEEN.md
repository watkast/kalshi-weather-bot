# 15-Minute 1¢ Study

*Updated Mon Nov 9, 4:38 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4080 finished bets | 1% | $190.55 | +42% | +4.67¢ | $93.10 / $97.45 |

*Expect about **97 buys a day** (~$14.50/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3789 | $107.90 | +26% |
| Volatility model ≥ 2%, hold to the close | 7477 | $80.15 | +9% |
| Momentum model ≥ 2%, hold to the close | 6169 | $5.55 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 50782 | 50765 | 187 (0%) | 1.07% | -$3,558.55 (-58%) | Hold to the close: -$3,558.55 (-58%) |

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
| Volatility model | 30994 | 4.8% | 0.4% (122) | -689% | ❌ Worse |
| Momentum model | 30994 | 4.6% | 0.4% (122) | -715% | ❌ Worse |
| Mean-reversion model | 30994 | 8.1% | 0.4% (122) | -833% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 30994 | 122 | -50% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7477 | 70 | +9% | -76% | -75% | -71% |
| Volatility model ≥ 5% | 4080 | 46 | +42% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2350 | 28 | +71% | -61% | -59% | -56% |
| Momentum model ≥ 2% | 6169 | 51 | +1% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3789 | 37 | +26% | -73% | -72% | -68% |
| Momentum model ≥ 10% | 2484 | 25 | +42% | -65% | -64% | -59% |
| Mean-reversion model ≥ 2% | 12812 | 90 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 8988 | 77 | -5% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6006 | 56 | +6% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31199 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11968 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7598 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 50765 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 187 | 0% | -$3,558.55 | -58% | — |
| Sell at 2¢ | 2003 | 4% | -$5,375.77 | -87% | 47 sec |
| Sell at 3¢ | 1362 | 3% | -$5,365.37 | -87% | 48 sec |
| Sell at 5¢ | 950 | 2% | -$5,251.05 | -85% | 62 sec |
| Sell at 10¢ | 573 | 1% | -$5,033.92 | -82% | 65 sec |
| Sell at 25¢ | 298 | 1% | -$4,686.17 | -76% | 83 sec |
| Sell at 50¢ | 192 | 0% | -$4,278.55 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2518 | 12 | 11% | 4% | -55% | -81% | -82% |
| 2–5 min | 16398 | 88 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 12832 | 41 | 3% | 2% | -65% | -92% | -92% |
| Under 1 min | 19005 | 46 | 1% | 0% | -65% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3497 | 14 | 5% | 2% | -48% | -88% | -88% |
| SOL | 3489 | 15 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3480 | 11 | 5% | 2% | -60% | -89% | -88% |
| BNB | 3474 | 18 | 5% | 2% | -35% | -86% | -85% |
| DOGE | 3472 | 7 | 4% | 2% | -75% | -90% | -90% |
| ETH | 3466 | 14 | 7% | 3% | -50% | -81% | -81% |
| NEAR | 3445 | 16 | 5% | 2% | -40% | -85% | -85% |
| BTC | 3443 | 16 | 5% | 2% | -36% | -87% | -89% |
| XRP | 3433 | 13 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1823 | 5 | 6% | 2% | -67% | -81% | -82% |
| WTI | 1794 | 6 | 4% | 1% | -60% | -92% | -92% |
| SILVER | 1774 | 8 | 5% | 2% | -47% | -82% | -82% |
| PLATINUM | 1604 | 4 | 2% | 1% | -77% | -96% | -95% |
| EURUSD | 1539 | 4 | 2% | 1% | -76% | -90% | -89% |
| COPPER | 1505 | 6 | 2% | 1% | -63% | -72% | -72% |
| NATGAS | 1464 | 8 | 2% | 1% | -49% | -77% | -77% |
| GBPUSD | 1460 | 4 | 2% | 1% | -74% | -96% | -96% |
| USDJPY | 1445 | 5 | 2% | 1% | -68% | -97% | -96% |
| PALLADIUM | 1440 | 3 | 1% | 0% | -81% | -92% | -92% |
| AUDUSD | 1000 | 5 | 2% | 1% | -53% | -87% | -87% |
| USDCAD | 966 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 564 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 316 | 1 | 4% | 2% | -70% | -63% | -61% |
| 2YRRATE | 297 | 3 | 4% | 1% | -6% | -30% | -29% |
| 30YRRATE | 295 | 0 | 2% | 1% | -100% | -96% | -95% |
| 5YRRATE | 273 | 1 | 4% | 1% | -66% | -93% | -95% |
| INX | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 25757 | 96 | 4% | 2% | -57% | -88% | -87% |
| DOWN (bought NO) | 25008 | 91 | 4% | 2% | -58% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5050 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5337 | 19 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 8028 | 27 | 5% | 2% | -58% | -89% | -89% |
| 0.2–0.5% | 9281 | 39 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 3495 | 14 | 7% | 3% | -59% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12540 | 43 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12223 | 54 | 4% | 2% | -50% | -84% | -84% |
| Afternoon (12–6pm) | 12200 | 47 | 4% | 2% | -55% | -86% | -86% |
| Evening (6pm–12am) | 13802 | 43 | 4% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,934 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/9 4:29:32 AM | GBPUSD | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:28:58 AM | EURUSD | UP | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:28:42 AM | COPPER | DOWN | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:28:26 AM | PALLADIUM | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:28:26 AM | SILVER | DOWN | 1.6 min | — | 0¢ | ❌ Lost | $0.00 |
| 11/9 4:28:26 AM | USDCAD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:28:26 AM | GOLD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | $0.00 |
| 11/9 4:27:15 AM | NATGAS | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:26:40 AM | BRENT | UP | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:26:24 AM | WTI | UP | 3.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:25:17 AM | ZEC | DOWN | 4.7 min | +0.924% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:25:03 AM | BTC | DOWN | 5.0 min | +0.494% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:23:21 AM | SOL | DOWN | 6.6 min | +0.826% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:22:31 AM | XRP | DOWN | 7.5 min | +1.049% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:22:15 AM | ETH | DOWN | 7.8 min | +0.990% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:21:44 AM | NEAR | DOWN | 8.3 min | +1.728% | 3¢ | ❌ Lost | -$0.15 |
| 11/9 4:20:56 AM | BNB | DOWN | 9.1 min | +0.705% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:20:40 AM | DOGE | DOWN | 9.3 min | +1.295% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:20:40 AM | HYPE | DOWN | 9.3 min | +1.409% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:14:59 AM | BNB | UP | 1 sec | -0.015% | 0¢ | ❌ Lost | $0.00 |
| 11/9 4:14:59 AM | AUDUSD | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:14:43 AM | BTC | UP | 17 sec | -0.062% | 0¢ | ❌ Lost | $0.00 |
| 11/9 4:14:28 AM | SILVER | DOWN | 32 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:14:28 AM | SOL | UP | 32 sec | -0.094% | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:14:28 AM | ETH | UP | 32 sec | -0.121% | 0¢ | ❌ Lost | $0.00 |
| 11/9 4:14:28 AM | NEAR | DOWN | 32 sec | +0.026% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:13:52 AM | BRENT | UP | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:13:52 AM | USDCAD | DOWN | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:13:36 AM | NATGAS | UP | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:13:36 AM | GOLD | DOWN | 83 sec | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
