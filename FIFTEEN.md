# 15-Minute 1¢ Study

*Updated Mon Nov 2, 3:04 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3487 finished bets | 1% | $128.00 | +33% | +3.67¢ | $72.65 / $55.35 |

*Expect about **99 buys a day** (~$14.88/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 2%, hold to the close | 6439 | $59.85 | +8% |
| Momentum model ≥ 5%, hold to the close | 3214 | $55.90 | +16% |
| Momentum model ≥ 2%, hold to the close | 5307 | -$26.25 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 42403 | 42393 | 159 (0%) | 1.07% | -$2,933.70 (-57%) | Hold to the close: -$2,933.70 (-57%) |

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
| Volatility model | 26396 | 4.7% | 0.4% (106) | -673% | ❌ Worse |
| Momentum model | 26396 | 4.6% | 0.4% (106) | -695% | ❌ Worse |
| Mean-reversion model | 26396 | 8.1% | 0.4% (106) | -820% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26396 | 106 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6439 | 60 | +8% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3487 | 37 | +33% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1976 | 22 | +59% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 5307 | 42 | -4% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3214 | 29 | +16% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2098 | 19 | +26% | -74% | -73% | -68% |
| Mean-reversion model ≥ 2% | 10914 | 76 | -24% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7652 | 65 | -6% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 5117 | 46 | +2% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 26598 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 9945 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5850 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 42393 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 159 | 0% | -$2,933.70 | -57% | — |
| Sell at 2¢ | 1660 | 4% | -$4,504.10 | -87% | 47 sec |
| Sell at 3¢ | 1138 | 3% | -$4,491.88 | -87% | 48 sec |
| Sell at 5¢ | 792 | 2% | -$4,392.90 | -85% | 63 sec |
| Sell at 10¢ | 478 | 1% | -$4,211.52 | -82% | 65 sec |
| Sell at 25¢ | 251 | 1% | -$3,894.89 | -75% | 83 sec |
| Sell at 50¢ | 164 | 0% | -$3,534.70 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2027 | 9 | 11% | 4% | -58% | -81% | -82% |
| 2–5 min | 13624 | 75 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10700 | 38 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 16031 | 37 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2980 | 13 | 5% | 3% | -44% | -88% | -87% |
| SOL | 2971 | 11 | 4% | 2% | -53% | -91% | -91% |
| BNB | 2968 | 17 | 5% | 2% | -28% | -85% | -84% |
| HYPE | 2966 | 9 | 5% | 2% | -62% | -89% | -87% |
| DOGE | 2955 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 2953 | 11 | 6% | 3% | -55% | -85% | -85% |
| BTC | 2936 | 14 | 5% | 2% | -36% | -88% | -89% |
| NEAR | 2935 | 15 | 5% | 2% | -34% | -83% | -83% |
| XRP | 2934 | 12 | 3% | 1% | -49% | -89% | -89% |
| GOLD | 1550 | 5 | 5% | 2% | -61% | -82% | -84% |
| SILVER | 1509 | 7 | 5% | 2% | -45% | -82% | -82% |
| WTI | 1506 | 4 | 3% | 1% | -68% | -93% | -94% |
| PLATINUM | 1341 | 3 | 2% | 1% | -79% | -96% | -96% |
| COPPER | 1283 | 5 | 1% | 1% | -64% | -76% | -76% |
| EURUSD | 1281 | 3 | 2% | 1% | -78% | -89% | -89% |
| NATGAS | 1235 | 7 | 2% | 1% | -47% | -81% | -80% |
| GBPUSD | 1213 | 2 | 2% | 1% | -85% | -96% | -96% |
| PALLADIUM | 1207 | 2 | 1% | 0% | -85% | -90% | -91% |
| USDJPY | 1201 | 5 | 2% | 1% | -61% | -97% | -96% |
| AUDUSD | 736 | 4 | 1% | 1% | -49% | -85% | -84% |
| USDCAD | 712 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 314 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 193 | 1 | 5% | 2% | -52% | -43% | -41% |
| 30YRRATE | 182 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 173 | 2 | 5% | 1% | +8% | +16% | +17% |
| 5YRRATE | 159 | 1 | 6% | 3% | -41% | -89% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 21531 | 87 | 4% | 2% | -53% | -88% | -87% |
| DOWN (bought NO) | 20862 | 72 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4337 | 21 | 2% | 1% | -16% | -82% | -81% |
| 0.05–0.1% | 4577 | 18 | 3% | 2% | -41% | -91% | -91% |
| 0.1–0.2% | 6893 | 24 | 4% | 2% | -57% | -90% | -90% |
| 0.2–0.5% | 7844 | 33 | 7% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2942 | 12 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10533 | 37 | 4% | 2% | -60% | -86% | -87% |
| Morning (6am–12pm) | 10513 | 48 | 5% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 9923 | 37 | 4% | 2% | -56% | -87% | -87% |
| Evening (6pm–12am) | 11424 | 37 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,797 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/2 2:59:44 AM | COPPER | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 2:59:44 AM | BTC | UP | 15 sec | -0.038% | 0¢ | ❌ Lost | $0.00 |
| 11/2 2:59:44 AM | GBPUSD | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 2:59:44 AM | SOL | UP | 15 sec | -0.025% | 0¢ | ❌ Lost | $0.00 |
| 11/2 2:59:44 AM | USDJPY | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 2:59:28 AM | NATGAS | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 2:59:12 AM | GOLD | UP | 47 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/2 2:59:12 AM | BNB | UP | 47 sec | -0.158% | 0¢ | ❌ Lost | $0.00 |
| 11/2 2:59:12 AM | NEAR | UP | 47 sec | -0.221% | 0¢ | ❌ Lost | $0.00 |
| 11/2 2:58:25 AM | ZEC | DOWN | 1.6 min | +0.249% | 0¢ | ❌ Lost | $0.00 |
| 11/2 2:58:25 AM | DOGE | DOWN | 1.6 min | +0.069% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 2:57:21 AM | PLATINUM | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 2:57:05 AM | PALLADIUM | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 2:44:52 AM | 10YRRATE | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 2:44:36 AM | XRP | UP | 24 sec | -0.056% | 0¢ | ❌ Lost | $0.00 |
| 11/2 2:44:36 AM | PALLADIUM | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 2:44:36 AM | WTI | UP | 24 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/2 2:44:36 AM | BRENT | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 2:44:05 AM | ETH | UP | 55 sec | -0.096% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 2:43:49 AM | USDJPY | DOWN | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 2:43:33 AM | BTC | UP | 87 sec | -0.062% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 2:43:01 AM | ZEC | UP | 2.0 min | -0.266% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 2:42:45 AM | NEAR | UP | 2.2 min | -0.353% | 2¢ | ❌ Lost | -$0.15 |
| 11/2 2:42:29 AM | BNB | UP | 2.5 min | -0.161% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 2:41:57 AM | SOL | UP | 3.0 min | -0.231% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 2:41:42 AM | AUDUSD | UP | 3.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 2:40:06 AM | HYPE | UP | 4.9 min | -0.418% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 2:39:18 AM | USDCAD | DOWN | 5.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 2:39:18 AM | GBPUSD | UP | 5.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 2:39:02 AM | EURUSD | UP | 6.0 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
