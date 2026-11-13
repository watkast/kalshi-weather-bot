# 15-Minute 1¢ Study

*Updated Fri Nov 13, 4:24 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4278 finished bets | 1% | $169.10 | +36% | +3.95¢ | $81.10 / $88.00 |

*Expect about **93 buys a day** (~$13.89/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4018 | $96.25 | +22% |
| Volatility model ≥ 2%, hold to the close | 7896 | $29.45 | +3% |
| Momentum model ≥ 2%, hold to the close | 6554 | -$25.30 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 55790 | 55766 | 212 (0%) | 1.07% | -$3,836.00 (-56%) | Hold to the close: -$3,836.00 (-56%) |

*In play or awaiting result: 12. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 33303 | 4.7% | 0.4% (133) | -671% | ❌ Worse |
| Momentum model | 33303 | 4.6% | 0.4% (133) | -697% | ❌ Worse |
| Mean-reversion model | 33303 | 8.0% | 0.4% (133) | -813% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 33303 | 133 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 7896 | 70 | +3% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4278 | 46 | +36% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 2477 | 28 | +62% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6554 | 52 | -3% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4018 | 38 | +22% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2634 | 25 | +33% | -66% | -65% | -61% |
| Mean-reversion model ≥ 2% | 13714 | 93 | -26% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9568 | 79 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6379 | 56 | -0% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 33508 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 13445 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8813 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 55766 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 212 | 0% | -$3,836.00 | -56% | — |
| Sell at 2¢ | 2223 | 4% | -$5,932.02 | -87% | 47 sec |
| Sell at 3¢ | 1510 | 3% | -$5,921.10 | -87% | 49 sec |
| Sell at 5¢ | 1038 | 2% | -$5,807.30 | -85% | 63 sec |
| Sell at 10¢ | 630 | 1% | -$5,572.70 | -82% | 65 sec |
| Sell at 25¢ | 330 | 1% | -$5,179.70 | -76% | 82 sec |
| Sell at 50¢ | 217 | 0% | -$4,695.25 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2773 | 13 | 11% | 4% | -56% | -81% | -82% |
| 2–5 min | 17984 | 97 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 14060 | 46 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 20936 | 56 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3751 | 17 | 5% | 3% | -41% | -88% | -87% |
| SOL | 3746 | 16 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3741 | 11 | 5% | 2% | -63% | -89% | -88% |
| BNB | 3728 | 19 | 5% | 2% | -36% | -86% | -85% |
| DOGE | 3727 | 8 | 4% | 2% | -73% | -90% | -90% |
| ETH | 3721 | 16 | 7% | 3% | -47% | -82% | -81% |
| BTC | 3704 | 18 | 5% | 2% | -33% | -87% | -88% |
| NEAR | 3702 | 17 | 5% | 2% | -40% | -85% | -85% |
| XRP | 3688 | 13 | 3% | 1% | -56% | -89% | -89% |
| GOLD | 2020 | 5 | 5% | 2% | -70% | -82% | -84% |
| WTI | 1999 | 7 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 1961 | 9 | 5% | 2% | -45% | -83% | -83% |
| PLATINUM | 1787 | 4 | 3% | 1% | -79% | -96% | -95% |
| EURUSD | 1734 | 6 | 3% | 1% | -68% | -90% | -90% |
| COPPER | 1676 | 6 | 2% | 1% | -67% | -74% | -74% |
| GBPUSD | 1659 | 6 | 2% | 1% | -66% | -96% | -96% |
| NATGAS | 1650 | 9 | 2% | 1% | -49% | -74% | -73% |
| USDJPY | 1625 | 6 | 2% | 1% | -66% | -96% | -96% |
| PALLADIUM | 1603 | 4 | 1% | 0% | -77% | -92% | -92% |
| AUDUSD | 1177 | 6 | 2% | 1% | -52% | -89% | -89% |
| USDCAD | 1143 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 749 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 379 | 2 | 4% | 2% | -51% | -69% | -66% |
| 2YRRATE | 363 | 4 | 4% | 2% | +3% | -42% | -41% |
| 30YRRATE | 359 | 0 | 3% | 1% | -100% | -96% | -93% |
| 5YRRATE | 333 | 2 | 4% | 2% | -44% | -93% | -95% |
| INX | 41 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 28346 | 110 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 27420 | 102 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5259 | 25 | 2% | 1% | -16% | -77% | -77% |
| 0.05–0.1% | 5664 | 20 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 8562 | 31 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 10142 | 41 | 6% | 3% | -55% | -87% | -87% |
| Over 0.5% | 3873 | 18 | 7% | 3% | -52% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13606 | 44 | 4% | 2% | -63% | -88% | -88% |
| Morning (6am–12pm) | 13343 | 62 | 4% | 2% | -47% | -85% | -84% |
| Afternoon (12–6pm) | 13453 | 59 | 4% | 2% | -49% | -86% | -87% |
| Evening (6pm–12am) | 15364 | 47 | 4% | 2% | -65% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,823 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/13 4:24:18 AM | ETH | DOWN | 5.7 min | +0.476% | — | In play | — |
| 11/13 4:24:18 AM | SOL | DOWN | 5.7 min | +0.363% | — | In play | — |
| 11/13 4:24:18 AM | BNB | DOWN | 5.7 min | +0.296% | — | In play | — |
| 11/13 4:14:48 AM | USDJPY | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 4:14:48 AM | SILVER | DOWN | 11 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/13 4:14:48 AM | EURUSD | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 4:14:48 AM | ETH | DOWN | 11 sec | +0.049% | 0¢ | ❌ Lost | $0.00 |
| 11/13 4:14:48 AM | NATGAS | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 4:14:48 AM | 2YRRATE | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 4:14:16 AM | GBPUSD | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 4:14:16 AM | BNB | UP | 43 sec | -0.105% | 0¢ | ❌ Lost | $0.00 |
| 11/13 4:14:00 AM | ZEC | DOWN | 59 sec | +0.302% | 0¢ | ❌ Lost | $0.00 |
| 11/13 4:14:00 AM | NEAR | DOWN | 59 sec | +0.283% | 0¢ | ❌ Lost | -$0.15 |
| 11/13 4:14:00 AM | SOL | UP | 59 sec | -0.151% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 4:13:44 AM | BTC | UP | 75 sec | -0.092% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 4:13:44 AM | PALLADIUM | DOWN | 75 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 4:12:55 AM | DOGE | UP | 2.1 min | -0.164% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 4:12:39 AM | HYPE | DOWN | 2.3 min | +0.254% | 0¢ | ❌ Lost | -$0.15 |
| 11/13 4:10:29 AM | XRP | UP | 4.5 min | -0.430% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 3:59:46 AM | XRP | UP | 14 sec | -0.078% | 0¢ | ❌ Lost | $0.00 |
| 11/13 3:59:46 AM | COPPER | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 3:59:46 AM | USDCAD | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 3:59:46 AM | GOLD | UP | 14 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/13 3:59:46 AM | 10YRRATE | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 3:59:31 AM | SILVER | UP | 29 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/13 3:59:31 AM | ZEC | DOWN | 29 sec | +0.070% | 0¢ | ❌ Lost | $0.00 |
| 11/13 3:58:58 AM | NATGAS | DOWN | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 3:58:58 AM | SOL | DOWN | 61 sec | +0.108% | 0¢ | ❌ Lost | $0.00 |
| 11/13 3:58:58 AM | DOGE | DOWN | 61 sec | +0.106% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 3:58:42 AM | WTI | DOWN | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
