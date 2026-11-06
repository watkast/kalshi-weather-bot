# 15-Minute 1¢ Study

*Updated Fri Nov 6, 3:32 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3795 finished bets | 1% | $124.80 | +30% | +3.29¢ | $82.50 / $42.30 |

*Expect about **96 buys a day** (~$14.35/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3536 | $52.55 | +14% |
| Volatility model ≥ 2%, hold to the close | 7015 | $23.80 | +3% |
| Momentum model ≥ 2%, hold to the close | 5788 | -$48.50 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 48277 | 48260 | 175 (0%) | 1.07% | -$3,436.30 (-58%) | Hold to the close: -$3,436.30 (-58%) |

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
| Volatility model | 29050 | 4.7% | 0.4% (111) | -693% | ❌ Worse |
| Momentum model | 29050 | 4.6% | 0.4% (111) | -720% | ❌ Worse |
| Mean-reversion model | 29050 | 8.1% | 0.4% (111) | -842% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 29050 | 111 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 7015 | 62 | +3% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3795 | 39 | +30% | -77% | -75% | -72% |
| Volatility model ≥ 10% | 2172 | 24 | +59% | -72% | -70% | -67% |
| Momentum model ≥ 2% | 5788 | 44 | -7% | -82% | -81% | -78% |
| Momentum model ≥ 5% | 3536 | 31 | +14% | -80% | -79% | -75% |
| Momentum model ≥ 10% | 2311 | 20 | +22% | -75% | -75% | -71% |
| Mean-reversion model ≥ 2% | 12013 | 80 | -27% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8415 | 69 | -9% | -81% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5626 | 49 | -1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 29255 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11637 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7368 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 48260 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 175 | 0% | -$3,436.30 | -58% | — |
| Sell at 2¢ | 1898 | 4% | -$5,140.82 | -87% | 47 sec |
| Sell at 3¢ | 1294 | 3% | -$5,129.64 | -87% | 48 sec |
| Sell at 5¢ | 897 | 2% | -$5,023.25 | -85% | 63 sec |
| Sell at 10¢ | 540 | 1% | -$4,814.90 | -82% | 66 sec |
| Sell at 25¢ | 282 | 1% | -$4,476.88 | -76% | 83 sec |
| Sell at 50¢ | 180 | 0% | -$4,097.30 | -70% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2390 | 10 | 11% | 4% | -60% | -81% | -82% |
| 2–5 min | 15502 | 83 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 12154 | 40 | 3% | 1% | -64% | -92% | -92% |
| Under 1 min | 18202 | 42 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3279 | 13 | 5% | 3% | -49% | -88% | -88% |
| SOL | 3272 | 12 | 4% | 2% | -53% | -90% | -90% |
| BNB | 3263 | 17 | 5% | 2% | -34% | -85% | -84% |
| HYPE | 3262 | 10 | 5% | 2% | -62% | -89% | -88% |
| DOGE | 3252 | 6 | 4% | 2% | -77% | -90% | -90% |
| ETH | 3249 | 12 | 7% | 3% | -55% | -85% | -85% |
| NEAR | 3230 | 16 | 5% | 2% | -36% | -84% | -84% |
| BTC | 3227 | 15 | 5% | 2% | -37% | -88% | -89% |
| XRP | 3221 | 12 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1783 | 5 | 5% | 2% | -66% | -81% | -83% |
| WTI | 1736 | 6 | 4% | 1% | -58% | -92% | -92% |
| SILVER | 1733 | 8 | 5% | 2% | -45% | -82% | -81% |
| PLATINUM | 1567 | 4 | 2% | 1% | -76% | -96% | -96% |
| EURUSD | 1503 | 4 | 2% | 1% | -75% | -90% | -89% |
| COPPER | 1471 | 6 | 2% | 1% | -62% | -72% | -71% |
| GBPUSD | 1426 | 4 | 2% | 1% | -74% | -96% | -96% |
| NATGAS | 1423 | 8 | 2% | 1% | -48% | -76% | -76% |
| PALLADIUM | 1408 | 3 | 1% | 0% | -80% | -91% | -92% |
| USDJPY | 1406 | 5 | 2% | 1% | -67% | -97% | -96% |
| AUDUSD | 960 | 4 | 2% | 1% | -61% | -87% | -87% |
| USDCAD | 929 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 516 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 303 | 1 | 4% | 1% | -69% | -62% | -60% |
| 2YRRATE | 287 | 3 | 4% | 1% | -2% | -28% | -27% |
| 30YRRATE | 285 | 0 | 2% | 1% | -100% | -96% | -95% |
| 5YRRATE | 262 | 1 | 4% | 2% | -64% | -93% | -95% |
| INX | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 24478 | 94 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 23782 | 81 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4667 | 22 | 2% | 1% | -17% | -83% | -82% |
| 0.05–0.1% | 4952 | 18 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 7526 | 26 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 8769 | 34 | 6% | 3% | -57% | -87% | -86% |
| Over 0.5% | 3333 | 13 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11768 | 41 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11949 | 51 | 4% | 2% | -51% | -86% | -85% |
| Afternoon (12–6pm) | 11596 | 42 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 12947 | 41 | 3% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,619 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/6 3:29:43 PM | BNB | DOWN | 16 sec | +0.019% | 0¢ | ❌ Lost | $0.00 |
| 11/6 3:29:43 PM | NEAR | UP | 16 sec | -0.013% | 0¢ | ❌ Lost | $0.00 |
| 11/6 3:29:43 PM | SOL | UP | 16 sec | -0.025% | 0¢ | ❌ Lost | $0.00 |
| 11/6 3:29:27 PM | NATGAS | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 3:29:27 PM | HYPE | DOWN | 32 sec | +0.049% | 0¢ | ❌ Lost | -$0.15 |
| 11/6 3:29:27 PM | BTC | DOWN | 32 sec | +0.042% | 0¢ | ❌ Lost | $0.00 |
| 11/6 3:29:27 PM | ETH | DOWN | 32 sec | +0.026% | 0¢ | ❌ Lost | $0.00 |
| 11/6 3:29:11 PM | ZEC | UP | 48 sec | -0.048% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 3:29:11 PM | BRENT | DOWN | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 3:27:51 PM | XRP | DOWN | 2.1 min | +0.136% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 3:27:51 PM | DOGE | UP | 2.1 min | -0.117% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 3:14:46 PM | XRP | DOWN | 14 sec | -0.009% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 3:14:46 PM | ETH | UP | 14 sec | -0.051% | 0¢ | ❌ Lost | $0.00 |
| 11/6 3:14:14 PM | SOL | UP | 46 sec | -0.097% | 0¢ | ❌ Lost | $0.00 |
| 11/6 3:14:14 PM | DOGE | UP | 46 sec | -0.058% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 3:13:59 PM | BTC | DOWN | 60 sec | +0.107% | 0¢ | ❌ Lost | $0.00 |
| 11/6 3:13:42 PM | WTI | UP | 78 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/6 3:13:26 PM | NEAR | UP | 1.6 min | -0.388% | 0¢ | ❌ Lost | $0.00 |
| 11/6 3:13:10 PM | ZEC | UP | 1.8 min | -0.309% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 3:11:51 PM | BNB | DOWN | 3.1 min | +0.130% | 0¢ | ❌ Lost | $0.00 |
| 11/6 3:09:27 PM | NATGAS | DOWN | 5.5 min | — | 7¢ | ❌ Lost | -$0.15 |
| 11/6 2:59:48 PM | GBPUSD | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:59:48 PM | 5YRRATE | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:59:32 PM | 10YRRATE | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:59:16 PM | AUDUSD | DOWN | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:59:16 PM | 30YRRATE | DOWN | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:59:16 PM | PALLADIUM | UP | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:59:00 PM | BRENT | UP | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 2:59:00 PM | WTI | UP | 60 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/6 2:58:28 PM | 2YRRATE | DOWN | 1.5 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
