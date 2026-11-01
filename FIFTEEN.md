# 15-Minute 1¢ Study

*Updated Sun Nov 1, 6:26 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3396 finished bets | 1% | $110.80 | +29% | +3.26¢ | $77.45 / $33.35 |

*Expect about **99 buys a day** (~$14.86/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3134 | $51.05 | +15% |
| Volatility model ≥ 2%, hold to the close | 6264 | $25.75 | +3% |
| Momentum model ≥ 2%, hold to the close | 5163 | -$50.55 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 41285 | 41274 | 153 (0%) | 1.07% | -$2,882.55 (-57%) | Hold to the close: -$2,882.55 (-57%) |

*In play or awaiting result: 10. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 25673 | 4.7% | 0.4% (100) | -696% | ❌ Worse |
| Momentum model | 25673 | 4.6% | 0.4% (100) | -719% | ❌ Worse |
| Mean-reversion model | 25673 | 8.1% | 0.4% (100) | -846% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 25673 | 100 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6264 | 56 | +3% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 3396 | 35 | +29% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1925 | 21 | +56% | -70% | -68% | -64% |
| Momentum model ≥ 2% | 5163 | 39 | -8% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3134 | 28 | +15% | -79% | -78% | -73% |
| Momentum model ≥ 10% | 2049 | 19 | +29% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 10595 | 71 | -27% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7425 | 61 | -9% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4969 | 43 | -2% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 25875 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9712 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5687 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 41274 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 153 | 0% | -$2,882.55 | -57% | — |
| Sell at 2¢ | 1606 | 4% | -$4,382.99 | -87% | 47 sec |
| Sell at 3¢ | 1104 | 3% | -$4,369.99 | -87% | 48 sec |
| Sell at 5¢ | 765 | 2% | -$4,289.30 | -85% | 63 sec |
| Sell at 10¢ | 459 | 1% | -$4,115.26 | -82% | 65 sec |
| Sell at 25¢ | 240 | 1% | -$3,810.15 | -76% | 82 sec |
| Sell at 50¢ | 157 | 0% | -$3,460.80 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1947 | 9 | 11% | 4% | -56% | -80% | -82% |
| 2–5 min | 13204 | 72 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10450 | 35 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 15662 | 37 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2898 | 13 | 5% | 3% | -42% | -88% | -88% |
| SOL | 2886 | 9 | 4% | 2% | -61% | -91% | -91% |
| HYPE | 2886 | 8 | 5% | 2% | -66% | -89% | -87% |
| BNB | 2885 | 17 | 5% | 2% | -26% | -85% | -84% |
| DOGE | 2876 | 6 | 4% | 2% | -74% | -90% | -90% |
| ETH | 2875 | 11 | 7% | 3% | -53% | -85% | -85% |
| NEAR | 2857 | 14 | 5% | 2% | -36% | -83% | -83% |
| BTC | 2857 | 13 | 5% | 2% | -39% | -88% | -89% |
| XRP | 2855 | 11 | 3% | 1% | -52% | -89% | -89% |
| GOLD | 1515 | 5 | 5% | 2% | -60% | -82% | -83% |
| SILVER | 1481 | 7 | 4% | 2% | -44% | -82% | -81% |
| WTI | 1476 | 4 | 3% | 1% | -67% | -93% | -93% |
| PLATINUM | 1314 | 3 | 2% | 1% | -79% | -96% | -96% |
| COPPER | 1253 | 5 | 1% | 1% | -63% | -75% | -75% |
| EURUSD | 1249 | 3 | 2% | 1% | -78% | -89% | -88% |
| NATGAS | 1212 | 7 | 2% | 1% | -46% | -81% | -80% |
| GBPUSD | 1185 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1178 | 2 | 1% | 0% | -84% | -90% | -91% |
| USDJPY | 1171 | 5 | 2% | 1% | -60% | -97% | -96% |
| AUDUSD | 705 | 4 | 2% | 1% | -47% | -84% | -83% |
| USDCAD | 685 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 283 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 188 | 1 | 5% | 2% | -50% | -41% | -39% |
| 30YRRATE | 177 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 170 | 2 | 5% | 1% | +10% | +18% | +19% |
| 5YRRATE | 157 | 1 | 6% | 3% | -41% | -89% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 20940 | 83 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 20334 | 70 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4206 | 21 | 2% | 1% | -14% | -82% | -81% |
| 0.05–0.1% | 4451 | 15 | 3% | 2% | -49% | -92% | -91% |
| 0.1–0.2% | 6685 | 22 | 4% | 2% | -59% | -90% | -90% |
| 0.2–0.5% | 7639 | 33 | 7% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2889 | 11 | 7% | 3% | -61% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10303 | 36 | 4% | 2% | -60% | -86% | -86% |
| Morning (6am–12pm) | 10310 | 46 | 4% | 2% | -49% | -85% | -84% |
| Afternoon (12–6pm) | 9655 | 34 | 4% | 2% | -59% | -87% | -87% |
| Evening (6pm–12am) | 11006 | 37 | 3% | 2% | -61% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,709 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/1 6:25:46 AM | ZEC | DOWN | 4.2 min | +0.384% | — | In play | — |
| 11/1 4:27:45 AM | SOL | UP | 2.2 min | -0.072% | 6¢ | ❌ Lost | -$0.15 |
| 11/1 4:27:45 AM | NEAR | DOWN | 2.2 min | +0.215% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 4:27:29 AM | DOGE | UP | 2.5 min | -0.096% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 4:26:33 AM | ETH | UP | 3.4 min | -0.077% | 10¢ | ❌ Lost | -$0.15 |
| 11/1 4:14:29 AM | NEAR | UP | 30 sec | +0.009% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 4:14:29 AM | ETH | DOWN | 30 sec | +0.010% | 0¢ | ❌ Lost | $0.00 |
| 11/1 4:14:13 AM | SOL | UP | 46 sec | -0.036% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 4:14:13 AM | ZEC | UP | 46 sec | -0.155% | 0¢ | ❌ Lost | $0.00 |
| 11/1 4:13:41 AM | BTC | UP | 79 sec | -0.060% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 4:13:41 AM | HYPE | UP | 79 sec | -0.153% | 0¢ | ❌ Lost | $0.00 |
| 11/1 4:12:06 AM | BNB | DOWN | 2.9 min | +0.180% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 4:11:50 AM | XRP | UP | 3.2 min | -0.080% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 4:11:34 AM | DOGE | DOWN | 3.4 min | +0.087% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 3:59:45 AM | BTC | UP | 14 sec | -0.028% | 0¢ | ❌ Lost | $0.00 |
| 11/1 3:59:29 AM | XRP | UP | 30 sec | -0.016% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 3:59:29 AM | SOL | DOWN | 30 sec | +0.023% | 0¢ | ❌ Lost | $0.00 |
| 11/1 3:59:29 AM | ETH | UP | 30 sec | -0.041% | 0¢ | ❌ Lost | $0.00 |
| 11/1 3:59:13 AM | ZEC | DOWN | 47 sec | +0.088% | 0¢ | ❌ Lost | $0.00 |
| 11/1 3:58:55 AM | DOGE | DOWN | 65 sec | -0.005% | 0¢ | ❌ Lost | $0.00 |
| 11/1 3:57:33 AM | BNB | UP | 2.4 min | -0.129% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 3:56:14 AM | HYPE | UP | 3.8 min | -0.192% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 3:54:39 AM | NEAR | UP | 5.3 min | -0.637% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 3:44:22 AM | HYPE | DOWN | 37 sec | +0.039% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 3:44:06 AM | BNB | DOWN | 54 sec | +0.102% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 3:43:34 AM | ZEC | UP | 85 sec | -0.122% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 3:43:34 AM | XRP | UP | 85 sec | -0.064% | 0¢ | ❌ Lost | $0.00 |
| 11/1 3:41:45 AM | ETH | UP | 3.2 min | -0.095% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 3:41:09 AM | DOGE | UP | 3.9 min | -0.132% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 3:40:38 AM | NEAR | UP | 4.3 min | -0.451% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
