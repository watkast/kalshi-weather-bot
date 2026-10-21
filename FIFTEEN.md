# 15-Minute 1¢ Study

*Updated Wed Oct 21, 2:31 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2214 finished bets | 1% | $85.95 | +34% | +3.88¢ | $47.70 / $38.25 |

*Expect about **96 buys a day** (~$14.39/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2054 | $66.15 | +29% |
| Momentum model ≥ 2%, hold to the close | 3424 | -$25.80 | -6% |
| Volatility model ≥ 2%, hold to the close | 4054 | -$34.80 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 26319 | 26312 | 96 (0%) | 1.07% | -$1,862.25 (-58%) | Hold to the close: -$1,862.25 (-58%) |

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
| Volatility model | 17088 | 4.6% | 0.4% (68) | -670% | ❌ Worse |
| Momentum model | 17088 | 4.5% | 0.4% (68) | -692% | ❌ Worse |
| Mean-reversion model | 17088 | 7.8% | 0.4% (68) | -809% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17088 | 68 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4054 | 33 | -7% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 2214 | 24 | +34% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 1274 | 16 | +75% | -61% | -59% | -56% |
| Momentum model ≥ 2% | 3424 | 27 | -6% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2054 | 21 | +29% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 1351 | 14 | +41% | -68% | -67% | -62% |
| Mean-reversion model ≥ 2% | 6731 | 44 | -29% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4691 | 36 | -16% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3110 | 24 | -12% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 17286 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6258 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2768 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 26312 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 96 | 0% | -$1,862.25 | -58% | — |
| Sell at 2¢ | 955 | 4% | -$2,817.95 | -88% | 46 sec |
| Sell at 3¢ | 649 | 2% | -$2,813.14 | -88% | 48 sec |
| Sell at 5¢ | 460 | 2% | -$2,767.25 | -86% | 56 sec |
| Sell at 10¢ | 279 | 1% | -$2,672.76 | -83% | 64 sec |
| Sell at 25¢ | 151 | 1% | -$2,482.44 | -77% | 80 sec |
| Sell at 50¢ | 98 | 0% | -$2,250.75 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1058 | 5 | 10% | 4% | -55% | -82% | -84% |
| 2–5 min | 8486 | 43 | 7% | 3% | -50% | -87% | -87% |
| 1–2 min | 6720 | 25 | 3% | 2% | -60% | -93% | -92% |
| Under 1 min | 10044 | 23 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1940 | 11 | 4% | 2% | -29% | -90% | -90% |
| BNB | 1932 | 10 | 5% | 2% | -37% | -83% | -82% |
| HYPE | 1930 | 6 | 5% | 3% | -62% | -89% | -87% |
| ETH | 1921 | 9 | 6% | 3% | -44% | -87% | -86% |
| DOGE | 1920 | 3 | 4% | 2% | -81% | -91% | -90% |
| SOL | 1919 | 2 | 3% | 1% | -87% | -92% | -92% |
| XRP | 1912 | 7 | 3% | 1% | -55% | -88% | -88% |
| NEAR | 1906 | 11 | 6% | 3% | -26% | -79% | -79% |
| BTC | 1906 | 11 | 5% | 2% | -22% | -88% | -90% |
| GOLD | 1026 | 2 | 4% | 1% | -77% | -81% | -83% |
| SILVER | 988 | 4 | 3% | 1% | -53% | -82% | -81% |
| WTI | 965 | 3 | 3% | 1% | -63% | -94% | -95% |
| PLATINUM | 858 | 0 | 1% | 0% | -100% | -99% | -98% |
| COPPER | 856 | 3 | 2% | 1% | -67% | -76% | -75% |
| NATGAS | 788 | 5 | 2% | 1% | -41% | -84% | -84% |
| EURUSD | 785 | 3 | 2% | 1% | -64% | -84% | -84% |
| PALLADIUM | 777 | 2 | 1% | 0% | -76% | -86% | -86% |
| GBPUSD | 735 | 1 | 2% | 1% | -87% | -97% | -96% |
| USDJPY | 695 | 3 | 1% | 1% | -60% | -99% | -98% |
| AUDUSD | 302 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 251 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 13226 | 48 | 4% | 2% | -58% | -87% | -87% |
| DOWN (bought NO) | 13086 | 48 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2900 | 15 | 2% | 1% | -14% | -78% | -77% |
| 0.05–0.1% | 3011 | 11 | 3% | 2% | -47% | -92% | -91% |
| 0.1–0.2% | 4389 | 14 | 5% | 2% | -61% | -89% | -89% |
| 0.2–0.5% | 5034 | 24 | 6% | 3% | -48% | -88% | -87% |
| Over 0.5% | 1949 | 6 | 7% | 3% | -68% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6610 | 27 | 4% | 2% | -54% | -85% | -85% |
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
| 10/21 2:28:20 AM | COPPER | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 2:28:20 AM | HYPE | DOWN | 1.7 min | +0.251% | 0¢ | ❌ Lost | $0.00 |
| 10/21 2:28:20 AM | XRP | DOWN | 1.7 min | +0.194% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 2:28:04 AM | ZEC | DOWN | 1.9 min | +0.285% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 2:14:56 AM | WTI | DOWN | 4 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/21 2:14:40 AM | GOLD | UP | 20 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/21 2:14:40 AM | ETH | UP | 20 sec | -0.043% | 0¢ | ❌ Lost | $0.00 |
| 10/21 2:14:24 AM | ZEC | DOWN | 36 sec | +0.078% | 0¢ | ❌ Lost | $0.00 |
| 10/21 2:14:24 AM | PLATINUM | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 2:14:24 AM | BTC | DOWN | 36 sec | +0.056% | 0¢ | ❌ Lost | $0.00 |
| 10/21 2:14:24 AM | PALLADIUM | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 2:14:09 AM | XRP | UP | 50 sec | -0.126% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 2:14:09 AM | EURUSD | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 2:13:35 AM | SILVER | UP | 85 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 2:13:04 AM | NEAR | UP | 1.9 min | -0.630% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 2:13:04 AM | SOL | UP | 1.9 min | -0.182% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 2:13:04 AM | BNB | UP | 1.9 min | -0.124% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 2:11:10 AM | DOGE | UP | 3.8 min | -0.226% | 2¢ | ❌ Lost | -$0.15 |
| 10/21 2:10:04 AM | HYPE | UP | 4.9 min | -0.343% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
