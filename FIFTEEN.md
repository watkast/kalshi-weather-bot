# 15-Minute 1¢ Study

*Updated Wed Oct 21, 5:20 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2231 finished bets | 1% | $84.15 | +33% | +3.77¢ | $46.80 / $37.35 |

*Expect about **96 buys a day** (~$14.43/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2067 | $64.65 | +28% |
| Volatility model ≥ 2%, hold to the close | 4089 | -$24.85 | -5% |
| Momentum model ≥ 2%, hold to the close | 3452 | -$28.80 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 26504 | 26497 | 97 (0%) | 1.07% | -$1,870.60 (-58%) | Hold to the close: -$1,870.60 (-58%) |

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
| Volatility model | 17185 | 4.6% | 0.4% (69) | -667% | ❌ Worse |
| Momentum model | 17185 | 4.6% | 0.4% (69) | -690% | ❌ Worse |
| Mean-reversion model | 17185 | 7.8% | 0.4% (69) | -806% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17185 | 69 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4089 | 34 | -5% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 2231 | 24 | +33% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 1282 | 16 | +75% | -61% | -59% | -56% |
| Momentum model ≥ 2% | 3452 | 27 | -7% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2067 | 21 | +28% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1360 | 14 | +40% | -68% | -67% | -62% |
| Mean-reversion model ≥ 2% | 6782 | 45 | -28% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4732 | 37 | -14% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3141 | 25 | -10% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 17383 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6315 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2799 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 26497 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 97 | 0% | -$1,870.60 | -58% | — |
| Sell at 2¢ | 960 | 4% | -$2,839.00 | -88% | 46 sec |
| Sell at 3¢ | 652 | 2% | -$2,834.32 | -88% | 48 sec |
| Sell at 5¢ | 461 | 2% | -$2,788.95 | -86% | 56 sec |
| Sell at 10¢ | 280 | 1% | -$2,693.80 | -83% | 64 sec |
| Sell at 25¢ | 152 | 1% | -$2,501.48 | -77% | 80 sec |
| Sell at 50¢ | 99 | 0% | -$2,266.35 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1069 | 6 | 10% | 4% | -46% | -81% | -84% |
| 2–5 min | 8541 | 43 | 7% | 3% | -50% | -87% | -87% |
| 1–2 min | 6767 | 25 | 3% | 1% | -60% | -93% | -92% |
| Under 1 min | 10116 | 23 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1951 | 11 | 5% | 2% | -30% | -90% | -90% |
| BNB | 1943 | 10 | 5% | 2% | -37% | -83% | -82% |
| HYPE | 1941 | 6 | 5% | 3% | -62% | -89% | -87% |
| ETH | 1932 | 10 | 6% | 3% | -38% | -87% | -86% |
| DOGE | 1930 | 3 | 4% | 2% | -81% | -91% | -90% |
| SOL | 1929 | 2 | 3% | 1% | -87% | -92% | -92% |
| XRP | 1923 | 7 | 3% | 1% | -55% | -88% | -88% |
| NEAR | 1917 | 11 | 6% | 3% | -26% | -79% | -79% |
| BTC | 1917 | 11 | 5% | 2% | -23% | -88% | -90% |
| GOLD | 1034 | 2 | 3% | 1% | -77% | -81% | -83% |
| SILVER | 996 | 4 | 3% | 1% | -54% | -82% | -82% |
| WTI | 974 | 3 | 3% | 1% | -64% | -94% | -95% |
| PLATINUM | 867 | 0 | 1% | 0% | -100% | -99% | -99% |
| COPPER | 863 | 3 | 2% | 1% | -68% | -76% | -75% |
| NATGAS | 797 | 5 | 2% | 1% | -41% | -85% | -84% |
| EURUSD | 792 | 3 | 2% | 1% | -65% | -84% | -84% |
| PALLADIUM | 784 | 2 | 1% | 0% | -76% | -86% | -86% |
| GBPUSD | 742 | 1 | 2% | 1% | -87% | -97% | -96% |
| USDJPY | 702 | 3 | 1% | 1% | -60% | -99% | -98% |
| AUDUSD | 306 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 257 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 13322 | 49 | 4% | 2% | -58% | -88% | -87% |
| DOWN (bought NO) | 13175 | 48 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2918 | 15 | 2% | 1% | -14% | -78% | -77% |
| 0.05–0.1% | 3020 | 11 | 3% | 2% | -47% | -92% | -91% |
| 0.1–0.2% | 4423 | 14 | 5% | 2% | -61% | -89% | -89% |
| 0.2–0.5% | 5063 | 25 | 6% | 3% | -46% | -88% | -87% |
| Over 0.5% | 1956 | 6 | 7% | 3% | -68% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6795 | 28 | 4% | 2% | -53% | -85% | -85% |
| Morning (6am–12pm) | 6213 | 29 | 4% | 2% | -47% | -88% | -87% |
| Afternoon (12–6pm) | 6157 | 19 | 3% | 1% | -64% | -88% | -89% |
| Evening (6pm–12am) | 7332 | 21 | 3% | 2% | -67% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,742 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/21 5:14:58 AM | USDCAD | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:14:42 AM | COPPER | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:14:42 AM | GOLD | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:14:42 AM | GBPUSD | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:14:42 AM | PLATINUM | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:14:26 AM | NATGAS | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:14:10 AM | DOGE | DOWN | 50 sec | +0.106% | 0¢ | ❌ Lost | $0.00 |
| 10/21 5:14:10 AM | EURUSD | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:13:54 AM | BTC | DOWN | 66 sec | +0.047% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 5:13:54 AM | USDJPY | UP | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:13:38 AM | BNB | DOWN | 82 sec | +0.015% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:13:38 AM | SILVER | DOWN | 82 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/21 5:13:22 AM | ZEC | DOWN | 1.6 min | +0.341% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:13:22 AM | XRP | DOWN | 1.6 min | +0.170% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:12:51 AM | HYPE | DOWN | 2.1 min | +0.130% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 5:10:43 AM | PALLADIUM | UP | 4.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:10:43 AM | WTI | UP | 4.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 5:10:43 AM | NEAR | DOWN | 4.3 min | +0.605% | 2¢ | ❌ Lost | -$0.15 |
| 10/21 5:09:49 AM | SOL | DOWN | 5.2 min | +0.266% | 2¢ | ❌ Lost | -$0.15 |
| 10/21 5:09:33 AM | ETH | DOWN | 5.4 min | +0.255% | 2¢ | ❌ Lost | -$0.15 |
| 10/21 4:59:45 AM | XRP | DOWN | 14 sec | -0.007% | 0¢ | ❌ Lost | $0.00 |
| 10/21 4:59:45 AM | GBPUSD | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:59:45 AM | HYPE | DOWN | 14 sec | -0.050% | 0¢ | ❌ Lost | $0.00 |
| 10/21 4:59:29 AM | ZEC | UP | 31 sec | -0.108% | 0¢ | ❌ Lost | $0.00 |
| 10/21 4:59:29 AM | GOLD | UP | 31 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/21 4:59:29 AM | BTC | UP | 31 sec | -0.049% | 0¢ | ❌ Lost | $0.00 |
| 10/21 4:59:11 AM | BNB | DOWN | 49 sec | +0.001% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:59:11 AM | NEAR | UP | 49 sec | -0.285% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 4:59:11 AM | NATGAS | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:58:55 AM | SILVER | UP | 65 sec | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
