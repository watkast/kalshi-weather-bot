# 15-Minute 1¢ Study

*Updated Fri Oct 9, 2:53 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 887 finished bets | 1% | $29.55 | +31% | +3.33¢ | -$19.25 / $48.80 |

*Expect about **77 buys a day** (~$11.48/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 866 | $18.85 | +20% |
| 5+ min left, hold to the close | 382 | -$0.40 | -1% |
| Volatility model ≥ 5%, sell at 50¢ | 887 | -$7.70 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 13223 | 13216 | 52 (0%) | 1.07% | -$876.55 (-55%) | Hold to the close: -$876.55 (-55%) |

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
| Volatility model | 8397 | 4.0% | 0.4% (35) | -581% | ❌ Worse |
| Momentum model | 8397 | 4.1% | 0.4% (35) | -615% | ❌ Worse |
| Mean-reversion model | 8397 | 6.7% | 0.4% (35) | -680% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 8397 | 35 | -48% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1620 | 13 | -7% | -75% | -75% | -72% |
| Volatility model ≥ 5% | 887 | 9 | +31% | -67% | -66% | -63% |
| Volatility model ≥ 10% | 543 | 7 | +89% | -52% | -52% | -48% |
| Momentum model ≥ 2% | 1434 | 11 | -8% | -76% | -78% | -75% |
| Momentum model ≥ 5% | 866 | 8 | +20% | -70% | -72% | -69% |
| Momentum model ≥ 10% | 593 | 6 | +45% | -62% | -62% | -59% |
| Mean-reversion model ≥ 2% | 2929 | 20 | -26% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1979 | 16 | -11% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1297 | 12 | +6% | -81% | -81% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 8594 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3421 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1201 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 13216 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 52 | 0% | -$876.55 | -55% | — |
| Sell at 2¢ | 443 | 3% | -$1,447.37 | -90% | 33 sec |
| Sell at 3¢ | 295 | 2% | -$1,447.50 | -90% | 47 sec |
| Sell at 5¢ | 216 | 2% | -$1,422.15 | -89% | 56 sec |
| Sell at 10¢ | 142 | 1% | -$1,348.53 | -84% | 64 sec |
| Sell at 25¢ | 81 | 1% | -$1,238.44 | -77% | 81 sec |
| Sell at 50¢ | 53 | 0% | -$1,106.80 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 378 | 4 | 10% | 3% | +0% | -82% | -86% |
| 2–5 min | 4269 | 26 | 6% | 3% | -40% | -89% | -89% |
| 1–2 min | 3456 | 13 | 3% | 2% | -59% | -94% | -94% |
| Under 1 min | 5109 | 9 | 1% | 0% | -74% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 961 | 6 | 4% | 3% | -24% | -90% | -90% |
| HYPE | 961 | 3 | 5% | 2% | -61% | -89% | -88% |
| DOGE | 959 | 2 | 3% | 1% | -74% | -92% | -92% |
| BNB | 958 | 4 | 4% | 2% | -49% | -91% | -92% |
| ETH | 955 | 7 | 5% | 2% | -10% | -89% | -89% |
| NEAR | 951 | 5 | 6% | 3% | -31% | -73% | -73% |
| BTC | 951 | 4 | 5% | 2% | -45% | -88% | -90% |
| SOL | 950 | 0 | 3% | 1% | -100% | -94% | -93% |
| XRP | 948 | 6 | 2% | 1% | -21% | -82% | -82% |
| GOLD | 567 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 555 | 1 | 3% | 1% | -79% | -94% | -94% |
| WTI | 522 | 3 | 3% | 1% | -35% | -94% | -96% |
| COPPER | 490 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 450 | 0 | 0% | 0% | -100% | -100% | -99% |
| PALLADIUM | 420 | 1 | 1% | 0% | -78% | -98% | -99% |
| NATGAS | 417 | 3 | 3% | 2% | -33% | -95% | -93% |
| EURUSD | 412 | 3 | 3% | 2% | -32% | -72% | -71% |
| GBPUSD | 388 | 1 | 3% | 2% | -76% | -96% | -95% |
| USDJPY | 352 | 3 | 1% | 1% | -20% | -98% | -97% |
| AUDUSD | 25 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 24 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6671 | 27 | 3% | 2% | -53% | -89% | -89% |
| DOWN (bought NO) | 6545 | 25 | 3% | 1% | -56% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1384 | 8 | 2% | 1% | +0% | -69% | -69% |
| 0.05–0.1% | 1455 | 4 | 3% | 1% | -60% | -92% | -92% |
| 0.1–0.2% | 2194 | 7 | 4% | 2% | -60% | -92% | -92% |
| 0.2–0.5% | 2514 | 13 | 5% | 3% | -43% | -89% | -88% |
| Over 0.5% | 1045 | 5 | 6% | 2% | -51% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3343 | 18 | 4% | 2% | -38% | -85% | -85% |
| Morning (6am–12pm) | 3238 | 17 | 4% | 2% | -40% | -91% | -91% |
| Afternoon (12–6pm) | 3014 | 8 | 3% | 1% | -69% | -89% | -90% |
| Evening (6pm–12am) | 3621 | 9 | 3% | 1% | -72% | -95% | -95% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,025 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/9 2:44:52 PM | GOLD | UP | 7 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/9 2:44:52 PM | USDJPY | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 2:44:52 PM | HYPE | DOWN | 7 sec | -0.004% | 0¢ | ❌ Lost | $0.00 |
| 10/9 2:44:36 PM | BTC | DOWN | 23 sec | +0.018% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 2:44:36 PM | PLATINUM | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 2:44:36 PM | DOGE | DOWN | 23 sec | +0.012% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 2:44:20 PM | ETH | UP | 39 sec | -0.036% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 2:44:20 PM | XRP | UP | 39 sec | -0.065% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 2:44:04 PM | COPPER | DOWN | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 2:43:30 PM | SOL | UP | 89 sec | -0.123% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 2:43:14 PM | ZEC | UP | 1.8 min | -0.281% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 2:42:10 PM | NEAR | DOWN | 2.8 min | +0.394% | 15¢ | ❌ Lost | -$0.15 |
| 10/9 2:42:10 PM | BNB | DOWN | 2.8 min | +0.056% | 5¢ | ❌ Lost | -$0.15 |
| 10/9 2:29:52 PM | COPPER | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 2:29:36 PM | NEAR | UP | 23 sec | -0.171% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 2:29:36 PM | GOLD | DOWN | 23 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/9 2:29:20 PM | BNB | UP | 39 sec | -0.031% | 0¢ | ❌ Lost | $0.00 |
| 10/9 2:29:20 PM | SOL | UP | 39 sec | -0.111% | 0¢ | ❌ Lost | $0.00 |
| 10/9 2:29:20 PM | WTI | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 2:29:20 PM | ETH | UP | 39 sec | -0.042% | 0¢ | ❌ Lost | $0.00 |
| 10/9 2:29:04 PM | GBPUSD | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 2:29:04 PM | XRP | UP | 56 sec | -0.094% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 2:29:04 PM | DOGE | UP | 56 sec | -0.083% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 2:28:45 PM | ZEC | DOWN | 74 sec | +0.198% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 2:28:45 PM | BTC | UP | 74 sec | -0.042% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 2:28:45 PM | PALLADIUM | DOWN | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 2:28:29 PM | HYPE | UP | 1.5 min | -0.132% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 2:27:43 PM | PLATINUM | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 2:27:27 PM | SILVER | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 2:14:36 PM | WTI | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
