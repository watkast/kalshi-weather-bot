# 15-Minute 1¢ Study

*Updated Tue Oct 6, 2:06 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 636 finished bets | 1% | $29.90 | +44% | +4.70¢ | -$6.95 / $36.85 |

*Expect about **79 buys a day** (~$11.84/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 635 | $16.35 | +24% |
| Volatility model ≥ 2%, hold to the close | 1182 | $11.80 | +8% |
| Mean-reversion model ≥ 5%, hold to the close | 1400 | $6.50 | +4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 9286 | 9280 | 40 (0%) | 1.07% | -$556.75 (-50%) | Hold to the close: -$556.75 (-50%) |

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
| Volatility model | 6077 | 4.0% | 0.5% (28) | -569% | ❌ Worse |
| Momentum model | 6077 | 4.1% | 0.5% (28) | -593% | ❌ Worse |
| Mean-reversion model | 6077 | 6.7% | 0.5% (28) | -667% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6077 | 28 | -42% | -86% | -86% | -83% |
| Volatility model ≥ 2% | 1182 | 11 | +8% | -71% | -71% | -66% |
| Volatility model ≥ 5% | 636 | 7 | +44% | -58% | -57% | -54% |
| Volatility model ≥ 10% | 392 | 5 | +91% | -39% | -40% | -35% |
| Momentum model ≥ 2% | 1045 | 9 | +4% | -71% | -73% | -71% |
| Momentum model ≥ 5% | 635 | 6 | +24% | -63% | -65% | -63% |
| Momentum model ≥ 10% | 439 | 5 | +64% | -51% | -52% | -49% |
| Mean-reversion model ≥ 2% | 2083 | 15 | -21% | -83% | -83% | -79% |
| Mean-reversion model ≥ 5% | 1400 | 13 | +4% | -80% | -80% | -73% |
| Mean-reversion model ≥ 10% | 924 | 9 | +13% | -78% | -78% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6274 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 2272 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 734 | 3% | 3% | 2% | 1% | 1% | 0% |
| **All** | 9280 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 40 | 0% | -$556.75 | -50% | — |
| Sell at 2¢ | 344 | 4% | -$999.31 | -89% | 33 sec |
| Sell at 3¢ | 225 | 2% | -$1,001.00 | -90% | 47 sec |
| Sell at 5¢ | 166 | 2% | -$980.85 | -88% | 56 sec |
| Sell at 10¢ | 112 | 1% | -$928.03 | -83% | 66 sec |
| Sell at 25¢ | 62 | 1% | -$841.53 | -75% | 82 sec |
| Sell at 50¢ | 39 | 0% | -$741.50 | -66% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 237 | 3 | 10% | 3% | +20% | -82% | -89% |
| 2–5 min | 2990 | 21 | 7% | 3% | -31% | -87% | -87% |
| 1–2 min | 2443 | 11 | 3% | 2% | -51% | -93% | -93% |
| Under 1 min | 3607 | 5 | 1% | 0% | -79% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 710 | 5 | 5% | 3% | -16% | -89% | -89% |
| HYPE | 701 | 3 | 5% | 3% | -47% | -89% | -86% |
| DOGE | 700 | 2 | 4% | 1% | -63% | -91% | -91% |
| ETH | 699 | 7 | 6% | 3% | +26% | -87% | -86% |
| BNB | 695 | 2 | 4% | 2% | -65% | -91% | -92% |
| XRP | 693 | 4 | 1% | 1% | -27% | -78% | -79% |
| SOL | 693 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 692 | 3 | 5% | 2% | -43% | -87% | -90% |
| NEAR | 691 | 4 | 6% | 3% | -25% | -66% | -67% |
| GOLD | 383 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 365 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 347 | 2 | 3% | 1% | -38% | -95% | -97% |
| COPPER | 324 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 290 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 285 | 2 | 3% | 2% | -35% | -95% | -93% |
| PALLADIUM | 278 | 1 | 2% | 1% | -66% | -97% | -98% |
| EURUSD | 265 | 1 | 4% | 3% | -65% | -93% | -91% |
| GBPUSD | 252 | 1 | 4% | 2% | -63% | -94% | -94% |
| USDJPY | 217 | 3 | 2% | 1% | +29% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4700 | 22 | 4% | 2% | -45% | -89% | -88% |
| DOWN (bought NO) | 4580 | 18 | 4% | 2% | -55% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1033 | 7 | 2% | 1% | +16% | -61% | -60% |
| 0.05–0.1% | 1076 | 4 | 3% | 1% | -45% | -91% | -92% |
| 0.1–0.2% | 1573 | 6 | 4% | 2% | -51% | -91% | -91% |
| 0.2–0.5% | 1837 | 9 | 6% | 3% | -46% | -88% | -87% |
| Over 0.5% | 753 | 4 | 7% | 3% | -45% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2340 | 10 | 4% | 2% | -51% | -86% | -87% |
| Morning (6am–12pm) | 2361 | 17 | 5% | 3% | -18% | -90% | -88% |
| Afternoon (12–6pm) | 1943 | 6 | 3% | 1% | -63% | -86% | -88% |
| Evening (6pm–12am) | 2636 | 7 | 3% | 1% | -69% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,096 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/6 1:59:46 AM | GOLD | DOWN | 13 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 1:59:46 AM | HYPE | UP | 13 sec | -0.075% | 0¢ | ❌ Lost | $0.00 |
| 10/6 1:59:30 AM | SILVER | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 1:59:14 AM | SOL | DOWN | 45 sec | +0.056% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 1:59:14 AM | DOGE | DOWN | 45 sec | +0.066% | 0¢ | ❌ Lost | $0.00 |
| 10/6 1:59:14 AM | GBPUSD | DOWN | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 1:58:42 AM | XRP | DOWN | 78 sec | +0.100% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 1:58:26 AM | ETH | DOWN | 1.6 min | +0.118% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 1:58:10 AM | PLATINUM | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 1:57:36 AM | EURUSD | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 1:55:46 AM | ZEC | DOWN | 4.2 min | +0.321% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 1:55:46 AM | BTC | DOWN | 4.2 min | +0.152% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 1:55:46 AM | NEAR | DOWN | 4.2 min | +0.775% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 1:44:32 AM | HYPE | DOWN | 28 sec | +0.012% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 1:44:16 AM | NATGAS | UP | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 1:44:16 AM | GOLD | DOWN | 44 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 1:43:28 AM | COPPER | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 1:42:06 AM | DOGE | DOWN | 2.9 min | +0.189% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 1:41:51 AM | EURUSD | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 1:41:04 AM | GBPUSD | DOWN | 3.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 1:40:47 AM | SOL | DOWN | 4.2 min | +0.293% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 1:40:47 AM | XRP | DOWN | 4.2 min | +0.214% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 1:40:32 AM | ZEC | DOWN | 4.5 min | +0.381% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 1:40:32 AM | BTC | DOWN | 4.5 min | +0.221% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 1:40:16 AM | NEAR | DOWN | 4.7 min | +0.746% | 0¢ | ❌ Lost | $0.00 |
| 10/6 1:40:16 AM | BNB | DOWN | 4.7 min | +0.109% | 0¢ | ❌ Lost | $0.00 |
| 10/6 1:39:44 AM | ETH | DOWN | 5.3 min | +0.199% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 1:29:49 AM | NATGAS | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 1:29:49 AM | GOLD | UP | 11 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 1:29:49 AM | SOL | DOWN | 11 sec | +0.037% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
