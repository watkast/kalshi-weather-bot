# 15-Minute 1¢ Study

*Updated Sun Oct 4, 9:31 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 568 finished bets | 1% | $22.95 | +38% | +4.04¢ | -$17.20 / $40.15 |

*Expect about **83 buys a day** (~$12.41/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 2%, hold to the close | 1046 | $14.15 | +11% |
| 5+ min left, hold to the close | 195 | $13.20 | +46% |
| Momentum model ≥ 5%, hold to the close | 572 | $9.25 | +15% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 7952 | 7946 | 36 (0%) | 1.07% | -$448.05 (-47%) | Hold to the close: -$448.05 (-47%) |

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
| Volatility model | 5287 | 4.2% | 0.5% (24) | -614% | ❌ Worse |
| Momentum model | 5287 | 4.3% | 0.5% (24) | -644% | ❌ Worse |
| Mean-reversion model | 5287 | 6.9% | 0.5% (24) | -710% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5287 | 24 | -43% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 1046 | 10 | +11% | -69% | -69% | -64% |
| Volatility model ≥ 5% | 568 | 6 | +38% | -55% | -54% | -49% |
| Volatility model ≥ 10% | 354 | 4 | +67% | -36% | -37% | -31% |
| Momentum model ≥ 2% | 922 | 7 | -8% | -69% | -71% | -69% |
| Momentum model ≥ 5% | 572 | 5 | +15% | -61% | -63% | -60% |
| Momentum model ≥ 10% | 396 | 4 | +45% | -47% | -49% | -45% |
| Mean-reversion model ≥ 2% | 1845 | 13 | -23% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1240 | 11 | -1% | -79% | -79% | -72% |
| Mean-reversion model ≥ 10% | 819 | 8 | +13% | -77% | -78% | -70% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5484 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1871 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 591 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 7946 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 36 | 0% | -$448.05 | -47% | — |
| Sell at 2¢ | 318 | 4% | -$841.37 | -88% | 33 sec |
| Sell at 3¢ | 206 | 3% | -$843.71 | -89% | 47 sec |
| Sell at 5¢ | 152 | 2% | -$825.25 | -87% | 61 sec |
| Sell at 10¢ | 104 | 1% | -$773.81 | -81% | 72 sec |
| Sell at 25¢ | 57 | 1% | -$693.38 | -73% | 1.6 min |
| Sell at 50¢ | 35 | 0% | -$603.80 | -63% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 192 | 3 | 12% | 3% | +48% | -79% | -88% |
| 2–5 min | 2563 | 19 | 8% | 4% | -28% | -86% | -86% |
| 1–2 min | 2099 | 9 | 3% | 2% | -53% | -93% | -93% |
| Under 1 min | 3089 | 5 | 1% | 0% | -76% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 619 | 5 | 5% | 3% | -4% | -89% | -89% |
| DOGE | 614 | 2 | 4% | 1% | -58% | -91% | -91% |
| ETH | 612 | 5 | 6% | 3% | +3% | -86% | -86% |
| HYPE | 612 | 3 | 5% | 3% | -40% | -88% | -86% |
| BNB | 608 | 2 | 4% | 2% | -61% | -90% | -92% |
| SOL | 607 | 0 | 3% | 1% | -100% | -92% | -91% |
| BTC | 605 | 3 | 6% | 2% | -35% | -86% | -89% |
| XRP | 605 | 4 | 2% | 1% | -15% | -75% | -75% |
| NEAR | 602 | 2 | 6% | 3% | -56% | -63% | -64% |
| GOLD | 317 | 0 | 4% | 1% | -100% | -90% | -93% |
| SILVER | 302 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 290 | 2 | 3% | 1% | -27% | -95% | -96% |
| COPPER | 268 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 237 | 2 | 3% | 2% | -21% | -94% | -92% |
| PLATINUM | 233 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 224 | 1 | 2% | 1% | -58% | -96% | -98% |
| EURUSD | 211 | 1 | 5% | 3% | -56% | -92% | -90% |
| GBPUSD | 203 | 1 | 4% | 2% | -54% | -93% | -94% |
| USDJPY | 177 | 3 | 2% | 2% | +58% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4005 | 20 | 4% | 2% | -41% | -88% | -87% |
| DOWN (bought NO) | 3941 | 16 | 4% | 2% | -53% | -89% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 921 | 7 | 2% | 1% | +29% | -57% | -57% |
| 0.05–0.1% | 934 | 2 | 4% | 1% | -68% | -90% | -92% |
| 0.1–0.2% | 1354 | 5 | 4% | 2% | -53% | -90% | -91% |
| 0.2–0.5% | 1603 | 8 | 6% | 3% | -45% | -87% | -87% |
| Over 0.5% | 670 | 4 | 7% | 3% | -39% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1882 | 8 | 5% | 2% | -50% | -84% | -86% |
| Morning (6am–12pm) | 2058 | 17 | 5% | 3% | -5% | -89% | -87% |
| Afternoon (12–6pm) | 1751 | 4 | 3% | 1% | -73% | -86% | -87% |
| Evening (6pm–12am) | 2255 | 7 | 3% | 2% | -64% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,167 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/4 9:29:48 PM | DOGE | DOWN | 11 sec | +0.020% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:29:32 PM | ETH | UP | 27 sec | -0.046% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:29:32 PM | USDJPY | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:29:16 PM | WTI | UP | 43 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:29:16 PM | SOL | UP | 43 sec | -0.098% | 0¢ | ❌ Lost | $0.00 |
| 10/4 9:29:16 PM | BTC | UP | 43 sec | -0.057% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:29:00 PM | EURUSD | DOWN | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:29:00 PM | PLATINUM | DOWN | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:28:44 PM | XRP | UP | 75 sec | -0.158% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:28:28 PM | ZEC | UP | 1.5 min | -0.312% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:28:28 PM | GBPUSD | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:28:28 PM | COPPER | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:27:56 PM | GOLD | DOWN | 2.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:27:40 PM | SILVER | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:26:36 PM | HYPE | UP | 3.4 min | -0.435% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:25:16 PM | BNB | UP | 4.7 min | -0.607% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:23:24 PM | NEAR | UP | 6.6 min | -1.392% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:14:45 PM | BNB | UP | 15 sec | -0.067% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:14:45 PM | ZEC | UP | 15 sec | -0.084% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:14:45 PM | DOGE | DOWN | 15 sec | +0.045% | 0¢ | ❌ Lost | $0.00 |
| 10/4 9:14:45 PM | XRP | DOWN | 15 sec | +0.053% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:14:13 PM | EURUSD | DOWN | 47 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:14:13 PM | COPPER | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:13:58 PM | BTC | UP | 61 sec | -0.064% | 8¢ | ❌ Lost | -$0.15 |
| 10/4 9:13:42 PM | WTI | DOWN | 77 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:13:42 PM | SOL | UP | 77 sec | -0.173% | 6¢ | ❌ Lost | $0.00 |
| 10/4 9:13:42 PM | NATGAS | UP | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:13:42 PM | GOLD | UP | 77 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:13:42 PM | NEAR | DOWN | 77 sec | +0.231% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:13:26 PM | ETH | UP | 1.6 min | -0.108% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
