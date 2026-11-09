# 15-Minute 1¢ Study

*Updated Mon Nov 9, 2:08 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4076 finished bets | 1% | $190.85 | +42% | +4.68¢ | $93.25 / $97.60 |

*Expect about **97 buys a day** (~$14.52/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3783 | $108.50 | +26% |
| Volatility model ≥ 2%, hold to the close | 7467 | $81.35 | +9% |
| Momentum model ≥ 2%, hold to the close | 6160 | $6.45 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 50593 | 50576 | 187 (0%) | 1.07% | -$3,535.45 (-57%) | Hold to the close: -$3,535.45 (-57%) |

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
| Volatility model | 30915 | 4.8% | 0.4% (122) | -688% | ❌ Worse |
| Momentum model | 30915 | 4.6% | 0.4% (122) | -714% | ❌ Worse |
| Mean-reversion model | 30915 | 8.1% | 0.4% (122) | -831% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 30915 | 122 | -50% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7467 | 70 | +9% | -76% | -75% | -71% |
| Volatility model ≥ 5% | 4076 | 46 | +42% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2347 | 28 | +71% | -61% | -59% | -55% |
| Momentum model ≥ 2% | 6160 | 51 | +1% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3783 | 37 | +26% | -73% | -72% | -68% |
| Momentum model ≥ 10% | 2481 | 25 | +42% | -64% | -64% | -59% |
| Mean-reversion model ≥ 2% | 12786 | 90 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 8967 | 77 | -5% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 5993 | 56 | +6% | -76% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31120 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11917 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7539 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 50576 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 187 | 0% | -$3,535.45 | -57% | — |
| Sell at 2¢ | 1996 | 4% | -$5,354.49 | -87% | 47 sec |
| Sell at 3¢ | 1356 | 3% | -$5,344.61 | -87% | 48 sec |
| Sell at 5¢ | 947 | 2% | -$5,229.90 | -85% | 62 sec |
| Sell at 10¢ | 571 | 1% | -$5,013.44 | -81% | 65 sec |
| Sell at 25¢ | 298 | 1% | -$4,663.07 | -76% | 83 sec |
| Sell at 50¢ | 192 | 0% | -$4,255.45 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2507 | 12 | 11% | 4% | -55% | -81% | -82% |
| 2–5 min | 16347 | 88 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 12776 | 41 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 18934 | 46 | 1% | 0% | -65% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3489 | 14 | 5% | 2% | -48% | -88% | -88% |
| SOL | 3480 | 15 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3471 | 11 | 5% | 2% | -60% | -89% | -88% |
| BNB | 3465 | 18 | 5% | 2% | -34% | -86% | -85% |
| DOGE | 3464 | 7 | 4% | 2% | -75% | -90% | -90% |
| ETH | 3457 | 14 | 7% | 3% | -50% | -81% | -81% |
| NEAR | 3436 | 16 | 5% | 2% | -40% | -85% | -85% |
| BTC | 3434 | 16 | 5% | 2% | -36% | -87% | -89% |
| XRP | 3424 | 13 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1816 | 5 | 6% | 2% | -66% | -81% | -82% |
| WTI | 1785 | 6 | 4% | 1% | -60% | -92% | -92% |
| SILVER | 1767 | 8 | 5% | 2% | -47% | -82% | -82% |
| PLATINUM | 1599 | 4 | 2% | 1% | -77% | -96% | -96% |
| EURUSD | 1532 | 4 | 2% | 1% | -76% | -90% | -89% |
| COPPER | 1499 | 6 | 2% | 1% | -63% | -72% | -72% |
| NATGAS | 1459 | 8 | 2% | 1% | -49% | -77% | -77% |
| GBPUSD | 1454 | 4 | 2% | 1% | -74% | -96% | -96% |
| USDJPY | 1439 | 5 | 2% | 1% | -68% | -97% | -96% |
| PALLADIUM | 1436 | 3 | 1% | 0% | -81% | -92% | -92% |
| AUDUSD | 994 | 5 | 2% | 1% | -53% | -87% | -87% |
| USDCAD | 960 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 556 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 308 | 1 | 4% | 1% | -70% | -62% | -60% |
| 2YRRATE | 292 | 3 | 4% | 1% | -4% | -29% | -28% |
| 30YRRATE | 287 | 0 | 2% | 1% | -100% | -96% | -95% |
| 5YRRATE | 266 | 1 | 4% | 2% | -65% | -93% | -95% |
| INX | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 25645 | 96 | 4% | 2% | -57% | -88% | -87% |
| DOWN (bought NO) | 24931 | 91 | 4% | 2% | -58% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5047 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5326 | 19 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 8008 | 27 | 5% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 9253 | 39 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 3478 | 14 | 7% | 3% | -58% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12351 | 43 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 12223 | 54 | 4% | 2% | -50% | -84% | -84% |
| Afternoon (12–6pm) | 12200 | 47 | 4% | 2% | -55% | -86% | -86% |
| Evening (6pm–12am) | 13802 | 43 | 4% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,947 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/9 1:59:52 AM | BRENT | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:59:52 AM | USDJPY | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:59:36 AM | AUDUSD | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:59:21 AM | WTI | DOWN | 38 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 1:59:03 AM | GBPUSD | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:58:47 AM | NATGAS | DOWN | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:58:17 AM | SILVER | UP | 1.7 min | — | 3¢ | ❌ Lost | -$0.15 |
| 11/9 1:57:59 AM | PLATINUM | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:57:12 AM | GOLD | UP | 2.8 min | — | 0¢ | ❌ Lost | $0.00 |
| 11/9 1:57:12 AM | 2YRRATE | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:56:54 AM | 30YRRATE | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:56:38 AM | DOGE | DOWN | 3.4 min | +0.297% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 1:56:38 AM | 10YRRATE | DOWN | 3.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:56:38 AM | BNB | DOWN | 3.4 min | +0.164% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 1:55:49 AM | ZEC | DOWN | 4.2 min | +0.765% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 1:55:49 AM | 5YRRATE | DOWN | 4.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:55:17 AM | SOL | DOWN | 4.7 min | +0.445% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 1:55:17 AM | NEAR | DOWN | 4.7 min | +0.716% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 1:55:17 AM | BTC | DOWN | 4.7 min | +0.260% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 1:55:02 AM | ETH | DOWN | 5.0 min | +0.508% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 1:55:02 AM | XRP | DOWN | 5.0 min | +0.522% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 1:54:28 AM | HYPE | DOWN | 5.5 min | +0.820% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 1:44:13 AM | SOL | DOWN | 46 sec | +0.163% | 0¢ | ❌ Lost | $0.00 |
| 11/9 1:43:39 AM | DOGE | DOWN | 81 sec | +0.190% | 0¢ | ❌ Lost | $0.00 |
| 11/9 1:43:39 AM | NEAR | DOWN | 81 sec | +0.219% | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:43:39 AM | BNB | DOWN | 81 sec | +0.094% | 0¢ | ❌ Lost | $0.00 |
| 11/9 1:43:39 AM | GOLD | DOWN | 81 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/9 1:43:39 AM | NATGAS | DOWN | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:43:39 AM | ETH | DOWN | 81 sec | +0.222% | 0¢ | ❌ Lost | $0.00 |
| 11/9 1:43:23 AM | COPPER | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
