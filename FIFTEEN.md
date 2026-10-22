# 15-Minute 1¢ Study

*Updated Thu Oct 22, 7:35 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2360 finished bets | 1% | $69.90 | +26% | +2.96¢ | $39.90 / $30.00 |

*Expect about **97 buys a day** (~$14.58/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2181 | $52.35 | +22% |
| Volatility model ≥ 2%, hold to the close | 4336 | -$12.25 | -2% |
| Momentum model ≥ 2%, hold to the close | 3636 | -$35.95 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 28116 | 28108 | 106 (0%) | 1.07% | -$1,940.95 (-57%) | Hold to the close: -$1,940.95 (-57%) |

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
| Volatility model | 18042 | 4.7% | 0.4% (76) | -657% | ❌ Worse |
| Momentum model | 18042 | 4.6% | 0.4% (76) | -681% | ❌ Worse |
| Mean-reversion model | 18042 | 7.9% | 0.4% (76) | -788% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 18042 | 76 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4336 | 37 | -2% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 2360 | 24 | +26% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 1351 | 16 | +67% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 3636 | 28 | -8% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2181 | 21 | +22% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 1432 | 14 | +34% | -69% | -68% | -63% |
| Mean-reversion model ≥ 2% | 7191 | 50 | -24% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 5021 | 41 | -10% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3344 | 28 | -5% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 18241 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 6749 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 3118 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 28108 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 106 | 0% | -$1,940.95 | -57% | — |
| Sell at 2¢ | 1025 | 4% | -$3,018.45 | -88% | 46 sec |
| Sell at 3¢ | 700 | 2% | -$3,011.95 | -88% | 48 sec |
| Sell at 5¢ | 494 | 2% | -$2,963.85 | -87% | 61 sec |
| Sell at 10¢ | 304 | 1% | -$2,858.71 | -83% | 64 sec |
| Sell at 25¢ | 168 | 1% | -$2,630.87 | -77% | 82 sec |
| Sell at 50¢ | 110 | 0% | -$2,374.45 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1164 | 6 | 11% | 4% | -51% | -81% | -84% |
| 2–5 min | 9041 | 50 | 7% | 3% | -45% | -87% | -87% |
| 1–2 min | 7155 | 27 | 3% | 1% | -59% | -93% | -93% |
| Under 1 min | 10744 | 23 | 1% | 0% | -69% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2044 | 11 | 5% | 2% | -33% | -89% | -89% |
| BNB | 2040 | 12 | 5% | 2% | -28% | -83% | -82% |
| HYPE | 2036 | 7 | 5% | 3% | -58% | -89% | -87% |
| ETH | 2027 | 10 | 6% | 3% | -41% | -86% | -86% |
| SOL | 2026 | 3 | 3% | 2% | -82% | -92% | -92% |
| DOGE | 2024 | 4 | 4% | 2% | -76% | -90% | -89% |
| XRP | 2017 | 7 | 3% | 1% | -57% | -88% | -88% |
| NEAR | 2014 | 12 | 6% | 3% | -23% | -80% | -80% |
| BTC | 2013 | 12 | 5% | 2% | -20% | -88% | -90% |
| GOLD | 1105 | 3 | 4% | 1% | -68% | -82% | -84% |
| SILVER | 1066 | 4 | 3% | 1% | -57% | -82% | -82% |
| WTI | 1040 | 3 | 3% | 1% | -66% | -94% | -95% |
| PLATINUM | 927 | 0 | 1% | 0% | -100% | -99% | -99% |
| COPPER | 916 | 3 | 1% | 1% | -69% | -77% | -77% |
| NATGAS | 855 | 5 | 2% | 1% | -45% | -86% | -85% |
| EURUSD | 853 | 3 | 2% | 1% | -67% | -85% | -85% |
| PALLADIUM | 832 | 2 | 1% | 0% | -78% | -87% | -87% |
| GBPUSD | 801 | 1 | 2% | 1% | -88% | -97% | -96% |
| USDJPY | 771 | 4 | 1% | 1% | -52% | -99% | -98% |
| AUDUSD | 358 | 0 | 0% | 0% | -100% | -100% | -99% |
| USDCAD | 313 | 0 | 1% | 0% | -100% | -99% | -99% |
| 10YRRATE | 9 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 8 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 14185 | 56 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 13923 | 50 | 3% | 1% | -59% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3038 | 15 | 2% | 1% | -17% | -78% | -78% |
| 0.05–0.1% | 3152 | 11 | 3% | 2% | -49% | -92% | -91% |
| 0.1–0.2% | 4663 | 17 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 5329 | 27 | 6% | 3% | -44% | -87% | -87% |
| Over 0.5% | 2055 | 8 | 7% | 3% | -60% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7128 | 30 | 4% | 2% | -52% | -86% | -85% |
| Morning (6am–12pm) | 6698 | 31 | 4% | 2% | -47% | -88% | -87% |
| Afternoon (12–6pm) | 6540 | 20 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 7742 | 25 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,691 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/22 7:29:16 AM | USDCAD | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 7:29:14 AM | EURUSD | UP | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 7:28:55 AM | AUDUSD | DOWN | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 7:28:18 AM | COPPER | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 7:28:06 AM | PLATINUM | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 7:27:21 AM | USDJPY | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 7:26:57 AM | ZEC | DOWN | 3.0 min | +0.418% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 7:26:41 AM | XRP | DOWN | 3.3 min | +0.280% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 7:26:29 AM | DOGE | DOWN | 3.5 min | +0.198% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 7:26:29 AM | SOL | DOWN | 3.5 min | +0.312% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 7:25:41 AM | BNB | DOWN | 4.3 min | +0.159% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 7:25:08 AM | ETH | DOWN | 4.9 min | +0.269% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 7:25:08 AM | HYPE | DOWN | 4.9 min | +0.276% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 7:24:37 AM | NEAR | DOWN | 5.4 min | +0.724% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 7:24:06 AM | BTC | DOWN | 5.9 min | +0.267% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 7:14:57 AM | BRENT | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 7:14:57 AM | USDJPY | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 7:14:57 AM | WTI | DOWN | 2 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/22 7:14:57 AM | GBPUSD | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 7:14:09 AM | BTC | UP | 50 sec | -0.106% | 0¢ | ❌ Lost | $0.00 |
| 10/22 7:13:54 AM | NATGAS | DOWN | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 7:13:38 AM | PLATINUM | UP | 82 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 7:13:38 AM | ETH | UP | 82 sec | -0.135% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 7:13:22 AM | AUDUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 7:13:22 AM | BNB | UP | 1.6 min | -0.150% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 7:13:22 AM | SOL | UP | 1.6 min | -0.135% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 7:13:22 AM | SILVER | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 7:13:06 AM | USDCAD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 7:13:06 AM | GOLD | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 7:12:34 AM | DOGE | UP | 2.4 min | -0.242% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
