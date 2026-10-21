# 15-Minute 1¢ Study

*Updated Wed Oct 21, 4:23 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2222 finished bets | 1% | $85.05 | +34% | +3.83¢ | $47.40 / $37.65 |

*Expect about **96 buys a day** (~$14.39/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2058 | $65.70 | +29% |
| Volatility model ≥ 2%, hold to the close | 4075 | -$23.20 | -5% |
| Momentum model ≥ 2%, hold to the close | 3439 | -$27.30 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 26434 | 26427 | 97 (0%) | 1.07% | -$1,861.75 (-58%) | Hold to the close: -$1,861.75 (-58%) |

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
| Volatility model | 17152 | 4.6% | 0.4% (69) | -665% | ❌ Worse |
| Momentum model | 17152 | 4.5% | 0.4% (69) | -687% | ❌ Worse |
| Mean-reversion model | 17152 | 7.8% | 0.4% (69) | -803% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17152 | 69 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4075 | 34 | -5% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 2222 | 24 | +34% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 1276 | 16 | +75% | -61% | -59% | -56% |
| Momentum model ≥ 2% | 3439 | 27 | -7% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2058 | 21 | +29% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 1353 | 14 | +41% | -68% | -67% | -62% |
| Mean-reversion model ≥ 2% | 6764 | 45 | -28% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4717 | 37 | -14% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3128 | 25 | -9% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 17350 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6292 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2785 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 26427 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 97 | 0% | -$1,861.75 | -58% | — |
| Sell at 2¢ | 958 | 4% | -$2,830.67 | -88% | 46 sec |
| Sell at 3¢ | 652 | 2% | -$2,825.47 | -88% | 48 sec |
| Sell at 5¢ | 461 | 2% | -$2,780.10 | -86% | 56 sec |
| Sell at 10¢ | 280 | 1% | -$2,684.95 | -83% | 64 sec |
| Sell at 25¢ | 152 | 1% | -$2,492.63 | -77% | 80 sec |
| Sell at 50¢ | 99 | 0% | -$2,257.50 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1062 | 6 | 10% | 4% | -46% | -81% | -84% |
| 2–5 min | 8523 | 43 | 7% | 3% | -50% | -87% | -87% |
| 1–2 min | 6751 | 25 | 3% | 1% | -60% | -93% | -92% |
| Under 1 min | 10087 | 23 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1947 | 11 | 5% | 2% | -30% | -90% | -90% |
| BNB | 1939 | 10 | 5% | 2% | -37% | -83% | -82% |
| HYPE | 1937 | 6 | 5% | 3% | -62% | -89% | -87% |
| ETH | 1929 | 10 | 6% | 3% | -38% | -87% | -86% |
| DOGE | 1927 | 3 | 4% | 2% | -81% | -91% | -90% |
| SOL | 1926 | 2 | 3% | 1% | -87% | -92% | -92% |
| XRP | 1919 | 7 | 3% | 1% | -55% | -88% | -88% |
| NEAR | 1913 | 11 | 6% | 3% | -26% | -79% | -79% |
| BTC | 1913 | 11 | 5% | 2% | -23% | -88% | -90% |
| GOLD | 1030 | 2 | 3% | 1% | -77% | -81% | -83% |
| SILVER | 992 | 4 | 3% | 1% | -53% | -82% | -82% |
| WTI | 971 | 3 | 3% | 1% | -64% | -94% | -95% |
| PLATINUM | 863 | 0 | 1% | 0% | -100% | -99% | -98% |
| COPPER | 861 | 3 | 2% | 1% | -67% | -76% | -75% |
| NATGAS | 794 | 5 | 2% | 1% | -41% | -85% | -84% |
| EURUSD | 789 | 3 | 2% | 1% | -65% | -84% | -84% |
| PALLADIUM | 781 | 2 | 1% | 0% | -76% | -86% | -86% |
| GBPUSD | 739 | 1 | 2% | 1% | -87% | -97% | -96% |
| USDJPY | 699 | 3 | 1% | 1% | -60% | -99% | -98% |
| AUDUSD | 304 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 254 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 13296 | 49 | 4% | 2% | -58% | -88% | -87% |
| DOWN (bought NO) | 13131 | 48 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2908 | 15 | 2% | 1% | -14% | -78% | -77% |
| 0.05–0.1% | 3017 | 11 | 3% | 2% | -47% | -92% | -91% |
| 0.1–0.2% | 4414 | 14 | 5% | 2% | -61% | -89% | -89% |
| 0.2–0.5% | 5055 | 25 | 6% | 3% | -46% | -88% | -87% |
| Over 0.5% | 1953 | 6 | 7% | 3% | -68% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6725 | 28 | 4% | 2% | -53% | -85% | -85% |
| Morning (6am–12pm) | 6213 | 29 | 4% | 2% | -47% | -88% | -87% |
| Afternoon (12–6pm) | 6157 | 19 | 3% | 1% | -64% | -88% | -89% |
| Evening (6pm–12am) | 7332 | 21 | 3% | 2% | -67% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,750 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/21 4:14:42 AM | EURUSD | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:14:10 AM | COPPER | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:14:10 AM | HYPE | UP | 50 sec | -0.211% | 0¢ | ❌ Lost | $0.00 |
| 10/21 4:13:55 AM | PLATINUM | UP | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:13:55 AM | BTC | UP | 64 sec | -0.127% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:13:35 AM | GOLD | UP | 85 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 4:13:35 AM | XRP | UP | 85 sec | -0.199% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 4:12:46 AM | ETH | UP | 2.2 min | -0.141% | 1¢ | ❌ Lost | $0.00 |
| 10/21 4:12:46 AM | DOGE | UP | 2.2 min | -0.165% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 4:12:30 AM | NATGAS | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:12:14 AM | USDCAD | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:11:58 AM | WTI | DOWN | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 4:11:28 AM | SOL | UP | 3.5 min | -0.282% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 4:10:39 AM | USDJPY | UP | 4.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:10:23 AM | BNB | UP | 4.6 min | -0.197% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 4:09:35 AM | NEAR | UP | 5.4 min | -0.840% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 4:09:03 AM | ZEC | UP | 6.0 min | -0.689% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 3:59:44 AM | BTC | UP | 15 sec | -0.046% | 0¢ | ❌ Lost | $0.00 |
| 10/21 3:59:44 AM | NEAR | UP | 15 sec | -0.252% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 3:59:44 AM | USDJPY | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 3:59:28 AM | AUDUSD | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 3:58:37 AM | EURUSD | UP | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 3:58:21 AM | HYPE | UP | 1.6 min | -0.238% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 3:58:21 AM | BNB | UP | 1.6 min | -0.102% | 0¢ | ❌ Lost | $0.00 |
| 10/21 3:58:21 AM | GOLD | UP | 1.6 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/21 3:58:21 AM | XRP | UP | 1.6 min | -0.228% | 0¢ | ❌ Lost | $0.00 |
| 10/21 3:58:21 AM | SOL | UP | 1.6 min | -0.137% | 0¢ | ❌ Lost | $0.00 |
| 10/21 3:58:06 AM | PLATINUM | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 3:58:06 AM | ETH | UP | 1.9 min | -0.144% | 0¢ | ❌ Lost | $0.00 |
| 10/21 3:58:06 AM | ZEC | UP | 1.9 min | -0.300% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
