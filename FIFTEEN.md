# 15-Minute 1¢ Study

*Updated Fri Oct 16, 7:38 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1684 finished bets | 1% | $79.10 | +42% | +4.70¢ | $34.35 / $44.75 |

*Expect about **90 buys a day** (~$13.44/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1552 | $42.00 | +25% |
| Momentum model ≥ 2%, hold to the close | 2625 | -$10.05 | -3% |
| Volatility model ≥ 5%, sell at 50¢ | 1684 | -$23.40 | -13% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 21430 | 21423 | 80 (0%) | 1.07% | -$1,486.85 (-57%) | Hold to the close: -$1,486.85 (-57%) |

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
| Volatility model | 13706 | 4.4% | 0.4% (54) | -651% | ❌ Worse |
| Momentum model | 13706 | 4.4% | 0.4% (54) | -674% | ❌ Worse |
| Mean-reversion model | 13706 | 7.4% | 0.4% (54) | -784% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13706 | 54 | -51% | -88% | -88% | -85% |
| Volatility model ≥ 2% | 3076 | 24 | -10% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1684 | 19 | +42% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 976 | 11 | +61% | -66% | -65% | -62% |
| Momentum model ≥ 2% | 2625 | 21 | -3% | -80% | -81% | -77% |
| Momentum model ≥ 5% | 1552 | 15 | +25% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1034 | 10 | +36% | -72% | -72% | -67% |
| Mean-reversion model ≥ 2% | 5196 | 34 | -29% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3592 | 27 | -17% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2358 | 16 | -22% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13904 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5302 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 21423 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 80 | 0% | -$1,486.85 | -57% | — |
| Sell at 2¢ | 767 | 4% | -$2,309.43 | -89% | 37 sec |
| Sell at 3¢ | 516 | 2% | -$2,307.61 | -89% | 47 sec |
| Sell at 5¢ | 371 | 2% | -$2,267.70 | -87% | 50 sec |
| Sell at 10¢ | 223 | 1% | -$2,188.72 | -84% | 63 sec |
| Sell at 25¢ | 126 | 1% | -$2,021.79 | -78% | 80 sec |
| Sell at 50¢ | 83 | 0% | -$1,808.60 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 730 | 5 | 10% | 3% | -35% | -82% | -85% |
| 2–5 min | 6926 | 37 | 7% | 3% | -47% | -88% | -87% |
| 1–2 min | 5572 | 20 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 8191 | 18 | 1% | 0% | -68% | -88% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1562 | 11 | 5% | 3% | -12% | -89% | -90% |
| HYPE | 1557 | 5 | 4% | 2% | -61% | -90% | -88% |
| ETH | 1549 | 8 | 6% | 3% | -37% | -87% | -86% |
| DOGE | 1547 | 2 | 4% | 2% | -84% | -90% | -90% |
| BNB | 1547 | 6 | 5% | 2% | -52% | -89% | -89% |
| SOL | 1544 | 2 | 3% | 2% | -84% | -92% | -92% |
| XRP | 1536 | 7 | 3% | 1% | -44% | -86% | -87% |
| NEAR | 1532 | 8 | 6% | 3% | -32% | -77% | -78% |
| BTC | 1530 | 7 | 5% | 2% | -39% | -88% | -91% |
| GOLD | 864 | 1 | 3% | 1% | -86% | -92% | -94% |
| SILVER | 841 | 4 | 3% | 1% | -45% | -80% | -80% |
| WTI | 816 | 3 | 3% | 1% | -57% | -94% | -95% |
| COPPER | 735 | 2 | 2% | 1% | -75% | -84% | -84% |
| PLATINUM | 722 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 665 | 5 | 2% | 2% | -30% | -82% | -81% |
| PALLADIUM | 659 | 2 | 1% | 0% | -72% | -84% | -84% |
| EURUSD | 659 | 3 | 3% | 1% | -58% | -81% | -81% |
| GBPUSD | 615 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 574 | 3 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 200 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 169 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10813 | 40 | 4% | 2% | -58% | -89% | -88% |
| DOWN (bought NO) | 10610 | 40 | 4% | 2% | -56% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2298 | 11 | 2% | 1% | -19% | -80% | -79% |
| 0.05–0.1% | 2384 | 7 | 3% | 1% | -57% | -92% | -91% |
| 0.1–0.2% | 3508 | 11 | 4% | 2% | -61% | -90% | -90% |
| 0.2–0.5% | 4089 | 21 | 6% | 3% | -43% | -88% | -88% |
| Over 0.5% | 1622 | 6 | 7% | 3% | -62% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5359 | 20 | 4% | 2% | -58% | -87% | -88% |
| Morning (6am–12pm) | 5104 | 27 | 4% | 2% | -39% | -87% | -86% |
| Afternoon (12–6pm) | 5104 | 16 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 5856 | 17 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,449 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/16 7:29:52 PM | XRP | UP | 8 sec | -0.061% | 0¢ | ❌ Lost | $0.00 |
| 10/16 7:29:36 PM | ZEC | UP | 24 sec | -0.023% | 0¢ | ❌ Lost | $0.00 |
| 10/16 7:29:36 PM | BTC | UP | 24 sec | -0.021% | 0¢ | ❌ Lost | $0.00 |
| 10/16 7:29:36 PM | HYPE | UP | 24 sec | -0.065% | 0¢ | ❌ Lost | $0.00 |
| 10/16 7:29:20 PM | NEAR | DOWN | 40 sec | -0.042% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 7:29:05 PM | DOGE | DOWN | 54 sec | +0.107% | 0¢ | ❌ Lost | $0.00 |
| 10/16 7:29:05 PM | BNB | DOWN | 54 sec | -0.015% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 7:28:47 PM | ETH | UP | 72 sec | -0.037% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 7:28:15 PM | SOL | DOWN | 1.8 min | +0.114% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 7:14:35 PM | WTI | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 7:14:19 PM | ZEC | DOWN | 40 sec | +0.183% | 0¢ | ❌ Lost | $0.00 |
| 10/16 7:14:19 PM | NEAR | DOWN | 40 sec | +0.135% | 0¢ | ❌ Lost | $0.00 |
| 10/16 7:14:03 PM | XRP | UP | 57 sec | -0.092% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 7:14:03 PM | SOL | DOWN | 57 sec | +0.099% | 0¢ | ❌ Lost | $0.00 |
| 10/16 7:13:29 PM | HYPE | UP | 1.5 min | -0.189% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 7:12:09 PM | DOGE | UP | 2.9 min | -0.323% | 3¢ | ❌ Lost | -$0.15 |
| 10/16 6:59:22 PM | XRP | DOWN | 37 sec | +0.008% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:59:06 PM | ZEC | UP | 53 sec | -0.126% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:59:06 PM | SOL | DOWN | 53 sec | +0.068% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:59:06 PM | ETH | DOWN | 53 sec | +0.070% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 6:57:43 PM | BNB | UP | 2.3 min | -0.096% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:57:11 PM | NEAR | DOWN | 2.8 min | +0.511% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 6:56:38 PM | HYPE | UP | 3.4 min | -0.189% | 3¢ | ❌ Lost | -$0.15 |
| 10/16 6:56:06 PM | DOGE | UP | 3.9 min | -0.663% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:44:52 PM | DOGE | UP | 8 sec | -0.027% | 0¢ | ❌ Lost | $0.00 |
| 10/16 6:44:52 PM | HYPE | UP | 8 sec | -0.079% | 0¢ | ❌ Lost | $0.00 |
| 10/16 6:44:36 PM | BTC | UP | 24 sec | -0.010% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:44:20 PM | SOL | UP | 40 sec | -0.088% | 0¢ | ❌ Lost | $0.00 |
| 10/16 6:44:03 PM | XRP | UP | 56 sec | -0.100% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:43:47 PM | NEAR | UP | 72 sec | -0.654% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
