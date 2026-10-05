# 15-Minute 1¢ Study

*Updated Mon Oct 5, 4:54 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 587 finished bets | 1% | $35.00 | +56% | +5.96¢ | -$18.10 / $53.10 |

*Expect about **82 buys a day** (~$12.27/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 2%, hold to the close | 1089 | $22.90 | +17% |
| Momentum model ≥ 5%, hold to the close | 586 | $21.75 | +35% |
| 5+ min left, hold to the close | 211 | $10.80 | +35% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 8357 | 8351 | 37 (0%) | 1.07% | -$484.75 (-48%) | Hold to the close: -$484.75 (-48%) |

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
| Volatility model | 5529 | 4.2% | 0.5% (25) | -600% | ❌ Worse |
| Momentum model | 5529 | 4.2% | 0.5% (25) | -625% | ❌ Worse |
| Mean-reversion model | 5529 | 6.9% | 0.5% (25) | -701% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5529 | 25 | -43% | -85% | -85% | -82% |
| Volatility model ≥ 2% | 1089 | 11 | +17% | -69% | -69% | -64% |
| Volatility model ≥ 5% | 587 | 7 | +56% | -55% | -54% | -50% |
| Volatility model ≥ 10% | 366 | 5 | +102% | -36% | -37% | -31% |
| Momentum model ≥ 2% | 956 | 8 | +2% | -70% | -72% | -69% |
| Momentum model ≥ 5% | 586 | 6 | +35% | -61% | -63% | -60% |
| Momentum model ≥ 10% | 408 | 5 | +76% | -48% | -48% | -45% |
| Mean-reversion model ≥ 2% | 1924 | 14 | -21% | -83% | -83% | -78% |
| Mean-reversion model ≥ 5% | 1291 | 12 | +3% | -79% | -79% | -72% |
| Mean-reversion model ≥ 10% | 856 | 9 | +22% | -78% | -78% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5726 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1991 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 634 | 4% | 3% | 2% | 2% | 1% | 0% |
| **All** | 8351 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 37 | 0% | -$484.75 | -48% | — |
| Sell at 2¢ | 328 | 4% | -$889.47 | -89% | 33 sec |
| Sell at 3¢ | 213 | 3% | -$891.68 | -89% | 47 sec |
| Sell at 5¢ | 158 | 2% | -$872.05 | -87% | 61 sec |
| Sell at 10¢ | 106 | 1% | -$821.89 | -82% | 66 sec |
| Sell at 25¢ | 59 | 1% | -$737.46 | -74% | 1.5 min |
| Sell at 50¢ | 36 | 0% | -$647.75 | -65% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 208 | 3 | 12% | 3% | +37% | -80% | -87% |
| 2–5 min | 2693 | 20 | 8% | 4% | -28% | -86% | -87% |
| 1–2 min | 2206 | 9 | 3% | 2% | -56% | -93% | -93% |
| Under 1 min | 3241 | 5 | 1% | 0% | -77% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 648 | 5 | 5% | 3% | -8% | -89% | -89% |
| ETH | 639 | 5 | 6% | 3% | -1% | -86% | -86% |
| DOGE | 639 | 2 | 4% | 2% | -60% | -90% | -90% |
| HYPE | 638 | 3 | 5% | 3% | -43% | -88% | -86% |
| BNB | 636 | 2 | 4% | 2% | -62% | -91% | -93% |
| XRP | 633 | 4 | 2% | 1% | -19% | -76% | -76% |
| SOL | 633 | 0 | 3% | 1% | -100% | -92% | -91% |
| BTC | 631 | 3 | 6% | 2% | -38% | -86% | -90% |
| NEAR | 629 | 3 | 7% | 3% | -38% | -63% | -64% |
| GOLD | 336 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 324 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 305 | 2 | 3% | 1% | -30% | -95% | -96% |
| COPPER | 282 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 251 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 249 | 2 | 4% | 2% | -25% | -94% | -92% |
| PALLADIUM | 244 | 1 | 2% | 1% | -62% | -96% | -98% |
| EURUSD | 227 | 1 | 5% | 3% | -59% | -92% | -90% |
| GBPUSD | 217 | 1 | 4% | 2% | -57% | -94% | -94% |
| USDJPY | 190 | 3 | 2% | 2% | +47% | -96% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4214 | 20 | 4% | 2% | -44% | -88% | -88% |
| DOWN (bought NO) | 4137 | 17 | 4% | 2% | -52% | -89% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 955 | 7 | 2% | 1% | +24% | -58% | -58% |
| 0.05–0.1% | 965 | 2 | 3% | 1% | -69% | -91% | -92% |
| 0.1–0.2% | 1424 | 6 | 4% | 2% | -46% | -90% | -91% |
| 0.2–0.5% | 1683 | 8 | 6% | 3% | -48% | -88% | -87% |
| Over 0.5% | 697 | 4 | 7% | 3% | -41% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2148 | 9 | 4% | 2% | -51% | -85% | -86% |
| Morning (6am–12pm) | 2058 | 17 | 5% | 3% | -5% | -89% | -87% |
| Afternoon (12–6pm) | 1751 | 4 | 3% | 1% | -73% | -86% | -87% |
| Evening (6pm–12am) | 2394 | 7 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,144 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/5 4:44:59 AM | WTI | DOWN | 0 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/5 4:44:43 AM | XRP | UP | 16 sec | -0.053% | 0¢ | ❌ Lost | $0.00 |
| 10/5 4:44:39 AM | ZEC | UP | 20 sec | -0.120% | 0¢ | ❌ Lost | $0.00 |
| 10/5 4:44:39 AM | COPPER | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 4:44:33 AM | DOGE | UP | 26 sec | -0.069% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 4:44:33 AM | GBPUSD | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 4:44:31 AM | NEAR | UP | 28 sec | -0.211% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 4:44:13 AM | PLATINUM | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 4:44:11 AM | PALLADIUM | UP | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 4:44:03 AM | NATGAS | UP | 56 sec | — | 34¢ | ❌ Lost | -$0.15 |
| 10/5 4:43:50 AM | BTC | UP | 69 sec | -0.076% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 4:43:37 AM | BNB | DOWN | 82 sec | +0.032% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 4:41:53 AM | SOL | UP | 3.1 min | -0.303% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 4:41:45 AM | HYPE | UP | 3.2 min | -0.364% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 4:41:08 AM | ETH | UP | 3.9 min | -0.200% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 4:29:14 AM | PLATINUM | UP | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 4:29:12 AM | DOGE | DOWN | 47 sec | +0.038% | 0¢ | ❌ Lost | $0.00 |
| 10/5 4:28:37 AM | USDJPY | DOWN | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 4:28:15 AM | PALLADIUM | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 4:27:19 AM | ETH | DOWN | 2.7 min | +0.130% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 4:27:17 AM | BTC | DOWN | 2.7 min | +0.135% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 4:26:55 AM | SOL | DOWN | 3.1 min | +0.229% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 4:26:53 AM | BNB | DOWN | 3.1 min | +0.072% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 4:26:50 AM | HYPE | DOWN | 3.1 min | +0.300% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 4:26:37 AM | ZEC | DOWN | 3.4 min | +0.478% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 4:25:37 AM | XRP | DOWN | 4.4 min | +0.330% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 4:25:03 AM | NEAR | DOWN | 4.9 min | +0.635% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 4:14:46 AM | SILVER | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 4:14:46 AM | DOGE | DOWN | 13 sec | +0.045% | 0¢ | ❌ Lost | $0.00 |
| 10/5 4:14:42 AM | ETH | UP | 17 sec | +0.005% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
