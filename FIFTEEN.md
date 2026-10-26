# 15-Minute 1¢ Study

*Updated Mon Oct 26, 2:43 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2726 finished bets | 1% | $82.55 | +27% | +3.03¢ | $32.45 / $50.10 |

*Expect about **97 buys a day** (~$14.56/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2532 | $55.95 | +20% |
| Volatility model ≥ 2%, hold to the close | 5050 | -$16.75 | -3% |
| Momentum model ≥ 2%, hold to the close | 4211 | -$31.80 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 32460 | 32438 | 120 (0%) | 1.07% | -$2,260.80 (-57%) | Hold to the close: -$2,260.80 (-57%) |

*In play or awaiting result: 21. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 20889 | 4.6% | 0.4% (85) | -660% | ❌ Worse |
| Momentum model | 20889 | 4.5% | 0.4% (85) | -685% | ❌ Worse |
| Mean-reversion model | 20889 | 7.9% | 0.4% (85) | -800% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 20889 | 85 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5050 | 43 | -3% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2726 | 28 | +27% | -74% | -73% | -70% |
| Volatility model ≥ 10% | 1545 | 18 | +63% | -66% | -65% | -62% |
| Momentum model ≥ 2% | 4211 | 33 | -6% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2532 | 24 | +20% | -77% | -76% | -72% |
| Momentum model ≥ 10% | 1653 | 16 | +33% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 8426 | 56 | -28% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5902 | 47 | -12% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 3928 | 33 | -5% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21089 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7547 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3802 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 32438 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 120 | 0% | -$2,260.80 | -57% | — |
| Sell at 2¢ | 1210 | 4% | -$3,458.20 | -88% | 47 sec |
| Sell at 3¢ | 831 | 3% | -$3,448.71 | -88% | 48 sec |
| Sell at 5¢ | 578 | 2% | -$3,397.10 | -86% | 61 sec |
| Sell at 10¢ | 359 | 1% | -$3,260.51 | -83% | 65 sec |
| Sell at 25¢ | 193 | 1% | -$3,021.97 | -77% | 82 sec |
| Sell at 50¢ | 124 | 0% | -$2,739.80 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1432 | 7 | 11% | 4% | -53% | -81% | -82% |
| 2–5 min | 10386 | 55 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 8217 | 30 | 3% | 1% | -60% | -92% | -91% |
| Under 1 min | 12399 | 28 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2363 | 12 | 5% | 2% | -36% | -89% | -89% |
| HYPE | 2356 | 8 | 5% | 3% | -58% | -89% | -87% |
| BNB | 2352 | 13 | 5% | 3% | -31% | -84% | -83% |
| SOL | 2349 | 6 | 3% | 2% | -68% | -92% | -92% |
| ETH | 2343 | 11 | 6% | 3% | -43% | -86% | -85% |
| DOGE | 2336 | 4 | 4% | 2% | -79% | -91% | -90% |
| NEAR | 2333 | 12 | 5% | 2% | -33% | -82% | -82% |
| XRP | 2333 | 9 | 3% | 1% | -52% | -89% | -89% |
| BTC | 2324 | 12 | 5% | 2% | -31% | -88% | -89% |
| GOLD | 1221 | 4 | 4% | 1% | -61% | -81% | -83% |
| SILVER | 1187 | 5 | 4% | 2% | -51% | -82% | -81% |
| WTI | 1164 | 3 | 3% | 1% | -69% | -94% | -95% |
| PLATINUM | 1035 | 0 | 1% | 1% | -100% | -98% | -97% |
| COPPER | 1011 | 4 | 1% | 1% | -63% | -70% | -70% |
| EURUSD | 968 | 3 | 2% | 1% | -71% | -87% | -87% |
| NATGAS | 960 | 5 | 2% | 1% | -51% | -87% | -86% |
| PALLADIUM | 923 | 2 | 1% | 0% | -80% | -88% | -88% |
| GBPUSD | 912 | 1 | 2% | 1% | -90% | -96% | -97% |
| USDJPY | 896 | 5 | 1% | 1% | -48% | -98% | -97% |
| AUDUSD | 456 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 418 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 46 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 16424 | 66 | 4% | 2% | -54% | -87% | -87% |
| DOWN (bought NO) | 16014 | 54 | 4% | 1% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3518 | 18 | 2% | 1% | -14% | -80% | -80% |
| 0.05–0.1% | 3621 | 11 | 3% | 2% | -55% | -92% | -92% |
| 0.1–0.2% | 5451 | 20 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 6158 | 28 | 6% | 3% | -50% | -87% | -86% |
| Over 0.5% | 2337 | 10 | 7% | 3% | -56% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8076 | 32 | 4% | 2% | -55% | -85% | -85% |
| Morning (6am–12pm) | 7781 | 35 | 4% | 2% | -49% | -88% | -87% |
| Afternoon (12–6pm) | 7607 | 24 | 4% | 2% | -63% | -87% | -88% |
| Evening (6pm–12am) | 8974 | 29 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,816 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/26 2:43:17 AM | AUDUSD | DOWN | 1.7 min | — | — | In play | — |
| 10/26 2:42:11 AM | SILVER | DOWN | 2.8 min | — | — | In play | — |
| 10/26 2:41:21 AM | BTC | DOWN | 3.6 min | +0.304% | — | In play | — |
| 10/26 2:41:21 AM | BRENT | UP | 3.6 min | — | — | In play | — |
| 10/26 2:41:21 AM | BNB | DOWN | 3.6 min | +0.232% | — | In play | — |
| 10/26 2:41:06 AM | ETH | DOWN | 3.9 min | +0.381% | — | In play | — |
| 10/26 2:41:06 AM | SOL | DOWN | 3.9 min | +0.414% | — | In play | — |
| 10/26 2:41:06 AM | HYPE | DOWN | 3.9 min | +0.526% | — | In play | — |
| 10/26 2:40:49 AM | DOGE | DOWN | 4.2 min | +0.372% | — | In play | — |
| 10/26 2:40:49 AM | XRP | DOWN | 4.2 min | +0.398% | — | In play | — |
| 10/26 2:40:33 AM | NEAR | DOWN | 4.4 min | +0.846% | — | In play | — |
| 10/26 2:40:17 AM | GBPUSD | UP | 4.7 min | — | — | In play | — |
| 10/26 2:39:44 AM | WTI | UP | 5.3 min | — | — | In play | — |
| 10/26 2:38:38 AM | ZEC | DOWN | 6.4 min | +0.807% | — | In play | — |
| 10/26 2:29:29 AM | COPPER | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 2:29:13 AM | GBPUSD | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 2:29:13 AM | WTI | DOWN | 47 sec | — | 13¢ | ❌ Lost | $0.00 |
| 10/26 2:29:13 AM | EURUSD | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 2:28:42 AM | SILVER | UP | 77 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 2:26:04 AM | BTC | DOWN | 3.9 min | +0.361% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 2:25:16 AM | NEAR | DOWN | 4.7 min | +0.663% | 2¢ | ❌ Lost | -$0.15 |
| 10/26 2:25:16 AM | HYPE | DOWN | 4.7 min | +0.515% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 2:24:45 AM | DOGE | DOWN | 5.2 min | +0.518% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 2:24:45 AM | XRP | DOWN | 5.2 min | +0.471% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 2:23:57 AM | ZEC | DOWN | 6.0 min | +0.985% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 2:23:41 AM | BNB | DOWN | 6.3 min | +0.407% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 2:23:09 AM | ETH | DOWN | 6.8 min | +0.508% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 2:23:09 AM | SOL | DOWN | 6.8 min | +0.513% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 2:14:58 AM | USDJPY | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 2:14:26 AM | PLATINUM | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
