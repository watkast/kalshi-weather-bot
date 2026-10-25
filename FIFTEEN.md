# 15-Minute 1¢ Study

*Updated Sun Oct 25, 12:14 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2673 finished bets | 1% | $88.25 | +29% | +3.30¢ | $36.05 / $52.20 |

*Expect about **97 buys a day** (~$14.61/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2462 | $63.45 | +23% |
| Volatility model ≥ 2%, hold to the close | 4940 | -$4.00 | -1% |
| Momentum model ≥ 2%, hold to the close | 4111 | -$21.00 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 31609 | 31592 | 120 (0%) | 1.07% | -$2,159.40 (-56%) | Hold to the close: -$2,159.40 (-56%) |

*In play or awaiting result: 16. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 20385 | 4.6% | 0.4% (85) | -645% | ❌ Worse |
| Momentum model | 20385 | 4.5% | 0.4% (85) | -669% | ❌ Worse |
| Mean-reversion model | 20385 | 7.9% | 0.4% (85) | -782% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 20385 | 85 | -48% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 4940 | 43 | -1% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 2673 | 28 | +29% | -74% | -73% | -70% |
| Volatility model ≥ 10% | 1512 | 18 | +67% | -66% | -64% | -61% |
| Momentum model ≥ 2% | 4111 | 33 | -4% | -80% | -80% | -76% |
| Momentum model ≥ 5% | 2462 | 24 | +23% | -76% | -76% | -72% |
| Momentum model ≥ 10% | 1607 | 16 | +37% | -70% | -69% | -65% |
| Mean-reversion model ≥ 2% | 8228 | 56 | -26% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 5762 | 47 | -10% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 3839 | 33 | -3% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 20585 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7352 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3655 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 31592 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 120 | 0% | -$2,159.40 | -56% | — |
| Sell at 2¢ | 1167 | 4% | -$3,367.98 | -88% | 47 sec |
| Sell at 3¢ | 799 | 3% | -$3,359.79 | -88% | 48 sec |
| Sell at 5¢ | 559 | 2% | -$3,308.05 | -86% | 61 sec |
| Sell at 10¢ | 345 | 1% | -$3,177.45 | -83% | 64 sec |
| Sell at 25¢ | 189 | 1% | -$2,933.81 | -76% | 82 sec |
| Sell at 50¢ | 122 | 0% | -$2,651.90 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1392 | 7 | 11% | 4% | -52% | -81% | -83% |
| 2–5 min | 10120 | 55 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 7998 | 30 | 3% | 1% | -59% | -92% | -91% |
| Under 1 min | 12078 | 28 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2307 | 12 | 5% | 2% | -34% | -89% | -89% |
| HYPE | 2301 | 8 | 5% | 3% | -57% | -89% | -87% |
| BNB | 2295 | 13 | 5% | 2% | -30% | -84% | -83% |
| SOL | 2292 | 6 | 3% | 2% | -68% | -92% | -92% |
| ETH | 2288 | 11 | 6% | 3% | -42% | -86% | -86% |
| DOGE | 2282 | 4 | 4% | 2% | -78% | -91% | -90% |
| XRP | 2277 | 9 | 3% | 1% | -51% | -88% | -88% |
| NEAR | 2276 | 12 | 5% | 2% | -31% | -82% | -81% |
| BTC | 2267 | 12 | 5% | 2% | -29% | -88% | -89% |
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
| UP (bought YES) | 15980 | 66 | 4% | 2% | -52% | -87% | -87% |
| DOWN (bought NO) | 15612 | 54 | 4% | 1% | -60% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3441 | 18 | 2% | 1% | -12% | -80% | -79% |
| 0.05–0.1% | 3539 | 11 | 3% | 1% | -54% | -92% | -92% |
| 0.1–0.2% | 5319 | 20 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 5999 | 28 | 6% | 3% | -49% | -87% | -86% |
| Over 0.5% | 2283 | 10 | 7% | 3% | -55% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7904 | 32 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 7781 | 35 | 4% | 2% | -49% | -88% | -87% |
| Afternoon (12–6pm) | 7332 | 24 | 4% | 2% | -61% | -87% | -88% |
| Evening (6pm–12am) | 8575 | 29 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,799 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/25 12:12:28 PM | BTC | UP | 2.5 min | -0.147% | — | In play | — |
| 10/25 12:11:56 PM | HYPE | UP | 3.0 min | -0.226% | — | In play | — |
| 10/25 12:11:40 PM | ETH | UP | 3.3 min | -0.151% | — | In play | — |
| 10/25 12:11:40 PM | SOL | UP | 3.3 min | -0.182% | — | In play | — |
| 10/25 12:11:40 PM | ZEC | UP | 3.3 min | -0.387% | — | In play | — |
| 10/25 12:11:40 PM | BNB | UP | 3.3 min | -0.167% | — | In play | — |
| 10/25 12:10:52 PM | DOGE | UP | 4.1 min | -0.235% | — | In play | — |
| 10/25 12:10:37 PM | NEAR | UP | 4.4 min | -0.721% | — | In play | — |
| 10/25 12:10:05 PM | XRP | UP | 4.9 min | -0.307% | — | In play | — |
| 10/25 11:59:47 AM | XRP | UP | 13 sec | -0.031% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 11:59:47 AM | DOGE | UP | 13 sec | -0.018% | 0¢ | ❌ Lost | $0.00 |
| 10/25 11:59:47 AM | BTC | UP | 13 sec | -0.025% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 11:59:47 AM | HYPE | UP | 13 sec | -0.009% | 0¢ | ❌ Lost | $0.00 |
| 10/25 11:59:31 AM | ETH | UP | 29 sec | -0.028% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 11:59:15 AM | NEAR | UP | 45 sec | -0.317% | 0¢ | ❌ Lost | $0.00 |
| 10/25 11:58:43 AM | ZEC | UP | 77 sec | -0.329% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 11:57:07 AM | BNB | DOWN | 2.9 min | +0.093% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 11:44:40 AM | XRP | DOWN | 20 sec | +0.023% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 11:44:40 AM | BNB | DOWN | 20 sec | +0.024% | 0¢ | ❌ Lost | $0.00 |
| 10/25 11:44:40 AM | NEAR | DOWN | 20 sec | +0.032% | 0¢ | ❌ Lost | $0.00 |
| 10/25 11:44:08 AM | DOGE | DOWN | 52 sec | +0.094% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 11:44:08 AM | HYPE | DOWN | 52 sec | +0.111% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 11:43:52 AM | ETH | DOWN | 67 sec | +0.075% | 2¢ | ❌ Lost | -$0.15 |
| 10/25 11:43:52 AM | BTC | DOWN | 67 sec | +0.067% | 0¢ | ❌ Lost | $0.00 |
| 10/25 11:43:12 AM | SOL | DOWN | 1.8 min | +0.140% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 11:42:09 AM | ZEC | DOWN | 2.9 min | +0.509% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 11:29:38 AM | BNB | DOWN | 22 sec | -0.015% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 11:29:22 AM | DOGE | DOWN | 38 sec | +0.040% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 11:29:22 AM | XRP | DOWN | 38 sec | +0.008% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 11:29:22 AM | HYPE | DOWN | 38 sec | +0.096% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
