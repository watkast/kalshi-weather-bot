# 15-Minute 1¢ Study

*Updated Sat Oct 10, 3:49 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 949 finished bets | 1% | $36.65 | +35% | +3.86¢ | -$8.10 / $44.75 |

*Expect about **78 buys a day** (~$11.74/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 924 | $13.00 | +13% |
| 5+ min left, hold to the close | 387 | -$1.15 | -2% |
| Volatility model ≥ 5%, sell at 50¢ | 949 | -$7.85 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 13644 | 13637 | 55 (0%) | 1.07% | -$882.85 (-53%) | Hold to the close: -$882.85 (-53%) |

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
| Volatility model | 8792 | 4.2% | 0.4% (38) | -589% | ❌ Worse |
| Momentum model | 8792 | 4.2% | 0.4% (38) | -622% | ❌ Worse |
| Mean-reversion model | 8792 | 6.8% | 0.4% (38) | -688% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 8792 | 38 | -46% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1705 | 14 | -5% | -76% | -76% | -72% |
| Volatility model ≥ 5% | 949 | 10 | +35% | -69% | -67% | -64% |
| Volatility model ≥ 10% | 590 | 8 | +98% | -54% | -54% | -49% |
| Momentum model ≥ 2% | 1510 | 11 | -12% | -77% | -78% | -76% |
| Momentum model ≥ 5% | 924 | 8 | +13% | -71% | -72% | -69% |
| Momentum model ≥ 10% | 632 | 6 | +36% | -63% | -63% | -59% |
| Mean-reversion model ≥ 2% | 3072 | 23 | -19% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2073 | 17 | -9% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1367 | 13 | +9% | -81% | -80% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 8990 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3444 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1203 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 13637 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 55 | 0% | -$882.85 | -53% | — |
| Sell at 2¢ | 459 | 3% | -$1,491.51 | -90% | 33 sec |
| Sell at 3¢ | 309 | 2% | -$1,490.34 | -90% | 47 sec |
| Sell at 5¢ | 226 | 2% | -$1,463.95 | -89% | 50 sec |
| Sell at 10¢ | 149 | 1% | -$1,387.66 | -84% | 64 sec |
| Sell at 25¢ | 84 | 1% | -$1,276.81 | -77% | 82 sec |
| Sell at 50¢ | 56 | 0% | -$1,134.85 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 383 | 4 | 10% | 3% | -1% | -82% | -86% |
| 2–5 min | 4404 | 28 | 6% | 3% | -38% | -89% | -89% |
| 1–2 min | 3565 | 14 | 3% | 2% | -57% | -94% | -94% |
| Under 1 min | 5281 | 9 | 1% | 0% | -75% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1006 | 6 | 4% | 3% | -28% | -90% | -90% |
| HYPE | 1004 | 3 | 4% | 2% | -63% | -90% | -88% |
| BNB | 1004 | 5 | 4% | 2% | -40% | -91% | -92% |
| DOGE | 1003 | 2 | 3% | 2% | -75% | -92% | -91% |
| ETH | 997 | 7 | 5% | 3% | -13% | -89% | -88% |
| NEAR | 996 | 6 | 6% | 3% | -21% | -73% | -74% |
| SOL | 995 | 1 | 3% | 1% | -87% | -94% | -93% |
| BTC | 993 | 4 | 5% | 2% | -47% | -88% | -90% |
| XRP | 992 | 6 | 2% | 1% | -25% | -83% | -83% |
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
| UP (bought YES) | 6865 | 29 | 3% | 2% | -51% | -89% | -89% |
| DOWN (bought NO) | 6772 | 26 | 3% | 1% | -56% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1494 | 8 | 2% | 1% | -9% | -71% | -70% |
| 0.05–0.1% | 1555 | 5 | 3% | 1% | -53% | -92% | -92% |
| 0.1–0.2% | 2292 | 8 | 4% | 2% | -56% | -92% | -92% |
| 0.2–0.5% | 2587 | 14 | 5% | 3% | -41% | -89% | -88% |
| Over 0.5% | 1059 | 5 | 6% | 2% | -51% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3476 | 19 | 4% | 2% | -37% | -85% | -85% |
| Morning (6am–12pm) | 3238 | 17 | 4% | 2% | -40% | -91% | -91% |
| Afternoon (12–6pm) | 3143 | 9 | 3% | 1% | -66% | -90% | -90% |
| Evening (6pm–12am) | 3780 | 10 | 3% | 1% | -70% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,130 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/10 3:44:36 AM | NEAR | UP | 23 sec | -0.166% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 3:44:36 AM | ETH | UP | 23 sec | -0.016% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 3:44:20 AM | XRP | UP | 39 sec | -0.028% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 3:44:05 AM | BTC | UP | 54 sec | -0.029% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 3:44:05 AM | SOL | UP | 54 sec | -0.088% | 0¢ | ❌ Lost | $0.00 |
| 10/10 3:44:05 AM | ZEC | UP | 54 sec | -0.125% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 3:44:05 AM | DOGE | UP | 54 sec | -0.099% | 0¢ | ❌ Lost | $0.00 |
| 10/10 3:42:45 AM | HYPE | UP | 2.2 min | -0.174% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 3:42:29 AM | BNB | UP | 2.5 min | -0.143% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 3:29:58 AM | BTC | DOWN | 2 sec | -0.000% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 3:29:26 AM | SOL | UP | 34 sec | -0.045% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 3:29:26 AM | ETH | UP | 34 sec | -0.018% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 3:29:26 AM | BNB | DOWN | 34 sec | +0.007% | 0¢ | ❌ Lost | $0.00 |
| 10/10 3:29:07 AM | XRP | UP | 53 sec | -0.085% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 3:28:33 AM | NEAR | DOWN | 87 sec | +0.237% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 3:27:46 AM | DOGE | UP | 2.2 min | -0.105% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 3:27:14 AM | ZEC | UP | 2.8 min | -0.227% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 3:24:48 AM | HYPE | UP | 5.2 min | -0.228% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 3:14:50 AM | NEAR | UP | 9 sec | -0.153% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 3:14:34 AM | DOGE | DOWN | 25 sec | -0.010% | 22¢ | ❌ Lost | $0.00 |
| 10/10 3:13:55 AM | ZEC | DOWN | 65 sec | +0.117% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 3:12:19 AM | XRP | DOWN | 2.7 min | +0.164% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 3:12:03 AM | HYPE | DOWN | 2.9 min | +0.135% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 3:12:03 AM | BTC | DOWN | 2.9 min | +0.106% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 3:12:03 AM | SOL | DOWN | 2.9 min | +0.114% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 3:12:03 AM | ETH | DOWN | 2.9 min | +0.093% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 3:11:48 AM | BNB | DOWN | 3.2 min | +0.043% | 0¢ | ❌ Lost | $0.00 |
| 10/10 2:59:57 AM | HYPE | UP | 3 sec | -0.055% | 0¢ | ❌ Lost | $0.00 |
| 10/10 2:59:25 AM | ZEC | UP | 35 sec | -0.082% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 2:58:49 AM | XRP | DOWN | 70 sec | +0.078% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
