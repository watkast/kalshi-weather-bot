# 15-Minute 1¢ Study

*Updated Wed Oct 28, 12:38 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3002 finished bets | 1% | $82.50 | +24% | +2.75¢ | $85.95 / -$3.45 |

*Expect about **98 buys a day** (~$14.77/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2785 | $44.30 | +14% |
| Volatility model ≥ 2%, hold to the close | 5558 | $9.20 | +1% |
| Momentum model ≥ 2%, hold to the close | 4595 | -$58.45 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 36744 | 36735 | 138 (0%) | 1.07% | -$2,549.55 (-57%) | Hold to the close: -$2,549.55 (-57%) |

*In play or awaiting result: 8. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 22898 | 4.7% | 0.4% (92) | -674% | ❌ Worse |
| Momentum model | 22898 | 4.6% | 0.4% (92) | -698% | ❌ Worse |
| Mean-reversion model | 22898 | 8.1% | 0.4% (92) | -818% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 22898 | 92 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5558 | 49 | +1% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 3002 | 30 | +24% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1702 | 19 | +58% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4595 | 34 | -11% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2785 | 25 | +14% | -78% | -77% | -74% |
| Momentum model ≥ 10% | 1827 | 17 | +29% | -72% | -71% | -68% |
| Mean-reversion model ≥ 2% | 9347 | 63 | -26% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6556 | 53 | -11% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4384 | 38 | -2% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 23098 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8759 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4878 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 36735 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 138 | 0% | -$2,549.55 | -57% | — |
| Sell at 2¢ | 1403 | 4% | -$3,920.77 | -87% | 47 sec |
| Sell at 3¢ | 965 | 3% | -$3,909.20 | -87% | 48 sec |
| Sell at 5¢ | 670 | 2% | -$3,850.05 | -86% | 62 sec |
| Sell at 10¢ | 408 | 1% | -$3,695.07 | -82% | 65 sec |
| Sell at 25¢ | 218 | 1% | -$3,409.97 | -76% | 83 sec |
| Sell at 50¢ | 143 | 0% | -$3,082.30 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1638 | 8 | 11% | 4% | -53% | -80% | -81% |
| 2–5 min | 11719 | 66 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 9327 | 32 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 14047 | 32 | 1% | 0% | -68% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2586 | 12 | 5% | 2% | -41% | -88% | -88% |
| HYPE | 2580 | 8 | 5% | 3% | -62% | -89% | -87% |
| BNB | 2578 | 15 | 5% | 2% | -27% | -85% | -84% |
| SOL | 2572 | 7 | 4% | 2% | -66% | -92% | -92% |
| ETH | 2566 | 11 | 7% | 3% | -48% | -85% | -85% |
| DOGE | 2564 | 5 | 4% | 2% | -76% | -90% | -90% |
| XRP | 2554 | 11 | 3% | 1% | -47% | -89% | -89% |
| NEAR | 2549 | 12 | 5% | 2% | -39% | -82% | -82% |
| BTC | 2549 | 13 | 5% | 2% | -32% | -88% | -89% |
| GOLD | 1384 | 5 | 4% | 2% | -57% | -81% | -83% |
| SILVER | 1355 | 6 | 4% | 2% | -48% | -82% | -81% |
| WTI | 1333 | 4 | 3% | 1% | -64% | -93% | -94% |
| PLATINUM | 1202 | 1 | 2% | 1% | -92% | -97% | -96% |
| COPPER | 1143 | 4 | 1% | 1% | -67% | -73% | -73% |
| EURUSD | 1125 | 3 | 2% | 1% | -75% | -88% | -88% |
| NATGAS | 1103 | 6 | 2% | 1% | -49% | -79% | -79% |
| GBPUSD | 1066 | 2 | 2% | 1% | -82% | -96% | -96% |
| PALLADIUM | 1065 | 2 | 1% | 0% | -82% | -89% | -90% |
| USDJPY | 1044 | 5 | 2% | 1% | -55% | -97% | -96% |
| AUDUSD | 604 | 4 | 1% | 1% | -38% | -82% | -81% |
| USDCAD | 571 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 174 | 0 | 1% | 1% | -100% | -99% | -99% |
| 10YRRATE | 125 | 0 | 4% | 1% | -100% | -93% | -92% |
| 30YRRATE | 119 | 0 | 1% | 0% | -100% | -99% | -98% |
| 2YRRATE | 115 | 1 | 3% | 1% | -19% | -13% | -12% |
| 5YRRATE | 109 | 1 | 6% | 3% | -14% | -90% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 18590 | 77 | 4% | 2% | -52% | -87% | -86% |
| DOWN (bought NO) | 18145 | 61 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3804 | 19 | 2% | 1% | -14% | -81% | -80% |
| 0.05–0.1% | 3978 | 14 | 3% | 2% | -48% | -92% | -91% |
| 0.1–0.2% | 6022 | 22 | 5% | 2% | -55% | -90% | -89% |
| 0.2–0.5% | 6786 | 29 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2504 | 10 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9229 | 35 | 4% | 2% | -57% | -86% | -86% |
| Morning (6am–12pm) | 9232 | 42 | 4% | 2% | -48% | -86% | -85% |
| Afternoon (12–6pm) | 8461 | 29 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 9813 | 32 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,559 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/28 12:37:36 PM | USDCAD | UP | 7.4 min | — | — | In play | — |
| 10/28 12:29:52 PM | HYPE | DOWN | 8 sec | +0.007% | 0¢ | ❌ Lost | $0.00 |
| 10/28 12:29:52 PM | EURUSD | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:29:52 PM | ZEC | DOWN | 8 sec | +0.067% | 0¢ | ❌ Lost | $0.00 |
| 10/28 12:29:52 PM | SOL | UP | 8 sec | +0.011% | 0¢ | ❌ Lost | $0.00 |
| 10/28 12:29:36 PM | 5YRRATE | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:29:36 PM | BRENT | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:29:36 PM | NEAR | DOWN | 24 sec | +0.095% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 12:29:36 PM | GOLD | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:29:36 PM | 30YRRATE | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:29:36 PM | 2YRRATE | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:29:36 PM | 10YRRATE | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:29:21 PM | PLATINUM | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:29:21 PM | PALLADIUM | UP | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:29:21 PM | AUDUSD | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:29:03 PM | DOGE | UP | 56 sec | -0.144% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 12:28:47 PM | XRP | DOWN | 72 sec | +0.114% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 12:28:47 PM | NATGAS | UP | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:28:47 PM | ETH | DOWN | 72 sec | +0.115% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 12:28:31 PM | USDCAD | DOWN | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:28:31 PM | BNB | DOWN | 88 sec | +0.078% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 12:27:45 PM | BTC | DOWN | 2.2 min | +0.166% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 12:14:57 PM | PALLADIUM | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:14:57 PM | AUDUSD | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:14:57 PM | BRENT | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:14:57 PM | ETH | DOWN | 3 sec | +0.098% | 0¢ | ❌ Lost | $0.00 |
| 10/28 12:14:41 PM | COPPER | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:14:41 PM | USDJPY | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 12:14:25 PM | DOGE | UP | 35 sec | -0.121% | 0¢ | ❌ Lost | $0.00 |
| 10/28 12:14:10 PM | SOL | UP | 49 sec | -0.167% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
