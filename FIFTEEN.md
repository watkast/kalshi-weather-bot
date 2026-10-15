# 15-Minute 1¢ Study

*Updated Thu Oct 15, 5:06 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1484 finished bets | 1% | $87.60 | +53% | +5.90¢ | $32.35 / $55.25 |

*Expect about **86 buys a day** (~$12.95/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1390 | $59.10 | +39% |
| Momentum model ≥ 2%, hold to the close | 2317 | $11.50 | +4% |
| Volatility model ≥ 2%, hold to the close | 2680 | -$2.00 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 19143 | 19136 | 75 (0%) | 1.07% | -$1,271.85 (-55%) | Hold to the close: -$1,271.85 (-55%) |

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
| Volatility model | 12375 | 4.4% | 0.4% (52) | -636% | ❌ Worse |
| Momentum model | 12375 | 4.4% | 0.4% (52) | -661% | ❌ Worse |
| Mean-reversion model | 12375 | 7.3% | 0.4% (52) | -758% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12375 | 52 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2680 | 23 | -1% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 1484 | 18 | +53% | -73% | -71% | -67% |
| Volatility model ≥ 10% | 882 | 11 | +77% | -64% | -62% | -59% |
| Momentum model ≥ 2% | 2317 | 20 | +4% | -79% | -80% | -77% |
| Momentum model ≥ 5% | 1390 | 15 | +39% | -76% | -76% | -72% |
| Momentum model ≥ 10% | 932 | 10 | +50% | -70% | -70% | -65% |
| Mean-reversion model ≥ 2% | 4587 | 32 | -24% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3141 | 25 | -12% | -82% | -81% | -78% |
| Mean-reversion model ≥ 10% | 2062 | 14 | -22% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12573 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4703 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1860 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 19136 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 75 | 0% | -$1,271.85 | -55% | — |
| Sell at 2¢ | 678 | 4% | -$2,089.57 | -90% | 36 sec |
| Sell at 3¢ | 457 | 2% | -$2,087.62 | -90% | 47 sec |
| Sell at 5¢ | 334 | 2% | -$2,048.75 | -88% | 50 sec |
| Sell at 10¢ | 209 | 1% | -$1,964.06 | -85% | 63 sec |
| Sell at 25¢ | 121 | 1% | -$1,795.34 | -77% | 79 sec |
| Sell at 50¢ | 79 | 0% | -$1,592.60 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 613 | 5 | 11% | 3% | -22% | -81% | -86% |
| 2–5 min | 6189 | 35 | 7% | 3% | -44% | -88% | -88% |
| 1–2 min | 4974 | 19 | 3% | 2% | -58% | -94% | -93% |
| Under 1 min | 7356 | 16 | 1% | 0% | -69% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1411 | 11 | 5% | 3% | -3% | -89% | -89% |
| HYPE | 1404 | 4 | 4% | 2% | -65% | -90% | -89% |
| ETH | 1401 | 8 | 5% | 3% | -31% | -88% | -86% |
| BNB | 1401 | 5 | 5% | 2% | -56% | -90% | -89% |
| DOGE | 1399 | 2 | 4% | 2% | -82% | -91% | -90% |
| SOL | 1396 | 2 | 3% | 2% | -82% | -93% | -92% |
| XRP | 1388 | 7 | 3% | 1% | -38% | -85% | -86% |
| BTC | 1387 | 7 | 5% | 2% | -33% | -88% | -91% |
| NEAR | 1386 | 8 | 5% | 3% | -25% | -77% | -78% |
| GOLD | 766 | 1 | 4% | 1% | -85% | -92% | -94% |
| SILVER | 747 | 4 | 3% | 1% | -38% | -78% | -78% |
| WTI | 717 | 3 | 3% | 1% | -51% | -94% | -96% |
| COPPER | 661 | 1 | 2% | 2% | -86% | -97% | -96% |
| PLATINUM | 638 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 588 | 1 | 1% | 0% | -84% | -98% | -98% |
| NATGAS | 586 | 4 | 2% | 2% | -36% | -96% | -95% |
| EURUSD | 577 | 3 | 3% | 1% | -51% | -79% | -78% |
| GBPUSD | 540 | 1 | 2% | 1% | -83% | -97% | -97% |
| USDJPY | 496 | 3 | 1% | 1% | -44% | -99% | -98% |
| AUDUSD | 128 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 119 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9692 | 38 | 3% | 2% | -55% | -89% | -88% |
| DOWN (bought NO) | 9444 | 37 | 4% | 2% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2129 | 11 | 2% | 1% | -14% | -78% | -78% |
| 0.05–0.1% | 2188 | 7 | 3% | 1% | -54% | -92% | -92% |
| 0.1–0.2% | 3170 | 10 | 4% | 2% | -61% | -90% | -90% |
| 0.2–0.5% | 3650 | 20 | 6% | 3% | -40% | -88% | -88% |
| Over 0.5% | 1433 | 6 | 6% | 2% | -57% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4916 | 20 | 4% | 2% | -54% | -87% | -87% |
| Morning (6am–12pm) | 4329 | 23 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 4482 | 16 | 3% | 1% | -58% | -87% | -88% |
| Evening (6pm–12am) | 5409 | 16 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,483 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/15 4:59:56 AM | NATGAS | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 4:59:56 AM | PLATINUM | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 4:59:40 AM | USDCAD | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 4:59:40 AM | ZEC | DOWN | 20 sec | +0.193% | 0¢ | ❌ Lost | $0.00 |
| 10/15 4:59:09 AM | GOLD | DOWN | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 4:59:09 AM | BNB | DOWN | 50 sec | +0.036% | 0¢ | ❌ Lost | $0.00 |
| 10/15 4:58:51 AM | AUDUSD | DOWN | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 4:58:51 AM | SILVER | DOWN | 69 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 4:58:19 AM | BTC | DOWN | 1.7 min | +0.144% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 4:58:19 AM | USDJPY | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 4:58:04 AM | EURUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 4:58:04 AM | XRP | DOWN | 1.9 min | +0.184% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 4:58:04 AM | NEAR | UP | 1.9 min | -0.369% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 4:57:48 AM | ETH | DOWN | 2.2 min | +0.128% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 4:55:49 AM | DOGE | DOWN | 4.2 min | +0.279% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 4:55:49 AM | SOL | DOWN | 4.2 min | +0.328% | 2¢ | ❌ Lost | -$0.15 |
| 10/15 4:55:15 AM | HYPE | UP | 4.8 min | -0.622% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 4:44:54 AM | XRP | UP | 6 sec | -0.107% | 0¢ | ❌ Lost | $0.00 |
| 10/15 4:44:54 AM | SILVER | DOWN | 6 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 4:44:38 AM | PALLADIUM | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 4:44:38 AM | HYPE | UP | 22 sec | -0.092% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 4:44:07 AM | EURUSD | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 4:44:07 AM | BTC | UP | 52 sec | -0.076% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 4:43:19 AM | USDCAD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 4:42:15 AM | USDJPY | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 4:40:37 AM | WTI | DOWN | 4.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 4:40:21 AM | NEAR | DOWN | 4.6 min | +0.689% | 15¢ | ❌ Lost | -$0.15 |
| 10/15 4:39:33 AM | SOL | DOWN | 5.5 min | +0.417% | 9¢ | ❌ Lost | -$0.15 |
| 10/15 4:39:17 AM | DOGE | DOWN | 5.7 min | +0.407% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 4:38:12 AM | ZEC | DOWN | 6.8 min | +0.878% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
