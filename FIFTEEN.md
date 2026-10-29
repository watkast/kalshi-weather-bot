# 15-Minute 1¢ Study

*Updated Wed Oct 28, 8:43 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3047 finished bets | 1% | $91.70 | +27% | +3.01¢ | $83.40 / $8.30 |

*Expect about **99 buys a day** (~$14.82/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2828 | $40.10 | +13% |
| Volatility model ≥ 2%, hold to the close | 5633 | $14.80 | +2% |
| Volatility model ≥ 5%, sell at 50¢ | 3047 | -$62.55 | -18% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 37336 | 37323 | 140 (0%) | 1.07% | -$2,596.70 (-57%) | Hold to the close: -$2,596.70 (-57%) |

*In play or awaiting result: 12. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 23177 | 4.7% | 0.4% (93) | -675% | ❌ Worse |
| Momentum model | 23177 | 4.6% | 0.4% (93) | -699% | ❌ Worse |
| Mean-reversion model | 23177 | 8.1% | 0.4% (93) | -820% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 23177 | 93 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5633 | 50 | +2% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 3047 | 31 | +27% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1728 | 19 | +56% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4661 | 34 | -12% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2828 | 25 | +13% | -78% | -77% | -74% |
| Momentum model ≥ 10% | 1851 | 17 | +27% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9463 | 64 | -26% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6640 | 54 | -10% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4433 | 39 | -0% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 23377 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8927 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5019 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 37323 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 140 | 0% | -$2,596.70 | -57% | — |
| Sell at 2¢ | 1421 | 4% | -$3,991.24 | -88% | 47 sec |
| Sell at 3¢ | 977 | 3% | -$3,979.67 | -87% | 48 sec |
| Sell at 5¢ | 678 | 2% | -$3,920.00 | -86% | 62 sec |
| Sell at 10¢ | 412 | 1% | -$3,764.98 | -83% | 64 sec |
| Sell at 25¢ | 220 | 1% | -$3,478.50 | -76% | 82 sec |
| Sell at 50¢ | 145 | 0% | -$3,143.95 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1683 | 8 | 11% | 4% | -55% | -80% | -82% |
| 2–5 min | 11924 | 67 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 9439 | 32 | 3% | 1% | -63% | -92% | -92% |
| Under 1 min | 14273 | 33 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2617 | 12 | 5% | 2% | -41% | -88% | -88% |
| HYPE | 2611 | 8 | 5% | 3% | -62% | -89% | -87% |
| BNB | 2610 | 15 | 5% | 2% | -28% | -85% | -83% |
| SOL | 2603 | 7 | 4% | 2% | -66% | -92% | -92% |
| ETH | 2598 | 11 | 6% | 3% | -49% | -85% | -85% |
| DOGE | 2597 | 6 | 4% | 2% | -71% | -90% | -90% |
| XRP | 2582 | 11 | 3% | 1% | -48% | -89% | -89% |
| NEAR | 2580 | 12 | 5% | 2% | -40% | -82% | -82% |
| BTC | 2579 | 13 | 5% | 2% | -33% | -88% | -89% |
| GOLD | 1407 | 5 | 4% | 2% | -57% | -82% | -83% |
| SILVER | 1378 | 6 | 4% | 2% | -49% | -82% | -82% |
| WTI | 1360 | 4 | 3% | 1% | -65% | -93% | -94% |
| PLATINUM | 1222 | 1 | 2% | 1% | -92% | -97% | -96% |
| COPPER | 1158 | 4 | 1% | 1% | -68% | -74% | -73% |
| EURUSD | 1147 | 3 | 2% | 1% | -76% | -88% | -88% |
| NATGAS | 1125 | 7 | 2% | 1% | -42% | -80% | -79% |
| GBPUSD | 1090 | 2 | 2% | 1% | -83% | -96% | -96% |
| PALLADIUM | 1085 | 2 | 1% | 0% | -83% | -89% | -90% |
| USDJPY | 1070 | 5 | 2% | 1% | -56% | -97% | -96% |
| AUDUSD | 623 | 4 | 1% | 1% | -40% | -83% | -82% |
| USDCAD | 590 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 192 | 0 | 1% | 1% | -100% | -99% | -99% |
| 10YRRATE | 133 | 0 | 5% | 1% | -100% | -92% | -90% |
| 30YRRATE | 125 | 0 | 1% | 0% | -100% | -99% | -98% |
| 2YRRATE | 124 | 1 | 4% | 1% | -25% | -18% | -16% |
| 5YRRATE | 117 | 1 | 6% | 3% | -20% | -90% | -91% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 18915 | 77 | 4% | 2% | -53% | -87% | -87% |
| DOWN (bought NO) | 18408 | 63 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3841 | 19 | 2% | 1% | -15% | -81% | -80% |
| 0.05–0.1% | 4029 | 14 | 3% | 2% | -48% | -92% | -92% |
| 0.1–0.2% | 6075 | 22 | 4% | 2% | -55% | -90% | -89% |
| 0.2–0.5% | 6883 | 30 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2545 | 10 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9229 | 35 | 4% | 2% | -57% | -86% | -86% |
| Morning (6am–12pm) | 9232 | 42 | 4% | 2% | -48% | -86% | -85% |
| Afternoon (12–6pm) | 8852 | 29 | 4% | 2% | -62% | -88% | -88% |
| Evening (6pm–12am) | 10010 | 34 | 3% | 2% | -61% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,554 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/28 8:42:28 PM | HYPE | UP | 2.5 min | -0.354% | — | In play | — |
| 10/28 8:42:28 PM | XRP | UP | 2.5 min | -0.348% | — | In play | — |
| 10/28 8:42:28 PM | BNB | UP | 2.5 min | -0.255% | — | In play | — |
| 10/28 8:41:40 PM | BTC | UP | 3.3 min | -0.235% | — | In play | — |
| 10/28 8:40:20 PM | WTI | DOWN | 4.7 min | — | — | In play | — |
| 10/28 8:29:49 PM | SOL | DOWN | 10 sec | +0.029% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 8:29:49 PM | BTC | UP | 10 sec | -0.018% | 0¢ | ❌ Lost | $0.00 |
| 10/28 8:29:49 PM | USDJPY | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 8:29:49 PM | NATGAS | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 8:29:49 PM | HYPE | UP | 10 sec | -0.059% | 0¢ | ❌ Lost | $0.00 |
| 10/28 8:29:33 PM | ETH | UP | 26 sec | -0.070% | 0¢ | ❌ Lost | $0.00 |
| 10/28 8:29:33 PM | DOGE | UP | 26 sec | -0.060% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 8:29:33 PM | GBPUSD | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 8:29:17 PM | BNB | UP | 42 sec | -0.083% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 8:29:17 PM | WTI | UP | 42 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 8:29:01 PM | NEAR | UP | 59 sec | -0.298% | 0¢ | ❌ Lost | $0.00 |
| 10/28 8:29:01 PM | SILVER | UP | 59 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 8:28:45 PM | GOLD | UP | 75 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 8:28:29 PM | PALLADIUM | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 8:28:29 PM | XRP | UP | 1.5 min | -0.355% | 0¢ | ❌ Lost | $0.00 |
| 10/28 8:28:13 PM | ZEC | UP | 1.8 min | -0.511% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 8:26:19 PM | DOGE | DOWN | 3.7 min | +0.364% | 99¢ | ✅ Won | $13.85 |
| 10/28 8:14:50 PM | BRENT | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 8:14:50 PM | PALLADIUM | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 8:14:50 PM | PLATINUM | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 8:14:18 PM | XRP | UP | 42 sec | -0.162% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 8:14:18 PM | WTI | UP | 42 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/28 8:14:03 PM | NATGAS | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 8:14:03 PM | BNB | DOWN | 56 sec | +0.158% | 0¢ | ❌ Lost | $0.00 |
| 10/28 8:13:45 PM | NEAR | UP | 74 sec | -0.545% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
