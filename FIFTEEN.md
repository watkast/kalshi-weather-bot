# 15-Minute 1¢ Study

*Updated Wed Oct 7, 6:39 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 735 finished bets | 1% | $33.10 | +42% | +4.50¢ | -$11.45 / $44.55 |

*Expect about **79 buys a day** (~$11.92/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 728 | $20.90 | +27% |
| 5+ min left, hold to the close | 275 | $15.20 | +37% |
| Mean-reversion model ≥ 5%, hold to the close | 1604 | $8.10 | +4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 10702 | 10694 | 49 (0%) | 1.07% | -$608.80 (-47%) | Hold to the close: -$608.80 (-47%) |

*In play or awaiting result: 8. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 6926 | 4.1% | 0.5% (33) | -563% | ❌ Worse |
| Momentum model | 6926 | 4.2% | 0.5% (33) | -592% | ❌ Worse |
| Mean-reversion model | 6926 | 6.8% | 0.5% (33) | -653% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6926 | 33 | -40% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 1342 | 12 | +4% | -73% | -73% | -69% |
| Volatility model ≥ 5% | 735 | 8 | +42% | -62% | -61% | -58% |
| Volatility model ≥ 10% | 458 | 6 | +94% | -46% | -47% | -42% |
| Momentum model ≥ 2% | 1193 | 10 | +1% | -74% | -75% | -73% |
| Momentum model ≥ 5% | 728 | 7 | +27% | -66% | -68% | -66% |
| Momentum model ≥ 10% | 505 | 6 | +72% | -56% | -57% | -54% |
| Mean-reversion model ≥ 2% | 2371 | 19 | -13% | -84% | -84% | -80% |
| Mean-reversion model ≥ 5% | 1604 | 15 | +4% | -81% | -81% | -75% |
| Mean-reversion model ≥ 10% | 1066 | 11 | +19% | -79% | -79% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7123 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2690 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 881 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 10694 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 49 | 0% | -$608.80 | -47% | — |
| Sell at 2¢ | 378 | 4% | -$1,154.52 | -89% | 34 sec |
| Sell at 3¢ | 252 | 2% | -$1,154.52 | -89% | 47 sec |
| Sell at 5¢ | 188 | 2% | -$1,130.60 | -87% | 60 sec |
| Sell at 10¢ | 127 | 1% | -$1,072.43 | -83% | 65 sec |
| Sell at 25¢ | 73 | 1% | -$969.17 | -75% | 82 sec |
| Sell at 50¢ | 48 | 0% | -$844.80 | -65% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 272 | 4 | 10% | 3% | +39% | -83% | -88% |
| 2–5 min | 3445 | 25 | 7% | 3% | -29% | -88% | -88% |
| 1–2 min | 2826 | 12 | 3% | 2% | -54% | -94% | -93% |
| Under 1 min | 4148 | 8 | 1% | 0% | -71% | -88% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 802 | 6 | 5% | 3% | -11% | -89% | -89% |
| HYPE | 798 | 3 | 5% | 3% | -54% | -89% | -87% |
| DOGE | 794 | 2 | 3% | 1% | -68% | -92% | -92% |
| ETH | 792 | 7 | 5% | 3% | +11% | -88% | -88% |
| BNB | 791 | 3 | 4% | 2% | -54% | -91% | -92% |
| NEAR | 789 | 5 | 6% | 3% | -17% | -69% | -70% |
| SOL | 787 | 0 | 3% | 1% | -100% | -94% | -93% |
| BTC | 786 | 4 | 5% | 2% | -33% | -88% | -90% |
| XRP | 784 | 5 | 2% | 1% | -20% | -80% | -80% |
| GOLD | 449 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 439 | 0 | 3% | 1% | -100% | -95% | -94% |
| WTI | 415 | 3 | 3% | 1% | -20% | -95% | -96% |
| COPPER | 385 | 0 | 1% | 1% | -100% | -99% | -99% |
| PLATINUM | 344 | 0 | 0% | 0% | -100% | -99% | -99% |
| NATGAS | 329 | 3 | 3% | 2% | -15% | -94% | -92% |
| PALLADIUM | 329 | 1 | 2% | 1% | -72% | -97% | -98% |
| EURUSD | 322 | 3 | 4% | 2% | -13% | -65% | -63% |
| GBPUSD | 301 | 1 | 3% | 2% | -69% | -95% | -95% |
| USDJPY | 258 | 3 | 2% | 1% | +9% | -97% | -96% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5437 | 26 | 4% | 2% | -44% | -88% | -87% |
| DOWN (bought NO) | 5257 | 23 | 3% | 2% | -50% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1174 | 8 | 2% | 1% | +17% | -65% | -65% |
| 0.05–0.1% | 1234 | 4 | 3% | 1% | -53% | -92% | -92% |
| 0.1–0.2% | 1811 | 6 | 3% | 2% | -58% | -92% | -92% |
| 0.2–0.5% | 2081 | 12 | 6% | 3% | -37% | -88% | -87% |
| Over 0.5% | 821 | 5 | 7% | 3% | -38% | -87% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2890 | 17 | 4% | 2% | -32% | -84% | -84% |
| Morning (6am–12pm) | 2570 | 17 | 5% | 2% | -25% | -90% | -89% |
| Afternoon (12–6pm) | 2244 | 7 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 2990 | 8 | 3% | 1% | -69% | -95% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,018 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/7 6:37:42 AM | HYPE | DOWN | 7.3 min | +0.689% | — | In play | — |
| 10/7 6:36:53 AM | ZEC | DOWN | 8.1 min | +1.232% | — | In play | — |
| 10/7 6:29:31 AM | NATGAS | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:28:25 AM | NEAR | UP | 1.6 min | -0.332% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:28:09 AM | COPPER | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:27:52 AM | SILVER | UP | 2.1 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/7 6:27:52 AM | PLATINUM | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:27:20 AM | PALLADIUM | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:27:20 AM | ZEC | UP | 2.6 min | -0.462% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:27:04 AM | EURUSD | UP | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:27:04 AM | HYPE | UP | 2.9 min | -0.270% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:27:04 AM | GBPUSD | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:26:47 AM | BTC | UP | 3.2 min | -0.205% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:26:31 AM | ETH | UP | 3.5 min | -0.233% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:26:15 AM | GOLD | UP | 3.8 min | — | 1¢ | ❌ Lost | $0.00 |
| 10/7 6:25:59 AM | XRP | UP | 4.0 min | -0.434% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:25:26 AM | BNB | UP | 4.5 min | -0.294% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:24:53 AM | DOGE | UP | 5.1 min | -0.488% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:24:53 AM | SOL | UP | 5.1 min | -0.403% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:14:31 AM | USDJPY | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:14:16 AM | BNB | DOWN | 44 sec | -0.005% | 0¢ | ❌ Lost | $0.00 |
| 10/7 6:14:16 AM | HYPE | DOWN | 44 sec | +0.096% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:14:16 AM | ETH | DOWN | 44 sec | +0.102% | 0¢ | ❌ Lost | $0.00 |
| 10/7 6:13:59 AM | SILVER | UP | 61 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:13:43 AM | SOL | DOWN | 77 sec | +0.125% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:13:27 AM | COPPER | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:13:11 AM | NATGAS | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:12:52 AM | BTC | UP | 2.1 min | -0.142% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:12:36 AM | XRP | DOWN | 2.4 min | +0.277% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:12:20 AM | PLATINUM | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
