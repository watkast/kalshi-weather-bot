# 15-Minute 1¢ Study

*Updated Mon Nov 2, 11:07 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3503 finished bets | 1% | $126.05 | +32% | +3.60¢ | $71.60 / $54.45 |

*Expect about **99 buys a day** (~$14.81/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 2%, hold to the close | 6472 | $55.80 | +7% |
| Momentum model ≥ 5%, hold to the close | 3236 | $53.35 | +15% |
| Momentum model ≥ 2%, hold to the close | 5340 | -$30.15 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 42719 | 42709 | 159 (0%) | 1.07% | -$2,972.55 (-57%) | Hold to the close: -$2,972.55 (-57%) |

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
| Volatility model | 26537 | 4.7% | 0.4% (106) | -674% | ❌ Worse |
| Momentum model | 26537 | 4.6% | 0.4% (106) | -697% | ❌ Worse |
| Mean-reversion model | 26537 | 8.1% | 0.4% (106) | -821% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26537 | 106 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6472 | 60 | +7% | -79% | -78% | -73% |
| Volatility model ≥ 5% | 3503 | 37 | +32% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1987 | 22 | +58% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 5340 | 42 | -5% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3236 | 29 | +15% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2114 | 19 | +25% | -74% | -73% | -69% |
| Mean-reversion model ≥ 2% | 10966 | 76 | -24% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7687 | 65 | -6% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 5140 | 46 | +1% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 26739 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10032 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5938 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 42709 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 159 | 0% | -$2,972.55 | -57% | — |
| Sell at 2¢ | 1669 | 4% | -$4,540.61 | -87% | 47 sec |
| Sell at 3¢ | 1145 | 3% | -$4,528.00 | -87% | 48 sec |
| Sell at 5¢ | 795 | 2% | -$4,429.80 | -85% | 63 sec |
| Sell at 10¢ | 480 | 1% | -$4,247.75 | -82% | 65 sec |
| Sell at 25¢ | 251 | 1% | -$3,933.74 | -76% | 83 sec |
| Sell at 50¢ | 164 | 0% | -$3,573.55 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2043 | 9 | 11% | 4% | -58% | -81% | -82% |
| 2–5 min | 13708 | 75 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10791 | 38 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 16156 | 37 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2996 | 13 | 5% | 3% | -44% | -88% | -88% |
| SOL | 2987 | 11 | 4% | 2% | -54% | -91% | -91% |
| BNB | 2984 | 17 | 5% | 2% | -29% | -85% | -84% |
| HYPE | 2982 | 9 | 5% | 2% | -63% | -89% | -87% |
| DOGE | 2970 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 2969 | 11 | 6% | 3% | -55% | -86% | -85% |
| BTC | 2952 | 14 | 5% | 2% | -36% | -88% | -89% |
| NEAR | 2950 | 15 | 5% | 2% | -34% | -83% | -83% |
| XRP | 2949 | 12 | 3% | 1% | -50% | -89% | -89% |
| GOLD | 1562 | 5 | 5% | 2% | -61% | -82% | -83% |
| SILVER | 1520 | 7 | 5% | 2% | -45% | -82% | -82% |
| WTI | 1518 | 4 | 3% | 1% | -68% | -93% | -94% |
| PLATINUM | 1353 | 3 | 2% | 1% | -79% | -96% | -96% |
| EURUSD | 1294 | 3 | 2% | 1% | -78% | -89% | -89% |
| COPPER | 1290 | 5 | 2% | 1% | -64% | -76% | -75% |
| NATGAS | 1245 | 7 | 2% | 1% | -48% | -81% | -80% |
| GBPUSD | 1223 | 2 | 2% | 1% | -85% | -96% | -96% |
| PALLADIUM | 1219 | 2 | 1% | 0% | -85% | -90% | -91% |
| USDJPY | 1211 | 5 | 2% | 1% | -61% | -97% | -96% |
| AUDUSD | 748 | 4 | 1% | 1% | -50% | -85% | -84% |
| USDCAD | 721 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 325 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 201 | 1 | 5% | 2% | -54% | -45% | -43% |
| 30YRRATE | 189 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 183 | 2 | 4% | 1% | +2% | +10% | +11% |
| 5YRRATE | 168 | 1 | 6% | 2% | -44% | -90% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 21724 | 87 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 20985 | 72 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4359 | 21 | 2% | 1% | -16% | -82% | -81% |
| 0.05–0.1% | 4600 | 18 | 3% | 2% | -41% | -91% | -91% |
| 0.1–0.2% | 6928 | 24 | 4% | 2% | -57% | -90% | -90% |
| 0.2–0.5% | 7890 | 33 | 7% | 3% | -54% | -87% | -86% |
| Over 0.5% | 2957 | 12 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10646 | 37 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 10716 | 48 | 4% | 2% | -49% | -85% | -85% |
| Afternoon (12–6pm) | 9923 | 37 | 4% | 2% | -56% | -87% | -87% |
| Evening (6pm–12am) | 11424 | 37 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,787 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/2 10:59:39 AM | COPPER | DOWN | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 10:59:24 AM | PLATINUM | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 10:59:24 AM | GOLD | DOWN | 36 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/2 10:59:24 AM | BNB | DOWN | 36 sec | +0.011% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 10:59:06 AM | DOGE | DOWN | 53 sec | +0.279% | 0¢ | ❌ Lost | $0.00 |
| 11/2 10:58:50 AM | ETH | DOWN | 69 sec | +0.203% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 10:58:50 AM | NEAR | DOWN | 69 sec | +0.265% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 10:58:50 AM | AUDUSD | DOWN | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 10:58:50 AM | HYPE | DOWN | 69 sec | +0.154% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 10:58:50 AM | SILVER | DOWN | 69 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 10:58:34 AM | BTC | DOWN | 85 sec | +0.165% | 0¢ | ❌ Lost | $0.00 |
| 11/2 10:58:03 AM | BRENT | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 10:57:14 AM | XRP | UP | 2.8 min | -0.282% | 17¢ | ❌ Lost | -$0.15 |
| 11/2 10:57:14 AM | ZEC | UP | 2.8 min | -0.853% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 10:56:11 AM | WTI | UP | 3.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 10:54:17 AM | SOL | UP | 5.7 min | -0.862% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 10:44:47 AM | WTI | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 10:44:47 AM | EURUSD | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 10:44:14 AM | ETH | UP | 45 sec | -0.106% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 10:44:14 AM | 10YRRATE | UP | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 10:44:14 AM | GBPUSD | UP | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 10:43:58 AM | XRP | UP | 61 sec | -0.137% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 10:43:58 AM | ZEC | UP | 61 sec | -0.336% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 10:43:58 AM | 30YRRATE | UP | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 10:43:58 AM | 5YRRATE | UP | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 10:43:58 AM | 2YRRATE | UP | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 10:43:42 AM | DOGE | UP | 77 sec | -0.228% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 10:43:42 AM | BTC | UP | 77 sec | -0.177% | 0¢ | ❌ Lost | $0.00 |
| 11/2 10:43:42 AM | GOLD | UP | 77 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 10:43:42 AM | NEAR | UP | 77 sec | -0.376% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
