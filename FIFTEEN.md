# 15-Minute 1¢ Study

*Updated Mon Nov 9, 4:48 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4082 finished bets | 1% | $190.25 | +42% | +4.66¢ | $92.95 / $97.30 |

*Expect about **97 buys a day** (~$14.51/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3791 | $107.60 | +26% |
| Volatility model ≥ 2%, hold to the close | 7481 | $79.55 | +9% |
| Momentum model ≥ 2%, hold to the close | 6173 | $4.95 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 50803 | 50786 | 187 (0%) | 1.07% | -$3,561.40 (-58%) | Hold to the close: -$3,561.40 (-58%) |

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
| Volatility model | 31003 | 4.8% | 0.4% (122) | -690% | ❌ Worse |
| Momentum model | 31003 | 4.6% | 0.4% (122) | -716% | ❌ Worse |
| Mean-reversion model | 31003 | 8.1% | 0.4% (122) | -834% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 31003 | 122 | -50% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7481 | 70 | +9% | -76% | -75% | -71% |
| Volatility model ≥ 5% | 4082 | 46 | +42% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2352 | 28 | +70% | -61% | -59% | -56% |
| Momentum model ≥ 2% | 6173 | 51 | +1% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3791 | 37 | +26% | -73% | -72% | -68% |
| Momentum model ≥ 10% | 2486 | 25 | +41% | -65% | -64% | -59% |
| Mean-reversion model ≥ 2% | 12818 | 90 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 8990 | 77 | -5% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6008 | 56 | +6% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31208 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11976 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7602 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 50786 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 187 | 0% | -$3,561.40 | -58% | — |
| Sell at 2¢ | 2003 | 4% | -$5,378.62 | -87% | 47 sec |
| Sell at 3¢ | 1362 | 3% | -$5,368.22 | -87% | 48 sec |
| Sell at 5¢ | 950 | 2% | -$5,253.90 | -85% | 62 sec |
| Sell at 10¢ | 573 | 1% | -$5,036.77 | -82% | 65 sec |
| Sell at 25¢ | 298 | 1% | -$4,689.02 | -76% | 83 sec |
| Sell at 50¢ | 192 | 0% | -$4,281.40 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2519 | 12 | 11% | 4% | -55% | -81% | -82% |
| 2–5 min | 16404 | 88 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 12841 | 41 | 3% | 2% | -65% | -92% | -92% |
| Under 1 min | 19010 | 46 | 1% | 0% | -65% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3498 | 14 | 5% | 2% | -48% | -88% | -88% |
| SOL | 3490 | 15 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3481 | 11 | 5% | 2% | -60% | -89% | -88% |
| BNB | 3475 | 18 | 5% | 2% | -35% | -86% | -85% |
| DOGE | 3473 | 7 | 4% | 2% | -75% | -90% | -90% |
| ETH | 3467 | 14 | 7% | 3% | -50% | -81% | -81% |
| NEAR | 3446 | 16 | 5% | 2% | -40% | -85% | -85% |
| BTC | 3444 | 16 | 5% | 2% | -36% | -87% | -89% |
| XRP | 3434 | 13 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1824 | 5 | 6% | 2% | -67% | -81% | -82% |
| WTI | 1795 | 6 | 4% | 1% | -60% | -92% | -92% |
| SILVER | 1775 | 8 | 5% | 2% | -47% | -82% | -82% |
| PLATINUM | 1605 | 4 | 2% | 1% | -77% | -96% | -95% |
| EURUSD | 1540 | 4 | 2% | 1% | -76% | -90% | -89% |
| COPPER | 1506 | 6 | 2% | 1% | -63% | -72% | -72% |
| NATGAS | 1465 | 8 | 2% | 1% | -49% | -77% | -77% |
| GBPUSD | 1461 | 4 | 2% | 1% | -74% | -96% | -96% |
| USDJPY | 1445 | 5 | 2% | 1% | -68% | -97% | -96% |
| PALLADIUM | 1441 | 3 | 1% | 0% | -81% | -92% | -92% |
| AUDUSD | 1001 | 5 | 2% | 1% | -53% | -87% | -87% |
| USDCAD | 967 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 565 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 316 | 1 | 4% | 2% | -70% | -63% | -61% |
| 2YRRATE | 297 | 3 | 4% | 1% | -6% | -30% | -29% |
| 30YRRATE | 295 | 0 | 2% | 1% | -100% | -96% | -95% |
| 5YRRATE | 273 | 1 | 4% | 1% | -66% | -93% | -95% |
| INX | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 25766 | 96 | 4% | 2% | -57% | -88% | -87% |
| DOWN (bought NO) | 25020 | 91 | 4% | 2% | -58% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5052 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5339 | 19 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 8029 | 27 | 5% | 2% | -58% | -89% | -89% |
| 0.2–0.5% | 9285 | 39 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 3495 | 14 | 7% | 3% | -59% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12561 | 43 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12223 | 54 | 4% | 2% | -50% | -84% | -84% |
| Afternoon (12–6pm) | 12200 | 47 | 4% | 2% | -55% | -86% | -86% |
| Evening (6pm–12am) | 13802 | 43 | 4% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,933 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/9 4:44:46 AM | XRP | DOWN | 13 sec | -0.037% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:44:28 AM | DOGE | UP | 31 sec | -0.096% | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:44:28 AM | BNB | UP | 31 sec | -0.045% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:44:09 AM | PALLADIUM | DOWN | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:44:09 AM | NEAR | UP | 51 sec | -0.233% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:43:53 AM | NATGAS | DOWN | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:43:53 AM | ETH | DOWN | 67 sec | +0.062% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:43:53 AM | BRENT | UP | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:43:37 AM | HYPE | UP | 83 sec | -0.338% | 0¢ | ❌ Lost | $0.00 |
| 11/9 4:43:37 AM | ZEC | UP | 83 sec | -0.426% | 0¢ | ❌ Lost | $0.00 |
| 11/9 4:43:22 AM | WTI | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:43:22 AM | PLATINUM | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:43:22 AM | USDCAD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:43:04 AM | BTC | DOWN | 1.9 min | +0.179% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:42:48 AM | GBPUSD | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:42:32 AM | SOL | UP | 2.5 min | -0.402% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:42:16 AM | EURUSD | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:41:26 AM | COPPER | DOWN | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:40:54 AM | AUDUSD | DOWN | 4.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:40:06 AM | GOLD | DOWN | 4.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:39:50 AM | SILVER | DOWN | 5.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 4:29:32 AM | GBPUSD | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:28:58 AM | EURUSD | UP | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:28:42 AM | COPPER | DOWN | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:28:26 AM | PALLADIUM | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:28:26 AM | SILVER | DOWN | 1.6 min | — | 0¢ | ❌ Lost | $0.00 |
| 11/9 4:28:26 AM | USDCAD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:28:26 AM | GOLD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | $0.00 |
| 11/9 4:27:15 AM | NATGAS | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 4:26:40 AM | BRENT | UP | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
