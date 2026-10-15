# 15-Minute 1¢ Study

*Updated Thu Oct 15, 3:14 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1481 finished bets | 1% | $87.90 | +54% | +5.94¢ | $32.65 / $55.25 |

*Expect about **87 buys a day** (~$12.99/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1389 | $59.25 | +39% |
| Momentum model ≥ 2%, hold to the close | 2311 | $12.10 | +5% |
| Volatility model ≥ 2%, hold to the close | 2659 | $0.85 | +0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 19027 | 19002 | 75 (0%) | 1.07% | -$1,254.15 (-54%) | Hold to the close: -$1,254.15 (-54%) |

*In play or awaiting result: 24. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 12304 | 4.5% | 0.4% (52) | -637% | ❌ Worse |
| Momentum model | 12304 | 4.4% | 0.4% (52) | -662% | ❌ Worse |
| Mean-reversion model | 12304 | 7.3% | 0.4% (52) | -757% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12304 | 52 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2659 | 23 | +0% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 1481 | 18 | +54% | -73% | -71% | -67% |
| Volatility model ≥ 10% | 881 | 11 | +77% | -64% | -62% | -58% |
| Momentum model ≥ 2% | 2311 | 20 | +5% | -79% | -80% | -77% |
| Momentum model ≥ 5% | 1389 | 15 | +39% | -76% | -76% | -72% |
| Momentum model ≥ 10% | 931 | 10 | +51% | -70% | -70% | -65% |
| Mean-reversion model ≥ 2% | 4548 | 32 | -23% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 3110 | 25 | -11% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2040 | 14 | -21% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12502 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4667 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1833 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 19002 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 75 | 0% | -$1,254.15 | -54% | — |
| Sell at 2¢ | 668 | 4% | -$2,074.47 | -90% | 34 sec |
| Sell at 3¢ | 448 | 2% | -$2,073.43 | -90% | 46 sec |
| Sell at 5¢ | 328 | 2% | -$2,034.95 | -88% | 49 sec |
| Sell at 10¢ | 206 | 1% | -$1,950.29 | -85% | 63 sec |
| Sell at 25¢ | 120 | 1% | -$1,780.95 | -77% | 78 sec |
| Sell at 50¢ | 79 | 0% | -$1,574.90 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 598 | 5 | 10% | 3% | -20% | -82% | -87% |
| 2–5 min | 6143 | 35 | 7% | 3% | -44% | -88% | -88% |
| 1–2 min | 4950 | 19 | 3% | 2% | -58% | -94% | -93% |
| Under 1 min | 7307 | 16 | 1% | 0% | -68% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1403 | 11 | 5% | 3% | -2% | -89% | -89% |
| HYPE | 1396 | 4 | 4% | 2% | -65% | -90% | -89% |
| ETH | 1393 | 8 | 5% | 3% | -30% | -88% | -87% |
| BNB | 1393 | 5 | 5% | 2% | -56% | -90% | -89% |
| DOGE | 1391 | 2 | 4% | 2% | -82% | -91% | -90% |
| SOL | 1388 | 2 | 3% | 1% | -82% | -93% | -93% |
| BTC | 1380 | 7 | 5% | 2% | -32% | -88% | -91% |
| XRP | 1380 | 7 | 3% | 1% | -37% | -85% | -86% |
| NEAR | 1378 | 8 | 5% | 2% | -24% | -78% | -78% |
| GOLD | 762 | 1 | 4% | 1% | -85% | -92% | -94% |
| SILVER | 741 | 4 | 3% | 1% | -37% | -78% | -78% |
| WTI | 712 | 3 | 3% | 1% | -51% | -94% | -96% |
| COPPER | 657 | 1 | 2% | 2% | -86% | -97% | -96% |
| PLATINUM | 633 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 582 | 1 | 1% | 0% | -84% | -98% | -98% |
| NATGAS | 580 | 4 | 2% | 2% | -36% | -96% | -95% |
| EURUSD | 570 | 3 | 2% | 1% | -51% | -79% | -79% |
| GBPUSD | 534 | 1 | 2% | 1% | -83% | -97% | -97% |
| USDJPY | 490 | 3 | 1% | 1% | -43% | -99% | -98% |
| AUDUSD | 125 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 114 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9619 | 38 | 3% | 2% | -54% | -89% | -88% |
| DOWN (bought NO) | 9383 | 37 | 4% | 2% | -54% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2120 | 11 | 2% | 1% | -13% | -78% | -78% |
| 0.05–0.1% | 2180 | 7 | 3% | 1% | -54% | -92% | -91% |
| 0.1–0.2% | 3155 | 10 | 4% | 2% | -61% | -90% | -90% |
| 0.2–0.5% | 3624 | 20 | 6% | 3% | -39% | -88% | -88% |
| Over 0.5% | 1420 | 6 | 6% | 2% | -56% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4782 | 20 | 4% | 2% | -52% | -87% | -88% |
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
| 10/15 3:14:23 AM | BTC | DOWN | 37 sec | +0.032% | — | In play | — |
| 10/15 3:14:23 AM | BNB | DOWN | 37 sec | +0.030% | — | In play | — |
| 10/15 3:14:23 AM | XRP | DOWN | 37 sec | +0.091% | — | In play | — |
| 10/15 3:14:06 AM | USDJPY | UP | 53 sec | — | — | In play | — |
| 10/15 3:14:06 AM | DOGE | UP | 53 sec | -0.102% | — | In play | — |
| 10/15 3:13:33 AM | HYPE | DOWN | 87 sec | +0.141% | — | In play | — |
| 10/15 3:13:17 AM | NATGAS | UP | 1.7 min | — | — | In play | — |
| 10/15 3:12:46 AM | COPPER | DOWN | 2.2 min | — | — | In play | — |
| 10/15 3:12:14 AM | PLATINUM | DOWN | 2.8 min | — | — | In play | — |
| 10/15 3:12:14 AM | PALLADIUM | DOWN | 2.8 min | — | — | In play | — |
| 10/15 3:11:58 AM | ZEC | UP | 3.0 min | -0.378% | — | In play | — |
| 10/15 3:11:41 AM | EURUSD | DOWN | 3.3 min | — | — | In play | — |
| 10/15 3:11:25 AM | ETH | DOWN | 3.6 min | +0.199% | — | In play | — |
| 10/15 3:11:09 AM | GBPUSD | DOWN | 3.8 min | — | — | In play | — |
| 10/15 3:10:22 AM | GOLD | DOWN | 4.6 min | — | — | In play | — |
| 10/15 3:10:22 AM | SILVER | DOWN | 4.6 min | — | — | In play | — |
| 10/15 3:09:50 AM | WTI | UP | 5.2 min | — | — | In play | — |
| 10/15 3:09:34 AM | NEAR | UP | 5.4 min | -0.692% | — | In play | — |
| 10/15 12:59:58 AM | GOLD | DOWN | 1 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/15 12:59:58 AM | USDJPY | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:59:58 AM | GBPUSD | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:59:58 AM | PLATINUM | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:59:26 AM | BTC | UP | 33 sec | -0.062% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:59:26 AM | NEAR | DOWN | 33 sec | +0.095% | 0¢ | ❌ Lost | $0.00 |
| 10/15 12:58:54 AM | COPPER | UP | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:58:54 AM | AUDUSD | UP | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:58:38 AM | ETH | UP | 81 sec | -0.164% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:57:18 AM | ZEC | DOWN | 2.7 min | +0.439% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:56:31 AM | SOL | UP | 3.5 min | -0.284% | 2¢ | ❌ Lost | -$0.15 |
| 10/15 12:56:31 AM | XRP | UP | 3.5 min | -0.337% | 7¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
