# 15-Minute 1¢ Study

*Updated Tue Nov 24, 9:30 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4865 finished bets | 1% | $211.90 | +40% | +4.36¢ | $89.05 / $122.85 |

*Expect about **84 buys a day** (~$12.60/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4615 | $110.00 | +22% |
| Volatility model ≥ 2%, hold to the close | 9062 | $40.30 | +4% |
| Momentum model ≥ 2%, hold to the close | 7540 | -$30.35 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 67018 | 66976 | 255 (0%) | 1.07% | -$4,536.15 (-56%) | Hold to the close: -$4,536.15 (-56%) |

*In play or awaiting result: 14. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 39823 | 4.5% | 0.4% (164) | -649% | ❌ Worse |
| Momentum model | 39823 | 4.4% | 0.4% (164) | -671% | ❌ Worse |
| Mean-reversion model | 39823 | 7.9% | 0.4% (164) | -787% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 39823 | 164 | -46% | -87% | -86% | -84% |
| Volatility model ≥ 2% | 9062 | 80 | +4% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 4865 | 53 | +40% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 2821 | 32 | +68% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 7540 | 59 | -4% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 4615 | 43 | +22% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 3012 | 28 | +34% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 16194 | 112 | -24% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11270 | 92 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7488 | 66 | +1% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 40029 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15905 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 11042 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 66976 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 255 | 0% | -$4,536.15 | -56% | — |
| Sell at 2¢ | 2736 | 4% | -$7,100.79 | -88% | 47 sec |
| Sell at 3¢ | 1842 | 3% | -$7,093.77 | -88% | 48 sec |
| Sell at 5¢ | 1252 | 2% | -$6,970.35 | -86% | 62 sec |
| Sell at 10¢ | 767 | 1% | -$6,695.38 | -83% | 65 sec |
| Sell at 25¢ | 413 | 1% | -$6,179.12 | -76% | 79 sec |
| Sell at 50¢ | 265 | 0% | -$5,575.40 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3442 | 17 | 11% | 4% | -53% | -81% | -83% |
| 2–5 min | 21677 | 116 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 16752 | 57 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 25092 | 65 | 1% | 0% | -62% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4476 | 19 | 5% | 2% | -43% | -88% | -87% |
| HYPE | 4469 | 16 | 5% | 2% | -54% | -89% | -88% |
| SOL | 4464 | 20 | 4% | 2% | -42% | -86% | -86% |
| BNB | 4458 | 22 | 5% | 2% | -37% | -86% | -85% |
| DOGE | 4454 | 12 | 4% | 2% | -65% | -89% | -89% |
| ETH | 4449 | 19 | 7% | 3% | -46% | -82% | -82% |
| BTC | 4427 | 24 | 5% | 2% | -25% | -86% | -87% |
| NEAR | 4421 | 18 | 5% | 2% | -47% | -85% | -86% |
| XRP | 4411 | 16 | 4% | 2% | -54% | -89% | -88% |
| GOLD | 2355 | 8 | 5% | 2% | -58% | -82% | -84% |
| WTI | 2343 | 8 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 2295 | 9 | 5% | 2% | -53% | -83% | -84% |
| PLATINUM | 2085 | 5 | 3% | 1% | -78% | -95% | -95% |
| EURUSD | 2044 | 7 | 3% | 1% | -68% | -91% | -90% |
| GBPUSD | 1978 | 8 | 2% | 1% | -62% | -96% | -96% |
| COPPER | 1976 | 6 | 2% | 1% | -72% | -78% | -78% |
| USDJPY | 1942 | 6 | 2% | 1% | -71% | -96% | -96% |
| NATGAS | 1934 | 10 | 2% | 1% | -52% | -77% | -77% |
| PALLADIUM | 1876 | 4 | 1% | 1% | -80% | -93% | -93% |
| AUDUSD | 1496 | 7 | 2% | 1% | -56% | -90% | -90% |
| USDCAD | 1414 | 1 | 3% | 1% | -93% | -96% | -96% |
| BRENT | 1041 | 1 | 2% | 1% | -91% | -97% | -97% |
| 10YRRATE | 538 | 2 | 3% | 1% | -65% | -77% | -75% |
| 2YRRATE | 501 | 4 | 4% | 2% | -25% | -56% | -55% |
| 30YRRATE | 498 | 0 | 3% | 1% | -100% | -95% | -93% |
| 5YRRATE | 488 | 2 | 4% | 2% | -62% | -94% | -95% |
| INX | 124 | 1 | 2% | 1% | -25% | -97% | -98% |
| USDMXN | 19 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 34253 | 131 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 32723 | 124 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5832 | 25 | 2% | 1% | -21% | -79% | -78% |
| 0.05–0.1% | 6383 | 26 | 3% | 2% | -35% | -91% | -91% |
| 0.1–0.2% | 9960 | 36 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12606 | 56 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 5239 | 23 | 7% | 3% | -54% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16271 | 50 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 15699 | 81 | 4% | 2% | -41% | -85% | -85% |
| Afternoon (12–6pm) | 16634 | 73 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 18372 | 51 | 4% | 2% | -68% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,113 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/24 9:29:47 PM | COPPER | DOWN | 13 sec | — | 0¢ | In play | — |
| 11/24 9:29:47 PM | BTC | UP | 13 sec | -0.028% | 0¢ | ❌ Lost | -$0.15 |
| 11/24 9:29:47 PM | EURUSD | UP | 13 sec | — | 0¢ | In play | — |
| 11/24 9:29:34 PM | GOLD | DOWN | 25 sec | — | 1¢ | In play | — |
| 11/24 9:29:34 PM | BNB | UP | 25 sec | -0.105% | 0¢ | ❌ Lost | $0.00 |
| 11/24 9:29:17 PM | USDJPY | DOWN | 42 sec | — | 0¢ | In play | — |
| 11/24 9:29:17 PM | NATGAS | DOWN | 42 sec | — | 0¢ | In play | — |
| 11/24 9:29:01 PM | DOGE | DOWN | 58 sec | +0.114% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 9:29:01 PM | AUDUSD | UP | 58 sec | — | 0¢ | In play | — |
| 11/24 9:28:45 PM | ZEC | UP | 74 sec | -0.199% | 4¢ | ❌ Lost | -$0.15 |
| 11/24 9:28:43 PM | SOL | UP | 76 sec | -0.238% | 0¢ | ❌ Lost | $0.00 |
| 11/24 9:28:27 PM | HYPE | UP | 1.5 min | -0.288% | 0¢ | In play | — |
| 11/24 9:27:18 PM | NEAR | DOWN | 2.7 min | +0.392% | 1¢ | In play | — |
| 11/24 9:26:42 PM | XRP | DOWN | 3.3 min | +0.228% | 4¢ | ❌ Lost | -$0.15 |
| 11/24 9:14:52 PM | USDJPY | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 9:14:52 PM | COPPER | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 9:14:52 PM | BNB | DOWN | 7 sec | -0.050% | 0¢ | ❌ Lost | $0.00 |
| 11/24 9:14:52 PM | BRENT | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 9:14:36 PM | XRP | DOWN | 23 sec | +0.043% | 0¢ | ❌ Lost | $0.00 |
| 11/24 9:14:36 PM | HYPE | DOWN | 23 sec | +0.165% | 0¢ | ❌ Lost | $0.00 |
| 11/24 9:14:21 PM | ZEC | DOWN | 39 sec | +0.333% | 0¢ | ❌ Lost | $0.00 |
| 11/24 9:14:21 PM | WTI | DOWN | 39 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/24 9:14:21 PM | ETH | UP | 39 sec | -0.075% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 9:14:05 PM | DOGE | DOWN | 55 sec | +0.183% | 0¢ | ❌ Lost | $0.00 |
| 11/24 9:14:05 PM | BTC | UP | 55 sec | -0.148% | 0¢ | ❌ Lost | $0.00 |
| 11/24 9:14:05 PM | GBPUSD | DOWN | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 9:14:05 PM | NATGAS | DOWN | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 9:12:21 PM | USDCAD | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 9:10:17 PM | PLATINUM | UP | 4.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/24 8:59:57 PM | WTI | UP | 3 sec | — | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
