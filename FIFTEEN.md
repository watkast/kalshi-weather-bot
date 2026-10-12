# 15-Minute 1¢ Study

*Updated Sun Oct 11, 6:17 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1149 finished bets | 1% | $43.20 | +35% | +3.76¢ | $36.05 / $7.15 |

*Expect about **84 buys a day** (~$12.55/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1098 | $22.25 | +19% |
| 5+ min left, hold to the close | 405 | -$3.85 | -6% |
| Volatility model ≥ 5%, sell at 50¢ | 1149 | -$15.80 | -13% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 14904 | 14897 | 59 (0%) | 1.07% | -$968.45 (-54%) | Hold to the close: -$968.45 (-54%) |

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
| Volatility model | 9984 | 4.5% | 0.4% (42) | -679% | ❌ Worse |
| Momentum model | 9984 | 4.5% | 0.4% (42) | -708% | ❌ Worse |
| Mean-reversion model | 9984 | 7.2% | 0.4% (42) | -783% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 9984 | 42 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2006 | 16 | -7% | -77% | -77% | -74% |
| Volatility model ≥ 5% | 1149 | 12 | +35% | -71% | -70% | -67% |
| Volatility model ≥ 10% | 727 | 8 | +59% | -61% | -61% | -57% |
| Momentum model ≥ 2% | 1769 | 13 | -10% | -78% | -79% | -77% |
| Momentum model ≥ 5% | 1098 | 10 | +19% | -75% | -75% | -72% |
| Momentum model ≥ 10% | 760 | 7 | +32% | -67% | -68% | -64% |
| Mean-reversion model ≥ 2% | 3499 | 25 | -22% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2387 | 19 | -11% | -83% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1605 | 13 | -6% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 10182 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3486 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1229 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 14897 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 59 | 0% | -$968.45 | -54% | — |
| Sell at 2¢ | 507 | 3% | -$1,620.63 | -90% | 33 sec |
| Sell at 3¢ | 334 | 2% | -$1,622.19 | -90% | 47 sec |
| Sell at 5¢ | 245 | 2% | -$1,593.20 | -89% | 50 sec |
| Sell at 10¢ | 162 | 1% | -$1,512.23 | -84% | 64 sec |
| Sell at 25¢ | 93 | 1% | -$1,388.62 | -77% | 81 sec |
| Sell at 50¢ | 61 | 0% | -$1,242.70 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 401 | 4 | 10% | 3% | -5% | -82% | -86% |
| 2–5 min | 4819 | 31 | 6% | 3% | -37% | -88% | -89% |
| 1–2 min | 3922 | 15 | 3% | 2% | -58% | -94% | -94% |
| Under 1 min | 5751 | 9 | 1% | 0% | -77% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1142 | 6 | 4% | 3% | -35% | -90% | -90% |
| HYPE | 1141 | 3 | 4% | 2% | -67% | -90% | -89% |
| DOGE | 1135 | 2 | 4% | 2% | -78% | -91% | -90% |
| BNB | 1133 | 5 | 4% | 2% | -46% | -91% | -92% |
| ETH | 1130 | 8 | 5% | 2% | -14% | -90% | -89% |
| SOL | 1130 | 2 | 3% | 1% | -78% | -93% | -92% |
| BTC | 1126 | 5 | 5% | 2% | -41% | -88% | -91% |
| XRP | 1123 | 7 | 2% | 1% | -22% | -84% | -84% |
| NEAR | 1122 | 6 | 5% | 2% | -30% | -75% | -76% |
| GOLD | 574 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 562 | 1 | 3% | 1% | -79% | -94% | -94% |
| WTI | 535 | 3 | 3% | 1% | -36% | -94% | -96% |
| COPPER | 495 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 457 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 438 | 3 | 3% | 2% | -36% | -95% | -93% |
| PALLADIUM | 425 | 1 | 1% | 0% | -78% | -98% | -99% |
| EURUSD | 419 | 3 | 3% | 2% | -33% | -73% | -72% |
| GBPUSD | 396 | 1 | 3% | 2% | -76% | -96% | -95% |
| USDJPY | 360 | 3 | 1% | 1% | -22% | -98% | -97% |
| USDCAD | 27 | 0 | 0% | 0% | -100% | -100% | -100% |
| AUDUSD | 27 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 7467 | 31 | 3% | 2% | -52% | -89% | -89% |
| DOWN (bought NO) | 7430 | 28 | 3% | 2% | -56% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1855 | 9 | 2% | 1% | -19% | -76% | -76% |
| 0.05–0.1% | 1817 | 6 | 3% | 1% | -53% | -92% | -92% |
| 0.1–0.2% | 2602 | 8 | 4% | 2% | -62% | -91% | -92% |
| 0.2–0.5% | 2789 | 16 | 5% | 3% | -37% | -89% | -88% |
| Over 0.5% | 1116 | 5 | 6% | 2% | -54% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3699 | 20 | 4% | 2% | -37% | -85% | -86% |
| Morning (6am–12pm) | 3615 | 20 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 3575 | 9 | 3% | 1% | -70% | -90% | -91% |
| Evening (6pm–12am) | 4008 | 10 | 3% | 1% | -71% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,521 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/11 6:14:47 PM | BTC | DOWN | 13 sec | +0.016% | 0¢ | ❌ Lost | $0.00 |
| 10/11 6:14:31 PM | HYPE | DOWN | 29 sec | +0.019% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 6:14:31 PM | PALLADIUM | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 6:14:31 PM | BNB | DOWN | 29 sec | -0.003% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 6:14:15 PM | DOGE | DOWN | 45 sec | -0.017% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 6:13:59 PM | ETH | DOWN | 61 sec | +0.102% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 6:13:43 PM | XRP | DOWN | 76 sec | +0.035% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 6:13:27 PM | SOL | UP | 1.5 min | -0.111% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 6:13:27 PM | USDJPY | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 6:12:55 PM | EURUSD | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 6:12:24 PM | COPPER | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 6:12:08 PM | GBPUSD | DOWN | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 6:11:52 PM | NEAR | DOWN | 3.1 min | +0.630% | 72¢ | ❌ Lost | $0.00 |
| 10/11 6:11:20 PM | ZEC | DOWN | 3.6 min | +0.310% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 6:11:20 PM | SILVER | DOWN | 3.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/11 6:10:48 PM | PLATINUM | DOWN | 4.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 6:10:33 PM | GOLD | DOWN | 4.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/11 5:59:39 PM | XRP | UP | 21 sec | -0.043% | 0¢ | ❌ Lost | $0.00 |
| 10/11 5:59:23 PM | HYPE | UP | 37 sec | -0.041% | 0¢ | ❌ Lost | $0.00 |
| 10/11 5:59:23 PM | NEAR | DOWN | 37 sec | +0.114% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 5:59:23 PM | PALLADIUM | UP | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 5:59:23 PM | BNB | UP | 37 sec | -0.035% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 5:58:52 PM | ETH | DOWN | 67 sec | +0.056% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 5:58:52 PM | NATGAS | UP | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 5:58:37 PM | COPPER | UP | 82 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 5:58:37 PM | WTI | UP | 82 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/11 5:58:21 PM | SOL | DOWN | 1.6 min | +0.095% | 0¢ | ❌ Lost | $0.00 |
| 10/11 5:58:21 PM | DOGE | DOWN | 1.6 min | +0.085% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 5:58:21 PM | ZEC | UP | 1.6 min | -0.215% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 5:58:21 PM | SILVER | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
