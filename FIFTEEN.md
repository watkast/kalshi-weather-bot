# 15-Minute 1¢ Study

*Updated Sun Oct 4, 8:51 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 567 finished bets | 1% | $23.10 | +38% | +4.07¢ | -$17.05 / $40.15 |

*Expect about **83 buys a day** (~$12.43/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 2%, hold to the close | 1045 | $14.30 | +11% |
| 5+ min left, hold to the close | 193 | $13.50 | +47% |
| Momentum model ≥ 5%, hold to the close | 571 | $9.40 | +16% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 7903 | 7897 | 36 (0%) | 1.07% | -$441.15 (-47%) | Hold to the close: -$441.15 (-47%) |

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
| Volatility model | 5260 | 4.2% | 0.5% (24) | -615% | ❌ Worse |
| Momentum model | 5260 | 4.3% | 0.5% (24) | -645% | ❌ Worse |
| Mean-reversion model | 5260 | 6.9% | 0.5% (24) | -712% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5260 | 24 | -42% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 1045 | 10 | +11% | -69% | -69% | -64% |
| Volatility model ≥ 5% | 567 | 6 | +38% | -55% | -54% | -49% |
| Volatility model ≥ 10% | 354 | 4 | +67% | -36% | -37% | -31% |
| Momentum model ≥ 2% | 920 | 7 | -8% | -69% | -71% | -68% |
| Momentum model ≥ 5% | 571 | 5 | +16% | -61% | -63% | -60% |
| Momentum model ≥ 10% | 396 | 4 | +45% | -47% | -49% | -45% |
| Mean-reversion model ≥ 2% | 1841 | 13 | -23% | -83% | -83% | -79% |
| Mean-reversion model ≥ 5% | 1238 | 11 | -1% | -79% | -79% | -72% |
| Mean-reversion model ≥ 10% | 817 | 8 | +14% | -77% | -78% | -70% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5457 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1856 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 584 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 7897 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 36 | 0% | -$441.15 | -47% | — |
| Sell at 2¢ | 316 | 4% | -$834.99 | -88% | 33 sec |
| Sell at 3¢ | 204 | 3% | -$837.59 | -89% | 47 sec |
| Sell at 5¢ | 150 | 2% | -$819.65 | -87% | 61 sec |
| Sell at 10¢ | 104 | 1% | -$766.91 | -81% | 72 sec |
| Sell at 25¢ | 57 | 1% | -$686.48 | -73% | 1.6 min |
| Sell at 50¢ | 35 | 0% | -$596.90 | -63% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 190 | 3 | 12% | 3% | +50% | -79% | -87% |
| 2–5 min | 2544 | 19 | 8% | 4% | -27% | -86% | -86% |
| 1–2 min | 2084 | 9 | 3% | 2% | -53% | -93% | -93% |
| Under 1 min | 3076 | 5 | 1% | 0% | -75% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 616 | 5 | 5% | 3% | -4% | -89% | -89% |
| DOGE | 611 | 2 | 4% | 1% | -58% | -91% | -91% |
| ETH | 609 | 5 | 6% | 3% | +4% | -86% | -86% |
| HYPE | 609 | 3 | 5% | 3% | -40% | -88% | -85% |
| BNB | 605 | 2 | 4% | 2% | -60% | -90% | -92% |
| SOL | 604 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 602 | 3 | 6% | 2% | -35% | -86% | -90% |
| XRP | 602 | 4 | 2% | 1% | -15% | -75% | -75% |
| NEAR | 599 | 2 | 6% | 3% | -56% | -63% | -64% |
| GOLD | 314 | 0 | 4% | 1% | -100% | -90% | -93% |
| SILVER | 300 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 287 | 2 | 3% | 1% | -26% | -94% | -96% |
| COPPER | 265 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 236 | 2 | 3% | 2% | -21% | -94% | -92% |
| PLATINUM | 231 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 223 | 1 | 2% | 1% | -58% | -96% | -98% |
| EURUSD | 208 | 1 | 5% | 3% | -55% | -92% | -90% |
| GBPUSD | 201 | 1 | 4% | 2% | -54% | -93% | -94% |
| USDJPY | 175 | 3 | 2% | 2% | +60% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 3970 | 20 | 4% | 2% | -41% | -88% | -87% |
| DOWN (bought NO) | 3927 | 16 | 4% | 2% | -53% | -89% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 918 | 7 | 2% | 1% | +29% | -57% | -56% |
| 0.05–0.1% | 928 | 2 | 3% | 1% | -68% | -91% | -92% |
| 0.1–0.2% | 1347 | 5 | 4% | 2% | -53% | -90% | -91% |
| 0.2–0.5% | 1595 | 8 | 6% | 4% | -44% | -87% | -86% |
| Over 0.5% | 667 | 4 | 7% | 3% | -38% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1882 | 8 | 5% | 2% | -50% | -84% | -86% |
| Morning (6am–12pm) | 2058 | 17 | 5% | 3% | -5% | -89% | -87% |
| Afternoon (12–6pm) | 1751 | 4 | 3% | 1% | -73% | -86% | -87% |
| Evening (6pm–12am) | 2206 | 7 | 3% | 2% | -63% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,152 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/4 8:44:46 PM | SOL | DOWN | 14 sec | -0.022% | 0¢ | ❌ Lost | $0.00 |
| 10/4 8:44:46 PM | COPPER | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 8:44:46 PM | NEAR | DOWN | 14 sec | -0.056% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 8:44:46 PM | USDJPY | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 8:44:30 PM | ETH | DOWN | 30 sec | +0.039% | 0¢ | ❌ Lost | $0.00 |
| 10/4 8:44:30 PM | XRP | DOWN | 30 sec | +0.072% | 0¢ | ❌ Lost | $0.00 |
| 10/4 8:44:14 PM | ZEC | DOWN | 46 sec | +0.202% | 0¢ | ❌ Lost | $0.00 |
| 10/4 8:44:14 PM | EURUSD | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 8:44:14 PM | DOGE | DOWN | 46 sec | +0.101% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 8:43:59 PM | WTI | DOWN | 60 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/4 8:43:59 PM | NATGAS | UP | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 8:43:44 PM | SILVER | UP | 76 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/4 8:43:12 PM | BNB | UP | 1.8 min | -0.128% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 8:42:55 PM | GOLD | UP | 2.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/4 8:41:37 PM | BTC | DOWN | 3.4 min | +0.210% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 8:21:25 PM | EURUSD | UP | 8.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/4 8:14:21 PM | NATGAS | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 8:13:58 PM | BTC | DOWN | 61 sec | +0.110% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 8:13:20 PM | COPPER | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 8:13:06 PM | GBPUSD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 8:12:32 PM | WTI | UP | 2.5 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/4 8:11:42 PM | ZEC | DOWN | 3.3 min | +0.829% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 8:11:42 PM | HYPE | DOWN | 3.3 min | +0.653% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 8:11:42 PM | XRP | DOWN | 3.3 min | +0.388% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 8:11:36 PM | DOGE | DOWN | 3.4 min | +0.441% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 8:11:26 PM | ETH | DOWN | 3.6 min | +0.236% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 8:11:26 PM | SOL | DOWN | 3.6 min | +0.277% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 8:11:04 PM | USDJPY | DOWN | 3.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 8:10:50 PM | EURUSD | UP | 4.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 8:10:15 PM | NEAR | DOWN | 4.8 min | +0.798% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
