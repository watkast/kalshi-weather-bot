# 15-Minute 1¢ Study

*Updated Sat Oct 24, 8:32 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2576 finished bets | 1% | $99.95 | +34% | +3.88¢ | $40.85 / $59.10 |

*Expect about **98 buys a day** (~$14.68/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2380 | $72.45 | +27% |
| Volatility model ≥ 2%, hold to the close | 4759 | $18.95 | +3% |
| Momentum model ≥ 2%, hold to the close | 3967 | -$4.20 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 30940 | 30932 | 119 (0%) | 1.07% | -$2,099.90 (-56%) | Hold to the close: -$2,099.90 (-56%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 19725 | 4.6% | 0.4% (84) | -635% | ❌ Worse |
| Momentum model | 19725 | 4.6% | 0.4% (84) | -660% | ❌ Worse |
| Mean-reversion model | 19725 | 7.9% | 0.4% (84) | -768% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 19725 | 84 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4759 | 43 | +3% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 2576 | 28 | +34% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 1468 | 18 | +72% | -65% | -63% | -60% |
| Momentum model ≥ 2% | 3967 | 33 | -1% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2380 | 24 | +27% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 1557 | 16 | +41% | -69% | -68% | -64% |
| Mean-reversion model ≥ 2% | 7920 | 55 | -24% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5541 | 46 | -9% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3686 | 33 | +1% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 19925 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 7352 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3655 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 30932 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 119 | 0% | -$2,099.90 | -56% | — |
| Sell at 2¢ | 1151 | 4% | -$3,298.64 | -88% | 47 sec |
| Sell at 3¢ | 789 | 3% | -$3,290.19 | -87% | 48 sec |
| Sell at 5¢ | 553 | 2% | -$3,238.45 | -86% | 61 sec |
| Sell at 10¢ | 340 | 1% | -$3,110.50 | -83% | 64 sec |
| Sell at 25¢ | 187 | 1% | -$2,866.93 | -76% | 82 sec |
| Sell at 50¢ | 121 | 0% | -$2,585.15 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1330 | 7 | 11% | 4% | -50% | -81% | -82% |
| 2–5 min | 9881 | 54 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 7852 | 30 | 3% | 1% | -58% | -92% | -91% |
| Under 1 min | 11865 | 28 | 1% | 0% | -66% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2234 | 12 | 5% | 2% | -32% | -89% | -89% |
| HYPE | 2226 | 8 | 5% | 3% | -56% | -88% | -86% |
| BNB | 2223 | 12 | 5% | 2% | -33% | -83% | -82% |
| SOL | 2218 | 6 | 4% | 2% | -66% | -92% | -92% |
| ETH | 2213 | 11 | 6% | 3% | -40% | -86% | -85% |
| DOGE | 2209 | 4 | 4% | 2% | -77% | -90% | -90% |
| XRP | 2205 | 9 | 3% | 1% | -49% | -88% | -88% |
| NEAR | 2202 | 12 | 5% | 3% | -29% | -81% | -81% |
| BTC | 2195 | 12 | 5% | 2% | -27% | -88% | -89% |
| GOLD | 1190 | 4 | 4% | 2% | -60% | -81% | -83% |
| SILVER | 1156 | 5 | 4% | 1% | -50% | -82% | -82% |
| WTI | 1143 | 3 | 3% | 1% | -69% | -94% | -95% |
| PLATINUM | 1010 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 987 | 4 | 1% | 1% | -62% | -69% | -69% |
| EURUSD | 938 | 3 | 2% | 1% | -70% | -86% | -86% |
| NATGAS | 933 | 5 | 2% | 1% | -50% | -86% | -86% |
| PALLADIUM | 897 | 2 | 1% | 0% | -79% | -88% | -88% |
| GBPUSD | 884 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 866 | 5 | 1% | 1% | -46% | -98% | -97% |
| AUDUSD | 428 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 387 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 36 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 15661 | 65 | 4% | 2% | -52% | -87% | -86% |
| DOWN (bought NO) | 15271 | 54 | 4% | 2% | -59% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3323 | 18 | 2% | 1% | -9% | -79% | -79% |
| 0.05–0.1% | 3434 | 11 | 3% | 1% | -53% | -92% | -92% |
| 0.1–0.2% | 5135 | 19 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 5802 | 28 | 6% | 3% | -47% | -87% | -86% |
| Over 0.5% | 2227 | 10 | 7% | 3% | -54% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7739 | 32 | 4% | 2% | -53% | -85% | -85% |
| Morning (6am–12pm) | 7510 | 34 | 4% | 2% | -48% | -88% | -87% |
| Afternoon (12–6pm) | 7298 | 24 | 4% | 2% | -61% | -87% | -88% |
| Evening (6pm–12am) | 8385 | 29 | 3% | 2% | -60% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,668 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/24 8:27:27 AM | BNB | UP | 2.5 min | -0.527% | 1¢ | ❌ Lost | $0.00 |
| 10/24 8:27:11 AM | HYPE | UP | 2.8 min | -0.826% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 8:26:38 AM | XRP | UP | 3.4 min | -0.813% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 8:26:06 AM | SOL | UP | 3.9 min | -0.864% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 8:25:35 AM | BTC | UP | 4.4 min | -0.569% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 8:24:46 AM | DOGE | UP | 5.2 min | -1.537% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 8:24:46 AM | ZEC | UP | 5.2 min | -1.622% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 8:24:30 AM | ETH | UP | 5.5 min | -0.809% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 8:24:30 AM | NEAR | UP | 5.5 min | -1.925% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 8:14:08 AM | XRP | UP | 51 sec | -0.179% | 0¢ | ❌ Lost | $0.00 |
| 10/24 8:13:51 AM | BTC | UP | 68 sec | -0.090% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 8:13:51 AM | BNB | UP | 68 sec | -0.158% | 0¢ | ❌ Lost | $0.00 |
| 10/24 8:12:47 AM | ETH | UP | 2.2 min | -0.190% | 0¢ | ❌ Lost | $0.00 |
| 10/24 8:12:47 AM | DOGE | UP | 2.2 min | -0.199% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 8:12:47 AM | ZEC | UP | 2.2 min | -0.363% | 0¢ | ❌ Lost | $0.00 |
| 10/24 8:12:47 AM | HYPE | UP | 2.2 min | -0.384% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 8:12:31 AM | SOL | UP | 2.5 min | -0.223% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 8:11:44 AM | NEAR | UP | 3.3 min | -0.611% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 7:59:37 AM | SOL | UP | 23 sec | -0.062% | 0¢ | ❌ Lost | $0.00 |
| 10/24 7:59:37 AM | DOGE | UP | 23 sec | -0.093% | 0¢ | ❌ Lost | $0.00 |
| 10/24 7:59:37 AM | BTC | UP | 23 sec | -0.019% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 7:59:21 AM | ETH | DOWN | 39 sec | +0.010% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 7:58:34 AM | HYPE | DOWN | 85 sec | +0.083% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 7:58:34 AM | BNB | UP | 85 sec | -0.079% | 0¢ | ❌ Lost | $0.00 |
| 10/24 7:57:12 AM | ZEC | UP | 2.8 min | -0.339% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 7:57:12 AM | NEAR | UP | 2.8 min | -0.449% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 7:44:54 AM | XRP | UP | 5 sec | -0.047% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 7:44:54 AM | BNB | DOWN | 5 sec | -0.005% | 0¢ | ❌ Lost | $0.00 |
| 10/24 7:44:38 AM | SOL | UP | 21 sec | -0.023% | 0¢ | ❌ Lost | $0.00 |
| 10/24 7:44:38 AM | DOGE | DOWN | 21 sec | -0.009% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
