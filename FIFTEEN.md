# 15-Minute 1¢ Study

*Updated Sun Nov 1, 8:07 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3457 finished bets | 1% | $131.90 | +34% | +3.82¢ | $74.45 / $57.45 |

*Expect about **99 buys a day** (~$14.88/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3188 | $59.35 | +17% |
| Volatility model ≥ 2%, hold to the close | 6383 | $53.20 | +7% |
| Momentum model ≥ 2%, hold to the close | 5261 | -$34.10 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 41895 | 41885 | 158 (0%) | 1.07% | -$2,885.00 (-57%) | Hold to the close: -$2,885.00 (-57%) |

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
| Volatility model | 26155 | 4.7% | 0.4% (105) | -677% | ❌ Worse |
| Momentum model | 26155 | 4.6% | 0.4% (105) | -698% | ❌ Worse |
| Mean-reversion model | 26155 | 8.1% | 0.4% (105) | -824% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26155 | 105 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6383 | 59 | +7% | -79% | -78% | -73% |
| Volatility model ≥ 5% | 3457 | 37 | +34% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1960 | 22 | +60% | -70% | -68% | -64% |
| Momentum model ≥ 2% | 5261 | 41 | -6% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3188 | 29 | +17% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 2081 | 19 | +28% | -73% | -73% | -68% |
| Mean-reversion model ≥ 2% | 10813 | 75 | -24% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7579 | 64 | -7% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 5070 | 46 | +3% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 26357 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 9791 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5737 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 41885 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 158 | 0% | -$2,885.00 | -57% | — |
| Sell at 2¢ | 1642 | 4% | -$4,446.08 | -87% | 47 sec |
| Sell at 3¢ | 1128 | 3% | -$4,433.08 | -87% | 48 sec |
| Sell at 5¢ | 784 | 2% | -$4,335.40 | -85% | 63 sec |
| Sell at 10¢ | 471 | 1% | -$4,157.99 | -82% | 65 sec |
| Sell at 25¢ | 250 | 1% | -$3,835.50 | -75% | 83 sec |
| Sell at 50¢ | 163 | 0% | -$3,478.75 | -68% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1990 | 9 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 13437 | 75 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 10596 | 37 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 15851 | 37 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2952 | 13 | 5% | 3% | -43% | -88% | -88% |
| SOL | 2943 | 11 | 4% | 2% | -53% | -91% | -90% |
| BNB | 2940 | 17 | 5% | 2% | -28% | -85% | -84% |
| HYPE | 2939 | 9 | 5% | 3% | -62% | -89% | -87% |
| ETH | 2928 | 11 | 6% | 3% | -54% | -85% | -85% |
| DOGE | 2928 | 6 | 4% | 2% | -74% | -90% | -90% |
| BTC | 2910 | 14 | 5% | 2% | -35% | -88% | -89% |
| XRP | 2909 | 11 | 3% | 1% | -53% | -89% | -89% |
| NEAR | 2908 | 15 | 5% | 2% | -33% | -83% | -83% |
| GOLD | 1527 | 5 | 5% | 2% | -60% | -82% | -84% |
| SILVER | 1492 | 7 | 4% | 2% | -44% | -82% | -81% |
| WTI | 1487 | 4 | 3% | 1% | -68% | -93% | -93% |
| PLATINUM | 1322 | 3 | 2% | 1% | -79% | -96% | -96% |
| COPPER | 1262 | 5 | 1% | 1% | -63% | -75% | -75% |
| EURUSD | 1259 | 3 | 2% | 1% | -78% | -89% | -88% |
| NATGAS | 1219 | 7 | 2% | 1% | -46% | -81% | -80% |
| GBPUSD | 1193 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1187 | 2 | 1% | 0% | -84% | -90% | -91% |
| USDJPY | 1182 | 5 | 2% | 1% | -61% | -97% | -96% |
| AUDUSD | 715 | 4 | 2% | 1% | -48% | -84% | -83% |
| USDCAD | 696 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 295 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 188 | 1 | 5% | 2% | -50% | -41% | -39% |
| 30YRRATE | 177 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 170 | 2 | 5% | 1% | +10% | +18% | +19% |
| 5YRRATE | 157 | 1 | 6% | 3% | -41% | -89% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 21260 | 87 | 4% | 2% | -53% | -88% | -87% |
| DOWN (bought NO) | 20625 | 71 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4309 | 21 | 2% | 1% | -16% | -82% | -81% |
| 0.05–0.1% | 4538 | 17 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 6817 | 24 | 4% | 2% | -56% | -90% | -90% |
| 0.2–0.5% | 7763 | 33 | 7% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2925 | 12 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10303 | 36 | 4% | 2% | -60% | -86% | -86% |
| Morning (6am–12pm) | 10513 | 48 | 5% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 9923 | 37 | 4% | 2% | -56% | -87% | -87% |
| Evening (6pm–12am) | 11146 | 37 | 3% | 2% | -62% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,806 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/1 7:59:48 PM | BNB | UP | 11 sec | -0.055% | 0¢ | ❌ Lost | $0.00 |
| 11/1 7:59:48 PM | DOGE | UP | 11 sec | -0.058% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 7:59:48 PM | SOL | DOWN | 11 sec | +0.025% | 0¢ | ❌ Lost | $0.00 |
| 11/1 7:59:48 PM | BTC | UP | 11 sec | -0.021% | 0¢ | ❌ Lost | $0.00 |
| 11/1 7:59:15 PM | BRENT | UP | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 7:59:15 PM | ETH | DOWN | 44 sec | +0.050% | 0¢ | ❌ Lost | $0.00 |
| 11/1 7:59:15 PM | WTI | UP | 44 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/1 7:59:15 PM | AUDUSD | UP | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 7:58:43 PM | USDJPY | UP | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 7:58:43 PM | GBPUSD | DOWN | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 7:58:43 PM | HYPE | UP | 76 sec | -0.098% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 7:58:27 PM | SILVER | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/1 7:58:08 PM | EURUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 7:57:21 PM | USDCAD | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 7:56:47 PM | PLATINUM | UP | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 7:56:31 PM | NATGAS | UP | 3.5 min | — | 4¢ | ❌ Lost | -$0.15 |
| 11/1 7:56:00 PM | GOLD | UP | 4.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/1 7:56:00 PM | XRP | UP | 4.0 min | -0.239% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 7:55:42 PM | NEAR | UP | 4.3 min | -0.590% | 2¢ | ❌ Lost | -$0.15 |
| 11/1 7:55:42 PM | COPPER | UP | 4.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 7:54:36 PM | PALLADIUM | UP | 5.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 7:44:54 PM | WTI | UP | 6 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/1 7:44:38 PM | BRENT | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 7:44:23 PM | BTC | UP | 36 sec | -0.074% | 0¢ | ❌ Lost | $0.00 |
| 11/1 7:44:23 PM | XRP | UP | 36 sec | -0.128% | 0¢ | ❌ Lost | $0.00 |
| 11/1 7:44:04 PM | SILVER | UP | 55 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/1 7:44:04 PM | ZEC | UP | 55 sec | -0.195% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 7:43:48 PM | ETH | UP | 71 sec | -0.114% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 7:43:48 PM | SOL | UP | 71 sec | -0.153% | 0¢ | ❌ Lost | $0.00 |
| 11/1 7:43:32 PM | GOLD | UP | 87 sec | — | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
