# 15-Minute 1¢ Study

*Updated Tue Oct 20, 7:07 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2119 finished bets | 1% | $83.80 | +35% | +3.95¢ | $23.90 / $59.90 |

*Expect about **95 buys a day** (~$14.27/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1949 | $65.35 | +30% |
| Momentum model ≥ 2%, hold to the close | 3250 | -$17.75 | -5% |
| Volatility model ≥ 5%, sell at 50¢ | 2119 | -$33.20 | -14% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 25108 | 25101 | 92 (0%) | 1.07% | -$1,763.90 (-58%) | Hold to the close: -$1,763.90 (-58%) |

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
| Volatility model | 16411 | 4.6% | 0.4% (65) | -673% | ❌ Worse |
| Momentum model | 16411 | 4.5% | 0.4% (65) | -696% | ❌ Worse |
| Mean-reversion model | 16411 | 7.7% | 0.4% (65) | -811% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16411 | 65 | -51% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3839 | 31 | -7% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2119 | 23 | +35% | -71% | -70% | -67% |
| Volatility model ≥ 10% | 1231 | 15 | +71% | -60% | -59% | -56% |
| Momentum model ≥ 2% | 3250 | 26 | -5% | -78% | -78% | -75% |
| Momentum model ≥ 5% | 1949 | 20 | +30% | -74% | -74% | -69% |
| Momentum model ≥ 10% | 1291 | 13 | +38% | -67% | -66% | -61% |
| Mean-reversion model ≥ 2% | 6410 | 42 | -29% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 4459 | 34 | -16% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2947 | 22 | -15% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16609 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5912 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2580 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 25101 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 92 | 0% | -$1,763.90 | -58% | — |
| Sell at 2¢ | 904 | 4% | -$2,690.86 | -88% | 46 sec |
| Sell at 3¢ | 614 | 2% | -$2,686.44 | -88% | 48 sec |
| Sell at 5¢ | 436 | 2% | -$2,642.50 | -87% | 51 sec |
| Sell at 10¢ | 266 | 1% | -$2,549.44 | -84% | 64 sec |
| Sell at 25¢ | 146 | 1% | -$2,358.64 | -77% | 80 sec |
| Sell at 50¢ | 95 | 0% | -$2,130.65 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 983 | 5 | 10% | 3% | -51% | -82% | -84% |
| 2–5 min | 8133 | 41 | 7% | 3% | -50% | -88% | -87% |
| 1–2 min | 6413 | 24 | 3% | 2% | -59% | -93% | -92% |
| Under 1 min | 9568 | 22 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1867 | 11 | 4% | 2% | -27% | -90% | -90% |
| HYPE | 1856 | 6 | 5% | 2% | -60% | -89% | -88% |
| BNB | 1855 | 9 | 5% | 2% | -41% | -83% | -82% |
| ETH | 1846 | 9 | 6% | 3% | -41% | -87% | -86% |
| DOGE | 1845 | 3 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1842 | 2 | 3% | 2% | -87% | -92% | -92% |
| XRP | 1836 | 7 | 3% | 1% | -53% | -87% | -88% |
| NEAR | 1831 | 10 | 6% | 3% | -30% | -79% | -79% |
| BTC | 1831 | 10 | 5% | 2% | -27% | -88% | -90% |
| GOLD | 971 | 1 | 3% | 1% | -88% | -93% | -95% |
| SILVER | 935 | 4 | 3% | 1% | -50% | -81% | -81% |
| WTI | 913 | 3 | 3% | 1% | -61% | -94% | -95% |
| COPPER | 811 | 3 | 2% | 1% | -65% | -74% | -74% |
| PLATINUM | 805 | 0 | 0% | 0% | -100% | -99% | -99% |
| NATGAS | 745 | 5 | 2% | 1% | -37% | -84% | -83% |
| EURUSD | 741 | 3 | 2% | 1% | -62% | -83% | -83% |
| PALLADIUM | 732 | 2 | 1% | 0% | -74% | -85% | -85% |
| GBPUSD | 699 | 1 | 2% | 1% | -87% | -97% | -97% |
| USDJPY | 650 | 3 | 1% | 1% | -57% | -99% | -98% |
| AUDUSD | 270 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 220 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12671 | 45 | 4% | 2% | -59% | -88% | -87% |
| DOWN (bought NO) | 12430 | 47 | 3% | 1% | -56% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2804 | 15 | 2% | 1% | -11% | -77% | -76% |
| 0.05–0.1% | 2892 | 10 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 4202 | 13 | 5% | 2% | -62% | -90% | -89% |
| 0.2–0.5% | 4841 | 23 | 6% | 3% | -48% | -88% | -87% |
| Over 0.5% | 1867 | 6 | 6% | 3% | -67% | -88% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6450 | 26 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 5882 | 29 | 4% | 2% | -43% | -87% | -86% |
| Afternoon (12–6pm) | 5807 | 19 | 3% | 1% | -61% | -89% | -89% |
| Evening (6pm–12am) | 6962 | 18 | 3% | 2% | -70% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,790 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/20 6:59:53 AM | PLATINUM | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:59:37 AM | HYPE | UP | 23 sec | -0.053% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:59:21 AM | GBPUSD | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:59:05 AM | WTI | DOWN | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:59:05 AM | BTC | UP | 55 sec | -0.059% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:59:05 AM | NEAR | UP | 55 sec | -0.279% | 0¢ | ❌ Lost | $0.00 |
| 10/20 6:58:50 AM | BNB | UP | 70 sec | -0.101% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:58:50 AM | XRP | UP | 70 sec | -0.123% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:58:50 AM | SOL | UP | 70 sec | -0.131% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:58:34 AM | ETH | UP | 86 sec | -0.092% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:58:18 AM | ZEC | UP | 1.7 min | -0.277% | 2¢ | ❌ Lost | -$0.15 |
| 10/20 6:58:18 AM | USDCAD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:58:02 AM | DOGE | UP | 2.0 min | -0.202% | 0¢ | ❌ Lost | $0.00 |
| 10/20 6:57:30 AM | USDJPY | DOWN | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:57:30 AM | GOLD | UP | 2.5 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/20 6:44:58 AM | EURUSD | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:44:42 AM | USDCAD | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:44:27 AM | USDJPY | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:44:27 AM | ZEC | UP | 33 sec | -0.060% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:44:27 AM | XRP | DOWN | 33 sec | +0.046% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:44:27 AM | SOL | DOWN | 33 sec | +0.096% | 0¢ | ❌ Lost | $0.00 |
| 10/20 6:44:27 AM | PALLADIUM | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:44:12 AM | GOLD | DOWN | 47 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:43:40 AM | BTC | DOWN | 79 sec | +0.128% | 0¢ | ❌ Lost | $0.00 |
| 10/20 6:43:40 AM | COPPER | DOWN | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:43:24 AM | SILVER | DOWN | 1.6 min | — | 1¢ | ❌ Lost | $0.00 |
| 10/20 6:43:24 AM | HYPE | DOWN | 1.6 min | +0.191% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:43:24 AM | DOGE | DOWN | 1.6 min | +0.153% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:43:09 AM | WTI | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:42:53 AM | BNB | DOWN | 2.1 min | +0.086% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
