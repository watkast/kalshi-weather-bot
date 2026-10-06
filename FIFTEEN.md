# 15-Minute 1¢ Study

*Updated Tue Oct 6, 5:30 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 684 finished bets | 1% | $38.65 | +53% | +5.65¢ | -$9.05 / $47.70 |

*Expect about **79 buys a day** (~$11.81/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 682 | $25.70 | +36% |
| Mean-reversion model ≥ 5%, hold to the close | 1501 | $21.15 | +11% |
| 5+ min left, hold to the close | 253 | $18.50 | +49% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 9961 | 9940 | 46 (0%) | 1.07% | -$555.55 (-46%) | Hold to the close: -$555.55 (-46%) |

*In play or awaiting result: 21. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 6484 | 4.2% | 0.5% (33) | -554% | ❌ Worse |
| Momentum model | 6484 | 4.2% | 0.5% (33) | -581% | ❌ Worse |
| Mean-reversion model | 6484 | 6.8% | 0.5% (33) | -637% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6484 | 33 | -36% | -86% | -86% | -83% |
| Volatility model ≥ 2% | 1261 | 12 | +11% | -72% | -72% | -68% |
| Volatility model ≥ 5% | 684 | 8 | +53% | -61% | -60% | -56% |
| Volatility model ≥ 10% | 424 | 6 | +111% | -43% | -44% | -39% |
| Momentum model ≥ 2% | 1125 | 10 | +7% | -73% | -75% | -72% |
| Momentum model ≥ 5% | 682 | 7 | +36% | -65% | -67% | -64% |
| Momentum model ≥ 10% | 473 | 6 | +84% | -53% | -54% | -51% |
| Mean-reversion model ≥ 2% | 2225 | 19 | -7% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1501 | 15 | +11% | -81% | -80% | -74% |
| Mean-reversion model ≥ 10% | 991 | 11 | +29% | -79% | -79% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6681 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2460 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 799 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 9940 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 46 | 0% | -$555.55 | -46% | — |
| Sell at 2¢ | 360 | 4% | -$1,077.95 | -90% | 33 sec |
| Sell at 3¢ | 237 | 2% | -$1,079.12 | -90% | 47 sec |
| Sell at 5¢ | 177 | 2% | -$1,056.50 | -88% | 50 sec |
| Sell at 10¢ | 121 | 1% | -$999.04 | -83% | 65 sec |
| Sell at 25¢ | 70 | 1% | -$897.85 | -75% | 82 sec |
| Sell at 50¢ | 46 | 0% | -$777.05 | -65% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 250 | 4 | 10% | 4% | +51% | -82% | -87% |
| 2–5 min | 3195 | 24 | 7% | 3% | -27% | -87% | -87% |
| 1–2 min | 2617 | 11 | 3% | 2% | -55% | -94% | -93% |
| Under 1 min | 3875 | 7 | 1% | 0% | -73% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 756 | 6 | 5% | 3% | -5% | -89% | -89% |
| HYPE | 748 | 3 | 5% | 3% | -51% | -89% | -87% |
| DOGE | 746 | 2 | 3% | 1% | -66% | -92% | -91% |
| ETH | 742 | 7 | 5% | 3% | +18% | -87% | -87% |
| BNB | 740 | 3 | 4% | 2% | -51% | -91% | -92% |
| NEAR | 738 | 5 | 6% | 3% | -11% | -67% | -68% |
| SOL | 738 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 737 | 4 | 5% | 3% | -29% | -87% | -89% |
| XRP | 736 | 5 | 1% | 1% | -14% | -79% | -79% |
| GOLD | 413 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 398 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 380 | 2 | 3% | 1% | -43% | -95% | -97% |
| COPPER | 354 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 312 | 0 | 0% | 0% | -100% | -99% | -99% |
| NATGAS | 304 | 3 | 3% | 2% | -8% | -94% | -92% |
| PALLADIUM | 299 | 1 | 2% | 1% | -69% | -97% | -98% |
| EURUSD | 288 | 1 | 4% | 2% | -68% | -93% | -92% |
| GBPUSD | 277 | 1 | 3% | 2% | -66% | -94% | -94% |
| USDJPY | 234 | 3 | 2% | 1% | +20% | -97% | -96% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5016 | 24 | 4% | 2% | -44% | -89% | -89% |
| DOWN (bought NO) | 4924 | 22 | 3% | 2% | -49% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1109 | 8 | 2% | 1% | +23% | -63% | -63% |
| 0.05–0.1% | 1150 | 4 | 3% | 1% | -49% | -91% | -92% |
| 0.1–0.2% | 1685 | 6 | 4% | 2% | -55% | -92% | -92% |
| 0.2–0.5% | 1956 | 12 | 6% | 3% | -33% | -88% | -87% |
| Over 0.5% | 779 | 5 | 7% | 3% | -34% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2570 | 15 | 4% | 2% | -32% | -87% | -88% |
| Morning (6am–12pm) | 2536 | 17 | 5% | 3% | -24% | -90% | -89% |
| Afternoon (12–6pm) | 2198 | 7 | 3% | 1% | -62% | -88% | -89% |
| Evening (6pm–12am) | 2636 | 7 | 3% | 1% | -69% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,084 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/6 5:29:48 PM | BNB | DOWN | 12 sec | -0.001% | — | In play | — |
| 10/6 5:29:32 PM | WTI | DOWN | 28 sec | — | — | In play | — |
| 10/6 5:29:32 PM | BTC | UP | 28 sec | -0.007% | — | In play | — |
| 10/6 5:29:16 PM | DOGE | DOWN | 44 sec | +0.092% | — | In play | — |
| 10/6 5:29:01 PM | SOL | UP | 58 sec | -0.115% | — | In play | — |
| 10/6 5:29:01 PM | PLATINUM | DOWN | 58 sec | — | — | In play | — |
| 10/6 5:28:43 PM | ETH | UP | 76 sec | -0.051% | — | In play | — |
| 10/6 5:28:11 PM | COPPER | DOWN | 1.8 min | — | — | In play | — |
| 10/6 5:27:57 PM | GOLD | DOWN | 2.0 min | — | — | In play | — |
| 10/6 5:27:41 PM | PALLADIUM | DOWN | 2.3 min | — | — | In play | — |
| 10/6 5:27:41 PM | XRP | DOWN | 2.3 min | +0.073% | — | In play | — |
| 10/6 5:27:25 PM | HYPE | DOWN | 2.6 min | +0.179% | — | In play | — |
| 10/6 5:26:21 PM | ZEC | DOWN | 3.6 min | +0.587% | — | In play | — |
| 10/6 5:26:21 PM | NEAR | DOWN | 3.6 min | +0.309% | — | In play | — |
| 10/6 5:26:05 PM | SILVER | DOWN | 3.9 min | — | — | In play | — |
| 10/6 5:14:49 PM | BNB | UP | 10 sec | -0.041% | 0¢ | ❌ Lost | $0.00 |
| 10/6 5:14:33 PM | HYPE | UP | 26 sec | -0.029% | 0¢ | ❌ Lost | $0.00 |
| 10/6 5:14:33 PM | XRP | DOWN | 26 sec | -0.020% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 5:14:33 PM | BTC | UP | 26 sec | -0.057% | 0¢ | ❌ Lost | $0.00 |
| 10/6 5:14:17 PM | SOL | UP | 42 sec | -0.056% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 5:14:17 PM | WTI | DOWN | 42 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 5:14:03 PM | GOLD | DOWN | 56 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 5:14:03 PM | SILVER | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 5:13:31 PM | GBPUSD | UP | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 5:13:31 PM | EURUSD | UP | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 5:12:42 PM | ETH | DOWN | 2.3 min | +0.069% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 5:12:26 PM | USDJPY | DOWN | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 5:11:22 PM | DOGE | DOWN | 3.6 min | +0.177% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 5:11:22 PM | NEAR | DOWN | 3.6 min | +0.253% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 5:09:28 PM | ZEC | DOWN | 5.5 min | +0.644% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
