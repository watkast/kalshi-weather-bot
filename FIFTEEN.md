# 15-Minute 1¢ Study

*Updated Tue Nov 24, 11:09 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4838 finished bets | 1% | $213.70 | +40% | +4.42¢ | $76.25 / $137.45 |

*Expect about **84 buys a day** (~$12.63/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4585 | $112.10 | +23% |
| Volatility model ≥ 2%, hold to the close | 9010 | $45.25 | +4% |
| Momentum model ≥ 2%, hold to the close | 7502 | -$27.50 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 66492 | 66458 | 255 (0%) | 1.07% | -$4,478.40 (-56%) | Hold to the close: -$4,478.40 (-56%) |

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
| Volatility model | 39575 | 4.5% | 0.4% (164) | -642% | ❌ Worse |
| Momentum model | 39575 | 4.4% | 0.4% (164) | -665% | ❌ Worse |
| Mean-reversion model | 39575 | 7.9% | 0.4% (164) | -780% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 39575 | 164 | -46% | -87% | -86% | -84% |
| Volatility model ≥ 2% | 9010 | 80 | +4% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 4838 | 53 | +40% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 2803 | 32 | +68% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 7502 | 59 | -3% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 4585 | 43 | +23% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 2990 | 28 | +35% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 16101 | 112 | -23% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11204 | 92 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7446 | 66 | +1% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 39781 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15769 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10908 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 66458 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 255 | 0% | -$4,478.40 | -56% | — |
| Sell at 2¢ | 2724 | 4% | -$7,046.16 | -88% | 47 sec |
| Sell at 3¢ | 1832 | 3% | -$7,039.92 | -87% | 48 sec |
| Sell at 5¢ | 1248 | 2% | -$6,915.20 | -86% | 62 sec |
| Sell at 10¢ | 765 | 1% | -$6,640.25 | -83% | 65 sec |
| Sell at 25¢ | 411 | 1% | -$6,127.99 | -76% | 79 sec |
| Sell at 50¢ | 264 | 0% | -$5,524.40 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3437 | 17 | 11% | 4% | -53% | -81% | -83% |
| 2–5 min | 21537 | 116 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 16606 | 57 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 24865 | 65 | 1% | 0% | -62% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4447 | 19 | 5% | 2% | -43% | -88% | -87% |
| HYPE | 4441 | 16 | 5% | 2% | -54% | -89% | -88% |
| SOL | 4439 | 20 | 4% | 2% | -42% | -86% | -86% |
| BNB | 4430 | 22 | 5% | 2% | -37% | -86% | -85% |
| DOGE | 4426 | 12 | 4% | 2% | -65% | -89% | -89% |
| ETH | 4421 | 19 | 7% | 3% | -46% | -82% | -82% |
| BTC | 4400 | 24 | 6% | 2% | -25% | -86% | -87% |
| NEAR | 4394 | 18 | 5% | 2% | -46% | -85% | -86% |
| XRP | 4383 | 16 | 4% | 2% | -53% | -89% | -88% |
| GOLD | 2336 | 8 | 5% | 2% | -58% | -82% | -84% |
| WTI | 2322 | 8 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 2279 | 9 | 5% | 2% | -53% | -83% | -84% |
| PLATINUM | 2070 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 2029 | 7 | 3% | 1% | -68% | -91% | -90% |
| COPPER | 1961 | 6 | 2% | 1% | -71% | -78% | -78% |
| GBPUSD | 1959 | 8 | 2% | 1% | -62% | -96% | -96% |
| USDJPY | 1925 | 6 | 2% | 1% | -71% | -96% | -96% |
| NATGAS | 1919 | 10 | 2% | 1% | -51% | -77% | -76% |
| PALLADIUM | 1860 | 4 | 1% | 1% | -80% | -93% | -93% |
| AUDUSD | 1478 | 7 | 2% | 1% | -56% | -90% | -90% |
| USDCAD | 1396 | 1 | 3% | 1% | -93% | -96% | -96% |
| BRENT | 1022 | 1 | 2% | 1% | -91% | -96% | -97% |
| 10YRRATE | 529 | 2 | 3% | 1% | -65% | -76% | -75% |
| 2YRRATE | 497 | 4 | 4% | 2% | -25% | -56% | -55% |
| 30YRRATE | 487 | 0 | 3% | 1% | -100% | -95% | -93% |
| 5YRRATE | 479 | 2 | 4% | 1% | -61% | -94% | -96% |
| INX | 114 | 1 | 2% | 1% | -18% | -97% | -98% |
| USDMXN | 15 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 33996 | 131 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 32462 | 124 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5804 | 25 | 2% | 1% | -21% | -78% | -78% |
| 0.05–0.1% | 6339 | 26 | 3% | 2% | -35% | -91% | -90% |
| 0.1–0.2% | 9884 | 36 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12524 | 56 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 5221 | 23 | 7% | 3% | -54% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16271 | 50 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 15626 | 81 | 4% | 2% | -41% | -85% | -85% |
| Afternoon (12–6pm) | 16344 | 73 | 4% | 2% | -47% | -87% | -87% |
| Evening (6pm–12am) | 18217 | 51 | 4% | 2% | -68% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,125 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/24 10:59:56 AM | WTI | UP | 3 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/24 10:59:56 AM | BRENT | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 10:59:56 AM | 2YRRATE | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 10:59:56 AM | AUDUSD | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 10:59:33 AM | COPPER | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 10:59:33 AM | INX | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 10:59:33 AM | USDJPY | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 10:59:33 AM | 5YRRATE | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 10:59:33 AM | HYPE | UP | 27 sec | -0.034% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 10:59:17 AM | DOGE | DOWN | 43 sec | +0.139% | 0¢ | ❌ Lost | $0.00 |
| 11/24 10:59:17 AM | 30YRRATE | UP | 43 sec | — | 3¢ | ❌ Lost | -$0.15 |
| 11/24 10:59:17 AM | PALLADIUM | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 10:59:17 AM | ETH | DOWN | 43 sec | +0.056% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 10:59:17 AM | 10YRRATE | UP | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 10:59:17 AM | BTC | DOWN | 43 sec | +0.082% | 0¢ | ❌ Lost | $0.00 |
| 11/24 10:59:01 AM | SOL | DOWN | 59 sec | +0.196% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 10:59:01 AM | BNB | DOWN | 59 sec | +0.015% | 0¢ | ❌ Lost | -$0.15 |
| 11/24 10:58:46 AM | XRP | DOWN | 73 sec | +0.163% | 0¢ | ❌ Lost | $0.00 |
| 11/24 10:58:46 AM | ZEC | DOWN | 73 sec | +0.777% | 0¢ | ❌ Lost | $0.00 |
| 11/24 10:58:26 AM | USDCAD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 10:57:37 AM | EURUSD | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 10:57:37 AM | GBPUSD | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 10:57:37 AM | NATGAS | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 10:44:42 AM | ZEC | DOWN | 17 sec | +0.114% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 10:44:42 AM | SOL | DOWN | 17 sec | +0.045% | 0¢ | ❌ Lost | $0.00 |
| 11/24 10:44:26 AM | PLATINUM | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 10:44:26 AM | GOLD | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 10:44:26 AM | 2YRRATE | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 10:44:26 AM | HYPE | UP | 33 sec | -0.336% | 0¢ | ❌ Lost | $0.00 |
| 11/24 10:44:10 AM | INX | DOWN | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
