# 15-Minute 1¢ Study

*Updated Wed Oct 14, 8:00 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1384 finished bets | 1% | $29.60 | +19% | +2.14¢ | $37.60 / -$8.00 |

*Expect about **85 buys a day** (~$12.73/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1305 | $13.15 | +9% |
| 5+ min left, hold to the close | 557 | -$26.05 | -32% |
| Volatility model ≥ 5%, sell at 50¢ | 1384 | -$29.40 | -19% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 17904 | 17883 | 66 (0%) | 1.07% | -$1,242.15 (-57%) | Hold to the close: -$1,242.15 (-57%) |

*In play or awaiting result: 20. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 11705 | 4.5% | 0.4% (46) | -681% | ❌ Worse |
| Momentum model | 11705 | 4.4% | 0.4% (46) | -707% | ❌ Worse |
| Mean-reversion model | 11705 | 7.3% | 0.4% (46) | -806% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 11705 | 46 | -51% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2461 | 18 | -15% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 1384 | 13 | +19% | -74% | -72% | -69% |
| Volatility model ≥ 10% | 843 | 9 | +52% | -65% | -63% | -60% |
| Momentum model ≥ 2% | 2153 | 15 | -16% | -80% | -80% | -78% |
| Momentum model ≥ 5% | 1305 | 11 | +9% | -77% | -77% | -74% |
| Momentum model ≥ 10% | 885 | 8 | +27% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 4262 | 27 | -31% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2911 | 20 | -24% | -83% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1916 | 14 | -16% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 11903 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4357 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1623 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 17883 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 66 | 0% | -$1,242.15 | -57% | — |
| Sell at 2¢ | 616 | 3% | -$1,963.99 | -91% | 34 sec |
| Sell at 3¢ | 414 | 2% | -$1,962.69 | -91% | 46 sec |
| Sell at 5¢ | 302 | 2% | -$1,927.85 | -89% | 49 sec |
| Sell at 10¢ | 192 | 1% | -$1,844.63 | -85% | 63 sec |
| Sell at 25¢ | 109 | 1% | -$1,707.36 | -79% | 79 sec |
| Sell at 50¢ | 72 | 0% | -$1,512.15 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 553 | 4 | 10% | 2% | -31% | -83% | -88% |
| 2–5 min | 5745 | 32 | 6% | 3% | -45% | -88% | -88% |
| 1–2 min | 4696 | 18 | 3% | 2% | -58% | -94% | -93% |
| Under 1 min | 6885 | 12 | 1% | 0% | -75% | -92% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1334 | 7 | 4% | 2% | -35% | -90% | -90% |
| HYPE | 1331 | 4 | 4% | 2% | -63% | -90% | -89% |
| ETH | 1327 | 8 | 5% | 3% | -26% | -89% | -88% |
| BNB | 1327 | 5 | 4% | 2% | -54% | -90% | -90% |
| DOGE | 1325 | 2 | 4% | 2% | -81% | -91% | -90% |
| SOL | 1322 | 2 | 3% | 1% | -81% | -93% | -92% |
| BTC | 1313 | 6 | 5% | 2% | -39% | -88% | -91% |
| NEAR | 1312 | 7 | 5% | 2% | -31% | -78% | -78% |
| XRP | 1312 | 7 | 2% | 1% | -34% | -86% | -86% |
| GOLD | 706 | 1 | 4% | 1% | -84% | -91% | -93% |
| SILVER | 694 | 2 | 3% | 1% | -67% | -94% | -94% |
| WTI | 667 | 3 | 3% | 1% | -48% | -94% | -96% |
| COPPER | 618 | 1 | 2% | 1% | -85% | -97% | -96% |
| PLATINUM | 588 | 0 | 1% | 1% | -100% | -99% | -98% |
| PALLADIUM | 544 | 1 | 1% | 0% | -83% | -98% | -98% |
| NATGAS | 540 | 3 | 2% | 2% | -48% | -96% | -95% |
| EURUSD | 521 | 3 | 3% | 2% | -46% | -77% | -77% |
| GBPUSD | 489 | 1 | 2% | 1% | -81% | -96% | -96% |
| USDJPY | 446 | 3 | 1% | 1% | -37% | -98% | -98% |
| AUDUSD | 90 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 77 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8998 | 35 | 3% | 2% | -55% | -90% | -89% |
| DOWN (bought NO) | 8885 | 31 | 3% | 2% | -60% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2074 | 10 | 2% | 1% | -19% | -78% | -78% |
| 0.05–0.1% | 2110 | 6 | 3% | 1% | -59% | -92% | -91% |
| 0.1–0.2% | 3035 | 9 | 4% | 2% | -63% | -91% | -91% |
| 0.2–0.5% | 3371 | 18 | 6% | 3% | -41% | -89% | -88% |
| Over 0.5% | 1310 | 5 | 6% | 2% | -60% | -89% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4717 | 20 | 4% | 2% | -52% | -87% | -88% |
| Morning (6am–12pm) | 4049 | 21 | 4% | 2% | -40% | -91% | -90% |
| Afternoon (12–6pm) | 4113 | 10 | 3% | 1% | -71% | -91% | -91% |
| Evening (6pm–12am) | 5004 | 15 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,499 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/14 7:59:44 AM | USDJPY | DOWN | 16 sec | — | 0¢ | In play | — |
| 10/14 7:58:07 AM | COPPER | UP | 1.9 min | — | 0¢ | In play | — |
| 10/14 7:58:07 AM | EURUSD | UP | 1.9 min | — | 0¢ | In play | — |
| 10/14 7:57:48 AM | PALLADIUM | UP | 2.2 min | — | 0¢ | In play | — |
| 10/14 7:57:32 AM | USDCAD | DOWN | 2.5 min | — | 0¢ | In play | — |
| 10/14 7:57:16 AM | GOLD | UP | 2.7 min | — | 1¢ | In play | — |
| 10/14 7:57:01 AM | AUDUSD | UP | 3.0 min | — | 0¢ | In play | — |
| 10/14 7:57:01 AM | SOL | UP | 3.0 min | -0.647% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 7:57:01 AM | BTC | UP | 3.0 min | -0.311% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 7:56:43 AM | GBPUSD | UP | 3.3 min | — | 0¢ | In play | — |
| 10/14 7:56:11 AM | XRP | UP | 3.8 min | -0.550% | 1¢ | In play | — |
| 10/14 7:56:11 AM | PLATINUM | UP | 3.8 min | — | 0¢ | In play | — |
| 10/14 7:55:56 AM | ETH | UP | 4.0 min | -0.505% | 1¢ | In play | — |
| 10/14 7:55:56 AM | BNB | UP | 4.0 min | -0.405% | 1¢ | In play | — |
| 10/14 7:55:40 AM | DOGE | UP | 4.3 min | -0.710% | 1¢ | In play | — |
| 10/14 7:55:40 AM | HYPE | UP | 4.3 min | -0.660% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 7:55:40 AM | NEAR | UP | 4.3 min | -1.135% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 7:55:24 AM | ZEC | UP | 4.6 min | -1.208% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 7:55:08 AM | SILVER | UP | 4.9 min | — | 1¢ | In play | — |
| 10/14 7:44:58 AM | WTI | UP | 1 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/14 7:44:58 AM | COPPER | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 7:44:58 AM | USDJPY | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 7:44:58 AM | PLATINUM | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 7:44:42 AM | SILVER | DOWN | 17 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/14 7:44:42 AM | USDCAD | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 7:43:54 AM | GBPUSD | UP | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 7:43:22 AM | GOLD | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 7:43:22 AM | AUDUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 7:43:22 AM | NATGAS | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 7:42:19 AM | ZEC | DOWN | 2.7 min | +0.702% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
