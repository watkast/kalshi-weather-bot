# 15-Minute 1¢ Study

*Updated Mon Oct 5, 5:04 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 589 finished bets | 1% | $34.70 | +55% | +5.89¢ | -$18.25 / $52.95 |

*Expect about **82 buys a day** (~$12.30/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 2%, hold to the close | 1091 | $22.60 | +17% |
| Momentum model ≥ 5%, hold to the close | 587 | $21.60 | +35% |
| 5+ min left, hold to the close | 211 | $10.80 | +35% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 8375 | 8369 | 37 (0%) | 1.07% | -$487.30 (-48%) | Hold to the close: -$487.30 (-48%) |

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
| Volatility model | 5537 | 4.2% | 0.5% (25) | -600% | ❌ Worse |
| Momentum model | 5537 | 4.2% | 0.5% (25) | -625% | ❌ Worse |
| Mean-reversion model | 5537 | 6.9% | 0.5% (25) | -701% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5537 | 25 | -43% | -85% | -85% | -82% |
| Volatility model ≥ 2% | 1091 | 11 | +17% | -69% | -69% | -64% |
| Volatility model ≥ 5% | 589 | 7 | +55% | -56% | -54% | -50% |
| Volatility model ≥ 10% | 366 | 5 | +102% | -36% | -37% | -31% |
| Momentum model ≥ 2% | 958 | 8 | +1% | -70% | -72% | -69% |
| Momentum model ≥ 5% | 587 | 6 | +35% | -61% | -63% | -60% |
| Momentum model ≥ 10% | 409 | 5 | +75% | -48% | -48% | -45% |
| Mean-reversion model ≥ 2% | 1928 | 14 | -21% | -83% | -83% | -78% |
| Mean-reversion model ≥ 5% | 1295 | 12 | +3% | -79% | -79% | -72% |
| Mean-reversion model ≥ 10% | 859 | 9 | +21% | -78% | -78% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5734 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1998 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 637 | 4% | 3% | 2% | 2% | 1% | 0% |
| **All** | 8369 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 37 | 0% | -$487.30 | -48% | — |
| Sell at 2¢ | 328 | 4% | -$892.02 | -89% | 33 sec |
| Sell at 3¢ | 213 | 3% | -$894.23 | -89% | 47 sec |
| Sell at 5¢ | 158 | 2% | -$874.60 | -87% | 61 sec |
| Sell at 10¢ | 106 | 1% | -$824.44 | -82% | 66 sec |
| Sell at 25¢ | 59 | 1% | -$740.01 | -74% | 1.5 min |
| Sell at 50¢ | 36 | 0% | -$650.30 | -65% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 208 | 3 | 12% | 3% | +37% | -80% | -87% |
| 2–5 min | 2704 | 20 | 8% | 4% | -28% | -86% | -87% |
| 1–2 min | 2209 | 9 | 3% | 2% | -56% | -93% | -93% |
| Under 1 min | 3245 | 5 | 1% | 0% | -77% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 649 | 5 | 5% | 3% | -8% | -89% | -89% |
| ETH | 640 | 5 | 6% | 3% | -1% | -86% | -86% |
| DOGE | 640 | 2 | 4% | 2% | -60% | -90% | -90% |
| HYPE | 639 | 3 | 5% | 3% | -43% | -88% | -86% |
| BNB | 637 | 2 | 4% | 2% | -63% | -91% | -93% |
| XRP | 634 | 4 | 2% | 1% | -19% | -76% | -76% |
| SOL | 634 | 0 | 3% | 1% | -100% | -92% | -91% |
| BTC | 632 | 3 | 6% | 2% | -38% | -87% | -90% |
| NEAR | 629 | 3 | 7% | 3% | -38% | -63% | -64% |
| GOLD | 337 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 325 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 306 | 2 | 3% | 1% | -30% | -95% | -96% |
| COPPER | 283 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 252 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 250 | 2 | 4% | 2% | -25% | -94% | -92% |
| PALLADIUM | 245 | 1 | 2% | 1% | -62% | -96% | -98% |
| EURUSD | 228 | 1 | 5% | 3% | -59% | -92% | -90% |
| GBPUSD | 218 | 1 | 4% | 2% | -57% | -94% | -94% |
| USDJPY | 191 | 3 | 2% | 2% | +47% | -96% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4219 | 20 | 4% | 2% | -44% | -88% | -88% |
| DOWN (bought NO) | 4150 | 17 | 4% | 2% | -53% | -89% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 956 | 7 | 2% | 1% | +24% | -58% | -58% |
| 0.05–0.1% | 966 | 2 | 3% | 1% | -69% | -91% | -92% |
| 0.1–0.2% | 1428 | 6 | 4% | 2% | -46% | -90% | -91% |
| 0.2–0.5% | 1684 | 8 | 6% | 3% | -48% | -88% | -87% |
| Over 0.5% | 698 | 4 | 7% | 3% | -41% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2166 | 9 | 4% | 2% | -52% | -86% | -87% |
| Morning (6am–12pm) | 2058 | 17 | 5% | 3% | -5% | -89% | -87% |
| Afternoon (12–6pm) | 1751 | 4 | 3% | 1% | -73% | -86% | -87% |
| Evening (6pm–12am) | 2394 | 7 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,143 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/5 4:59:47 AM | NATGAS | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 4:59:33 AM | GBPUSD | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 4:59:33 AM | EURUSD | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 4:59:07 AM | DOGE | DOWN | 52 sec | +0.045% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 4:58:57 AM | SOL | DOWN | 62 sec | +0.078% | 0¢ | ❌ Lost | $0.00 |
| 10/5 4:58:19 AM | GOLD | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 4:58:09 AM | WTI | UP | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 4:57:59 AM | XRP | DOWN | 2.0 min | +0.185% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 4:57:38 AM | COPPER | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 4:57:36 AM | USDJPY | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 4:57:24 AM | PALLADIUM | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 4:56:24 AM | ETH | DOWN | 3.6 min | +0.140% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 4:56:20 AM | SILVER | DOWN | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 4:56:02 AM | BTC | DOWN | 4.0 min | +0.177% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 4:55:52 AM | BNB | DOWN | 4.1 min | +0.144% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 4:55:40 AM | PLATINUM | DOWN | 4.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 4:55:38 AM | ZEC | DOWN | 4.3 min | +0.606% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 4:55:02 AM | HYPE | DOWN | 5.0 min | +0.257% | 1¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
