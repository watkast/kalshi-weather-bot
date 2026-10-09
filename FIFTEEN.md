# 15-Minute 1¢ Study

*Updated Thu Oct 8, 9:02 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 828 finished bets | 1% | $36.30 | +40% | +4.38¢ | -$16.25 / $52.55 |

*Expect about **76 buys a day** (~$11.45/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 812 | $24.85 | +29% |
| 5+ min left, hold to the close | 358 | $3.20 | +6% |
| Volatility model ≥ 5%, sell at 50¢ | 828 | -$0.95 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 12418 | 12411 | 51 (0%) | 1.07% | -$793.65 (-53%) | Hold to the close: -$793.65 (-53%) |

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
| Volatility model | 7923 | 4.0% | 0.4% (35) | -564% | ❌ Worse |
| Momentum model | 7923 | 4.1% | 0.4% (35) | -596% | ❌ Worse |
| Mean-reversion model | 7923 | 6.7% | 0.4% (35) | -660% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7923 | 35 | -45% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 1519 | 13 | -1% | -74% | -74% | -70% |
| Volatility model ≥ 5% | 828 | 9 | +40% | -65% | -64% | -60% |
| Volatility model ≥ 10% | 507 | 7 | +104% | -49% | -49% | -44% |
| Momentum model ≥ 2% | 1344 | 11 | -1% | -75% | -77% | -74% |
| Momentum model ≥ 5% | 812 | 8 | +29% | -69% | -70% | -67% |
| Momentum model ≥ 10% | 554 | 6 | +56% | -59% | -60% | -56% |
| Mean-reversion model ≥ 2% | 2745 | 20 | -21% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1854 | 16 | -5% | -82% | -82% | -76% |
| Mean-reversion model ≥ 10% | 1226 | 12 | +13% | -80% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 8120 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3170 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1121 | 2% | 2% | 2% | 1% | 1% | 0% |
| **All** | 12411 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 51 | 0% | -$793.65 | -53% | — |
| Sell at 2¢ | 425 | 3% | -$1,355.15 | -90% | 33 sec |
| Sell at 3¢ | 281 | 2% | -$1,356.06 | -90% | 47 sec |
| Sell at 5¢ | 207 | 2% | -$1,331.10 | -88% | 51 sec |
| Sell at 10¢ | 136 | 1% | -$1,273.49 | -84% | 64 sec |
| Sell at 25¢ | 78 | 1% | -$1,165.47 | -77% | 82 sec |
| Sell at 50¢ | 51 | 0% | -$1,037.40 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 354 | 4 | 11% | 3% | +7% | -81% | -85% |
| 2–5 min | 4036 | 26 | 6% | 3% | -37% | -88% | -89% |
| 1–2 min | 3249 | 13 | 3% | 2% | -57% | -94% | -94% |
| Under 1 min | 4768 | 8 | 1% | 0% | -75% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 909 | 6 | 4% | 3% | -20% | -90% | -90% |
| HYPE | 908 | 3 | 5% | 3% | -59% | -89% | -87% |
| DOGE | 905 | 2 | 3% | 2% | -72% | -92% | -91% |
| BNB | 905 | 4 | 4% | 2% | -47% | -91% | -92% |
| ETH | 903 | 7 | 5% | 3% | -5% | -89% | -88% |
| NEAR | 899 | 5 | 6% | 2% | -27% | -72% | -73% |
| SOL | 898 | 0 | 3% | 1% | -100% | -94% | -93% |
| BTC | 897 | 4 | 5% | 2% | -41% | -87% | -90% |
| XRP | 896 | 6 | 2% | 1% | -16% | -82% | -82% |
| GOLD | 530 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 516 | 0 | 3% | 1% | -100% | -94% | -94% |
| WTI | 489 | 3 | 3% | 1% | -31% | -94% | -96% |
| COPPER | 451 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 412 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 391 | 3 | 3% | 2% | -28% | -95% | -93% |
| EURUSD | 385 | 3 | 3% | 2% | -27% | -70% | -69% |
| PALLADIUM | 381 | 1 | 1% | 1% | -76% | -98% | -99% |
| GBPUSD | 365 | 1 | 3% | 2% | -74% | -95% | -95% |
| USDJPY | 326 | 3 | 1% | 1% | -14% | -98% | -97% |
| AUDUSD | 23 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 22 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6282 | 27 | 4% | 2% | -50% | -89% | -88% |
| DOWN (bought NO) | 6129 | 24 | 3% | 2% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1308 | 8 | 2% | 1% | +5% | -68% | -67% |
| 0.05–0.1% | 1365 | 4 | 3% | 1% | -57% | -92% | -92% |
| 0.1–0.2% | 2060 | 7 | 4% | 2% | -57% | -91% | -92% |
| 0.2–0.5% | 2382 | 13 | 5% | 3% | -40% | -89% | -88% |
| Over 0.5% | 1003 | 5 | 6% | 2% | -49% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3090 | 17 | 4% | 2% | -37% | -85% | -85% |
| Morning (6am–12pm) | 3025 | 17 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 2853 | 8 | 3% | 1% | -67% | -89% | -90% |
| Evening (6pm–12am) | 3443 | 9 | 3% | 1% | -70% | -94% | -94% |

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
| 10/8 8:59:10 PM | NEAR | DOWN | 50 sec | +0.071% | 0¢ | ❌ Lost | $0.00 |
| 10/8 8:58:54 PM | GBPUSD | DOWN | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:58:54 PM | DOGE | DOWN | 66 sec | +0.170% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:58:39 PM | GOLD | DOWN | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:58:39 PM | EURUSD | DOWN | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:58:07 PM | SILVER | DOWN | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:57:35 PM | BTC | DOWN | 2.4 min | +0.163% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:57:35 PM | ETH | DOWN | 2.4 min | +0.263% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:57:19 PM | HYPE | DOWN | 2.7 min | +0.217% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:57:03 PM | ZEC | DOWN | 2.9 min | +0.856% | 0¢ | ❌ Lost | $0.00 |
| 10/8 8:56:47 PM | XRP | DOWN | 3.2 min | +0.324% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:54:09 PM | SOL | DOWN | 5.8 min | +0.797% | 2¢ | ❌ Lost | -$0.15 |
| 10/8 8:53:22 PM | BNB | DOWN | 6.6 min | +0.396% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:44:53 PM | COPPER | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:44:53 PM | GBPUSD | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:44:53 PM | USDJPY | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:44:20 PM | AUDUSD | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:44:20 PM | WTI | UP | 40 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:44:04 PM | PLATINUM | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:44:04 PM | DOGE | DOWN | 56 sec | +0.139% | 0¢ | ❌ Lost | $0.00 |
| 10/8 8:43:49 PM | SILVER | DOWN | 70 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/8 8:43:49 PM | NEAR | DOWN | 70 sec | +0.325% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:43:02 PM | XRP | DOWN | 1.9 min | +0.202% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:42:46 PM | BTC | DOWN | 2.2 min | +0.133% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:42:29 PM | HYPE | DOWN | 2.5 min | +0.260% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:42:29 PM | ZEC | DOWN | 2.5 min | +0.427% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:42:29 PM | SOL | DOWN | 2.5 min | +0.296% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:42:13 PM | PALLADIUM | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:41:42 PM | BNB | DOWN | 3.3 min | +0.060% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:41:42 PM | GOLD | DOWN | 3.3 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
