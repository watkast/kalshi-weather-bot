# 15-Minute 1¢ Study

*Updated Tue Nov 24, 12:52 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4830 finished bets | 1% | $214.75 | +41% | +4.45¢ | $76.85 / $137.90 |

*Expect about **85 buys a day** (~$12.70/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4575 | $113.30 | +23% |
| Volatility model ≥ 2%, hold to the close | 8991 | $47.50 | +4% |
| Momentum model ≥ 2%, hold to the close | 7491 | -$26.15 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 66229 | 66195 | 254 (0%) | 1.07% | -$4,458.80 (-56%) | Hold to the close: -$4,458.80 (-56%) |

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
| Volatility model | 39468 | 4.5% | 0.4% (164) | -641% | ❌ Worse |
| Momentum model | 39468 | 4.4% | 0.4% (164) | -664% | ❌ Worse |
| Mean-reversion model | 39468 | 7.9% | 0.4% (164) | -779% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 39468 | 164 | -46% | -87% | -86% | -84% |
| Volatility model ≥ 2% | 8991 | 80 | +4% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4830 | 53 | +41% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 2796 | 32 | +69% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 7491 | 59 | -3% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 4575 | 43 | +23% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 2982 | 28 | +35% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 16054 | 112 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 11175 | 92 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7422 | 66 | +2% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 39674 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15692 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10829 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 66195 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 254 | 0% | -$4,458.80 | -56% | — |
| Sell at 2¢ | 2712 | 4% | -$7,015.68 | -88% | 47 sec |
| Sell at 3¢ | 1827 | 3% | -$7,008.27 | -87% | 48 sec |
| Sell at 5¢ | 1247 | 2% | -$6,882.25 | -86% | 62 sec |
| Sell at 10¢ | 764 | 1% | -$6,607.96 | -82% | 65 sec |
| Sell at 25¢ | 410 | 1% | -$6,097.70 | -76% | 79 sec |
| Sell at 50¢ | 263 | 0% | -$5,497.55 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3422 | 17 | 11% | 4% | -53% | -81% | -83% |
| 2–5 min | 21459 | 115 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 16542 | 57 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 24759 | 65 | 1% | 0% | -62% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4435 | 19 | 5% | 2% | -43% | -88% | -87% |
| HYPE | 4429 | 16 | 5% | 2% | -53% | -89% | -88% |
| SOL | 4427 | 20 | 4% | 2% | -42% | -86% | -86% |
| BNB | 4418 | 22 | 5% | 2% | -37% | -86% | -85% |
| DOGE | 4414 | 12 | 5% | 2% | -65% | -89% | -89% |
| ETH | 4409 | 19 | 7% | 3% | -46% | -82% | -82% |
| BTC | 4388 | 24 | 5% | 2% | -25% | -86% | -87% |
| NEAR | 4383 | 18 | 5% | 2% | -46% | -85% | -86% |
| XRP | 4371 | 16 | 4% | 2% | -53% | -89% | -88% |
| GOLD | 2326 | 8 | 5% | 2% | -58% | -82% | -84% |
| WTI | 2311 | 8 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 2268 | 9 | 5% | 2% | -52% | -83% | -83% |
| PLATINUM | 2061 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 2023 | 7 | 3% | 1% | -68% | -91% | -90% |
| GBPUSD | 1952 | 8 | 2% | 1% | -62% | -96% | -96% |
| COPPER | 1950 | 6 | 2% | 1% | -71% | -78% | -78% |
| USDJPY | 1916 | 6 | 2% | 1% | -71% | -96% | -96% |
| NATGAS | 1913 | 10 | 2% | 1% | -51% | -77% | -76% |
| PALLADIUM | 1851 | 4 | 1% | 1% | -80% | -93% | -93% |
| AUDUSD | 1468 | 6 | 2% | 1% | -62% | -90% | -90% |
| USDCAD | 1387 | 1 | 3% | 1% | -93% | -96% | -96% |
| BRENT | 1012 | 1 | 2% | 1% | -91% | -96% | -97% |
| 10YRRATE | 520 | 2 | 3% | 1% | -64% | -77% | -75% |
| 2YRRATE | 494 | 4 | 4% | 2% | -24% | -56% | -55% |
| 30YRRATE | 479 | 0 | 3% | 1% | -100% | -96% | -93% |
| 5YRRATE | 471 | 2 | 3% | 1% | -60% | -94% | -96% |
| INX | 112 | 1 | 2% | 1% | -17% | -97% | -98% |
| USDMXN | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 33843 | 130 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 32352 | 124 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5795 | 25 | 2% | 1% | -21% | -78% | -78% |
| 0.05–0.1% | 6330 | 26 | 3% | 2% | -34% | -91% | -90% |
| 0.1–0.2% | 9866 | 36 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12477 | 56 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 5197 | 23 | 7% | 3% | -54% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16048 | 49 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 15586 | 81 | 4% | 2% | -41% | -85% | -85% |
| Afternoon (12–6pm) | 16344 | 73 | 4% | 2% | -47% | -87% | -87% |
| Evening (6pm–12am) | 18217 | 51 | 4% | 2% | -68% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,136 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/24 12:44:56 AM | BNB | DOWN | 3 sec | -0.040% | 0¢ | ❌ Lost | -$0.15 |
| 11/24 12:44:56 AM | WTI | DOWN | 3 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/24 12:44:56 AM | NATGAS | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 12:44:56 AM | BTC | DOWN | 3 sec | +0.093% | 0¢ | ❌ Lost | $0.00 |
| 11/24 12:44:56 AM | USDJPY | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 12:44:40 AM | XRP | UP | 19 sec | -0.085% | 0¢ | ❌ Lost | $0.00 |
| 11/24 12:44:24 AM | EURUSD | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 12:44:08 AM | SOL | UP | 52 sec | -0.181% | 0¢ | ❌ Lost | $0.00 |
| 11/24 12:43:36 AM | ETH | DOWN | 84 sec | +0.165% | 0¢ | ❌ Lost | $0.00 |
| 11/24 12:43:36 AM | COPPER | DOWN | 84 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 12:43:36 AM | USDCAD | UP | 84 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 12:43:05 AM | ZEC | UP | 1.9 min | -0.354% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 12:43:05 AM | SILVER | DOWN | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/24 12:42:49 AM | DOGE | UP | 2.2 min | -0.247% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 12:42:49 AM | NEAR | UP | 2.2 min | -0.424% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 12:42:49 AM | GOLD | DOWN | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/24 12:42:49 AM | PLATINUM | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 12:41:56 AM | PALLADIUM | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 12:41:40 AM | HYPE | UP | 3.3 min | -0.574% | 0¢ | ❌ Lost | -$0.15 |
| 11/24 12:29:54 AM | GBPUSD | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 12:29:54 AM | ZEC | DOWN | 5 sec | -0.001% | 0¢ | ❌ Lost | -$0.15 |
| 11/24 12:29:54 AM | BTC | UP | 5 sec | -0.042% | 0¢ | ❌ Lost | $0.00 |
| 11/24 12:29:38 AM | USDCAD | DOWN | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 12:29:38 AM | PLATINUM | DOWN | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 12:29:38 AM | SILVER | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 12:29:22 AM | COPPER | UP | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 12:29:06 AM | ETH | UP | 54 sec | -0.156% | 0¢ | ❌ Lost | $0.00 |
| 11/24 12:29:06 AM | DOGE | UP | 54 sec | -0.135% | 0¢ | ❌ Lost | -$0.15 |
| 11/24 12:29:06 AM | SOL | UP | 54 sec | -0.120% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 12:29:06 AM | XRP | UP | 54 sec | -0.159% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
