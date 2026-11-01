# 15-Minute 1¢ Study

*Updated Sun Nov 1, 3:15 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3385 finished bets | 1% | $112.00 | +30% | +3.31¢ | $78.20 / $33.80 |

*Expect about **99 buys a day** (~$14.87/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3127 | $51.80 | +15% |
| Volatility model ≥ 2%, hold to the close | 6246 | $27.70 | +4% |
| Momentum model ≥ 2%, hold to the close | 5149 | -$48.90 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 41245 | 41232 | 153 (0%) | 1.07% | -$2,878.35 (-57%) | Hold to the close: -$2,878.35 (-57%) |

*In play or awaiting result: 12. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 25631 | 4.7% | 0.4% (100) | -696% | ❌ Worse |
| Momentum model | 25631 | 4.6% | 0.4% (100) | -719% | ❌ Worse |
| Mean-reversion model | 25631 | 8.1% | 0.4% (100) | -846% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 25631 | 100 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6246 | 56 | +4% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3385 | 35 | +30% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1919 | 21 | +57% | -70% | -68% | -64% |
| Momentum model ≥ 2% | 5149 | 39 | -8% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3127 | 28 | +15% | -78% | -78% | -73% |
| Momentum model ≥ 10% | 2043 | 19 | +30% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 10569 | 71 | -26% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7407 | 61 | -9% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4954 | 43 | -1% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 25833 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9712 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5687 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 41232 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 153 | 0% | -$2,878.35 | -57% | — |
| Sell at 2¢ | 1604 | 4% | -$4,379.31 | -87% | 47 sec |
| Sell at 3¢ | 1102 | 3% | -$4,366.57 | -87% | 48 sec |
| Sell at 5¢ | 763 | 2% | -$4,286.40 | -85% | 63 sec |
| Sell at 10¢ | 458 | 1% | -$4,112.37 | -82% | 65 sec |
| Sell at 25¢ | 240 | 1% | -$3,805.95 | -76% | 82 sec |
| Sell at 50¢ | 157 | 0% | -$3,456.60 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1944 | 9 | 11% | 4% | -56% | -80% | -82% |
| 2–5 min | 13190 | 72 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10439 | 35 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 15648 | 37 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2894 | 13 | 5% | 3% | -42% | -88% | -88% |
| SOL | 2881 | 9 | 4% | 2% | -61% | -91% | -91% |
| HYPE | 2881 | 8 | 5% | 2% | -66% | -89% | -87% |
| BNB | 2881 | 17 | 5% | 2% | -26% | -85% | -84% |
| DOGE | 2872 | 6 | 4% | 2% | -74% | -90% | -90% |
| ETH | 2869 | 11 | 6% | 3% | -53% | -85% | -85% |
| NEAR | 2852 | 14 | 5% | 2% | -36% | -83% | -83% |
| BTC | 2852 | 13 | 5% | 2% | -39% | -88% | -89% |
| XRP | 2851 | 11 | 3% | 1% | -52% | -89% | -89% |
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
| UP (bought YES) | 20915 | 83 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 20317 | 70 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4193 | 21 | 2% | 1% | -13% | -82% | -81% |
| 0.05–0.1% | 4438 | 15 | 3% | 2% | -49% | -92% | -91% |
| 0.1–0.2% | 6675 | 22 | 4% | 2% | -59% | -90% | -90% |
| 0.2–0.5% | 7634 | 33 | 7% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2888 | 11 | 7% | 3% | -61% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10261 | 36 | 4% | 2% | -60% | -86% | -86% |
| Morning (6am–12pm) | 10310 | 46 | 4% | 2% | -49% | -85% | -84% |
| Afternoon (12–6pm) | 9655 | 34 | 4% | 2% | -59% | -87% | -87% |
| Evening (6pm–12am) | 11006 | 37 | 3% | 2% | -61% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,696 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/1 3:14:27 AM | NEAR | DOWN | 33 sec | -0.034% | 0¢ | ❌ Lost | $0.00 |
| 11/1 3:14:13 AM | ZEC | UP | 47 sec | -0.094% | 0¢ | ❌ Lost | $0.00 |
| 11/1 3:13:58 AM | HYPE | DOWN | 61 sec | +0.093% | 1¢ | In play | — |
| 11/1 3:13:58 AM | BTC | DOWN | 61 sec | +0.029% | 0¢ | In play | — |
| 11/1 3:13:58 AM | SOL | DOWN | 61 sec | +0.062% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 3:13:02 AM | ETH | DOWN | 2.0 min | +0.077% | 0¢ | In play | — |
| 11/1 3:12:41 AM | BNB | DOWN | 2.3 min | +0.189% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 3:10:39 AM | DOGE | DOWN | 4.3 min | +0.219% | 2¢ | ❌ Lost | -$0.15 |
| 11/1 3:09:12 AM | XRP | DOWN | 5.8 min | +0.224% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 2:59:53 AM | HYPE | DOWN | 7 sec | +0.101% | 0¢ | ❌ Lost | $0.00 |
| 11/1 2:59:37 AM | SOL | DOWN | 23 sec | +0.012% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 2:59:21 AM | ETH | UP | 39 sec | -0.025% | 0¢ | ❌ Lost | $0.00 |
| 11/1 2:58:42 AM | XRP | DOWN | 78 sec | +0.080% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 2:58:04 AM | BNB | DOWN | 1.9 min | +0.099% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 2:57:06 AM | BTC | DOWN | 2.9 min | +0.062% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 2:56:52 AM | ZEC | DOWN | 3.1 min | +0.228% | 4¢ | ❌ Lost | -$0.15 |
| 11/1 2:56:36 AM | DOGE | DOWN | 3.4 min | +0.081% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 2:56:36 AM | NEAR | DOWN | 3.4 min | +0.262% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 2:44:07 AM | DOGE | UP | 53 sec | -0.069% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 2:44:07 AM | BNB | DOWN | 53 sec | +0.054% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 2:43:35 AM | ETH | DOWN | 84 sec | +0.064% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 2:43:19 AM | XRP | DOWN | 1.7 min | +0.104% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 2:42:45 AM | BTC | DOWN | 2.2 min | +0.068% | 2¢ | ❌ Lost | -$0.15 |
| 11/1 2:42:29 AM | ZEC | DOWN | 2.5 min | +0.304% | 2¢ | ❌ Lost | -$0.15 |
| 11/1 2:42:13 AM | SOL | DOWN | 2.8 min | +0.158% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 2:42:13 AM | NEAR | DOWN | 2.8 min | +0.226% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 2:41:24 AM | HYPE | DOWN | 3.6 min | +0.392% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 2:26:29 AM | NEAR | UP | 3.5 min | -0.397% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 2:26:07 AM | ETH | UP | 3.9 min | -0.188% | 0¢ | ❌ Lost | $0.00 |
| 11/1 2:26:07 AM | DOGE | UP | 3.9 min | -0.214% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
