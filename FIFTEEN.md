# 15-Minute 1¢ Study

*Updated Thu Oct 15, 2:53 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1542 finished bets | 1% | $81.30 | +48% | +5.27¢ | $28.90 / $52.40 |

*Expect about **88 buys a day** (~$13.15/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1438 | $54.60 | +35% |
| Momentum model ≥ 2%, hold to the close | 2414 | $0.55 | +0% |
| Volatility model ≥ 5%, sell at 50¢ | 1542 | -$13.95 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 19744 | 19737 | 78 (0%) | 1.07% | -$1,305.00 (-54%) | Hold to the close: -$1,305.00 (-54%) |

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
| Volatility model | 12705 | 4.5% | 0.4% (53) | -638% | ❌ Worse |
| Momentum model | 12705 | 4.4% | 0.4% (53) | -662% | ❌ Worse |
| Mean-reversion model | 12705 | 7.4% | 0.4% (53) | -761% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12705 | 53 | -48% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2804 | 23 | -5% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1542 | 18 | +48% | -74% | -72% | -67% |
| Volatility model ≥ 10% | 909 | 11 | +72% | -65% | -64% | -60% |
| Momentum model ≥ 2% | 2414 | 20 | +0% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1438 | 15 | +35% | -77% | -76% | -73% |
| Momentum model ≥ 10% | 963 | 10 | +46% | -71% | -71% | -66% |
| Mean-reversion model ≥ 2% | 4758 | 33 | -24% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 3266 | 26 | -12% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2137 | 15 | -19% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12903 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4864 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1970 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 19737 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 78 | 0% | -$1,305.00 | -54% | — |
| Sell at 2¢ | 701 | 4% | -$2,130.74 | -89% | 37 sec |
| Sell at 3¢ | 472 | 2% | -$2,128.92 | -89% | 47 sec |
| Sell at 5¢ | 344 | 2% | -$2,089.40 | -87% | 50 sec |
| Sell at 10¢ | 213 | 1% | -$2,005.97 | -84% | 63 sec |
| Sell at 25¢ | 124 | 1% | -$1,832.56 | -76% | 80 sec |
| Sell at 50¢ | 81 | 0% | -$1,626.25 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 632 | 5 | 11% | 3% | -25% | -81% | -85% |
| 2–5 min | 6394 | 36 | 7% | 3% | -44% | -88% | -88% |
| 1–2 min | 5138 | 20 | 3% | 2% | -58% | -92% | -91% |
| Under 1 min | 7569 | 17 | 1% | 0% | -68% | -89% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1449 | 11 | 5% | 3% | -5% | -89% | -89% |
| HYPE | 1443 | 5 | 4% | 2% | -57% | -90% | -89% |
| ETH | 1437 | 8 | 5% | 3% | -32% | -88% | -87% |
| DOGE | 1437 | 2 | 4% | 2% | -82% | -91% | -90% |
| BNB | 1436 | 5 | 4% | 2% | -57% | -90% | -90% |
| SOL | 1431 | 2 | 3% | 1% | -83% | -93% | -92% |
| XRP | 1426 | 7 | 3% | 1% | -39% | -85% | -86% |
| BTC | 1423 | 7 | 5% | 2% | -34% | -88% | -91% |
| NEAR | 1421 | 8 | 5% | 3% | -27% | -78% | -78% |
| GOLD | 793 | 1 | 4% | 1% | -85% | -92% | -93% |
| SILVER | 772 | 4 | 3% | 1% | -40% | -79% | -79% |
| WTI | 745 | 3 | 3% | 1% | -53% | -94% | -96% |
| COPPER | 684 | 2 | 2% | 1% | -73% | -83% | -83% |
| PLATINUM | 654 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 609 | 4 | 2% | 2% | -39% | -96% | -94% |
| PALLADIUM | 607 | 2 | 1% | 0% | -69% | -83% | -83% |
| EURUSD | 600 | 3 | 3% | 1% | -53% | -80% | -79% |
| GBPUSD | 563 | 1 | 2% | 1% | -83% | -97% | -96% |
| USDJPY | 524 | 3 | 1% | 1% | -47% | -99% | -98% |
| AUDUSD | 150 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 133 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9946 | 39 | 4% | 2% | -55% | -89% | -88% |
| DOWN (bought NO) | 9791 | 39 | 4% | 2% | -54% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2161 | 11 | 2% | 1% | -14% | -79% | -78% |
| 0.05–0.1% | 2227 | 7 | 3% | 1% | -54% | -92% | -92% |
| 0.1–0.2% | 3246 | 10 | 4% | 2% | -62% | -90% | -90% |
| 0.2–0.5% | 3761 | 21 | 6% | 3% | -38% | -88% | -88% |
| Over 0.5% | 1505 | 6 | 6% | 2% | -59% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4976 | 20 | 4% | 2% | -54% | -87% | -87% |
| Morning (6am–12pm) | 4701 | 26 | 4% | 2% | -36% | -86% | -86% |
| Afternoon (12–6pm) | 4651 | 16 | 3% | 1% | -59% | -88% | -88% |
| Evening (6pm–12am) | 5409 | 16 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,460 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/15 2:44:57 PM | ETH | DOWN | 3 sec | -0.002% | 0¢ | ❌ Lost | $0.00 |
| 10/15 2:44:41 PM | GBPUSD | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 2:44:41 PM | SILVER | UP | 19 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 10/15 2:44:41 PM | USDCAD | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 2:44:41 PM | NEAR | DOWN | 19 sec | +0.086% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 2:44:41 PM | SOL | DOWN | 19 sec | +0.030% | 0¢ | ❌ Lost | $0.00 |
| 10/15 2:44:09 PM | XRP | DOWN | 51 sec | +0.060% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 2:43:53 PM | DOGE | DOWN | 67 sec | +0.080% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 2:42:59 PM | USDJPY | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 2:42:59 PM | EURUSD | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 2:42:43 PM | AUDUSD | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 2:42:11 PM | BNB | UP | 2.8 min | -0.123% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 2:41:54 PM | HYPE | DOWN | 3.1 min | +0.250% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 2:41:38 PM | ZEC | DOWN | 3.4 min | +0.424% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 2:29:52 PM | NATGAS | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 2:29:20 PM | HYPE | DOWN | 39 sec | +0.018% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 2:29:20 PM | PLATINUM | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 2:29:04 PM | SILVER | UP | 56 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/15 2:29:04 PM | AUDUSD | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 2:28:14 PM | GOLD | UP | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 2:27:59 PM | BTC | DOWN | 2.0 min | +0.137% | 0¢ | ❌ Lost | $0.00 |
| 10/15 2:27:41 PM | BNB | DOWN | 2.3 min | +0.051% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 2:27:25 PM | SOL | DOWN | 2.6 min | +0.169% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 2:27:09 PM | DOGE | DOWN | 2.8 min | +0.165% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 2:26:55 PM | XRP | DOWN | 3.1 min | +0.149% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 2:25:35 PM | ETH | DOWN | 4.4 min | +0.274% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 2:24:13 PM | ZEC | DOWN | 5.8 min | +0.641% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 2:14:48 PM | ETH | DOWN | 12 sec | +0.034% | 0¢ | ❌ Lost | $0.00 |
| 10/15 2:14:48 PM | PALLADIUM | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 2:14:48 PM | WTI | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
