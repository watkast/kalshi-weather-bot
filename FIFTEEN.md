# 15-Minute 1¢ Study

*Updated Wed Oct 21, 2:51 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2215 finished bets | 1% | $85.80 | +34% | +3.87¢ | $47.70 / $38.10 |

*Expect about **96 buys a day** (~$14.39/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2055 | $66.00 | +29% |
| Volatility model ≥ 2%, hold to the close | 4057 | -$21.25 | -4% |
| Momentum model ≥ 2%, hold to the close | 3425 | -$25.95 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 26338 | 26331 | 97 (0%) | 1.07% | -$1,850.35 (-58%) | Hold to the close: -$1,850.35 (-58%) |

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
| Volatility model | 17098 | 4.6% | 0.4% (69) | -664% | ❌ Worse |
| Momentum model | 17098 | 4.6% | 0.4% (69) | -686% | ❌ Worse |
| Mean-reversion model | 17098 | 7.8% | 0.4% (69) | -801% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17098 | 69 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4057 | 34 | -4% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 2215 | 24 | +34% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 1275 | 16 | +75% | -61% | -59% | -56% |
| Momentum model ≥ 2% | 3425 | 27 | -6% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2055 | 21 | +29% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 1352 | 14 | +41% | -68% | -67% | -62% |
| Mean-reversion model ≥ 2% | 6736 | 45 | -27% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4695 | 37 | -13% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3114 | 25 | -9% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 17296 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6264 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2771 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 26331 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 97 | 0% | -$1,850.35 | -58% | — |
| Sell at 2¢ | 957 | 4% | -$2,819.53 | -88% | 46 sec |
| Sell at 3¢ | 651 | 2% | -$2,814.46 | -88% | 48 sec |
| Sell at 5¢ | 461 | 2% | -$2,768.70 | -86% | 56 sec |
| Sell at 10¢ | 280 | 1% | -$2,673.55 | -83% | 64 sec |
| Sell at 25¢ | 152 | 1% | -$2,481.23 | -77% | 80 sec |
| Sell at 50¢ | 99 | 0% | -$2,246.10 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1060 | 6 | 10% | 4% | -46% | -81% | -84% |
| 2–5 min | 8489 | 43 | 7% | 3% | -50% | -87% | -87% |
| 1–2 min | 6723 | 25 | 3% | 2% | -60% | -93% | -92% |
| Under 1 min | 10055 | 23 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1941 | 11 | 4% | 2% | -29% | -90% | -90% |
| BNB | 1933 | 10 | 5% | 2% | -37% | -83% | -82% |
| HYPE | 1931 | 6 | 5% | 3% | -62% | -89% | -87% |
| ETH | 1923 | 10 | 6% | 3% | -38% | -87% | -86% |
| DOGE | 1921 | 3 | 4% | 2% | -81% | -91% | -90% |
| SOL | 1920 | 2 | 3% | 1% | -87% | -92% | -92% |
| XRP | 1913 | 7 | 3% | 1% | -55% | -88% | -88% |
| NEAR | 1907 | 11 | 6% | 3% | -26% | -79% | -79% |
| BTC | 1907 | 11 | 5% | 2% | -22% | -88% | -90% |
| GOLD | 1026 | 2 | 4% | 1% | -77% | -81% | -83% |
| SILVER | 989 | 4 | 3% | 1% | -53% | -82% | -81% |
| WTI | 966 | 3 | 3% | 1% | -63% | -94% | -95% |
| PLATINUM | 859 | 0 | 1% | 0% | -100% | -99% | -98% |
| COPPER | 857 | 3 | 2% | 1% | -67% | -76% | -75% |
| NATGAS | 789 | 5 | 2% | 1% | -41% | -84% | -84% |
| EURUSD | 785 | 3 | 2% | 1% | -64% | -84% | -84% |
| PALLADIUM | 778 | 2 | 1% | 0% | -76% | -86% | -86% |
| GBPUSD | 736 | 1 | 2% | 1% | -87% | -97% | -96% |
| USDJPY | 695 | 3 | 1% | 1% | -60% | -99% | -98% |
| AUDUSD | 303 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 252 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 13236 | 49 | 4% | 2% | -58% | -87% | -87% |
| DOWN (bought NO) | 13095 | 48 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2902 | 15 | 2% | 1% | -14% | -78% | -77% |
| 0.05–0.1% | 3012 | 11 | 3% | 2% | -47% | -92% | -91% |
| 0.1–0.2% | 4392 | 14 | 5% | 2% | -61% | -89% | -89% |
| 0.2–0.5% | 5036 | 25 | 6% | 3% | -46% | -88% | -87% |
| Over 0.5% | 1951 | 6 | 7% | 3% | -68% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6629 | 28 | 4% | 2% | -52% | -85% | -85% |
| Morning (6am–12pm) | 6213 | 29 | 4% | 2% | -47% | -88% | -87% |
| Afternoon (12–6pm) | 6157 | 19 | 3% | 1% | -64% | -88% | -89% |
| Evening (6pm–12am) | 7332 | 21 | 3% | 2% | -67% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,760 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/21 2:44:54 AM | NATGAS | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 2:44:54 AM | USDCAD | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 2:44:54 AM | SILVER | UP | 5 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/21 2:44:38 AM | AUDUSD | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 2:44:38 AM | GBPUSD | DOWN | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 2:44:38 AM | ETH | DOWN | 21 sec | +0.011% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 2:44:38 AM | PALLADIUM | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 2:44:22 AM | BTC | DOWN | 37 sec | +0.132% | 0¢ | ❌ Lost | $0.00 |
| 10/21 2:44:22 AM | BNB | DOWN | 37 sec | -0.020% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 2:44:06 AM | SOL | DOWN | 54 sec | +0.076% | 0¢ | ❌ Lost | $0.00 |
| 10/21 2:44:06 AM | DOGE | DOWN | 54 sec | +0.107% | 0¢ | ❌ Lost | $0.00 |
| 10/21 2:43:48 AM | NEAR | DOWN | 72 sec | +0.503% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 2:43:48 AM | XRP | DOWN | 72 sec | +0.186% | 0¢ | ❌ Lost | $0.00 |
| 10/21 2:43:16 AM | COPPER | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 2:42:45 AM | PLATINUM | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 2:41:08 AM | WTI | DOWN | 3.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 2:40:17 AM | HYPE | UP | 4.7 min | -0.392% | 4¢ | ❌ Lost | -$0.15 |
| 10/21 2:39:46 AM | ZEC | UP | 5.2 min | -0.519% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 2:37:20 AM | ETH | UP | 7.7 min | -0.246% | 100¢ | ✅ Won | $13.85 |
| 10/21 2:29:56 AM | NEAR | DOWN | 3 sec | -0.131% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 2:29:56 AM | WTI | DOWN | 3 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/21 2:29:56 AM | DOGE | DOWN | 3 sec | -0.024% | 0¢ | ❌ Lost | $0.00 |
| 10/21 2:29:56 AM | PALLADIUM | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 2:29:40 AM | AUDUSD | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 2:29:24 AM | BNB | DOWN | 35 sec | -0.008% | 0¢ | ❌ Lost | $0.00 |
| 10/21 2:29:08 AM | SOL | DOWN | 51 sec | +0.070% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 2:29:08 AM | NATGAS | UP | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 2:29:08 AM | USDJPY | DOWN | 51 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 2:28:36 AM | BTC | DOWN | 84 sec | +0.140% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 2:28:36 AM | ETH | DOWN | 84 sec | +0.114% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
