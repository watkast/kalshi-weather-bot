# 15-Minute 1¢ Study

*Updated Wed Oct 14, 9:53 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1463 finished bets | 1% | $89.55 | +55% | +6.12¢ | $33.40 / $56.15 |

*Expect about **87 buys a day** (~$13.00/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1371 | $61.20 | +41% |
| Momentum model ≥ 2%, hold to the close | 2277 | $15.70 | +6% |
| Volatility model ≥ 2%, hold to the close | 2622 | $4.60 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 18792 | 18785 | 74 (0%) | 1.07% | -$1,241.90 (-55%) | Hold to the close: -$1,241.90 (-55%) |

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
| Volatility model | 12188 | 4.5% | 0.4% (52) | -636% | ❌ Worse |
| Momentum model | 12188 | 4.4% | 0.4% (52) | -661% | ❌ Worse |
| Mean-reversion model | 12188 | 7.3% | 0.4% (52) | -755% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12188 | 52 | -46% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2622 | 23 | +1% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 1463 | 18 | +55% | -73% | -71% | -67% |
| Volatility model ≥ 10% | 876 | 11 | +78% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 2277 | 20 | +6% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1371 | 15 | +41% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 924 | 10 | +52% | -70% | -70% | -65% |
| Mean-reversion model ≥ 2% | 4494 | 32 | -22% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 3076 | 25 | -10% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2021 | 14 | -21% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12386 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4606 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1793 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 18785 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 74 | 0% | -$1,241.90 | -55% | — |
| Sell at 2¢ | 659 | 4% | -$2,050.56 | -90% | 34 sec |
| Sell at 3¢ | 443 | 2% | -$2,049.13 | -90% | 46 sec |
| Sell at 5¢ | 323 | 2% | -$2,011.95 | -88% | 49 sec |
| Sell at 10¢ | 203 | 1% | -$1,927.97 | -85% | 63 sec |
| Sell at 25¢ | 118 | 1% | -$1,761.32 | -77% | 80 sec |
| Sell at 50¢ | 78 | 0% | -$1,555.40 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 586 | 5 | 10% | 3% | -19% | -82% | -87% |
| 2–5 min | 6064 | 35 | 7% | 3% | -43% | -88% | -88% |
| 1–2 min | 4905 | 18 | 3% | 2% | -60% | -94% | -93% |
| Under 1 min | 7226 | 16 | 1% | 0% | -68% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1390 | 11 | 5% | 3% | -1% | -89% | -89% |
| HYPE | 1383 | 4 | 4% | 2% | -64% | -90% | -89% |
| ETH | 1380 | 8 | 5% | 3% | -29% | -88% | -87% |
| BNB | 1380 | 5 | 4% | 2% | -56% | -90% | -89% |
| DOGE | 1378 | 2 | 4% | 2% | -82% | -91% | -90% |
| SOL | 1375 | 2 | 3% | 1% | -82% | -93% | -92% |
| BTC | 1368 | 7 | 5% | 2% | -31% | -88% | -91% |
| XRP | 1367 | 7 | 2% | 1% | -37% | -85% | -86% |
| NEAR | 1365 | 8 | 5% | 2% | -23% | -77% | -78% |
| GOLD | 751 | 1 | 4% | 1% | -84% | -92% | -93% |
| SILVER | 733 | 4 | 3% | 1% | -36% | -78% | -77% |
| WTI | 705 | 3 | 3% | 1% | -51% | -94% | -96% |
| COPPER | 650 | 1 | 2% | 2% | -86% | -97% | -96% |
| PLATINUM | 623 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 572 | 3 | 2% | 2% | -51% | -96% | -95% |
| PALLADIUM | 572 | 1 | 1% | 0% | -84% | -98% | -98% |
| EURUSD | 560 | 3 | 2% | 1% | -50% | -79% | -78% |
| GBPUSD | 526 | 1 | 2% | 1% | -82% | -97% | -97% |
| USDJPY | 479 | 3 | 1% | 1% | -42% | -99% | -98% |
| AUDUSD | 119 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 109 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9507 | 38 | 3% | 2% | -54% | -89% | -88% |
| DOWN (bought NO) | 9278 | 36 | 4% | 2% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2116 | 11 | 2% | 1% | -13% | -78% | -78% |
| 0.05–0.1% | 2168 | 7 | 3% | 1% | -53% | -92% | -91% |
| 0.1–0.2% | 3133 | 10 | 4% | 2% | -60% | -90% | -90% |
| 0.2–0.5% | 3576 | 20 | 6% | 3% | -38% | -88% | -88% |
| Over 0.5% | 1390 | 6 | 6% | 2% | -55% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4717 | 20 | 4% | 2% | -52% | -87% | -88% |
| Morning (6am–12pm) | 4329 | 23 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 4482 | 16 | 3% | 1% | -58% | -87% | -88% |
| Evening (6pm–12am) | 5257 | 15 | 3% | 2% | -67% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,512 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/14 9:44:56 PM | WTI | DOWN | 3 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 9:44:56 PM | PALLADIUM | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:44:40 PM | ZEC | UP | 19 sec | +0.036% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:44:40 PM | SILVER | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:44:24 PM | EURUSD | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:44:24 PM | DOGE | UP | 35 sec | -0.155% | 0¢ | ❌ Lost | $0.00 |
| 10/14 9:44:24 PM | NATGAS | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:44:24 PM | SOL | UP | 35 sec | -0.103% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:44:08 PM | XRP | UP | 52 sec | -0.276% | 0¢ | ❌ Lost | $0.00 |
| 10/14 9:44:08 PM | BNB | UP | 52 sec | -0.135% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 9:43:50 PM | PLATINUM | DOWN | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:43:50 PM | BTC | UP | 69 sec | -0.197% | 0¢ | ❌ Lost | $0.00 |
| 10/14 9:43:34 PM | ETH | UP | 85 sec | -0.205% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 9:43:18 PM | NEAR | UP | 1.7 min | -0.750% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 9:42:46 PM | GOLD | DOWN | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 9:42:30 PM | USDCAD | UP | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 9:40:19 PM | HYPE | UP | 4.7 min | -0.738% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 9:29:55 PM | EURUSD | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:29:55 PM | SOL | DOWN | 4 sec | +0.069% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:29:55 PM | GBPUSD | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:29:07 PM | USDJPY | UP | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:29:07 PM | DOGE | UP | 53 sec | -0.331% | 0¢ | ❌ Lost | $0.00 |
| 10/14 9:28:49 PM | WTI | DOWN | 71 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 9:28:02 PM | GOLD | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:28:02 PM | ETH | UP | 2.0 min | -0.309% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 9:28:02 PM | XRP | UP | 2.0 min | -0.466% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 9:28:02 PM | PLATINUM | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:28:02 PM | NEAR | UP | 2.0 min | -1.007% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 9:28:02 PM | BNB | UP | 2.0 min | -0.241% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 9:28:02 PM | BTC | UP | 2.0 min | -0.304% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
