# 15-Minute 1¢ Study

*Updated Mon Nov 9, 12:25 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4071 finished bets | 1% | $191.45 | +42% | +4.70¢ | $93.70 / $97.75 |

*Expect about **97 buys a day** (~$14.53/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3777 | $109.25 | +27% |
| Volatility model ≥ 2%, hold to the close | 7451 | $83.30 | +9% |
| Momentum model ≥ 2%, hold to the close | 6151 | $7.35 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 50437 | 50420 | 186 (0%) | 1.07% | -$3,529.95 (-58%) | Hold to the close: -$3,529.95 (-58%) |

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
| Volatility model | 30853 | 4.8% | 0.4% (121) | -692% | ❌ Worse |
| Momentum model | 30853 | 4.6% | 0.4% (121) | -718% | ❌ Worse |
| Mean-reversion model | 30853 | 8.1% | 0.4% (121) | -836% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 30853 | 121 | -50% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7451 | 70 | +9% | -76% | -75% | -71% |
| Volatility model ≥ 5% | 4071 | 46 | +42% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2343 | 28 | +71% | -61% | -59% | -55% |
| Momentum model ≥ 2% | 6151 | 51 | +1% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3777 | 37 | +27% | -73% | -72% | -68% |
| Momentum model ≥ 10% | 2477 | 25 | +42% | -64% | -64% | -59% |
| Mean-reversion model ≥ 2% | 12750 | 89 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 8939 | 77 | -4% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 5977 | 56 | +7% | -76% | -76% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31058 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11869 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7493 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 50420 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 186 | 0% | -$3,529.95 | -58% | — |
| Sell at 2¢ | 1985 | 4% | -$5,337.85 | -87% | 47 sec |
| Sell at 3¢ | 1348 | 3% | -$5,328.23 | -87% | 48 sec |
| Sell at 5¢ | 942 | 2% | -$5,213.65 | -85% | 62 sec |
| Sell at 10¢ | 566 | 1% | -$5,000.49 | -82% | 65 sec |
| Sell at 25¢ | 296 | 1% | -$4,650.19 | -76% | 83 sec |
| Sell at 50¢ | 190 | 0% | -$4,249.45 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2492 | 12 | 11% | 4% | -54% | -81% | -82% |
| 2–5 min | 16293 | 87 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 12728 | 41 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 18895 | 46 | 1% | 0% | -65% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3481 | 13 | 5% | 2% | -52% | -88% | -88% |
| SOL | 3474 | 15 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3464 | 11 | 5% | 2% | -60% | -89% | -88% |
| BNB | 3458 | 18 | 5% | 2% | -34% | -86% | -85% |
| DOGE | 3457 | 7 | 4% | 2% | -75% | -90% | -90% |
| ETH | 3450 | 14 | 7% | 3% | -50% | -81% | -81% |
| NEAR | 3430 | 16 | 5% | 2% | -40% | -85% | -85% |
| BTC | 3427 | 16 | 5% | 2% | -36% | -87% | -89% |
| XRP | 3417 | 13 | 3% | 1% | -52% | -89% | -89% |
| GOLD | 1809 | 5 | 6% | 2% | -66% | -81% | -83% |
| WTI | 1779 | 6 | 4% | 1% | -59% | -92% | -92% |
| SILVER | 1760 | 8 | 5% | 2% | -46% | -82% | -82% |
| PLATINUM | 1592 | 4 | 2% | 1% | -77% | -96% | -96% |
| EURUSD | 1528 | 4 | 2% | 1% | -76% | -90% | -89% |
| COPPER | 1494 | 6 | 2% | 1% | -63% | -72% | -72% |
| NATGAS | 1453 | 8 | 2% | 1% | -49% | -77% | -76% |
| GBPUSD | 1447 | 4 | 2% | 1% | -74% | -96% | -96% |
| USDJPY | 1432 | 5 | 2% | 1% | -67% | -97% | -96% |
| PALLADIUM | 1431 | 3 | 1% | 0% | -80% | -92% | -92% |
| AUDUSD | 987 | 5 | 2% | 1% | -53% | -87% | -87% |
| USDCAD | 955 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 551 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 303 | 1 | 4% | 1% | -69% | -62% | -60% |
| 2YRRATE | 287 | 3 | 4% | 1% | -2% | -28% | -27% |
| 30YRRATE | 285 | 0 | 2% | 1% | -100% | -96% | -95% |
| 5YRRATE | 262 | 1 | 4% | 2% | -64% | -93% | -95% |
| INX | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 25590 | 95 | 4% | 2% | -57% | -88% | -87% |
| DOWN (bought NO) | 24830 | 91 | 4% | 2% | -58% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5047 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5322 | 19 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 7993 | 27 | 5% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 9227 | 38 | 6% | 3% | -54% | -87% | -86% |
| Over 0.5% | 3461 | 14 | 7% | 3% | -58% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12195 | 42 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12223 | 54 | 4% | 2% | -50% | -84% | -84% |
| Afternoon (12–6pm) | 12200 | 47 | 4% | 2% | -55% | -86% | -86% |
| Evening (6pm–12am) | 13802 | 43 | 4% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,952 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/9 12:13:56 AM | AUDUSD | UP | 64 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 11/9 12:13:56 AM | GOLD | UP | 64 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 12:13:24 AM | ZEC | UP | 1.6 min | -0.522% | 0¢ | ❌ Lost | -$0.15 |
| 11/9 12:13:09 AM | BRENT | DOWN | 1.9 min | — | 2¢ | ❌ Lost | -$0.15 |
| 11/9 12:13:09 AM | WTI | DOWN | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 12:12:36 AM | PALLADIUM | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 12:12:20 AM | PLATINUM | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 12:12:20 AM | XRP | UP | 2.6 min | -0.513% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 12:12:20 AM | SILVER | UP | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 12:12:04 AM | BTC | UP | 2.9 min | -0.291% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 12:12:04 AM | ETH | UP | 2.9 min | -0.493% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 12:11:47 AM | SOL | UP | 3.2 min | -0.508% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 12:11:47 AM | DOGE | UP | 3.2 min | -0.412% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 12:11:31 AM | NEAR | UP | 3.5 min | -0.860% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 12:10:59 AM | HYPE | UP | 4.0 min | -0.655% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 12:09:54 AM | BNB | UP | 5.1 min | -0.331% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 11:59:44 PM | COPPER | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 11:59:44 PM | AUDUSD | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 11:59:28 PM | SOL | DOWN | 32 sec | +0.101% | 0¢ | ❌ Lost | $0.00 |
| 11/8 11:58:23 PM | BRENT | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 11:58:23 PM | PLATINUM | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 11:58:23 PM | GOLD | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/8 11:58:08 PM | WTI | DOWN | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/8 11:57:36 PM | ZEC | UP | 2.4 min | -0.456% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 11:57:36 PM | PALLADIUM | UP | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/8 11:57:36 PM | NEAR | UP | 2.4 min | -0.535% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 11:57:20 PM | USDJPY | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 11:56:48 PM | NATGAS | UP | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 11:56:16 PM | ETH | DOWN | 3.7 min | +0.367% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 11:55:46 PM | BNB | DOWN | 4.2 min | +0.188% | 3¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
