# 15-Minute 1¢ Study

*Updated Sat Oct 24, 4:11 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2558 finished bets | 1% | $102.05 | +35% | +3.99¢ | $42.05 / $60.00 |

*Expect about **98 buys a day** (~$14.68/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2362 | $74.70 | +29% |
| Volatility model ≥ 2%, hold to the close | 4734 | $22.10 | +4% |
| Momentum model ≥ 2%, hold to the close | 3937 | -$0.60 | -0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 30789 | 30781 | 119 (0%) | 1.07% | -$2,084.75 (-56%) | Hold to the close: -$2,084.75 (-56%) |

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
| Volatility model | 19574 | 4.6% | 0.4% (84) | -630% | ❌ Worse |
| Momentum model | 19574 | 4.6% | 0.4% (84) | -656% | ❌ Worse |
| Mean-reversion model | 19574 | 7.9% | 0.4% (84) | -762% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 19574 | 84 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4734 | 43 | +4% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 2558 | 28 | +35% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 1458 | 18 | +73% | -65% | -63% | -60% |
| Momentum model ≥ 2% | 3937 | 33 | -0% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2362 | 24 | +29% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 1548 | 16 | +42% | -69% | -68% | -63% |
| Mean-reversion model ≥ 2% | 7870 | 55 | -24% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5504 | 46 | -8% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3663 | 33 | +2% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 19774 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 7352 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3655 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 30781 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 119 | 0% | -$2,084.75 | -56% | — |
| Sell at 2¢ | 1148 | 4% | -$3,284.27 | -88% | 47 sec |
| Sell at 3¢ | 787 | 3% | -$3,275.82 | -87% | 48 sec |
| Sell at 5¢ | 552 | 2% | -$3,223.95 | -86% | 61 sec |
| Sell at 10¢ | 340 | 1% | -$3,095.35 | -83% | 64 sec |
| Sell at 25¢ | 187 | 1% | -$2,851.78 | -76% | 82 sec |
| Sell at 50¢ | 121 | 0% | -$2,570.00 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1318 | 7 | 11% | 4% | -49% | -80% | -82% |
| 2–5 min | 9829 | 54 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 7825 | 30 | 3% | 1% | -58% | -92% | -91% |
| Under 1 min | 11805 | 28 | 1% | 0% | -66% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2216 | 12 | 5% | 2% | -32% | -89% | -89% |
| HYPE | 2208 | 8 | 5% | 3% | -55% | -88% | -86% |
| BNB | 2206 | 12 | 5% | 2% | -33% | -83% | -82% |
| SOL | 2201 | 6 | 4% | 2% | -66% | -92% | -92% |
| ETH | 2198 | 11 | 6% | 3% | -40% | -86% | -85% |
| DOGE | 2192 | 4 | 4% | 2% | -77% | -90% | -90% |
| XRP | 2188 | 9 | 3% | 1% | -49% | -88% | -88% |
| NEAR | 2184 | 12 | 5% | 3% | -29% | -81% | -81% |
| BTC | 2181 | 12 | 5% | 2% | -26% | -88% | -89% |
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
| UP (bought YES) | 15565 | 65 | 4% | 2% | -52% | -87% | -86% |
| DOWN (bought NO) | 15216 | 54 | 4% | 2% | -59% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3286 | 18 | 2% | 1% | -8% | -79% | -79% |
| 0.05–0.1% | 3404 | 11 | 3% | 1% | -52% | -92% | -92% |
| 0.1–0.2% | 5096 | 19 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 5774 | 28 | 6% | 3% | -47% | -87% | -86% |
| Over 0.5% | 2210 | 10 | 7% | 3% | -53% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7673 | 32 | 4% | 2% | -53% | -85% | -84% |
| Morning (6am–12pm) | 7425 | 34 | 4% | 2% | -48% | -88% | -87% |
| Afternoon (12–6pm) | 7298 | 24 | 4% | 2% | -61% | -87% | -88% |
| Evening (6pm–12am) | 8385 | 29 | 3% | 2% | -60% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,650 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/24 3:59:07 AM | NEAR | DOWN | 52 sec | +0.196% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 3:57:08 AM | HYPE | DOWN | 2.9 min | +0.138% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 3:56:53 AM | SOL | DOWN | 3.1 min | +0.195% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 3:56:37 AM | XRP | DOWN | 3.4 min | +0.228% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 3:56:21 AM | BTC | DOWN | 3.6 min | +0.139% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 3:56:05 AM | BNB | DOWN | 3.9 min | +0.140% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 3:55:24 AM | ETH | DOWN | 4.6 min | +0.241% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 3:54:37 AM | DOGE | DOWN | 5.4 min | +0.308% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 3:54:05 AM | ZEC | DOWN | 5.9 min | +0.582% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 3:43:38 AM | HYPE | UP | 82 sec | -0.147% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 3:43:38 AM | ETH | UP | 82 sec | -0.129% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 3:43:22 AM | XRP | UP | 1.6 min | -0.267% | 0¢ | ❌ Lost | $0.00 |
| 10/24 3:43:22 AM | BTC | UP | 1.6 min | -0.121% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 3:43:22 AM | BNB | UP | 1.6 min | -0.159% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 3:42:51 AM | SOL | UP | 2.1 min | -0.243% | 0¢ | ❌ Lost | $0.00 |
| 10/24 3:42:51 AM | ZEC | UP | 2.1 min | -0.409% | 0¢ | ❌ Lost | $0.00 |
| 10/24 3:42:19 AM | DOGE | UP | 2.7 min | -0.293% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 3:39:31 AM | NEAR | UP | 5.5 min | -0.821% | 3¢ | ❌ Lost | -$0.15 |
| 10/24 3:28:36 AM | HYPE | UP | 84 sec | -0.089% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 3:27:49 AM | NEAR | UP | 2.2 min | -0.507% | 2¢ | ❌ Lost | -$0.15 |
| 10/24 3:26:46 AM | BTC | UP | 3.2 min | -0.132% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 3:26:30 AM | ETH | UP | 3.5 min | -0.174% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 3:25:58 AM | ZEC | UP | 4.0 min | -0.644% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 3:25:43 AM | XRP | UP | 4.3 min | -0.305% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 3:25:43 AM | SOL | UP | 4.3 min | -0.284% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 3:25:27 AM | BNB | UP | 4.5 min | -0.146% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 3:25:11 AM | DOGE | UP | 4.8 min | -0.321% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 3:14:49 AM | DOGE | UP | 11 sec | -0.066% | 0¢ | ❌ Lost | $0.00 |
| 10/24 3:13:44 AM | XRP | UP | 75 sec | -0.148% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 3:13:44 AM | BTC | UP | 75 sec | -0.088% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
