# 15-Minute 1¢ Study

*Updated Sun Nov 22, 8:06 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4765 finished bets | 1% | $221.50 | +43% | +4.65¢ | $80.90 / $140.60 |

*Expect about **85 buys a day** (~$12.80/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4516 | $119.15 | +25% |
| Volatility model ≥ 2%, hold to the close | 8889 | $58.90 | +6% |
| Momentum model ≥ 2%, hold to the close | 7405 | -$17.15 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 65017 | 64983 | 251 (0%) | 1.07% | -$4,355.00 (-55%) | Hold to the close: -$4,355.00 (-55%) |

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
| Volatility model | 38911 | 4.5% | 0.4% (163) | -636% | ❌ Worse |
| Momentum model | 38911 | 4.4% | 0.4% (163) | -659% | ❌ Worse |
| Mean-reversion model | 38911 | 7.8% | 0.4% (163) | -772% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 38911 | 163 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8889 | 80 | +6% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4765 | 53 | +43% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 2751 | 32 | +71% | -64% | -62% | -58% |
| Momentum model ≥ 2% | 7405 | 59 | -2% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4516 | 43 | +25% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2939 | 28 | +37% | -67% | -67% | -62% |
| Mean-reversion model ≥ 2% | 15837 | 111 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 11007 | 91 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7308 | 66 | +3% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 39117 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15347 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10519 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 64983 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 251 | 0% | -$4,355.00 | -55% | — |
| Sell at 2¢ | 2648 | 4% | -$6,886.52 | -88% | 47 sec |
| Sell at 3¢ | 1782 | 3% | -$6,880.02 | -87% | 48 sec |
| Sell at 5¢ | 1214 | 2% | -$6,757.90 | -86% | 61 sec |
| Sell at 10¢ | 740 | 1% | -$6,493.60 | -83% | 65 sec |
| Sell at 25¢ | 398 | 1% | -$5,991.62 | -76% | 80 sec |
| Sell at 50¢ | 259 | 0% | -$5,392.75 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3362 | 17 | 10% | 4% | -52% | -82% | -83% |
| 2–5 min | 21073 | 112 | 7% | 3% | -48% | -86% | -86% |
| 1–2 min | 16231 | 57 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 24304 | 65 | 1% | 0% | -61% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4373 | 19 | 5% | 2% | -42% | -88% | -87% |
| HYPE | 4367 | 16 | 5% | 2% | -53% | -89% | -88% |
| SOL | 4365 | 20 | 4% | 2% | -41% | -86% | -86% |
| BNB | 4355 | 22 | 5% | 2% | -36% | -86% | -85% |
| DOGE | 4352 | 11 | 4% | 2% | -68% | -90% | -89% |
| ETH | 4348 | 19 | 7% | 3% | -45% | -82% | -82% |
| BTC | 4325 | 24 | 5% | 2% | -24% | -86% | -87% |
| NEAR | 4322 | 18 | 5% | 2% | -45% | -85% | -86% |
| XRP | 4310 | 16 | 3% | 2% | -53% | -89% | -88% |
| GOLD | 2276 | 8 | 5% | 2% | -57% | -82% | -84% |
| WTI | 2264 | 7 | 4% | 1% | -62% | -91% | -92% |
| SILVER | 2221 | 9 | 5% | 2% | -51% | -83% | -83% |
| PLATINUM | 2021 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 1978 | 7 | 3% | 1% | -67% | -91% | -90% |
| GBPUSD | 1909 | 8 | 2% | 1% | -61% | -96% | -96% |
| COPPER | 1905 | 6 | 2% | 1% | -71% | -77% | -77% |
| NATGAS | 1869 | 10 | 2% | 1% | -50% | -76% | -76% |
| USDJPY | 1868 | 6 | 2% | 1% | -70% | -96% | -96% |
| PALLADIUM | 1815 | 4 | 1% | 1% | -79% | -93% | -93% |
| AUDUSD | 1420 | 6 | 2% | 1% | -61% | -90% | -90% |
| USDCAD | 1348 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 976 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 499 | 2 | 3% | 1% | -63% | -76% | -74% |
| 2YRRATE | 476 | 4 | 4% | 2% | -22% | -54% | -53% |
| 30YRRATE | 462 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 451 | 2 | 4% | 2% | -59% | -94% | -95% |
| INX | 108 | 1 | 2% | 1% | -14% | -97% | -98% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 33249 | 128 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 31734 | 123 | 4% | 2% | -55% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5730 | 25 | 2% | 1% | -20% | -78% | -78% |
| 0.05–0.1% | 6269 | 26 | 3% | 2% | -34% | -91% | -90% |
| 0.1–0.2% | 9730 | 36 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12248 | 55 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 5131 | 23 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15529 | 48 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 15586 | 81 | 4% | 2% | -41% | -85% | -85% |
| Afternoon (12–6pm) | 15984 | 71 | 4% | 2% | -47% | -87% | -87% |
| Evening (6pm–12am) | 17884 | 51 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,171 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/22 7:59:46 PM | SILVER | UP | 13 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/22 7:59:46 PM | XRP | DOWN | 13 sec | +0.011% | 0¢ | ❌ Lost | $0.00 |
| 11/22 7:59:30 PM | AUDUSD | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/22 7:59:14 PM | BTC | DOWN | 45 sec | +0.138% | 0¢ | ❌ Lost | $0.00 |
| 11/22 7:58:58 PM | HYPE | DOWN | 62 sec | +0.179% | 0¢ | ❌ Lost | $0.00 |
| 11/22 7:58:58 PM | WTI | DOWN | 62 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 11/22 7:58:58 PM | BRENT | DOWN | 62 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 11/22 7:58:58 PM | ZEC | DOWN | 62 sec | +0.418% | 0¢ | ❌ Lost | $0.00 |
| 11/22 7:58:42 PM | USDJPY | DOWN | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/22 7:58:42 PM | EURUSD | UP | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/22 7:58:42 PM | DOGE | DOWN | 78 sec | +0.140% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 7:58:10 PM | NEAR | DOWN | 1.8 min | +0.288% | 0¢ | ❌ Lost | -$0.15 |
| 11/22 7:58:10 PM | SOL | DOWN | 1.8 min | +0.232% | 0¢ | ❌ Lost | -$0.15 |
| 11/22 7:57:55 PM | GBPUSD | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/22 7:57:55 PM | ETH | DOWN | 2.1 min | +0.214% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 7:57:55 PM | BNB | DOWN | 2.1 min | +0.125% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 7:57:39 PM | GOLD | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/22 7:57:39 PM | COPPER | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/22 7:57:23 PM | USDCAD | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/22 7:44:45 PM | USDJPY | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/22 7:44:45 PM | COPPER | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/22 7:44:29 PM | WTI | UP | 31 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/22 7:43:40 PM | GOLD | UP | 79 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/22 7:43:08 PM | SILVER | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/22 7:42:34 PM | NEAR | UP | 2.4 min | -0.791% | 0¢ | ❌ Lost | -$0.15 |
| 11/22 7:42:34 PM | BTC | UP | 2.4 min | -0.565% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 7:42:18 PM | XRP | UP | 2.7 min | -0.338% | 1¢ | ❌ Lost | -$0.15 |
| 11/22 7:42:03 PM | HYPE | UP | 3.0 min | -0.524% | 0¢ | ❌ Lost | $0.00 |
| 11/22 7:42:03 PM | DOGE | UP | 3.0 min | -0.408% | 0¢ | ❌ Lost | -$0.15 |
| 11/22 7:42:03 PM | ETH | UP | 3.0 min | -0.386% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
