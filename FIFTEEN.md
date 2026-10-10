# 15-Minute 1¢ Study

*Updated Fri Oct 9, 10:00 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 918 finished bets | 1% | $39.95 | +40% | +4.35¢ | -$6.75 / $46.70 |

*Expect about **77 buys a day** (~$11.61/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 896 | $15.85 | +16% |
| 5+ min left, hold to the close | 386 | -$1.00 | -2% |
| Volatility model ≥ 5%, sell at 50¢ | 918 | -$4.55 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 13502 | 13489 | 54 (0%) | 1.07% | -$880.20 (-54%) | Hold to the close: -$880.20 (-54%) |

*In play or awaiting result: 12. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 8644 | 4.1% | 0.4% (37) | -578% | ❌ Worse |
| Momentum model | 8644 | 4.1% | 0.4% (37) | -612% | ❌ Worse |
| Mean-reversion model | 8644 | 6.8% | 0.4% (37) | -675% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 8644 | 37 | -46% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1669 | 14 | -3% | -76% | -76% | -72% |
| Volatility model ≥ 5% | 918 | 10 | +40% | -68% | -67% | -64% |
| Volatility model ≥ 10% | 566 | 8 | +106% | -53% | -54% | -49% |
| Momentum model ≥ 2% | 1477 | 11 | -10% | -77% | -78% | -76% |
| Momentum model ≥ 5% | 896 | 8 | +16% | -71% | -72% | -70% |
| Momentum model ≥ 10% | 612 | 6 | +41% | -62% | -63% | -60% |
| Mean-reversion model ≥ 2% | 3014 | 22 | -21% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2032 | 17 | -8% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1336 | 13 | +11% | -81% | -80% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 8842 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3444 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1203 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 13489 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 54 | 0% | -$880.20 | -54% | — |
| Sell at 2¢ | 455 | 3% | -$1,475.90 | -90% | 33 sec |
| Sell at 3¢ | 306 | 2% | -$1,474.86 | -90% | 47 sec |
| Sell at 5¢ | 223 | 2% | -$1,449.25 | -89% | 50 sec |
| Sell at 10¢ | 146 | 1% | -$1,374.94 | -84% | 64 sec |
| Sell at 25¢ | 83 | 1% | -$1,263.47 | -77% | 82 sec |
| Sell at 50¢ | 55 | 0% | -$1,124.95 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 382 | 4 | 10% | 3% | -1% | -82% | -85% |
| 2–5 min | 4356 | 28 | 6% | 3% | -37% | -88% | -89% |
| 1–2 min | 3526 | 13 | 3% | 2% | -60% | -94% | -94% |
| Under 1 min | 5221 | 9 | 1% | 0% | -75% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 989 | 6 | 4% | 3% | -27% | -90% | -90% |
| DOGE | 988 | 2 | 3% | 2% | -74% | -92% | -91% |
| HYPE | 987 | 3 | 4% | 2% | -62% | -90% | -88% |
| BNB | 987 | 5 | 4% | 2% | -39% | -90% | -91% |
| ETH | 981 | 7 | 5% | 2% | -12% | -89% | -88% |
| NEAR | 979 | 5 | 6% | 2% | -33% | -73% | -74% |
| SOL | 978 | 1 | 3% | 1% | -87% | -94% | -93% |
| BTC | 977 | 4 | 5% | 2% | -46% | -88% | -90% |
| XRP | 976 | 6 | 2% | 1% | -23% | -82% | -82% |
| GOLD | 568 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 555 | 1 | 3% | 1% | -79% | -94% | -94% |
| WTI | 529 | 3 | 3% | 1% | -35% | -94% | -96% |
| COPPER | 490 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 451 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 431 | 3 | 3% | 2% | -35% | -95% | -93% |
| PALLADIUM | 420 | 1 | 1% | 0% | -78% | -98% | -99% |
| EURUSD | 412 | 3 | 3% | 2% | -32% | -72% | -71% |
| GBPUSD | 389 | 1 | 3% | 2% | -76% | -96% | -95% |
| USDJPY | 353 | 3 | 1% | 1% | -21% | -98% | -97% |
| AUDUSD | 25 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 24 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6787 | 28 | 3% | 2% | -52% | -89% | -89% |
| DOWN (bought NO) | 6702 | 26 | 3% | 1% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1450 | 8 | 2% | 1% | -5% | -70% | -70% |
| 0.05–0.1% | 1512 | 5 | 3% | 1% | -52% | -92% | -92% |
| 0.1–0.2% | 2258 | 8 | 4% | 2% | -56% | -92% | -92% |
| 0.2–0.5% | 2562 | 13 | 5% | 3% | -44% | -89% | -88% |
| Over 0.5% | 1057 | 5 | 6% | 2% | -51% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3343 | 18 | 4% | 2% | -38% | -85% | -85% |
| Morning (6am–12pm) | 3238 | 17 | 4% | 2% | -40% | -91% | -91% |
| Afternoon (12–6pm) | 3143 | 9 | 3% | 1% | -66% | -90% | -90% |
| Evening (6pm–12am) | 3765 | 10 | 3% | 1% | -70% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,101 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/9 9:59:48 PM | SOL | UP | 11 sec | -0.001% | 0¢ | In play | — |
| 10/9 9:58:59 PM | ETH | DOWN | 60 sec | +0.035% | 1¢ | In play | — |
| 10/9 9:58:59 PM | BTC | DOWN | 60 sec | +0.037% | 0¢ | ❌ Lost | $0.00 |
| 10/9 9:58:43 PM | DOGE | UP | 76 sec | -0.118% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 9:58:43 PM | HYPE | UP | 76 sec | -0.085% | 0¢ | In play | — |
| 10/9 9:57:54 PM | XRP | DOWN | 2.1 min | +0.093% | 1¢ | In play | — |
| 10/9 9:57:06 PM | BNB | DOWN | 2.9 min | +0.039% | 0¢ | In play | — |
| 10/9 9:57:06 PM | ZEC | DOWN | 2.9 min | +0.280% | 0¢ | In play | — |
| 10/9 9:44:43 PM | DOGE | UP | 17 sec | -0.083% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 9:44:43 PM | NEAR | UP | 17 sec | -0.155% | 0¢ | ❌ Lost | $0.00 |
| 10/9 9:44:27 PM | ZEC | DOWN | 33 sec | +0.061% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 9:44:27 PM | NATGAS | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 9:44:12 PM | SOL | DOWN | 47 sec | +0.052% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 9:44:12 PM | XRP | DOWN | 47 sec | +0.043% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 9:43:54 PM | ETH | UP | 66 sec | -0.041% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 9:43:54 PM | BTC | UP | 66 sec | -0.044% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 9:43:07 PM | HYPE | UP | 1.9 min | -0.101% | 0¢ | ❌ Lost | $0.00 |
| 10/9 9:42:17 PM | BNB | UP | 2.7 min | -0.128% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 9:29:44 PM | BTC | DOWN | 15 sec | +0.000% | 0¢ | ❌ Lost | $0.00 |
| 10/9 9:29:44 PM | HYPE | DOWN | 15 sec | -0.016% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 9:29:28 PM | BNB | DOWN | 31 sec | -0.018% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 9:28:39 PM | SOL | UP | 80 sec | -0.118% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 9:28:39 PM | NEAR | UP | 80 sec | -0.516% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 9:28:23 PM | DOGE | UP | 1.6 min | -0.131% | 4¢ | ❌ Lost | -$0.15 |
| 10/9 9:28:23 PM | ETH | UP | 1.6 min | -0.063% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 9:27:33 PM | ZEC | DOWN | 2.5 min | +0.118% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 9:27:02 PM | XRP | UP | 3.0 min | -0.214% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 9:14:49 PM | WTI | DOWN | 11 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/9 9:14:00 PM | NEAR | UP | 60 sec | -0.283% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 9:14:00 PM | HYPE | UP | 60 sec | -0.068% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
