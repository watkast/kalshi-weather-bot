# 15-Minute 1¢ Study

*Updated Thu Oct 8, 9:13 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 782 finished bets | 1% | $27.70 | +33% | +3.54¢ | -$13.40 / $41.10 |

*Expect about **76 buys a day** (~$11.33/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 774 | $15.50 | +19% |
| 5+ min left, hold to the close | 321 | $8.60 | +18% |
| Volatility model ≥ 5%, sell at 50¢ | 782 | -$2.30 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 11764 | 11743 | 49 (0%) | 1.07% | -$740.50 (-52%) | Hold to the close: -$740.50 (-52%) |

*In play or awaiting result: 20. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 7539 | 4.0% | 0.4% (33) | -565% | ❌ Worse |
| Momentum model | 7539 | 4.1% | 0.4% (33) | -596% | ❌ Worse |
| Mean-reversion model | 7539 | 6.7% | 0.4% (33) | -662% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7539 | 33 | -45% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 1433 | 12 | -3% | -74% | -74% | -70% |
| Volatility model ≥ 5% | 782 | 8 | +33% | -64% | -63% | -59% |
| Volatility model ≥ 10% | 487 | 6 | +82% | -47% | -48% | -43% |
| Momentum model ≥ 2% | 1273 | 10 | -5% | -75% | -76% | -73% |
| Momentum model ≥ 5% | 774 | 7 | +19% | -68% | -69% | -66% |
| Momentum model ≥ 10% | 534 | 6 | +62% | -57% | -58% | -54% |
| Mean-reversion model ≥ 2% | 2595 | 19 | -20% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1755 | 15 | -5% | -82% | -82% | -76% |
| Mean-reversion model ≥ 10% | 1158 | 11 | +10% | -80% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7736 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 2990 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1017 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 11743 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 49 | 0% | -$740.50 | -52% | — |
| Sell at 2¢ | 406 | 3% | -$1,278.94 | -90% | 34 sec |
| Sell at 3¢ | 269 | 2% | -$1,279.59 | -90% | 47 sec |
| Sell at 5¢ | 200 | 2% | -$1,254.50 | -88% | 50 sec |
| Sell at 10¢ | 131 | 1% | -$1,198.89 | -84% | 64 sec |
| Sell at 25¢ | 75 | 1% | -$1,094.25 | -77% | 82 sec |
| Sell at 50¢ | 49 | 0% | -$969.75 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 317 | 4 | 10% | 4% | +20% | -82% | -85% |
| 2–5 min | 3831 | 25 | 7% | 3% | -36% | -88% | -88% |
| 1–2 min | 3079 | 12 | 3% | 2% | -58% | -94% | -94% |
| Under 1 min | 4512 | 8 | 1% | 0% | -74% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 867 | 6 | 4% | 3% | -18% | -90% | -90% |
| HYPE | 866 | 3 | 5% | 3% | -57% | -89% | -88% |
| DOGE | 862 | 2 | 3% | 2% | -71% | -92% | -91% |
| BNB | 861 | 3 | 4% | 2% | -58% | -91% | -92% |
| ETH | 860 | 7 | 5% | 3% | +1% | -89% | -88% |
| NEAR | 856 | 5 | 5% | 3% | -24% | -71% | -72% |
| SOL | 856 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 855 | 4 | 5% | 2% | -39% | -88% | -90% |
| XRP | 853 | 5 | 2% | 1% | -27% | -81% | -82% |
| GOLD | 500 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 486 | 0 | 3% | 1% | -100% | -94% | -94% |
| WTI | 460 | 3 | 3% | 1% | -29% | -95% | -97% |
| COPPER | 428 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 390 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 366 | 3 | 3% | 2% | -23% | -95% | -93% |
| PALLADIUM | 360 | 1 | 1% | 1% | -74% | -98% | -99% |
| EURUSD | 359 | 3 | 3% | 2% | -22% | -68% | -67% |
| GBPUSD | 338 | 1 | 3% | 2% | -72% | -95% | -95% |
| USDJPY | 301 | 3 | 1% | 1% | -7% | -98% | -97% |
| AUDUSD | 10 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 9 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5971 | 26 | 4% | 2% | -50% | -89% | -88% |
| DOWN (bought NO) | 5772 | 23 | 3% | 2% | -54% | -91% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1263 | 8 | 2% | 1% | +9% | -67% | -66% |
| 0.05–0.1% | 1311 | 4 | 3% | 1% | -55% | -91% | -92% |
| 0.1–0.2% | 1967 | 6 | 4% | 2% | -62% | -92% | -92% |
| 0.2–0.5% | 2283 | 12 | 6% | 3% | -42% | -89% | -88% |
| Over 0.5% | 910 | 5 | 6% | 2% | -44% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3090 | 17 | 4% | 2% | -37% | -85% | -85% |
| Morning (6am–12pm) | 2826 | 17 | 4% | 2% | -32% | -91% | -90% |
| Afternoon (12–6pm) | 2560 | 7 | 3% | 1% | -68% | -88% | -89% |
| Evening (6pm–12am) | 3267 | 8 | 3% | 1% | -72% | -94% | -94% |

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
| 10/8 9:13:46 AM | WTI | DOWN | 73 sec | — | — | In play | — |
| 10/8 9:13:31 AM | SILVER | UP | 88 sec | — | — | In play | — |
| 10/8 9:12:28 AM | COPPER | UP | 2.5 min | — | — | In play | — |
| 10/8 9:12:12 AM | GOLD | UP | 2.8 min | — | — | In play | — |
| 10/8 9:11:07 AM | PLATINUM | UP | 3.9 min | — | — | In play | — |
| 10/8 9:10:21 AM | BNB | UP | 4.6 min | -0.396% | — | In play | — |
| 10/8 9:10:05 AM | SOL | UP | 4.9 min | -0.647% | — | In play | — |
| 10/8 9:10:05 AM | BTC | UP | 4.9 min | -0.389% | — | In play | — |
| 10/8 9:09:49 AM | XRP | UP | 5.2 min | -0.790% | — | In play | — |
| 10/8 9:09:18 AM | DOGE | UP | 5.7 min | -0.753% | — | In play | — |
| 10/8 9:08:46 AM | ETH | UP | 6.2 min | -0.441% | — | In play | — |
| 10/8 9:08:46 AM | ZEC | UP | 6.2 min | -2.180% | — | In play | — |
| 10/8 9:08:46 AM | HYPE | UP | 6.2 min | -0.818% | — | In play | — |
| 10/8 9:07:10 AM | NEAR | UP | 7.8 min | -1.214% | — | In play | — |
| 10/8 8:59:52 AM | NATGAS | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:59:52 AM | PALLADIUM | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:59:20 AM | HYPE | DOWN | 40 sec | +0.169% | 0¢ | ❌ Lost | $0.00 |
| 10/8 8:59:04 AM | ZEC | DOWN | 56 sec | +0.313% | 0¢ | ❌ Lost | $0.00 |
| 10/8 8:59:04 AM | BNB | DOWN | 56 sec | +0.061% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:59:04 AM | SILVER | UP | 56 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:58:49 AM | AUDUSD | UP | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:58:49 AM | USDJPY | DOWN | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:58:34 AM | NEAR | DOWN | 85 sec | +0.278% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:58:34 AM | DOGE | DOWN | 85 sec | +0.170% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:58:18 AM | ETH | DOWN | 1.7 min | +0.183% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:58:18 AM | COPPER | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:58:18 AM | XRP | DOWN | 1.7 min | +0.243% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:58:02 AM | SOL | DOWN | 1.9 min | +0.239% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:58:02 AM | BTC | DOWN | 1.9 min | +0.159% | 0¢ | ❌ Lost | $0.00 |
| 10/8 8:57:46 AM | USDCAD | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
