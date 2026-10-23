# 15-Minute 1¢ Study

*Updated Thu Oct 22, 6:51 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2407 finished bets | 1% | $77.60 | +28% | +3.22¢ | $37.35 / $40.25 |

*Expect about **97 buys a day** (~$14.58/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2224 | $47.25 | +19% |
| Volatility model ≥ 2%, hold to the close | 4444 | $1.05 | +0% |
| Momentum model ≥ 2%, hold to the close | 3713 | -$31.55 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 28883 | 28875 | 110 (0%) | 1.07% | -$1,980.50 (-56%) | Hold to the close: -$1,980.50 (-56%) |

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
| Volatility model | 18437 | 4.7% | 0.4% (79) | -642% | ❌ Worse |
| Momentum model | 18437 | 4.6% | 0.4% (79) | -666% | ❌ Worse |
| Mean-reversion model | 18437 | 7.9% | 0.4% (79) | -773% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 18437 | 79 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4444 | 39 | +0% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 2407 | 25 | +28% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 1370 | 16 | +64% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 3713 | 29 | -7% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2224 | 21 | +19% | -76% | -76% | -72% |
| Momentum model ≥ 10% | 1463 | 14 | +31% | -69% | -68% | -64% |
| Mean-reversion model ≥ 2% | 7376 | 52 | -23% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5160 | 43 | -8% | -81% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3431 | 30 | -1% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 18636 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 6939 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 3300 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 28875 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 110 | 0% | -$1,980.50 | -56% | — |
| Sell at 2¢ | 1063 | 4% | -$3,104.12 | -88% | 47 sec |
| Sell at 3¢ | 725 | 3% | -$3,097.75 | -88% | 48 sec |
| Sell at 5¢ | 510 | 2% | -$3,049.00 | -87% | 61 sec |
| Sell at 10¢ | 313 | 1% | -$2,942.47 | -84% | 64 sec |
| Sell at 25¢ | 173 | 1% | -$2,709.87 | -77% | 82 sec |
| Sell at 50¢ | 114 | 0% | -$2,443.00 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1213 | 7 | 11% | 4% | -45% | -81% | -83% |
| 2–5 min | 9290 | 52 | 7% | 3% | -45% | -87% | -87% |
| 1–2 min | 7331 | 28 | 3% | 1% | -58% | -93% | -93% |
| Under 1 min | 11037 | 23 | 1% | 0% | -70% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2089 | 12 | 5% | 2% | -28% | -89% | -89% |
| BNB | 2082 | 12 | 5% | 3% | -29% | -83% | -82% |
| HYPE | 2080 | 8 | 5% | 3% | -53% | -89% | -87% |
| ETH | 2071 | 10 | 6% | 3% | -42% | -86% | -85% |
| SOL | 2071 | 3 | 3% | 1% | -82% | -92% | -92% |
| DOGE | 2067 | 4 | 4% | 2% | -76% | -90% | -89% |
| XRP | 2062 | 8 | 3% | 1% | -52% | -88% | -88% |
| NEAR | 2058 | 12 | 6% | 3% | -24% | -80% | -80% |
| BTC | 2056 | 12 | 5% | 2% | -22% | -88% | -90% |
| GOLD | 1134 | 3 | 4% | 1% | -69% | -82% | -83% |
| SILVER | 1095 | 5 | 3% | 1% | -47% | -82% | -82% |
| WTI | 1075 | 3 | 3% | 1% | -67% | -94% | -95% |
| PLATINUM | 953 | 0 | 1% | 1% | -100% | -99% | -98% |
| COPPER | 941 | 3 | 1% | 1% | -70% | -78% | -77% |
| EURUSD | 883 | 3 | 2% | 1% | -68% | -86% | -86% |
| NATGAS | 878 | 5 | 2% | 1% | -47% | -86% | -85% |
| PALLADIUM | 850 | 2 | 1% | 0% | -78% | -87% | -87% |
| GBPUSD | 832 | 1 | 2% | 1% | -89% | -97% | -97% |
| USDJPY | 803 | 4 | 1% | 1% | -54% | -99% | -98% |
| AUDUSD | 378 | 0 | 0% | 0% | -100% | -100% | -99% |
| USDCAD | 336 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 21 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 13 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 11 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 14584 | 59 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 14291 | 51 | 3% | 1% | -59% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3094 | 15 | 2% | 1% | -19% | -79% | -78% |
| 0.05–0.1% | 3199 | 11 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 4779 | 17 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 5455 | 28 | 6% | 3% | -44% | -87% | -87% |
| Over 0.5% | 2105 | 10 | 7% | 3% | -51% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7128 | 30 | 4% | 2% | -52% | -86% | -85% |
| Morning (6am–12pm) | 7002 | 33 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6955 | 21 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 7790 | 26 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,681 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/22 6:44:47 PM | GBPUSD | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 6:44:31 PM | PLATINUM | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 6:44:17 PM | AUDUSD | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 6:44:17 PM | HYPE | DOWN | 42 sec | +0.134% | 0¢ | ❌ Lost | $0.00 |
| 10/22 6:44:17 PM | DOGE | DOWN | 42 sec | +0.116% | 0¢ | ❌ Lost | $0.00 |
| 10/22 6:44:01 PM | ZEC | DOWN | 59 sec | +0.298% | 0¢ | ❌ Lost | $0.00 |
| 10/22 6:44:01 PM | NEAR | DOWN | 59 sec | +0.404% | 0¢ | ❌ Lost | $0.00 |
| 10/22 6:44:01 PM | WTI | DOWN | 59 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 6:43:42 PM | SILVER | DOWN | 77 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 6:43:26 PM | BNB | DOWN | 1.6 min | +0.078% | 0¢ | ❌ Lost | $0.00 |
| 10/22 6:43:26 PM | SOL | DOWN | 1.6 min | +0.104% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 6:42:25 PM | XRP | DOWN | 2.6 min | +0.145% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 6:41:32 PM | BTC | DOWN | 3.5 min | +0.192% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 6:40:45 PM | ETH | DOWN | 4.2 min | +0.259% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 6:29:54 PM | BNB | UP | 5 sec | -0.034% | 0¢ | ❌ Lost | $0.00 |
| 10/22 6:29:54 PM | NATGAS | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 6:29:54 PM | BTC | DOWN | 5 sec | +0.027% | 0¢ | ❌ Lost | $0.00 |
| 10/22 6:29:38 PM | GBPUSD | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 6:29:38 PM | ZEC | UP | 21 sec | -0.101% | 0¢ | ❌ Lost | $0.00 |
| 10/22 6:29:22 PM | XRP | DOWN | 37 sec | +0.046% | 0¢ | ❌ Lost | $0.00 |
| 10/22 6:29:22 PM | PALLADIUM | UP | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 6:29:22 PM | ETH | UP | 37 sec | -0.056% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 6:29:22 PM | DOGE | DOWN | 37 sec | +0.071% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 6:29:06 PM | AUDUSD | DOWN | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 6:29:06 PM | PLATINUM | UP | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 6:29:06 PM | HYPE | DOWN | 53 sec | +0.088% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 6:28:35 PM | SILVER | UP | 85 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/22 6:28:19 PM | NEAR | UP | 1.7 min | -0.330% | 2¢ | ❌ Lost | -$0.15 |
| 10/22 6:28:03 PM | GOLD | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 6:27:47 PM | SOL | DOWN | 2.2 min | +0.152% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
