# 15-Minute 1¢ Study

*Updated Thu Oct 8, 12:47 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 794 finished bets | 1% | $26.35 | +31% | +3.32¢ | -$14.30 / $40.65 |

*Expect about **76 buys a day** (~$11.34/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 793 | $12.95 | +15% |
| 5+ min left, hold to the close | 350 | $4.40 | +9% |
| Volatility model ≥ 5%, sell at 50¢ | 794 | -$3.65 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 11998 | 11991 | 49 (0%) | 1.07% | -$770.80 (-53%) | Hold to the close: -$770.80 (-53%) |

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
| Volatility model | 7673 | 4.0% | 0.4% (33) | -566% | ❌ Worse |
| Momentum model | 7673 | 4.0% | 0.4% (33) | -597% | ❌ Worse |
| Mean-reversion model | 7673 | 6.7% | 0.4% (33) | -664% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7673 | 33 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 1464 | 12 | -5% | -74% | -74% | -70% |
| Volatility model ≥ 5% | 794 | 8 | +31% | -64% | -63% | -60% |
| Volatility model ≥ 10% | 490 | 6 | +81% | -47% | -48% | -43% |
| Momentum model ≥ 2% | 1302 | 10 | -8% | -75% | -77% | -74% |
| Momentum model ≥ 5% | 793 | 7 | +15% | -69% | -70% | -67% |
| Momentum model ≥ 10% | 541 | 6 | +59% | -58% | -59% | -55% |
| Mean-reversion model ≥ 2% | 2648 | 19 | -22% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1785 | 15 | -7% | -82% | -82% | -76% |
| Mean-reversion model ≥ 10% | 1175 | 11 | +8% | -80% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7870 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3061 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1060 | 2% | 2% | 2% | 1% | 1% | 0% |
| **All** | 11991 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 49 | 0% | -$770.80 | -53% | — |
| Sell at 2¢ | 413 | 3% | -$1,307.42 | -90% | 33 sec |
| Sell at 3¢ | 272 | 2% | -$1,308.72 | -90% | 47 sec |
| Sell at 5¢ | 201 | 2% | -$1,284.15 | -88% | 50 sec |
| Sell at 10¢ | 131 | 1% | -$1,229.19 | -84% | 64 sec |
| Sell at 25¢ | 75 | 1% | -$1,124.55 | -77% | 82 sec |
| Sell at 50¢ | 49 | 0% | -$1,000.05 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 346 | 4 | 11% | 3% | +10% | -81% | -85% |
| 2–5 min | 3910 | 25 | 6% | 3% | -38% | -88% | -89% |
| 1–2 min | 3135 | 12 | 3% | 2% | -59% | -94% | -94% |
| Under 1 min | 4596 | 8 | 1% | 0% | -74% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 882 | 6 | 5% | 3% | -19% | -90% | -90% |
| HYPE | 881 | 3 | 5% | 2% | -58% | -89% | -87% |
| DOGE | 877 | 2 | 3% | 1% | -71% | -92% | -92% |
| BNB | 876 | 3 | 4% | 2% | -59% | -91% | -92% |
| ETH | 875 | 7 | 5% | 3% | -1% | -89% | -88% |
| NEAR | 871 | 5 | 6% | 3% | -25% | -71% | -73% |
| SOL | 871 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 870 | 4 | 5% | 2% | -40% | -87% | -90% |
| XRP | 867 | 5 | 2% | 1% | -28% | -81% | -81% |
| GOLD | 511 | 0 | 4% | 1% | -100% | -91% | -94% |
| SILVER | 497 | 0 | 3% | 1% | -100% | -94% | -94% |
| WTI | 470 | 3 | 3% | 1% | -30% | -95% | -97% |
| COPPER | 437 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 399 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 378 | 3 | 3% | 2% | -26% | -95% | -93% |
| PALLADIUM | 369 | 1 | 1% | 1% | -75% | -98% | -99% |
| EURUSD | 366 | 3 | 3% | 2% | -23% | -69% | -67% |
| GBPUSD | 348 | 1 | 3% | 2% | -73% | -95% | -95% |
| USDJPY | 314 | 3 | 1% | 1% | -11% | -98% | -97% |
| USDCAD | 16 | 0 | 0% | 0% | -100% | -100% | -100% |
| AUDUSD | 16 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6115 | 26 | 3% | 2% | -51% | -89% | -88% |
| DOWN (bought NO) | 5876 | 23 | 3% | 2% | -55% | -91% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1271 | 8 | 2% | 1% | +9% | -67% | -66% |
| 0.05–0.1% | 1316 | 4 | 3% | 1% | -55% | -92% | -92% |
| 0.1–0.2% | 1989 | 6 | 4% | 2% | -62% | -92% | -92% |
| 0.2–0.5% | 2314 | 12 | 5% | 3% | -43% | -89% | -88% |
| Over 0.5% | 978 | 5 | 6% | 2% | -48% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3090 | 17 | 4% | 2% | -37% | -85% | -85% |
| Morning (6am–12pm) | 3025 | 17 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 2609 | 7 | 3% | 1% | -68% | -89% | -89% |
| Evening (6pm–12am) | 3267 | 8 | 3% | 1% | -72% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,048 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/8 12:44:58 PM | EURUSD | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:44:58 PM | GBPUSD | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:44:43 PM | GOLD | UP | 17 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/8 12:44:43 PM | USDCAD | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:44:43 PM | SOL | DOWN | 17 sec | +0.140% | 0¢ | ❌ Lost | $0.00 |
| 10/8 12:44:27 PM | PALLADIUM | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:44:27 PM | ZEC | UP | 33 sec | -0.069% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:44:27 PM | BTC | DOWN | 33 sec | +0.127% | 0¢ | ❌ Lost | $0.00 |
| 10/8 12:44:27 PM | HYPE | DOWN | 33 sec | +0.102% | 0¢ | ❌ Lost | $0.00 |
| 10/8 12:44:11 PM | NATGAS | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:43:55 PM | NEAR | DOWN | 65 sec | +0.447% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:43:55 PM | DOGE | DOWN | 65 sec | +0.132% | 0¢ | ❌ Lost | $0.00 |
| 10/8 12:43:23 PM | COPPER | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:42:36 PM | BNB | DOWN | 2.4 min | +0.175% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:41:48 PM | ETH | DOWN | 3.2 min | +0.332% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:41:01 PM | XRP | DOWN | 4.0 min | +0.643% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:29:53 PM | GOLD | UP | 7 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/8 12:28:50 PM | WTI | UP | 70 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/8 12:26:28 PM | NATGAS | DOWN | 3.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:25:09 PM | DOGE | DOWN | 4.8 min | +1.143% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:25:09 PM | XRP | DOWN | 4.8 min | +1.486% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:24:53 PM | ZEC | DOWN | 5.1 min | +1.122% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:24:37 PM | ETH | DOWN | 5.4 min | +0.870% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:24:37 PM | BNB | DOWN | 5.4 min | +0.550% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:24:22 PM | HYPE | DOWN | 5.6 min | +0.994% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:24:06 PM | NEAR | DOWN | 5.9 min | +3.015% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:23:18 PM | SOL | DOWN | 6.7 min | +1.373% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:23:02 PM | BTC | DOWN | 7.0 min | +0.903% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:14:54 PM | AUDUSD | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:14:54 PM | PALLADIUM | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
