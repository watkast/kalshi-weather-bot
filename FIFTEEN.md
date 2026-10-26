# 15-Minute 1¢ Study

*Updated Mon Oct 26, 3:42 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2729 finished bets | 1% | $82.25 | +27% | +3.01¢ | $32.30 / $49.95 |

*Expect about **97 buys a day** (~$14.55/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2535 | $55.65 | +20% |
| Volatility model ≥ 2%, hold to the close | 5062 | -$18.10 | -3% |
| Momentum model ≥ 2%, hold to the close | 4216 | -$32.40 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 32509 | 32498 | 121 (0%) | 1.07% | -$2,254.00 (-57%) | Hold to the close: -$2,254.00 (-57%) |

*In play or awaiting result: 10. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 20922 | 4.6% | 0.4% (85) | -661% | ❌ Worse |
| Momentum model | 20922 | 4.5% | 0.4% (85) | -686% | ❌ Worse |
| Mean-reversion model | 20922 | 7.9% | 0.4% (85) | -802% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 20922 | 85 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5062 | 43 | -3% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2729 | 28 | +27% | -75% | -73% | -70% |
| Volatility model ≥ 10% | 1546 | 18 | +63% | -66% | -65% | -62% |
| Momentum model ≥ 2% | 4216 | 33 | -7% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2535 | 24 | +20% | -77% | -76% | -72% |
| Momentum model ≥ 10% | 1655 | 16 | +32% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 8447 | 56 | -28% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 5916 | 47 | -13% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 3939 | 33 | -5% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21122 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7564 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3812 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 32498 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 121 | 0% | -$2,254.00 | -57% | — |
| Sell at 2¢ | 1212 | 4% | -$3,464.88 | -88% | 47 sec |
| Sell at 3¢ | 833 | 3% | -$3,455.13 | -88% | 48 sec |
| Sell at 5¢ | 580 | 2% | -$3,403.00 | -86% | 61 sec |
| Sell at 10¢ | 361 | 1% | -$3,265.09 | -83% | 65 sec |
| Sell at 25¢ | 194 | 1% | -$3,025.86 | -77% | 82 sec |
| Sell at 50¢ | 125 | 0% | -$2,740.25 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1439 | 7 | 11% | 4% | -54% | -81% | -82% |
| 2–5 min | 10410 | 56 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8231 | 30 | 3% | 1% | -60% | -92% | -91% |
| Under 1 min | 12414 | 28 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2367 | 12 | 5% | 2% | -36% | -89% | -89% |
| HYPE | 2359 | 8 | 5% | 3% | -58% | -89% | -87% |
| BNB | 2356 | 13 | 5% | 3% | -31% | -84% | -83% |
| SOL | 2353 | 6 | 3% | 2% | -68% | -92% | -92% |
| ETH | 2347 | 11 | 6% | 3% | -44% | -86% | -85% |
| DOGE | 2340 | 4 | 4% | 2% | -79% | -91% | -90% |
| NEAR | 2336 | 12 | 5% | 2% | -33% | -82% | -82% |
| XRP | 2336 | 9 | 3% | 1% | -52% | -89% | -89% |
| BTC | 2328 | 12 | 5% | 2% | -31% | -88% | -89% |
| GOLD | 1223 | 4 | 4% | 2% | -61% | -81% | -83% |
| SILVER | 1189 | 6 | 4% | 2% | -41% | -82% | -81% |
| WTI | 1167 | 3 | 3% | 1% | -69% | -94% | -95% |
| PLATINUM | 1036 | 0 | 1% | 1% | -100% | -98% | -97% |
| COPPER | 1014 | 4 | 1% | 1% | -63% | -70% | -70% |
| EURUSD | 969 | 3 | 2% | 1% | -71% | -87% | -87% |
| NATGAS | 962 | 5 | 2% | 1% | -51% | -87% | -86% |
| PALLADIUM | 925 | 2 | 1% | 0% | -80% | -88% | -88% |
| GBPUSD | 915 | 1 | 2% | 1% | -90% | -96% | -97% |
| USDJPY | 897 | 5 | 1% | 1% | -48% | -98% | -97% |
| AUDUSD | 459 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 420 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 48 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 16456 | 66 | 4% | 2% | -54% | -87% | -87% |
| DOWN (bought NO) | 16042 | 55 | 4% | 2% | -60% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3519 | 18 | 2% | 1% | -14% | -80% | -80% |
| 0.05–0.1% | 3624 | 11 | 3% | 2% | -55% | -92% | -92% |
| 0.1–0.2% | 5460 | 20 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 6173 | 28 | 6% | 3% | -50% | -87% | -86% |
| Over 0.5% | 2342 | 10 | 7% | 3% | -56% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8136 | 33 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 7781 | 35 | 4% | 2% | -49% | -88% | -87% |
| Afternoon (12–6pm) | 7607 | 24 | 4% | 2% | -63% | -87% | -88% |
| Evening (6pm–12am) | 8974 | 29 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,812 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/26 3:41:33 AM | GOLD | DOWN | 3.4 min | — | — | In play | — |
| 10/26 3:41:17 AM | COPPER | DOWN | 3.7 min | — | — | In play | — |
| 10/26 3:41:01 AM | PALLADIUM | DOWN | 4.0 min | — | — | In play | — |
| 10/26 3:25:46 AM | ZEC | DOWN | 4.2 min | +0.533% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 3:24:59 AM | ETH | DOWN | 5.0 min | +0.357% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 3:24:59 AM | BNB | DOWN | 5.0 min | +0.292% | 0¢ | ❌ Lost | $0.00 |
| 10/26 3:24:59 AM | BTC | DOWN | 5.0 min | +0.314% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 3:24:59 AM | SOL | DOWN | 5.0 min | +0.390% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 3:24:59 AM | DOGE | DOWN | 5.0 min | +0.427% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 3:14:51 AM | GOLD | UP | 8 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/26 3:14:51 AM | ZEC | DOWN | 8 sec | -0.065% | 0¢ | ❌ Lost | $0.00 |
| 10/26 3:14:51 AM | SILVER | UP | 8 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/26 3:14:51 AM | BTC | UP | 8 sec | -0.026% | 0¢ | ❌ Lost | $0.00 |
| 10/26 3:14:35 AM | PALLADIUM | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 3:14:12 AM | GBPUSD | DOWN | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 3:14:12 AM | BNB | UP | 48 sec | -0.102% | 0¢ | ❌ Lost | $0.00 |
| 10/26 3:14:12 AM | USDCAD | UP | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 3:14:12 AM | SOL | UP | 48 sec | -0.130% | 0¢ | ❌ Lost | $0.00 |
| 10/26 3:13:54 AM | ETH | UP | 66 sec | -0.081% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 3:13:38 AM | NEAR | UP | 82 sec | -0.441% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 3:13:38 AM | HYPE | UP | 82 sec | -0.236% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 3:13:38 AM | XRP | UP | 82 sec | -0.179% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 3:13:07 AM | DOGE | UP | 1.9 min | -0.173% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 3:12:50 AM | BRENT | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 3:12:18 AM | NATGAS | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 3:12:02 AM | WTI | UP | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 3:12:02 AM | COPPER | DOWN | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 3:12:02 AM | EURUSD | DOWN | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 3:10:23 AM | AUDUSD | DOWN | 4.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 2:59:58 AM | NATGAS | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
