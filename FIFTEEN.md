# 15-Minute 1¢ Study

*Updated Wed Oct 28, 4:48 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3032 finished bets | 1% | $79.35 | +23% | +2.62¢ | $84.30 / -$4.95 |

*Expect about **99 buys a day** (~$14.83/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2817 | $41.30 | +13% |
| Volatility model ≥ 2%, hold to the close | 5610 | $3.20 | +0% |
| Momentum model ≥ 2%, hold to the close | 4641 | -$63.55 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 37050 | 37042 | 138 (0%) | 1.07% | -$2,588.70 (-57%) | Hold to the close: -$2,588.70 (-57%) |

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
| Volatility model | 23047 | 4.7% | 0.4% (92) | -676% | ❌ Worse |
| Momentum model | 23047 | 4.6% | 0.4% (92) | -700% | ❌ Worse |
| Mean-reversion model | 23047 | 8.1% | 0.4% (92) | -820% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 23047 | 92 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5610 | 49 | +0% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 3032 | 30 | +23% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1718 | 19 | +57% | -68% | -66% | -64% |
| Momentum model ≥ 2% | 4641 | 34 | -12% | -81% | -80% | -78% |
| Momentum model ≥ 5% | 2817 | 25 | +13% | -78% | -77% | -74% |
| Momentum model ≥ 10% | 1845 | 17 | +27% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9426 | 63 | -27% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6609 | 53 | -11% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4413 | 38 | -3% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 23247 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8840 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4955 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 37042 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 138 | 0% | -$2,588.70 | -57% | — |
| Sell at 2¢ | 1411 | 4% | -$3,957.84 | -88% | 47 sec |
| Sell at 3¢ | 970 | 3% | -$3,946.40 | -87% | 48 sec |
| Sell at 5¢ | 672 | 2% | -$3,887.90 | -86% | 63 sec |
| Sell at 10¢ | 408 | 1% | -$3,734.22 | -83% | 65 sec |
| Sell at 25¢ | 218 | 1% | -$3,449.12 | -76% | 83 sec |
| Sell at 50¢ | 143 | 0% | -$3,121.45 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1657 | 8 | 11% | 4% | -54% | -80% | -81% |
| 2–5 min | 11831 | 66 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 9393 | 32 | 3% | 1% | -63% | -92% | -92% |
| Under 1 min | 14157 | 32 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2602 | 12 | 5% | 2% | -41% | -88% | -88% |
| HYPE | 2596 | 8 | 5% | 3% | -62% | -89% | -87% |
| BNB | 2595 | 15 | 5% | 2% | -28% | -85% | -84% |
| SOL | 2589 | 7 | 4% | 2% | -66% | -92% | -91% |
| ETH | 2583 | 11 | 7% | 3% | -48% | -85% | -85% |
| DOGE | 2581 | 5 | 4% | 2% | -76% | -90% | -90% |
| XRP | 2570 | 11 | 3% | 1% | -47% | -89% | -89% |
| NEAR | 2566 | 12 | 5% | 2% | -39% | -82% | -82% |
| BTC | 2565 | 13 | 5% | 2% | -32% | -88% | -89% |
| GOLD | 1394 | 5 | 4% | 2% | -57% | -82% | -83% |
| SILVER | 1365 | 6 | 4% | 2% | -48% | -82% | -81% |
| WTI | 1347 | 4 | 3% | 1% | -65% | -93% | -94% |
| PLATINUM | 1211 | 1 | 2% | 1% | -92% | -97% | -96% |
| COPPER | 1150 | 4 | 1% | 1% | -68% | -73% | -73% |
| EURUSD | 1134 | 3 | 2% | 1% | -75% | -88% | -88% |
| NATGAS | 1114 | 6 | 2% | 1% | -50% | -80% | -79% |
| GBPUSD | 1076 | 2 | 2% | 1% | -83% | -96% | -96% |
| PALLADIUM | 1074 | 2 | 1% | 0% | -83% | -89% | -90% |
| USDJPY | 1057 | 5 | 2% | 1% | -56% | -97% | -96% |
| AUDUSD | 611 | 4 | 1% | 1% | -39% | -82% | -81% |
| USDCAD | 578 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 185 | 0 | 1% | 1% | -100% | -99% | -99% |
| 10YRRATE | 133 | 0 | 5% | 1% | -100% | -92% | -90% |
| 30YRRATE | 125 | 0 | 1% | 0% | -100% | -99% | -98% |
| 2YRRATE | 124 | 1 | 4% | 1% | -25% | -18% | -16% |
| 5YRRATE | 117 | 1 | 6% | 3% | -20% | -90% | -91% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 18735 | 77 | 4% | 2% | -53% | -87% | -87% |
| DOWN (bought NO) | 18307 | 61 | 4% | 2% | -62% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3821 | 19 | 2% | 1% | -14% | -81% | -80% |
| 0.05–0.1% | 3996 | 14 | 3% | 2% | -48% | -92% | -91% |
| 0.1–0.2% | 6054 | 22 | 4% | 2% | -55% | -90% | -89% |
| 0.2–0.5% | 6848 | 29 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2524 | 10 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9229 | 35 | 4% | 2% | -57% | -86% | -86% |
| Morning (6am–12pm) | 9232 | 42 | 4% | 2% | -48% | -86% | -85% |
| Afternoon (12–6pm) | 8768 | 29 | 4% | 2% | -61% | -88% | -88% |
| Evening (6pm–12am) | 9813 | 32 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,556 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/28 4:44:56 PM | DOGE | DOWN | 3 sec | +0.064% | 0¢ | ❌ Lost | $0.00 |
| 10/28 4:44:56 PM | GBPUSD | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:44:40 PM | WTI | DOWN | 20 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 4:44:40 PM | USDCAD | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:44:22 PM | BRENT | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:44:22 PM | ZEC | DOWN | 38 sec | +0.048% | 0¢ | ❌ Lost | $0.00 |
| 10/28 4:44:22 PM | HYPE | UP | 38 sec | -0.117% | 0¢ | ❌ Lost | $0.00 |
| 10/28 4:44:22 PM | SOL | DOWN | 38 sec | +0.050% | 0¢ | ❌ Lost | $0.00 |
| 10/28 4:44:22 PM | XRP | DOWN | 38 sec | +0.015% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 4:44:06 PM | AUDUSD | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:44:06 PM | NEAR | UP | 54 sec | -0.245% | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:43:50 PM | EURUSD | DOWN | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:43:35 PM | BNB | DOWN | 84 sec | +0.028% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 4:43:35 PM | BTC | DOWN | 84 sec | +0.063% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 4:43:19 PM | NATGAS | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:43:03 PM | ETH | DOWN | 1.9 min | +0.101% | 1¢ | ❌ Lost | $0.00 |
| 10/28 4:41:43 PM | USDJPY | UP | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:29:52 PM | USDCAD | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:29:36 PM | WTI | UP | 24 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/28 4:29:36 PM | BRENT | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:29:03 PM | BNB | DOWN | 56 sec | +0.042% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 4:28:17 PM | USDJPY | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:28:17 PM | ZEC | DOWN | 1.7 min | +0.361% | 0¢ | ❌ Lost | $0.00 |
| 10/28 4:28:00 PM | NATGAS | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:26:54 PM | PALLADIUM | UP | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:26:38 PM | NEAR | UP | 3.4 min | -0.521% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 4:26:22 PM | SOL | UP | 3.6 min | -0.298% | 5¢ | ❌ Lost | -$0.15 |
| 10/28 4:26:07 PM | ETH | UP | 3.9 min | -0.231% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 4:25:33 PM | DOGE | UP | 4.5 min | -0.308% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 4:25:33 PM | BTC | UP | 4.5 min | -0.187% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
