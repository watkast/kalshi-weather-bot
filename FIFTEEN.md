# 15-Minute 1¢ Study

*Updated Thu Oct 15, 12:36 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1474 finished bets | 1% | $88.80 | +54% | +6.02¢ | $32.95 / $55.85 |

*Expect about **87 buys a day** (~$13.01/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1383 | $60.15 | +40% |
| Momentum model ≥ 2%, hold to the close | 2300 | $13.60 | +5% |
| Volatility model ≥ 2%, hold to the close | 2646 | $2.50 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 18976 | 18969 | 75 (0%) | 1.07% | -$1,249.80 (-54%) | Hold to the close: -$1,249.80 (-54%) |

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
| Volatility model | 12286 | 4.5% | 0.4% (52) | -637% | ❌ Worse |
| Momentum model | 12286 | 4.4% | 0.4% (52) | -662% | ❌ Worse |
| Mean-reversion model | 12286 | 7.3% | 0.4% (52) | -757% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12286 | 52 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2646 | 23 | +1% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1474 | 18 | +54% | -73% | -71% | -67% |
| Volatility model ≥ 10% | 879 | 11 | +78% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 2300 | 20 | +5% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1383 | 15 | +40% | -77% | -76% | -73% |
| Momentum model ≥ 10% | 929 | 10 | +51% | -70% | -70% | -65% |
| Mean-reversion model ≥ 2% | 4535 | 32 | -23% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 3101 | 25 | -11% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2036 | 14 | -21% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12484 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4660 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1825 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 18969 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 75 | 0% | -$1,249.80 | -54% | — |
| Sell at 2¢ | 663 | 3% | -$2,071.42 | -90% | 34 sec |
| Sell at 3¢ | 445 | 2% | -$2,070.25 | -90% | 46 sec |
| Sell at 5¢ | 325 | 2% | -$2,032.55 | -88% | 49 sec |
| Sell at 10¢ | 205 | 1% | -$1,947.25 | -85% | 63 sec |
| Sell at 25¢ | 119 | 1% | -$1,779.91 | -77% | 79 sec |
| Sell at 50¢ | 79 | 0% | -$1,570.55 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 598 | 5 | 10% | 3% | -20% | -82% | -87% |
| 2–5 min | 6131 | 35 | 7% | 3% | -44% | -88% | -88% |
| 1–2 min | 4942 | 19 | 3% | 2% | -58% | -94% | -93% |
| Under 1 min | 7294 | 16 | 1% | 0% | -68% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1401 | 11 | 5% | 3% | -2% | -89% | -89% |
| HYPE | 1394 | 4 | 4% | 2% | -65% | -90% | -89% |
| ETH | 1391 | 8 | 5% | 3% | -30% | -88% | -87% |
| BNB | 1391 | 5 | 4% | 2% | -56% | -90% | -89% |
| DOGE | 1389 | 2 | 4% | 2% | -82% | -91% | -90% |
| SOL | 1386 | 2 | 3% | 1% | -82% | -94% | -93% |
| BTC | 1378 | 7 | 5% | 2% | -32% | -88% | -91% |
| XRP | 1378 | 7 | 3% | 1% | -37% | -85% | -86% |
| NEAR | 1376 | 8 | 5% | 2% | -24% | -78% | -78% |
| GOLD | 760 | 1 | 4% | 1% | -85% | -92% | -94% |
| SILVER | 741 | 4 | 3% | 1% | -37% | -78% | -78% |
| WTI | 712 | 3 | 3% | 1% | -51% | -94% | -96% |
| COPPER | 656 | 1 | 2% | 2% | -86% | -97% | -96% |
| PLATINUM | 631 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 581 | 1 | 1% | 0% | -84% | -98% | -98% |
| NATGAS | 579 | 4 | 2% | 2% | -36% | -96% | -95% |
| EURUSD | 569 | 3 | 2% | 1% | -51% | -79% | -79% |
| GBPUSD | 532 | 1 | 2% | 1% | -82% | -97% | -97% |
| USDJPY | 488 | 3 | 1% | 1% | -43% | -99% | -98% |
| AUDUSD | 123 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 113 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9600 | 38 | 3% | 2% | -54% | -89% | -88% |
| DOWN (bought NO) | 9369 | 37 | 4% | 2% | -54% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2120 | 11 | 2% | 1% | -13% | -78% | -78% |
| 0.05–0.1% | 2177 | 7 | 3% | 1% | -53% | -92% | -91% |
| 0.1–0.2% | 3150 | 10 | 4% | 2% | -61% | -90% | -90% |
| 0.2–0.5% | 3614 | 20 | 6% | 3% | -39% | -88% | -88% |
| Over 0.5% | 1420 | 6 | 6% | 2% | -56% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4749 | 20 | 4% | 2% | -52% | -87% | -88% |
| Morning (6am–12pm) | 4329 | 23 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 4482 | 16 | 3% | 1% | -58% | -87% | -88% |
| Evening (6pm–12am) | 5409 | 16 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,513 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/15 12:29:53 AM | PALLADIUM | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:29:53 AM | NATGAS | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:29:37 AM | EURUSD | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:29:21 AM | PLATINUM | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:29:21 AM | HYPE | DOWN | 38 sec | +0.074% | 0¢ | ❌ Lost | $0.00 |
| 10/15 12:29:05 AM | SILVER | DOWN | 55 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:28:49 AM | NEAR | DOWN | 70 sec | +0.276% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:28:01 AM | GOLD | DOWN | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:27:29 AM | BTC | DOWN | 2.5 min | +0.227% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:27:29 AM | SOL | DOWN | 2.5 min | +0.294% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:27:13 AM | DOGE | DOWN | 2.8 min | +0.396% | 0¢ | ❌ Lost | $0.00 |
| 10/15 12:27:13 AM | ZEC | DOWN | 2.8 min | +0.553% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:26:22 AM | XRP | DOWN | 3.6 min | +0.463% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:26:22 AM | ETH | DOWN | 3.6 min | +0.342% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:26:07 AM | BNB | DOWN | 3.9 min | +0.192% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:14:52 AM | ETH | DOWN | 7 sec | +0.069% | 0¢ | ❌ Lost | $0.00 |
| 10/15 12:14:36 AM | SILVER | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:14:20 AM | DOGE | DOWN | 39 sec | +0.089% | 0¢ | ❌ Lost | $0.00 |
| 10/15 12:14:04 AM | HYPE | UP | 56 sec | -0.173% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:14:04 AM | NEAR | UP | 56 sec | -0.440% | 0¢ | ❌ Lost | $0.00 |
| 10/15 12:13:45 AM | AUDUSD | UP | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:13:29 AM | BTC | DOWN | 1.5 min | +0.143% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:13:29 AM | USDCAD | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:13:13 AM | PALLADIUM | UP | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:13:13 AM | EURUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:12:59 AM | PLATINUM | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:12:59 AM | ZEC | UP | 2.0 min | -0.680% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:12:09 AM | GOLD | UP | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:11:54 AM | USDJPY | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:10:50 AM | BNB | DOWN | 4.2 min | +0.281% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
