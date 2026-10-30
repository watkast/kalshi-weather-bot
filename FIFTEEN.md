# 15-Minute 1¢ Study

*Updated Thu Oct 29, 7:38 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3123 finished bets | 1% | $83.75 | +24% | +2.68¢ | $79.05 / $4.70 |

*Expect about **98 buys a day** (~$14.74/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2888 | $33.65 | +11% |
| Volatility model ≥ 2%, hold to the close | 5773 | -$1.25 | -0% |
| Volatility model ≥ 5%, sell at 50¢ | 3123 | -$70.50 | -20% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 38574 | 38562 | 143 (0%) | 1.07% | -$2,706.95 (-57%) | Hold to the close: -$2,706.95 (-57%) |

*In play or awaiting result: 11. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 23745 | 4.6% | 0.4% (93) | -677% | ❌ Worse |
| Momentum model | 23745 | 4.5% | 0.4% (93) | -700% | ❌ Worse |
| Mean-reversion model | 23745 | 8.0% | 0.4% (93) | -825% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 23745 | 93 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5773 | 50 | -0% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3123 | 31 | +24% | -75% | -74% | -70% |
| Volatility model ≥ 10% | 1763 | 19 | +53% | -68% | -67% | -64% |
| Momentum model ≥ 2% | 4769 | 34 | -14% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2888 | 25 | +11% | -78% | -77% | -73% |
| Momentum model ≥ 10% | 1884 | 17 | +25% | -72% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9721 | 64 | -28% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 6814 | 54 | -12% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4545 | 39 | -3% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 23946 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9273 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5343 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 38562 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 143 | 0% | -$2,706.95 | -57% | — |
| Sell at 2¢ | 1484 | 4% | -$4,127.11 | -88% | 47 sec |
| Sell at 3¢ | 1023 | 3% | -$4,113.98 | -87% | 49 sec |
| Sell at 5¢ | 713 | 2% | -$4,035.50 | -86% | 63 sec |
| Sell at 10¢ | 431 | 1% | -$3,864.34 | -82% | 65 sec |
| Sell at 25¢ | 226 | 1% | -$3,568.89 | -76% | 83 sec |
| Sell at 50¢ | 146 | 0% | -$3,247.45 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 9 | 0 | 33% | 22% | -100% | -42% | -13% |
| 5–10 min | 1791 | 8 | 11% | 4% | -57% | -80% | -81% |
| 2–5 min | 12277 | 68 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 9754 | 34 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 14731 | 33 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2679 | 12 | 5% | 3% | -43% | -88% | -88% |
| HYPE | 2676 | 8 | 5% | 3% | -63% | -89% | -87% |
| BNB | 2673 | 15 | 5% | 2% | -30% | -85% | -84% |
| SOL | 2667 | 7 | 4% | 2% | -67% | -91% | -91% |
| ETH | 2660 | 11 | 6% | 3% | -50% | -86% | -85% |
| DOGE | 2660 | 6 | 4% | 2% | -72% | -90% | -89% |
| BTC | 2644 | 13 | 5% | 2% | -34% | -88% | -89% |
| XRP | 2644 | 11 | 3% | 1% | -49% | -89% | -89% |
| NEAR | 2643 | 12 | 5% | 2% | -41% | -82% | -82% |
| GOLD | 1456 | 5 | 4% | 2% | -59% | -82% | -83% |
| SILVER | 1424 | 7 | 4% | 2% | -42% | -82% | -81% |
| WTI | 1410 | 4 | 3% | 1% | -66% | -93% | -94% |
| PLATINUM | 1259 | 2 | 2% | 1% | -85% | -97% | -96% |
| COPPER | 1201 | 5 | 1% | 1% | -61% | -74% | -74% |
| EURUSD | 1199 | 3 | 2% | 1% | -77% | -88% | -88% |
| NATGAS | 1163 | 7 | 2% | 1% | -44% | -80% | -79% |
| GBPUSD | 1135 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1127 | 2 | 1% | 0% | -83% | -90% | -90% |
| USDJPY | 1116 | 5 | 2% | 1% | -58% | -97% | -96% |
| AUDUSD | 671 | 4 | 2% | 1% | -44% | -83% | -82% |
| USDCAD | 630 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 233 | 0 | 0% | 0% | -100% | -99% | -99% |
| 10YRRATE | 158 | 0 | 4% | 1% | -100% | -92% | -90% |
| 30YRRATE | 152 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 146 | 1 | 5% | 1% | -36% | -28% | -27% |
| 5YRRATE | 136 | 1 | 7% | 3% | -31% | -89% | -90% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 19588 | 78 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 18974 | 65 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3879 | 19 | 2% | 1% | -15% | -81% | -81% |
| 0.05–0.1% | 4092 | 14 | 3% | 2% | -49% | -92% | -92% |
| 0.1–0.2% | 6189 | 22 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 7078 | 30 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2704 | 10 | 7% | 3% | -62% | -86% | -86% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9458 | 35 | 4% | 2% | -58% | -86% | -86% |
| Morning (6am–12pm) | 9668 | 43 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 9178 | 31 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 10258 | 34 | 3% | 2% | -62% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,494 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/29 7:37:52 PM | WTI | DOWN | 7.1 min | — | — | In play | — |
| 10/29 7:37:37 PM | BRENT | DOWN | 7.4 min | — | — | In play | — |
| 10/29 7:29:42 PM | NATGAS | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:29:26 PM | BRENT | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:29:11 PM | PALLADIUM | DOWN | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:28:39 PM | PLATINUM | DOWN | 80 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:28:39 PM | COPPER | DOWN | 80 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:28:39 PM | USDJPY | DOWN | 80 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:27:21 PM | ZEC | UP | 2.6 min | -0.970% | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:27:21 PM | NEAR | UP | 2.6 min | -1.066% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 7:27:21 PM | GOLD | DOWN | 2.6 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/29 7:27:07 PM | AUDUSD | DOWN | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:26:33 PM | SILVER | DOWN | 3.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 7:25:12 PM | BTC | UP | 4.8 min | -0.574% | 2¢ | ❌ Lost | -$0.15 |
| 10/29 7:24:57 PM | SOL | UP | 5.0 min | -1.089% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 7:24:57 PM | DOGE | UP | 5.0 min | -1.075% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 7:24:57 PM | ETH | UP | 5.0 min | -0.936% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 7:24:57 PM | XRP | UP | 5.0 min | -1.016% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 7:24:57 PM | HYPE | UP | 5.0 min | -1.429% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 7:24:38 PM | BNB | UP | 5.4 min | -0.878% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 7:07:07 PM | PALLADIUM | UP | 7.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 7:05:48 PM | PLATINUM | UP | 9.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 6:59:57 PM | NATGAS | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 6:59:25 PM | AUDUSD | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 6:58:36 PM | PALLADIUM | UP | 84 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 6:58:20 PM | EURUSD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 6:58:20 PM | BTC | DOWN | 1.7 min | +0.204% | 1¢ | ❌ Lost | $0.00 |
| 10/29 6:58:04 PM | ZEC | DOWN | 1.9 min | +0.726% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 6:58:04 PM | GBPUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 6:58:04 PM | ETH | DOWN | 1.9 min | +0.316% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
