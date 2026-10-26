# 15-Minute 1¢ Study

*Updated Mon Oct 26, 1:21 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2724 finished bets | 1% | $82.85 | +27% | +3.04¢ | $32.60 / $50.25 |

*Expect about **97 buys a day** (~$14.58/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2530 | $56.25 | +20% |
| Volatility model ≥ 2%, hold to the close | 5045 | -$16.00 | -3% |
| Momentum model ≥ 2%, hold to the close | 4208 | -$31.35 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 32365 | 32357 | 120 (0%) | 1.07% | -$2,250.60 (-57%) | Hold to the close: -$2,250.60 (-57%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 20845 | 4.6% | 0.4% (85) | -661% | ❌ Worse |
| Momentum model | 20845 | 4.6% | 0.4% (85) | -685% | ❌ Worse |
| Mean-reversion model | 20845 | 7.9% | 0.4% (85) | -800% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 20845 | 85 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5045 | 43 | -3% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2724 | 28 | +27% | -74% | -73% | -70% |
| Volatility model ≥ 10% | 1543 | 18 | +63% | -66% | -64% | -62% |
| Momentum model ≥ 2% | 4208 | 33 | -6% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2530 | 24 | +20% | -77% | -76% | -72% |
| Momentum model ≥ 10% | 1651 | 16 | +33% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 8408 | 56 | -27% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5891 | 47 | -12% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 3921 | 33 | -5% | -78% | -78% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21045 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7526 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3786 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 32357 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 120 | 0% | -$2,250.60 | -57% | — |
| Sell at 2¢ | 1205 | 4% | -$3,449.30 | -88% | 47 sec |
| Sell at 3¢ | 827 | 3% | -$3,440.07 | -88% | 48 sec |
| Sell at 5¢ | 575 | 2% | -$3,388.85 | -86% | 61 sec |
| Sell at 10¢ | 356 | 1% | -$3,254.24 | -83% | 65 sec |
| Sell at 25¢ | 192 | 1% | -$3,015.08 | -77% | 82 sec |
| Sell at 50¢ | 123 | 0% | -$2,736.35 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1419 | 7 | 11% | 4% | -53% | -81% | -83% |
| 2–5 min | 10361 | 55 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 8193 | 30 | 3% | 1% | -60% | -92% | -91% |
| Under 1 min | 12380 | 28 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2358 | 12 | 5% | 2% | -35% | -89% | -89% |
| HYPE | 2351 | 8 | 5% | 3% | -58% | -89% | -87% |
| BNB | 2348 | 13 | 5% | 3% | -31% | -84% | -82% |
| SOL | 2344 | 6 | 3% | 1% | -68% | -92% | -92% |
| ETH | 2338 | 11 | 6% | 3% | -43% | -86% | -85% |
| DOGE | 2331 | 4 | 4% | 2% | -79% | -91% | -90% |
| NEAR | 2328 | 12 | 5% | 2% | -33% | -82% | -82% |
| XRP | 2328 | 9 | 3% | 1% | -52% | -89% | -88% |
| BTC | 2319 | 12 | 5% | 2% | -31% | -88% | -89% |
| GOLD | 1219 | 4 | 4% | 1% | -61% | -81% | -83% |
| SILVER | 1183 | 5 | 4% | 2% | -51% | -82% | -82% |
| WTI | 1161 | 3 | 3% | 1% | -69% | -94% | -95% |
| PLATINUM | 1032 | 0 | 1% | 1% | -100% | -98% | -97% |
| COPPER | 1008 | 4 | 1% | 1% | -63% | -70% | -70% |
| EURUSD | 964 | 3 | 2% | 1% | -71% | -87% | -87% |
| NATGAS | 957 | 5 | 2% | 1% | -51% | -87% | -86% |
| PALLADIUM | 920 | 2 | 1% | 0% | -80% | -88% | -88% |
| GBPUSD | 909 | 1 | 2% | 1% | -90% | -96% | -97% |
| USDJPY | 893 | 5 | 1% | 1% | -48% | -98% | -97% |
| AUDUSD | 454 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 414 | 0 | 1% | 0% | -100% | -97% | -99% |
| BRENT | 46 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 16385 | 66 | 4% | 2% | -54% | -87% | -87% |
| DOWN (bought NO) | 15972 | 54 | 4% | 1% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3515 | 18 | 2% | 1% | -13% | -80% | -80% |
| 0.05–0.1% | 3616 | 11 | 3% | 2% | -55% | -92% | -92% |
| 0.1–0.2% | 5443 | 20 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 6139 | 28 | 6% | 3% | -50% | -87% | -86% |
| Over 0.5% | 2328 | 10 | 7% | 3% | -56% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7995 | 32 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 7781 | 35 | 4% | 2% | -49% | -88% | -87% |
| Afternoon (12–6pm) | 7607 | 24 | 4% | 2% | -63% | -87% | -88% |
| Evening (6pm–12am) | 8974 | 29 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,813 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/26 1:14:59 AM | PLATINUM | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 1:14:59 AM | HYPE | UP | 0 sec | +0.031% | 0¢ | ❌ Lost | $0.00 |
| 10/26 1:14:59 AM | BTC | DOWN | 0 sec | -0.014% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 1:14:59 AM | GOLD | UP | 0 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/26 1:14:59 AM | COPPER | DOWN | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 1:14:59 AM | GBPUSD | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 1:14:59 AM | DOGE | DOWN | 0 sec | +0.006% | 0¢ | ❌ Lost | $0.00 |
| 10/26 1:14:59 AM | SILVER | UP | 0 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/26 1:14:43 AM | AUDUSD | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 1:14:43 AM | USDJPY | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 1:14:43 AM | BNB | DOWN | 16 sec | +0.004% | 0¢ | ❌ Lost | $0.00 |
| 10/26 1:14:28 AM | ZEC | DOWN | 31 sec | +0.171% | 0¢ | ❌ Lost | $0.00 |
| 10/26 1:14:28 AM | NEAR | DOWN | 31 sec | +0.121% | 0¢ | ❌ Lost | $0.00 |
| 10/26 1:14:11 AM | PALLADIUM | UP | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 1:13:55 AM | SOL | UP | 64 sec | -0.126% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 1:13:55 AM | ETH | UP | 64 sec | -0.089% | 67¢ | ❌ Lost | -$0.15 |
| 10/26 1:13:23 AM | USDCAD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 1:13:23 AM | XRP | UP | 1.6 min | -0.187% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 1:13:05 AM | NATGAS | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 1:09:55 AM | EURUSD | UP | 5.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:59:55 AM | WTI | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:59:55 AM | USDCAD | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:59:23 AM | HYPE | DOWN | 37 sec | +0.076% | 0¢ | ❌ Lost | $0.00 |
| 10/26 12:59:04 AM | PALLADIUM | DOWN | 56 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 12:58:48 AM | AUDUSD | DOWN | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:58:48 AM | EURUSD | UP | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:58:17 AM | SOL | DOWN | 1.7 min | +0.167% | 0¢ | ❌ Lost | $0.00 |
| 10/26 12:58:17 AM | BNB | DOWN | 1.7 min | +0.037% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 12:58:17 AM | ZEC | DOWN | 1.7 min | +0.280% | 0¢ | ❌ Lost | $0.00 |
| 10/26 12:58:00 AM | BTC | DOWN | 2.0 min | +0.093% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
