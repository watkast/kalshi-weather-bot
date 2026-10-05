# 15-Minute 1¢ Study

*Updated Sun Oct 4, 9:51 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 568 finished bets | 1% | $22.95 | +38% | +4.04¢ | -$17.20 / $40.15 |

*Expect about **83 buys a day** (~$12.38/day at risk); max loss per buy **15¢**.*

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
| 7967 | 7961 | 36 (0%) | 1.07% | -$450.15 (-47%) | Hold to the close: -$450.15 (-47%) |

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
| Volatility model | 5294 | 4.2% | 0.5% (24) | -613% | ❌ Worse |
| Momentum model | 5294 | 4.3% | 0.5% (24) | -644% | ❌ Worse |
| Mean-reversion model | 5294 | 6.9% | 0.5% (24) | -710% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5294 | 24 | -43% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 1046 | 10 | +11% | -69% | -69% | -64% |
| Volatility model ≥ 5% | 568 | 6 | +38% | -55% | -54% | -49% |
| Volatility model ≥ 10% | 354 | 4 | +67% | -36% | -37% | -31% |
| Momentum model ≥ 2% | 922 | 7 | -8% | -69% | -71% | -69% |
| Momentum model ≥ 5% | 572 | 5 | +15% | -61% | -63% | -60% |
| Momentum model ≥ 10% | 396 | 4 | +45% | -47% | -49% | -45% |
| Mean-reversion model ≥ 2% | 1847 | 13 | -23% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1241 | 11 | -1% | -79% | -79% | -72% |
| Mean-reversion model ≥ 10% | 820 | 8 | +13% | -77% | -78% | -70% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5491 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1876 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 594 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 7961 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 36 | 0% | -$450.15 | -47% | — |
| Sell at 2¢ | 318 | 4% | -$843.47 | -88% | 33 sec |
| Sell at 3¢ | 206 | 3% | -$845.81 | -89% | 47 sec |
| Sell at 5¢ | 152 | 2% | -$827.35 | -87% | 61 sec |
| Sell at 10¢ | 104 | 1% | -$775.91 | -81% | 72 sec |
| Sell at 25¢ | 57 | 1% | -$695.48 | -73% | 1.6 min |
| Sell at 50¢ | 35 | 0% | -$605.90 | -64% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 192 | 3 | 12% | 3% | +48% | -79% | -88% |
| 2–5 min | 2568 | 19 | 8% | 4% | -28% | -86% | -86% |
| 1–2 min | 2105 | 9 | 3% | 2% | -53% | -93% | -93% |
| Under 1 min | 3093 | 5 | 1% | 0% | -76% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 620 | 5 | 5% | 3% | -4% | -89% | -89% |
| DOGE | 614 | 2 | 4% | 1% | -58% | -91% | -91% |
| ETH | 613 | 5 | 6% | 3% | +3% | -86% | -86% |
| HYPE | 613 | 3 | 5% | 3% | -40% | -88% | -86% |
| BNB | 609 | 2 | 4% | 2% | -61% | -91% | -92% |
| SOL | 608 | 0 | 3% | 1% | -100% | -92% | -91% |
| BTC | 606 | 3 | 6% | 2% | -35% | -86% | -89% |
| XRP | 606 | 4 | 2% | 1% | -15% | -75% | -75% |
| NEAR | 602 | 2 | 6% | 3% | -56% | -63% | -64% |
| GOLD | 317 | 0 | 4% | 1% | -100% | -90% | -93% |
| SILVER | 303 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 290 | 2 | 3% | 1% | -27% | -95% | -96% |
| COPPER | 269 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 238 | 2 | 3% | 2% | -22% | -94% | -92% |
| PLATINUM | 234 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 225 | 1 | 2% | 1% | -59% | -96% | -98% |
| EURUSD | 212 | 1 | 5% | 3% | -56% | -92% | -90% |
| GBPUSD | 204 | 1 | 4% | 2% | -54% | -93% | -94% |
| USDJPY | 178 | 3 | 2% | 2% | +57% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4015 | 20 | 4% | 2% | -41% | -88% | -87% |
| DOWN (bought NO) | 3946 | 16 | 4% | 2% | -53% | -89% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 921 | 7 | 2% | 1% | +29% | -57% | -57% |
| 0.05–0.1% | 935 | 2 | 4% | 1% | -69% | -90% | -92% |
| 0.1–0.2% | 1357 | 5 | 4% | 2% | -53% | -90% | -91% |
| 0.2–0.5% | 1606 | 8 | 6% | 3% | -45% | -87% | -87% |
| Over 0.5% | 670 | 4 | 7% | 3% | -39% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1882 | 8 | 5% | 2% | -50% | -84% | -86% |
| Morning (6am–12pm) | 2058 | 17 | 5% | 3% | -5% | -89% | -87% |
| Afternoon (12–6pm) | 1751 | 4 | 3% | 1% | -73% | -86% | -87% |
| Evening (6pm–12am) | 2270 | 7 | 3% | 2% | -64% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,160 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/4 9:44:49 PM | HYPE | UP | 10 sec | -0.069% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:44:49 PM | SILVER | DOWN | 10 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/4 9:44:33 PM | PALLADIUM | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:44:33 PM | PLATINUM | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:43:43 PM | XRP | UP | 77 sec | -0.185% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:43:43 PM | COPPER | DOWN | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:43:27 PM | USDJPY | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:43:27 PM | GBPUSD | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:43:11 PM | ZEC | UP | 1.8 min | -0.334% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:43:11 PM | NATGAS | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:42:56 PM | SOL | UP | 2.0 min | -0.206% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:42:38 PM | BNB | UP | 2.4 min | -0.253% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:41:51 PM | BTC | UP | 3.1 min | -0.189% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:41:51 PM | ETH | UP | 3.1 min | -0.159% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:41:35 PM | EURUSD | UP | 3.4 min | — | 0¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
