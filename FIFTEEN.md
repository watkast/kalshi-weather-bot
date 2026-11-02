# 15-Minute 1¢ Study

*Updated Sun Nov 1, 10:52 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3467 finished bets | 1% | $130.55 | +34% | +3.77¢ | $73.85 / $56.70 |

*Expect about **99 buys a day** (~$14.87/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3198 | $57.85 | +17% |
| Volatility model ≥ 2%, hold to the close | 6403 | $50.50 | +7% |
| Momentum model ≥ 2%, hold to the close | 5276 | -$36.35 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 42083 | 42073 | 158 (0%) | 1.07% | -$2,907.50 (-57%) | Hold to the close: -$2,907.50 (-57%) |

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
| Volatility model | 26249 | 4.7% | 0.4% (105) | -676% | ❌ Worse |
| Momentum model | 26249 | 4.6% | 0.4% (105) | -698% | ❌ Worse |
| Mean-reversion model | 26249 | 8.1% | 0.4% (105) | -824% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26249 | 105 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6403 | 59 | +7% | -79% | -78% | -73% |
| Volatility model ≥ 5% | 3467 | 37 | +34% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1965 | 22 | +60% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 5276 | 41 | -6% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3198 | 29 | +17% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2088 | 19 | +27% | -74% | -73% | -68% |
| Mean-reversion model ≥ 2% | 10844 | 75 | -24% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7605 | 64 | -7% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 5088 | 46 | +3% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 26451 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9852 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5770 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 42073 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 158 | 0% | -$2,907.50 | -57% | — |
| Sell at 2¢ | 1649 | 4% | -$4,466.76 | -87% | 47 sec |
| Sell at 3¢ | 1132 | 3% | -$4,454.02 | -87% | 48 sec |
| Sell at 5¢ | 787 | 2% | -$4,355.95 | -85% | 63 sec |
| Sell at 10¢ | 474 | 1% | -$4,176.56 | -82% | 65 sec |
| Sell at 25¢ | 250 | 1% | -$3,858.00 | -75% | 83 sec |
| Sell at 50¢ | 163 | 0% | -$3,501.25 | -68% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2000 | 9 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 13500 | 75 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 10639 | 37 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 15923 | 37 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2963 | 13 | 5% | 3% | -44% | -88% | -87% |
| SOL | 2954 | 11 | 4% | 2% | -53% | -91% | -90% |
| BNB | 2951 | 17 | 5% | 2% | -28% | -85% | -84% |
| HYPE | 2950 | 9 | 5% | 3% | -62% | -89% | -87% |
| DOGE | 2938 | 6 | 4% | 2% | -74% | -90% | -90% |
| ETH | 2937 | 11 | 6% | 3% | -54% | -85% | -85% |
| BTC | 2921 | 14 | 5% | 2% | -35% | -87% | -89% |
| NEAR | 2919 | 15 | 5% | 2% | -33% | -83% | -83% |
| XRP | 2918 | 11 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1537 | 5 | 5% | 2% | -61% | -82% | -84% |
| SILVER | 1498 | 7 | 5% | 2% | -44% | -82% | -81% |
| WTI | 1495 | 4 | 3% | 1% | -68% | -93% | -93% |
| PLATINUM | 1331 | 3 | 2% | 1% | -79% | -96% | -96% |
| COPPER | 1269 | 5 | 1% | 1% | -63% | -75% | -75% |
| EURUSD | 1267 | 3 | 2% | 1% | -78% | -89% | -89% |
| NATGAS | 1226 | 7 | 2% | 1% | -47% | -81% | -80% |
| GBPUSD | 1199 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1194 | 2 | 1% | 0% | -84% | -90% | -91% |
| USDJPY | 1190 | 5 | 2% | 1% | -61% | -97% | -96% |
| AUDUSD | 722 | 4 | 2% | 1% | -48% | -84% | -83% |
| USDCAD | 700 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 302 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 188 | 1 | 5% | 2% | -50% | -41% | -39% |
| 30YRRATE | 177 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 170 | 2 | 5% | 1% | +10% | +18% | +19% |
| 5YRRATE | 157 | 1 | 6% | 3% | -41% | -89% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 21343 | 87 | 4% | 2% | -53% | -88% | -87% |
| DOWN (bought NO) | 20730 | 71 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4320 | 21 | 2% | 1% | -16% | -82% | -81% |
| 0.05–0.1% | 4552 | 17 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 6848 | 24 | 4% | 2% | -56% | -90% | -90% |
| 0.2–0.5% | 7795 | 33 | 7% | 3% | -53% | -86% | -86% |
| Over 0.5% | 2931 | 12 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10303 | 36 | 4% | 2% | -60% | -86% | -86% |
| Morning (6am–12pm) | 10513 | 48 | 5% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 9923 | 37 | 4% | 2% | -56% | -87% | -87% |
| Evening (6pm–12am) | 11334 | 37 | 3% | 2% | -62% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,811 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/1 10:44:17 PM | NEAR | DOWN | 43 sec | +0.045% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 10:43:46 PM | BRENT | UP | 73 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 10:43:30 PM | WTI | UP | 89 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/1 10:43:30 PM | SILVER | DOWN | 89 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/1 10:43:30 PM | HYPE | DOWN | 89 sec | +0.107% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 10:43:14 PM | BTC | DOWN | 1.8 min | +0.077% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 10:43:14 PM | BNB | DOWN | 1.8 min | +0.035% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 10:43:14 PM | ZEC | DOWN | 1.8 min | +0.354% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 10:42:58 PM | SOL | DOWN | 2.0 min | +0.178% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 10:42:42 PM | PLATINUM | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 10:42:26 PM | DOGE | DOWN | 2.5 min | +0.215% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 10:42:06 PM | NATGAS | DOWN | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 10:42:06 PM | XRP | DOWN | 2.9 min | +0.136% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 10:42:06 PM | GOLD | DOWN | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/1 10:41:47 PM | ETH | DOWN | 3.2 min | +0.151% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 10:41:31 PM | USDJPY | DOWN | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 10:41:00 PM | PALLADIUM | DOWN | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 10:39:35 PM | COPPER | DOWN | 5.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 10:29:34 PM | USDJPY | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 10:29:34 PM | SILVER | DOWN | 26 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/1 10:29:34 PM | SOL | DOWN | 26 sec | +0.094% | 0¢ | ❌ Lost | $0.00 |
| 11/1 10:29:34 PM | GOLD | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 10:29:34 PM | DOGE | DOWN | 26 sec | +0.018% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 10:29:34 PM | PALLADIUM | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 10:29:17 PM | USDCAD | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 10:29:17 PM | ZEC | DOWN | 42 sec | +0.163% | 0¢ | ❌ Lost | $0.00 |
| 11/1 10:29:01 PM | HYPE | UP | 58 sec | -0.071% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 10:29:01 PM | BTC | DOWN | 58 sec | +0.050% | 0¢ | ❌ Lost | $0.00 |
| 11/1 10:29:01 PM | NEAR | DOWN | 58 sec | +0.141% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 10:28:45 PM | AUDUSD | UP | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
