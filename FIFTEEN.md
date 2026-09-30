# 15-Minute 1¢ Study

*Updated Tue Sep 29, 7:13 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 78 finished bets | 3% | $16.30 | +139% | +20.90¢ | $22.15 / -$5.85 |

*Expect about **40 buys a day** (~$6.03/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 78 | $1.80 | +15% |
| Mean-reversion model ≥ 5%, hold to the close | 329 | -$1.20 | -3% |
| Volatility model ≥ 5%, sell at 25¢ | 119 | -$2.37 | -19% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 2467 | 2454 | 10 (0%) | 1.07% | -$158.05 (-53%) | Hold to the close: -$158.05 (-53%) |

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
| Volatility model | 1353 | 2.9% | 0.3% (4) | -477% | ❌ Worse |
| Momentum model | 1353 | 3.0% | 0.3% (4) | -538% | ❌ Worse |
| Mean-reversion model | 1353 | 5.8% | 0.3% (4) | -583% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1353 | 4 | -63% | -90% | -91% | -89% |
| Volatility model ≥ 2% | 264 | 1 | -56% | -85% | -88% | -86% |
| Volatility model ≥ 5% | 119 | 0 | -100% | -75% | -75% | -68% |
| Volatility model ≥ 10% | 64 | 0 | -100% | -73% | -73% | -66% |
| Momentum model ≥ 2% | 225 | 0 | -100% | -86% | -90% | -90% |
| Momentum model ≥ 5% | 127 | 0 | -100% | -83% | -89% | -86% |
| Momentum model ≥ 10% | 82 | 0 | -100% | -87% | -85% | -83% |
| Mean-reversion model ≥ 2% | 503 | 3 | -36% | -86% | -88% | -84% |
| Mean-reversion model ≥ 5% | 329 | 3 | -3% | -84% | -85% | -79% |
| Mean-reversion model ≥ 10% | 204 | 2 | +10% | -79% | -82% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1549 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 748 | 2% | 1% | 1% | 0% | 0% | 0% |
| Financials | 157 | 5% | 3% | 3% | 2% | 2% | 1% |
| **All** | 2454 | 4% | 2% | 1% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 10 | 0% | -$158.05 | -53% | — |
| Sell at 2¢ | 87 | 4% | -$275.43 | -92% | 34 sec |
| Sell at 3¢ | 52 | 2% | -$277.77 | -93% | 48 sec |
| Sell at 5¢ | 36 | 1% | -$274.65 | -92% | 66 sec |
| Sell at 10¢ | 30 | 1% | -$244.75 | -82% | 1.6 min |
| Sell at 25¢ | 15 | 1% | -$234.40 | -79% | 2.1 min |
| Sell at 50¢ | 9 | 0% | -$209.30 | -70% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 78 | 2 | 12% | 3% | +139% | -80% | -87% |
| 2–5 min | 832 | 5 | 6% | 3% | -42% | -89% | -90% |
| 1–2 min | 657 | 2 | 3% | 1% | -67% | -94% | -94% |
| Under 1 min | 887 | 1 | 1% | 0% | -83% | -97% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 176 | 2 | 5% | 3% | +40% | -90% | -86% |
| DOGE | 175 | 1 | 4% | 2% | -25% | -90% | -90% |
| ZEC | 174 | 1 | 5% | 2% | -31% | -90% | -94% |
| NEAR | 172 | 0 | 6% | 1% | -100% | -86% | -89% |
| XRP | 172 | 2 | 2% | 2% | +49% | -94% | -94% |
| BTC | 171 | 0 | 7% | 2% | -100% | -83% | -90% |
| SOL | 171 | 0 | 4% | 2% | -100% | -91% | -89% |
| HYPE | 169 | 0 | 4% | 2% | -100% | -92% | -92% |
| BNB | 169 | 0 | 2% | 1% | -100% | -96% | -96% |
| GOLD | 134 | 0 | 3% | 0% | -100% | -93% | -97% |
| SILVER | 119 | 0 | 3% | 1% | -100% | -95% | -95% |
| WTI | 118 | 0 | 3% | 1% | -100% | -95% | -98% |
| COPPER | 109 | 0 | 1% | 1% | -100% | -98% | -98% |
| NATGAS | 101 | 0 | 3% | 1% | -100% | -95% | -92% |
| PLATINUM | 87 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 80 | 0 | 1% | 0% | -100% | -98% | -100% |
| GBPUSD | 60 | 1 | 5% | 2% | +56% | -91% | -91% |
| EURUSD | 52 | 1 | 6% | 2% | +79% | -90% | -95% |
| USDJPY | 45 | 2 | 4% | 4% | +315% | -92% | -88% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1288 | 7 | 4% | 2% | -38% | -92% | -92% |
| DOWN (bought NO) | 1166 | 3 | 3% | 1% | -70% | -93% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 159 | 0 | 2% | 1% | -100% | -93% | -93% |
| 0.05–0.1% | 193 | 0 | 1% | 0% | -100% | -97% | -97% |
| 0.1–0.2% | 359 | 0 | 4% | 1% | -100% | -91% | -93% |
| 0.2–0.5% | 574 | 2 | 5% | 3% | -62% | -90% | -91% |
| Over 0.5% | 263 | 4 | 6% | 3% | +58% | -88% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 577 | 1 | 3% | 1% | -80% | -93% | -96% |
| Morning (6am–12pm) | 647 | 6 | 4% | 2% | +7% | -91% | -90% |
| Afternoon (12–6pm) | 583 | 1 | 3% | 1% | -81% | -94% | -97% |
| Evening (6pm–12am) | 647 | 2 | 4% | 2% | -64% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,809 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 44 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/29 7:13:51 PM | GOLD | UP | 68 sec | — | — | In play | — |
| 9/29 7:13:04 PM | SILVER | UP | 1.9 min | — | — | In play | — |
| 9/29 7:12:48 PM | SOL | DOWN | 2.2 min | +0.254% | — | In play | — |
| 9/29 7:12:31 PM | XRP | DOWN | 2.5 min | +0.315% | — | In play | — |
| 9/29 7:11:59 PM | DOGE | DOWN | 3.0 min | +0.384% | — | In play | — |
| 9/29 7:11:44 PM | BNB | DOWN | 3.2 min | +0.191% | — | In play | — |
| 9/29 7:11:44 PM | NEAR | DOWN | 3.2 min | +0.766% | — | In play | — |
| 9/29 6:59:59 PM | GOLD | UP | 0 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/29 6:59:43 PM | BNB | DOWN | 16 sec | -0.013% | 0¢ | ❌ Lost | $0.00 |
| 9/29 6:59:43 PM | SILVER | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 6:59:43 PM | WTI | DOWN | 16 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 6:59:27 PM | SOL | DOWN | 32 sec | +0.099% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 6:59:27 PM | ZEC | UP | 32 sec | -0.119% | 0¢ | ❌ Lost | $0.00 |
| 9/29 6:59:27 PM | DOGE | DOWN | 32 sec | +0.015% | 0¢ | ❌ Lost | $0.00 |
| 9/29 6:59:27 PM | HYPE | DOWN | 32 sec | +0.084% | 0¢ | ❌ Lost | $0.00 |
| 9/29 6:59:27 PM | ETH | DOWN | 32 sec | +0.037% | 0¢ | ❌ Lost | $0.00 |
| 9/29 6:59:27 PM | PALLADIUM | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 6:59:11 PM | EURUSD | DOWN | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 6:59:11 PM | PLATINUM | UP | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 6:58:56 PM | XRP | DOWN | 63 sec | +0.121% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 6:58:56 PM | GBPUSD | DOWN | 63 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 6:58:24 PM | BTC | UP | 1.6 min | -0.097% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 6:56:48 PM | USDJPY | UP | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 6:55:14 PM | NEAR | UP | 4.8 min | -1.128% | 5¢ | ❌ Lost | -$0.15 |
| 9/29 6:44:55 PM | BNB | DOWN | 4 sec | -0.015% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 6:44:55 PM | NATGAS | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 6:44:55 PM | XRP | UP | 4 sec | -0.027% | 0¢ | ❌ Lost | $0.00 |
| 9/29 6:44:23 PM | COPPER | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 6:44:07 PM | SOL | UP | 52 sec | -0.096% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 6:44:07 PM | DOGE | UP | 52 sec | -0.157% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
