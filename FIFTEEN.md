# 15-Minute 1¢ Study

*Updated Thu Oct 15, 5:58 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1492 finished bets | 1% | $86.85 | +53% | +5.82¢ | $31.75 / $55.10 |

*Expect about **87 buys a day** (~$13.00/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1397 | $58.50 | +39% |
| Momentum model ≥ 2%, hold to the close | 2326 | $10.60 | +4% |
| Volatility model ≥ 2%, hold to the close | 2691 | -$3.20 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 19191 | 19177 | 75 (0%) | 1.07% | -$1,276.50 (-55%) | Hold to the close: -$1,276.50 (-55%) |

*In play or awaiting result: 13. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 12399 | 4.5% | 0.4% (52) | -646% | ❌ Worse |
| Momentum model | 12399 | 4.4% | 0.4% (52) | -669% | ❌ Worse |
| Mean-reversion model | 12399 | 7.4% | 0.4% (52) | -768% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12399 | 52 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2691 | 23 | -1% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 1492 | 18 | +53% | -73% | -71% | -67% |
| Volatility model ≥ 10% | 888 | 11 | +76% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 2326 | 20 | +4% | -79% | -80% | -77% |
| Momentum model ≥ 5% | 1397 | 15 | +39% | -76% | -76% | -72% |
| Momentum model ≥ 10% | 939 | 10 | +49% | -70% | -70% | -65% |
| Mean-reversion model ≥ 2% | 4602 | 32 | -24% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3152 | 25 | -12% | -82% | -81% | -78% |
| Mean-reversion model ≥ 10% | 2071 | 14 | -22% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12597 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4714 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1866 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 19177 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 75 | 0% | -$1,276.50 | -55% | — |
| Sell at 2¢ | 680 | 4% | -$2,093.70 | -90% | 36 sec |
| Sell at 3¢ | 458 | 2% | -$2,091.88 | -90% | 47 sec |
| Sell at 5¢ | 334 | 2% | -$2,053.40 | -88% | 50 sec |
| Sell at 10¢ | 209 | 1% | -$1,968.71 | -85% | 63 sec |
| Sell at 25¢ | 121 | 1% | -$1,799.99 | -77% | 79 sec |
| Sell at 50¢ | 79 | 0% | -$1,597.25 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 613 | 5 | 11% | 3% | -22% | -81% | -86% |
| 2–5 min | 6201 | 35 | 7% | 3% | -44% | -88% | -88% |
| 1–2 min | 4983 | 19 | 3% | 2% | -59% | -94% | -93% |
| Under 1 min | 7376 | 16 | 1% | 0% | -69% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1414 | 11 | 5% | 3% | -3% | -89% | -89% |
| HYPE | 1407 | 4 | 4% | 2% | -65% | -90% | -89% |
| ETH | 1404 | 8 | 5% | 3% | -31% | -88% | -86% |
| BNB | 1403 | 5 | 5% | 2% | -56% | -90% | -89% |
| DOGE | 1402 | 2 | 4% | 2% | -82% | -91% | -90% |
| SOL | 1398 | 2 | 3% | 2% | -82% | -93% | -92% |
| XRP | 1391 | 7 | 3% | 1% | -38% | -85% | -86% |
| NEAR | 1389 | 8 | 5% | 3% | -25% | -78% | -78% |
| BTC | 1389 | 7 | 5% | 2% | -33% | -88% | -91% |
| GOLD | 769 | 1 | 4% | 1% | -85% | -92% | -94% |
| SILVER | 749 | 4 | 3% | 1% | -38% | -78% | -78% |
| WTI | 718 | 3 | 3% | 1% | -51% | -94% | -96% |
| COPPER | 663 | 1 | 2% | 2% | -86% | -97% | -96% |
| PLATINUM | 638 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 589 | 1 | 1% | 0% | -84% | -98% | -98% |
| NATGAS | 588 | 4 | 2% | 2% | -37% | -96% | -95% |
| EURUSD | 578 | 3 | 3% | 1% | -52% | -79% | -78% |
| GBPUSD | 542 | 1 | 2% | 1% | -83% | -97% | -97% |
| USDJPY | 498 | 3 | 1% | 1% | -44% | -99% | -98% |
| AUDUSD | 128 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 120 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9703 | 38 | 3% | 2% | -55% | -89% | -88% |
| DOWN (bought NO) | 9474 | 37 | 4% | 2% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2135 | 11 | 2% | 1% | -14% | -78% | -78% |
| 0.05–0.1% | 2192 | 7 | 3% | 1% | -54% | -92% | -92% |
| 0.1–0.2% | 3175 | 10 | 4% | 2% | -61% | -90% | -90% |
| 0.2–0.5% | 3657 | 20 | 6% | 3% | -40% | -88% | -88% |
| Over 0.5% | 1435 | 6 | 6% | 2% | -57% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4957 | 20 | 4% | 2% | -54% | -87% | -87% |
| Morning (6am–12pm) | 4329 | 23 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 4482 | 16 | 3% | 1% | -58% | -87% | -88% |
| Evening (6pm–12am) | 5409 | 16 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,475 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/15 5:58:04 AM | SOL | UP | 1.9 min | -0.251% | — | In play | — |
| 10/15 5:57:58 AM | BNB | UP | 2.0 min | -0.173% | — | In play | — |
| 10/15 5:57:54 AM | GBPUSD | UP | 2.1 min | — | — | In play | — |
| 10/15 5:57:50 AM | ETH | UP | 2.1 min | -0.176% | — | In play | — |
| 10/15 5:57:40 AM | XRP | UP | 2.3 min | -0.260% | — | In play | — |
| 10/15 5:57:28 AM | AUDUSD | UP | 2.5 min | — | — | In play | — |
| 10/15 5:57:12 AM | EURUSD | UP | 2.8 min | — | — | In play | — |
| 10/15 5:44:50 AM | DOGE | DOWN | 10 sec | -0.009% | 0¢ | ❌ Lost | $0.00 |
| 10/15 5:44:24 AM | BTC | DOWN | 36 sec | +0.087% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 5:44:18 AM | ETH | DOWN | 42 sec | +0.137% | 0¢ | ❌ Lost | $0.00 |
| 10/15 5:43:41 AM | WTI | DOWN | 78 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 5:43:35 AM | GOLD | UP | 84 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/15 5:43:29 AM | NATGAS | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 5:42:27 AM | COPPER | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 5:42:23 AM | HYPE | DOWN | 2.6 min | +0.249% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 5:42:09 AM | BNB | DOWN | 2.9 min | +0.110% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 5:42:09 AM | ZEC | DOWN | 2.9 min | +0.552% | 0¢ | ❌ Lost | $0.00 |
| 10/15 5:42:03 AM | USDJPY | DOWN | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 5:41:08 AM | SOL | DOWN | 3.9 min | +0.321% | 4¢ | ❌ Lost | -$0.15 |
| 10/15 5:40:18 AM | XRP | DOWN | 4.7 min | +0.344% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 5:40:02 AM | NEAR | DOWN | 5.0 min | +0.881% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 5:29:52 AM | GBPUSD | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 5:29:52 AM | BTC | DOWN | 8 sec | -0.003% | 0¢ | ❌ Lost | $0.00 |
| 10/15 5:29:52 AM | GOLD | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 5:29:52 AM | BNB | DOWN | 8 sec | -0.013% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 5:29:52 AM | ETH | DOWN | 8 sec | -0.038% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 5:29:36 AM | XRP | UP | 24 sec | -0.122% | 0¢ | ❌ Lost | $0.00 |
| 10/15 5:29:36 AM | NEAR | UP | 24 sec | -0.217% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 5:29:36 AM | SOL | UP | 24 sec | -0.085% | 0¢ | ❌ Lost | $0.00 |
| 10/15 5:29:05 AM | COPPER | DOWN | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
