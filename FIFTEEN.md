# 15-Minute 1¢ Study

*Updated Tue Oct 27, 10:04 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2856 finished bets | 1% | $69.35 | +21% | +2.43¢ | $80.20 / -$10.85 |

*Expect about **97 buys a day** (~$14.58/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2664 | $42.60 | +15% |
| Volatility model ≥ 2%, hold to the close | 5307 | -$18.75 | -3% |
| Momentum model ≥ 2%, hold to the close | 4410 | -$52.65 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 34798 | 34789 | 130 (0%) | 1.07% | -$2,417.50 (-57%) | Hold to the close: -$2,417.50 (-57%) |

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
| Volatility model | 21985 | 4.6% | 0.4% (87) | -674% | ❌ Worse |
| Momentum model | 21985 | 4.6% | 0.4% (87) | -700% | ❌ Worse |
| Mean-reversion model | 21985 | 8.0% | 0.4% (87) | -820% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21985 | 87 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5307 | 45 | -3% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2856 | 28 | +21% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1620 | 18 | +56% | -67% | -66% | -63% |
| Momentum model ≥ 2% | 4410 | 33 | -10% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2664 | 24 | +15% | -78% | -77% | -73% |
| Momentum model ≥ 10% | 1741 | 16 | +27% | -72% | -71% | -67% |
| Mean-reversion model ≥ 2% | 8924 | 58 | -29% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6246 | 48 | -15% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4165 | 34 | -8% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 22185 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8217 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4387 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 34789 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 130 | 0% | -$2,417.50 | -57% | — |
| Sell at 2¢ | 1313 | 4% | -$3,714.12 | -88% | 47 sec |
| Sell at 3¢ | 894 | 3% | -$3,706.84 | -87% | 48 sec |
| Sell at 5¢ | 618 | 2% | -$3,653.80 | -86% | 62 sec |
| Sell at 10¢ | 382 | 1% | -$3,499.08 | -83% | 65 sec |
| Sell at 25¢ | 206 | 1% | -$3,233.64 | -76% | 1.5 min |
| Sell at 50¢ | 136 | 0% | -$2,913.50 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1548 | 8 | 11% | 4% | -51% | -81% | -82% |
| 2–5 min | 11155 | 61 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 8821 | 31 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 13261 | 30 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2484 | 12 | 5% | 2% | -38% | -89% | -89% |
| HYPE | 2476 | 8 | 5% | 3% | -60% | -88% | -86% |
| BNB | 2475 | 14 | 5% | 2% | -29% | -84% | -83% |
| SOL | 2472 | 6 | 4% | 2% | -70% | -92% | -92% |
| ETH | 2466 | 11 | 6% | 3% | -46% | -86% | -85% |
| DOGE | 2461 | 5 | 4% | 2% | -75% | -90% | -90% |
| NEAR | 2454 | 12 | 5% | 2% | -37% | -82% | -82% |
| XRP | 2451 | 9 | 3% | 1% | -55% | -89% | -89% |
| BTC | 2446 | 12 | 5% | 2% | -34% | -88% | -89% |
| GOLD | 1309 | 5 | 4% | 2% | -54% | -81% | -83% |
| SILVER | 1278 | 6 | 4% | 2% | -45% | -82% | -82% |
| WTI | 1259 | 4 | 3% | 1% | -62% | -93% | -94% |
| PLATINUM | 1131 | 1 | 2% | 1% | -92% | -97% | -97% |
| COPPER | 1084 | 4 | 1% | 1% | -66% | -72% | -72% |
| EURUSD | 1054 | 3 | 2% | 1% | -73% | -87% | -87% |
| NATGAS | 1043 | 6 | 2% | 1% | -46% | -79% | -78% |
| PALLADIUM | 999 | 2 | 1% | 0% | -81% | -89% | -89% |
| GBPUSD | 992 | 1 | 2% | 1% | -91% | -96% | -97% |
| USDJPY | 981 | 5 | 1% | 1% | -52% | -98% | -97% |
| AUDUSD | 539 | 2 | 1% | 1% | -65% | -98% | -97% |
| USDCAD | 499 | 0 | 1% | 0% | -100% | -98% | -98% |
| BRENT | 114 | 0 | 1% | 1% | -100% | -98% | -98% |
| 10YRRATE | 89 | 0 | 4% | 0% | -100% | -92% | -91% |
| 30YRRATE | 79 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 77 | 1 | 4% | 1% | +21% | +28% | +28% |
| 5YRRATE | 77 | 1 | 5% | 3% | +21% | -91% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17607 | 71 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 17182 | 59 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3643 | 18 | 2% | 1% | -16% | -81% | -80% |
| 0.05–0.1% | 3794 | 12 | 3% | 2% | -53% | -92% | -92% |
| 0.1–0.2% | 5755 | 20 | 5% | 2% | -57% | -90% | -89% |
| 0.2–0.5% | 6547 | 29 | 6% | 3% | -51% | -87% | -86% |
| Over 0.5% | 2442 | 10 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8784 | 34 | 4% | 2% | -56% | -86% | -86% |
| Morning (6am–12pm) | 8587 | 40 | 4% | 2% | -47% | -87% | -86% |
| Afternoon (12–6pm) | 8019 | 25 | 4% | 2% | -63% | -88% | -88% |
| Evening (6pm–12am) | 9399 | 31 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,650 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/27 9:59:44 AM | 5YRRATE | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 9:59:44 AM | 2YRRATE | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 9:59:44 AM | ZEC | DOWN | 15 sec | -0.052% | 0¢ | In play | — |
| 10/27 9:59:44 AM | 10YRRATE | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 9:59:44 AM | USDJPY | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 9:59:28 AM | GOLD | DOWN | 31 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 9:59:28 AM | 30YRRATE | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 9:59:28 AM | BNB | DOWN | 31 sec | +0.021% | 0¢ | ❌ Lost | $0.00 |
| 10/27 9:59:12 AM | HYPE | UP | 47 sec | -0.110% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 9:59:12 AM | BTC | UP | 47 sec | -0.082% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 9:58:56 AM | ETH | UP | 63 sec | -0.096% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 9:58:56 AM | SOL | UP | 63 sec | -0.108% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 9:58:41 AM | DOGE | UP | 78 sec | -0.157% | 0¢ | ❌ Lost | $0.00 |
| 10/27 9:58:09 AM | XRP | UP | 1.8 min | -0.197% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 9:58:09 AM | PLATINUM | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 9:58:09 AM | NEAR | UP | 1.8 min | -0.608% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 9:57:53 AM | BRENT | DOWN | 2.1 min | — | 20¢ | ❌ Lost | -$0.15 |
| 10/27 9:57:22 AM | NATGAS | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 9:56:34 AM | WTI | DOWN | 3.4 min | — | 92¢ | ✅ Won | $13.85 |
| 10/27 9:44:57 AM | SILVER | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 9:44:57 AM | NATGAS | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 9:44:57 AM | EURUSD | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 9:44:57 AM | SOL | DOWN | 2 sec | +0.001% | 0¢ | ❌ Lost | $0.00 |
| 10/27 9:44:57 AM | 30YRRATE | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 9:44:41 AM | DOGE | UP | 18 sec | -0.059% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 9:44:41 AM | AUDUSD | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 9:44:41 AM | GOLD | DOWN | 18 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/27 9:44:41 AM | XRP | UP | 18 sec | -0.114% | 0¢ | ❌ Lost | $0.00 |
| 10/27 9:44:25 AM | USDJPY | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 9:44:09 AM | HYPE | DOWN | 50 sec | +0.087% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
