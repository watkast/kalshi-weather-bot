# 15-Minute 1¢ Study

*Updated Thu Oct 8, 8:21 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 825 finished bets | 1% | $36.60 | +41% | +4.44¢ | -$15.95 / $52.55 |

*Expect about **76 buys a day** (~$11.44/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 811 | $24.85 | +29% |
| 5+ min left, hold to the close | 356 | $3.50 | +7% |
| Volatility model ≥ 2%, hold to the close | 1512 | -$0.55 | -0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 12372 | 12365 | 51 (0%) | 1.07% | -$787.80 (-52%) | Hold to the close: -$787.80 (-52%) |

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
| Volatility model | 7896 | 4.0% | 0.4% (35) | -564% | ❌ Worse |
| Momentum model | 7896 | 4.1% | 0.4% (35) | -596% | ❌ Worse |
| Mean-reversion model | 7896 | 6.7% | 0.4% (35) | -660% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7896 | 35 | -44% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 1512 | 13 | -0% | -74% | -74% | -70% |
| Volatility model ≥ 5% | 825 | 9 | +41% | -65% | -64% | -60% |
| Volatility model ≥ 10% | 505 | 7 | +104% | -49% | -49% | -44% |
| Momentum model ≥ 2% | 1339 | 11 | -1% | -75% | -77% | -74% |
| Momentum model ≥ 5% | 811 | 8 | +29% | -69% | -70% | -67% |
| Momentum model ≥ 10% | 553 | 6 | +56% | -59% | -60% | -56% |
| Mean-reversion model ≥ 2% | 2731 | 20 | -20% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1844 | 16 | -4% | -82% | -82% | -76% |
| Mean-reversion model ≥ 10% | 1218 | 12 | +13% | -80% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 8093 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3159 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1113 | 2% | 2% | 2% | 1% | 1% | 0% |
| **All** | 12365 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 51 | 0% | -$787.80 | -52% | — |
| Sell at 2¢ | 425 | 3% | -$1,349.30 | -90% | 33 sec |
| Sell at 3¢ | 281 | 2% | -$1,350.21 | -90% | 47 sec |
| Sell at 5¢ | 207 | 2% | -$1,325.25 | -88% | 51 sec |
| Sell at 10¢ | 136 | 1% | -$1,267.64 | -84% | 64 sec |
| Sell at 25¢ | 78 | 1% | -$1,159.62 | -77% | 82 sec |
| Sell at 50¢ | 51 | 0% | -$1,031.55 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 352 | 4 | 11% | 3% | +8% | -81% | -85% |
| 2–5 min | 4022 | 26 | 6% | 3% | -37% | -88% | -89% |
| 1–2 min | 3234 | 13 | 3% | 2% | -57% | -94% | -94% |
| Under 1 min | 4753 | 8 | 1% | 0% | -75% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 906 | 6 | 4% | 3% | -20% | -90% | -90% |
| HYPE | 905 | 3 | 5% | 3% | -59% | -89% | -87% |
| DOGE | 902 | 2 | 3% | 2% | -72% | -92% | -91% |
| BNB | 902 | 4 | 4% | 2% | -47% | -91% | -92% |
| ETH | 900 | 7 | 5% | 3% | -4% | -89% | -88% |
| NEAR | 896 | 5 | 6% | 2% | -27% | -72% | -73% |
| SOL | 895 | 0 | 3% | 1% | -100% | -94% | -92% |
| BTC | 894 | 4 | 5% | 2% | -41% | -87% | -90% |
| XRP | 893 | 6 | 2% | 1% | -16% | -82% | -82% |
| GOLD | 528 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 513 | 0 | 3% | 1% | -100% | -94% | -94% |
| WTI | 488 | 3 | 3% | 1% | -31% | -94% | -96% |
| COPPER | 449 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 411 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 390 | 3 | 3% | 2% | -28% | -95% | -93% |
| EURUSD | 383 | 3 | 3% | 2% | -27% | -70% | -69% |
| PALLADIUM | 380 | 1 | 1% | 1% | -75% | -98% | -99% |
| GBPUSD | 362 | 1 | 3% | 2% | -74% | -95% | -95% |
| USDJPY | 324 | 3 | 1% | 1% | -14% | -98% | -97% |
| USDCAD | 22 | 0 | 0% | 0% | -100% | -100% | -100% |
| AUDUSD | 22 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6271 | 27 | 4% | 2% | -50% | -89% | -88% |
| DOWN (bought NO) | 6094 | 24 | 3% | 2% | -55% | -91% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1307 | 8 | 2% | 1% | +5% | -68% | -67% |
| 0.05–0.1% | 1361 | 4 | 3% | 1% | -57% | -92% | -92% |
| 0.1–0.2% | 2051 | 7 | 4% | 2% | -57% | -91% | -92% |
| 0.2–0.5% | 2372 | 13 | 5% | 3% | -40% | -89% | -88% |
| Over 0.5% | 1000 | 5 | 6% | 2% | -49% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3090 | 17 | 4% | 2% | -37% | -85% | -85% |
| Morning (6am–12pm) | 3025 | 17 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 2853 | 8 | 3% | 1% | -67% | -89% | -90% |
| Evening (6pm–12am) | 3397 | 9 | 3% | 1% | -70% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,055 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/8 8:14:36 PM | BNB | DOWN | 23 sec | -0.042% | 0¢ | ❌ Lost | $0.00 |
| 10/8 8:14:36 PM | ETH | DOWN | 23 sec | +0.038% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:14:36 PM | HYPE | UP | 23 sec | -0.089% | 0¢ | ❌ Lost | $0.00 |
| 10/8 8:14:20 PM | NATGAS | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:14:04 PM | DOGE | UP | 55 sec | -0.088% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:14:04 PM | XRP | UP | 55 sec | -0.130% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:14:04 PM | WTI | DOWN | 55 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/8 8:14:04 PM | BTC | DOWN | 55 sec | +0.082% | 0¢ | ❌ Lost | $0.00 |
| 10/8 8:13:48 PM | GOLD | UP | 72 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:13:33 PM | SILVER | UP | 87 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:13:33 PM | COPPER | DOWN | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:13:33 PM | SOL | DOWN | 87 sec | +0.208% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:13:01 PM | NEAR | DOWN | 2.0 min | +0.679% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:11:57 PM | GBPUSD | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:11:41 PM | EURUSD | UP | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 8:11:26 PM | ZEC | DOWN | 3.5 min | +0.768% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 8:10:05 PM | USDJPY | DOWN | 4.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 7:59:37 PM | ZEC | DOWN | 22 sec | +0.070% | 0¢ | ❌ Lost | $0.00 |
| 10/8 7:59:37 PM | NEAR | DOWN | 22 sec | +0.260% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 7:59:21 PM | BNB | DOWN | 38 sec | -0.014% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 7:59:21 PM | BTC | UP | 38 sec | -0.037% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 7:59:21 PM | HYPE | UP | 38 sec | -0.119% | 0¢ | ❌ Lost | $0.00 |
| 10/8 7:59:05 PM | PALLADIUM | DOWN | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 7:58:49 PM | COPPER | DOWN | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 7:58:49 PM | SOL | UP | 71 sec | -0.098% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 7:58:49 PM | ETH | UP | 71 sec | -0.078% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 7:58:32 PM | SILVER | DOWN | 88 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/8 7:58:32 PM | GBPUSD | UP | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 7:58:32 PM | EURUSD | UP | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 7:58:16 PM | GOLD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
