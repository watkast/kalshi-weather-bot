# 15-Minute 1¢ Study

*Updated Tue Oct 6, 10:19 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 710 finished bets | 1% | $35.95 | +47% | +5.06¢ | -$10.40 / $46.35 |

*Expect about **80 buys a day** (~$11.96/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 708 | $23.15 | +31% |
| 5+ min left, hold to the close | 262 | $17.15 | +44% |
| Mean-reversion model ≥ 5%, hold to the close | 1550 | $15.45 | +8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 10249 | 10243 | 46 (0%) | 1.07% | -$592.60 (-48%) | Hold to the close: -$592.60 (-48%) |

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
| Volatility model | 6660 | 4.2% | 0.5% (33) | -566% | ❌ Worse |
| Momentum model | 6660 | 4.2% | 0.5% (33) | -595% | ❌ Worse |
| Mean-reversion model | 6660 | 6.8% | 0.5% (33) | -653% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6660 | 33 | -37% | -86% | -86% | -84% |
| Volatility model ≥ 2% | 1302 | 12 | +8% | -72% | -73% | -68% |
| Volatility model ≥ 5% | 710 | 8 | +47% | -61% | -61% | -57% |
| Volatility model ≥ 10% | 446 | 6 | +100% | -45% | -46% | -40% |
| Momentum model ≥ 2% | 1159 | 10 | +5% | -73% | -75% | -73% |
| Momentum model ≥ 5% | 708 | 7 | +31% | -66% | -68% | -65% |
| Momentum model ≥ 10% | 493 | 6 | +76% | -55% | -56% | -53% |
| Mean-reversion model ≥ 2% | 2283 | 19 | -9% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1550 | 15 | +8% | -81% | -81% | -74% |
| Mean-reversion model ≥ 10% | 1029 | 11 | +24% | -79% | -79% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6857 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2557 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 829 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 10243 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 46 | 0% | -$592.60 | -48% | — |
| Sell at 2¢ | 365 | 4% | -$1,113.70 | -90% | 34 sec |
| Sell at 3¢ | 241 | 2% | -$1,114.61 | -90% | 47 sec |
| Sell at 5¢ | 180 | 2% | -$1,091.60 | -88% | 50 sec |
| Sell at 10¢ | 122 | 1% | -$1,034.78 | -84% | 64 sec |
| Sell at 25¢ | 70 | 1% | -$934.90 | -76% | 82 sec |
| Sell at 50¢ | 46 | 0% | -$814.10 | -66% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 259 | 4 | 10% | 3% | +46% | -82% | -88% |
| 2–5 min | 3284 | 24 | 7% | 3% | -29% | -87% | -88% |
| 1–2 min | 2683 | 11 | 3% | 2% | -56% | -94% | -94% |
| Under 1 min | 4014 | 7 | 1% | 0% | -74% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 775 | 6 | 5% | 3% | -7% | -90% | -89% |
| HYPE | 767 | 3 | 5% | 3% | -52% | -88% | -87% |
| DOGE | 765 | 2 | 3% | 1% | -66% | -92% | -92% |
| ETH | 762 | 7 | 5% | 3% | +15% | -88% | -87% |
| BNB | 760 | 3 | 4% | 2% | -52% | -91% | -92% |
| NEAR | 758 | 5 | 6% | 3% | -13% | -68% | -69% |
| SOL | 758 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 756 | 4 | 5% | 3% | -30% | -87% | -89% |
| XRP | 756 | 5 | 2% | 1% | -17% | -80% | -80% |
| GOLD | 428 | 0 | 4% | 1% | -100% | -92% | -95% |
| SILVER | 416 | 0 | 2% | 1% | -100% | -95% | -95% |
| WTI | 396 | 2 | 3% | 1% | -45% | -95% | -97% |
| COPPER | 367 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 326 | 0 | 0% | 0% | -100% | -99% | -99% |
| NATGAS | 312 | 3 | 3% | 2% | -10% | -94% | -92% |
| PALLADIUM | 312 | 1 | 2% | 1% | -70% | -97% | -98% |
| EURUSD | 300 | 1 | 4% | 2% | -69% | -94% | -92% |
| GBPUSD | 284 | 1 | 3% | 2% | -67% | -95% | -95% |
| USDJPY | 245 | 3 | 2% | 1% | +14% | -97% | -96% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5181 | 24 | 4% | 2% | -46% | -90% | -89% |
| DOWN (bought NO) | 5062 | 22 | 3% | 2% | -50% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1142 | 8 | 2% | 1% | +20% | -65% | -64% |
| 0.05–0.1% | 1188 | 4 | 3% | 1% | -51% | -92% | -92% |
| 0.1–0.2% | 1734 | 6 | 4% | 2% | -56% | -91% | -92% |
| 0.2–0.5% | 1992 | 12 | 6% | 3% | -34% | -88% | -87% |
| Over 0.5% | 799 | 5 | 7% | 3% | -36% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2570 | 15 | 4% | 2% | -32% | -87% | -88% |
| Morning (6am–12pm) | 2536 | 17 | 5% | 3% | -24% | -90% | -89% |
| Afternoon (12–6pm) | 2244 | 7 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 2893 | 7 | 3% | 1% | -72% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,084 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/6 10:14:50 PM | DOGE | DOWN | 10 sec | +0.028% | 0¢ | ❌ Lost | $0.00 |
| 10/6 10:14:34 PM | SILVER | DOWN | 25 sec | — | 13¢ | ❌ Lost | -$0.15 |
| 10/6 10:14:18 PM | XRP | UP | 41 sec | -0.068% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 10:14:18 PM | EURUSD | UP | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 10:14:18 PM | ZEC | UP | 41 sec | -0.109% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 10:14:18 PM | WTI | UP | 41 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/6 10:14:18 PM | SOL | DOWN | 41 sec | +0.104% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 10:14:02 PM | PALLADIUM | DOWN | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 10:14:02 PM | BNB | DOWN | 57 sec | -0.003% | 0¢ | ❌ Lost | $0.00 |
| 10/6 10:13:46 PM | ETH | DOWN | 74 sec | +0.065% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 10:13:46 PM | PLATINUM | DOWN | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 10:13:31 PM | NATGAS | UP | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 10:13:15 PM | GBPUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 10:12:59 PM | NEAR | DOWN | 2.0 min | +0.558% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 10:11:39 PM | HYPE | UP | 3.4 min | -0.305% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:59:58 PM | WTI | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 9:59:58 PM | USDJPY | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 9:59:58 PM | BTC | UP | 1 sec | +0.001% | 0¢ | ❌ Lost | $0.00 |
| 10/6 9:59:58 PM | NATGAS | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 9:59:43 PM | GOLD | UP | 17 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/6 9:59:43 PM | COPPER | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 9:59:43 PM | SILVER | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 9:59:27 PM | XRP | UP | 33 sec | -0.061% | 0¢ | ❌ Lost | $0.00 |
| 10/6 9:59:27 PM | ETH | UP | 33 sec | -0.090% | 0¢ | ❌ Lost | $0.00 |
| 10/6 9:59:27 PM | SOL | UP | 33 sec | -0.080% | 0¢ | ❌ Lost | $0.00 |
| 10/6 9:59:27 PM | BNB | UP | 33 sec | -0.065% | 0¢ | ❌ Lost | $0.00 |
| 10/6 9:59:11 PM | DOGE | UP | 48 sec | -0.151% | 0¢ | ❌ Lost | $0.00 |
| 10/6 9:59:11 PM | PALLADIUM | DOWN | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 9:58:39 PM | HYPE | UP | 80 sec | -0.162% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 9:58:39 PM | NEAR | UP | 80 sec | -0.676% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
