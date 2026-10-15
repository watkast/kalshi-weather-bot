# 15-Minute 1¢ Study

*Updated Thu Oct 15, 2:44 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1477 finished bets | 1% | $88.35 | +54% | +5.98¢ | $32.95 / $55.40 |

*Expect about **87 buys a day** (~$13.00/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1385 | $59.85 | +40% |
| Momentum model ≥ 2%, hold to the close | 2305 | $12.85 | +5% |
| Volatility model ≥ 2%, hold to the close | 2652 | $1.60 | +0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 19009 | 18987 | 75 (0%) | 1.07% | -$1,252.35 (-54%) | Hold to the close: -$1,252.35 (-54%) |

*In play or awaiting result: 21. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 12295 | 4.5% | 0.4% (52) | -637% | ❌ Worse |
| Momentum model | 12295 | 4.4% | 0.4% (52) | -662% | ❌ Worse |
| Mean-reversion model | 12295 | 7.3% | 0.4% (52) | -757% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12295 | 52 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2652 | 23 | +0% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1477 | 18 | +54% | -73% | -71% | -67% |
| Volatility model ≥ 10% | 880 | 11 | +78% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 2305 | 20 | +5% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1385 | 15 | +40% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 929 | 10 | +51% | -70% | -70% | -65% |
| Mean-reversion model ≥ 2% | 4542 | 32 | -23% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 3107 | 25 | -11% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2038 | 14 | -21% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12493 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4664 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1830 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 18987 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 75 | 0% | -$1,252.35 | -54% | — |
| Sell at 2¢ | 665 | 4% | -$2,073.45 | -90% | 34 sec |
| Sell at 3¢ | 446 | 2% | -$2,072.41 | -90% | 46 sec |
| Sell at 5¢ | 326 | 2% | -$2,034.45 | -88% | 49 sec |
| Sell at 10¢ | 206 | 1% | -$1,948.49 | -85% | 63 sec |
| Sell at 25¢ | 120 | 1% | -$1,779.15 | -77% | 78 sec |
| Sell at 50¢ | 79 | 0% | -$1,573.10 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 598 | 5 | 10% | 3% | -20% | -82% | -87% |
| 2–5 min | 6137 | 35 | 7% | 3% | -44% | -88% | -88% |
| 1–2 min | 4947 | 19 | 3% | 2% | -58% | -94% | -93% |
| Under 1 min | 7301 | 16 | 1% | 0% | -68% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1402 | 11 | 5% | 3% | -2% | -89% | -89% |
| HYPE | 1395 | 4 | 4% | 2% | -65% | -90% | -89% |
| ETH | 1392 | 8 | 5% | 3% | -30% | -88% | -87% |
| BNB | 1392 | 5 | 4% | 2% | -56% | -90% | -89% |
| DOGE | 1390 | 2 | 4% | 2% | -82% | -91% | -90% |
| SOL | 1387 | 2 | 3% | 1% | -82% | -94% | -93% |
| BTC | 1379 | 7 | 5% | 2% | -32% | -88% | -91% |
| XRP | 1379 | 7 | 3% | 1% | -37% | -85% | -86% |
| NEAR | 1377 | 8 | 5% | 2% | -24% | -78% | -78% |
| GOLD | 761 | 1 | 4% | 1% | -85% | -92% | -94% |
| SILVER | 741 | 4 | 3% | 1% | -37% | -78% | -78% |
| WTI | 712 | 3 | 3% | 1% | -51% | -94% | -96% |
| COPPER | 656 | 1 | 2% | 2% | -86% | -97% | -96% |
| PLATINUM | 632 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 582 | 1 | 1% | 0% | -84% | -98% | -98% |
| NATGAS | 580 | 4 | 2% | 2% | -36% | -96% | -95% |
| EURUSD | 570 | 3 | 2% | 1% | -51% | -79% | -79% |
| GBPUSD | 533 | 1 | 2% | 1% | -82% | -97% | -97% |
| USDJPY | 489 | 3 | 1% | 1% | -43% | -99% | -98% |
| AUDUSD | 124 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 114 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9608 | 38 | 3% | 2% | -54% | -89% | -88% |
| DOWN (bought NO) | 9379 | 37 | 4% | 2% | -54% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2120 | 11 | 2% | 1% | -13% | -78% | -78% |
| 0.05–0.1% | 2178 | 7 | 3% | 1% | -53% | -92% | -91% |
| 0.1–0.2% | 3153 | 10 | 4% | 2% | -61% | -90% | -90% |
| 0.2–0.5% | 3619 | 20 | 6% | 3% | -39% | -88% | -88% |
| Over 0.5% | 1420 | 6 | 6% | 2% | -56% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4767 | 20 | 4% | 2% | -52% | -87% | -88% |
| Morning (6am–12pm) | 4329 | 23 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 4482 | 16 | 3% | 1% | -58% | -87% | -88% |
| Evening (6pm–12am) | 5409 | 16 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,506 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/15 12:59:58 AM | GOLD | DOWN | 1 sec | — | 0¢ | In play | — |
| 10/15 12:59:58 AM | USDJPY | UP | 1 sec | — | 0¢ | In play | — |
| 10/15 12:59:58 AM | GBPUSD | DOWN | 1 sec | — | 0¢ | In play | — |
| 10/15 12:59:58 AM | PLATINUM | UP | 1 sec | — | 0¢ | In play | — |
| 10/15 12:59:26 AM | BTC | UP | 33 sec | -0.062% | 1¢ | In play | — |
| 10/15 12:59:26 AM | NEAR | DOWN | 33 sec | +0.095% | 0¢ | In play | — |
| 10/15 12:58:54 AM | COPPER | UP | 65 sec | — | 0¢ | In play | — |
| 10/15 12:58:54 AM | AUDUSD | UP | 65 sec | — | 0¢ | In play | — |
| 10/15 12:58:38 AM | ETH | UP | 81 sec | -0.164% | 0¢ | In play | — |
| 10/15 12:57:18 AM | ZEC | DOWN | 2.7 min | +0.439% | 1¢ | In play | — |
| 10/15 12:56:31 AM | SOL | UP | 3.5 min | -0.284% | 2¢ | In play | — |
| 10/15 12:56:31 AM | XRP | UP | 3.5 min | -0.337% | 7¢ | In play | — |
| 10/15 12:56:15 AM | DOGE | UP | 3.8 min | -0.331% | 1¢ | In play | — |
| 10/15 12:56:15 AM | BNB | UP | 3.8 min | -0.180% | 6¢ | In play | — |
| 10/15 12:55:27 AM | HYPE | UP | 4.5 min | -0.435% | 0¢ | In play | — |
| 10/15 12:44:50 AM | USDCAD | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:44:50 AM | PLATINUM | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:44:50 AM | NATGAS | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:44:34 AM | GBPUSD | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:44:18 AM | ETH | UP | 42 sec | -0.182% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:44:18 AM | ZEC | UP | 42 sec | -0.259% | 0¢ | ❌ Lost | $0.00 |
| 10/15 12:44:01 AM | USDJPY | DOWN | 58 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:43:45 AM | GOLD | UP | 74 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:43:29 AM | BTC | DOWN | 1.5 min | +0.101% | 39¢ | ❌ Lost | -$0.15 |
| 10/15 12:43:29 AM | PALLADIUM | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:43:13 AM | SOL | DOWN | 1.8 min | +0.198% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:43:13 AM | NEAR | DOWN | 1.8 min | +0.424% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:42:55 AM | HYPE | DOWN | 2.1 min | +0.307% | 3¢ | ❌ Lost | -$0.15 |
| 10/15 12:42:39 AM | BNB | DOWN | 2.4 min | +0.091% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:42:23 AM | AUDUSD | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
