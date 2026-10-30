# 15-Minute 1¢ Study

*Updated Fri Oct 30, 5:05 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3199 finished bets | 1% | $90.70 | +25% | +2.84¢ | $74.25 / $16.45 |

*Expect about **98 buys a day** (~$14.68/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2967 | $40.30 | +12% |
| Volatility model ≥ 2%, hold to the close | 5937 | $8.60 | +1% |
| Momentum model ≥ 2%, hold to the close | 4899 | -$63.00 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 40050 | 40040 | 148 (0%) | 1.07% | -$2,818.30 (-58%) | Hold to the close: -$2,818.30 (-58%) |

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
| Volatility model | 24453 | 4.6% | 0.4% (95) | -682% | ❌ Worse |
| Momentum model | 24453 | 4.5% | 0.4% (95) | -704% | ❌ Worse |
| Mean-reversion model | 24453 | 8.0% | 0.4% (95) | -831% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 24453 | 95 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5937 | 52 | +1% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3199 | 32 | +25% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1805 | 19 | +51% | -69% | -67% | -64% |
| Momentum model ≥ 2% | 4899 | 36 | -11% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2967 | 26 | +12% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1931 | 17 | +23% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 10042 | 66 | -28% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7025 | 56 | -12% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4684 | 39 | -5% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 24654 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9699 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5687 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 40040 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 148 | 0% | -$2,818.30 | -58% | — |
| Sell at 2¢ | 1544 | 4% | -$4,264.86 | -87% | 47 sec |
| Sell at 3¢ | 1063 | 3% | -$4,251.73 | -87% | 49 sec |
| Sell at 5¢ | 741 | 2% | -$4,170.65 | -85% | 63 sec |
| Sell at 10¢ | 445 | 1% | -$3,999.35 | -82% | 65 sec |
| Sell at 25¢ | 232 | 1% | -$3,702.38 | -76% | 83 sec |
| Sell at 50¢ | 151 | 0% | -$3,367.05 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1865 | 8 | 11% | 4% | -59% | -80% | -81% |
| 2–5 min | 12763 | 70 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10140 | 35 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 15261 | 35 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2759 | 13 | 5% | 3% | -40% | -88% | -88% |
| HYPE | 2752 | 8 | 5% | 3% | -64% | -89% | -87% |
| BNB | 2751 | 16 | 5% | 3% | -27% | -85% | -83% |
| SOL | 2747 | 7 | 4% | 2% | -68% | -91% | -91% |
| DOGE | 2740 | 6 | 4% | 2% | -72% | -90% | -89% |
| ETH | 2738 | 11 | 6% | 3% | -51% | -85% | -85% |
| BTC | 2723 | 13 | 5% | 2% | -36% | -88% | -89% |
| NEAR | 2722 | 12 | 5% | 2% | -43% | -83% | -83% |
| XRP | 2722 | 11 | 3% | 1% | -50% | -89% | -89% |
| GOLD | 1515 | 5 | 5% | 2% | -60% | -82% | -83% |
| SILVER | 1481 | 7 | 4% | 2% | -44% | -82% | -81% |
| WTI | 1467 | 4 | 3% | 1% | -67% | -93% | -93% |
| PLATINUM | 1314 | 3 | 2% | 1% | -79% | -96% | -96% |
| COPPER | 1253 | 5 | 1% | 1% | -63% | -75% | -75% |
| EURUSD | 1249 | 3 | 2% | 1% | -78% | -89% | -88% |
| NATGAS | 1210 | 7 | 2% | 1% | -46% | -81% | -80% |
| GBPUSD | 1185 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1178 | 2 | 1% | 0% | -84% | -90% | -91% |
| USDJPY | 1171 | 5 | 2% | 1% | -60% | -97% | -96% |
| AUDUSD | 705 | 4 | 2% | 1% | -47% | -84% | -83% |
| USDCAD | 685 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 281 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 188 | 1 | 5% | 2% | -50% | -41% | -39% |
| 30YRRATE | 177 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 170 | 2 | 5% | 1% | +10% | +18% | +19% |
| 5YRRATE | 157 | 1 | 6% | 3% | -41% | -89% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 20343 | 81 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 19697 | 67 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3929 | 19 | 2% | 1% | -16% | -81% | -81% |
| 0.05–0.1% | 4181 | 14 | 3% | 2% | -49% | -92% | -91% |
| 0.1–0.2% | 6327 | 22 | 4% | 2% | -57% | -90% | -89% |
| 0.2–0.5% | 7369 | 32 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2844 | 10 | 7% | 3% | -64% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9916 | 36 | 4% | 2% | -59% | -86% | -86% |
| Morning (6am–12pm) | 10122 | 46 | 4% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 9422 | 32 | 4% | 2% | -60% | -87% | -87% |
| Evening (6pm–12am) | 10580 | 34 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,456 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/30 4:59:45 PM | SOL | DOWN | 14 sec | +0.014% | 0¢ | ❌ Lost | $0.00 |
| 10/30 4:59:29 PM | BRENT | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 4:59:14 PM | DOGE | UP | 45 sec | -0.024% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 4:59:14 PM | ZEC | UP | 45 sec | -0.165% | 0¢ | ❌ Lost | $0.00 |
| 10/30 4:59:14 PM | NEAR | UP | 45 sec | -0.230% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 4:58:40 PM | BTC | UP | 80 sec | -0.063% | 77¢ | ❌ Lost | -$0.15 |
| 10/30 4:58:40 PM | ETH | UP | 80 sec | -0.093% | 5¢ | ❌ Lost | $0.00 |
| 10/30 4:58:40 PM | WTI | DOWN | 80 sec | — | 1¢ | ❌ Lost | $0.00 |
| 10/30 4:58:09 PM | HYPE | UP | 1.9 min | -0.236% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 4:57:54 PM | XRP | UP | 2.1 min | -0.136% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 4:44:46 PM | WTI | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 4:44:15 PM | NEAR | DOWN | 44 sec | +0.063% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 4:43:57 PM | ETH | DOWN | 63 sec | +0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/30 4:43:57 PM | BRENT | DOWN | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 4:43:41 PM | HYPE | UP | 79 sec | -0.260% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 4:43:25 PM | ZEC | DOWN | 1.6 min | +0.349% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 4:42:21 PM | BTC | DOWN | 2.6 min | +0.128% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 4:41:14 PM | XRP | DOWN | 3.8 min | +0.184% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 4:40:59 PM | BNB | DOWN | 4.0 min | +0.090% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 4:40:25 PM | SOL | DOWN | 4.6 min | +0.238% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 4:40:09 PM | DOGE | DOWN | 4.8 min | +0.224% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 4:29:44 PM | NEAR | DOWN | 15 sec | +0.014% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 4:29:29 PM | BNB | UP | 30 sec | -0.097% | 0¢ | ❌ Lost | $0.00 |
| 10/30 4:29:11 PM | BTC | UP | 49 sec | -0.067% | 0¢ | ❌ Lost | $0.00 |
| 10/30 4:29:11 PM | XRP | UP | 49 sec | -0.072% | 0¢ | ❌ Lost | $0.00 |
| 10/30 4:29:11 PM | WTI | UP | 49 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/30 4:29:11 PM | BRENT | UP | 49 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/30 4:28:55 PM | DOGE | UP | 65 sec | -0.118% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 4:28:55 PM | SOL | DOWN | 65 sec | +0.059% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 4:28:39 PM | HYPE | DOWN | 81 sec | +0.158% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
