# 15-Minute 1¢ Study

*Updated Mon Nov 9, 12:56 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4073 finished bets | 1% | $191.15 | +42% | +4.69¢ | $93.55 / $97.60 |

*Expect about **97 buys a day** (~$14.53/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3780 | $108.80 | +27% |
| Volatility model ≥ 2%, hold to the close | 7454 | $82.85 | +9% |
| Momentum model ≥ 2%, hold to the close | 6154 | $6.90 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 50482 | 50463 | 186 (0%) | 1.07% | -$3,535.20 (-58%) | Hold to the close: -$3,535.20 (-58%) |

*In play or awaiting result: 11. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 30870 | 4.8% | 0.4% (121) | -692% | ❌ Worse |
| Momentum model | 30870 | 4.6% | 0.4% (121) | -718% | ❌ Worse |
| Mean-reversion model | 30870 | 8.1% | 0.4% (121) | -836% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 30870 | 121 | -50% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7454 | 70 | +9% | -76% | -75% | -71% |
| Volatility model ≥ 5% | 4073 | 46 | +42% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2344 | 28 | +71% | -61% | -59% | -55% |
| Momentum model ≥ 2% | 6154 | 51 | +1% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3780 | 37 | +27% | -73% | -72% | -68% |
| Momentum model ≥ 10% | 2479 | 25 | +42% | -64% | -64% | -59% |
| Mean-reversion model ≥ 2% | 12758 | 89 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 8944 | 77 | -4% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 5979 | 56 | +7% | -76% | -76% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31075 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11885 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7503 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 50463 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 186 | 0% | -$3,535.20 | -58% | — |
| Sell at 2¢ | 1990 | 4% | -$5,341.80 | -87% | 47 sec |
| Sell at 3¢ | 1351 | 3% | -$5,332.31 | -87% | 48 sec |
| Sell at 5¢ | 945 | 2% | -$5,216.95 | -85% | 62 sec |
| Sell at 10¢ | 569 | 1% | -$5,001.81 | -81% | 65 sec |
| Sell at 25¢ | 297 | 1% | -$4,652.13 | -76% | 83 sec |
| Sell at 50¢ | 191 | 0% | -$4,247.95 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2496 | 12 | 11% | 4% | -54% | -81% | -82% |
| 2–5 min | 16305 | 87 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 12742 | 41 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 18908 | 46 | 1% | 0% | -65% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3483 | 13 | 5% | 2% | -52% | -88% | -88% |
| SOL | 3476 | 15 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3466 | 11 | 5% | 2% | -60% | -89% | -88% |
| BNB | 3460 | 18 | 5% | 2% | -34% | -86% | -85% |
| DOGE | 3459 | 7 | 4% | 2% | -75% | -90% | -90% |
| ETH | 3452 | 14 | 7% | 3% | -50% | -81% | -81% |
| NEAR | 3431 | 16 | 5% | 2% | -40% | -85% | -85% |
| BTC | 3429 | 16 | 5% | 2% | -36% | -87% | -89% |
| XRP | 3419 | 13 | 3% | 1% | -52% | -89% | -89% |
| GOLD | 1811 | 5 | 6% | 2% | -66% | -81% | -83% |
| WTI | 1781 | 6 | 4% | 1% | -60% | -92% | -92% |
| SILVER | 1762 | 8 | 5% | 2% | -46% | -82% | -82% |
| PLATINUM | 1594 | 4 | 2% | 1% | -77% | -96% | -96% |
| EURUSD | 1530 | 4 | 2% | 1% | -76% | -90% | -89% |
| COPPER | 1496 | 6 | 2% | 1% | -63% | -72% | -72% |
| NATGAS | 1455 | 8 | 2% | 1% | -49% | -77% | -76% |
| GBPUSD | 1449 | 4 | 2% | 1% | -74% | -96% | -96% |
| USDJPY | 1434 | 5 | 2% | 1% | -67% | -97% | -96% |
| PALLADIUM | 1433 | 3 | 1% | 0% | -80% | -92% | -92% |
| AUDUSD | 989 | 5 | 2% | 1% | -53% | -87% | -87% |
| USDCAD | 957 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 553 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 303 | 1 | 4% | 1% | -69% | -62% | -60% |
| 2YRRATE | 287 | 3 | 4% | 1% | -2% | -28% | -27% |
| 30YRRATE | 285 | 0 | 2% | 1% | -100% | -96% | -95% |
| 5YRRATE | 262 | 1 | 4% | 2% | -64% | -93% | -95% |
| INX | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 25619 | 95 | 4% | 2% | -57% | -88% | -87% |
| DOWN (bought NO) | 24844 | 91 | 4% | 2% | -58% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5047 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5322 | 19 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 7999 | 27 | 5% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 9234 | 38 | 6% | 3% | -54% | -87% | -86% |
| Over 0.5% | 3465 | 14 | 7% | 3% | -58% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12238 | 42 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12223 | 54 | 4% | 2% | -50% | -84% | -84% |
| Afternoon (12–6pm) | 12200 | 47 | 4% | 2% | -55% | -86% | -86% |
| Evening (6pm–12am) | 13802 | 43 | 4% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,951 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/9 12:55:52 AM | HYPE | UP | 4.1 min | -0.726% | — | In play | — |
| 11/9 12:55:36 AM | USDCAD | UP | 4.4 min | — | — | In play | — |
| 11/9 12:44:29 AM | USDCAD | UP | 30 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 11/9 12:44:14 AM | HYPE | UP | 45 sec | -0.231% | 0¢ | ❌ Lost | $0.00 |
| 11/9 12:44:14 AM | ZEC | UP | 45 sec | -0.261% | 0¢ | ❌ Lost | $0.00 |
| 11/9 12:44:14 AM | USDJPY | UP | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 12:44:14 AM | NEAR | UP | 45 sec | -0.310% | 0¢ | ❌ Lost | $0.00 |
| 11/9 12:43:56 AM | BRENT | UP | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 12:43:56 AM | AUDUSD | UP | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 12:43:40 AM | PLATINUM | UP | 80 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 12:43:40 AM | GBPUSD | DOWN | 80 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 12:43:40 AM | WTI | UP | 80 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 12:43:24 AM | COPPER | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 12:43:09 AM | BNB | DOWN | 1.8 min | +0.116% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 12:42:51 AM | SILVER | UP | 2.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 12:42:35 AM | ETH | DOWN | 2.4 min | +0.280% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 12:41:48 AM | GOLD | UP | 3.2 min | — | 0¢ | ❌ Lost | $0.00 |
| 11/9 12:41:00 AM | NATGAS | DOWN | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 12:41:00 AM | PALLADIUM | UP | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 12:40:41 AM | EURUSD | DOWN | 4.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 12:39:54 AM | XRP | DOWN | 5.1 min | +0.674% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 12:39:54 AM | BTC | DOWN | 5.1 min | +0.333% | 2¢ | ❌ Lost | -$0.15 |
| 11/9 12:39:54 AM | SOL | DOWN | 5.1 min | +0.566% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 12:39:36 AM | DOGE | DOWN | 5.4 min | +0.589% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 12:29:51 AM | PLATINUM | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 12:29:35 AM | XRP | UP | 24 sec | -0.101% | 0¢ | ❌ Lost | $0.00 |
| 11/9 12:29:35 AM | BTC | UP | 24 sec | -0.112% | 0¢ | ❌ Lost | $0.00 |
| 11/9 12:29:35 AM | ETH | UP | 24 sec | -0.117% | 10¢ | ❌ Lost | -$0.15 |
| 11/9 12:29:35 AM | BNB | UP | 24 sec | -0.224% | 0¢ | ❌ Lost | $0.00 |
| 11/9 12:29:35 AM | DOGE | UP | 24 sec | -0.159% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
