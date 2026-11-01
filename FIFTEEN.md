# 15-Minute 1¢ Study

*Updated Sun Nov 1, 4:35 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3445 finished bets | 1% | $132.95 | +35% | +3.86¢ | $74.90 / $58.05 |

*Expect about **99 buys a day** (~$14.89/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3181 | $59.80 | +17% |
| Volatility model ≥ 2%, hold to the close | 6360 | $55.75 | +7% |
| Momentum model ≥ 2%, hold to the close | 5245 | -$32.60 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 41660 | 41650 | 157 (0%) | 1.07% | -$2,870.35 (-57%) | Hold to the close: -$2,870.35 (-57%) |

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
| Volatility model | 26036 | 4.7% | 0.4% (104) | -680% | ❌ Worse |
| Momentum model | 26036 | 4.6% | 0.4% (104) | -702% | ❌ Worse |
| Mean-reversion model | 26036 | 8.1% | 0.4% (104) | -828% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26036 | 104 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6360 | 59 | +7% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3445 | 37 | +35% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1954 | 22 | +61% | -70% | -68% | -64% |
| Momentum model ≥ 2% | 5245 | 41 | -5% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3181 | 29 | +17% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 2076 | 19 | +28% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 10749 | 74 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7531 | 64 | -6% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 5041 | 46 | +4% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 26238 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9717 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5695 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 41650 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 157 | 0% | -$2,870.35 | -57% | — |
| Sell at 2¢ | 1633 | 4% | -$4,419.77 | -87% | 47 sec |
| Sell at 3¢ | 1123 | 3% | -$4,406.38 | -87% | 48 sec |
| Sell at 5¢ | 781 | 2% | -$4,308.70 | -85% | 63 sec |
| Sell at 10¢ | 470 | 1% | -$4,130.65 | -81% | 65 sec |
| Sell at 25¢ | 249 | 1% | -$3,810.16 | -75% | 83 sec |
| Sell at 50¢ | 162 | 0% | -$3,456.85 | -68% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1966 | 9 | 11% | 4% | -56% | -80% | -82% |
| 2–5 min | 13365 | 74 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 10531 | 37 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 15777 | 37 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2939 | 13 | 5% | 3% | -43% | -88% | -87% |
| SOL | 2929 | 11 | 4% | 2% | -53% | -91% | -91% |
| HYPE | 2926 | 9 | 5% | 2% | -62% | -89% | -87% |
| BNB | 2926 | 17 | 5% | 2% | -27% | -85% | -84% |
| ETH | 2915 | 11 | 6% | 3% | -54% | -85% | -85% |
| DOGE | 2915 | 6 | 4% | 2% | -74% | -90% | -90% |
| BTC | 2898 | 14 | 5% | 2% | -35% | -87% | -89% |
| NEAR | 2895 | 14 | 5% | 2% | -37% | -83% | -83% |
| XRP | 2895 | 11 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1516 | 5 | 5% | 2% | -60% | -82% | -83% |
| SILVER | 1482 | 7 | 5% | 2% | -44% | -82% | -81% |
| WTI | 1477 | 4 | 3% | 1% | -67% | -93% | -93% |
| PLATINUM | 1314 | 3 | 2% | 1% | -79% | -96% | -96% |
| COPPER | 1253 | 5 | 1% | 1% | -63% | -75% | -75% |
| EURUSD | 1251 | 3 | 2% | 1% | -78% | -89% | -88% |
| NATGAS | 1212 | 7 | 2% | 1% | -46% | -81% | -80% |
| GBPUSD | 1185 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1178 | 2 | 1% | 0% | -84% | -90% | -91% |
| USDJPY | 1172 | 5 | 2% | 1% | -60% | -97% | -96% |
| AUDUSD | 708 | 4 | 2% | 1% | -47% | -84% | -83% |
| USDCAD | 687 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 285 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 188 | 1 | 5% | 2% | -50% | -41% | -39% |
| 30YRRATE | 177 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 170 | 2 | 5% | 1% | +10% | +18% | +19% |
| 5YRRATE | 157 | 1 | 6% | 3% | -41% | -89% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 21138 | 86 | 4% | 2% | -53% | -88% | -87% |
| DOWN (bought NO) | 20512 | 71 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4293 | 21 | 2% | 1% | -15% | -82% | -81% |
| 0.05–0.1% | 4517 | 17 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 6791 | 24 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 7727 | 33 | 7% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2905 | 11 | 7% | 3% | -61% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10303 | 36 | 4% | 2% | -60% | -86% | -86% |
| Morning (6am–12pm) | 10513 | 48 | 5% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 9828 | 36 | 4% | 2% | -57% | -87% | -87% |
| Evening (6pm–12am) | 11006 | 37 | 3% | 2% | -61% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,799 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/1 4:29:59 PM | EURUSD | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 4:29:27 PM | AUDUSD | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 4:28:55 PM | SILVER | DOWN | 65 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 11/1 4:28:55 PM | XRP | UP | 65 sec | -0.104% | 0¢ | ❌ Lost | $0.00 |
| 11/1 4:28:55 PM | WTI | DOWN | 65 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/1 4:28:55 PM | BTC | UP | 65 sec | -0.106% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 4:28:39 PM | ZEC | UP | 81 sec | -0.213% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 4:28:25 PM | BRENT | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 4:28:09 PM | HYPE | UP | 1.9 min | -0.188% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 4:27:53 PM | USDCAD | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 4:27:53 PM | SOL | UP | 2.1 min | -0.181% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 4:27:53 PM | NEAR | UP | 2.1 min | -0.430% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 4:27:25 PM | DOGE | UP | 2.6 min | -0.208% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 4:27:09 PM | BNB | DOWN | 2.8 min | +0.143% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 4:26:53 PM | GOLD | DOWN | 3.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/1 4:26:53 PM | ETH | UP | 3.1 min | -0.203% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 4:14:32 PM | BRENT | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 4:12:25 PM | EURUSD | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 4:12:25 PM | AUDUSD | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 4:11:37 PM | XRP | DOWN | 3.4 min | +0.289% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 4:11:37 PM | SOL | DOWN | 3.4 min | +0.354% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 4:11:37 PM | NEAR | DOWN | 3.4 min | +0.576% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 4:11:21 PM | HYPE | DOWN | 3.6 min | +0.385% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 4:11:05 PM | BNB | DOWN | 3.9 min | +0.189% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 4:11:05 PM | ZEC | DOWN | 3.9 min | +0.517% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 4:10:49 PM | ETH | DOWN | 4.2 min | +0.356% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 4:10:49 PM | BTC | DOWN | 4.2 min | +0.291% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 4:10:33 PM | USDJPY | DOWN | 4.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 4:09:32 PM | DOGE | DOWN | 5.5 min | +0.496% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 3:59:55 PM | AUDUSD | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
