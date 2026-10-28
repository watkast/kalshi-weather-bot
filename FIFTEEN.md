# 15-Minute 1¢ Study

*Updated Wed Oct 28, 1:21 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3005 finished bets | 1% | $82.20 | +24% | +2.74¢ | $85.80 / -$3.60 |

*Expect about **98 buys a day** (~$14.77/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2788 | $44.00 | +14% |
| Volatility model ≥ 2%, hold to the close | 5566 | $8.15 | +1% |
| Momentum model ≥ 2%, hold to the close | 4602 | -$59.35 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 36816 | 36808 | 138 (0%) | 1.07% | -$2,559.30 (-57%) | Hold to the close: -$2,559.30 (-57%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 22925 | 4.7% | 0.4% (92) | -674% | ❌ Worse |
| Momentum model | 22925 | 4.6% | 0.4% (92) | -698% | ❌ Worse |
| Mean-reversion model | 22925 | 8.1% | 0.4% (92) | -818% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 22925 | 92 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5566 | 49 | +1% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 3005 | 30 | +24% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1704 | 19 | +58% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4602 | 34 | -11% | -81% | -80% | -78% |
| Momentum model ≥ 5% | 2788 | 25 | +14% | -78% | -77% | -74% |
| Momentum model ≥ 10% | 1829 | 17 | +28% | -72% | -71% | -68% |
| Mean-reversion model ≥ 2% | 9364 | 63 | -27% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6566 | 53 | -11% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4389 | 38 | -2% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 23125 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8780 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4903 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 36808 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 138 | 0% | -$2,559.30 | -57% | — |
| Sell at 2¢ | 1405 | 4% | -$3,930.00 | -88% | 47 sec |
| Sell at 3¢ | 965 | 3% | -$3,918.95 | -87% | 48 sec |
| Sell at 5¢ | 670 | 2% | -$3,859.80 | -86% | 62 sec |
| Sell at 10¢ | 408 | 1% | -$3,704.82 | -82% | 65 sec |
| Sell at 25¢ | 218 | 1% | -$3,419.72 | -76% | 83 sec |
| Sell at 50¢ | 143 | 0% | -$3,092.05 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1643 | 8 | 11% | 4% | -54% | -80% | -81% |
| 2–5 min | 11749 | 66 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 9337 | 32 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 14075 | 32 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2589 | 12 | 5% | 2% | -41% | -88% | -88% |
| HYPE | 2583 | 8 | 5% | 3% | -62% | -89% | -87% |
| BNB | 2581 | 15 | 5% | 2% | -27% | -85% | -84% |
| SOL | 2575 | 7 | 4% | 2% | -66% | -92% | -92% |
| ETH | 2569 | 11 | 7% | 3% | -48% | -85% | -85% |
| DOGE | 2567 | 5 | 4% | 2% | -76% | -90% | -90% |
| XRP | 2557 | 11 | 3% | 1% | -47% | -89% | -89% |
| NEAR | 2552 | 12 | 5% | 2% | -39% | -82% | -82% |
| BTC | 2552 | 13 | 5% | 2% | -32% | -88% | -89% |
| GOLD | 1387 | 5 | 4% | 2% | -57% | -81% | -83% |
| SILVER | 1358 | 6 | 4% | 2% | -48% | -82% | -81% |
| WTI | 1336 | 4 | 3% | 1% | -64% | -93% | -94% |
| PLATINUM | 1205 | 1 | 2% | 1% | -92% | -97% | -96% |
| COPPER | 1146 | 4 | 1% | 1% | -67% | -73% | -73% |
| EURUSD | 1128 | 3 | 2% | 1% | -75% | -88% | -88% |
| NATGAS | 1105 | 6 | 2% | 1% | -49% | -79% | -79% |
| GBPUSD | 1069 | 2 | 2% | 1% | -83% | -96% | -96% |
| PALLADIUM | 1068 | 2 | 1% | 0% | -83% | -89% | -90% |
| USDJPY | 1047 | 5 | 2% | 1% | -55% | -97% | -96% |
| AUDUSD | 607 | 4 | 1% | 1% | -38% | -82% | -81% |
| USDCAD | 573 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 175 | 0 | 1% | 1% | -100% | -99% | -99% |
| 10YRRATE | 128 | 0 | 4% | 1% | -100% | -93% | -92% |
| 30YRRATE | 121 | 0 | 1% | 0% | -100% | -99% | -98% |
| 2YRRATE | 118 | 1 | 3% | 1% | -21% | -15% | -14% |
| 5YRRATE | 112 | 1 | 5% | 3% | -17% | -91% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 18624 | 77 | 4% | 2% | -52% | -87% | -86% |
| DOWN (bought NO) | 18184 | 61 | 4% | 2% | -62% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3807 | 19 | 2% | 1% | -14% | -81% | -80% |
| 0.05–0.1% | 3981 | 14 | 3% | 2% | -48% | -92% | -91% |
| 0.1–0.2% | 6027 | 22 | 4% | 2% | -55% | -90% | -89% |
| 0.2–0.5% | 6792 | 29 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2514 | 10 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9229 | 35 | 4% | 2% | -57% | -86% | -86% |
| Morning (6am–12pm) | 9232 | 42 | 4% | 2% | -48% | -86% | -85% |
| Afternoon (12–6pm) | 8534 | 29 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 9813 | 32 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,555 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/28 1:14:57 PM | SOL | UP | 3 sec | -0.046% | 0¢ | ❌ Lost | $0.00 |
| 10/28 1:14:41 PM | HYPE | UP | 19 sec | +0.002% | 0¢ | ❌ Lost | -$0.15 |
| 10/28 1:14:41 PM | COPPER | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 1:14:41 PM | 10YRRATE | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 1:14:41 PM | ETH | DOWN | 19 sec | +0.111% | 0¢ | ❌ Lost | $0.00 |
| 10/28 1:14:41 PM | PALLADIUM | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 1:14:26 PM | DOGE | DOWN | 33 sec | +0.088% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 1:14:26 PM | USDJPY | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 1:14:26 PM | XRP | UP | 33 sec | -0.068% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 1:14:26 PM | BTC | DOWN | 33 sec | +0.099% | 0¢ | ❌ Lost | $0.00 |
| 10/28 1:14:26 PM | PLATINUM | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 1:14:26 PM | ZEC | DOWN | 33 sec | +0.141% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 1:14:26 PM | NEAR | DOWN | 33 sec | +0.309% | 0¢ | ❌ Lost | $0.00 |
| 10/28 1:14:10 PM | AUDUSD | DOWN | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 1:14:10 PM | SILVER | DOWN | 50 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 1:14:10 PM | EURUSD | DOWN | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 1:14:10 PM | BNB | DOWN | 50 sec | +0.035% | 0¢ | ❌ Lost | $0.00 |
| 10/28 1:14:10 PM | BRENT | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 1:13:54 PM | GOLD | DOWN | 66 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/28 1:13:54 PM | GBPUSD | DOWN | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 1:13:38 PM | NATGAS | DOWN | 82 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 1:13:38 PM | 5YRRATE | UP | 82 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 1:13:38 PM | USDCAD | UP | 82 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 1:12:17 PM | 30YRRATE | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 1:12:01 PM | WTI | UP | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 1:09:12 PM | 2YRRATE | UP | 5.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:59:44 PM | COPPER | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:59:28 PM | GBPUSD | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:59:28 PM | AUDUSD | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:59:28 PM | EURUSD | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
