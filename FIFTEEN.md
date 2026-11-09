# 15-Minute 1¢ Study

*Updated Mon Nov 9, 2:54 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4077 finished bets | 1% | $190.85 | +42% | +4.68¢ | $93.25 / $97.60 |

*Expect about **97 buys a day** (~$14.51/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3784 | $108.50 | +26% |
| Volatility model ≥ 2%, hold to the close | 7468 | $81.35 | +9% |
| Momentum model ≥ 2%, hold to the close | 6161 | $6.45 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 50631 | 50614 | 187 (0%) | 1.07% | -$3,539.50 (-57%) | Hold to the close: -$3,539.50 (-57%) |

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
| Volatility model | 30931 | 4.8% | 0.4% (122) | -689% | ❌ Worse |
| Momentum model | 30931 | 4.6% | 0.4% (122) | -715% | ❌ Worse |
| Mean-reversion model | 30931 | 8.1% | 0.4% (122) | -832% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 30931 | 122 | -50% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7468 | 70 | +9% | -76% | -75% | -71% |
| Volatility model ≥ 5% | 4077 | 46 | +42% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2348 | 28 | +71% | -61% | -59% | -55% |
| Momentum model ≥ 2% | 6161 | 51 | +1% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3784 | 37 | +26% | -73% | -72% | -68% |
| Momentum model ≥ 10% | 2482 | 25 | +42% | -64% | -64% | -59% |
| Mean-reversion model ≥ 2% | 12792 | 90 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 8971 | 77 | -5% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 5995 | 56 | +6% | -76% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31136 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11927 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7551 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 50614 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 187 | 0% | -$3,539.50 | -57% | — |
| Sell at 2¢ | 1996 | 4% | -$5,358.54 | -87% | 47 sec |
| Sell at 3¢ | 1356 | 3% | -$5,348.66 | -87% | 48 sec |
| Sell at 5¢ | 947 | 2% | -$5,233.95 | -85% | 62 sec |
| Sell at 10¢ | 571 | 1% | -$5,017.49 | -81% | 65 sec |
| Sell at 25¢ | 298 | 1% | -$4,667.12 | -76% | 83 sec |
| Sell at 50¢ | 192 | 0% | -$4,259.50 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2507 | 12 | 11% | 4% | -55% | -81% | -82% |
| 2–5 min | 16351 | 88 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 12785 | 41 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 18959 | 46 | 1% | 0% | -65% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3490 | 14 | 5% | 2% | -48% | -88% | -88% |
| SOL | 3482 | 15 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3473 | 11 | 5% | 2% | -60% | -89% | -88% |
| BNB | 3467 | 18 | 5% | 2% | -34% | -86% | -85% |
| DOGE | 3465 | 7 | 4% | 2% | -75% | -90% | -90% |
| ETH | 3459 | 14 | 7% | 3% | -50% | -81% | -81% |
| NEAR | 3438 | 16 | 5% | 2% | -40% | -85% | -85% |
| BTC | 3436 | 16 | 5% | 2% | -36% | -87% | -89% |
| XRP | 3426 | 13 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1817 | 5 | 6% | 2% | -66% | -81% | -82% |
| WTI | 1787 | 6 | 4% | 1% | -60% | -92% | -92% |
| SILVER | 1768 | 8 | 5% | 2% | -47% | -82% | -82% |
| PLATINUM | 1601 | 4 | 2% | 1% | -77% | -96% | -96% |
| EURUSD | 1532 | 4 | 2% | 1% | -76% | -90% | -89% |
| COPPER | 1500 | 6 | 2% | 1% | -63% | -72% | -72% |
| NATGAS | 1460 | 8 | 2% | 1% | -49% | -77% | -77% |
| GBPUSD | 1454 | 4 | 2% | 1% | -74% | -96% | -96% |
| USDJPY | 1441 | 5 | 2% | 1% | -68% | -97% | -96% |
| PALLADIUM | 1437 | 3 | 1% | 0% | -81% | -92% | -92% |
| AUDUSD | 995 | 5 | 2% | 1% | -53% | -87% | -87% |
| USDCAD | 961 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 557 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 310 | 1 | 4% | 1% | -70% | -63% | -61% |
| 2YRRATE | 294 | 3 | 4% | 1% | -5% | -29% | -29% |
| 30YRRATE | 289 | 0 | 2% | 1% | -100% | -96% | -95% |
| 5YRRATE | 268 | 1 | 4% | 1% | -65% | -93% | -95% |
| INX | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 25669 | 96 | 4% | 2% | -57% | -88% | -87% |
| DOWN (bought NO) | 24945 | 91 | 4% | 2% | -58% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5047 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5327 | 19 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 8013 | 27 | 5% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 9261 | 39 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 3480 | 14 | 7% | 3% | -58% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12389 | 43 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 12223 | 54 | 4% | 2% | -50% | -84% | -84% |
| Afternoon (12–6pm) | 12200 | 47 | 4% | 2% | -55% | -86% | -86% |
| Evening (6pm–12am) | 13802 | 43 | 4% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,943 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/9 2:44:48 AM | USDCAD | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 2:44:48 AM | PLATINUM | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 2:44:48 AM | 2YRRATE | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 2:44:48 AM | BTC | UP | 11 sec | -0.110% | 0¢ | ❌ Lost | $0.00 |
| 11/9 2:44:48 AM | BNB | UP | 11 sec | -0.156% | 0¢ | ❌ Lost | $0.00 |
| 11/9 2:44:48 AM | NATGAS | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 2:44:48 AM | BRENT | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 2:44:48 AM | USDJPY | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 2:44:48 AM | SOL | UP | 11 sec | -0.290% | 0¢ | ❌ Lost | $0.00 |
| 11/9 2:44:48 AM | AUDUSD | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 2:44:48 AM | 5YRRATE | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 2:44:48 AM | NEAR | DOWN | 11 sec | -0.059% | 0¢ | ❌ Lost | $0.00 |
| 11/9 2:44:48 AM | WTI | DOWN | 11 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/9 2:44:48 AM | XRP | UP | 11 sec | -0.402% | 0¢ | ❌ Lost | $0.00 |
| 11/9 2:44:48 AM | 10YRRATE | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 2:44:48 AM | HYPE | UP | 11 sec | -0.295% | 0¢ | ❌ Lost | $0.00 |
| 11/9 2:44:48 AM | COPPER | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 2:44:48 AM | 30YRRATE | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 2:44:48 AM | ETH | UP | 11 sec | -0.200% | 0¢ | ❌ Lost | $0.00 |
| 11/9 2:14:46 AM | SILVER | DOWN | 13 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 2:14:30 AM | GOLD | DOWN | 29 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/9 2:14:30 AM | PALLADIUM | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 2:14:30 AM | 2YRRATE | UP | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 2:14:13 AM | DOGE | UP | 46 sec | -0.195% | 0¢ | ❌ Lost | $0.00 |
| 11/9 2:14:13 AM | BNB | UP | 46 sec | -0.133% | 0¢ | ❌ Lost | $0.00 |
| 11/9 2:13:55 AM | PLATINUM | DOWN | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 2:13:39 AM | WTI | UP | 81 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 2:13:39 AM | SOL | UP | 81 sec | -0.216% | 0¢ | ❌ Lost | -$0.15 |
| 11/9 2:13:39 AM | 5YRRATE | UP | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 2:13:39 AM | 30YRRATE | UP | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
