# 15-Minute 1¢ Study

*Updated Fri Oct 30, 3:14 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3158 finished bets | 1% | $80.90 | +23% | +2.56¢ | $76.80 / $4.10 |

*Expect about **98 buys a day** (~$14.75/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2920 | $30.80 | +10% |
| Volatility model ≥ 2%, hold to the close | 5842 | -$8.30 | -1% |
| Volatility model ≥ 5%, sell at 50¢ | 3158 | -$73.35 | -21% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 39138 | 39112 | 144 (0%) | 1.07% | -$2,760.45 (-58%) | Hold to the close: -$2,760.45 (-58%) |

*In play or awaiting result: 25. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 24010 | 4.7% | 0.4% (93) | -684% | ❌ Worse |
| Momentum model | 24010 | 4.5% | 0.4% (93) | -707% | ❌ Worse |
| Mean-reversion model | 24010 | 8.0% | 0.4% (93) | -834% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 24010 | 93 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5842 | 50 | -1% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 3158 | 31 | +23% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1781 | 19 | +52% | -68% | -67% | -64% |
| Momentum model ≥ 2% | 4817 | 34 | -15% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2920 | 25 | +10% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1904 | 17 | +24% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9853 | 64 | -29% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 6903 | 54 | -13% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4597 | 39 | -4% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 24211 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9447 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5454 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 39112 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 144 | 0% | -$2,760.45 | -58% | — |
| Sell at 2¢ | 1503 | 4% | -$4,189.67 | -88% | 47 sec |
| Sell at 3¢ | 1037 | 3% | -$4,176.02 | -87% | 49 sec |
| Sell at 5¢ | 723 | 2% | -$4,096.50 | -86% | 63 sec |
| Sell at 10¢ | 437 | 1% | -$3,923.98 | -82% | 65 sec |
| Sell at 25¢ | 227 | 1% | -$3,633.08 | -76% | 83 sec |
| Sell at 50¢ | 147 | 0% | -$3,308.20 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 9 | 0 | 33% | 22% | -100% | -42% | -13% |
| 5–10 min | 1824 | 8 | 11% | 4% | -58% | -80% | -81% |
| 2–5 min | 12467 | 69 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 9894 | 34 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 14918 | 33 | 1% | 0% | -69% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2708 | 12 | 5% | 3% | -43% | -88% | -88% |
| HYPE | 2705 | 8 | 5% | 3% | -63% | -89% | -87% |
| BNB | 2702 | 15 | 5% | 3% | -30% | -85% | -83% |
| SOL | 2697 | 7 | 4% | 2% | -67% | -91% | -91% |
| ETH | 2690 | 11 | 6% | 3% | -50% | -86% | -85% |
| DOGE | 2690 | 6 | 4% | 2% | -72% | -90% | -89% |
| BTC | 2674 | 13 | 5% | 2% | -35% | -88% | -89% |
| XRP | 2673 | 11 | 3% | 1% | -49% | -89% | -89% |
| NEAR | 2672 | 12 | 5% | 2% | -42% | -83% | -83% |
| GOLD | 1484 | 5 | 4% | 2% | -59% | -82% | -84% |
| SILVER | 1449 | 7 | 4% | 2% | -43% | -82% | -81% |
| WTI | 1432 | 4 | 3% | 1% | -67% | -93% | -93% |
| PLATINUM | 1283 | 3 | 2% | 1% | -78% | -96% | -96% |
| EURUSD | 1222 | 3 | 2% | 1% | -77% | -88% | -88% |
| COPPER | 1221 | 5 | 1% | 1% | -62% | -75% | -74% |
| NATGAS | 1178 | 7 | 2% | 1% | -45% | -80% | -80% |
| GBPUSD | 1155 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1150 | 2 | 1% | 0% | -84% | -90% | -90% |
| USDJPY | 1141 | 5 | 2% | 1% | -59% | -97% | -96% |
| AUDUSD | 686 | 4 | 2% | 1% | -46% | -84% | -83% |
| USDCAD | 652 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 250 | 0 | 0% | 0% | -100% | -99% | -99% |
| 10YRRATE | 159 | 0 | 4% | 1% | -100% | -92% | -90% |
| 30YRRATE | 155 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 148 | 1 | 5% | 1% | -37% | -29% | -28% |
| 5YRRATE | 136 | 1 | 7% | 3% | -31% | -89% | -90% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 19850 | 79 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 19262 | 65 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3898 | 19 | 2% | 1% | -16% | -81% | -81% |
| 0.05–0.1% | 4123 | 14 | 3% | 2% | -49% | -92% | -92% |
| 0.1–0.2% | 6233 | 22 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 7191 | 30 | 6% | 3% | -54% | -87% | -86% |
| Over 0.5% | 2762 | 10 | 7% | 3% | -63% | -86% | -86% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9686 | 36 | 4% | 2% | -58% | -86% | -86% |
| Morning (6am–12pm) | 9668 | 43 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 9178 | 31 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 10580 | 34 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,490 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/30 3:14:41 AM | WTI | UP | 18 sec | — | — | In play | — |
| 10/30 3:14:25 AM | NATGAS | UP | 34 sec | — | — | In play | — |
| 10/30 3:14:25 AM | ZEC | UP | 34 sec | -0.122% | — | In play | — |
| 10/30 3:14:09 AM | GBPUSD | DOWN | 51 sec | — | — | In play | — |
| 10/30 3:14:09 AM | HYPE | UP | 51 sec | -0.240% | — | In play | — |
| 10/30 3:13:50 AM | SOL | UP | 69 sec | -0.240% | — | In play | — |
| 10/30 3:13:50 AM | NEAR | UP | 69 sec | -0.503% | — | In play | — |
| 10/30 3:13:50 AM | DOGE | UP | 69 sec | -0.131% | — | In play | — |
| 10/30 3:13:34 AM | SILVER | UP | 85 sec | — | — | In play | — |
| 10/30 3:13:34 AM | USDJPY | DOWN | 85 sec | — | — | In play | — |
| 10/30 3:13:04 AM | BRENT | UP | 1.9 min | — | — | In play | — |
| 10/30 3:12:46 AM | BNB | UP | 2.2 min | -0.248% | — | In play | — |
| 10/30 3:12:30 AM | XRP | DOWN | 2.5 min | +0.327% | — | In play | — |
| 10/30 3:11:59 AM | ETH | UP | 3.0 min | -0.266% | — | In play | — |
| 10/30 3:11:42 AM | BTC | UP | 3.3 min | -0.293% | — | In play | — |
| 10/30 3:10:54 AM | GOLD | UP | 4.1 min | — | — | In play | — |
| 10/30 2:59:44 AM | GBPUSD | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 2:59:44 AM | EURUSD | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 2:59:44 AM | ZEC | UP | 16 sec | -0.094% | 0¢ | ❌ Lost | $0.00 |
| 10/30 2:59:28 AM | USDCAD | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 2:59:28 AM | USDJPY | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 2:59:28 AM | BNB | UP | 32 sec | -0.082% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 2:59:12 AM | 30YRRATE | UP | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 2:59:12 AM | BTC | DOWN | 48 sec | +0.037% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 2:59:12 AM | WTI | UP | 48 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/30 2:59:12 AM | DOGE | DOWN | 48 sec | +0.049% | 0¢ | ❌ Lost | $0.00 |
| 10/30 2:58:57 AM | BRENT | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 2:58:57 AM | COPPER | DOWN | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 2:58:25 AM | XRP | DOWN | 1.6 min | +0.104% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 2:58:25 AM | NATGAS | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
