# 15-Minute 1¢ Study

*Updated Wed Oct 14, 1:37 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1343 finished bets | 1% | $35.15 | +24% | +2.62¢ | $26.30 / $8.85 |

*Expect about **84 buys a day** (~$12.56/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1270 | $17.80 | +13% |
| 5+ min left, hold to the close | 524 | -$21.10 | -27% |
| Volatility model ≥ 5%, sell at 50¢ | 1343 | -$23.85 | -16% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 17487 | 17480 | 65 (0%) | 1.07% | -$1,205.15 (-57%) | Hold to the close: -$1,205.15 (-57%) |

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
| Volatility model | 11481 | 4.5% | 0.4% (46) | -672% | ❌ Worse |
| Momentum model | 11481 | 4.4% | 0.4% (46) | -698% | ❌ Worse |
| Mean-reversion model | 11481 | 7.2% | 0.4% (46) | -793% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 11481 | 46 | -50% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2385 | 18 | -12% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1343 | 13 | +24% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 821 | 9 | +58% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 2095 | 15 | -13% | -79% | -79% | -77% |
| Momentum model ≥ 5% | 1270 | 11 | +13% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 865 | 8 | +31% | -70% | -69% | -64% |
| Mean-reversion model ≥ 2% | 4145 | 27 | -29% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2827 | 20 | -21% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1861 | 14 | -13% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 11679 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4239 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1562 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 17480 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 65 | 0% | -$1,205.15 | -57% | — |
| Sell at 2¢ | 602 | 3% | -$1,916.63 | -91% | 33 sec |
| Sell at 3¢ | 403 | 2% | -$1,915.98 | -91% | 46 sec |
| Sell at 5¢ | 293 | 2% | -$1,882.70 | -89% | 48 sec |
| Sell at 10¢ | 186 | 1% | -$1,801.49 | -85% | 63 sec |
| Sell at 25¢ | 103 | 1% | -$1,676.22 | -79% | 67 sec |
| Sell at 50¢ | 66 | 0% | -$1,501.65 | -71% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 520 | 4 | 10% | 2% | -27% | -82% | -87% |
| 2–5 min | 5624 | 32 | 6% | 3% | -44% | -88% | -88% |
| 1–2 min | 4598 | 17 | 3% | 2% | -60% | -94% | -93% |
| Under 1 min | 6734 | 12 | 1% | 0% | -74% | -92% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1310 | 7 | 4% | 2% | -33% | -90% | -90% |
| HYPE | 1305 | 4 | 4% | 2% | -62% | -90% | -89% |
| ETH | 1302 | 8 | 5% | 3% | -25% | -89% | -88% |
| BNB | 1302 | 5 | 4% | 2% | -53% | -90% | -90% |
| DOGE | 1300 | 2 | 4% | 2% | -81% | -91% | -90% |
| SOL | 1297 | 2 | 3% | 1% | -81% | -93% | -92% |
| BTC | 1290 | 6 | 5% | 2% | -38% | -88% | -91% |
| XRP | 1287 | 7 | 2% | 1% | -33% | -85% | -86% |
| NEAR | 1286 | 7 | 5% | 2% | -29% | -77% | -78% |
| GOLD | 693 | 1 | 4% | 1% | -83% | -92% | -93% |
| SILVER | 681 | 2 | 3% | 1% | -66% | -94% | -93% |
| WTI | 646 | 3 | 3% | 1% | -46% | -94% | -96% |
| COPPER | 599 | 0 | 2% | 1% | -100% | -97% | -97% |
| PLATINUM | 569 | 0 | 1% | 0% | -100% | -99% | -99% |
| PALLADIUM | 528 | 1 | 1% | 0% | -82% | -98% | -98% |
| NATGAS | 523 | 3 | 2% | 2% | -46% | -96% | -95% |
| EURUSD | 506 | 3 | 3% | 2% | -45% | -77% | -76% |
| GBPUSD | 477 | 1 | 2% | 1% | -80% | -96% | -96% |
| USDJPY | 435 | 3 | 1% | 1% | -36% | -98% | -98% |
| AUDUSD | 77 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 67 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8793 | 35 | 3% | 2% | -54% | -90% | -90% |
| DOWN (bought NO) | 8687 | 30 | 3% | 2% | -60% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2041 | 10 | 2% | 1% | -18% | -78% | -77% |
| 0.05–0.1% | 2082 | 6 | 3% | 1% | -59% | -92% | -91% |
| 0.1–0.2% | 2987 | 9 | 4% | 2% | -63% | -91% | -91% |
| 0.2–0.5% | 3294 | 18 | 5% | 3% | -40% | -89% | -88% |
| Over 0.5% | 1272 | 5 | 6% | 2% | -59% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4440 | 20 | 4% | 2% | -49% | -87% | -87% |
| Morning (6am–12pm) | 3923 | 20 | 4% | 2% | -41% | -91% | -91% |
| Afternoon (12–6pm) | 4113 | 10 | 3% | 1% | -71% | -91% | -91% |
| Evening (6pm–12am) | 5004 | 15 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,550 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/14 1:29:44 AM | DOGE | DOWN | 16 sec | +0.056% | 0¢ | ❌ Lost | $0.00 |
| 10/14 1:29:44 AM | SILVER | UP | 16 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/14 1:29:44 AM | AUDUSD | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:29:44 AM | ETH | UP | 16 sec | -0.015% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 1:29:28 AM | BNB | UP | 32 sec | -0.065% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 1:29:28 AM | BTC | UP | 32 sec | -0.025% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:29:28 AM | PLATINUM | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:29:13 AM | USDCAD | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:29:13 AM | ZEC | UP | 46 sec | -0.163% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:29:13 AM | SOL | DOWN | 46 sec | +0.067% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 1:28:55 AM | GBPUSD | DOWN | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:28:55 AM | EURUSD | DOWN | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:28:39 AM | GOLD | UP | 81 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 10/14 1:28:39 AM | PALLADIUM | UP | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:28:39 AM | USDJPY | UP | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:28:23 AM | COPPER | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:26:46 AM | XRP | DOWN | 3.2 min | +0.241% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 1:25:41 AM | NEAR | DOWN | 4.3 min | +0.380% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 1:14:48 AM | WTI | DOWN | 12 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/14 1:14:48 AM | PALLADIUM | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:14:32 AM | HYPE | DOWN | 28 sec | +0.022% | 0¢ | ❌ Lost | $0.00 |
| 10/14 1:14:17 AM | ZEC | DOWN | 43 sec | +0.069% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 1:14:17 AM | BNB | UP | 43 sec | -0.085% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:14:17 AM | ETH | DOWN | 43 sec | +0.051% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:14:17 AM | NATGAS | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:13:58 AM | USDCAD | DOWN | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:13:58 AM | USDJPY | DOWN | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:13:42 AM | BTC | DOWN | 78 sec | +0.080% | 2¢ | ❌ Lost | -$0.15 |
| 10/14 1:13:42 AM | COPPER | UP | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:13:26 AM | EURUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
