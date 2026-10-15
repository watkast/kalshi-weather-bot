# 15-Minute 1¢ Study

*Updated Thu Oct 15, 1:41 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1536 finished bets | 1% | $82.05 | +48% | +5.34¢ | $29.20 / $52.85 |

*Expect about **88 buys a day** (~$13.13/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1434 | $55.05 | +36% |
| Momentum model ≥ 2%, hold to the close | 2408 | $1.30 | +0% |
| Volatility model ≥ 5%, sell at 50¢ | 1536 | -$13.20 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 19667 | 19657 | 78 (0%) | 1.07% | -$1,294.95 (-54%) | Hold to the close: -$1,294.95 (-54%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 12662 | 4.5% | 0.4% (53) | -636% | ❌ Worse |
| Momentum model | 12662 | 4.4% | 0.4% (53) | -660% | ❌ Worse |
| Mean-reversion model | 12662 | 7.4% | 0.4% (53) | -758% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12662 | 53 | -48% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2790 | 23 | -4% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1536 | 18 | +48% | -74% | -72% | -67% |
| Volatility model ≥ 10% | 905 | 11 | +73% | -65% | -63% | -60% |
| Momentum model ≥ 2% | 2408 | 20 | +0% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1434 | 15 | +36% | -77% | -76% | -73% |
| Momentum model ≥ 10% | 960 | 10 | +46% | -71% | -71% | -66% |
| Mean-reversion model ≥ 2% | 4742 | 33 | -24% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 3254 | 26 | -12% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2128 | 15 | -19% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12860 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4843 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1954 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 19657 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 78 | 0% | -$1,294.95 | -54% | — |
| Sell at 2¢ | 697 | 4% | -$2,121.73 | -89% | 41 sec |
| Sell at 3¢ | 470 | 2% | -$2,119.65 | -89% | 47 sec |
| Sell at 5¢ | 342 | 2% | -$2,080.65 | -87% | 50 sec |
| Sell at 10¢ | 213 | 1% | -$1,995.92 | -84% | 63 sec |
| Sell at 25¢ | 124 | 1% | -$1,822.51 | -76% | 80 sec |
| Sell at 50¢ | 81 | 0% | -$1,616.20 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 631 | 5 | 11% | 3% | -25% | -81% | -85% |
| 2–5 min | 6367 | 36 | 7% | 3% | -44% | -88% | -88% |
| 1–2 min | 5119 | 20 | 3% | 2% | -58% | -92% | -91% |
| Under 1 min | 7536 | 17 | 1% | 0% | -67% | -89% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1444 | 11 | 5% | 3% | -5% | -89% | -89% |
| HYPE | 1438 | 5 | 4% | 2% | -57% | -90% | -89% |
| ETH | 1432 | 8 | 5% | 3% | -32% | -88% | -87% |
| DOGE | 1432 | 2 | 4% | 2% | -82% | -91% | -90% |
| BNB | 1431 | 5 | 4% | 2% | -57% | -90% | -89% |
| SOL | 1426 | 2 | 3% | 1% | -83% | -93% | -92% |
| XRP | 1421 | 7 | 3% | 1% | -39% | -85% | -86% |
| BTC | 1419 | 7 | 5% | 2% | -34% | -88% | -91% |
| NEAR | 1417 | 8 | 5% | 3% | -27% | -78% | -78% |
| GOLD | 789 | 1 | 4% | 1% | -85% | -92% | -93% |
| SILVER | 767 | 4 | 3% | 1% | -39% | -79% | -79% |
| WTI | 742 | 3 | 3% | 1% | -53% | -94% | -96% |
| COPPER | 683 | 2 | 2% | 1% | -73% | -83% | -83% |
| PLATINUM | 651 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 606 | 4 | 2% | 2% | -38% | -96% | -94% |
| PALLADIUM | 605 | 2 | 1% | 0% | -69% | -83% | -83% |
| EURUSD | 597 | 3 | 3% | 1% | -53% | -80% | -79% |
| GBPUSD | 560 | 1 | 2% | 1% | -83% | -97% | -96% |
| USDJPY | 520 | 3 | 1% | 1% | -46% | -99% | -98% |
| AUDUSD | 146 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 131 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9907 | 39 | 4% | 2% | -55% | -89% | -88% |
| DOWN (bought NO) | 9750 | 39 | 4% | 2% | -54% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2154 | 11 | 2% | 1% | -14% | -78% | -78% |
| 0.05–0.1% | 2217 | 7 | 3% | 1% | -54% | -92% | -92% |
| 0.1–0.2% | 3233 | 10 | 4% | 2% | -62% | -90% | -90% |
| 0.2–0.5% | 3751 | 21 | 6% | 3% | -38% | -88% | -88% |
| Over 0.5% | 1502 | 6 | 6% | 2% | -59% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4976 | 20 | 4% | 2% | -54% | -87% | -87% |
| Morning (6am–12pm) | 4701 | 26 | 4% | 2% | -36% | -86% | -86% |
| Afternoon (12–6pm) | 4571 | 16 | 3% | 1% | -59% | -88% | -88% |
| Evening (6pm–12am) | 5409 | 16 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,464 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/15 1:41:05 PM | SILVER | DOWN | 3.9 min | — | — | In play | — |
| 10/15 1:41:05 PM | PLATINUM | DOWN | 3.9 min | — | — | In play | — |
| 10/15 1:40:49 PM | GOLD | DOWN | 4.2 min | — | — | In play | — |
| 10/15 1:29:53 PM | WTI | UP | 7 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 1:29:53 PM | PLATINUM | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 1:29:53 PM | GOLD | UP | 7 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/15 1:29:53 PM | SOL | UP | 7 sec | -0.103% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 1:29:37 PM | HYPE | DOWN | 23 sec | +0.009% | 0¢ | ❌ Lost | $0.00 |
| 10/15 1:29:37 PM | USDJPY | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 1:29:37 PM | SILVER | UP | 23 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 1:29:21 PM | PALLADIUM | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 1:29:04 PM | NATGAS | UP | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 1:29:04 PM | BNB | UP | 55 sec | -0.044% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 1:28:18 PM | GBPUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 1:28:18 PM | EURUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 1:28:18 PM | ZEC | DOWN | 1.7 min | +0.345% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 1:27:46 PM | DOGE | DOWN | 2.2 min | +0.160% | 6¢ | ❌ Lost | -$0.15 |
| 10/15 1:27:46 PM | BTC | DOWN | 2.2 min | +0.102% | 2¢ | ❌ Lost | -$0.15 |
| 10/15 1:26:26 PM | XRP | DOWN | 3.6 min | +0.276% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 1:25:23 PM | NEAR | DOWN | 4.6 min | +0.636% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 1:24:51 PM | ETH | DOWN | 5.1 min | +0.352% | 3¢ | ❌ Lost | -$0.15 |
| 10/15 1:14:49 PM | AUDUSD | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 1:14:49 PM | COPPER | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 1:14:49 PM | XRP | DOWN | 10 sec | +0.037% | 0¢ | ❌ Lost | $0.00 |
| 10/15 1:14:49 PM | BNB | UP | 10 sec | -0.014% | 0¢ | ❌ Lost | $0.00 |
| 10/15 1:14:49 PM | PALLADIUM | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 1:14:33 PM | ETH | DOWN | 26 sec | +0.027% | 0¢ | ❌ Lost | $0.00 |
| 10/15 1:14:03 PM | NATGAS | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 1:14:03 PM | SOL | DOWN | 56 sec | +0.121% | 0¢ | ❌ Lost | $0.00 |
| 10/15 1:13:47 PM | GBPUSD | UP | 73 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
