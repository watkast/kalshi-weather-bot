# 15-Minute 1¢ Study

*Updated Tue Oct 20, 12:05 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2160 finished bets | 1% | $78.25 | +32% | +3.62¢ | $21.80 / $56.45 |

*Expect about **96 buys a day** (~$14.42/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1991 | $59.65 | +27% |
| Momentum model ≥ 2%, hold to the close | 3321 | -$27.20 | -7% |
| Volatility model ≥ 5%, sell at 50¢ | 2160 | -$38.75 | -16% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 25439 | 25432 | 92 (0%) | 1.07% | -$1,808.00 (-58%) | Hold to the close: -$1,808.00 (-58%) |

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
| Volatility model | 16580 | 4.6% | 0.4% (65) | -673% | ❌ Worse |
| Momentum model | 16580 | 4.5% | 0.4% (65) | -696% | ❌ Worse |
| Mean-reversion model | 16580 | 7.8% | 0.4% (65) | -813% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16580 | 65 | -51% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3927 | 31 | -10% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2160 | 23 | +32% | -71% | -70% | -67% |
| Volatility model ≥ 10% | 1241 | 15 | +69% | -60% | -58% | -55% |
| Momentum model ≥ 2% | 3321 | 26 | -7% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 1991 | 20 | +27% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 1312 | 13 | +35% | -67% | -66% | -61% |
| Mean-reversion model ≥ 2% | 6515 | 42 | -30% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4534 | 34 | -17% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3001 | 22 | -17% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16778 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6013 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2641 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 25432 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 92 | 0% | -$1,808.00 | -58% | — |
| Sell at 2¢ | 920 | 4% | -$2,730.80 | -88% | 46 sec |
| Sell at 3¢ | 625 | 2% | -$2,726.25 | -88% | 47 sec |
| Sell at 5¢ | 444 | 2% | -$2,681.40 | -87% | 51 sec |
| Sell at 10¢ | 271 | 1% | -$2,586.99 | -84% | 64 sec |
| Sell at 25¢ | 147 | 1% | -$2,399.43 | -78% | 80 sec |
| Sell at 50¢ | 95 | 0% | -$2,174.75 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1010 | 5 | 11% | 4% | -53% | -81% | -83% |
| 2–5 min | 8230 | 41 | 7% | 3% | -51% | -88% | -87% |
| 1–2 min | 6494 | 24 | 3% | 2% | -60% | -93% | -92% |
| Under 1 min | 9694 | 22 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1887 | 11 | 4% | 2% | -27% | -90% | -90% |
| HYPE | 1875 | 6 | 5% | 3% | -61% | -89% | -87% |
| BNB | 1874 | 9 | 5% | 2% | -41% | -83% | -82% |
| ETH | 1864 | 9 | 6% | 3% | -42% | -87% | -86% |
| DOGE | 1863 | 3 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1862 | 2 | 3% | 2% | -87% | -92% | -92% |
| XRP | 1855 | 7 | 3% | 1% | -54% | -87% | -88% |
| NEAR | 1850 | 10 | 6% | 3% | -30% | -79% | -79% |
| BTC | 1848 | 10 | 5% | 2% | -28% | -88% | -90% |
| GOLD | 986 | 1 | 3% | 1% | -88% | -92% | -95% |
| SILVER | 950 | 4 | 3% | 1% | -51% | -81% | -81% |
| WTI | 926 | 3 | 3% | 1% | -62% | -94% | -95% |
| COPPER | 827 | 3 | 2% | 1% | -66% | -75% | -74% |
| PLATINUM | 820 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 757 | 5 | 2% | 1% | -38% | -84% | -83% |
| EURUSD | 756 | 3 | 2% | 1% | -63% | -84% | -84% |
| PALLADIUM | 747 | 2 | 1% | 0% | -75% | -86% | -86% |
| GBPUSD | 713 | 1 | 2% | 1% | -87% | -97% | -97% |
| USDJPY | 664 | 3 | 1% | 1% | -58% | -99% | -98% |
| AUDUSD | 279 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 229 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12798 | 45 | 4% | 2% | -60% | -88% | -87% |
| DOWN (bought NO) | 12634 | 47 | 3% | 1% | -57% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2815 | 15 | 2% | 1% | -11% | -77% | -76% |
| 0.05–0.1% | 2910 | 10 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 4243 | 13 | 5% | 2% | -62% | -90% | -89% |
| 0.2–0.5% | 4902 | 23 | 6% | 3% | -49% | -88% | -87% |
| Over 0.5% | 1905 | 6 | 7% | 3% | -68% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6450 | 26 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6213 | 29 | 4% | 2% | -47% | -88% | -87% |
| Afternoon (12–6pm) | 5807 | 19 | 3% | 1% | -61% | -89% | -89% |
| Evening (6pm–12am) | 6962 | 18 | 3% | 2% | -70% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,762 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/20 11:59:47 AM | ETH | DOWN | 13 sec | +0.012% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:59:47 AM | XRP | DOWN | 13 sec | +0.023% | 0¢ | ❌ Lost | $0.00 |
| 10/20 11:59:47 AM | GOLD | DOWN | 13 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 11:59:15 AM | SOL | DOWN | 45 sec | +0.101% | 0¢ | ❌ Lost | $0.00 |
| 10/20 11:59:15 AM | WTI | UP | 45 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 11:59:00 AM | BNB | DOWN | 59 sec | +0.050% | 0¢ | ❌ Lost | $0.00 |
| 10/20 11:59:00 AM | EURUSD | UP | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:56:38 AM | COPPER | DOWN | 3.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 11:54:08 AM | ZEC | DOWN | 5.9 min | +0.572% | 19¢ | ❌ Lost | -$0.15 |
| 10/20 11:44:56 AM | USDCAD | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:44:56 AM | EURUSD | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:44:56 AM | GBPUSD | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:44:23 AM | USDJPY | UP | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:44:23 AM | AUDUSD | DOWN | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:44:07 AM | ZEC | UP | 53 sec | -0.326% | 0¢ | ❌ Lost | $0.00 |
| 10/20 11:43:52 AM | PALLADIUM | DOWN | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:43:52 AM | ETH | DOWN | 67 sec | +0.081% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:43:52 AM | NEAR | DOWN | 67 sec | +0.259% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:43:21 AM | HYPE | DOWN | 1.6 min | +0.212% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:43:21 AM | COPPER | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:43:05 AM | BTC | DOWN | 1.9 min | +0.108% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 11:43:05 AM | XRP | DOWN | 1.9 min | +0.136% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 11:43:05 AM | DOGE | DOWN | 1.9 min | +0.148% | 0¢ | ❌ Lost | $0.00 |
| 10/20 11:42:49 AM | BNB | DOWN | 2.2 min | +0.115% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 11:42:01 AM | SOL | DOWN | 3.0 min | +0.230% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 11:29:38 AM | DOGE | UP | 22 sec | -0.091% | 0¢ | ❌ Lost | $0.00 |
| 10/20 11:29:38 AM | USDJPY | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:29:38 AM | BTC | UP | 22 sec | -0.062% | 0¢ | ❌ Lost | $0.00 |
| 10/20 11:29:38 AM | PALLADIUM | DOWN | 22 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 11:29:38 AM | XRP | UP | 22 sec | -0.136% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
