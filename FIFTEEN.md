# 15-Minute 1¢ Study

*Updated Sat Oct 17, 3:09 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1734 finished bets | 1% | $73.85 | +38% | +4.26¢ | $31.80 / $42.05 |

*Expect about **91 buys a day** (~$13.62/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1597 | $37.05 | +21% |
| Momentum model ≥ 2%, hold to the close | 2696 | -$18.45 | -6% |
| Volatility model ≥ 5%, sell at 50¢ | 1734 | -$28.65 | -15% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 21698 | 21691 | 81 (0%) | 1.07% | -$1,503.15 (-57%) | Hold to the close: -$1,503.15 (-57%) |

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
| Volatility model | 13967 | 4.5% | 0.4% (55) | -663% | ❌ Worse |
| Momentum model | 13967 | 4.4% | 0.4% (55) | -686% | ❌ Worse |
| Mean-reversion model | 13967 | 7.5% | 0.4% (55) | -796% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13967 | 55 | -51% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 3149 | 24 | -12% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 1734 | 19 | +38% | -74% | -73% | -69% |
| Volatility model ≥ 10% | 1012 | 11 | +55% | -66% | -66% | -63% |
| Momentum model ≥ 2% | 2696 | 21 | -6% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 1597 | 15 | +21% | -78% | -77% | -73% |
| Momentum model ≥ 10% | 1062 | 10 | +32% | -73% | -73% | -68% |
| Mean-reversion model ≥ 2% | 5313 | 35 | -28% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3669 | 27 | -19% | -82% | -82% | -79% |
| Mean-reversion model ≥ 10% | 2415 | 16 | -24% | -80% | -80% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 14165 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5309 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 21691 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 81 | 0% | -$1,503.15 | -57% | — |
| Sell at 2¢ | 775 | 4% | -$2,337.65 | -89% | 37 sec |
| Sell at 3¢ | 519 | 2% | -$2,336.74 | -89% | 47 sec |
| Sell at 5¢ | 373 | 2% | -$2,296.70 | -87% | 50 sec |
| Sell at 10¢ | 225 | 1% | -$2,216.40 | -84% | 63 sec |
| Sell at 25¢ | 127 | 1% | -$2,048.78 | -78% | 79 sec |
| Sell at 50¢ | 84 | 0% | -$1,832.15 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 740 | 5 | 10% | 3% | -36% | -82% | -85% |
| 2–5 min | 7009 | 38 | 7% | 3% | -47% | -88% | -88% |
| 1–2 min | 5641 | 20 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 8297 | 18 | 1% | 0% | -69% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1592 | 11 | 5% | 3% | -14% | -90% | -90% |
| HYPE | 1587 | 6 | 4% | 2% | -53% | -90% | -88% |
| ETH | 1578 | 8 | 6% | 3% | -39% | -87% | -87% |
| DOGE | 1576 | 2 | 4% | 2% | -84% | -91% | -90% |
| BNB | 1576 | 6 | 5% | 2% | -53% | -89% | -89% |
| SOL | 1572 | 2 | 3% | 2% | -84% | -92% | -92% |
| XRP | 1565 | 7 | 2% | 1% | -45% | -86% | -87% |
| NEAR | 1561 | 8 | 6% | 3% | -33% | -78% | -78% |
| BTC | 1558 | 7 | 5% | 2% | -40% | -88% | -91% |
| GOLD | 864 | 1 | 3% | 1% | -86% | -92% | -94% |
| SILVER | 841 | 4 | 3% | 1% | -45% | -80% | -80% |
| WTI | 821 | 3 | 3% | 1% | -57% | -94% | -95% |
| COPPER | 735 | 2 | 2% | 1% | -75% | -84% | -84% |
| PLATINUM | 722 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 667 | 5 | 2% | 2% | -30% | -82% | -81% |
| PALLADIUM | 659 | 2 | 1% | 0% | -72% | -84% | -84% |
| EURUSD | 659 | 3 | 3% | 1% | -58% | -81% | -81% |
| GBPUSD | 615 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 574 | 3 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 200 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 169 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10932 | 41 | 4% | 2% | -57% | -89% | -89% |
| DOWN (bought NO) | 10759 | 40 | 4% | 2% | -57% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2386 | 11 | 2% | 1% | -23% | -80% | -80% |
| 0.05–0.1% | 2442 | 7 | 3% | 1% | -58% | -92% | -92% |
| 0.1–0.2% | 3568 | 12 | 4% | 2% | -58% | -90% | -90% |
| 0.2–0.5% | 4132 | 21 | 6% | 3% | -44% | -88% | -88% |
| Over 0.5% | 1634 | 6 | 6% | 3% | -62% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5460 | 21 | 4% | 2% | -56% | -88% | -88% |
| Morning (6am–12pm) | 5104 | 27 | 4% | 2% | -39% | -87% | -86% |
| Afternoon (12–6pm) | 5104 | 16 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 6023 | 17 | 3% | 2% | -68% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,505 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/17 2:59:56 AM | HYPE | DOWN | 3 sec | -0.040% | 0¢ | ❌ Lost | $0.00 |
| 10/17 2:59:08 AM | BTC | DOWN | 51 sec | +0.057% | 0¢ | ❌ Lost | $0.00 |
| 10/17 2:58:35 AM | DOGE | UP | 84 sec | -0.056% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 2:58:19 AM | XRP | DOWN | 1.7 min | +0.046% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 2:57:13 AM | NEAR | DOWN | 2.8 min | +0.594% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 2:56:40 AM | ETH | DOWN | 3.3 min | +0.118% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 2:56:24 AM | ZEC | DOWN | 3.6 min | +0.458% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 2:56:24 AM | SOL | DOWN | 3.6 min | +0.133% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 2:44:58 AM | HYPE | UP | 2 sec | -0.034% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 2:44:42 AM | BNB | UP | 18 sec | -0.010% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 2:44:42 AM | ZEC | DOWN | 18 sec | +0.047% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 2:43:37 AM | SOL | UP | 82 sec | -0.069% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 2:43:37 AM | ETH | UP | 82 sec | -0.036% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 2:43:37 AM | BTC | UP | 82 sec | -0.039% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 2:42:16 AM | NEAR | DOWN | 2.7 min | +0.285% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 2:41:58 AM | DOGE | UP | 3.0 min | -0.148% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 2:39:34 AM | XRP | UP | 5.4 min | -0.244% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 2:29:49 AM | ETH | UP | 10 sec | -0.007% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 2:29:49 AM | BTC | DOWN | 10 sec | +0.002% | 0¢ | ❌ Lost | $0.00 |
| 10/17 2:29:49 AM | ZEC | DOWN | 10 sec | +0.024% | 0¢ | ❌ Lost | $0.00 |
| 10/17 2:29:33 AM | BNB | UP | 27 sec | -0.025% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 2:29:17 AM | DOGE | UP | 43 sec | -0.070% | 0¢ | ❌ Lost | $0.00 |
| 10/17 2:28:46 AM | XRP | DOWN | 73 sec | +0.061% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 2:28:31 AM | HYPE | DOWN | 88 sec | +0.072% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 2:28:15 AM | SOL | UP | 1.7 min | -0.115% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 2:14:49 AM | BTC | DOWN | 10 sec | +0.011% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 2:14:49 AM | ZEC | UP | 10 sec | -0.047% | 0¢ | ❌ Lost | $0.00 |
| 10/17 2:14:02 AM | ETH | DOWN | 57 sec | +0.039% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 2:14:02 AM | DOGE | DOWN | 57 sec | +0.024% | 0¢ | ❌ Lost | $0.00 |
| 10/17 2:14:02 AM | XRP | DOWN | 57 sec | +0.054% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
