# 15-Minute 1¢ Study

*Updated Wed Oct 28, 4:53 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2962 finished bets | 1% | $85.95 | +26% | +2.90¢ | $87.90 / -$1.95 |

*Expect about **98 buys a day** (~$14.72/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2747 | $48.05 | +16% |
| Volatility model ≥ 2%, hold to the close | 5487 | $16.70 | +2% |
| Momentum model ≥ 2%, hold to the close | 4538 | -$52.60 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 36131 | 36123 | 138 (0%) | 1.07% | -$2,471.55 (-56%) | Hold to the close: -$2,471.55 (-56%) |

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
| Volatility model | 22634 | 4.7% | 0.4% (92) | -666% | ❌ Worse |
| Momentum model | 22634 | 4.6% | 0.4% (92) | -691% | ❌ Worse |
| Mean-reversion model | 22634 | 8.0% | 0.4% (92) | -809% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 22634 | 92 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5487 | 49 | +2% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2962 | 30 | +26% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1682 | 19 | +59% | -68% | -66% | -64% |
| Momentum model ≥ 2% | 4538 | 34 | -10% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 2747 | 25 | +16% | -78% | -77% | -74% |
| Momentum model ≥ 10% | 1806 | 17 | +30% | -72% | -71% | -68% |
| Mean-reversion model ≥ 2% | 9228 | 63 | -25% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6481 | 53 | -10% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4334 | 38 | -1% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 22834 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8598 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4691 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 36123 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 138 | 0% | -$2,471.55 | -56% | — |
| Sell at 2¢ | 1365 | 4% | -$3,852.65 | -87% | 47 sec |
| Sell at 3¢ | 937 | 3% | -$3,842.12 | -87% | 48 sec |
| Sell at 5¢ | 651 | 2% | -$3,784.40 | -86% | 62 sec |
| Sell at 10¢ | 399 | 1% | -$3,628.86 | -82% | 65 sec |
| Sell at 25¢ | 215 | 1% | -$3,341.90 | -76% | 83 sec |
| Sell at 50¢ | 142 | 0% | -$3,011.05 | -68% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1603 | 8 | 11% | 4% | -52% | -81% | -82% |
| 2–5 min | 11541 | 66 | 7% | 3% | -44% | -87% | -87% |
| 1–2 min | 9167 | 32 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 13808 | 32 | 1% | 0% | -67% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2557 | 12 | 5% | 2% | -40% | -89% | -88% |
| HYPE | 2550 | 8 | 5% | 3% | -61% | -89% | -87% |
| BNB | 2549 | 15 | 5% | 2% | -27% | -85% | -84% |
| SOL | 2542 | 7 | 4% | 2% | -65% | -92% | -92% |
| ETH | 2537 | 11 | 6% | 3% | -48% | -86% | -85% |
| DOGE | 2534 | 5 | 4% | 2% | -75% | -90% | -90% |
| XRP | 2525 | 11 | 3% | 1% | -46% | -89% | -89% |
| NEAR | 2521 | 12 | 5% | 2% | -38% | -82% | -82% |
| BTC | 2519 | 13 | 5% | 2% | -31% | -88% | -89% |
| GOLD | 1362 | 5 | 4% | 2% | -56% | -81% | -83% |
| SILVER | 1331 | 6 | 4% | 2% | -47% | -82% | -82% |
| WTI | 1313 | 4 | 3% | 1% | -64% | -93% | -94% |
| PLATINUM | 1179 | 1 | 2% | 1% | -92% | -97% | -97% |
| COPPER | 1125 | 4 | 1% | 1% | -67% | -73% | -73% |
| EURUSD | 1102 | 3 | 2% | 1% | -75% | -88% | -88% |
| NATGAS | 1085 | 6 | 2% | 1% | -48% | -79% | -79% |
| PALLADIUM | 1044 | 2 | 1% | 0% | -82% | -89% | -89% |
| GBPUSD | 1042 | 2 | 2% | 1% | -82% | -96% | -97% |
| USDJPY | 1026 | 5 | 2% | 1% | -55% | -97% | -96% |
| AUDUSD | 582 | 4 | 1% | 1% | -36% | -82% | -80% |
| USDCAD | 543 | 0 | 1% | 0% | -100% | -97% | -98% |
| BRENT | 159 | 0 | 1% | 1% | -100% | -99% | -98% |
| 10YRRATE | 108 | 0 | 4% | 0% | -100% | -94% | -93% |
| 30YRRATE | 100 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 96 | 1 | 3% | 1% | -3% | +3% | +3% |
| 5YRRATE | 92 | 1 | 4% | 2% | +1% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 18275 | 77 | 4% | 2% | -52% | -87% | -86% |
| DOWN (bought NO) | 17848 | 61 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3772 | 19 | 2% | 1% | -14% | -81% | -80% |
| 0.05–0.1% | 3931 | 14 | 3% | 2% | -47% | -92% | -91% |
| 0.1–0.2% | 5948 | 22 | 5% | 2% | -54% | -90% | -89% |
| 0.2–0.5% | 6704 | 29 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2475 | 10 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9150 | 35 | 4% | 2% | -57% | -86% | -86% |
| Morning (6am–12pm) | 8741 | 42 | 4% | 2% | -45% | -86% | -85% |
| Afternoon (12–6pm) | 8419 | 29 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 9813 | 32 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,620 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/28 4:44:57 AM | COPPER | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:44:57 AM | USDCAD | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:44:57 AM | GOLD | DOWN | 2 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/28 4:44:57 AM | 30YRRATE | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:44:41 AM | ETH | UP | 18 sec | -0.019% | 0¢ | ❌ Lost | $0.00 |
| 10/28 4:44:41 AM | PLATINUM | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:44:41 AM | 10YRRATE | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:44:41 AM | GBPUSD | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:44:25 AM | BTC | DOWN | 34 sec | +0.021% | 0¢ | ❌ Lost | $0.00 |
| 10/28 4:44:25 AM | PALLADIUM | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:44:09 AM | 2YRRATE | UP | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:44:09 AM | 5YRRATE | UP | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:43:34 AM | NEAR | UP | 86 sec | -0.293% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 4:43:18 AM | XRP | UP | 1.7 min | -0.105% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 4:43:03 AM | SILVER | DOWN | 1.9 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/28 4:43:03 AM | SOL | UP | 1.9 min | -0.158% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 4:43:03 AM | BNB | DOWN | 1.9 min | +0.098% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 4:42:47 AM | WTI | UP | 2.2 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/28 4:40:53 AM | HYPE | UP | 4.1 min | -0.309% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 4:40:37 AM | ZEC | UP | 4.4 min | -0.488% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 4:39:49 AM | DOGE | UP | 5.2 min | -0.294% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 4:29:58 AM | COPPER | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:29:58 AM | AUDUSD | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:29:58 AM | ETH | DOWN | 1 sec | +0.021% | 0¢ | ❌ Lost | $0.00 |
| 10/28 4:29:58 AM | USDCAD | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:29:58 AM | PLATINUM | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:29:58 AM | BRENT | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:29:58 AM | DOGE | UP | 1 sec | -0.017% | 0¢ | ❌ Lost | $0.00 |
| 10/28 4:29:58 AM | 30YRRATE | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 4:29:42 AM | BTC | DOWN | 17 sec | +0.018% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
