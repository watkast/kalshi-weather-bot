# 15-Minute 1¢ Study

*Updated Sun Nov 15, 11:52 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4415 finished bets | 1% | $224.85 | +46% | +5.09¢ | $86.40 / $138.45 |

*Expect about **90 buys a day** (~$13.51/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4164 | $123.40 | +27% |
| Volatility model ≥ 2%, hold to the close | 8214 | $89.35 | +9% |
| Momentum model ≥ 2%, hold to the close | 6828 | $13.95 | +2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 58280 | 58259 | 226 (0%) | 1.07% | -$3,918.40 (-55%) | Hold to the close: -$3,918.40 (-55%) |

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
| Volatility model | 35175 | 4.6% | 0.4% (147) | -634% | ❌ Worse |
| Momentum model | 35175 | 4.5% | 0.4% (147) | -659% | ❌ Worse |
| Mean-reversion model | 35175 | 7.9% | 0.4% (147) | -770% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 35175 | 147 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8214 | 77 | +9% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4415 | 51 | +46% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2537 | 30 | +71% | -63% | -61% | -57% |
| Momentum model ≥ 2% | 6828 | 57 | +2% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4164 | 41 | +27% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2711 | 26 | +36% | -66% | -66% | -61% |
| Mean-reversion model ≥ 2% | 14402 | 102 | -22% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10021 | 85 | -6% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6645 | 61 | +4% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 35381 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 13778 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9100 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 58259 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 226 | 0% | -$3,918.40 | -55% | — |
| Sell at 2¢ | 2345 | 4% | -$6,178.70 | -87% | 47 sec |
| Sell at 3¢ | 1584 | 3% | -$6,170.64 | -87% | 48 sec |
| Sell at 5¢ | 1085 | 2% | -$6,055.15 | -85% | 62 sec |
| Sell at 10¢ | 663 | 1% | -$5,807.87 | -82% | 65 sec |
| Sell at 25¢ | 349 | 1% | -$5,395.21 | -76% | 80 sec |
| Sell at 50¢ | 233 | 0% | -$4,851.65 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2911 | 13 | 11% | 4% | -58% | -81% | -82% |
| 2–5 min | 18822 | 103 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 14699 | 51 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 21814 | 59 | 1% | 0% | -61% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3960 | 19 | 5% | 2% | -37% | -88% | -87% |
| SOL | 3954 | 17 | 4% | 2% | -45% | -86% | -86% |
| HYPE | 3949 | 12 | 4% | 2% | -61% | -89% | -88% |
| DOGE | 3939 | 11 | 4% | 2% | -65% | -90% | -89% |
| BNB | 3936 | 20 | 5% | 2% | -36% | -85% | -85% |
| ETH | 3928 | 17 | 6% | 3% | -46% | -82% | -82% |
| BTC | 3910 | 21 | 5% | 2% | -27% | -86% | -88% |
| NEAR | 3909 | 17 | 5% | 2% | -43% | -85% | -86% |
| XRP | 3896 | 15 | 3% | 2% | -51% | -89% | -88% |
| GOLD | 2062 | 5 | 5% | 2% | -70% | -82% | -84% |
| WTI | 2049 | 7 | 4% | 2% | -59% | -91% | -92% |
| SILVER | 2007 | 9 | 5% | 2% | -47% | -83% | -83% |
| PLATINUM | 1826 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1774 | 6 | 2% | 1% | -68% | -90% | -90% |
| COPPER | 1713 | 6 | 2% | 1% | -67% | -75% | -75% |
| GBPUSD | 1699 | 6 | 2% | 1% | -67% | -96% | -96% |
| NATGAS | 1686 | 9 | 2% | 1% | -50% | -74% | -74% |
| USDJPY | 1665 | 6 | 2% | 1% | -66% | -97% | -96% |
| PALLADIUM | 1641 | 4 | 1% | 0% | -77% | -92% | -93% |
| AUDUSD | 1219 | 6 | 2% | 1% | -54% | -89% | -89% |
| USDCAD | 1173 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 794 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 401 | 2 | 4% | 1% | -53% | -70% | -68% |
| 2YRRATE | 384 | 4 | 4% | 2% | -3% | -45% | -43% |
| 30YRRATE | 376 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 355 | 2 | 4% | 2% | -47% | -93% | -95% |
| INX | 54 | 0 | 2% | 0% | -100% | -97% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 29667 | 113 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 28592 | 113 | 4% | 2% | -55% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5386 | 25 | 2% | 1% | -17% | -78% | -77% |
| 0.05–0.1% | 5831 | 24 | 3% | 2% | -36% | -91% | -91% |
| 0.1–0.2% | 8896 | 34 | 5% | 2% | -51% | -89% | -89% |
| 0.2–0.5% | 10879 | 47 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4380 | 19 | 7% | 3% | -55% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14049 | 44 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13903 | 70 | 4% | 2% | -43% | -85% | -84% |
| Afternoon (12–6pm) | 14272 | 63 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 16035 | 49 | 4% | 2% | -65% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,100 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/15 11:44:45 PM | ETH | DOWN | 15 sec | +0.047% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 11:44:29 PM | NEAR | DOWN | 31 sec | +0.057% | 0¢ | ❌ Lost | -$0.15 |
| 11/15 11:44:29 PM | HYPE | DOWN | 31 sec | +0.087% | 0¢ | ❌ Lost | -$0.15 |
| 11/15 11:44:13 PM | NATGAS | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 11:44:13 PM | BNB | DOWN | 47 sec | +0.003% | 0¢ | ❌ Lost | $0.00 |
| 11/15 11:44:13 PM | XRP | UP | 47 sec | -0.116% | 0¢ | ❌ Lost | $0.00 |
| 11/15 11:43:41 PM | PLATINUM | UP | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 11:43:25 PM | WTI | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 11:43:09 PM | BTC | DOWN | 1.8 min | +0.171% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 11:43:09 PM | PALLADIUM | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 11:42:53 PM | USDJPY | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 11:42:38 PM | SILVER | UP | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/15 11:42:22 PM | EURUSD | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 11:42:06 PM | DOGE | DOWN | 2.9 min | +0.289% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 11:42:06 PM | SOL | DOWN | 2.9 min | +0.323% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 11:42:06 PM | GBPUSD | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 11:41:32 PM | AUDUSD | DOWN | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 11:41:00 PM | ZEC | DOWN | 4.0 min | +0.752% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 11:40:44 PM | BRENT | DOWN | 4.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/15 11:40:12 PM | GOLD | UP | 4.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/15 11:29:52 PM | NEAR | UP | 7 sec | -0.121% | 0¢ | ❌ Lost | $0.00 |
| 11/15 11:29:37 PM | NATGAS | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 11:29:05 PM | DOGE | DOWN | 55 sec | +0.123% | 0¢ | ❌ Lost | -$0.15 |
| 11/15 11:29:05 PM | BNB | DOWN | 55 sec | +0.075% | 0¢ | ❌ Lost | $0.00 |
| 11/15 11:29:05 PM | XRP | DOWN | 55 sec | +0.169% | 0¢ | ❌ Lost | $0.00 |
| 11/15 11:29:05 PM | AUDUSD | DOWN | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 11:28:48 PM | ETH | DOWN | 71 sec | +0.180% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 11:28:17 PM | USDJPY | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 11:28:17 PM | BTC | DOWN | 1.7 min | +0.217% | 0¢ | ❌ Lost | $0.00 |
| 11/15 11:28:17 PM | GBPUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
