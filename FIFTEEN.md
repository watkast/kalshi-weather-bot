# 15-Minute 1¢ Study

*Updated Mon Nov 23, 11:50 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4826 finished bets | 1% | $215.20 | +41% | +4.46¢ | $76.85 / $138.35 |

*Expect about **85 buys a day** (~$12.70/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4573 | $113.45 | +23% |
| Volatility model ≥ 2%, hold to the close | 8985 | $48.25 | +5% |
| Momentum model ≥ 2%, hold to the close | 7485 | -$25.55 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 66151 | 66117 | 254 (0%) | 1.07% | -$4,449.35 (-56%) | Hold to the close: -$4,449.35 (-56%) |

*In play or awaiting result: 6. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 39436 | 4.5% | 0.4% (164) | -640% | ❌ Worse |
| Momentum model | 39436 | 4.4% | 0.4% (164) | -663% | ❌ Worse |
| Mean-reversion model | 39436 | 7.9% | 0.4% (164) | -778% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 39436 | 164 | -46% | -87% | -86% | -84% |
| Volatility model ≥ 2% | 8985 | 80 | +5% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4826 | 53 | +41% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 2793 | 32 | +69% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 7485 | 59 | -3% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 4573 | 43 | +23% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 2980 | 28 | +35% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 16046 | 112 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 11167 | 92 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7416 | 66 | +2% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 39642 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15665 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10810 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 66117 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 254 | 0% | -$4,449.35 | -56% | — |
| Sell at 2¢ | 2709 | 4% | -$7,007.01 | -88% | 47 sec |
| Sell at 3¢ | 1825 | 3% | -$6,999.60 | -87% | 48 sec |
| Sell at 5¢ | 1246 | 2% | -$6,873.45 | -86% | 62 sec |
| Sell at 10¢ | 763 | 1% | -$6,599.82 | -82% | 65 sec |
| Sell at 25¢ | 410 | 1% | -$6,088.25 | -76% | 79 sec |
| Sell at 50¢ | 263 | 0% | -$5,488.10 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3422 | 17 | 11% | 4% | -53% | -81% | -83% |
| 2–5 min | 21430 | 115 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 16524 | 57 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 24728 | 65 | 1% | 0% | -62% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4431 | 19 | 5% | 2% | -43% | -88% | -87% |
| HYPE | 4426 | 16 | 5% | 2% | -53% | -89% | -88% |
| SOL | 4423 | 20 | 4% | 2% | -41% | -86% | -86% |
| BNB | 4415 | 22 | 5% | 2% | -37% | -86% | -85% |
| DOGE | 4411 | 12 | 5% | 2% | -65% | -89% | -89% |
| ETH | 4406 | 19 | 7% | 3% | -46% | -82% | -82% |
| BTC | 4384 | 24 | 5% | 2% | -25% | -86% | -87% |
| NEAR | 4379 | 18 | 5% | 2% | -46% | -85% | -86% |
| XRP | 4367 | 16 | 4% | 2% | -53% | -89% | -88% |
| GOLD | 2324 | 8 | 5% | 2% | -58% | -82% | -84% |
| WTI | 2307 | 8 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 2264 | 9 | 5% | 2% | -52% | -83% | -83% |
| PLATINUM | 2057 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 2020 | 7 | 3% | 1% | -68% | -91% | -90% |
| GBPUSD | 1949 | 8 | 2% | 1% | -62% | -96% | -96% |
| COPPER | 1947 | 6 | 2% | 1% | -71% | -78% | -78% |
| USDJPY | 1912 | 6 | 2% | 1% | -71% | -96% | -96% |
| NATGAS | 1909 | 10 | 2% | 1% | -51% | -77% | -76% |
| PALLADIUM | 1848 | 4 | 1% | 1% | -80% | -93% | -93% |
| AUDUSD | 1465 | 6 | 2% | 1% | -62% | -90% | -90% |
| USDCAD | 1383 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 1009 | 1 | 2% | 1% | -91% | -97% | -97% |
| 10YRRATE | 520 | 2 | 3% | 1% | -64% | -77% | -75% |
| 2YRRATE | 494 | 4 | 4% | 2% | -24% | -56% | -55% |
| 30YRRATE | 479 | 0 | 3% | 1% | -100% | -96% | -93% |
| 5YRRATE | 471 | 2 | 3% | 1% | -60% | -94% | -96% |
| INX | 112 | 1 | 2% | 1% | -17% | -97% | -98% |
| USDMXN | 5 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 33806 | 130 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 32311 | 124 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5790 | 25 | 2% | 1% | -21% | -78% | -78% |
| 0.05–0.1% | 6327 | 26 | 3% | 2% | -34% | -91% | -90% |
| 0.1–0.2% | 9856 | 36 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12466 | 56 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 5194 | 23 | 7% | 3% | -54% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15988 | 49 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 15586 | 81 | 4% | 2% | -41% | -85% | -85% |
| Afternoon (12–6pm) | 16344 | 73 | 4% | 2% | -47% | -87% | -87% |
| Evening (6pm–12am) | 18199 | 51 | 4% | 2% | -68% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,137 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/23 11:44:35 PM | BTC | DOWN | 24 sec | +0.036% | 0¢ | ❌ Lost | $0.00 |
| 11/23 11:44:35 PM | HYPE | DOWN | 24 sec | +0.003% | 0¢ | ❌ Lost | $0.00 |
| 11/23 11:44:35 PM | PALLADIUM | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 11:44:35 PM | ETH | DOWN | 24 sec | +0.022% | 1¢ | ❌ Lost | -$0.15 |
| 11/23 11:44:35 PM | WTI | DOWN | 24 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/23 11:44:19 PM | ZEC | UP | 40 sec | -0.257% | 0¢ | ❌ Lost | $0.00 |
| 11/23 11:44:19 PM | XRP | UP | 40 sec | -0.126% | 0¢ | ❌ Lost | $0.00 |
| 11/23 11:43:48 PM | PLATINUM | DOWN | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 11:43:48 PM | GOLD | DOWN | 71 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/23 11:43:48 PM | DOGE | DOWN | 71 sec | +0.106% | 0¢ | ❌ Lost | $0.00 |
| 11/23 11:43:32 PM | BNB | DOWN | 87 sec | -0.009% | 0¢ | ❌ Lost | -$0.15 |
| 11/23 11:43:32 PM | EURUSD | UP | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 11:43:16 PM | SILVER | DOWN | 1.7 min | — | 0¢ | ❌ Lost | $0.00 |
| 11/23 11:43:16 PM | USDJPY | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/23 11:43:16 PM | AUDUSD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 11:43:16 PM | SOL | DOWN | 1.7 min | +0.268% | 0¢ | ❌ Lost | $0.00 |
| 11/23 11:42:45 PM | COPPER | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 11:29:50 PM | BTC | UP | 9 sec | -0.056% | 0¢ | ❌ Lost | $0.00 |
| 11/23 11:29:50 PM | ETH | UP | 9 sec | -0.052% | 0¢ | ❌ Lost | -$0.15 |
| 11/23 11:29:50 PM | WTI | DOWN | 9 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/23 11:29:34 PM | USDCAD | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 11:29:18 PM | SOL | UP | 41 sec | -0.058% | 1¢ | ❌ Lost | -$0.15 |
| 11/23 11:28:46 PM | HYPE | UP | 74 sec | -0.230% | 1¢ | ❌ Lost | -$0.15 |
| 11/23 11:28:46 PM | GBPUSD | DOWN | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 11:28:30 PM | PALLADIUM | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 11:28:14 PM | PLATINUM | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 11:28:14 PM | NATGAS | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 11:28:14 PM | SILVER | UP | 1.8 min | — | 0¢ | ❌ Lost | $0.00 |
| 11/23 11:27:26 PM | AUDUSD | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 11:27:10 PM | USDJPY | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
