# 15-Minute 1¢ Study

*Updated Wed Sep 30, 9:27 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 120 finished bets | 2% | $10.30 | +58% | +8.58¢ | $19.00 / -$8.70 |

*Expect about **40 buys a day** (~$5.93/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 216 | $4.45 | +19% |
| Volatility model ≥ 5%, sell at 25¢ | 214 | $0.38 | +2% |
| Volatility model ≥ 5%, sell at 10¢ | 214 | -$0.38 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 3841 | 3834 | 14 (0%) | 1.07% | -$272.00 (-58%) | Hold to the close: -$272.00 (-58%) |

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
| Volatility model | 2201 | 3.3% | 0.3% (6) | -565% | ❌ Worse |
| Momentum model | 2201 | 3.4% | 0.3% (6) | -608% | ❌ Worse |
| Mean-reversion model | 2201 | 6.4% | 0.3% (6) | -722% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2201 | 6 | -66% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 433 | 3 | -21% | -58% | -59% | -54% |
| Volatility model ≥ 5% | 214 | 1 | -41% | -20% | -19% | -13% |
| Volatility model ≥ 10% | 121 | 1 | +21% | +39% | +41% | +49% |
| Momentum model ≥ 2% | 382 | 2 | -38% | -53% | -55% | -51% |
| Momentum model ≥ 5% | 216 | 2 | +19% | -24% | -27% | -21% |
| Momentum model ≥ 10% | 143 | 1 | +1% | +13% | +16% | +20% |
| Mean-reversion model ≥ 2% | 830 | 3 | -62% | -86% | -87% | -83% |
| Mean-reversion model ≥ 5% | 545 | 3 | -41% | -83% | -84% | -77% |
| Mean-reversion model ≥ 10% | 345 | 2 | -36% | -78% | -80% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2397 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 1130 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 307 | 3% | 2% | 2% | 1% | 1% | 1% |
| **All** | 3834 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 14 | 0% | -$272.00 | -58% | — |
| Sell at 2¢ | 144 | 4% | -$416.56 | -89% | 46 sec |
| Sell at 3¢ | 89 | 2% | -$419.29 | -90% | 49 sec |
| Sell at 5¢ | 66 | 2% | -$411.10 | -88% | 66 sec |
| Sell at 10¢ | 48 | 1% | -$377.12 | -81% | 80 sec |
| Sell at 25¢ | 24 | 1% | -$360.56 | -77% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$331.00 | -71% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 120 | 2 | 12% | 3% | +58% | -79% | -87% |
| 2–5 min | 1256 | 6 | 7% | 3% | -54% | -88% | -89% |
| 1–2 min | 983 | 4 | 3% | 2% | -56% | -93% | -92% |
| Under 1 min | 1475 | 2 | 1% | 0% | -80% | -88% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 272 | 1 | 4% | 1% | -53% | -91% | -91% |
| NEAR | 267 | 0 | 5% | 1% | -100% | -88% | -91% |
| ETH | 267 | 2 | 5% | 3% | -8% | -89% | -86% |
| XRP | 266 | 3 | 2% | 2% | +46% | -47% | -46% |
| ZEC | 266 | 1 | 6% | 2% | -55% | -87% | -92% |
| BNB | 266 | 0 | 4% | 1% | -100% | -92% | -94% |
| HYPE | 265 | 1 | 5% | 3% | -54% | -90% | -87% |
| BTC | 264 | 0 | 7% | 3% | -100% | -84% | -87% |
| SOL | 264 | 0 | 3% | 1% | -100% | -92% | -93% |
| GOLD | 196 | 0 | 5% | 2% | -100% | -89% | -92% |
| SILVER | 181 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 174 | 1 | 3% | 1% | -39% | -93% | -95% |
| COPPER | 159 | 0 | 1% | 1% | -100% | -98% | -98% |
| NATGAS | 151 | 1 | 4% | 3% | -38% | -93% | -90% |
| PLATINUM | 137 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 132 | 0 | 2% | 1% | -100% | -96% | -98% |
| GBPUSD | 110 | 1 | 5% | 2% | -15% | -92% | -93% |
| EURUSD | 105 | 1 | 3% | 1% | -11% | -95% | -98% |
| USDJPY | 92 | 2 | 2% | 2% | +103% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1983 | 8 | 4% | 2% | -54% | -92% | -92% |
| DOWN (bought NO) | 1851 | 6 | 4% | 2% | -63% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 269 | 1 | 1% | 1% | -28% | -23% | -22% |
| 0.05–0.1% | 325 | 0 | 1% | 0% | -100% | -96% | -97% |
| 0.1–0.2% | 574 | 1 | 4% | 2% | -77% | -90% | -91% |
| 0.2–0.5% | 823 | 2 | 6% | 3% | -73% | -89% | -89% |
| Over 0.5% | 405 | 4 | 6% | 3% | +2% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 888 | 2 | 4% | 2% | -74% | -91% | -93% |
| Morning (6am–12pm) | 960 | 6 | 4% | 2% | -29% | -91% | -90% |
| Afternoon (12–6pm) | 841 | 2 | 3% | 1% | -73% | -80% | -84% |
| Evening (6pm–12am) | 1145 | 4 | 4% | 2% | -59% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,376 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 9:25:59 PM | HYPE | UP | 4.0 min | -0.499% | — | In play | — |
| 9/30 9:14:44 PM | ZEC | DOWN | 15 sec | +0.039% | 0¢ | ❌ Lost | $0.00 |
| 9/30 9:14:44 PM | ETH | DOWN | 15 sec | +0.009% | 0¢ | ❌ Lost | $0.00 |
| 9/30 9:14:28 PM | XRP | UP | 31 sec | -0.047% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:14:12 PM | BTC | UP | 47 sec | -0.023% | 0¢ | ❌ Lost | $0.00 |
| 9/30 9:13:58 PM | NEAR | DOWN | 62 sec | +0.355% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:13:58 PM | SOL | UP | 62 sec | -0.104% | 0¢ | ❌ Lost | $0.00 |
| 9/30 9:13:42 PM | HYPE | UP | 77 sec | -0.195% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:13:42 PM | DOGE | UP | 77 sec | -0.173% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:12:38 PM | BNB | UP | 2.4 min | -0.130% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:12:06 PM | PLATINUM | DOWN | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 9:12:06 PM | GOLD | DOWN | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:11:50 PM | SILVER | DOWN | 3.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 9:11:18 PM | PALLADIUM | DOWN | 3.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 8:59:31 PM | NATGAS | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 8:59:15 PM | ETH | DOWN | 44 sec | +0.057% | 0¢ | ❌ Lost | $0.00 |
| 9/30 8:59:15 PM | SILVER | DOWN | 44 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/30 8:59:15 PM | GOLD | DOWN | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 8:58:43 PM | HYPE | DOWN | 76 sec | +0.312% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 8:57:55 PM | BTC | DOWN | 2.1 min | +0.099% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 8:57:55 PM | XRP | DOWN | 2.1 min | +0.188% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 8:57:37 PM | WTI | UP | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 8:57:21 PM | ZEC | DOWN | 2.6 min | +0.309% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 8:56:50 PM | BNB | DOWN | 3.1 min | +0.092% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 8:56:50 PM | DOGE | DOWN | 3.1 min | +0.353% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 8:56:50 PM | SOL | DOWN | 3.1 min | +0.156% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 8:54:10 PM | NEAR | DOWN | 5.8 min | +1.191% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 8:44:53 PM | HYPE | DOWN | 7 sec | -0.025% | 0¢ | ❌ Lost | $0.00 |
| 9/30 8:44:53 PM | SOL | UP | 7 sec | -0.022% | 0¢ | ❌ Lost | $0.00 |
| 9/30 8:44:53 PM | NEAR | DOWN | 7 sec | +0.173% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
