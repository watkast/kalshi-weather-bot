# 15-Minute 1¢ Study

*Updated Sun Oct 4, 8:05 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 564 finished bets | 1% | $23.40 | +39% | +4.15¢ | -$16.90 / $40.30 |

*Expect about **83 buys a day** (~$12.43/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 2%, hold to the close | 1042 | $14.60 | +12% |
| 5+ min left, hold to the close | 191 | $13.80 | +49% |
| Momentum model ≥ 5%, hold to the close | 568 | $9.70 | +16% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 7872 | 7866 | 36 (0%) | 1.07% | -$437.25 (-46%) | Hold to the close: -$437.25 (-46%) |

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
| Volatility model | 5243 | 4.2% | 0.5% (24) | -604% | ❌ Worse |
| Momentum model | 5243 | 4.3% | 0.5% (24) | -635% | ❌ Worse |
| Mean-reversion model | 5243 | 6.9% | 0.5% (24) | -701% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5243 | 24 | -42% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 1042 | 10 | +12% | -69% | -69% | -63% |
| Volatility model ≥ 5% | 564 | 6 | +39% | -55% | -54% | -49% |
| Volatility model ≥ 10% | 352 | 4 | +67% | -36% | -37% | -31% |
| Momentum model ≥ 2% | 917 | 7 | -7% | -69% | -71% | -68% |
| Momentum model ≥ 5% | 568 | 5 | +16% | -60% | -63% | -60% |
| Momentum model ≥ 10% | 394 | 4 | +46% | -47% | -48% | -45% |
| Mean-reversion model ≥ 2% | 1835 | 13 | -23% | -82% | -83% | -78% |
| Mean-reversion model ≥ 5% | 1233 | 11 | -1% | -79% | -79% | -72% |
| Mean-reversion model ≥ 10% | 814 | 8 | +14% | -77% | -78% | -70% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5440 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1848 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 578 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 7866 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 36 | 0% | -$437.25 | -46% | — |
| Sell at 2¢ | 316 | 4% | -$831.09 | -88% | 33 sec |
| Sell at 3¢ | 204 | 3% | -$833.69 | -89% | 47 sec |
| Sell at 5¢ | 150 | 2% | -$815.75 | -87% | 61 sec |
| Sell at 10¢ | 104 | 1% | -$763.01 | -81% | 72 sec |
| Sell at 25¢ | 57 | 1% | -$682.58 | -73% | 1.6 min |
| Sell at 50¢ | 35 | 0% | -$593.00 | -63% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 188 | 3 | 12% | 3% | +51% | -78% | -87% |
| 2–5 min | 2532 | 19 | 8% | 4% | -27% | -86% | -86% |
| 1–2 min | 2077 | 9 | 3% | 2% | -53% | -93% | -93% |
| Under 1 min | 3066 | 5 | 1% | 0% | -75% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 614 | 5 | 5% | 3% | -3% | -89% | -89% |
| DOGE | 609 | 2 | 4% | 1% | -57% | -91% | -91% |
| HYPE | 608 | 3 | 5% | 3% | -40% | -88% | -85% |
| ETH | 607 | 5 | 6% | 3% | +4% | -86% | -85% |
| BNB | 603 | 2 | 4% | 2% | -60% | -90% | -92% |
| SOL | 602 | 0 | 3% | 1% | -100% | -93% | -91% |
| BTC | 600 | 3 | 6% | 2% | -34% | -86% | -90% |
| XRP | 600 | 4 | 2% | 1% | -14% | -75% | -75% |
| NEAR | 597 | 2 | 6% | 3% | -56% | -63% | -64% |
| GOLD | 313 | 0 | 4% | 1% | -100% | -90% | -92% |
| SILVER | 299 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 285 | 2 | 3% | 1% | -26% | -94% | -96% |
| COPPER | 263 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 234 | 2 | 3% | 2% | -20% | -94% | -92% |
| PLATINUM | 231 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 223 | 1 | 2% | 1% | -58% | -96% | -98% |
| EURUSD | 205 | 1 | 5% | 3% | -54% | -92% | -90% |
| GBPUSD | 200 | 1 | 4% | 2% | -53% | -93% | -94% |
| USDJPY | 173 | 3 | 2% | 2% | +62% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 3958 | 20 | 4% | 2% | -40% | -88% | -87% |
| DOWN (bought NO) | 3908 | 16 | 4% | 2% | -52% | -89% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 916 | 7 | 2% | 1% | +29% | -57% | -56% |
| 0.05–0.1% | 926 | 2 | 3% | 1% | -68% | -91% | -92% |
| 0.1–0.2% | 1344 | 5 | 4% | 2% | -52% | -90% | -91% |
| 0.2–0.5% | 1588 | 8 | 6% | 4% | -44% | -87% | -86% |
| Over 0.5% | 664 | 4 | 7% | 3% | -38% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1882 | 8 | 5% | 2% | -50% | -84% | -86% |
| Morning (6am–12pm) | 2058 | 17 | 5% | 3% | -5% | -89% | -87% |
| Afternoon (12–6pm) | 1751 | 4 | 3% | 1% | -73% | -86% | -87% |
| Evening (6pm–12am) | 2175 | 7 | 3% | 2% | -62% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,142 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/4 7:59:56 PM | EURUSD | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 7:59:48 PM | ZEC | UP | 12 sec | -0.179% | 0¢ | ❌ Lost | $0.00 |
| 10/4 7:59:42 PM | SOL | DOWN | 18 sec | +0.009% | 0¢ | ❌ Lost | $0.00 |
| 10/4 7:59:38 PM | BNB | DOWN | 22 sec | +0.015% | 0¢ | ❌ Lost | $0.00 |
| 10/4 7:59:38 PM | HYPE | DOWN | 22 sec | +0.012% | 0¢ | ❌ Lost | $0.00 |
| 10/4 7:59:26 PM | XRP | UP | 34 sec | -0.092% | 0¢ | ❌ Lost | $0.00 |
| 10/4 7:59:09 PM | ETH | UP | 50 sec | -0.042% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 7:58:43 PM | BTC | UP | 77 sec | -0.130% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 7:58:25 PM | USDJPY | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 7:58:17 PM | COPPER | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 7:58:11 PM | NATGAS | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 7:58:09 PM | PLATINUM | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 7:57:11 PM | SILVER | DOWN | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/4 7:55:54 PM | GOLD | DOWN | 4.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/4 7:44:55 PM | GOLD | UP | 4 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/4 7:44:55 PM | SILVER | UP | 4 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/4 7:44:23 PM | USDJPY | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 7:44:09 PM | PALLADIUM | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 7:43:51 PM | EURUSD | UP | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 7:43:13 PM | BTC | UP | 1.8 min | -0.263% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 7:43:01 PM | BNB | UP | 2.0 min | -0.241% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 7:43:00 PM | ETH | UP | 2.0 min | -0.231% | 0¢ | ❌ Lost | $0.00 |
| 10/4 7:43:00 PM | XRP | UP | 2.0 min | -0.386% | 0¢ | ❌ Lost | $0.00 |
| 10/4 7:42:49 PM | HYPE | UP | 2.2 min | -0.433% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 7:41:59 PM | ZEC | UP | 3.0 min | -0.914% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 7:41:55 PM | NEAR | UP | 3.1 min | -0.665% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 7:41:38 PM | DOGE | UP | 3.4 min | -0.635% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 7:40:12 PM | SOL | UP | 4.8 min | -0.397% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 7:29:44 PM | NEAR | UP | 16 sec | -0.212% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 7:29:26 PM | ETH | DOWN | 34 sec | +0.118% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
