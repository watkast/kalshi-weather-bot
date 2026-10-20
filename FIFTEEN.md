# 15-Minute 1¢ Study

*Updated Tue Oct 20, 4:05 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2168 finished bets | 1% | $77.20 | +32% | +3.56¢ | $21.50 / $55.70 |

*Expect about **96 buys a day** (~$14.36/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2004 | $58.15 | +26% |
| Momentum model ≥ 2%, hold to the close | 3347 | -$30.05 | -8% |
| Volatility model ≥ 5%, sell at 50¢ | 2168 | -$39.80 | -16% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 25674 | 25667 | 92 (0%) | 1.07% | -$1,838.00 (-59%) | Hold to the close: -$1,838.00 (-59%) |

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
| Volatility model | 16722 | 4.6% | 0.4% (65) | -675% | ❌ Worse |
| Momentum model | 16722 | 4.5% | 0.4% (65) | -697% | ❌ Worse |
| Mean-reversion model | 16722 | 7.8% | 0.4% (65) | -817% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16722 | 65 | -52% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3959 | 31 | -10% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 2168 | 23 | +32% | -71% | -70% | -67% |
| Volatility model ≥ 10% | 1245 | 15 | +68% | -60% | -58% | -56% |
| Momentum model ≥ 2% | 3347 | 26 | -8% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 2004 | 20 | +26% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 1319 | 13 | +35% | -67% | -66% | -62% |
| Mean-reversion model ≥ 2% | 6570 | 42 | -30% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4573 | 34 | -18% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3030 | 22 | -18% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16920 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6077 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2670 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 25667 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 92 | 0% | -$1,838.00 | -59% | — |
| Sell at 2¢ | 936 | 4% | -$2,756.64 | -88% | 46 sec |
| Sell at 3¢ | 637 | 2% | -$2,751.57 | -88% | 48 sec |
| Sell at 5¢ | 452 | 2% | -$2,706.20 | -87% | 53 sec |
| Sell at 10¢ | 275 | 1% | -$2,611.75 | -84% | 64 sec |
| Sell at 25¢ | 147 | 1% | -$2,429.43 | -78% | 80 sec |
| Sell at 50¢ | 95 | 0% | -$2,204.75 | -71% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1025 | 5 | 11% | 4% | -53% | -81% | -84% |
| 2–5 min | 8309 | 41 | 7% | 3% | -51% | -88% | -87% |
| 1–2 min | 6551 | 24 | 3% | 2% | -60% | -93% | -92% |
| Under 1 min | 9778 | 22 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1902 | 11 | 4% | 2% | -28% | -90% | -90% |
| HYPE | 1891 | 6 | 5% | 3% | -61% | -89% | -87% |
| BNB | 1890 | 9 | 5% | 2% | -42% | -83% | -82% |
| ETH | 1879 | 9 | 6% | 3% | -43% | -87% | -86% |
| DOGE | 1879 | 3 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1878 | 2 | 3% | 1% | -87% | -92% | -92% |
| XRP | 1871 | 7 | 3% | 1% | -54% | -87% | -88% |
| NEAR | 1866 | 10 | 6% | 3% | -31% | -79% | -79% |
| BTC | 1864 | 10 | 5% | 2% | -28% | -88% | -90% |
| GOLD | 997 | 1 | 4% | 1% | -88% | -92% | -94% |
| SILVER | 958 | 4 | 3% | 1% | -52% | -81% | -81% |
| WTI | 936 | 3 | 3% | 1% | -62% | -94% | -95% |
| COPPER | 834 | 3 | 2% | 1% | -66% | -75% | -75% |
| PLATINUM | 829 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 767 | 5 | 2% | 1% | -39% | -84% | -83% |
| EURUSD | 762 | 3 | 2% | 1% | -63% | -84% | -84% |
| PALLADIUM | 756 | 2 | 1% | 0% | -75% | -86% | -86% |
| GBPUSD | 720 | 1 | 2% | 1% | -87% | -97% | -96% |
| USDJPY | 670 | 3 | 1% | 1% | -58% | -99% | -98% |
| AUDUSD | 284 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 234 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12907 | 45 | 4% | 2% | -60% | -88% | -87% |
| DOWN (bought NO) | 12760 | 47 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2830 | 15 | 2% | 1% | -11% | -77% | -76% |
| 0.05–0.1% | 2928 | 10 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 4287 | 13 | 5% | 2% | -63% | -89% | -89% |
| 0.2–0.5% | 4951 | 23 | 6% | 3% | -49% | -88% | -87% |
| Over 0.5% | 1921 | 6 | 7% | 3% | -68% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6450 | 26 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6213 | 29 | 4% | 2% | -47% | -88% | -87% |
| Afternoon (12–6pm) | 6042 | 19 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 6962 | 18 | 3% | 2% | -70% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,780 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/20 3:59:41 PM | NATGAS | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:58:53 PM | WTI | DOWN | 67 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 3:58:37 PM | GBPUSD | UP | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:57:01 PM | XRP | DOWN | 3.0 min | +0.143% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 3:56:45 PM | SOL | DOWN | 3.2 min | +0.202% | 2¢ | ❌ Lost | -$0.15 |
| 10/20 3:56:29 PM | BNB | DOWN | 3.5 min | +0.122% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:56:13 PM | BTC | DOWN | 3.8 min | +0.147% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 3:55:57 PM | HYPE | UP | 4.0 min | -0.326% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 3:55:25 PM | DOGE | DOWN | 4.6 min | +0.314% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 3:55:25 PM | NEAR | DOWN | 4.6 min | +0.748% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 3:55:06 PM | ETH | DOWN | 4.9 min | +0.328% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 3:54:02 PM | ZEC | DOWN | 6.0 min | +1.177% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 3:44:19 PM | WTI | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:44:03 PM | BNB | UP | 56 sec | -0.046% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:44:03 PM | BTC | UP | 56 sec | -0.055% | 0¢ | ❌ Lost | $0.00 |
| 10/20 3:43:31 PM | SOL | UP | 89 sec | -0.122% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:42:14 PM | HYPE | UP | 2.8 min | -0.347% | 23¢ | ❌ Lost | -$0.15 |
| 10/20 3:42:06 PM | ETH | UP | 2.9 min | -0.126% | 8¢ | ❌ Lost | -$0.15 |
| 10/20 3:40:30 PM | ZEC | UP | 4.5 min | -0.577% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 3:40:14 PM | XRP | UP | 4.8 min | -0.218% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 3:40:14 PM | DOGE | UP | 4.8 min | -0.232% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 3:40:14 PM | NEAR | UP | 4.8 min | -0.604% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 3:29:31 PM | DOGE | UP | 29 sec | -0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/20 3:29:31 PM | AUDUSD | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:29:31 PM | BTC | DOWN | 29 sec | +0.021% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:29:15 PM | BNB | DOWN | 45 sec | +0.030% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:29:00 PM | NEAR | DOWN | 59 sec | +0.224% | 0¢ | ❌ Lost | $0.00 |
| 10/20 3:28:43 PM | NATGAS | UP | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:28:11 PM | SOL | UP | 1.8 min | -0.125% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 3:25:47 PM | XRP | UP | 4.2 min | -0.232% | 3¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
