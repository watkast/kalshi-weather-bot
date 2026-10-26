# 15-Minute 1¢ Study

*Updated Mon Oct 26, 8:40 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2749 finished bets | 1% | $80.15 | +26% | +2.92¢ | $30.95 / $49.20 |

*Expect about **97 buys a day** (~$14.55/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2555 | $53.55 | +19% |
| Volatility model ≥ 2%, hold to the close | 5102 | -$22.60 | -4% |
| Momentum model ≥ 2%, hold to the close | 4248 | -$35.55 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 32899 | 32889 | 122 (0%) | 1.07% | -$2,290.10 (-57%) | Hold to the close: -$2,290.10 (-57%) |

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
| Volatility model | 21100 | 4.6% | 0.4% (85) | -663% | ❌ Worse |
| Momentum model | 21100 | 4.5% | 0.4% (85) | -688% | ❌ Worse |
| Mean-reversion model | 21100 | 7.9% | 0.4% (85) | -804% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21100 | 85 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 5102 | 43 | -4% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2749 | 28 | +26% | -75% | -74% | -70% |
| Volatility model ≥ 10% | 1556 | 18 | +62% | -66% | -65% | -62% |
| Momentum model ≥ 2% | 4248 | 33 | -7% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2555 | 24 | +19% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1664 | 16 | +32% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 8529 | 56 | -28% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 5970 | 47 | -13% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 3975 | 33 | -6% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21300 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7683 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3906 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 32889 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 122 | 0% | -$2,290.10 | -57% | — |
| Sell at 2¢ | 1238 | 4% | -$3,508.22 | -88% | 47 sec |
| Sell at 3¢ | 848 | 3% | -$3,499.38 | -88% | 48 sec |
| Sell at 5¢ | 591 | 2% | -$3,445.95 | -86% | 61 sec |
| Sell at 10¢ | 366 | 1% | -$3,308.64 | -83% | 65 sec |
| Sell at 25¢ | 195 | 1% | -$3,072.65 | -77% | 83 sec |
| Sell at 50¢ | 126 | 0% | -$2,783.60 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1455 | 8 | 11% | 4% | -48% | -81% | -82% |
| 2–5 min | 10553 | 56 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 8339 | 30 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 12538 | 28 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2387 | 12 | 5% | 3% | -36% | -89% | -89% |
| HYPE | 2379 | 8 | 5% | 3% | -58% | -88% | -86% |
| BNB | 2376 | 13 | 5% | 3% | -32% | -84% | -83% |
| SOL | 2373 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2367 | 11 | 6% | 3% | -44% | -86% | -85% |
| DOGE | 2359 | 4 | 4% | 2% | -79% | -91% | -90% |
| XRP | 2356 | 9 | 3% | 1% | -53% | -89% | -89% |
| NEAR | 2355 | 12 | 5% | 2% | -34% | -82% | -81% |
| BTC | 2348 | 12 | 5% | 2% | -31% | -88% | -89% |
| GOLD | 1240 | 4 | 4% | 2% | -62% | -81% | -83% |
| SILVER | 1207 | 6 | 4% | 2% | -42% | -82% | -81% |
| WTI | 1181 | 3 | 3% | 1% | -70% | -94% | -95% |
| PLATINUM | 1053 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 1026 | 4 | 1% | 1% | -64% | -70% | -70% |
| EURUSD | 985 | 3 | 2% | 1% | -72% | -87% | -87% |
| NATGAS | 977 | 5 | 2% | 1% | -52% | -87% | -86% |
| PALLADIUM | 942 | 2 | 1% | 0% | -80% | -88% | -88% |
| GBPUSD | 932 | 1 | 2% | 1% | -90% | -96% | -96% |
| USDJPY | 912 | 5 | 1% | 1% | -49% | -98% | -97% |
| AUDUSD | 474 | 1 | 1% | 1% | -80% | -98% | -97% |
| USDCAD | 436 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 57 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 48 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 43 | 1 | 5% | 0% | +117% | +125% | +123% |
| 30YRRATE | 42 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 34 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 16662 | 67 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 16227 | 55 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3536 | 18 | 2% | 1% | -14% | -80% | -80% |
| 0.05–0.1% | 3649 | 11 | 3% | 2% | -55% | -92% | -92% |
| 0.1–0.2% | 5503 | 20 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 6241 | 28 | 6% | 3% | -51% | -87% | -86% |
| Over 0.5% | 2367 | 10 | 7% | 3% | -56% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8317 | 33 | 4% | 2% | -55% | -85% | -85% |
| Morning (6am–12pm) | 7991 | 36 | 4% | 2% | -49% | -88% | -87% |
| Afternoon (12–6pm) | 7607 | 24 | 4% | 2% | -63% | -87% | -88% |
| Evening (6pm–12am) | 8974 | 29 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,772 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/26 8:40:07 AM | SILVER | DOWN | 4.9 min | — | — | In play | — |
| 10/26 8:39:34 AM | GOLD | DOWN | 5.4 min | — | — | In play | — |
| 10/26 8:29:56 AM | 10YRRATE | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:29:56 AM | 5YRRATE | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:29:40 AM | GOLD | DOWN | 20 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/26 8:29:40 AM | 2YRRATE | DOWN | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:29:40 AM | SOL | DOWN | 20 sec | +0.043% | 0¢ | ❌ Lost | $0.00 |
| 10/26 8:29:40 AM | ETH | DOWN | 20 sec | +0.019% | 0¢ | ❌ Lost | $0.00 |
| 10/26 8:29:24 AM | BNB | DOWN | 36 sec | -0.001% | 0¢ | ❌ Lost | $0.00 |
| 10/26 8:29:24 AM | NEAR | DOWN | 36 sec | +0.147% | 0¢ | ❌ Lost | $0.00 |
| 10/26 8:29:09 AM | BTC | UP | 50 sec | -0.131% | 0¢ | ❌ Lost | $0.00 |
| 10/26 8:29:09 AM | XRP | DOWN | 50 sec | +0.171% | 0¢ | ❌ Lost | $0.00 |
| 10/26 8:29:09 AM | EURUSD | DOWN | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:28:52 AM | DOGE | DOWN | 67 sec | +0.226% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 8:28:52 AM | GBPUSD | DOWN | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:28:36 AM | USDJPY | DOWN | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:28:36 AM | PALLADIUM | DOWN | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:28:20 AM | USDCAD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:28:20 AM | SILVER | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 8:27:02 AM | AUDUSD | DOWN | 3.0 min | — | 7¢ | ❌ Lost | -$0.15 |
| 10/26 8:26:31 AM | NATGAS | DOWN | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:23:21 AM | ZEC | DOWN | 6.7 min | +1.120% | 15¢ | ❌ Lost | -$0.15 |
| 10/26 8:23:05 AM | HYPE | DOWN | 6.9 min | +0.841% | 12¢ | ❌ Lost | -$0.15 |
| 10/26 8:14:47 AM | NATGAS | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:14:31 AM | 5YRRATE | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:14:15 AM | COPPER | DOWN | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:13:58 AM | PLATINUM | DOWN | 61 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 8:13:42 AM | AUDUSD | DOWN | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:13:42 AM | ZEC | DOWN | 77 sec | +0.419% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 8:13:26 AM | 10YRRATE | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
