# 15-Minute 1¢ Study

*Updated Thu Oct 8, 4:00 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 771 finished bets | 1% | $28.90 | +35% | +3.75¢ | -$13.10 / $42.00 |

*Expect about **76 buys a day** (~$11.42/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 763 | $16.70 | +21% |
| 5+ min left, hold to the close | 311 | $10.10 | +22% |
| Volatility model ≥ 5%, sell at 50¢ | 771 | -$1.10 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 11552 | 11533 | 49 (0%) | 1.07% | -$714.10 (-51%) | Hold to the close: -$714.10 (-51%) |

*In play or awaiting result: 18. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 7424 | 4.0% | 0.4% (33) | -563% | ❌ Worse |
| Momentum model | 7424 | 4.1% | 0.4% (33) | -595% | ❌ Worse |
| Mean-reversion model | 7424 | 6.7% | 0.4% (33) | -659% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7424 | 33 | -44% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 1408 | 12 | -1% | -73% | -73% | -69% |
| Volatility model ≥ 5% | 771 | 8 | +35% | -63% | -62% | -59% |
| Volatility model ≥ 10% | 483 | 6 | +82% | -47% | -48% | -43% |
| Momentum model ≥ 2% | 1249 | 10 | -3% | -74% | -76% | -73% |
| Momentum model ≥ 5% | 763 | 7 | +21% | -67% | -69% | -66% |
| Momentum model ≥ 10% | 529 | 6 | +63% | -57% | -58% | -54% |
| Mean-reversion model ≥ 2% | 2551 | 19 | -19% | -84% | -85% | -80% |
| Mean-reversion model ≥ 5% | 1726 | 15 | -4% | -82% | -81% | -76% |
| Mean-reversion model ≥ 10% | 1141 | 11 | +11% | -80% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7621 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 2924 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 988 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 11533 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 49 | 0% | -$714.10 | -51% | — |
| Sell at 2¢ | 400 | 3% | -$1,254.10 | -90% | 33 sec |
| Sell at 3¢ | 267 | 2% | -$1,253.97 | -90% | 47 sec |
| Sell at 5¢ | 198 | 2% | -$1,229.40 | -88% | 56 sec |
| Sell at 10¢ | 131 | 1% | -$1,172.49 | -84% | 64 sec |
| Sell at 25¢ | 75 | 1% | -$1,067.85 | -76% | 82 sec |
| Sell at 50¢ | 49 | 0% | -$943.35 | -67% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 307 | 4 | 11% | 4% | +24% | -81% | -85% |
| 2–5 min | 3741 | 25 | 7% | 3% | -35% | -88% | -88% |
| 1–2 min | 3029 | 12 | 3% | 2% | -57% | -94% | -94% |
| Under 1 min | 4452 | 8 | 1% | 0% | -74% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 854 | 6 | 5% | 3% | -16% | -90% | -90% |
| HYPE | 853 | 3 | 5% | 3% | -57% | -89% | -88% |
| DOGE | 849 | 2 | 3% | 1% | -70% | -92% | -92% |
| BNB | 848 | 3 | 4% | 2% | -57% | -91% | -92% |
| ETH | 847 | 7 | 5% | 3% | +2% | -89% | -88% |
| NEAR | 844 | 5 | 6% | 3% | -22% | -71% | -72% |
| SOL | 843 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 842 | 4 | 5% | 2% | -38% | -88% | -90% |
| XRP | 841 | 5 | 2% | 1% | -25% | -81% | -81% |
| GOLD | 489 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 474 | 0 | 3% | 1% | -100% | -95% | -94% |
| WTI | 452 | 3 | 2% | 1% | -27% | -95% | -97% |
| COPPER | 417 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 380 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 358 | 3 | 3% | 2% | -22% | -95% | -93% |
| PALLADIUM | 354 | 1 | 1% | 1% | -74% | -98% | -99% |
| EURUSD | 353 | 3 | 3% | 2% | -21% | -68% | -66% |
| GBPUSD | 331 | 1 | 3% | 2% | -72% | -95% | -95% |
| USDJPY | 293 | 3 | 1% | 1% | -4% | -98% | -96% |
| AUDUSD | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 5 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5849 | 26 | 4% | 2% | -49% | -89% | -88% |
| DOWN (bought NO) | 5684 | 23 | 3% | 2% | -54% | -91% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1250 | 8 | 2% | 1% | +10% | -66% | -66% |
| 0.05–0.1% | 1302 | 4 | 3% | 1% | -55% | -91% | -92% |
| 0.1–0.2% | 1941 | 6 | 4% | 2% | -61% | -92% | -92% |
| 0.2–0.5% | 2241 | 12 | 6% | 3% | -41% | -89% | -88% |
| Over 0.5% | 885 | 5 | 6% | 2% | -42% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3000 | 17 | 4% | 2% | -35% | -84% | -85% |
| Morning (6am–12pm) | 2706 | 17 | 4% | 2% | -28% | -91% | -90% |
| Afternoon (12–6pm) | 2560 | 7 | 3% | 1% | -68% | -88% | -89% |
| Evening (6pm–12am) | 3267 | 8 | 3% | 1% | -72% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,090 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/8 3:59:45 AM | XRP | UP | 15 sec | -0.028% | — | In play | — |
| 10/8 3:59:45 AM | BTC | DOWN | 15 sec | +0.010% | — | In play | — |
| 10/8 3:59:45 AM | ETH | DOWN | 15 sec | +0.031% | — | In play | — |
| 10/8 3:59:29 AM | BNB | UP | 31 sec | -0.078% | — | In play | — |
| 10/8 3:59:29 AM | SOL | DOWN | 31 sec | +0.041% | — | In play | — |
| 10/8 3:59:13 AM | EURUSD | UP | 47 sec | — | — | In play | — |
| 10/8 3:59:13 AM | ZEC | UP | 47 sec | -0.180% | — | In play | — |
| 10/8 3:58:58 AM | USDJPY | DOWN | 61 sec | — | — | In play | — |
| 10/8 3:58:58 AM | HYPE | DOWN | 61 sec | +0.086% | — | In play | — |
| 10/8 3:58:42 AM | GOLD | DOWN | 77 sec | — | — | In play | — |
| 10/8 3:58:42 AM | DOGE | DOWN | 77 sec | +0.173% | — | In play | — |
| 10/8 3:55:14 AM | NEAR | DOWN | 4.8 min | +0.659% | — | In play | — |
| 10/8 3:44:48 AM | ZEC | UP | 12 sec | -0.018% | 0¢ | ❌ Lost | $0.00 |
| 10/8 3:44:16 AM | USDJPY | DOWN | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 3:44:16 AM | SILVER | UP | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 3:44:01 AM | COPPER | UP | 58 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 3:43:45 AM | EURUSD | UP | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 3:43:29 AM | GOLD | UP | 1.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 3:42:41 AM | HYPE | DOWN | 2.3 min | +0.259% | 0¢ | ❌ Lost | $0.00 |
| 10/8 3:42:25 AM | PALLADIUM | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 3:42:09 AM | XRP | DOWN | 2.8 min | +0.276% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 3:42:09 AM | PLATINUM | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 3:41:37 AM | SOL | DOWN | 3.4 min | +0.214% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 3:41:37 AM | DOGE | DOWN | 3.4 min | +0.316% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 3:41:21 AM | NEAR | DOWN | 3.6 min | +0.555% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 3:41:21 AM | BNB | DOWN | 3.6 min | +0.113% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 3:41:21 AM | BTC | DOWN | 3.6 min | +0.133% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 3:38:55 AM | ETH | DOWN | 6.1 min | +0.267% | 2¢ | ❌ Lost | -$0.15 |
| 10/8 3:29:48 AM | WTI | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 3:29:48 AM | DOGE | DOWN | 12 sec | +0.086% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
