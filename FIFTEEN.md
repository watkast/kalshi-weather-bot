# 15-Minute 1¢ Study

*Updated Wed Oct 14, 3:45 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1351 finished bets | 1% | $33.95 | +23% | +2.51¢ | $39.85 / -$5.90 |

*Expect about **84 buys a day** (~$12.57/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1278 | $16.60 | +12% |
| 5+ min left, hold to the close | 539 | -$23.35 | -29% |
| Volatility model ≥ 5%, sell at 50¢ | 1351 | -$25.05 | -17% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 17638 | 17621 | 65 (0%) | 1.07% | -$1,223.60 (-57%) | Hold to the close: -$1,223.60 (-57%) |

*In play or awaiting result: 16. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 11558 | 4.5% | 0.4% (46) | -680% | ❌ Worse |
| Momentum model | 11558 | 4.4% | 0.4% (46) | -706% | ❌ Worse |
| Mean-reversion model | 11558 | 7.3% | 0.4% (46) | -802% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 11558 | 46 | -50% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2402 | 18 | -13% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1351 | 13 | +23% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 826 | 9 | +56% | -64% | -62% | -59% |
| Momentum model ≥ 2% | 2106 | 15 | -14% | -79% | -79% | -77% |
| Momentum model ≥ 5% | 1278 | 11 | +12% | -77% | -76% | -74% |
| Momentum model ≥ 10% | 871 | 8 | +30% | -70% | -69% | -65% |
| Mean-reversion model ≥ 2% | 4182 | 27 | -29% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2851 | 20 | -22% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 1877 | 14 | -14% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 11756 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4281 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1584 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 17621 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 65 | 0% | -$1,223.60 | -57% | — |
| Sell at 2¢ | 604 | 3% | -$1,934.56 | -91% | 33 sec |
| Sell at 3¢ | 404 | 2% | -$1,934.04 | -91% | 46 sec |
| Sell at 5¢ | 293 | 2% | -$1,901.15 | -89% | 48 sec |
| Sell at 10¢ | 186 | 1% | -$1,819.94 | -85% | 63 sec |
| Sell at 25¢ | 103 | 1% | -$1,694.67 | -79% | 67 sec |
| Sell at 50¢ | 66 | 0% | -$1,520.10 | -71% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 535 | 4 | 10% | 2% | -29% | -83% | -88% |
| 2–5 min | 5673 | 32 | 6% | 3% | -44% | -88% | -88% |
| 1–2 min | 4622 | 17 | 3% | 2% | -60% | -94% | -93% |
| Under 1 min | 6787 | 12 | 1% | 0% | -74% | -92% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1317 | 7 | 4% | 2% | -34% | -90% | -90% |
| HYPE | 1313 | 4 | 4% | 2% | -62% | -90% | -89% |
| ETH | 1311 | 8 | 5% | 3% | -26% | -89% | -88% |
| BNB | 1311 | 5 | 4% | 2% | -54% | -90% | -90% |
| DOGE | 1308 | 2 | 4% | 2% | -81% | -91% | -90% |
| SOL | 1306 | 2 | 3% | 1% | -81% | -93% | -92% |
| BTC | 1299 | 6 | 5% | 2% | -39% | -88% | -91% |
| XRP | 1296 | 7 | 2% | 1% | -33% | -85% | -86% |
| NEAR | 1295 | 7 | 5% | 2% | -30% | -77% | -78% |
| GOLD | 698 | 1 | 4% | 1% | -83% | -92% | -93% |
| SILVER | 685 | 2 | 3% | 1% | -66% | -94% | -93% |
| WTI | 654 | 3 | 3% | 1% | -47% | -94% | -96% |
| COPPER | 606 | 0 | 1% | 1% | -100% | -97% | -97% |
| PLATINUM | 576 | 0 | 1% | 0% | -100% | -99% | -99% |
| PALLADIUM | 534 | 1 | 1% | 0% | -83% | -98% | -98% |
| NATGAS | 528 | 3 | 2% | 2% | -47% | -96% | -95% |
| EURUSD | 513 | 3 | 3% | 2% | -45% | -77% | -77% |
| GBPUSD | 482 | 1 | 2% | 1% | -81% | -96% | -96% |
| USDJPY | 439 | 3 | 1% | 1% | -36% | -98% | -98% |
| AUDUSD | 81 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 69 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8875 | 35 | 3% | 2% | -54% | -90% | -90% |
| DOWN (bought NO) | 8746 | 30 | 3% | 2% | -60% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2049 | 10 | 2% | 1% | -18% | -78% | -77% |
| 0.05–0.1% | 2092 | 6 | 3% | 1% | -59% | -92% | -91% |
| 0.1–0.2% | 3006 | 9 | 4% | 2% | -63% | -91% | -91% |
| 0.2–0.5% | 3321 | 18 | 5% | 3% | -40% | -89% | -88% |
| Over 0.5% | 1285 | 5 | 6% | 2% | -60% | -89% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4581 | 20 | 4% | 2% | -50% | -87% | -87% |
| Morning (6am–12pm) | 3923 | 20 | 4% | 2% | -41% | -91% | -91% |
| Afternoon (12–6pm) | 4113 | 10 | 3% | 1% | -71% | -91% | -91% |
| Evening (6pm–12am) | 5004 | 15 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,536 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/14 3:44:45 AM | PALLADIUM | DOWN | 14 sec | — | 0¢ | In play | — |
| 10/14 3:44:45 AM | SOL | DOWN | 14 sec | +0.070% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 3:44:29 AM | NEAR | DOWN | 30 sec | +0.098% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 3:44:29 AM | USDJPY | UP | 30 sec | — | 0¢ | In play | — |
| 10/14 3:44:29 AM | AUDUSD | DOWN | 30 sec | — | 0¢ | In play | — |
| 10/14 3:44:29 AM | SILVER | DOWN | 30 sec | — | 1¢ | In play | — |
| 10/14 3:44:29 AM | PLATINUM | DOWN | 30 sec | — | 0¢ | In play | — |
| 10/14 3:44:13 AM | BTC | UP | 47 sec | -0.056% | 0¢ | ❌ Lost | $0.00 |
| 10/14 3:44:13 AM | BNB | UP | 47 sec | -0.086% | 0¢ | ❌ Lost | $0.00 |
| 10/14 3:44:13 AM | HYPE | UP | 47 sec | -0.079% | 0¢ | In play | — |
| 10/14 3:43:38 AM | WTI | DOWN | 82 sec | — | 1¢ | In play | — |
| 10/14 3:43:38 AM | EURUSD | DOWN | 82 sec | — | 4¢ | In play | — |
| 10/14 3:43:22 AM | ETH | UP | 1.6 min | -0.109% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 3:43:22 AM | ZEC | UP | 1.6 min | -0.264% | 1¢ | In play | — |
| 10/14 3:43:07 AM | DOGE | UP | 1.9 min | -0.158% | 1¢ | In play | — |
| 10/14 3:42:51 AM | XRP | UP | 2.1 min | -0.154% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 3:29:59 AM | EURUSD | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 3:29:59 AM | COPPER | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 3:29:43 AM | GOLD | UP | 17 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 3:29:43 AM | PALLADIUM | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 3:29:27 AM | USDCAD | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 3:29:12 AM | GBPUSD | DOWN | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 3:29:12 AM | BNB | UP | 47 sec | -0.102% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 3:28:56 AM | NATGAS | UP | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 3:28:40 AM | SILVER | UP | 80 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 3:27:51 AM | PLATINUM | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 3:27:35 AM | XRP | UP | 2.4 min | -0.234% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 3:27:19 AM | HYPE | UP | 2.7 min | -0.366% | 0¢ | ❌ Lost | $0.00 |
| 10/14 3:27:19 AM | DOGE | UP | 2.7 min | -0.258% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 3:27:19 AM | ZEC | UP | 2.7 min | -0.530% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
