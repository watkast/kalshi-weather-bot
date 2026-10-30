# 15-Minute 1¢ Study

*Updated Fri Oct 30, 10:15 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3174 finished bets | 1% | $92.95 | +26% | +2.93¢ | $75.75 / $17.20 |

*Expect about **98 buys a day** (~$14.70/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2939 | $42.70 | +13% |
| Volatility model ≥ 2%, hold to the close | 5885 | $0.30 | +0% |
| Volatility model ≥ 5%, sell at 50¢ | 3174 | -$68.55 | -19% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 39664 | 39637 | 145 (0%) | 1.07% | -$2,813.65 (-58%) | Hold to the close: -$2,813.65 (-58%) |

*In play or awaiting result: 26. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 24247 | 4.6% | 0.4% (94) | -680% | ❌ Worse |
| Momentum model | 24247 | 4.5% | 0.4% (94) | -703% | ❌ Worse |
| Mean-reversion model | 24247 | 8.0% | 0.4% (94) | -829% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 24247 | 94 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5885 | 51 | +0% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3174 | 32 | +26% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1790 | 19 | +52% | -68% | -67% | -64% |
| Momentum model ≥ 2% | 4853 | 35 | -13% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2939 | 26 | +13% | -78% | -78% | -73% |
| Momentum model ≥ 10% | 1911 | 17 | +23% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9953 | 65 | -29% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 6967 | 55 | -13% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4642 | 39 | -5% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 24448 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9591 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5598 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 39637 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 145 | 0% | -$2,813.65 | -58% | — |
| Sell at 2¢ | 1525 | 4% | -$4,251.15 | -88% | 47 sec |
| Sell at 3¢ | 1051 | 3% | -$4,237.76 | -87% | 49 sec |
| Sell at 5¢ | 731 | 2% | -$4,158.50 | -86% | 63 sec |
| Sell at 10¢ | 442 | 1% | -$3,984.63 | -82% | 65 sec |
| Sell at 25¢ | 230 | 1% | -$3,690.35 | -76% | 83 sec |
| Sell at 50¢ | 149 | 0% | -$3,361.90 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 9 | 0 | 33% | 22% | -100% | -42% | -13% |
| 5–10 min | 1848 | 8 | 11% | 4% | -59% | -80% | -81% |
| 2–5 min | 12646 | 69 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10034 | 35 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 15100 | 33 | 1% | 0% | -69% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2736 | 13 | 5% | 3% | -39% | -88% | -88% |
| HYPE | 2730 | 8 | 5% | 3% | -64% | -89% | -87% |
| BNB | 2727 | 15 | 5% | 3% | -31% | -85% | -83% |
| SOL | 2724 | 7 | 4% | 2% | -68% | -91% | -91% |
| ETH | 2717 | 11 | 6% | 3% | -51% | -86% | -85% |
| DOGE | 2717 | 6 | 4% | 2% | -72% | -90% | -89% |
| BTC | 2700 | 13 | 5% | 2% | -35% | -88% | -89% |
| NEAR | 2699 | 12 | 5% | 2% | -42% | -83% | -83% |
| XRP | 2698 | 11 | 3% | 1% | -50% | -89% | -89% |
| GOLD | 1501 | 5 | 5% | 2% | -60% | -82% | -83% |
| SILVER | 1467 | 7 | 4% | 2% | -43% | -82% | -81% |
| WTI | 1448 | 4 | 3% | 1% | -67% | -92% | -93% |
| PLATINUM | 1304 | 3 | 2% | 1% | -79% | -96% | -96% |
| COPPER | 1241 | 5 | 1% | 1% | -62% | -75% | -75% |
| EURUSD | 1240 | 3 | 2% | 1% | -77% | -88% | -88% |
| NATGAS | 1197 | 7 | 2% | 1% | -45% | -81% | -80% |
| GBPUSD | 1175 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1168 | 2 | 1% | 0% | -84% | -90% | -90% |
| USDJPY | 1160 | 5 | 2% | 1% | -60% | -97% | -96% |
| AUDUSD | 700 | 4 | 2% | 1% | -47% | -84% | -83% |
| USDCAD | 673 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 265 | 0 | 1% | 0% | -100% | -99% | -98% |
| 10YRRATE | 175 | 0 | 4% | 1% | -100% | -93% | -91% |
| 30YRRATE | 168 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 161 | 1 | 5% | 1% | -42% | -33% | -32% |
| 5YRRATE | 146 | 1 | 6% | 3% | -36% | -89% | -91% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 20142 | 80 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 19495 | 65 | 4% | 2% | -62% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3905 | 19 | 2% | 1% | -16% | -81% | -81% |
| 0.05–0.1% | 4142 | 14 | 3% | 2% | -49% | -92% | -92% |
| 0.1–0.2% | 6279 | 22 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 7294 | 31 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2824 | 10 | 7% | 3% | -63% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9916 | 36 | 4% | 2% | -59% | -86% | -86% |
| Morning (6am–12pm) | 9963 | 44 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 9178 | 31 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 10580 | 34 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,456 |
| Time from buy to best bounce (bounced bets) | 52 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/30 10:14:56 AM | GOLD | UP | 3 sec | — | 0¢ | In play | — |
| 10/30 10:14:56 AM | USDJPY | UP | 3 sec | — | 0¢ | In play | — |
| 10/30 10:14:56 AM | PALLADIUM | UP | 3 sec | — | 0¢ | In play | — |
| 10/30 10:14:25 AM | DOGE | DOWN | 34 sec | +0.028% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 10:14:25 AM | SILVER | UP | 34 sec | — | 0¢ | In play | — |
| 10/30 10:14:25 AM | BTC | UP | 34 sec | -0.064% | 0¢ | ❌ Lost | $0.00 |
| 10/30 10:14:25 AM | NATGAS | DOWN | 34 sec | — | 0¢ | In play | — |
| 10/30 10:14:25 AM | COPPER | UP | 34 sec | — | 0¢ | In play | — |
| 10/30 10:14:08 AM | GBPUSD | DOWN | 52 sec | — | 0¢ | In play | — |
| 10/30 10:13:52 AM | BRENT | DOWN | 68 sec | — | 0¢ | In play | — |
| 10/30 10:13:52 AM | NEAR | DOWN | 68 sec | +0.415% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 10:13:36 AM | ETH | DOWN | 84 sec | +0.173% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 10:13:36 AM | ZEC | DOWN | 84 sec | +0.469% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 10:13:36 AM | SOL | DOWN | 84 sec | +0.224% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 10:13:21 AM | BNB | DOWN | 1.6 min | +0.154% | 2¢ | In play | — |
| 10/30 10:13:21 AM | EURUSD | DOWN | 1.6 min | — | 0¢ | In play | — |
| 10/30 10:13:21 AM | WTI | DOWN | 1.6 min | — | 0¢ | In play | — |
| 10/30 10:11:58 AM | USDCAD | UP | 3.0 min | — | 0¢ | In play | — |
| 10/30 10:11:42 AM | XRP | UP | 3.3 min | -0.582% | 1¢ | In play | — |
| 10/30 10:11:26 AM | PLATINUM | UP | 3.5 min | — | 1¢ | In play | — |
| 10/30 10:11:11 AM | HYPE | UP | 3.8 min | -0.684% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 10:11:11 AM | 10YRRATE | UP | 3.8 min | — | 9¢ | In play | — |
| 10/30 10:09:16 AM | 2YRRATE | UP | 5.7 min | — | 0¢ | In play | — |
| 10/30 10:09:00 AM | 5YRRATE | UP | 6.0 min | — | 0¢ | In play | — |
| 10/30 9:59:47 AM | WTI | DOWN | 12 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/30 9:59:31 AM | EURUSD | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 9:59:31 AM | AUDUSD | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 9:59:16 AM | ETH | UP | 43 sec | -0.155% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 9:59:16 AM | DOGE | DOWN | 43 sec | +0.159% | 0¢ | ❌ Lost | $0.00 |
| 10/30 9:59:16 AM | GBPUSD | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
