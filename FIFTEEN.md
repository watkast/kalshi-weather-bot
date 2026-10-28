# 15-Minute 1¢ Study

*Updated Wed Oct 28, 5:39 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3036 finished bets | 1% | $78.75 | +23% | +2.59¢ | $84.00 / -$5.25 |

*Expect about **99 buys a day** (~$14.83/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2819 | $41.00 | +13% |
| Volatility model ≥ 2%, hold to the close | 5615 | $2.60 | +0% |
| Momentum model ≥ 2%, hold to the close | 4647 | -$64.30 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 37097 | 37088 | 138 (0%) | 1.07% | -$2,594.25 (-57%) | Hold to the close: -$2,594.25 (-57%) |

*In play or awaiting result: 8. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 23070 | 4.7% | 0.4% (92) | -676% | ❌ Worse |
| Momentum model | 23070 | 4.6% | 0.4% (92) | -700% | ❌ Worse |
| Mean-reversion model | 23070 | 8.1% | 0.4% (92) | -820% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 23070 | 92 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5615 | 49 | +0% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 3036 | 30 | +23% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1720 | 19 | +57% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4647 | 34 | -12% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2819 | 25 | +13% | -78% | -77% | -74% |
| Momentum model ≥ 10% | 1846 | 17 | +27% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9432 | 63 | -27% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6614 | 53 | -11% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4416 | 38 | -3% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 23270 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8853 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4965 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 37088 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 138 | 0% | -$2,594.25 | -57% | — |
| Sell at 2¢ | 1412 | 4% | -$3,963.13 | -88% | 47 sec |
| Sell at 3¢ | 971 | 3% | -$3,951.56 | -87% | 48 sec |
| Sell at 5¢ | 673 | 2% | -$3,892.80 | -86% | 63 sec |
| Sell at 10¢ | 408 | 1% | -$3,739.77 | -83% | 65 sec |
| Sell at 25¢ | 218 | 1% | -$3,454.67 | -76% | 83 sec |
| Sell at 50¢ | 143 | 0% | -$3,127.00 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1657 | 8 | 11% | 4% | -54% | -80% | -81% |
| 2–5 min | 11847 | 66 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 9399 | 32 | 3% | 1% | -63% | -92% | -92% |
| Under 1 min | 14181 | 32 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2605 | 12 | 5% | 2% | -41% | -88% | -88% |
| HYPE | 2599 | 8 | 5% | 3% | -62% | -89% | -87% |
| BNB | 2598 | 15 | 5% | 2% | -28% | -85% | -84% |
| SOL | 2591 | 7 | 4% | 2% | -66% | -92% | -91% |
| ETH | 2586 | 11 | 6% | 3% | -49% | -85% | -85% |
| DOGE | 2584 | 5 | 4% | 2% | -76% | -90% | -90% |
| XRP | 2571 | 11 | 3% | 1% | -47% | -89% | -89% |
| NEAR | 2568 | 12 | 5% | 2% | -39% | -82% | -82% |
| BTC | 2568 | 13 | 5% | 2% | -32% | -88% | -89% |
| GOLD | 1397 | 5 | 4% | 2% | -57% | -82% | -83% |
| SILVER | 1367 | 6 | 4% | 2% | -48% | -82% | -81% |
| WTI | 1349 | 4 | 3% | 1% | -65% | -93% | -94% |
| PLATINUM | 1213 | 1 | 2% | 1% | -92% | -97% | -96% |
| COPPER | 1151 | 4 | 1% | 1% | -68% | -73% | -73% |
| EURUSD | 1136 | 3 | 2% | 1% | -75% | -88% | -88% |
| NATGAS | 1116 | 6 | 2% | 1% | -50% | -80% | -79% |
| GBPUSD | 1078 | 2 | 2% | 1% | -83% | -96% | -96% |
| PALLADIUM | 1075 | 2 | 1% | 0% | -83% | -89% | -90% |
| USDJPY | 1058 | 5 | 2% | 1% | -56% | -97% | -96% |
| AUDUSD | 614 | 4 | 1% | 1% | -39% | -83% | -81% |
| USDCAD | 580 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 185 | 0 | 1% | 1% | -100% | -99% | -99% |
| 10YRRATE | 133 | 0 | 5% | 1% | -100% | -92% | -90% |
| 30YRRATE | 125 | 0 | 1% | 0% | -100% | -99% | -98% |
| 2YRRATE | 124 | 1 | 4% | 1% | -25% | -18% | -16% |
| 5YRRATE | 117 | 1 | 6% | 3% | -20% | -90% | -91% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 18758 | 77 | 4% | 2% | -53% | -87% | -87% |
| DOWN (bought NO) | 18330 | 61 | 4% | 2% | -62% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3827 | 19 | 2% | 1% | -15% | -81% | -80% |
| 0.05–0.1% | 4003 | 14 | 3% | 2% | -48% | -92% | -91% |
| 0.1–0.2% | 6062 | 22 | 4% | 2% | -55% | -90% | -89% |
| 0.2–0.5% | 6850 | 29 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2524 | 10 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9229 | 35 | 4% | 2% | -57% | -86% | -86% |
| Morning (6am–12pm) | 9232 | 42 | 4% | 2% | -48% | -86% | -85% |
| Afternoon (12–6pm) | 8814 | 29 | 4% | 2% | -61% | -88% | -88% |
| Evening (6pm–12am) | 9813 | 32 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,556 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/28 5:39:10 PM | ZEC | UP | 5.8 min | -0.833% | — | In play | — |
| 10/28 5:29:54 PM | COPPER | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 5:29:38 PM | PLATINUM | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 5:29:38 PM | BTC | DOWN | 22 sec | +0.019% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 5:29:38 PM | XRP | UP | 22 sec | -0.038% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 5:29:22 PM | NATGAS | UP | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 5:29:22 PM | ETH | UP | 38 sec | -0.045% | 0¢ | ❌ Lost | -$0.15 |
| 10/28 5:29:22 PM | HYPE | UP | 38 sec | -0.109% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 5:29:01 PM | SOL | UP | 59 sec | -0.102% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 5:28:43 PM | EURUSD | DOWN | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 5:27:56 PM | DOGE | UP | 2.0 min | -0.146% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 5:27:40 PM | USDJPY | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 5:27:40 PM | GBPUSD | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 5:27:40 PM | ZEC | DOWN | 2.3 min | +0.252% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 5:27:24 PM | GOLD | UP | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 5:27:08 PM | USDCAD | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 5:26:52 PM | AUDUSD | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 5:26:20 PM | SILVER | UP | 3.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 5:25:30 PM | BNB | DOWN | 4.5 min | +0.121% | 10¢ | ❌ Lost | -$0.15 |
| 10/28 5:14:51 PM | ZEC | DOWN | 8 sec | +0.081% | 0¢ | ❌ Lost | $0.00 |
| 10/28 5:14:51 PM | SOL | UP | 8 sec | -0.041% | 0¢ | ❌ Lost | -$0.15 |
| 10/28 5:14:51 PM | USDCAD | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 5:14:19 PM | NATGAS | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 5:14:19 PM | ETH | DOWN | 40 sec | +0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/28 5:14:19 PM | NEAR | DOWN | 40 sec | +0.061% | 0¢ | ❌ Lost | $0.00 |
| 10/28 5:14:03 PM | DOGE | DOWN | 57 sec | +0.109% | 0¢ | ❌ Lost | $0.00 |
| 10/28 5:14:03 PM | BTC | DOWN | 57 sec | +0.058% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 5:14:03 PM | WTI | DOWN | 57 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 5:13:45 PM | GBPUSD | DOWN | 75 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 5:13:29 PM | HYPE | UP | 1.5 min | -0.198% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
