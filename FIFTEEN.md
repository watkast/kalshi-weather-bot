# 15-Minute 1¢ Study

*Updated Wed Oct 14, 6:24 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1439 finished bets | 1% | $92.85 | +58% | +6.45¢ | $34.75 / $58.10 |

*Expect about **86 buys a day** (~$12.90/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1351 | $64.05 | +44% |
| Momentum model ≥ 2%, hold to the close | 2238 | $20.65 | +8% |
| Volatility model ≥ 2%, hold to the close | 2578 | $10.45 | +3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 18557 | 18550 | 74 (0%) | 1.07% | -$1,212.05 (-54%) | Hold to the close: -$1,212.05 (-54%) |

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
| Volatility model | 12069 | 4.5% | 0.4% (52) | -636% | ❌ Worse |
| Momentum model | 12069 | 4.4% | 0.4% (52) | -662% | ❌ Worse |
| Mean-reversion model | 12069 | 7.3% | 0.4% (52) | -755% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12069 | 52 | -46% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2578 | 23 | +3% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1439 | 18 | +58% | -73% | -71% | -66% |
| Volatility model ≥ 10% | 864 | 11 | +81% | -64% | -62% | -58% |
| Momentum model ≥ 2% | 2238 | 20 | +8% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1351 | 15 | +44% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 911 | 10 | +55% | -70% | -70% | -65% |
| Mean-reversion model ≥ 2% | 4438 | 32 | -21% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3042 | 25 | -9% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1998 | 14 | -19% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12267 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4537 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1746 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 18550 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 74 | 0% | -$1,212.05 | -54% | — |
| Sell at 2¢ | 651 | 4% | -$2,022.79 | -90% | 34 sec |
| Sell at 3¢ | 438 | 2% | -$2,021.23 | -90% | 46 sec |
| Sell at 5¢ | 320 | 2% | -$1,984.05 | -88% | 49 sec |
| Sell at 10¢ | 202 | 1% | -$1,899.43 | -84% | 63 sec |
| Sell at 25¢ | 117 | 1% | -$1,734.78 | -77% | 79 sec |
| Sell at 50¢ | 78 | 0% | -$1,525.55 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 579 | 5 | 10% | 3% | -18% | -82% | -87% |
| 2–5 min | 5979 | 35 | 7% | 3% | -42% | -88% | -88% |
| 1–2 min | 4847 | 18 | 3% | 2% | -60% | -94% | -93% |
| Under 1 min | 7141 | 16 | 1% | 0% | -68% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1376 | 11 | 5% | 3% | -0% | -89% | -89% |
| HYPE | 1370 | 4 | 4% | 2% | -64% | -90% | -89% |
| ETH | 1367 | 8 | 5% | 3% | -29% | -88% | -87% |
| DOGE | 1367 | 2 | 4% | 2% | -82% | -91% | -90% |
| BNB | 1366 | 5 | 4% | 2% | -55% | -90% | -90% |
| SOL | 1363 | 2 | 3% | 1% | -82% | -93% | -92% |
| BTC | 1354 | 7 | 5% | 2% | -31% | -88% | -91% |
| XRP | 1353 | 7 | 2% | 1% | -36% | -86% | -86% |
| NEAR | 1351 | 8 | 5% | 3% | -23% | -77% | -78% |
| GOLD | 738 | 1 | 4% | 1% | -84% | -91% | -93% |
| SILVER | 723 | 4 | 3% | 1% | -36% | -78% | -77% |
| WTI | 694 | 3 | 3% | 1% | -50% | -94% | -96% |
| COPPER | 639 | 1 | 2% | 2% | -85% | -97% | -96% |
| PLATINUM | 613 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 566 | 1 | 1% | 0% | -84% | -98% | -98% |
| NATGAS | 564 | 3 | 2% | 2% | -50% | -96% | -95% |
| EURUSD | 549 | 3 | 3% | 1% | -49% | -79% | -78% |
| GBPUSD | 516 | 1 | 2% | 1% | -82% | -97% | -96% |
| USDJPY | 470 | 3 | 1% | 1% | -40% | -99% | -98% |
| AUDUSD | 109 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 102 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9359 | 38 | 3% | 2% | -53% | -89% | -88% |
| DOWN (bought NO) | 9191 | 36 | 4% | 2% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2109 | 11 | 2% | 1% | -13% | -78% | -78% |
| 0.05–0.1% | 2160 | 7 | 3% | 1% | -53% | -92% | -91% |
| 0.1–0.2% | 3116 | 10 | 4% | 2% | -60% | -91% | -90% |
| 0.2–0.5% | 3524 | 20 | 6% | 3% | -38% | -88% | -88% |
| Over 0.5% | 1355 | 6 | 6% | 2% | -54% | -89% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4717 | 20 | 4% | 2% | -52% | -87% | -88% |
| Morning (6am–12pm) | 4329 | 23 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 4482 | 16 | 3% | 1% | -58% | -87% | -88% |
| Evening (6pm–12am) | 5022 | 15 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,500 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/14 6:14:41 PM | COPPER | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 6:14:41 PM | PLATINUM | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 6:14:22 PM | WTI | UP | 38 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/14 6:14:22 PM | USDCAD | UP | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 6:14:22 PM | BNB | DOWN | 38 sec | +0.025% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 6:14:06 PM | NEAR | UP | 54 sec | -0.381% | 0¢ | ❌ Lost | $0.00 |
| 10/14 6:14:06 PM | SILVER | DOWN | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 6:14:06 PM | AUDUSD | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 6:13:50 PM | BTC | DOWN | 69 sec | +0.163% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 6:13:50 PM | USDJPY | UP | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 6:13:34 PM | DOGE | DOWN | 86 sec | +0.106% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 6:13:34 PM | PALLADIUM | DOWN | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 6:13:15 PM | SOL | DOWN | 1.8 min | +0.162% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 6:12:43 PM | ZEC | DOWN | 2.3 min | +0.376% | 1¢ | ❌ Lost | $0.00 |
| 10/14 6:12:43 PM | XRP | DOWN | 2.3 min | +0.196% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 6:12:26 PM | ETH | DOWN | 2.5 min | +0.236% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 6:11:35 PM | GOLD | DOWN | 3.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 6:10:28 PM | HYPE | DOWN | 4.5 min | +0.404% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 5:59:44 PM | ETH | DOWN | 16 sec | +0.001% | 0¢ | ❌ Lost | $0.00 |
| 10/14 5:59:44 PM | XRP | UP | 16 sec | -0.053% | 0¢ | ❌ Lost | $0.00 |
| 10/14 5:59:24 PM | SOL | UP | 35 sec | -0.076% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:59:08 PM | ZEC | DOWN | 51 sec | +0.187% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 5:59:08 PM | BNB | DOWN | 51 sec | -0.026% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:59:08 PM | GBPUSD | DOWN | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:58:52 PM | BTC | DOWN | 67 sec | +0.104% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:58:52 PM | EURUSD | DOWN | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:58:52 PM | HYPE | UP | 67 sec | -0.097% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 5:58:19 PM | NATGAS | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:57:47 PM | SILVER | DOWN | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 5:57:31 PM | GOLD | DOWN | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
