# 15-Minute 1¢ Study

*Updated Thu Oct 29, 6:16 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3115 finished bets | 1% | $84.65 | +24% | +2.72¢ | $79.35 / $5.30 |

*Expect about **98 buys a day** (~$14.72/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2884 | $34.10 | +11% |
| Volatility model ≥ 2%, hold to the close | 5763 | -$0.05 | -0% |
| Volatility model ≥ 5%, sell at 50¢ | 3115 | -$69.60 | -20% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 38494 | 38475 | 143 (0%) | 1.07% | -$2,695.25 (-57%) | Hold to the close: -$2,695.25 (-57%) |

*In play or awaiting result: 18. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 23705 | 4.7% | 0.4% (93) | -677% | ❌ Worse |
| Momentum model | 23705 | 4.6% | 0.4% (93) | -701% | ❌ Worse |
| Mean-reversion model | 23705 | 8.0% | 0.4% (93) | -825% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 23705 | 93 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5763 | 50 | -0% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3115 | 31 | +24% | -75% | -74% | -70% |
| Volatility model ≥ 10% | 1758 | 19 | +54% | -68% | -67% | -64% |
| Momentum model ≥ 2% | 4762 | 34 | -14% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2884 | 25 | +11% | -78% | -77% | -73% |
| Momentum model ≥ 10% | 1882 | 17 | +25% | -72% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9697 | 64 | -28% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 6796 | 54 | -12% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4533 | 39 | -2% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 23906 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9246 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5323 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 38475 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 143 | 0% | -$2,695.25 | -57% | — |
| Sell at 2¢ | 1479 | 4% | -$4,116.71 | -88% | 47 sec |
| Sell at 3¢ | 1020 | 3% | -$4,103.45 | -87% | 48 sec |
| Sell at 5¢ | 711 | 2% | -$4,025.10 | -86% | 63 sec |
| Sell at 10¢ | 429 | 1% | -$3,855.26 | -82% | 65 sec |
| Sell at 25¢ | 226 | 1% | -$3,557.19 | -76% | 83 sec |
| Sell at 50¢ | 146 | 0% | -$3,235.75 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 9 | 0 | 33% | 22% | -100% | -42% | -13% |
| 5–10 min | 1779 | 8 | 11% | 4% | -57% | -80% | -81% |
| 2–5 min | 12245 | 68 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 9738 | 34 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 14704 | 33 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2675 | 12 | 5% | 3% | -43% | -88% | -88% |
| HYPE | 2672 | 8 | 5% | 3% | -63% | -89% | -87% |
| BNB | 2669 | 15 | 4% | 2% | -30% | -85% | -84% |
| SOL | 2662 | 7 | 4% | 2% | -67% | -92% | -91% |
| ETH | 2656 | 11 | 6% | 3% | -50% | -86% | -85% |
| DOGE | 2656 | 6 | 4% | 2% | -72% | -90% | -89% |
| BTC | 2639 | 13 | 5% | 2% | -34% | -88% | -89% |
| XRP | 2639 | 11 | 3% | 1% | -49% | -89% | -89% |
| NEAR | 2638 | 12 | 5% | 2% | -41% | -82% | -82% |
| GOLD | 1452 | 5 | 4% | 2% | -59% | -82% | -83% |
| SILVER | 1421 | 7 | 5% | 2% | -42% | -82% | -81% |
| WTI | 1409 | 4 | 3% | 1% | -66% | -93% | -94% |
| PLATINUM | 1255 | 2 | 2% | 1% | -85% | -97% | -96% |
| COPPER | 1199 | 5 | 1% | 1% | -61% | -74% | -74% |
| EURUSD | 1195 | 3 | 2% | 1% | -77% | -88% | -88% |
| NATGAS | 1158 | 7 | 2% | 1% | -44% | -80% | -79% |
| GBPUSD | 1131 | 2 | 2% | 1% | -83% | -96% | -96% |
| PALLADIUM | 1122 | 2 | 1% | 0% | -83% | -90% | -90% |
| USDJPY | 1112 | 5 | 2% | 1% | -58% | -97% | -96% |
| AUDUSD | 666 | 4 | 2% | 1% | -44% | -83% | -82% |
| USDCAD | 627 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 230 | 0 | 0% | 0% | -100% | -99% | -99% |
| 10YRRATE | 158 | 0 | 4% | 1% | -100% | -92% | -90% |
| 30YRRATE | 152 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 146 | 1 | 5% | 1% | -36% | -28% | -27% |
| 5YRRATE | 136 | 1 | 7% | 3% | -31% | -89% | -90% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 19545 | 78 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 18930 | 65 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3879 | 19 | 2% | 1% | -15% | -81% | -81% |
| 0.05–0.1% | 4090 | 14 | 3% | 2% | -49% | -92% | -92% |
| 0.1–0.2% | 6186 | 22 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 7073 | 30 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2674 | 10 | 7% | 3% | -61% | -86% | -86% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9458 | 35 | 4% | 2% | -58% | -86% | -86% |
| Morning (6am–12pm) | 9668 | 43 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 9178 | 31 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 10171 | 34 | 3% | 2% | -62% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,495 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/29 6:14:52 PM | EURUSD | DOWN | 8 sec | — | 0¢ | In play | — |
| 10/29 6:14:36 PM | PALLADIUM | UP | 24 sec | — | 0¢ | In play | — |
| 10/29 6:14:36 PM | XRP | UP | 24 sec | -0.154% | 1¢ | In play | — |
| 10/29 6:14:36 PM | DOGE | UP | 24 sec | -0.085% | 0¢ | ❌ Lost | $0.00 |
| 10/29 6:14:36 PM | GBPUSD | DOWN | 24 sec | — | 0¢ | In play | — |
| 10/29 6:14:36 PM | NEAR | UP | 24 sec | -0.422% | 0¢ | In play | — |
| 10/29 6:14:36 PM | BTC | UP | 24 sec | -0.095% | 1¢ | In play | — |
| 10/29 6:14:20 PM | SOL | UP | 40 sec | -0.218% | 0¢ | In play | — |
| 10/29 6:14:20 PM | AUDUSD | UP | 40 sec | — | 15¢ | In play | — |
| 10/29 6:14:04 PM | ZEC | DOWN | 56 sec | +0.531% | 0¢ | ❌ Lost | -$0.15 |
| 10/29 6:13:32 PM | NATGAS | UP | 88 sec | — | 0¢ | In play | — |
| 10/29 6:13:32 PM | HYPE | DOWN | 88 sec | +0.732% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 6:13:16 PM | ETH | UP | 1.7 min | -0.502% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 6:13:00 PM | BNB | UP | 2.0 min | -0.732% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 6:13:00 PM | WTI | UP | 2.0 min | — | 3¢ | ❌ Lost | -$0.15 |
| 10/29 6:11:56 PM | USDJPY | UP | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 6:09:32 PM | COPPER | UP | 5.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 6:09:16 PM | USDCAD | UP | 5.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 5:59:31 PM | PALLADIUM | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 5:59:31 PM | SILVER | DOWN | 29 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 5:58:45 PM | XRP | UP | 74 sec | -0.267% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 5:58:45 PM | GOLD | UP | 74 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 5:58:45 PM | NEAR | UP | 74 sec | -0.627% | 0¢ | ❌ Lost | -$0.15 |
| 10/29 5:58:45 PM | ETH | UP | 74 sec | -0.316% | 0¢ | ❌ Lost | $0.00 |
| 10/29 5:58:29 PM | WTI | DOWN | 1.5 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/29 5:58:13 PM | ZEC | UP | 1.8 min | -0.599% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 5:57:40 PM | BRENT | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 5:57:24 PM | AUDUSD | DOWN | 2.6 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/29 5:56:53 PM | HYPE | UP | 3.1 min | -0.977% | 2¢ | ❌ Lost | -$0.15 |
| 10/29 5:56:38 PM | DOGE | UP | 3.4 min | -0.504% | 5¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
