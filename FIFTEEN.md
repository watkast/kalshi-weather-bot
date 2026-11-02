# 15-Minute 1¢ Study

*Updated Mon Nov 2, 12:19 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3510 finished bets | 1% | $125.45 | +32% | +3.57¢ | $71.00 / $54.45 |

*Expect about **99 buys a day** (~$14.82/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 2%, hold to the close | 6491 | $53.55 | +7% |
| Momentum model ≥ 5%, hold to the close | 3244 | $52.45 | +15% |
| Momentum model ≥ 2%, hold to the close | 5359 | -$32.25 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 42827 | 42817 | 159 (0%) | 1.07% | -$2,986.05 (-57%) | Hold to the close: -$2,986.05 (-57%) |

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
| Volatility model | 26582 | 4.7% | 0.4% (106) | -674% | ❌ Worse |
| Momentum model | 26582 | 4.6% | 0.4% (106) | -697% | ❌ Worse |
| Mean-reversion model | 26582 | 8.1% | 0.4% (106) | -821% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26582 | 106 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6491 | 60 | +7% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3510 | 37 | +32% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1989 | 22 | +58% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 5359 | 42 | -5% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3244 | 29 | +15% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2118 | 19 | +25% | -74% | -73% | -69% |
| Mean-reversion model ≥ 2% | 10989 | 76 | -24% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7701 | 65 | -7% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 5145 | 46 | +1% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 26784 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10062 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5971 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 42817 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 159 | 0% | -$2,986.05 | -57% | — |
| Sell at 2¢ | 1670 | 4% | -$4,553.85 | -87% | 47 sec |
| Sell at 3¢ | 1145 | 3% | -$4,541.50 | -87% | 48 sec |
| Sell at 5¢ | 795 | 2% | -$4,443.30 | -85% | 63 sec |
| Sell at 10¢ | 480 | 1% | -$4,261.25 | -82% | 65 sec |
| Sell at 25¢ | 251 | 1% | -$3,947.24 | -76% | 83 sec |
| Sell at 50¢ | 164 | 0% | -$3,587.05 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2046 | 9 | 11% | 4% | -58% | -81% | -82% |
| 2–5 min | 13743 | 75 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10825 | 38 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 16192 | 37 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3001 | 13 | 5% | 3% | -44% | -88% | -88% |
| SOL | 2992 | 11 | 4% | 2% | -54% | -91% | -91% |
| BNB | 2989 | 17 | 5% | 2% | -29% | -85% | -84% |
| HYPE | 2987 | 9 | 5% | 2% | -63% | -89% | -87% |
| DOGE | 2975 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 2974 | 11 | 6% | 3% | -55% | -86% | -85% |
| BTC | 2957 | 14 | 5% | 2% | -36% | -88% | -89% |
| NEAR | 2955 | 15 | 5% | 2% | -34% | -83% | -84% |
| XRP | 2954 | 12 | 3% | 1% | -50% | -89% | -89% |
| GOLD | 1565 | 5 | 5% | 2% | -61% | -81% | -83% |
| SILVER | 1524 | 7 | 5% | 2% | -45% | -82% | -82% |
| WTI | 1522 | 4 | 3% | 1% | -68% | -93% | -94% |
| PLATINUM | 1357 | 3 | 2% | 1% | -79% | -96% | -96% |
| EURUSD | 1298 | 3 | 2% | 1% | -78% | -89% | -89% |
| COPPER | 1294 | 5 | 2% | 1% | -64% | -76% | -75% |
| NATGAS | 1249 | 7 | 2% | 1% | -48% | -81% | -80% |
| GBPUSD | 1228 | 2 | 2% | 1% | -85% | -96% | -96% |
| PALLADIUM | 1223 | 2 | 1% | 0% | -85% | -90% | -91% |
| USDJPY | 1215 | 5 | 2% | 1% | -62% | -97% | -96% |
| AUDUSD | 752 | 4 | 1% | 1% | -50% | -85% | -84% |
| USDCAD | 724 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 328 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 204 | 1 | 5% | 2% | -54% | -46% | -44% |
| 30YRRATE | 192 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 187 | 2 | 4% | 1% | -0% | +7% | +8% |
| 5YRRATE | 171 | 1 | 6% | 2% | -45% | -90% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 21782 | 87 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 21035 | 72 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4362 | 21 | 2% | 1% | -16% | -82% | -81% |
| 0.05–0.1% | 4603 | 18 | 3% | 2% | -41% | -91% | -91% |
| 0.1–0.2% | 6943 | 24 | 4% | 2% | -57% | -90% | -90% |
| 0.2–0.5% | 7907 | 33 | 7% | 3% | -54% | -87% | -86% |
| Over 0.5% | 2964 | 12 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10646 | 37 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 10804 | 48 | 4% | 2% | -49% | -85% | -85% |
| Afternoon (12–6pm) | 9943 | 37 | 4% | 2% | -56% | -87% | -87% |
| Evening (6pm–12am) | 11424 | 37 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,780 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/2 12:14:48 PM | USDCAD | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 12:14:48 PM | WTI | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 12:14:48 PM | SILVER | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 12:14:48 PM | PLATINUM | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 12:14:48 PM | 10YRRATE | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 12:14:32 PM | BTC | UP | 27 sec | -0.045% | 0¢ | ❌ Lost | $0.00 |
| 11/2 12:14:17 PM | XRP | UP | 42 sec | -0.105% | 0¢ | ❌ Lost | $0.00 |
| 11/2 12:14:17 PM | BNB | UP | 42 sec | -0.095% | 0¢ | ❌ Lost | $0.00 |
| 11/2 12:14:17 PM | 5YRRATE | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 12:14:17 PM | DOGE | UP | 42 sec | -0.152% | 0¢ | ❌ Lost | $0.00 |
| 11/2 12:13:27 PM | PALLADIUM | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 12:13:12 PM | NEAR | UP | 1.8 min | -0.515% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 12:12:21 PM | ZEC | UP | 2.6 min | -0.590% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 12:12:21 PM | ETH | UP | 2.6 min | -0.228% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 12:12:06 PM | USDJPY | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 12:11:50 PM | GBPUSD | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 12:11:50 PM | SOL | UP | 3.1 min | -0.342% | 0¢ | ❌ Lost | $0.00 |
| 11/2 12:11:34 PM | HYPE | UP | 3.4 min | -0.479% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 12:11:34 PM | EURUSD | DOWN | 3.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 12:11:18 PM | 2YRRATE | UP | 3.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 11:59:46 AM | NATGAS | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 11:59:46 AM | USDJPY | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 11:59:46 AM | AUDUSD | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 11:59:31 AM | GBPUSD | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 11:59:31 AM | EURUSD | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 11:59:31 AM | ZEC | UP | 29 sec | -0.246% | 0¢ | ❌ Lost | $0.00 |
| 11/2 11:59:31 AM | 30YRRATE | UP | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 11:59:31 AM | BNB | DOWN | 29 sec | -0.003% | 0¢ | ❌ Lost | $0.00 |
| 11/2 11:58:56 AM | NEAR | DOWN | 64 sec | +0.248% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 11:58:56 AM | BTC | DOWN | 64 sec | +0.079% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
