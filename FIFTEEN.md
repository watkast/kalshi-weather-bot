# 15-Minute 1¢ Study

*Updated Wed Nov 4, 8:22 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3675 finished bets | 1% | $122.20 | +30% | +3.33¢ | $90.15 / $32.05 |

*Expect about **97 buys a day** (~$14.56/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3408 | $49.95 | +13% |
| Volatility model ≥ 2%, hold to the close | 6810 | $31.55 | +4% |
| Momentum model ≥ 2%, hold to the close | 5614 | -$45.25 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 46043 | 46032 | 169 (0%) | 1.07% | -$3,247.00 (-58%) | Hold to the close: -$3,247.00 (-58%) |

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
| Volatility model | 28053 | 4.7% | 0.4% (109) | -682% | ❌ Worse |
| Momentum model | 28053 | 4.6% | 0.4% (109) | -708% | ❌ Worse |
| Mean-reversion model | 28053 | 8.1% | 0.4% (109) | -831% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 28053 | 109 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6810 | 61 | +4% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3675 | 38 | +30% | -77% | -75% | -71% |
| Volatility model ≥ 10% | 2091 | 23 | +58% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5614 | 43 | -7% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 3408 | 30 | +13% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2225 | 19 | +20% | -75% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11619 | 79 | -25% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8155 | 68 | -8% | -81% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5463 | 48 | -0% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 28258 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10973 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6801 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 46032 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 169 | 0% | -$3,247.00 | -58% | — |
| Sell at 2¢ | 1810 | 4% | -$4,890.40 | -87% | 47 sec |
| Sell at 3¢ | 1236 | 3% | -$4,878.96 | -87% | 48 sec |
| Sell at 5¢ | 855 | 2% | -$4,777.25 | -85% | 63 sec |
| Sell at 10¢ | 516 | 1% | -$4,573.04 | -81% | 65 sec |
| Sell at 25¢ | 268 | 1% | -$4,249.92 | -76% | 83 sec |
| Sell at 50¢ | 172 | 0% | -$3,878.00 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2283 | 10 | 11% | 4% | -58% | -81% | -83% |
| 2–5 min | 14822 | 79 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 11581 | 39 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 17335 | 41 | 1% | 0% | -66% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3166 | 13 | 5% | 2% | -47% | -88% | -88% |
| SOL | 3161 | 12 | 4% | 2% | -52% | -90% | -90% |
| HYPE | 3153 | 9 | 5% | 2% | -64% | -89% | -87% |
| BNB | 3153 | 17 | 5% | 2% | -32% | -85% | -84% |
| DOGE | 3141 | 6 | 4% | 2% | -76% | -90% | -90% |
| ETH | 3135 | 12 | 7% | 3% | -53% | -85% | -85% |
| BTC | 3120 | 15 | 5% | 2% | -35% | -88% | -89% |
| NEAR | 3118 | 15 | 5% | 2% | -38% | -84% | -84% |
| XRP | 3111 | 12 | 3% | 1% | -52% | -89% | -89% |
| GOLD | 1697 | 5 | 5% | 2% | -64% | -81% | -83% |
| WTI | 1651 | 5 | 4% | 1% | -63% | -92% | -92% |
| SILVER | 1650 | 8 | 5% | 2% | -43% | -82% | -81% |
| PLATINUM | 1479 | 4 | 2% | 1% | -75% | -96% | -96% |
| EURUSD | 1422 | 3 | 2% | 1% | -80% | -89% | -89% |
| COPPER | 1393 | 6 | 2% | 1% | -60% | -70% | -70% |
| GBPUSD | 1349 | 3 | 2% | 1% | -79% | -96% | -96% |
| NATGAS | 1338 | 8 | 2% | 1% | -44% | -75% | -75% |
| USDJPY | 1330 | 5 | 2% | 1% | -65% | -97% | -96% |
| PALLADIUM | 1326 | 3 | 1% | 1% | -79% | -91% | -91% |
| AUDUSD | 877 | 4 | 2% | 1% | -57% | -86% | -86% |
| USDCAD | 851 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 439 | 0 | 1% | 1% | -100% | -98% | -96% |
| 10YRRATE | 260 | 1 | 5% | 2% | -64% | -56% | -54% |
| 30YRRATE | 244 | 0 | 2% | 1% | -100% | -96% | -95% |
| 2YRRATE | 243 | 2 | 3% | 0% | -23% | -17% | -17% |
| 5YRRATE | 225 | 1 | 4% | 2% | -59% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 23340 | 90 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 22692 | 79 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4542 | 22 | 2% | 1% | -15% | -83% | -82% |
| 0.05–0.1% | 4805 | 18 | 3% | 2% | -43% | -91% | -90% |
| 0.1–0.2% | 7283 | 25 | 5% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 8430 | 33 | 6% | 3% | -56% | -87% | -86% |
| Over 0.5% | 3190 | 13 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11276 | 40 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11422 | 50 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 10960 | 39 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 12374 | 40 | 3% | 2% | -63% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,686 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/4 8:14:45 PM | USDJPY | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 8:14:45 PM | BNB | DOWN | 14 sec | -0.061% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 8:14:29 PM | COPPER | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 8:14:29 PM | NEAR | DOWN | 30 sec | +0.146% | 0¢ | ❌ Lost | $0.00 |
| 11/4 8:14:29 PM | BTC | DOWN | 30 sec | +0.043% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 8:14:29 PM | AUDUSD | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 8:14:29 PM | DOGE | DOWN | 30 sec | +0.053% | 0¢ | ❌ Lost | $0.00 |
| 11/4 8:14:29 PM | SILVER | DOWN | 30 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/4 8:14:14 PM | EURUSD | DOWN | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 8:14:14 PM | ETH | DOWN | 45 sec | +0.070% | 0¢ | ❌ Lost | $0.00 |
| 11/4 8:14:14 PM | NATGAS | DOWN | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 8:14:14 PM | USDCAD | UP | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 8:14:14 PM | SOL | DOWN | 45 sec | +0.115% | 0¢ | ❌ Lost | $0.00 |
| 11/4 8:13:57 PM | PLATINUM | DOWN | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 8:13:41 PM | ZEC | UP | 78 sec | -0.311% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 8:13:41 PM | GOLD | DOWN | 78 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/4 8:13:25 PM | PALLADIUM | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 8:13:09 PM | XRP | DOWN | 1.9 min | +0.122% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 8:13:09 PM | BRENT | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 8:13:09 PM | WTI | DOWN | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/4 8:12:50 PM | HYPE | UP | 2.2 min | -0.304% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 8:10:37 PM | GBPUSD | DOWN | 4.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 7:59:58 PM | USDJPY | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 7:59:58 PM | PALLADIUM | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 7:59:42 PM | XRP | UP | 17 sec | -0.076% | 0¢ | ❌ Lost | $0.00 |
| 11/4 7:59:26 PM | NEAR | UP | 33 sec | -0.190% | 0¢ | ❌ Lost | -$0.15 |
| 11/4 7:59:26 PM | BTC | UP | 33 sec | -0.050% | 0¢ | ❌ Lost | $0.00 |
| 11/4 7:58:53 PM | GOLD | UP | 66 sec | — | 1¢ | ❌ Lost | $0.00 |
| 11/4 7:58:37 PM | ZEC | DOWN | 82 sec | +0.429% | 0¢ | ❌ Lost | $0.00 |
| 11/4 7:58:21 PM | ETH | UP | 1.6 min | -0.155% | 4¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
