# 15-Minute 1¢ Study

*Updated Thu Oct 29, 8:07 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3070 finished bets | 1% | $89.60 | +26% | +2.92¢ | $82.05 / $7.55 |

*Expect about **98 buys a day** (~$14.71/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2846 | $38.60 | +12% |
| Volatility model ≥ 2%, hold to the close | 5683 | $9.40 | +1% |
| Volatility model ≥ 5%, sell at 50¢ | 3070 | -$64.65 | -19% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 37813 | 37803 | 140 (0%) | 1.07% | -$2,653.55 (-58%) | Hold to the close: -$2,653.55 (-58%) |

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
| Volatility model | 23397 | 4.7% | 0.4% (93) | -677% | ❌ Worse |
| Momentum model | 23397 | 4.6% | 0.4% (93) | -700% | ❌ Worse |
| Mean-reversion model | 23397 | 8.1% | 0.4% (93) | -823% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 23397 | 93 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5683 | 50 | +1% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 3070 | 31 | +26% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1741 | 19 | +55% | -69% | -66% | -64% |
| Momentum model ≥ 2% | 4687 | 34 | -13% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 2846 | 25 | +12% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1862 | 17 | +27% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9557 | 64 | -27% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6708 | 54 | -11% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4479 | 39 | -1% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 23597 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9067 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5139 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 37803 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 140 | 0% | -$2,653.55 | -58% | — |
| Sell at 2¢ | 1435 | 4% | -$4,044.45 | -88% | 47 sec |
| Sell at 3¢ | 989 | 3% | -$4,031.84 | -87% | 48 sec |
| Sell at 5¢ | 687 | 2% | -$3,971.00 | -86% | 63 sec |
| Sell at 10¢ | 417 | 1% | -$3,815.28 | -83% | 65 sec |
| Sell at 25¢ | 222 | 1% | -$3,528.73 | -76% | 82 sec |
| Sell at 50¢ | 145 | 0% | -$3,200.80 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 8 | 0 | 38% | 25% | -100% | -35% | -3% |
| 5–10 min | 1716 | 8 | 11% | 4% | -56% | -80% | -81% |
| 2–5 min | 12058 | 67 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 9575 | 32 | 3% | 1% | -63% | -92% | -92% |
| Under 1 min | 14446 | 33 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2641 | 12 | 5% | 2% | -42% | -88% | -88% |
| HYPE | 2635 | 8 | 5% | 3% | -62% | -89% | -87% |
| BNB | 2635 | 15 | 5% | 2% | -29% | -85% | -84% |
| SOL | 2627 | 7 | 4% | 2% | -66% | -92% | -91% |
| DOGE | 2623 | 6 | 4% | 2% | -71% | -90% | -90% |
| ETH | 2622 | 11 | 6% | 3% | -49% | -85% | -85% |
| XRP | 2607 | 11 | 3% | 1% | -48% | -89% | -89% |
| BTC | 2604 | 13 | 5% | 2% | -33% | -88% | -89% |
| NEAR | 2603 | 12 | 5% | 2% | -40% | -82% | -82% |
| GOLD | 1426 | 5 | 4% | 2% | -58% | -82% | -83% |
| SILVER | 1399 | 6 | 4% | 2% | -49% | -82% | -81% |
| WTI | 1380 | 4 | 3% | 1% | -65% | -93% | -94% |
| PLATINUM | 1237 | 1 | 2% | 1% | -92% | -97% | -96% |
| COPPER | 1175 | 4 | 1% | 1% | -68% | -74% | -74% |
| EURUSD | 1171 | 3 | 2% | 1% | -76% | -88% | -88% |
| NATGAS | 1138 | 7 | 2% | 1% | -43% | -80% | -79% |
| GBPUSD | 1110 | 2 | 2% | 1% | -83% | -96% | -96% |
| PALLADIUM | 1104 | 2 | 1% | 0% | -83% | -90% | -90% |
| USDJPY | 1087 | 5 | 2% | 1% | -57% | -97% | -96% |
| AUDUSD | 642 | 4 | 1% | 1% | -42% | -83% | -82% |
| USDCAD | 607 | 0 | 2% | 0% | -100% | -97% | -97% |
| BRENT | 208 | 0 | 0% | 0% | -100% | -99% | -99% |
| 10YRRATE | 139 | 0 | 4% | 1% | -100% | -93% | -91% |
| 30YRRATE | 134 | 0 | 1% | 0% | -100% | -99% | -98% |
| 2YRRATE | 129 | 1 | 4% | 1% | -28% | -21% | -20% |
| 5YRRATE | 120 | 1 | 6% | 2% | -22% | -90% | -91% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 19163 | 77 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 18640 | 63 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3860 | 19 | 2% | 1% | -15% | -81% | -81% |
| 0.05–0.1% | 4064 | 14 | 3% | 2% | -48% | -92% | -92% |
| 0.1–0.2% | 6143 | 22 | 4% | 2% | -55% | -90% | -89% |
| 0.2–0.5% | 6958 | 30 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2568 | 10 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9458 | 35 | 4% | 2% | -58% | -86% | -86% |
| Morning (6am–12pm) | 9331 | 42 | 4% | 2% | -49% | -86% | -85% |
| Afternoon (12–6pm) | 8852 | 29 | 4% | 2% | -62% | -88% | -88% |
| Evening (6pm–12am) | 10162 | 34 | 3% | 2% | -62% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,521 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/29 7:59:57 AM | HYPE | DOWN | 3 sec | -0.068% | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:59:57 AM | 2YRRATE | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:59:41 AM | AUDUSD | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:59:25 AM | PALLADIUM | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:59:25 AM | 10YRRATE | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:59:25 AM | GOLD | DOWN | 35 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/29 7:59:10 AM | SILVER | DOWN | 49 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 7:58:54 AM | GBPUSD | DOWN | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:58:54 AM | 30YRRATE | DOWN | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:58:22 AM | ZEC | DOWN | 1.6 min | +0.434% | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:58:22 AM | NEAR | DOWN | 1.6 min | +0.356% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 7:58:06 AM | XRP | DOWN | 1.9 min | +0.288% | 0¢ | ❌ Lost | $0.00 |
| 10/29 7:57:47 AM | SOL | DOWN | 2.2 min | +0.243% | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:57:47 AM | DOGE | DOWN | 2.2 min | +0.276% | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:57:31 AM | BRENT | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:57:31 AM | WTI | DOWN | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 7:57:15 AM | EURUSD | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:57:15 AM | USDCAD | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:57:00 AM | BNB | DOWN | 3.0 min | +0.205% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 7:57:00 AM | ETH | DOWN | 3.0 min | +0.290% | 1¢ | ❌ Lost | $0.00 |
| 10/29 7:56:12 AM | BTC | DOWN | 3.8 min | +0.315% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 7:44:54 AM | EURUSD | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:44:38 AM | SILVER | UP | 22 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/29 7:44:23 AM | USDCAD | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:44:23 AM | HYPE | UP | 36 sec | -0.389% | 0¢ | ❌ Lost | $0.00 |
| 10/29 7:44:05 AM | AUDUSD | UP | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:44:05 AM | BNB | UP | 55 sec | -0.181% | 0¢ | ❌ Lost | $0.00 |
| 10/29 7:44:05 AM | BRENT | UP | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:43:18 AM | WTI | UP | 1.7 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/29 7:43:18 AM | COPPER | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
