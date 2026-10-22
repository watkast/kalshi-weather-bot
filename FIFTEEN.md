# 15-Minute 1¢ Study

*Updated Thu Oct 22, 4:31 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2351 finished bets | 1% | $71.10 | +27% | +3.02¢ | $40.65 / $30.45 |

*Expect about **97 buys a day** (~$14.60/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2174 | $53.10 | +22% |
| Volatility model ≥ 2%, hold to the close | 4318 | -$9.85 | -2% |
| Momentum model ≥ 2%, hold to the close | 3624 | -$34.60 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 27899 | 27891 | 106 (0%) | 1.07% | -$1,914.55 (-56%) | Hold to the close: -$1,914.55 (-56%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 17936 | 4.7% | 0.4% (76) | -656% | ❌ Worse |
| Momentum model | 17936 | 4.6% | 0.4% (76) | -680% | ❌ Worse |
| Mean-reversion model | 17936 | 7.9% | 0.4% (76) | -787% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17936 | 76 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4318 | 37 | -2% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 2351 | 24 | +27% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 1345 | 16 | +68% | -62% | -61% | -58% |
| Momentum model ≥ 2% | 3624 | 28 | -8% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2174 | 21 | +22% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 1429 | 14 | +34% | -68% | -68% | -63% |
| Mean-reversion model ≥ 2% | 7153 | 50 | -24% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4998 | 41 | -9% | -80% | -79% | -76% |
| Mean-reversion model ≥ 10% | 3331 | 28 | -4% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 18135 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 6686 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 3070 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 27891 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 106 | 0% | -$1,914.55 | -56% | — |
| Sell at 2¢ | 1021 | 4% | -$2,993.09 | -88% | 46 sec |
| Sell at 3¢ | 697 | 2% | -$2,986.72 | -88% | 48 sec |
| Sell at 5¢ | 493 | 2% | -$2,938.10 | -86% | 61 sec |
| Sell at 10¢ | 304 | 1% | -$2,832.31 | -83% | 64 sec |
| Sell at 25¢ | 168 | 1% | -$2,604.47 | -77% | 82 sec |
| Sell at 50¢ | 110 | 0% | -$2,348.05 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1151 | 6 | 11% | 4% | -50% | -81% | -84% |
| 2–5 min | 8980 | 50 | 7% | 3% | -45% | -87% | -87% |
| 1–2 min | 7094 | 27 | 3% | 1% | -59% | -93% | -93% |
| Under 1 min | 10662 | 23 | 1% | 0% | -69% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2032 | 11 | 5% | 2% | -32% | -89% | -89% |
| BNB | 2028 | 12 | 5% | 3% | -27% | -83% | -82% |
| HYPE | 2025 | 7 | 5% | 3% | -57% | -89% | -87% |
| ETH | 2015 | 10 | 6% | 3% | -40% | -86% | -86% |
| SOL | 2014 | 3 | 3% | 2% | -82% | -92% | -92% |
| DOGE | 2012 | 4 | 4% | 2% | -75% | -90% | -90% |
| XRP | 2006 | 7 | 3% | 1% | -57% | -88% | -88% |
| NEAR | 2002 | 12 | 6% | 3% | -23% | -80% | -80% |
| BTC | 2001 | 12 | 5% | 2% | -20% | -88% | -90% |
| GOLD | 1094 | 3 | 4% | 1% | -68% | -81% | -83% |
| SILVER | 1057 | 4 | 3% | 1% | -56% | -82% | -82% |
| WTI | 1032 | 3 | 3% | 1% | -66% | -94% | -95% |
| PLATINUM | 920 | 0 | 1% | 0% | -100% | -99% | -99% |
| COPPER | 904 | 3 | 1% | 1% | -69% | -77% | -76% |
| NATGAS | 848 | 5 | 2% | 1% | -45% | -86% | -85% |
| EURUSD | 844 | 3 | 2% | 1% | -67% | -85% | -85% |
| PALLADIUM | 825 | 2 | 1% | 0% | -77% | -87% | -87% |
| GBPUSD | 792 | 1 | 2% | 1% | -88% | -96% | -96% |
| USDJPY | 761 | 4 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 350 | 0 | 0% | 0% | -100% | -100% | -99% |
| USDCAD | 307 | 0 | 1% | 0% | -100% | -99% | -99% |
| 10YRRATE | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 5 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 4 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 14062 | 56 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 13829 | 50 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3024 | 15 | 2% | 1% | -17% | -78% | -78% |
| 0.05–0.1% | 3132 | 11 | 3% | 2% | -49% | -92% | -91% |
| 0.1–0.2% | 4630 | 17 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 5295 | 27 | 6% | 3% | -44% | -87% | -87% |
| Over 0.5% | 2050 | 8 | 7% | 3% | -60% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7014 | 30 | 4% | 2% | -51% | -85% | -85% |
| Morning (6am–12pm) | 6595 | 31 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6540 | 20 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 7742 | 25 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,720 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/22 4:29:53 AM | USDJPY | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 4:29:53 AM | NATGAS | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 4:29:37 AM | NEAR | DOWN | 22 sec | -0.048% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 4:29:37 AM | BTC | UP | 22 sec | -0.035% | 0¢ | ❌ Lost | $0.00 |
| 10/22 4:29:21 AM | BNB | DOWN | 38 sec | +0.004% | 0¢ | ❌ Lost | $0.00 |
| 10/22 4:29:21 AM | DOGE | DOWN | 38 sec | +0.062% | 0¢ | ❌ Lost | $0.00 |
| 10/22 4:28:50 AM | GBPUSD | UP | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 4:28:02 AM | USDCAD | DOWN | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 4:28:02 AM | GOLD | DOWN | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 4:27:46 AM | ETH | DOWN | 2.2 min | +0.091% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 4:27:30 AM | SOL | DOWN | 2.5 min | +0.139% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 4:26:43 AM | HYPE | DOWN | 3.3 min | +0.231% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 4:26:43 AM | ZEC | DOWN | 3.3 min | +0.515% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 4:26:43 AM | XRP | DOWN | 3.3 min | +0.143% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 4:25:55 AM | WTI | UP | 4.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 4:24:36 AM | PALLADIUM | DOWN | 5.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 4:24:20 AM | SILVER | DOWN | 5.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 4:14:55 AM | BNB | DOWN | 4 sec | -0.025% | 0¢ | ❌ Lost | $0.00 |
| 10/22 4:14:55 AM | EURUSD | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 4:14:55 AM | SILVER | UP | 4 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/22 4:14:55 AM | ZEC | DOWN | 4 sec | -0.009% | 0¢ | ❌ Lost | $0.00 |
| 10/22 4:14:38 AM | WTI | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 4:14:06 AM | ETH | DOWN | 54 sec | +0.066% | 0¢ | ❌ Lost | $0.00 |
| 10/22 4:13:51 AM | HYPE | DOWN | 68 sec | +0.120% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 4:13:51 AM | DOGE | DOWN | 68 sec | +0.080% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 4:13:18 AM | USDCAD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 4:13:02 AM | USDJPY | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 4:13:02 AM | NEAR | DOWN | 2.0 min | +0.411% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 4:13:02 AM | PLATINUM | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 4:12:47 AM | BTC | DOWN | 2.2 min | +0.114% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
