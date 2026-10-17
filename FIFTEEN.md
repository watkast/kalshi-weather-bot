# 15-Minute 1¢ Study

*Updated Fri Oct 16, 9:37 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1700 finished bets | 1% | $77.15 | +41% | +4.54¢ | $33.90 / $43.25 |

*Expect about **90 buys a day** (~$13.51/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1564 | $40.50 | +24% |
| Momentum model ≥ 2%, hold to the close | 2646 | -$12.75 | -4% |
| Volatility model ≥ 5%, sell at 50¢ | 1700 | -$25.35 | -13% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 21507 | 21500 | 80 (0%) | 1.07% | -$1,496.75 (-57%) | Hold to the close: -$1,496.75 (-57%) |

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
| Volatility model | 13778 | 4.5% | 0.4% (54) | -656% | ❌ Worse |
| Momentum model | 13778 | 4.4% | 0.4% (54) | -679% | ❌ Worse |
| Mean-reversion model | 13778 | 7.5% | 0.4% (54) | -791% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13778 | 54 | -51% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 3100 | 24 | -11% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 1700 | 19 | +41% | -74% | -73% | -69% |
| Volatility model ≥ 10% | 987 | 11 | +59% | -66% | -65% | -62% |
| Momentum model ≥ 2% | 2646 | 21 | -4% | -80% | -81% | -77% |
| Momentum model ≥ 5% | 1564 | 15 | +24% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1041 | 10 | +35% | -72% | -72% | -67% |
| Mean-reversion model ≥ 2% | 5239 | 34 | -29% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3620 | 27 | -18% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2377 | 16 | -23% | -80% | -80% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13976 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5307 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 21500 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 80 | 0% | -$1,496.75 | -57% | — |
| Sell at 2¢ | 769 | 4% | -$2,318.81 | -89% | 37 sec |
| Sell at 3¢ | 516 | 2% | -$2,317.51 | -89% | 47 sec |
| Sell at 5¢ | 371 | 2% | -$2,277.60 | -87% | 50 sec |
| Sell at 10¢ | 223 | 1% | -$2,198.62 | -84% | 63 sec |
| Sell at 25¢ | 126 | 1% | -$2,031.69 | -78% | 80 sec |
| Sell at 50¢ | 83 | 0% | -$1,818.50 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 735 | 5 | 10% | 3% | -35% | -82% | -85% |
| 2–5 min | 6963 | 37 | 7% | 3% | -48% | -88% | -88% |
| 1–2 min | 5581 | 20 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 8217 | 18 | 1% | 0% | -69% | -88% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1570 | 11 | 5% | 3% | -13% | -89% | -90% |
| HYPE | 1565 | 5 | 4% | 2% | -61% | -90% | -88% |
| ETH | 1557 | 8 | 6% | 3% | -38% | -87% | -87% |
| DOGE | 1555 | 2 | 4% | 2% | -84% | -91% | -90% |
| BNB | 1555 | 6 | 5% | 2% | -53% | -89% | -89% |
| SOL | 1552 | 2 | 3% | 2% | -84% | -92% | -92% |
| XRP | 1544 | 7 | 3% | 1% | -44% | -86% | -87% |
| NEAR | 1540 | 8 | 6% | 3% | -32% | -78% | -78% |
| BTC | 1538 | 7 | 5% | 2% | -39% | -88% | -91% |
| GOLD | 864 | 1 | 3% | 1% | -86% | -92% | -94% |
| SILVER | 841 | 4 | 3% | 1% | -45% | -80% | -80% |
| WTI | 820 | 3 | 3% | 1% | -57% | -94% | -95% |
| COPPER | 735 | 2 | 2% | 1% | -75% | -84% | -84% |
| PLATINUM | 722 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 666 | 5 | 2% | 2% | -30% | -82% | -81% |
| PALLADIUM | 659 | 2 | 1% | 0% | -72% | -84% | -84% |
| EURUSD | 659 | 3 | 3% | 1% | -58% | -81% | -81% |
| GBPUSD | 615 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 574 | 3 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 200 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 169 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10844 | 40 | 4% | 2% | -58% | -89% | -89% |
| DOWN (bought NO) | 10656 | 40 | 4% | 2% | -57% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2314 | 11 | 2% | 1% | -20% | -80% | -79% |
| 0.05–0.1% | 2396 | 7 | 3% | 1% | -57% | -92% | -92% |
| 0.1–0.2% | 3528 | 11 | 4% | 2% | -61% | -90% | -90% |
| 0.2–0.5% | 4107 | 21 | 6% | 3% | -44% | -88% | -88% |
| Over 0.5% | 1628 | 6 | 7% | 3% | -62% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5359 | 20 | 4% | 2% | -58% | -87% | -88% |
| Morning (6am–12pm) | 5104 | 27 | 4% | 2% | -39% | -87% | -86% |
| Afternoon (12–6pm) | 5104 | 16 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 5933 | 17 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,460 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/16 9:29:54 PM | WTI | UP | 5 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 9:27:17 PM | BNB | DOWN | 2.7 min | +0.047% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 9:27:02 PM | DOGE | DOWN | 3.0 min | +0.229% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 9:26:46 PM | NEAR | DOWN | 3.2 min | +0.641% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 9:26:31 PM | HYPE | DOWN | 3.5 min | +0.222% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 9:25:59 PM | BTC | DOWN | 4.0 min | +0.159% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 9:25:43 PM | SOL | DOWN | 4.3 min | +0.261% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 9:25:28 PM | XRP | DOWN | 4.5 min | +0.238% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 9:24:56 PM | ZEC | DOWN | 5.0 min | +0.552% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 9:24:09 PM | ETH | DOWN | 5.8 min | +0.150% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 9:14:47 PM | WTI | DOWN | 13 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/16 9:14:31 PM | ZEC | DOWN | 29 sec | +0.031% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 9:14:31 PM | SOL | UP | 29 sec | -0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/16 9:14:16 PM | NEAR | DOWN | 43 sec | +0.101% | 0¢ | ❌ Lost | $0.00 |
| 10/16 9:14:01 PM | ETH | UP | 58 sec | -0.021% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 9:13:45 PM | BNB | UP | 74 sec | -0.101% | 0¢ | ❌ Lost | $0.00 |
| 10/16 9:13:45 PM | HYPE | DOWN | 74 sec | +0.045% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 9:12:58 PM | DOGE | UP | 2.0 min | -0.126% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 9:12:58 PM | BTC | UP | 2.0 min | -0.080% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 9:12:26 PM | XRP | UP | 2.5 min | -0.146% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:59:57 PM | NATGAS | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 8:59:04 PM | WTI | UP | 56 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 10/16 8:58:30 PM | BTC | DOWN | 1.5 min | +0.046% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:57:59 PM | DOGE | DOWN | 2.0 min | +0.135% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 8:57:43 PM | ZEC | DOWN | 2.3 min | +0.224% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:57:43 PM | NEAR | DOWN | 2.3 min | +0.260% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 8:57:27 PM | ETH | DOWN | 2.5 min | +0.060% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:57:11 PM | BNB | DOWN | 2.8 min | +0.042% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 8:56:07 PM | SOL | DOWN | 3.9 min | +0.213% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:56:07 PM | HYPE | DOWN | 3.9 min | +0.184% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
