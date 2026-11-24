# 15-Minute 1¢ Study

*Updated Mon Nov 23, 5:43 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4813 finished bets | 1% | $216.40 | +41% | +4.50¢ | $77.75 / $138.65 |

*Expect about **85 buys a day** (~$12.72/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4564 | $113.90 | +23% |
| Volatility model ≥ 2%, hold to the close | 8964 | $50.20 | +5% |
| Momentum model ≥ 2%, hold to the close | 7470 | -$24.35 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 65929 | 65893 | 254 (0%) | 1.07% | -$4,421.75 (-55%) | Hold to the close: -$4,421.75 (-55%) |

*In play or awaiting result: 8. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 39330 | 4.5% | 0.4% (164) | -639% | ❌ Worse |
| Momentum model | 39330 | 4.4% | 0.4% (164) | -663% | ❌ Worse |
| Mean-reversion model | 39330 | 7.9% | 0.4% (164) | -775% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 39330 | 164 | -46% | -87% | -86% | -84% |
| Volatility model ≥ 2% | 8964 | 80 | +5% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4813 | 53 | +41% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 2783 | 32 | +70% | -64% | -62% | -59% |
| Momentum model ≥ 2% | 7470 | 59 | -3% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 4564 | 43 | +23% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 2974 | 28 | +36% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 16002 | 112 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 11130 | 92 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7393 | 66 | +2% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 39536 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15591 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10766 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 65893 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 254 | 0% | -$4,421.75 | -55% | — |
| Sell at 2¢ | 2699 | 4% | -$6,982.01 | -88% | 47 sec |
| Sell at 3¢ | 1819 | 3% | -$6,974.34 | -87% | 48 sec |
| Sell at 5¢ | 1243 | 2% | -$6,847.80 | -86% | 62 sec |
| Sell at 10¢ | 762 | 1% | -$6,573.53 | -82% | 65 sec |
| Sell at 25¢ | 410 | 1% | -$6,060.65 | -76% | 79 sec |
| Sell at 50¢ | 263 | 0% | -$5,460.50 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3405 | 17 | 11% | 4% | -53% | -81% | -83% |
| 2–5 min | 21357 | 115 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 16464 | 57 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 24654 | 65 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4419 | 19 | 5% | 2% | -42% | -88% | -87% |
| HYPE | 4414 | 16 | 5% | 2% | -53% | -89% | -88% |
| SOL | 4411 | 20 | 5% | 2% | -41% | -86% | -86% |
| BNB | 4403 | 22 | 5% | 2% | -36% | -86% | -85% |
| DOGE | 4399 | 12 | 5% | 2% | -65% | -89% | -89% |
| ETH | 4394 | 19 | 7% | 3% | -46% | -82% | -82% |
| BTC | 4372 | 24 | 6% | 2% | -25% | -86% | -87% |
| NEAR | 4368 | 18 | 5% | 2% | -46% | -85% | -86% |
| XRP | 4356 | 16 | 4% | 2% | -53% | -89% | -88% |
| GOLD | 2312 | 8 | 5% | 2% | -58% | -82% | -84% |
| WTI | 2297 | 8 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 2255 | 9 | 5% | 2% | -52% | -83% | -84% |
| PLATINUM | 2050 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 2010 | 7 | 3% | 1% | -67% | -91% | -90% |
| GBPUSD | 1942 | 8 | 2% | 1% | -62% | -96% | -96% |
| COPPER | 1936 | 6 | 2% | 1% | -71% | -77% | -77% |
| USDJPY | 1901 | 6 | 2% | 1% | -71% | -97% | -96% |
| NATGAS | 1899 | 10 | 2% | 1% | -51% | -77% | -76% |
| PALLADIUM | 1841 | 4 | 1% | 1% | -80% | -93% | -93% |
| AUDUSD | 1457 | 6 | 2% | 1% | -62% | -90% | -90% |
| USDCAD | 1376 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 1001 | 1 | 2% | 1% | -91% | -97% | -97% |
| 10YRRATE | 520 | 2 | 3% | 1% | -64% | -77% | -75% |
| 2YRRATE | 494 | 4 | 4% | 2% | -24% | -56% | -55% |
| 30YRRATE | 479 | 0 | 3% | 1% | -100% | -96% | -93% |
| 5YRRATE | 471 | 2 | 3% | 1% | -60% | -94% | -96% |
| INX | 112 | 1 | 2% | 1% | -17% | -97% | -98% |
| USDMXN | 4 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 33705 | 130 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 32188 | 124 | 4% | 2% | -55% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5777 | 25 | 2% | 1% | -21% | -78% | -78% |
| 0.05–0.1% | 6321 | 26 | 3% | 2% | -34% | -91% | -90% |
| 0.1–0.2% | 9831 | 36 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12422 | 56 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 5176 | 23 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15988 | 49 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 15586 | 81 | 4% | 2% | -41% | -85% | -85% |
| Afternoon (12–6pm) | 16307 | 73 | 4% | 2% | -47% | -87% | -87% |
| Evening (6pm–12am) | 18012 | 51 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,136 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/23 5:42:16 PM | NEAR | UP | 2.7 min | -0.678% | — | In play | — |
| 11/23 5:42:06 PM | GOLD | DOWN | 2.9 min | — | — | In play | — |
| 11/23 5:29:54 PM | BTC | UP | 6 sec | -0.030% | 1¢ | ❌ Lost | -$0.15 |
| 11/23 5:29:54 PM | NATGAS | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 5:29:54 PM | BRENT | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 5:29:38 PM | WTI | DOWN | 22 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/23 5:29:38 PM | PALLADIUM | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 5:29:06 PM | ETH | DOWN | 54 sec | +0.053% | 1¢ | ❌ Lost | -$0.15 |
| 11/23 5:29:06 PM | USDCAD | DOWN | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 5:29:06 PM | COPPER | DOWN | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 5:28:50 PM | PLATINUM | DOWN | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 5:28:18 PM | GBPUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 5:28:18 PM | ZEC | DOWN | 1.7 min | +0.412% | 0¢ | ❌ Lost | -$0.15 |
| 11/23 5:28:02 PM | EURUSD | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 5:28:02 PM | USDJPY | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 5:27:44 PM | AUDUSD | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 5:27:28 PM | HYPE | DOWN | 2.5 min | +0.349% | 0¢ | ❌ Lost | $0.00 |
| 11/23 5:27:12 PM | BNB | DOWN | 2.8 min | +0.147% | 1¢ | ❌ Lost | -$0.15 |
| 11/23 5:27:12 PM | SOL | DOWN | 2.8 min | +0.248% | 1¢ | ❌ Lost | -$0.15 |
| 11/23 5:26:57 PM | DOGE | DOWN | 3.0 min | +0.474% | 0¢ | ❌ Lost | $0.00 |
| 11/23 5:26:57 PM | GOLD | DOWN | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/23 5:26:41 PM | SILVER | DOWN | 3.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/23 5:26:09 PM | XRP | DOWN | 3.8 min | +0.320% | 1¢ | ❌ Lost | -$0.15 |
| 11/23 5:24:49 PM | NEAR | DOWN | 5.2 min | +0.596% | 2¢ | ❌ Lost | -$0.15 |
| 11/23 5:14:52 PM | BNB | UP | 8 sec | -0.086% | 0¢ | ❌ Lost | $0.00 |
| 11/23 5:14:52 PM | NEAR | UP | 8 sec | -0.043% | 0¢ | ❌ Lost | -$0.15 |
| 11/23 5:14:52 PM | PALLADIUM | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 5:14:36 PM | GBPUSD | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 5:14:36 PM | GOLD | DOWN | 24 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/23 5:13:50 PM | SILVER | DOWN | 69 sec | — | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
