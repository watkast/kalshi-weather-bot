# 15-Minute 1¢ Study

*Updated Mon Nov 9, 5:50 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4099 finished bets | 1% | $188.30 | +41% | +4.59¢ | $92.05 / $96.25 |

*Expect about **97 buys a day** (~$14.55/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3803 | $106.25 | +26% |
| Volatility model ≥ 2%, hold to the close | 7503 | $76.85 | +9% |
| Momentum model ≥ 2%, hold to the close | 6191 | $2.85 | +0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 50889 | 50872 | 187 (0%) | 1.07% | -$3,572.80 (-58%) | Hold to the close: -$3,572.80 (-58%) |

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
| Volatility model | 31039 | 4.8% | 0.4% (122) | -692% | ❌ Worse |
| Momentum model | 31039 | 4.6% | 0.4% (122) | -717% | ❌ Worse |
| Mean-reversion model | 31039 | 8.1% | 0.4% (122) | -836% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 31039 | 122 | -50% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7503 | 70 | +9% | -77% | -75% | -71% |
| Volatility model ≥ 5% | 4099 | 46 | +41% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2359 | 28 | +70% | -61% | -59% | -56% |
| Momentum model ≥ 2% | 6191 | 51 | +0% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3803 | 37 | +26% | -73% | -73% | -68% |
| Momentum model ≥ 10% | 2494 | 25 | +41% | -65% | -64% | -59% |
| Mean-reversion model ≥ 2% | 12843 | 90 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9010 | 77 | -5% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6023 | 56 | +6% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31244 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12000 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7628 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 50872 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 187 | 0% | -$3,572.80 | -58% | — |
| Sell at 2¢ | 2005 | 4% | -$5,389.50 | -87% | 47 sec |
| Sell at 3¢ | 1363 | 3% | -$5,379.23 | -87% | 48 sec |
| Sell at 5¢ | 950 | 2% | -$5,265.30 | -85% | 62 sec |
| Sell at 10¢ | 573 | 1% | -$5,048.17 | -82% | 65 sec |
| Sell at 25¢ | 298 | 1% | -$4,700.42 | -76% | 83 sec |
| Sell at 50¢ | 192 | 0% | -$4,292.80 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2525 | 12 | 11% | 4% | -55% | -81% | -82% |
| 2–5 min | 16436 | 88 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 12859 | 41 | 3% | 2% | -65% | -92% | -92% |
| Under 1 min | 19040 | 46 | 1% | 0% | -65% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3502 | 14 | 5% | 2% | -48% | -88% | -88% |
| SOL | 3494 | 15 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3485 | 11 | 5% | 2% | -60% | -89% | -88% |
| BNB | 3479 | 18 | 5% | 2% | -35% | -86% | -85% |
| DOGE | 3477 | 7 | 4% | 2% | -75% | -90% | -90% |
| ETH | 3471 | 14 | 7% | 3% | -50% | -81% | -81% |
| NEAR | 3450 | 16 | 5% | 2% | -40% | -85% | -85% |
| BTC | 3448 | 16 | 5% | 2% | -36% | -87% | -89% |
| XRP | 3438 | 13 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1827 | 5 | 6% | 2% | -67% | -81% | -83% |
| WTI | 1799 | 6 | 4% | 1% | -60% | -92% | -92% |
| SILVER | 1776 | 8 | 5% | 2% | -47% | -82% | -82% |
| PLATINUM | 1609 | 4 | 2% | 1% | -77% | -96% | -95% |
| EURUSD | 1543 | 4 | 2% | 1% | -76% | -90% | -89% |
| COPPER | 1508 | 6 | 2% | 1% | -63% | -72% | -72% |
| NATGAS | 1468 | 8 | 2% | 1% | -49% | -77% | -77% |
| GBPUSD | 1464 | 4 | 2% | 1% | -74% | -96% | -96% |
| USDJPY | 1448 | 5 | 2% | 1% | -68% | -97% | -96% |
| PALLADIUM | 1444 | 3 | 1% | 0% | -81% | -92% | -92% |
| AUDUSD | 1004 | 5 | 2% | 1% | -54% | -87% | -87% |
| USDCAD | 970 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 569 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 319 | 1 | 4% | 2% | -71% | -63% | -61% |
| 2YRRATE | 300 | 3 | 4% | 1% | -7% | -31% | -30% |
| 30YRRATE | 297 | 0 | 2% | 1% | -100% | -96% | -95% |
| 5YRRATE | 276 | 1 | 4% | 1% | -66% | -93% | -95% |
| INX | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 25795 | 96 | 4% | 2% | -57% | -88% | -87% |
| DOWN (bought NO) | 25077 | 91 | 4% | 2% | -58% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5055 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5342 | 19 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 8037 | 27 | 5% | 2% | -58% | -89% | -89% |
| 0.2–0.5% | 9302 | 39 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 3500 | 14 | 7% | 3% | -59% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12647 | 43 | 4% | 2% | -61% | -87% | -88% |
| Morning (6am–12pm) | 12223 | 54 | 4% | 2% | -50% | -84% | -84% |
| Afternoon (12–6pm) | 12200 | 47 | 4% | 2% | -55% | -86% | -86% |
| Evening (6pm–12am) | 13802 | 43 | 4% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,926 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/9 5:44:58 AM | HYPE | DOWN | 2 sec | -0.028% | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:44:58 AM | PLATINUM | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:44:42 AM | GBPUSD | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:44:42 AM | ZEC | UP | 18 sec | -0.090% | 0¢ | ❌ Lost | $0.00 |
| 11/9 5:44:42 AM | ETH | DOWN | 18 sec | -0.017% | 0¢ | ❌ Lost | $0.00 |
| 11/9 5:44:42 AM | BTC | DOWN | 18 sec | +0.007% | 0¢ | ❌ Lost | $0.00 |
| 11/9 5:44:27 AM | SOL | UP | 33 sec | -0.086% | 0¢ | ❌ Lost | $0.00 |
| 11/9 5:44:27 AM | AUDUSD | UP | 33 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 11/9 5:44:27 AM | GOLD | DOWN | 33 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/9 5:44:27 AM | PALLADIUM | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:44:27 AM | BNB | UP | 33 sec | -0.067% | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:43:51 AM | BRENT | DOWN | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:43:20 AM | WTI | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 5:43:05 AM | 30YRRATE | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:40:57 AM | USDJPY | DOWN | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:40:57 AM | NEAR | DOWN | 4.0 min | +0.573% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 5:40:57 AM | 10YRRATE | DOWN | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:40:57 AM | NATGAS | DOWN | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:40:18 AM | DOGE | DOWN | 4.7 min | +0.378% | 4¢ | ❌ Lost | -$0.15 |
| 11/9 5:38:36 AM | XRP | DOWN | 6.4 min | +0.731% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 5:37:49 AM | 5YRRATE | DOWN | 7.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 5:36:10 AM | 2YRRATE | DOWN | 8.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 5:29:46 AM | USDJPY | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:29:46 AM | GBPUSD | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:29:46 AM | PLATINUM | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:29:46 AM | EURUSD | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:29:46 AM | USDCAD | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:29:46 AM | WTI | UP | 13 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/9 5:29:30 AM | BRENT | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:28:40 AM | NEAR | DOWN | 79 sec | +0.210% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
