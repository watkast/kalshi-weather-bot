# 15-Minute 1¢ Study

*Updated Mon Nov 23, 3:15 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4783 finished bets | 1% | $219.70 | +42% | +4.59¢ | $79.70 / $140.00 |

*Expect about **85 buys a day** (~$12.78/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4538 | $116.60 | +24% |
| Volatility model ≥ 2%, hold to the close | 8918 | $55.75 | +5% |
| Momentum model ≥ 2%, hold to the close | 7438 | -$20.90 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 65379 | 65323 | 252 (0%) | 1.07% | -$4,381.65 (-55%) | Hold to the close: -$4,381.65 (-55%) |

*In play or awaiting result: 28. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 39065 | 4.5% | 0.4% (163) | -638% | ❌ Worse |
| Momentum model | 39065 | 4.4% | 0.4% (163) | -661% | ❌ Worse |
| Mean-reversion model | 39065 | 7.9% | 0.4% (163) | -775% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 39065 | 163 | -46% | -87% | -86% | -84% |
| Volatility model ≥ 2% | 8918 | 80 | +5% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4783 | 53 | +42% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 2767 | 32 | +70% | -64% | -62% | -59% |
| Momentum model ≥ 2% | 7438 | 59 | -2% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4538 | 43 | +24% | -75% | -74% | -71% |
| Momentum model ≥ 10% | 2954 | 28 | +36% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 15901 | 111 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 11063 | 91 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7352 | 66 | +3% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 39271 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15443 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10609 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 65323 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 252 | 0% | -$4,381.65 | -55% | — |
| Sell at 2¢ | 2664 | 4% | -$6,923.01 | -88% | 47 sec |
| Sell at 3¢ | 1796 | 3% | -$6,915.21 | -87% | 48 sec |
| Sell at 5¢ | 1225 | 2% | -$6,791.40 | -86% | 62 sec |
| Sell at 10¢ | 748 | 1% | -$6,523.77 | -82% | 65 sec |
| Sell at 25¢ | 401 | 1% | -$6,022.34 | -76% | 80 sec |
| Sell at 50¢ | 259 | 0% | -$5,419.40 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3387 | 17 | 11% | 4% | -52% | -81% | -83% |
| 2–5 min | 21169 | 113 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 16325 | 57 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 24429 | 65 | 1% | 0% | -61% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4391 | 19 | 5% | 2% | -42% | -88% | -87% |
| HYPE | 4384 | 16 | 5% | 2% | -53% | -89% | -88% |
| SOL | 4381 | 20 | 4% | 2% | -41% | -86% | -86% |
| BNB | 4373 | 22 | 5% | 2% | -36% | -86% | -85% |
| DOGE | 4368 | 11 | 4% | 2% | -68% | -90% | -89% |
| ETH | 4365 | 19 | 7% | 3% | -45% | -82% | -82% |
| BTC | 4343 | 24 | 5% | 2% | -24% | -86% | -87% |
| NEAR | 4338 | 18 | 5% | 2% | -46% | -85% | -86% |
| XRP | 4328 | 16 | 3% | 2% | -53% | -89% | -88% |
| GOLD | 2290 | 8 | 5% | 2% | -57% | -82% | -84% |
| WTI | 2275 | 8 | 4% | 1% | -57% | -91% | -92% |
| SILVER | 2236 | 9 | 5% | 2% | -52% | -83% | -84% |
| PLATINUM | 2032 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 1992 | 7 | 3% | 1% | -67% | -91% | -90% |
| GBPUSD | 1923 | 8 | 2% | 1% | -61% | -96% | -96% |
| COPPER | 1918 | 6 | 2% | 1% | -71% | -77% | -77% |
| NATGAS | 1881 | 10 | 2% | 1% | -50% | -77% | -76% |
| USDJPY | 1880 | 6 | 2% | 1% | -70% | -96% | -96% |
| PALLADIUM | 1826 | 4 | 1% | 1% | -80% | -93% | -93% |
| AUDUSD | 1434 | 6 | 2% | 1% | -61% | -90% | -90% |
| USDCAD | 1359 | 1 | 3% | 1% | -93% | -96% | -96% |
| BRENT | 985 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 504 | 2 | 3% | 1% | -63% | -76% | -74% |
| 2YRRATE | 480 | 4 | 4% | 2% | -22% | -55% | -54% |
| 30YRRATE | 469 | 0 | 3% | 1% | -100% | -96% | -93% |
| 5YRRATE | 456 | 2 | 4% | 2% | -59% | -94% | -95% |
| INX | 108 | 1 | 2% | 1% | -14% | -97% | -98% |
| USDMXN | 4 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 33408 | 129 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 31915 | 123 | 4% | 2% | -55% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5754 | 25 | 2% | 1% | -21% | -78% | -78% |
| 0.05–0.1% | 6287 | 26 | 3% | 2% | -34% | -91% | -90% |
| 0.1–0.2% | 9767 | 36 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12299 | 55 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 5155 | 23 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15741 | 49 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 15586 | 81 | 4% | 2% | -41% | -85% | -85% |
| Afternoon (12–6pm) | 15984 | 71 | 4% | 2% | -47% | -87% | -87% |
| Evening (6pm–12am) | 18012 | 51 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,160 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/23 3:14:52 AM | GBPUSD | UP | 7 sec | — | 0¢ | In play | — |
| 11/23 3:14:52 AM | ETH | UP | 7 sec | -0.033% | 0¢ | In play | — |
| 11/23 3:14:36 AM | AUDUSD | DOWN | 23 sec | — | 2¢ | In play | — |
| 11/23 3:14:36 AM | PALLADIUM | DOWN | 23 sec | — | 0¢ | In play | — |
| 11/23 3:14:36 AM | USDCAD | DOWN | 23 sec | — | 0¢ | In play | — |
| 11/23 3:14:36 AM | USDJPY | DOWN | 23 sec | — | 0¢ | In play | — |
| 11/23 3:14:20 AM | 10YRRATE | UP | 40 sec | — | 0¢ | In play | — |
| 11/23 3:14:20 AM | BRENT | UP | 40 sec | — | 33¢ | In play | — |
| 11/23 3:14:20 AM | SILVER | DOWN | 40 sec | — | 1¢ | In play | — |
| 11/23 3:14:20 AM | 30YRRATE | UP | 40 sec | — | 0¢ | In play | — |
| 11/23 3:14:03 AM | WTI | UP | 56 sec | — | 33¢ | In play | — |
| 11/23 3:14:03 AM | NEAR | DOWN | 56 sec | +0.084% | 0¢ | In play | — |
| 11/23 3:14:03 AM | DOGE | UP | 56 sec | -0.162% | 0¢ | In play | — |
| 11/23 3:14:03 AM | NATGAS | DOWN | 56 sec | — | 0¢ | In play | — |
| 11/23 3:13:47 AM | BTC | UP | 72 sec | -0.146% | 34¢ | In play | — |
| 11/23 3:13:47 AM | PLATINUM | DOWN | 72 sec | — | 0¢ | In play | — |
| 11/23 3:13:31 AM | COPPER | DOWN | 88 sec | — | 0¢ | In play | — |
| 11/23 3:13:31 AM | BNB | UP | 88 sec | -0.178% | 1¢ | In play | — |
| 11/23 3:13:31 AM | ZEC | UP | 88 sec | -0.470% | 13¢ | ❌ Lost | $0.00 |
| 11/23 3:13:31 AM | SOL | UP | 88 sec | -0.227% | 21¢ | In play | — |
| 11/23 3:13:15 AM | HYPE | UP | 1.8 min | -0.270% | 0¢ | In play | — |
| 11/23 3:12:24 AM | XRP | DOWN | 2.6 min | +0.224% | 3¢ | In play | — |
| 11/23 3:10:47 AM | GOLD | DOWN | 4.2 min | — | 1¢ | In play | — |
| 11/23 2:59:57 AM | BRENT | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 2:59:57 AM | DOGE | DOWN | 2 sec | -0.005% | 0¢ | ❌ Lost | $0.00 |
| 11/23 2:59:41 AM | XRP | DOWN | 18 sec | +0.021% | 0¢ | ❌ Lost | $0.00 |
| 11/23 2:59:41 AM | HYPE | DOWN | 18 sec | +0.090% | 0¢ | ❌ Lost | $0.00 |
| 11/23 2:59:10 AM | GBPUSD | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 2:59:10 AM | GOLD | UP | 49 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/23 2:59:10 AM | EURUSD | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
