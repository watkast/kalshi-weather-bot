# 15-Minute 1¢ Study

*Updated Mon Oct 26, 5:30 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2782 finished bets | 1% | $77.30 | +25% | +2.78¢ | $28.70 / $48.60 |

*Expect about **97 buys a day** (~$14.54/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2587 | $50.85 | +18% |
| Volatility model ≥ 2%, hold to the close | 5175 | -$17.00 | -3% |
| Momentum model ≥ 2%, hold to the close | 4302 | -$41.10 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 33552 | 33529 | 124 (0%) | 1.07% | -$2,339.80 (-57%) | Hold to the close: -$2,339.80 (-57%) |

*In play or awaiting result: 22. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 21413 | 4.6% | 0.4% (86) | -665% | ❌ Worse |
| Momentum model | 21413 | 4.5% | 0.4% (86) | -689% | ❌ Worse |
| Mean-reversion model | 21413 | 7.9% | 0.4% (86) | -807% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21413 | 86 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 5175 | 44 | -3% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2782 | 28 | +25% | -75% | -74% | -70% |
| Volatility model ≥ 10% | 1576 | 18 | +60% | -67% | -65% | -62% |
| Momentum model ≥ 2% | 4302 | 33 | -8% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2587 | 24 | +18% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1687 | 16 | +30% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 8664 | 57 | -28% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 6068 | 47 | -15% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4042 | 33 | -8% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21613 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7847 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4069 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 33529 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 124 | 0% | -$2,339.80 | -57% | — |
| Sell at 2¢ | 1264 | 4% | -$3,579.16 | -88% | 47 sec |
| Sell at 3¢ | 864 | 3% | -$3,570.84 | -88% | 48 sec |
| Sell at 5¢ | 600 | 2% | -$3,517.80 | -86% | 61 sec |
| Sell at 10¢ | 371 | 1% | -$3,379.79 | -83% | 65 sec |
| Sell at 25¢ | 197 | 1% | -$3,129.73 | -77% | 82 sec |
| Sell at 50¢ | 127 | 0% | -$2,840.55 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1469 | 8 | 11% | 4% | -48% | -80% | -82% |
| 2–5 min | 10742 | 57 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 8487 | 31 | 3% | 1% | -60% | -92% | -92% |
| Under 1 min | 12827 | 28 | 1% | 0% | -69% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2421 | 12 | 5% | 2% | -37% | -88% | -88% |
| HYPE | 2415 | 8 | 5% | 3% | -59% | -88% | -86% |
| BNB | 2411 | 13 | 5% | 2% | -33% | -84% | -83% |
| SOL | 2408 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2401 | 11 | 6% | 3% | -45% | -86% | -85% |
| DOGE | 2395 | 5 | 4% | 2% | -74% | -91% | -90% |
| XRP | 2390 | 9 | 3% | 1% | -54% | -89% | -89% |
| NEAR | 2389 | 12 | 5% | 2% | -35% | -82% | -82% |
| BTC | 2383 | 12 | 5% | 2% | -32% | -88% | -89% |
| GOLD | 1260 | 4 | 4% | 2% | -62% | -81% | -83% |
| SILVER | 1227 | 6 | 4% | 2% | -43% | -82% | -81% |
| WTI | 1207 | 3 | 3% | 1% | -70% | -94% | -95% |
| PLATINUM | 1071 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 1043 | 4 | 1% | 1% | -64% | -71% | -71% |
| EURUSD | 1008 | 3 | 2% | 1% | -72% | -87% | -87% |
| NATGAS | 1003 | 5 | 2% | 1% | -53% | -87% | -87% |
| PALLADIUM | 961 | 2 | 1% | 0% | -81% | -88% | -89% |
| GBPUSD | 949 | 1 | 2% | 1% | -90% | -96% | -96% |
| USDJPY | 934 | 5 | 1% | 1% | -50% | -98% | -97% |
| AUDUSD | 494 | 1 | 1% | 1% | -81% | -98% | -97% |
| USDCAD | 457 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 75 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 63 | 0 | 3% | 0% | -100% | -94% | -96% |
| 2YRRATE | 57 | 1 | 4% | 0% | +64% | +70% | +68% |
| 30YRRATE | 57 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 50 | 1 | 4% | 4% | +87% | -93% | -90% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17010 | 68 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 16519 | 56 | 4% | 2% | -61% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3572 | 18 | 2% | 1% | -15% | -81% | -80% |
| 0.05–0.1% | 3700 | 12 | 3% | 2% | -52% | -92% | -92% |
| 0.1–0.2% | 5597 | 20 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 6345 | 28 | 6% | 3% | -51% | -87% | -86% |
| Over 0.5% | 2395 | 10 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8317 | 33 | 4% | 2% | -55% | -85% | -85% |
| Morning (6am–12pm) | 8268 | 37 | 4% | 2% | -49% | -88% | -88% |
| Afternoon (12–6pm) | 7970 | 25 | 4% | 2% | -63% | -88% | -88% |
| Evening (6pm–12am) | 8974 | 29 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,723 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/26 5:29:41 PM | GBPUSD | DOWN | 19 sec | — | 0¢ | In play | — |
| 10/26 5:29:41 PM | NATGAS | UP | 19 sec | — | 1¢ | In play | — |
| 10/26 5:29:41 PM | USDCAD | UP | 19 sec | — | 0¢ | In play | — |
| 10/26 5:29:09 PM | COPPER | DOWN | 51 sec | — | 0¢ | In play | — |
| 10/26 5:28:37 PM | USDJPY | DOWN | 83 sec | — | 0¢ | In play | — |
| 10/26 5:28:37 PM | WTI | DOWN | 83 sec | — | 0¢ | In play | — |
| 10/26 5:28:21 PM | BRENT | DOWN | 1.6 min | — | 0¢ | In play | — |
| 10/26 5:27:33 PM | BNB | DOWN | 2.5 min | +0.042% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:27:33 PM | HYPE | DOWN | 2.5 min | +0.260% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:27:33 PM | GOLD | DOWN | 2.5 min | — | 1¢ | In play | — |
| 10/26 5:27:17 PM | NEAR | DOWN | 2.7 min | +0.516% | 1¢ | In play | — |
| 10/26 5:27:01 PM | ZEC | DOWN | 3.0 min | +0.460% | 0¢ | In play | — |
| 10/26 5:26:46 PM | SILVER | DOWN | 3.2 min | — | 0¢ | In play | — |
| 10/26 5:26:30 PM | AUDUSD | DOWN | 3.5 min | — | 0¢ | In play | — |
| 10/26 5:26:30 PM | SOL | DOWN | 3.5 min | +0.270% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:25:42 PM | BTC | DOWN | 4.3 min | +0.151% | 1¢ | In play | — |
| 10/26 5:25:42 PM | XRP | DOWN | 4.3 min | +0.256% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:25:10 PM | DOGE | DOWN | 4.8 min | +0.239% | 1¢ | In play | — |
| 10/26 5:25:10 PM | ETH | DOWN | 4.8 min | +0.212% | 1¢ | In play | — |
| 10/26 5:14:53 PM | BRENT | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:14:53 PM | AUDUSD | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:14:53 PM | NEAR | DOWN | 7 sec | -0.074% | 0¢ | ❌ Lost | $0.00 |
| 10/26 5:14:21 PM | COPPER | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:14:05 PM | NATGAS | DOWN | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:13:34 PM | EURUSD | UP | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:13:34 PM | GBPUSD | UP | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 5:13:34 PM | SOL | UP | 85 sec | -0.157% | 0¢ | ❌ Lost | $0.00 |
| 10/26 5:13:02 PM | SILVER | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:13:02 PM | ZEC | UP | 1.9 min | -0.349% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 5:13:02 PM | GOLD | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
