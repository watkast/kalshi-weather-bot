# 15-Minute 1¢ Study

*Updated Tue Oct 6, 10:17 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 660 finished bets | 1% | $27.20 | +38% | +4.12¢ | -$7.85 / $35.05 |

*Expect about **79 buys a day** (~$11.79/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 245 | $19.70 | +54% |
| Momentum model ≥ 5%, hold to the close | 658 | $14.10 | +20% |
| Mean-reversion model ≥ 5%, hold to the close | 1451 | $13.75 | +8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 9593 | 9587 | 45 (0%) | 1.07% | -$524.40 (-45%) | Hold to the close: -$524.40 (-45%) |

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
| Volatility model | 6257 | 4.1% | 0.5% (32) | -542% | ❌ Worse |
| Momentum model | 6257 | 4.1% | 0.5% (32) | -571% | ❌ Worse |
| Mean-reversion model | 6257 | 6.7% | 0.5% (32) | -623% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6257 | 32 | -35% | -86% | -86% | -83% |
| Volatility model ≥ 2% | 1222 | 11 | +5% | -72% | -72% | -68% |
| Volatility model ≥ 5% | 660 | 7 | +38% | -60% | -59% | -55% |
| Volatility model ≥ 10% | 405 | 5 | +86% | -41% | -42% | -37% |
| Momentum model ≥ 2% | 1083 | 9 | +0% | -72% | -74% | -72% |
| Momentum model ≥ 5% | 658 | 6 | +20% | -64% | -67% | -64% |
| Momentum model ≥ 10% | 455 | 5 | +59% | -52% | -53% | -51% |
| Mean-reversion model ≥ 2% | 2149 | 18 | -9% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1451 | 14 | +8% | -80% | -80% | -74% |
| Mean-reversion model ≥ 10% | 954 | 10 | +22% | -78% | -79% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6454 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2365 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 768 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 9587 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 45 | 0% | -$524.40 | -45% | — |
| Sell at 2¢ | 354 | 4% | -$1,034.36 | -90% | 33 sec |
| Sell at 3¢ | 233 | 2% | -$1,035.53 | -90% | 47 sec |
| Sell at 5¢ | 174 | 2% | -$1,013.30 | -88% | 50 sec |
| Sell at 10¢ | 119 | 1% | -$956.51 | -83% | 65 sec |
| Sell at 25¢ | 68 | 1% | -$859.32 | -74% | 82 sec |
| Sell at 50¢ | 44 | 0% | -$745.40 | -65% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 242 | 4 | 10% | 3% | +56% | -82% | -88% |
| 2–5 min | 3092 | 24 | 7% | 3% | -24% | -87% | -87% |
| 1–2 min | 2531 | 11 | 3% | 2% | -53% | -94% | -93% |
| Under 1 min | 3719 | 6 | 1% | 0% | -76% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 731 | 6 | 5% | 3% | -2% | -89% | -89% |
| HYPE | 721 | 3 | 5% | 3% | -49% | -89% | -87% |
| DOGE | 720 | 2 | 4% | 1% | -64% | -91% | -91% |
| ETH | 718 | 7 | 6% | 3% | +23% | -87% | -86% |
| BNB | 715 | 3 | 4% | 2% | -49% | -91% | -92% |
| BTC | 713 | 4 | 5% | 3% | -26% | -87% | -89% |
| SOL | 713 | 0 | 3% | 1% | -100% | -93% | -92% |
| XRP | 712 | 5 | 2% | 1% | -11% | -79% | -79% |
| NEAR | 711 | 4 | 6% | 3% | -26% | -67% | -68% |
| GOLD | 399 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 382 | 0 | 2% | 1% | -100% | -96% | -97% |
| WTI | 361 | 2 | 2% | 1% | -40% | -95% | -97% |
| COPPER | 338 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 304 | 0 | 0% | 0% | -100% | -99% | -99% |
| NATGAS | 292 | 3 | 3% | 2% | -4% | -94% | -92% |
| PALLADIUM | 289 | 1 | 2% | 1% | -68% | -97% | -98% |
| EURUSD | 278 | 1 | 4% | 3% | -66% | -93% | -92% |
| GBPUSD | 266 | 1 | 3% | 2% | -65% | -94% | -94% |
| USDJPY | 224 | 3 | 2% | 1% | +25% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4820 | 23 | 4% | 2% | -44% | -89% | -88% |
| DOWN (bought NO) | 4767 | 22 | 4% | 2% | -47% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1062 | 7 | 2% | 1% | +13% | -62% | -61% |
| 0.05–0.1% | 1106 | 4 | 3% | 1% | -46% | -91% | -92% |
| 0.1–0.2% | 1616 | 6 | 4% | 2% | -53% | -91% | -91% |
| 0.2–0.5% | 1898 | 12 | 6% | 3% | -30% | -88% | -87% |
| Over 0.5% | 770 | 5 | 7% | 3% | -33% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2570 | 15 | 4% | 2% | -32% | -87% | -88% |
| Morning (6am–12pm) | 2438 | 17 | 5% | 3% | -21% | -90% | -89% |
| Afternoon (12–6pm) | 1943 | 6 | 3% | 1% | -63% | -86% | -88% |
| Evening (6pm–12am) | 2636 | 7 | 3% | 1% | -69% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,012 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/6 10:14:50 AM | BNB | DOWN | 9 sec | -0.014% | 0¢ | ❌ Lost | $0.00 |
| 10/6 10:14:34 AM | DOGE | DOWN | 25 sec | +0.066% | 0¢ | ❌ Lost | $0.00 |
| 10/6 10:14:34 AM | BTC | DOWN | 25 sec | +0.031% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 10:14:18 AM | GOLD | UP | 41 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 10:14:18 AM | ZEC | DOWN | 41 sec | +0.117% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 10:14:18 AM | NEAR | DOWN | 41 sec | +0.020% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 10:14:18 AM | XRP | UP | 41 sec | -0.133% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 10:14:02 AM | ETH | DOWN | 57 sec | +0.081% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 10:14:02 AM | HYPE | DOWN | 57 sec | +0.182% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 10:13:31 AM | GBPUSD | UP | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 10:13:31 AM | WTI | DOWN | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 10:13:31 AM | USDJPY | DOWN | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 10:13:15 AM | EURUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 10:12:43 AM | SOL | DOWN | 2.3 min | +0.387% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 9:59:48 AM | PALLADIUM | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 9:59:48 AM | NATGAS | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 9:59:16 AM | USDJPY | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 9:58:12 AM | GOLD | UP | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:57:56 AM | GBPUSD | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 9:57:56 AM | EURUSD | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 9:57:23 AM | COPPER | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 9:57:07 AM | SOL | UP | 2.9 min | -0.304% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:56:50 AM | NEAR | UP | 3.1 min | -0.780% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:56:50 AM | BNB | UP | 3.1 min | -0.225% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:56:50 AM | HYPE | UP | 3.1 min | -0.391% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 9:56:33 AM | BTC | UP | 3.5 min | -0.269% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:56:33 AM | ZEC | UP | 3.5 min | -0.924% | 0¢ | ❌ Lost | $0.00 |
| 10/6 9:55:46 AM | DOGE | UP | 4.2 min | -0.466% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:55:46 AM | ETH | UP | 4.2 min | -0.303% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:55:10 AM | XRP | UP | 4.8 min | -0.588% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
