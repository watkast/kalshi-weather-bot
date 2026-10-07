# 15-Minute 1¢ Study

*Updated Tue Oct 6, 6:51 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 688 finished bets | 1% | $38.20 | +52% | +5.55¢ | -$9.35 / $47.55 |

*Expect about **79 buys a day** (~$11.79/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 686 | $25.25 | +35% |
| Mean-reversion model ≥ 5%, hold to the close | 1517 | $19.20 | +10% |
| 5+ min left, hold to the close | 255 | $18.20 | +48% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 10038 | 10032 | 46 (0%) | 1.07% | -$566.50 (-47%) | Hold to the close: -$566.50 (-47%) |

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
| Volatility model | 6537 | 4.2% | 0.5% (33) | -560% | ❌ Worse |
| Momentum model | 6537 | 4.2% | 0.5% (33) | -586% | ❌ Worse |
| Mean-reversion model | 6537 | 6.8% | 0.5% (33) | -646% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6537 | 33 | -36% | -86% | -86% | -83% |
| Volatility model ≥ 2% | 1268 | 12 | +10% | -72% | -72% | -68% |
| Volatility model ≥ 5% | 688 | 8 | +52% | -61% | -60% | -56% |
| Volatility model ≥ 10% | 427 | 6 | +110% | -44% | -45% | -39% |
| Momentum model ≥ 2% | 1130 | 10 | +7% | -73% | -75% | -72% |
| Momentum model ≥ 5% | 686 | 7 | +35% | -65% | -67% | -65% |
| Momentum model ≥ 10% | 477 | 6 | +82% | -54% | -55% | -51% |
| Mean-reversion model ≥ 2% | 2242 | 19 | -8% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1517 | 15 | +10% | -81% | -80% | -74% |
| Mean-reversion model ≥ 10% | 1003 | 11 | +27% | -79% | -79% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6734 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2490 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 808 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 10032 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 46 | 0% | -$566.50 | -47% | — |
| Sell at 2¢ | 362 | 4% | -$1,088.38 | -90% | 34 sec |
| Sell at 3¢ | 239 | 2% | -$1,089.29 | -90% | 47 sec |
| Sell at 5¢ | 178 | 2% | -$1,066.80 | -88% | 50 sec |
| Sell at 10¢ | 121 | 1% | -$1,009.99 | -83% | 65 sec |
| Sell at 25¢ | 70 | 1% | -$908.80 | -75% | 82 sec |
| Sell at 50¢ | 46 | 0% | -$788.00 | -65% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 252 | 4 | 10% | 4% | +50% | -82% | -87% |
| 2–5 min | 3223 | 24 | 7% | 3% | -27% | -87% | -87% |
| 1–2 min | 2639 | 11 | 3% | 2% | -55% | -94% | -94% |
| Under 1 min | 3915 | 7 | 1% | 0% | -73% | -91% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 762 | 6 | 5% | 3% | -6% | -89% | -89% |
| HYPE | 753 | 3 | 5% | 3% | -51% | -88% | -87% |
| DOGE | 752 | 2 | 3% | 1% | -66% | -92% | -91% |
| ETH | 748 | 7 | 5% | 3% | +17% | -88% | -87% |
| BNB | 746 | 3 | 4% | 2% | -51% | -91% | -92% |
| NEAR | 744 | 5 | 6% | 3% | -12% | -68% | -69% |
| SOL | 744 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 743 | 4 | 5% | 3% | -29% | -87% | -89% |
| XRP | 742 | 5 | 2% | 1% | -15% | -79% | -79% |
| GOLD | 417 | 0 | 4% | 1% | -100% | -92% | -95% |
| SILVER | 404 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 384 | 2 | 3% | 1% | -43% | -95% | -97% |
| COPPER | 359 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 317 | 0 | 0% | 0% | -100% | -99% | -99% |
| NATGAS | 305 | 3 | 3% | 2% | -8% | -94% | -92% |
| PALLADIUM | 304 | 1 | 2% | 1% | -69% | -97% | -98% |
| EURUSD | 291 | 1 | 4% | 2% | -68% | -93% | -92% |
| GBPUSD | 279 | 1 | 3% | 2% | -67% | -94% | -94% |
| USDJPY | 238 | 3 | 2% | 1% | +18% | -97% | -96% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5059 | 24 | 4% | 2% | -45% | -90% | -89% |
| DOWN (bought NO) | 4973 | 22 | 3% | 2% | -49% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1121 | 8 | 2% | 1% | +22% | -64% | -63% |
| 0.05–0.1% | 1168 | 4 | 3% | 1% | -50% | -91% | -92% |
| 0.1–0.2% | 1700 | 6 | 4% | 2% | -55% | -91% | -92% |
| 0.2–0.5% | 1961 | 12 | 6% | 3% | -33% | -88% | -87% |
| Over 0.5% | 782 | 5 | 7% | 3% | -34% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2570 | 15 | 4% | 2% | -32% | -87% | -88% |
| Morning (6am–12pm) | 2536 | 17 | 5% | 3% | -24% | -90% | -89% |
| Afternoon (12–6pm) | 2244 | 7 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 2682 | 7 | 3% | 1% | -70% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,059 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/6 6:44:52 PM | PLATINUM | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 6:44:36 PM | PALLADIUM | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 6:44:05 PM | ZEC | DOWN | 54 sec | +0.146% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 6:44:05 PM | USDJPY | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 6:43:49 PM | SOL | DOWN | 70 sec | +0.118% | 0¢ | ❌ Lost | $0.00 |
| 10/6 6:43:49 PM | XRP | DOWN | 70 sec | +0.100% | 0¢ | ❌ Lost | $0.00 |
| 10/6 6:43:49 PM | BTC | DOWN | 70 sec | +0.076% | 0¢ | ❌ Lost | $0.00 |
| 10/6 6:43:33 PM | SILVER | DOWN | 86 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 6:43:33 PM | COPPER | DOWN | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 6:43:17 PM | DOGE | DOWN | 1.7 min | +0.110% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 6:42:45 PM | ETH | DOWN | 2.2 min | +0.097% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 6:42:29 PM | WTI | UP | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 6:42:29 PM | BNB | DOWN | 2.5 min | +0.062% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 6:41:56 PM | HYPE | DOWN | 3.0 min | +0.249% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 6:40:20 PM | NEAR | DOWN | 4.7 min | +0.911% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 6:29:49 PM | GBPUSD | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 6:29:49 PM | ZEC | UP | 10 sec | -0.059% | 0¢ | ❌ Lost | $0.00 |
| 10/6 6:29:49 PM | COPPER | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 6:29:33 PM | HYPE | UP | 26 sec | -0.021% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 6:29:03 PM | EURUSD | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 6:29:03 PM | PLATINUM | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 6:28:47 PM | PALLADIUM | UP | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 6:28:15 PM | NEAR | DOWN | 1.7 min | +0.323% | 0¢ | ❌ Lost | $0.00 |
| 10/6 6:28:15 PM | XRP | UP | 1.7 min | -0.200% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 6:27:59 PM | BNB | UP | 2.0 min | -0.094% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 6:27:43 PM | SOL | UP | 2.3 min | -0.161% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 6:27:43 PM | WTI | DOWN | 2.3 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/6 6:27:27 PM | SILVER | UP | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 6:27:27 PM | BTC | UP | 2.5 min | -0.154% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 6:27:11 PM | DOGE | UP | 2.8 min | -0.151% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
