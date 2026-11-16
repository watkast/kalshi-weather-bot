# 15-Minute 1¢ Study

*Updated Mon Nov 16, 1:05 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4417 finished bets | 1% | $224.70 | +46% | +5.09¢ | $86.25 / $138.45 |

*Expect about **90 buys a day** (~$13.51/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4165 | $123.40 | +27% |
| Volatility model ≥ 2%, hold to the close | 8222 | $88.30 | +9% |
| Momentum model ≥ 2%, hold to the close | 6832 | $13.50 | +2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 58378 | 58357 | 227 (0%) | 1.07% | -$3,917.15 (-55%) | Hold to the close: -$3,917.15 (-55%) |

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
| Volatility model | 35221 | 4.6% | 0.4% (148) | -631% | ❌ Worse |
| Momentum model | 35221 | 4.5% | 0.4% (148) | -656% | ❌ Worse |
| Mean-reversion model | 35221 | 7.9% | 0.4% (148) | -766% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 35221 | 148 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8222 | 77 | +9% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4417 | 51 | +46% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2538 | 30 | +71% | -63% | -61% | -57% |
| Momentum model ≥ 2% | 6832 | 57 | +2% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4165 | 41 | +27% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2712 | 26 | +36% | -66% | -66% | -61% |
| Mean-reversion model ≥ 2% | 14423 | 103 | -22% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10034 | 85 | -6% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6654 | 61 | +4% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 35427 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 13810 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9120 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 58357 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 227 | 0% | -$3,917.15 | -55% | — |
| Sell at 2¢ | 2348 | 4% | -$6,190.67 | -87% | 47 sec |
| Sell at 3¢ | 1587 | 3% | -$6,182.22 | -87% | 48 sec |
| Sell at 5¢ | 1088 | 2% | -$6,065.95 | -85% | 62 sec |
| Sell at 10¢ | 665 | 1% | -$5,818.00 | -82% | 65 sec |
| Sell at 25¢ | 351 | 1% | -$5,401.34 | -76% | 80 sec |
| Sell at 50¢ | 234 | 0% | -$4,857.65 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2917 | 13 | 11% | 4% | -58% | -81% | -82% |
| 2–5 min | 18861 | 104 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 14721 | 51 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 21845 | 59 | 1% | 0% | -61% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3965 | 19 | 5% | 2% | -37% | -88% | -87% |
| SOL | 3960 | 18 | 4% | 2% | -42% | -86% | -86% |
| HYPE | 3954 | 12 | 5% | 2% | -62% | -89% | -88% |
| DOGE | 3944 | 11 | 4% | 2% | -65% | -90% | -89% |
| BNB | 3941 | 20 | 5% | 2% | -36% | -85% | -85% |
| ETH | 3933 | 17 | 6% | 3% | -46% | -82% | -82% |
| BTC | 3915 | 21 | 5% | 2% | -27% | -86% | -88% |
| NEAR | 3914 | 17 | 5% | 2% | -43% | -85% | -86% |
| XRP | 3901 | 15 | 3% | 2% | -52% | -89% | -88% |
| GOLD | 2067 | 5 | 5% | 2% | -70% | -83% | -84% |
| WTI | 2053 | 7 | 4% | 2% | -59% | -91% | -92% |
| SILVER | 2012 | 9 | 5% | 2% | -47% | -83% | -83% |
| PLATINUM | 1831 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1778 | 6 | 2% | 1% | -69% | -90% | -90% |
| COPPER | 1715 | 6 | 2% | 1% | -67% | -75% | -75% |
| GBPUSD | 1703 | 6 | 2% | 1% | -67% | -96% | -96% |
| NATGAS | 1689 | 9 | 2% | 1% | -50% | -74% | -74% |
| USDJPY | 1669 | 6 | 2% | 1% | -66% | -97% | -96% |
| PALLADIUM | 1645 | 4 | 1% | 0% | -77% | -92% | -93% |
| AUDUSD | 1223 | 6 | 2% | 1% | -54% | -89% | -89% |
| USDCAD | 1176 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 798 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 401 | 2 | 4% | 1% | -53% | -70% | -68% |
| 2YRRATE | 385 | 4 | 4% | 2% | -3% | -45% | -43% |
| 30YRRATE | 376 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 355 | 2 | 4% | 2% | -47% | -93% | -95% |
| INX | 54 | 0 | 2% | 0% | -100% | -97% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 29709 | 113 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 28648 | 114 | 4% | 2% | -54% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5387 | 25 | 2% | 1% | -17% | -78% | -77% |
| 0.05–0.1% | 5833 | 24 | 3% | 2% | -36% | -91% | -91% |
| 0.1–0.2% | 8904 | 34 | 5% | 2% | -51% | -89% | -89% |
| 0.2–0.5% | 10908 | 48 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 4386 | 19 | 7% | 3% | -55% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14125 | 45 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13903 | 70 | 4% | 2% | -43% | -85% | -84% |
| Afternoon (12–6pm) | 14272 | 63 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 16057 | 49 | 4% | 2% | -65% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,099 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/16 12:59:50 AM | GOLD | DOWN | 9 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/16 12:59:50 AM | 2YRRATE | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:59:50 AM | BNB | UP | 9 sec | -0.061% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:59:34 AM | GBPUSD | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:59:18 AM | SILVER | UP | 41 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/16 12:59:02 AM | EURUSD | UP | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:58:31 AM | NEAR | DOWN | 89 sec | +0.216% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 12:58:15 AM | ETH | DOWN | 1.8 min | +0.172% | 0¢ | ❌ Lost | $0.00 |
| 11/16 12:57:59 AM | USDJPY | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:57:27 AM | ZEC | DOWN | 2.5 min | +0.459% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 12:57:27 AM | PALLADIUM | UP | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/16 12:57:27 AM | BTC | DOWN | 2.5 min | +0.168% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 12:57:27 AM | HYPE | DOWN | 2.5 min | +0.351% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:57:27 AM | XRP | DOWN | 2.5 min | +0.303% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:56:55 AM | SOL | DOWN | 3.1 min | +0.340% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 12:56:55 AM | DOGE | DOWN | 3.1 min | +0.241% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 12:56:24 AM | PLATINUM | UP | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:44:56 AM | PLATINUM | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:44:56 AM | SILVER | UP | 3 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/16 12:44:56 AM | USDCAD | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:44:56 AM | NATGAS | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:44:37 AM | SOL | UP | 23 sec | -0.156% | 0¢ | ❌ Lost | $0.00 |
| 11/16 12:44:37 AM | DOGE | UP | 23 sec | -0.058% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:44:37 AM | BNB | UP | 23 sec | -0.132% | 0¢ | ❌ Lost | $0.00 |
| 11/16 12:44:37 AM | NEAR | DOWN | 23 sec | -0.025% | 0¢ | ❌ Lost | $0.00 |
| 11/16 12:44:00 AM | ETH | DOWN | 60 sec | +0.136% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 12:43:44 AM | GOLD | UP | 75 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/16 12:43:28 AM | BRENT | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:42:40 AM | AUDUSD | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:42:40 AM | WTI | UP | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
