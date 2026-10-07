# 15-Minute 1¢ Study

*Updated Tue Oct 6, 7:31 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 692 finished bets | 1% | $37.60 | +51% | +5.43¢ | -$9.65 / $47.25 |

*Expect about **79 buys a day** (~$11.82/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 690 | $24.65 | +34% |
| Mean-reversion model ≥ 5%, hold to the close | 1522 | $18.45 | +10% |
| 5+ min left, hold to the close | 260 | $17.45 | +45% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 10087 | 10081 | 46 (0%) | 1.07% | -$573.55 (-47%) | Hold to the close: -$573.55 (-47%) |

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
| Volatility model | 6564 | 4.2% | 0.5% (33) | -560% | ❌ Worse |
| Momentum model | 6564 | 4.2% | 0.5% (33) | -588% | ❌ Worse |
| Mean-reversion model | 6564 | 6.8% | 0.5% (33) | -646% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6564 | 33 | -37% | -86% | -86% | -84% |
| Volatility model ≥ 2% | 1272 | 12 | +10% | -72% | -72% | -68% |
| Volatility model ≥ 5% | 692 | 8 | +51% | -61% | -60% | -57% |
| Volatility model ≥ 10% | 430 | 6 | +107% | -44% | -45% | -40% |
| Momentum model ≥ 2% | 1134 | 10 | +6% | -73% | -75% | -73% |
| Momentum model ≥ 5% | 690 | 7 | +34% | -66% | -68% | -65% |
| Momentum model ≥ 10% | 480 | 6 | +80% | -54% | -55% | -52% |
| Mean-reversion model ≥ 2% | 2249 | 19 | -8% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1522 | 15 | +10% | -81% | -80% | -74% |
| Mean-reversion model ≥ 10% | 1006 | 11 | +27% | -79% | -79% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6761 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2507 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 813 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 10081 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 46 | 0% | -$573.55 | -47% | — |
| Sell at 2¢ | 362 | 4% | -$1,095.43 | -90% | 34 sec |
| Sell at 3¢ | 239 | 2% | -$1,096.34 | -90% | 47 sec |
| Sell at 5¢ | 178 | 2% | -$1,073.85 | -88% | 50 sec |
| Sell at 10¢ | 121 | 1% | -$1,017.04 | -84% | 65 sec |
| Sell at 25¢ | 70 | 1% | -$915.85 | -75% | 82 sec |
| Sell at 50¢ | 46 | 0% | -$795.05 | -65% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 257 | 4 | 10% | 4% | +47% | -82% | -88% |
| 2–5 min | 3241 | 24 | 7% | 3% | -28% | -87% | -88% |
| 1–2 min | 2646 | 11 | 3% | 2% | -55% | -94% | -94% |
| Under 1 min | 3934 | 7 | 1% | 0% | -74% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 765 | 6 | 5% | 3% | -6% | -90% | -89% |
| HYPE | 756 | 3 | 5% | 3% | -51% | -89% | -87% |
| DOGE | 755 | 2 | 3% | 1% | -66% | -92% | -92% |
| ETH | 751 | 7 | 5% | 3% | +16% | -88% | -87% |
| BNB | 749 | 3 | 4% | 2% | -52% | -91% | -92% |
| NEAR | 747 | 5 | 6% | 3% | -12% | -68% | -69% |
| SOL | 747 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 746 | 4 | 5% | 3% | -29% | -87% | -89% |
| XRP | 745 | 5 | 2% | 1% | -15% | -79% | -79% |
| GOLD | 419 | 0 | 4% | 1% | -100% | -92% | -95% |
| SILVER | 407 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 387 | 2 | 3% | 1% | -43% | -95% | -97% |
| COPPER | 362 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 319 | 0 | 0% | 0% | -100% | -99% | -99% |
| NATGAS | 308 | 3 | 3% | 2% | -9% | -94% | -92% |
| PALLADIUM | 305 | 1 | 2% | 1% | -69% | -97% | -98% |
| EURUSD | 294 | 1 | 4% | 2% | -68% | -94% | -92% |
| GBPUSD | 279 | 1 | 3% | 2% | -67% | -94% | -94% |
| USDJPY | 240 | 3 | 2% | 1% | +17% | -97% | -96% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5095 | 24 | 4% | 2% | -45% | -90% | -89% |
| DOWN (bought NO) | 4986 | 22 | 3% | 2% | -49% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1128 | 8 | 2% | 1% | +21% | -64% | -63% |
| 0.05–0.1% | 1170 | 4 | 3% | 1% | -50% | -91% | -92% |
| 0.1–0.2% | 1707 | 6 | 4% | 2% | -56% | -91% | -92% |
| 0.2–0.5% | 1970 | 12 | 6% | 3% | -33% | -88% | -87% |
| Over 0.5% | 784 | 5 | 7% | 3% | -34% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2570 | 15 | 4% | 2% | -32% | -87% | -88% |
| Morning (6am–12pm) | 2536 | 17 | 5% | 3% | -24% | -90% | -89% |
| Afternoon (12–6pm) | 2244 | 7 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 2731 | 7 | 3% | 1% | -70% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,083 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/6 7:29:34 PM | WTI | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 7:29:18 PM | SILVER | UP | 42 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 7:27:59 PM | XRP | UP | 2.0 min | -0.187% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 7:27:59 PM | NATGAS | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 7:27:43 PM | COPPER | UP | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 7:27:27 PM | NEAR | UP | 2.5 min | -0.513% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 7:26:55 PM | DOGE | UP | 3.1 min | -0.202% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 7:26:37 PM | BTC | UP | 3.4 min | -0.164% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 7:26:37 PM | BNB | UP | 3.4 min | -0.146% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 7:26:05 PM | ZEC | UP | 3.9 min | -0.436% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 7:25:32 PM | EURUSD | UP | 4.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 7:24:46 PM | SOL | UP | 5.2 min | -0.304% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 7:24:30 PM | HYPE | UP | 5.5 min | -0.420% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 7:24:14 PM | ETH | UP | 5.8 min | -0.249% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 7:24:14 PM | USDJPY | UP | 5.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 7:14:51 PM | HYPE | UP | 8 sec | -0.037% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 7:14:35 PM | SILVER | UP | 24 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 7:14:35 PM | PLATINUM | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 7:14:35 PM | USDJPY | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 7:14:19 PM | EURUSD | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 7:14:19 PM | NATGAS | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 7:14:03 PM | GOLD | UP | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 7:13:31 PM | ZEC | UP | 88 sec | -0.247% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 7:13:31 PM | BNB | UP | 88 sec | -0.085% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 7:13:15 PM | COPPER | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 7:12:59 PM | DOGE | UP | 2.0 min | -0.124% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 7:12:11 PM | BTC | UP | 2.8 min | -0.156% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 7:11:54 PM | WTI | DOWN | 3.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 7:11:54 PM | SOL | UP | 3.1 min | -0.204% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 7:11:38 PM | XRP | UP | 3.4 min | -0.247% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
