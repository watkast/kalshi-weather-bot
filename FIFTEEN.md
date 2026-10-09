# 15-Minute 1¢ Study

*Updated Fri Oct 9, 6:21 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 860 finished bets | 1% | $32.70 | +35% | +3.80¢ | -$17.90 / $50.60 |

*Expect about **77 buys a day** (~$11.48/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 843 | $21.25 | +23% |
| 5+ min left, hold to the close | 376 | $0.50 | +1% |
| Volatility model ≥ 5%, sell at 50¢ | 860 | -$4.55 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 12866 | 12859 | 52 (0%) | 1.07% | -$832.45 (-53%) | Hold to the close: -$832.45 (-53%) |

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
| Volatility model | 8186 | 4.0% | 0.4% (35) | -576% | ❌ Worse |
| Momentum model | 8186 | 4.1% | 0.4% (35) | -610% | ❌ Worse |
| Mean-reversion model | 8186 | 6.7% | 0.4% (35) | -675% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 8186 | 35 | -46% | -87% | -88% | -85% |
| Volatility model ≥ 2% | 1569 | 13 | -4% | -75% | -75% | -71% |
| Volatility model ≥ 5% | 860 | 9 | +35% | -67% | -65% | -62% |
| Volatility model ≥ 10% | 528 | 7 | +95% | -51% | -51% | -46% |
| Momentum model ≥ 2% | 1394 | 11 | -5% | -76% | -77% | -74% |
| Momentum model ≥ 5% | 843 | 8 | +23% | -70% | -71% | -68% |
| Momentum model ≥ 10% | 578 | 6 | +48% | -61% | -62% | -58% |
| Mean-reversion model ≥ 2% | 2843 | 20 | -23% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1925 | 16 | -8% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1264 | 12 | +9% | -81% | -80% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 8383 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3307 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1169 | 2% | 2% | 1% | 1% | 1% | 0% |
| **All** | 12859 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 52 | 0% | -$832.45 | -53% | — |
| Sell at 2¢ | 438 | 3% | -$1,404.57 | -90% | 33 sec |
| Sell at 3¢ | 291 | 2% | -$1,404.96 | -90% | 47 sec |
| Sell at 5¢ | 214 | 2% | -$1,379.35 | -88% | 60 sec |
| Sell at 10¢ | 141 | 1% | -$1,305.74 | -84% | 64 sec |
| Sell at 25¢ | 81 | 1% | -$1,194.34 | -77% | 81 sec |
| Sell at 50¢ | 53 | 0% | -$1,062.70 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 372 | 4 | 10% | 3% | +2% | -82% | -86% |
| 2–5 min | 4162 | 26 | 6% | 3% | -39% | -88% | -89% |
| 1–2 min | 3372 | 13 | 3% | 2% | -58% | -94% | -94% |
| Under 1 min | 4949 | 9 | 1% | 0% | -73% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 938 | 6 | 4% | 3% | -23% | -90% | -90% |
| HYPE | 937 | 3 | 5% | 2% | -60% | -89% | -88% |
| DOGE | 935 | 2 | 3% | 1% | -73% | -92% | -92% |
| BNB | 934 | 4 | 4% | 2% | -48% | -91% | -92% |
| ETH | 933 | 7 | 5% | 2% | -8% | -89% | -88% |
| NEAR | 928 | 5 | 6% | 2% | -29% | -72% | -73% |
| BTC | 927 | 4 | 5% | 2% | -43% | -87% | -90% |
| SOL | 926 | 0 | 3% | 1% | -100% | -94% | -93% |
| XRP | 925 | 6 | 2% | 1% | -19% | -82% | -82% |
| GOLD | 552 | 0 | 4% | 1% | -100% | -92% | -93% |
| SILVER | 537 | 1 | 3% | 1% | -78% | -94% | -93% |
| WTI | 509 | 3 | 3% | 1% | -33% | -94% | -96% |
| COPPER | 474 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 430 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 405 | 3 | 3% | 2% | -31% | -95% | -93% |
| EURUSD | 402 | 3 | 3% | 2% | -30% | -72% | -70% |
| PALLADIUM | 400 | 1 | 1% | 0% | -77% | -98% | -99% |
| GBPUSD | 381 | 1 | 3% | 2% | -76% | -95% | -95% |
| USDJPY | 340 | 3 | 1% | 1% | -18% | -98% | -97% |
| AUDUSD | 24 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 22 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6482 | 27 | 3% | 2% | -52% | -89% | -88% |
| DOWN (bought NO) | 6377 | 25 | 3% | 1% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1353 | 8 | 2% | 1% | +3% | -69% | -68% |
| 0.05–0.1% | 1413 | 4 | 3% | 1% | -58% | -92% | -92% |
| 0.1–0.2% | 2141 | 7 | 4% | 2% | -59% | -92% | -92% |
| 0.2–0.5% | 2447 | 13 | 5% | 3% | -42% | -89% | -88% |
| Over 0.5% | 1027 | 5 | 6% | 2% | -50% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3343 | 18 | 4% | 2% | -38% | -85% | -85% |
| Morning (6am–12pm) | 3042 | 17 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 2853 | 8 | 3% | 1% | -67% | -89% | -90% |
| Evening (6pm–12am) | 3621 | 9 | 3% | 1% | -72% | -95% | -95% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,055 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/9 6:14:53 AM | PALLADIUM | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 6:14:20 AM | XRP | UP | 39 sec | -0.121% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 6:14:20 AM | ETH | DOWN | 39 sec | +0.027% | 0¢ | ❌ Lost | $0.00 |
| 10/9 6:14:20 AM | USDJPY | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 6:13:47 AM | WTI | DOWN | 73 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 6:13:47 AM | BNB | DOWN | 73 sec | +0.090% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 6:13:47 AM | PLATINUM | UP | 73 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 6:13:47 AM | SOL | UP | 73 sec | -0.162% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 6:13:47 AM | NEAR | UP | 73 sec | -0.546% | 0¢ | ❌ Lost | $0.00 |
| 10/9 6:13:31 AM | BTC | DOWN | 89 sec | +0.116% | 0¢ | ❌ Lost | $0.00 |
| 10/9 6:13:31 AM | ZEC | DOWN | 89 sec | +0.231% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 6:13:14 AM | EURUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 6:13:14 AM | HYPE | DOWN | 1.8 min | +0.172% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 6:12:57 AM | GBPUSD | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 6:12:57 AM | COPPER | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 6:12:41 AM | DOGE | DOWN | 2.3 min | +0.212% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 6:11:49 AM | SILVER | UP | 3.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/9 5:59:58 AM | WTI | UP | 1 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/9 5:59:58 AM | EURUSD | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 5:59:26 AM | DOGE | DOWN | 34 sec | +0.024% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 5:59:26 AM | SILVER | DOWN | 34 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/9 5:59:06 AM | PLATINUM | DOWN | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 5:58:50 AM | NEAR | DOWN | 69 sec | +0.348% | 0¢ | ❌ Lost | $0.00 |
| 10/9 5:58:50 AM | PALLADIUM | UP | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 5:58:34 AM | ETH | DOWN | 85 sec | +0.129% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 5:58:34 AM | HYPE | UP | 85 sec | -0.183% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 5:58:20 AM | ZEC | UP | 1.7 min | -0.382% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 5:57:28 AM | BNB | DOWN | 2.5 min | +0.197% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 5:57:14 AM | SOL | DOWN | 2.8 min | +0.417% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 5:56:23 AM | BTC | DOWN | 3.6 min | +0.282% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
