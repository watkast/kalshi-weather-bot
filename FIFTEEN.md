# 15-Minute 1¢ Study

*Updated Mon Oct 26, 12:40 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2717 finished bets | 1% | $83.60 | +27% | +3.08¢ | $33.05 / $50.55 |

*Expect about **97 buys a day** (~$14.56/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2523 | $57.00 | +20% |
| Volatility model ≥ 2%, hold to the close | 5037 | -$15.10 | -2% |
| Momentum model ≥ 2%, hold to the close | 4199 | -$30.30 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 32316 | 32307 | 120 (0%) | 1.07% | -$2,244.75 (-57%) | Hold to the close: -$2,244.75 (-57%) |

*In play or awaiting result: 8. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 20818 | 4.6% | 0.4% (85) | -657% | ❌ Worse |
| Momentum model | 20818 | 4.5% | 0.4% (85) | -682% | ❌ Worse |
| Mean-reversion model | 20818 | 7.9% | 0.4% (85) | -796% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 20818 | 85 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5037 | 43 | -2% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2717 | 28 | +27% | -75% | -73% | -70% |
| Volatility model ≥ 10% | 1537 | 18 | +64% | -66% | -65% | -62% |
| Momentum model ≥ 2% | 4199 | 33 | -6% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2523 | 24 | +20% | -77% | -76% | -72% |
| Momentum model ≥ 10% | 1644 | 16 | +33% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 8395 | 56 | -27% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 5881 | 47 | -12% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 3914 | 33 | -5% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21018 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7512 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3777 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 32307 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 120 | 0% | -$2,244.75 | -57% | — |
| Sell at 2¢ | 1202 | 4% | -$3,444.23 | -88% | 47 sec |
| Sell at 3¢ | 824 | 3% | -$3,435.39 | -88% | 48 sec |
| Sell at 5¢ | 573 | 2% | -$3,384.30 | -86% | 61 sec |
| Sell at 10¢ | 354 | 1% | -$3,251.01 | -83% | 65 sec |
| Sell at 25¢ | 191 | 1% | -$3,012.54 | -77% | 82 sec |
| Sell at 50¢ | 122 | 0% | -$2,737.25 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1417 | 7 | 11% | 4% | -53% | -81% | -83% |
| 2–5 min | 10352 | 55 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 8178 | 30 | 3% | 1% | -60% | -92% | -91% |
| Under 1 min | 12356 | 28 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2355 | 12 | 5% | 2% | -35% | -89% | -89% |
| HYPE | 2348 | 8 | 5% | 3% | -58% | -89% | -87% |
| BNB | 2345 | 13 | 5% | 3% | -31% | -84% | -83% |
| SOL | 2341 | 6 | 3% | 1% | -68% | -92% | -92% |
| ETH | 2335 | 11 | 6% | 3% | -43% | -86% | -85% |
| DOGE | 2328 | 4 | 4% | 2% | -79% | -91% | -90% |
| NEAR | 2325 | 12 | 5% | 2% | -33% | -82% | -81% |
| XRP | 2325 | 9 | 3% | 1% | -52% | -89% | -88% |
| BTC | 2316 | 12 | 5% | 2% | -30% | -88% | -89% |
| GOLD | 1217 | 4 | 4% | 1% | -61% | -81% | -83% |
| SILVER | 1182 | 5 | 4% | 2% | -51% | -82% | -82% |
| WTI | 1159 | 3 | 3% | 1% | -69% | -94% | -95% |
| PLATINUM | 1030 | 0 | 1% | 1% | -100% | -98% | -97% |
| COPPER | 1006 | 4 | 1% | 1% | -63% | -70% | -70% |
| EURUSD | 962 | 3 | 2% | 1% | -71% | -87% | -87% |
| NATGAS | 955 | 5 | 2% | 1% | -51% | -87% | -86% |
| PALLADIUM | 918 | 2 | 1% | 0% | -80% | -88% | -88% |
| GBPUSD | 908 | 1 | 2% | 1% | -90% | -96% | -97% |
| USDJPY | 892 | 5 | 1% | 1% | -48% | -98% | -97% |
| AUDUSD | 451 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 412 | 0 | 1% | 0% | -100% | -97% | -99% |
| BRENT | 45 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 16371 | 66 | 4% | 2% | -54% | -87% | -87% |
| DOWN (bought NO) | 15936 | 54 | 4% | 1% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3507 | 18 | 2% | 1% | -13% | -80% | -80% |
| 0.05–0.1% | 3612 | 11 | 3% | 1% | -55% | -92% | -92% |
| 0.1–0.2% | 5432 | 20 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 6135 | 28 | 6% | 3% | -50% | -87% | -86% |
| Over 0.5% | 2328 | 10 | 7% | 3% | -56% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7945 | 32 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 7781 | 35 | 4% | 2% | -49% | -88% | -87% |
| Afternoon (12–6pm) | 7607 | 24 | 4% | 2% | -63% | -87% | -88% |
| Evening (6pm–12am) | 8974 | 29 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,819 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/26 12:39:56 AM | HYPE | DOWN | 5.1 min | +0.432% | — | In play | — |
| 10/26 12:29:30 AM | GOLD | UP | 29 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/26 12:29:30 AM | AUDUSD | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:29:14 AM | PALLADIUM | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:28:56 AM | ZEC | UP | 64 sec | -0.293% | 0¢ | ❌ Lost | $0.00 |
| 10/26 12:28:40 AM | XRP | UP | 80 sec | -0.163% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 12:28:40 AM | NEAR | UP | 80 sec | -0.329% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 12:28:09 AM | DOGE | UP | 1.9 min | -0.144% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 12:28:09 AM | HYPE | UP | 1.9 min | -0.213% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 12:28:09 AM | PLATINUM | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:28:09 AM | SOL | UP | 1.9 min | -0.179% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 12:27:51 AM | BTC | UP | 2.1 min | -0.130% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 12:27:51 AM | SILVER | UP | 2.1 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/26 12:27:19 AM | ETH | UP | 2.7 min | -0.227% | 0¢ | ❌ Lost | $0.00 |
| 10/26 12:26:48 AM | USDJPY | UP | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:26:32 AM | NATGAS | DOWN | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:26:32 AM | BNB | UP | 3.5 min | -0.178% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 12:25:11 AM | USDCAD | UP | 4.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:23:32 AM | EURUSD | DOWN | 6.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 12:21:24 AM | GBPUSD | DOWN | 8.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 12:14:59 AM | COPPER | DOWN | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:14:27 AM | BRENT | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:14:11 AM | NATGAS | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:14:11 AM | PALLADIUM | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:13:38 AM | WTI | DOWN | 82 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 12:13:38 AM | USDJPY | DOWN | 82 sec | — | 5¢ | ❌ Lost | -$0.15 |
| 10/26 12:13:38 AM | PLATINUM | UP | 82 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:13:22 AM | EURUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:12:47 AM | USDCAD | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:12:47 AM | AUDUSD | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
