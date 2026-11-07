# 15-Minute 1¢ Study

*Updated Fri Nov 6, 6:07 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3815 finished bets | 1% | $122.85 | +29% | +3.22¢ | $81.00 / $41.85 |

*Expect about **96 buys a day** (~$14.39/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3546 | $51.50 | +13% |
| Volatility model ≥ 2%, hold to the close | 7042 | $20.95 | +2% |
| Momentum model ≥ 2%, hold to the close | 5810 | -$50.45 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 48375 | 48358 | 175 (0%) | 1.07% | -$3,446.65 (-58%) | Hold to the close: -$3,446.65 (-58%) |

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
| Volatility model | 29132 | 4.7% | 0.4% (111) | -697% | ❌ Worse |
| Momentum model | 29132 | 4.6% | 0.4% (111) | -724% | ❌ Worse |
| Mean-reversion model | 29132 | 8.1% | 0.4% (111) | -847% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 29132 | 111 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 7042 | 62 | +2% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3815 | 39 | +29% | -77% | -75% | -72% |
| Volatility model ≥ 10% | 2181 | 24 | +59% | -72% | -70% | -67% |
| Momentum model ≥ 2% | 5810 | 44 | -8% | -82% | -81% | -78% |
| Momentum model ≥ 5% | 3546 | 31 | +13% | -80% | -79% | -75% |
| Momentum model ≥ 10% | 2317 | 20 | +22% | -75% | -75% | -71% |
| Mean-reversion model ≥ 2% | 12051 | 80 | -27% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8446 | 69 | -9% | -82% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5651 | 49 | -1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 29337 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11653 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7368 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 48358 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 175 | 0% | -$3,446.65 | -58% | — |
| Sell at 2¢ | 1900 | 4% | -$5,150.65 | -87% | 47 sec |
| Sell at 3¢ | 1295 | 3% | -$5,139.60 | -87% | 48 sec |
| Sell at 5¢ | 898 | 2% | -$5,032.95 | -85% | 63 sec |
| Sell at 10¢ | 540 | 1% | -$4,825.25 | -82% | 66 sec |
| Sell at 25¢ | 282 | 1% | -$4,487.23 | -76% | 83 sec |
| Sell at 50¢ | 180 | 0% | -$4,107.65 | -70% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2391 | 10 | 11% | 4% | -60% | -81% | -83% |
| 2–5 min | 15537 | 83 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 12182 | 40 | 3% | 1% | -64% | -92% | -92% |
| Under 1 min | 18236 | 42 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3289 | 13 | 5% | 2% | -49% | -88% | -88% |
| SOL | 3282 | 12 | 4% | 2% | -53% | -90% | -90% |
| HYPE | 3271 | 10 | 5% | 2% | -62% | -89% | -88% |
| BNB | 3271 | 17 | 5% | 2% | -34% | -85% | -84% |
| DOGE | 3261 | 6 | 4% | 2% | -77% | -90% | -90% |
| ETH | 3258 | 12 | 7% | 3% | -55% | -85% | -85% |
| NEAR | 3238 | 16 | 5% | 2% | -36% | -84% | -84% |
| BTC | 3236 | 15 | 5% | 2% | -37% | -88% | -89% |
| XRP | 3231 | 12 | 3% | 1% | -54% | -89% | -89% |
| GOLD | 1783 | 5 | 5% | 2% | -66% | -81% | -83% |
| WTI | 1743 | 6 | 4% | 1% | -59% | -92% | -92% |
| SILVER | 1733 | 8 | 5% | 2% | -45% | -82% | -81% |
| PLATINUM | 1567 | 4 | 2% | 1% | -76% | -96% | -96% |
| EURUSD | 1503 | 4 | 2% | 1% | -75% | -90% | -89% |
| COPPER | 1471 | 6 | 2% | 1% | -62% | -72% | -71% |
| NATGAS | 1427 | 8 | 2% | 1% | -48% | -76% | -76% |
| GBPUSD | 1426 | 4 | 2% | 1% | -74% | -96% | -96% |
| PALLADIUM | 1408 | 3 | 1% | 0% | -80% | -91% | -92% |
| USDJPY | 1406 | 5 | 2% | 1% | -67% | -97% | -96% |
| AUDUSD | 960 | 4 | 2% | 1% | -61% | -87% | -87% |
| USDCAD | 929 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 521 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 303 | 1 | 4% | 1% | -69% | -62% | -60% |
| 2YRRATE | 287 | 3 | 4% | 1% | -2% | -28% | -27% |
| 30YRRATE | 285 | 0 | 2% | 1% | -100% | -96% | -95% |
| 5YRRATE | 262 | 1 | 4% | 2% | -64% | -93% | -95% |
| INX | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 24525 | 94 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 23833 | 81 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4684 | 22 | 2% | 1% | -17% | -83% | -82% |
| 0.05–0.1% | 4972 | 18 | 3% | 2% | -45% | -91% | -91% |
| 0.1–0.2% | 7548 | 26 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 8789 | 34 | 6% | 3% | -57% | -87% | -86% |
| Over 0.5% | 3336 | 13 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11768 | 41 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11949 | 51 | 4% | 2% | -51% | -86% | -85% |
| Afternoon (12–6pm) | 11694 | 42 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 12947 | 41 | 3% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,634 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/6 5:59:55 PM | BNB | DOWN | 5 sec | -0.029% | 0¢ | ❌ Lost | $0.00 |
| 11/6 5:59:55 PM | SOL | DOWN | 5 sec | -0.010% | 0¢ | ❌ Lost | $0.00 |
| 11/6 5:59:39 PM | DOGE | DOWN | 21 sec | +0.005% | 0¢ | ❌ Lost | $0.00 |
| 11/6 5:59:23 PM | XRP | UP | 37 sec | -0.076% | 0¢ | ❌ Lost | $0.00 |
| 11/6 5:59:23 PM | BTC | UP | 37 sec | -0.039% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 5:59:07 PM | ETH | UP | 52 sec | -0.058% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 5:57:04 PM | NEAR | DOWN | 2.9 min | +0.285% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 5:55:45 PM | ZEC | DOWN | 4.2 min | +0.564% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 5:54:57 PM | HYPE | DOWN | 5.0 min | +0.279% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 5:44:49 PM | NATGAS | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 5:44:49 PM | BRENT | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 5:44:33 PM | DOGE | UP | 26 sec | -0.064% | 0¢ | ❌ Lost | $0.00 |
| 11/6 5:44:33 PM | WTI | UP | 26 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/6 5:44:17 PM | SOL | UP | 42 sec | -0.056% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 5:44:01 PM | BNB | UP | 58 sec | -0.079% | 0¢ | ❌ Lost | -$0.15 |
| 11/6 5:43:29 PM | XRP | DOWN | 1.5 min | +0.102% | 0¢ | ❌ Lost | -$0.15 |
| 11/6 5:43:29 PM | NEAR | DOWN | 1.5 min | +0.194% | 0¢ | ❌ Lost | $0.00 |
| 11/6 5:42:57 PM | ZEC | DOWN | 2.0 min | +0.241% | 0¢ | ❌ Lost | -$0.15 |
| 11/6 5:41:22 PM | HYPE | DOWN | 3.6 min | +0.228% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 5:29:47 PM | NATGAS | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 5:29:47 PM | ZEC | UP | 12 sec | -0.066% | 0¢ | ❌ Lost | $0.00 |
| 11/6 5:29:31 PM | BNB | DOWN | 28 sec | -0.035% | 0¢ | ❌ Lost | -$0.15 |
| 11/6 5:29:15 PM | BTC | UP | 44 sec | -0.038% | 0¢ | ❌ Lost | $0.00 |
| 11/6 5:28:43 PM | BRENT | UP | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 5:28:43 PM | ETH | UP | 76 sec | -0.071% | 0¢ | ❌ Lost | $0.00 |
| 11/6 5:27:39 PM | WTI | UP | 2.3 min | — | 2¢ | ❌ Lost | -$0.15 |
| 11/6 5:27:39 PM | SOL | DOWN | 2.3 min | +0.100% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 5:27:07 PM | HYPE | DOWN | 2.9 min | +0.196% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 5:26:51 PM | XRP | UP | 3.1 min | -0.212% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 5:14:27 PM | HYPE | DOWN | 33 sec | -0.001% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
