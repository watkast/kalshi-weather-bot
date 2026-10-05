# 15-Minute 1¢ Study

*Updated Mon Oct 5, 4:46 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 617 finished bets | 1% | $31.55 | +47% | +5.11¢ | -$5.90 / $37.45 |

*Expect about **80 buys a day** (~$12.07/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 619 | $17.85 | +27% |
| Volatility model ≥ 2%, hold to the close | 1146 | $16.00 | +12% |
| Mean-reversion model ≥ 5%, hold to the close | 1353 | $11.75 | +7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 8857 | 8844 | 38 (0%) | 1.07% | -$531.65 (-50%) | Hold to the close: -$531.65 (-50%) |

*In play or awaiting result: 13. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 5823 | 4.1% | 0.4% (26) | -595% | ❌ Worse |
| Momentum model | 5823 | 4.2% | 0.4% (26) | -621% | ❌ Worse |
| Mean-reversion model | 5823 | 6.8% | 0.4% (26) | -695% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5823 | 26 | -44% | -85% | -85% | -83% |
| Volatility model ≥ 2% | 1146 | 11 | +12% | -70% | -70% | -65% |
| Volatility model ≥ 5% | 617 | 7 | +47% | -57% | -57% | -53% |
| Volatility model ≥ 10% | 381 | 5 | +94% | -38% | -39% | -34% |
| Momentum model ≥ 2% | 1013 | 8 | -4% | -71% | -73% | -71% |
| Momentum model ≥ 5% | 619 | 6 | +27% | -62% | -65% | -62% |
| Momentum model ≥ 10% | 427 | 5 | +68% | -50% | -51% | -48% |
| Mean-reversion model ≥ 2% | 2017 | 15 | -19% | -83% | -83% | -78% |
| Mean-reversion model ≥ 5% | 1353 | 13 | +7% | -79% | -79% | -72% |
| Mean-reversion model ≥ 10% | 893 | 9 | +17% | -78% | -78% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6020 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 2138 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 686 | 3% | 3% | 2% | 2% | 1% | 0% |
| **All** | 8844 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 38 | 0% | -$531.65 | -50% | — |
| Sell at 2¢ | 339 | 4% | -$947.51 | -89% | 33 sec |
| Sell at 3¢ | 222 | 3% | -$949.07 | -89% | 47 sec |
| Sell at 5¢ | 164 | 2% | -$929.05 | -87% | 56 sec |
| Sell at 10¢ | 110 | 1% | -$877.55 | -83% | 66 sec |
| Sell at 25¢ | 60 | 1% | -$795.05 | -75% | 86 sec |
| Sell at 50¢ | 37 | 0% | -$701.90 | -66% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 222 | 3 | 11% | 3% | +28% | -81% | -88% |
| 2–5 min | 2869 | 20 | 7% | 3% | -32% | -87% | -87% |
| 1–2 min | 2328 | 10 | 3% | 2% | -53% | -93% | -93% |
| Under 1 min | 3422 | 5 | 1% | 0% | -78% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 680 | 5 | 5% | 3% | -12% | -89% | -89% |
| DOGE | 672 | 2 | 4% | 1% | -62% | -91% | -90% |
| HYPE | 672 | 3 | 5% | 3% | -46% | -89% | -86% |
| ETH | 669 | 5 | 6% | 3% | -6% | -87% | -86% |
| BNB | 668 | 2 | 4% | 2% | -64% | -90% | -92% |
| XRP | 666 | 4 | 2% | 1% | -23% | -77% | -78% |
| SOL | 666 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 665 | 3 | 5% | 2% | -41% | -87% | -90% |
| NEAR | 662 | 4 | 6% | 3% | -21% | -65% | -65% |
| GOLD | 358 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 344 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 330 | 2 | 3% | 1% | -35% | -95% | -96% |
| COPPER | 303 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 273 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 268 | 2 | 3% | 2% | -30% | -94% | -92% |
| PALLADIUM | 262 | 1 | 2% | 1% | -64% | -97% | -98% |
| EURUSD | 246 | 1 | 4% | 3% | -62% | -92% | -90% |
| GBPUSD | 235 | 1 | 4% | 2% | -60% | -93% | -93% |
| USDJPY | 205 | 3 | 2% | 1% | +37% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4455 | 21 | 4% | 2% | -45% | -89% | -88% |
| DOWN (bought NO) | 4389 | 17 | 4% | 2% | -55% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 998 | 7 | 2% | 1% | +20% | -60% | -59% |
| 0.05–0.1% | 1009 | 2 | 3% | 1% | -71% | -91% | -92% |
| 0.1–0.2% | 1503 | 6 | 4% | 2% | -49% | -91% | -91% |
| 0.2–0.5% | 1774 | 9 | 6% | 3% | -44% | -87% | -87% |
| Over 0.5% | 734 | 4 | 7% | 3% | -44% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2228 | 9 | 4% | 2% | -53% | -86% | -87% |
| Morning (6am–12pm) | 2361 | 17 | 5% | 3% | -18% | -90% | -88% |
| Afternoon (12–6pm) | 1861 | 5 | 3% | 1% | -68% | -86% | -87% |
| Evening (6pm–12am) | 2394 | 7 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,118 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/5 4:44:56 PM | GBPUSD | UP | 3 sec | — | 0¢ | In play | — |
| 10/5 4:44:42 PM | ETH | DOWN | 18 sec | +0.028% | 0¢ | In play | — |
| 10/5 4:44:42 PM | ZEC | UP | 18 sec | -0.051% | 0¢ | In play | — |
| 10/5 4:44:42 PM | BNB | DOWN | 18 sec | -0.010% | 0¢ | ❌ Lost | $0.00 |
| 10/5 4:44:42 PM | BTC | UP | 18 sec | -0.005% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 4:43:38 PM | GOLD | DOWN | 82 sec | — | 1¢ | In play | — |
| 10/5 4:42:33 PM | NEAR | DOWN | 2.4 min | +0.566% | 1¢ | In play | — |
| 10/5 4:42:17 PM | DOGE | UP | 2.7 min | -0.142% | 1¢ | In play | — |
| 10/5 4:41:13 PM | SOL | UP | 3.8 min | -0.246% | 1¢ | In play | — |
| 10/5 4:39:35 PM | HYPE | UP | 5.4 min | -0.427% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 1:59:50 PM | ZEC | UP | 9 sec | -0.046% | 0¢ | ❌ Lost | $0.00 |
| 10/5 1:59:34 PM | BTC | DOWN | 25 sec | +0.007% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 1:59:34 PM | GOLD | UP | 25 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 1:59:34 PM | NEAR | DOWN | 25 sec | +0.181% | 0¢ | ❌ Lost | $0.00 |
| 10/5 1:59:18 PM | PALLADIUM | UP | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 1:59:18 PM | SOL | DOWN | 41 sec | +0.118% | 0¢ | ❌ Lost | $0.00 |
| 10/5 1:59:18 PM | XRP | DOWN | 41 sec | +0.193% | 0¢ | ❌ Lost | $0.00 |
| 10/5 1:58:30 PM | COPPER | UP | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 1:58:30 PM | ETH | UP | 89 sec | -0.058% | 13¢ | ❌ Lost | -$0.15 |
| 10/5 1:58:30 PM | PLATINUM | UP | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 1:58:30 PM | DOGE | DOWN | 89 sec | +0.132% | 0¢ | ❌ Lost | $0.00 |
| 10/5 1:58:14 PM | BNB | DOWN | 1.8 min | +0.067% | 0¢ | ❌ Lost | $0.00 |
| 10/5 1:58:14 PM | NEAR | UP | 1.8 min | -0.299% | 100¢ | ✅ Won | $13.85 |
| 10/5 1:57:26 PM | HYPE | DOWN | 2.5 min | +0.335% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 1:57:26 PM | WTI | DOWN | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 1:56:38 PM | SILVER | UP | 3.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 1:44:53 PM | BTC | UP | 7 sec | -0.012% | 0¢ | ❌ Lost | $0.00 |
| 10/5 1:44:53 PM | ETH | UP | 7 sec | -0.003% | 0¢ | ❌ Lost | $0.00 |
| 10/5 1:44:37 PM | SOL | UP | 23 sec | -0.033% | 0¢ | ❌ Lost | $0.00 |
| 10/5 1:44:37 PM | NEAR | UP | 23 sec | -0.062% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
