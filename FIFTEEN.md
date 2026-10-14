# 15-Minute 1¢ Study

*Updated Wed Oct 14, 2:54 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1345 finished bets | 1% | $34.85 | +24% | +2.59¢ | $40.15 / -$5.30 |

*Expect about **84 buys a day** (~$12.54/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1272 | $17.50 | +13% |
| 5+ min left, hold to the close | 538 | -$23.20 | -29% |
| Volatility model ≥ 5%, sell at 50¢ | 1345 | -$24.15 | -16% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 17574 | 17567 | 65 (0%) | 1.07% | -$1,217.00 (-57%) | Hold to the close: -$1,217.00 (-57%) |

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
| Volatility model | 11525 | 4.5% | 0.4% (46) | -674% | ❌ Worse |
| Momentum model | 11525 | 4.4% | 0.4% (46) | -700% | ❌ Worse |
| Mean-reversion model | 11525 | 7.2% | 0.4% (46) | -796% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 11525 | 46 | -50% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2391 | 18 | -12% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1345 | 13 | +24% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 822 | 9 | +57% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 2097 | 15 | -13% | -79% | -79% | -77% |
| Momentum model ≥ 5% | 1272 | 11 | +13% | -76% | -76% | -74% |
| Momentum model ≥ 10% | 867 | 8 | +31% | -70% | -69% | -65% |
| Mean-reversion model ≥ 2% | 4168 | 27 | -29% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2843 | 20 | -22% | -83% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1870 | 14 | -13% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 11723 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4264 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1580 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 17567 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 65 | 0% | -$1,217.00 | -57% | — |
| Sell at 2¢ | 602 | 3% | -$1,928.48 | -91% | 33 sec |
| Sell at 3¢ | 403 | 2% | -$1,927.83 | -91% | 46 sec |
| Sell at 5¢ | 293 | 2% | -$1,894.55 | -89% | 48 sec |
| Sell at 10¢ | 186 | 1% | -$1,813.34 | -85% | 63 sec |
| Sell at 25¢ | 103 | 1% | -$1,688.07 | -79% | 67 sec |
| Sell at 50¢ | 66 | 0% | -$1,513.50 | -71% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 534 | 4 | 10% | 2% | -29% | -82% | -88% |
| 2–5 min | 5658 | 32 | 6% | 3% | -44% | -88% | -88% |
| 1–2 min | 4616 | 17 | 3% | 2% | -60% | -94% | -93% |
| Under 1 min | 6755 | 12 | 1% | 0% | -74% | -92% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1314 | 7 | 4% | 2% | -34% | -90% | -90% |
| HYPE | 1310 | 4 | 4% | 2% | -62% | -90% | -89% |
| ETH | 1307 | 8 | 5% | 3% | -25% | -89% | -88% |
| BNB | 1307 | 5 | 4% | 2% | -53% | -90% | -90% |
| DOGE | 1305 | 2 | 4% | 2% | -81% | -91% | -90% |
| SOL | 1302 | 2 | 3% | 1% | -81% | -93% | -92% |
| BTC | 1295 | 6 | 5% | 2% | -39% | -88% | -91% |
| XRP | 1292 | 7 | 2% | 1% | -33% | -85% | -86% |
| NEAR | 1291 | 7 | 5% | 2% | -29% | -78% | -78% |
| GOLD | 696 | 1 | 4% | 1% | -83% | -92% | -93% |
| SILVER | 684 | 2 | 3% | 1% | -66% | -94% | -93% |
| WTI | 651 | 3 | 3% | 1% | -47% | -94% | -96% |
| COPPER | 603 | 0 | 1% | 1% | -100% | -97% | -97% |
| PLATINUM | 573 | 0 | 1% | 0% | -100% | -99% | -99% |
| PALLADIUM | 531 | 1 | 1% | 0% | -82% | -98% | -98% |
| NATGAS | 526 | 3 | 2% | 2% | -47% | -96% | -95% |
| EURUSD | 511 | 3 | 3% | 2% | -45% | -77% | -77% |
| GBPUSD | 481 | 1 | 2% | 1% | -81% | -96% | -96% |
| USDJPY | 439 | 3 | 1% | 1% | -36% | -98% | -98% |
| AUDUSD | 81 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 68 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8839 | 35 | 3% | 2% | -54% | -90% | -90% |
| DOWN (bought NO) | 8728 | 30 | 3% | 2% | -60% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2043 | 10 | 2% | 1% | -18% | -78% | -77% |
| 0.05–0.1% | 2083 | 6 | 3% | 1% | -59% | -92% | -91% |
| 0.1–0.2% | 2998 | 9 | 4% | 2% | -63% | -91% | -91% |
| 0.2–0.5% | 3313 | 18 | 5% | 3% | -40% | -89% | -88% |
| Over 0.5% | 1283 | 5 | 6% | 2% | -60% | -89% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4527 | 20 | 4% | 2% | -50% | -87% | -87% |
| Morning (6am–12pm) | 3923 | 20 | 4% | 2% | -41% | -91% | -91% |
| Afternoon (12–6pm) | 4113 | 10 | 3% | 1% | -71% | -91% | -91% |
| Evening (6pm–12am) | 5004 | 15 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,547 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/14 2:44:46 AM | AUDUSD | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:44:46 AM | USDJPY | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:44:14 AM | COPPER | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:43:22 AM | EURUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:43:22 AM | NATGAS | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:43:06 AM | GBPUSD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:42:50 AM | WTI | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:42:31 AM | PLATINUM | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:42:15 AM | PALLADIUM | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:41:59 AM | NEAR | UP | 3.0 min | -0.885% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 2:41:59 AM | XRP | UP | 3.0 min | -0.414% | 0¢ | ❌ Lost | $0.00 |
| 10/14 2:41:44 AM | ETH | UP | 3.2 min | -0.345% | 0¢ | ❌ Lost | $0.00 |
| 10/14 2:41:27 AM | DOGE | UP | 3.5 min | -0.322% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 2:41:27 AM | ZEC | UP | 3.5 min | -0.572% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 2:41:27 AM | BTC | UP | 3.5 min | -0.202% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 2:41:27 AM | SOL | UP | 3.5 min | -0.331% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 2:41:11 AM | GOLD | UP | 3.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 2:40:20 AM | BNB | UP | 4.7 min | -0.226% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:40:20 AM | HYPE | UP | 4.7 min | -0.457% | 0¢ | ❌ Lost | $0.00 |
| 10/14 2:39:34 AM | SILVER | UP | 5.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 2:29:51 AM | WTI | DOWN | 8 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/14 2:29:35 AM | USDJPY | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:29:35 AM | PALLADIUM | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:29:02 AM | GOLD | UP | 58 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 2:29:02 AM | EURUSD | DOWN | 58 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 2:28:30 AM | BTC | UP | 1.5 min | -0.117% | 0¢ | ❌ Lost | $0.00 |
| 10/14 2:28:12 AM | NATGAS | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:28:12 AM | AUDUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:28:12 AM | PLATINUM | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:27:22 AM | GBPUSD | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
