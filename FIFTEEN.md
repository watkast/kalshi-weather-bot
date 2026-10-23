# 15-Minute 1¢ Study

*Updated Fri Oct 23, 2:37 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2482 finished bets | 1% | $97.05 | +35% | +3.91¢ | $46.25 / $50.80 |

*Expect about **97 buys a day** (~$14.55/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2298 | $53.60 | +21% |
| Volatility model ≥ 2%, hold to the close | 4610 | $9.25 | +2% |
| Momentum model ≥ 2%, hold to the close | 3841 | -$17.80 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 30273 | 30265 | 116 (0%) | 1.07% | -$2,071.55 (-56%) | Hold to the close: -$2,071.55 (-56%) |

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
| Volatility model | 19108 | 4.6% | 0.4% (82) | -633% | ❌ Worse |
| Momentum model | 19108 | 4.5% | 0.4% (82) | -658% | ❌ Worse |
| Mean-reversion model | 19108 | 7.9% | 0.4% (82) | -764% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 19108 | 82 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4610 | 41 | +2% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2482 | 27 | +35% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 1412 | 17 | +70% | -64% | -62% | -59% |
| Momentum model ≥ 2% | 3841 | 31 | -4% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2298 | 22 | +21% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1506 | 15 | +37% | -69% | -68% | -63% |
| Mean-reversion model ≥ 2% | 7674 | 54 | -23% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5356 | 45 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3562 | 32 | +2% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 19308 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 7314 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3643 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 30265 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 116 | 0% | -$2,071.55 | -56% | — |
| Sell at 2¢ | 1130 | 4% | -$3,247.75 | -88% | 47 sec |
| Sell at 3¢ | 774 | 3% | -$3,239.69 | -88% | 48 sec |
| Sell at 5¢ | 542 | 2% | -$3,189.25 | -86% | 61 sec |
| Sell at 10¢ | 331 | 1% | -$3,065.94 | -83% | 64 sec |
| Sell at 25¢ | 184 | 1% | -$2,820.51 | -76% | 82 sec |
| Sell at 50¢ | 118 | 0% | -$2,549.05 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1275 | 7 | 11% | 4% | -48% | -80% | -82% |
| 2–5 min | 9697 | 53 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 7716 | 28 | 3% | 1% | -61% | -93% | -93% |
| Under 1 min | 11573 | 28 | 1% | 0% | -66% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2164 | 12 | 5% | 2% | -30% | -89% | -89% |
| BNB | 2157 | 12 | 5% | 3% | -31% | -83% | -82% |
| HYPE | 2154 | 8 | 5% | 3% | -54% | -88% | -86% |
| SOL | 2147 | 5 | 4% | 2% | -71% | -92% | -92% |
| ETH | 2146 | 10 | 6% | 3% | -44% | -86% | -85% |
| DOGE | 2141 | 4 | 4% | 2% | -77% | -90% | -89% |
| XRP | 2136 | 9 | 3% | 1% | -48% | -88% | -88% |
| NEAR | 2132 | 12 | 5% | 3% | -27% | -81% | -81% |
| BTC | 2131 | 12 | 5% | 2% | -25% | -88% | -89% |
| GOLD | 1188 | 4 | 4% | 2% | -60% | -81% | -83% |
| SILVER | 1154 | 5 | 4% | 1% | -50% | -82% | -82% |
| WTI | 1125 | 3 | 3% | 1% | -69% | -94% | -95% |
| PLATINUM | 1009 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 986 | 4 | 1% | 1% | -62% | -69% | -69% |
| EURUSD | 937 | 3 | 2% | 1% | -70% | -86% | -86% |
| NATGAS | 927 | 5 | 2% | 1% | -50% | -86% | -86% |
| PALLADIUM | 897 | 2 | 1% | 0% | -79% | -88% | -88% |
| GBPUSD | 882 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 864 | 5 | 1% | 1% | -46% | -98% | -97% |
| AUDUSD | 428 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 386 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 41 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 39 | 0 | 3% | 0% | -100% | -96% | -100% |
| 30YRRATE | 38 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 28 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 28 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 15282 | 64 | 4% | 2% | -52% | -87% | -86% |
| DOWN (bought NO) | 14983 | 52 | 4% | 2% | -60% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3170 | 17 | 2% | 1% | -10% | -79% | -78% |
| 0.05–0.1% | 3315 | 11 | 3% | 2% | -51% | -92% | -91% |
| 0.1–0.2% | 4988 | 18 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 5663 | 28 | 6% | 3% | -46% | -87% | -86% |
| Over 0.5% | 2168 | 10 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7532 | 31 | 4% | 2% | -53% | -84% | -84% |
| Morning (6am–12pm) | 7425 | 34 | 4% | 2% | -48% | -88% | -87% |
| Afternoon (12–6pm) | 7146 | 23 | 4% | 2% | -62% | -89% | -89% |
| Evening (6pm–12am) | 8162 | 28 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,581 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/23 2:29:51 PM | SILVER | DOWN | 8 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/23 2:29:51 PM | 30YRRATE | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 2:29:51 PM | AUDUSD | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 2:29:51 PM | SOL | DOWN | 8 sec | +0.047% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 2:29:35 PM | HYPE | DOWN | 24 sec | +0.057% | 0¢ | ❌ Lost | $0.00 |
| 10/23 2:29:35 PM | GBPUSD | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 2:29:19 PM | 5YRRATE | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 2:29:19 PM | XRP | DOWN | 40 sec | +0.061% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 2:29:19 PM | GOLD | DOWN | 40 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/23 2:29:19 PM | USDJPY | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 2:29:02 PM | ETH | DOWN | 57 sec | +0.041% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 2:29:02 PM | BTC | DOWN | 57 sec | +0.059% | 0¢ | ❌ Lost | $0.00 |
| 10/23 2:29:02 PM | 10YRRATE | UP | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 2:29:02 PM | NEAR | DOWN | 57 sec | +0.301% | 0¢ | ❌ Lost | $0.00 |
| 10/23 2:27:40 PM | USDCAD | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 2:26:54 PM | BNB | UP | 3.1 min | -0.237% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 2:26:54 PM | WTI | UP | 3.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/23 2:26:54 PM | DOGE | UP | 3.1 min | -0.259% | 14¢ | ❌ Lost | -$0.15 |
| 10/23 2:26:54 PM | SOL | UP | 3.1 min | -0.195% | 99¢ | ✅ Won | $13.85 |
| 10/23 2:25:32 PM | ZEC | UP | 4.5 min | -0.657% | 1¢ | ❌ Lost | $0.00 |
| 10/23 2:14:52 PM | BRENT | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 2:14:52 PM | NATGAS | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 2:14:36 PM | EURUSD | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 2:14:36 PM | COPPER | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 2:14:36 PM | PLATINUM | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 2:14:20 PM | ZEC | DOWN | 40 sec | +0.118% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 2:14:20 PM | USDCAD | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 2:14:05 PM | SOL | DOWN | 55 sec | +0.075% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 2:14:05 PM | HYPE | DOWN | 55 sec | +0.134% | 0¢ | ❌ Lost | $0.00 |
| 10/23 2:13:49 PM | SILVER | UP | 70 sec | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
