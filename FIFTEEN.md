# 15-Minute 1¢ Study

*Updated Sun Nov 1, 5:53 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3451 finished bets | 1% | $132.65 | +34% | +3.84¢ | $74.45 / $58.20 |

*Expect about **99 buys a day** (~$14.89/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3185 | $59.65 | +17% |
| Volatility model ≥ 2%, hold to the close | 6369 | $55.00 | +7% |
| Momentum model ≥ 2%, hold to the close | 5251 | -$32.90 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 41740 | 41730 | 158 (0%) | 1.07% | -$2,866.85 (-56%) | Hold to the close: -$2,866.85 (-56%) |

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
| Volatility model | 26077 | 4.7% | 0.4% (105) | -677% | ❌ Worse |
| Momentum model | 26077 | 4.6% | 0.4% (105) | -699% | ❌ Worse |
| Mean-reversion model | 26077 | 8.1% | 0.4% (105) | -824% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26077 | 105 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6369 | 59 | +7% | -79% | -78% | -73% |
| Volatility model ≥ 5% | 3451 | 37 | +34% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1957 | 22 | +61% | -70% | -68% | -64% |
| Momentum model ≥ 2% | 5251 | 41 | -5% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3185 | 29 | +17% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 2079 | 19 | +28% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 10775 | 75 | -24% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7553 | 64 | -6% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 5053 | 46 | +3% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 26279 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 9740 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5711 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 41730 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 158 | 0% | -$2,866.85 | -56% | — |
| Sell at 2¢ | 1639 | 4% | -$4,428.71 | -87% | 47 sec |
| Sell at 3¢ | 1127 | 3% | -$4,415.32 | -87% | 48 sec |
| Sell at 5¢ | 784 | 2% | -$4,317.25 | -85% | 63 sec |
| Sell at 10¢ | 471 | 1% | -$4,139.84 | -82% | 65 sec |
| Sell at 25¢ | 250 | 1% | -$3,817.35 | -75% | 83 sec |
| Sell at 50¢ | 163 | 0% | -$3,460.60 | -68% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1978 | 9 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 13392 | 75 | 7% | 4% | -45% | -87% | -86% |
| 1–2 min | 10549 | 37 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 15800 | 37 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2944 | 13 | 5% | 3% | -43% | -88% | -87% |
| SOL | 2934 | 11 | 4% | 2% | -53% | -91% | -90% |
| BNB | 2931 | 17 | 5% | 2% | -27% | -85% | -84% |
| HYPE | 2930 | 9 | 5% | 3% | -62% | -89% | -87% |
| ETH | 2919 | 11 | 6% | 3% | -54% | -85% | -85% |
| DOGE | 2919 | 6 | 4% | 2% | -74% | -90% | -90% |
| BTC | 2902 | 14 | 5% | 2% | -35% | -87% | -89% |
| NEAR | 2900 | 15 | 5% | 2% | -33% | -83% | -83% |
| XRP | 2900 | 11 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1520 | 5 | 5% | 2% | -60% | -82% | -83% |
| SILVER | 1485 | 7 | 5% | 2% | -44% | -82% | -81% |
| WTI | 1479 | 4 | 3% | 1% | -67% | -93% | -93% |
| PLATINUM | 1317 | 3 | 2% | 1% | -79% | -96% | -96% |
| COPPER | 1256 | 5 | 1% | 1% | -63% | -75% | -75% |
| EURUSD | 1254 | 3 | 2% | 1% | -78% | -89% | -88% |
| NATGAS | 1215 | 7 | 2% | 1% | -46% | -81% | -80% |
| GBPUSD | 1189 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1181 | 2 | 1% | 0% | -84% | -90% | -91% |
| USDJPY | 1175 | 5 | 2% | 1% | -60% | -97% | -96% |
| AUDUSD | 711 | 4 | 2% | 1% | -47% | -84% | -83% |
| USDCAD | 690 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 287 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 188 | 1 | 5% | 2% | -50% | -41% | -39% |
| 30YRRATE | 177 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 170 | 2 | 5% | 1% | +10% | +18% | +19% |
| 5YRRATE | 157 | 1 | 6% | 3% | -41% | -89% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 21177 | 87 | 4% | 2% | -53% | -87% | -87% |
| DOWN (bought NO) | 20553 | 71 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4300 | 21 | 2% | 1% | -15% | -82% | -81% |
| 0.05–0.1% | 4521 | 17 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 6798 | 24 | 4% | 2% | -56% | -90% | -90% |
| 0.2–0.5% | 7742 | 33 | 7% | 3% | -53% | -86% | -86% |
| Over 0.5% | 2913 | 12 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10303 | 36 | 4% | 2% | -60% | -86% | -86% |
| Morning (6am–12pm) | 10513 | 48 | 5% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 9908 | 37 | 4% | 2% | -56% | -87% | -87% |
| Evening (6pm–12am) | 11006 | 37 | 3% | 2% | -61% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,802 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/1 5:44:50 PM | BNB | DOWN | 10 sec | -0.035% | 0¢ | ❌ Lost | $0.00 |
| 11/1 5:44:50 PM | PALLADIUM | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 5:44:34 PM | XRP | DOWN | 26 sec | +0.040% | 0¢ | ❌ Lost | $0.00 |
| 11/1 5:44:18 PM | HYPE | DOWN | 42 sec | +0.110% | 0¢ | ❌ Lost | $0.00 |
| 11/1 5:43:47 PM | SILVER | UP | 73 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/1 5:43:31 PM | BTC | UP | 89 sec | -0.099% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 5:43:15 PM | GBPUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 5:43:15 PM | AUDUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 5:43:15 PM | USDCAD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 5:43:15 PM | PLATINUM | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 5:42:50 PM | GOLD | UP | 2.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/1 5:41:46 PM | COPPER | UP | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 5:40:40 PM | SOL | UP | 4.3 min | -0.350% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 5:40:40 PM | ETH | UP | 4.3 min | -0.249% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 5:40:40 PM | NEAR | UP | 4.3 min | -0.664% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 5:40:21 PM | ZEC | UP | 4.7 min | -0.620% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 5:40:21 PM | DOGE | UP | 4.7 min | -0.318% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 5:25:11 PM | XRP | UP | 4.8 min | -0.377% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 5:25:11 PM | NEAR | UP | 4.8 min | -0.643% | 100¢ | ✅ Won | $13.85 |
| 11/1 5:25:11 PM | ZEC | UP | 4.8 min | -0.777% | 3¢ | ❌ Lost | -$0.15 |
| 11/1 5:23:56 PM | SOL | UP | 6.0 min | -0.525% | 7¢ | ❌ Lost | -$0.15 |
| 11/1 5:23:40 PM | BNB | UP | 6.3 min | -0.294% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 5:14:45 PM | COPPER | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 5:14:45 PM | ZEC | UP | 15 sec | -0.080% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 5:14:13 PM | DOGE | UP | 47 sec | -0.115% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 5:13:57 PM | SILVER | DOWN | 62 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/1 5:13:41 PM | GOLD | DOWN | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 5:13:25 PM | BNB | UP | 1.6 min | -0.143% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 5:13:25 PM | ETH | UP | 1.6 min | -0.158% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 5:13:25 PM | NEAR | UP | 1.6 min | -0.359% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
