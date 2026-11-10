# 15-Minute 1¢ Study

*Updated Tue Nov 10, 4:04 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4178 finished bets | 1% | $179.60 | +39% | +4.30¢ | $87.85 / $91.75 |

*Expect about **96 buys a day** (~$14.35/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3899 | $95.60 | +23% |
| Volatility model ≥ 2%, hold to the close | 7651 | $59.00 | +6% |
| Momentum model ≥ 2%, hold to the close | 6351 | -$15.75 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 52596 | 52579 | 201 (0%) | 1.07% | -$3,593.70 (-56%) | Hold to the close: -$3,593.70 (-56%) |

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
| Volatility model | 31788 | 4.8% | 0.4% (128) | -678% | ❌ Worse |
| Momentum model | 31788 | 4.6% | 0.4% (128) | -702% | ❌ Worse |
| Mean-reversion model | 31788 | 8.1% | 0.4% (128) | -821% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 31788 | 128 | -49% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7651 | 70 | +6% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4178 | 46 | +39% | -72% | -70% | -66% |
| Volatility model ≥ 10% | 2406 | 28 | +67% | -62% | -60% | -57% |
| Momentum model ≥ 2% | 6351 | 51 | -2% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3899 | 37 | +23% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2557 | 25 | +37% | -65% | -65% | -60% |
| Mean-reversion model ≥ 2% | 13157 | 91 | -24% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9219 | 78 | -6% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6160 | 56 | +3% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31993 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12487 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8099 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 52579 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 201 | 0% | -$3,593.70 | -56% | — |
| Sell at 2¢ | 2089 | 4% | -$5,584.56 | -87% | 47 sec |
| Sell at 3¢ | 1420 | 3% | -$5,573.90 | -87% | 48 sec |
| Sell at 5¢ | 987 | 2% | -$5,458.15 | -85% | 63 sec |
| Sell at 10¢ | 597 | 1% | -$5,233.63 | -82% | 65 sec |
| Sell at 25¢ | 316 | 1% | -$4,857.74 | -76% | 82 sec |
| Sell at 50¢ | 207 | 0% | -$4,408.45 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2632 | 12 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 16992 | 93 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 13268 | 44 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 19675 | 52 | 1% | 0% | -62% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3581 | 15 | 5% | 2% | -46% | -88% | -88% |
| SOL | 3578 | 16 | 4% | 2% | -43% | -87% | -86% |
| HYPE | 3571 | 11 | 5% | 2% | -61% | -89% | -88% |
| BNB | 3563 | 19 | 5% | 2% | -33% | -86% | -85% |
| DOGE | 3559 | 8 | 4% | 2% | -72% | -90% | -90% |
| ETH | 3553 | 15 | 7% | 3% | -48% | -82% | -81% |
| BTC | 3534 | 17 | 5% | 2% | -34% | -87% | -88% |
| NEAR | 3532 | 16 | 5% | 2% | -41% | -85% | -85% |
| XRP | 3522 | 13 | 3% | 1% | -54% | -89% | -89% |
| GOLD | 1887 | 5 | 5% | 2% | -68% | -81% | -83% |
| WTI | 1869 | 6 | 4% | 2% | -61% | -91% | -92% |
| SILVER | 1840 | 8 | 5% | 2% | -49% | -83% | -82% |
| PLATINUM | 1669 | 4 | 2% | 1% | -78% | -96% | -95% |
| EURUSD | 1607 | 5 | 2% | 1% | -71% | -90% | -89% |
| COPPER | 1563 | 6 | 2% | 1% | -64% | -73% | -73% |
| NATGAS | 1530 | 8 | 2% | 1% | -51% | -78% | -78% |
| GBPUSD | 1524 | 5 | 2% | 1% | -69% | -96% | -96% |
| USDJPY | 1506 | 6 | 2% | 1% | -63% | -97% | -96% |
| PALLADIUM | 1500 | 4 | 1% | 1% | -75% | -92% | -92% |
| AUDUSD | 1068 | 6 | 2% | 1% | -48% | -88% | -88% |
| USDCAD | 1037 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 629 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 353 | 2 | 4% | 2% | -47% | -66% | -64% |
| 2YRRATE | 338 | 4 | 4% | 2% | +10% | -38% | -36% |
| 30YRRATE | 332 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 311 | 2 | 4% | 2% | -40% | -93% | -95% |
| INX | 23 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 26647 | 105 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 25932 | 96 | 4% | 2% | -58% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5115 | 25 | 2% | 1% | -14% | -77% | -76% |
| 0.05–0.1% | 5455 | 20 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 8217 | 30 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 9563 | 40 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 3635 | 15 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12908 | 43 | 4% | 2% | -62% | -88% | -88% |
| Morning (6am–12pm) | 12871 | 58 | 4% | 2% | -49% | -85% | -84% |
| Afternoon (12–6pm) | 12683 | 57 | 4% | 2% | -47% | -86% | -86% |
| Evening (6pm–12am) | 14117 | 43 | 4% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,869 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/10 3:59:57 PM | USDJPY | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 3:59:57 PM | USDCAD | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 3:59:57 PM | NATGAS | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 3:59:57 PM | AUDUSD | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 3:59:57 PM | EURUSD | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 3:59:25 PM | WTI | UP | 35 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/10 3:59:25 PM | XRP | DOWN | 35 sec | +0.028% | 0¢ | ❌ Lost | $0.00 |
| 11/10 3:59:09 PM | BNB | UP | 51 sec | -0.021% | 0¢ | ❌ Lost | $0.00 |
| 11/10 3:58:54 PM | ETH | UP | 66 sec | -0.088% | 0¢ | ❌ Lost | $0.00 |
| 11/10 3:58:54 PM | HYPE | UP | 66 sec | -0.145% | 0¢ | ❌ Lost | $0.00 |
| 11/10 3:58:54 PM | BTC | UP | 66 sec | -0.062% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 3:58:38 PM | SOL | UP | 82 sec | -0.096% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 3:58:22 PM | DOGE | UP | 1.6 min | -0.175% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 3:56:32 PM | NEAR | UP | 3.5 min | -0.579% | 0¢ | ❌ Lost | -$0.15 |
| 11/10 3:55:44 PM | ZEC | UP | 4.3 min | -0.676% | 0¢ | ❌ Lost | -$0.15 |
| 11/10 3:44:53 PM | GBPUSD | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 3:44:53 PM | NATGAS | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 3:44:53 PM | NEAR | DOWN | 7 sec | +0.011% | 0¢ | ❌ Lost | $0.00 |
| 11/10 3:44:22 PM | DOGE | DOWN | 38 sec | +0.010% | 0¢ | ❌ Lost | -$0.15 |
| 11/10 3:44:22 PM | EURUSD | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 3:43:56 PM | ZEC | DOWN | 63 sec | +0.343% | 0¢ | ❌ Lost | $0.00 |
| 11/10 3:43:24 PM | ETH | UP | 1.6 min | -0.099% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 3:43:24 PM | SOL | UP | 1.6 min | -0.204% | 0¢ | ❌ Lost | $0.00 |
| 11/10 3:43:08 PM | BRENT | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 3:42:50 PM | BNB | DOWN | 2.1 min | +0.086% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 3:42:18 PM | HYPE | UP | 2.7 min | -0.312% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 3:40:06 PM | BTC | DOWN | 4.9 min | +0.210% | 2¢ | ❌ Lost | -$0.15 |
| 11/10 3:39:19 PM | XRP | UP | 5.7 min | -0.481% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 3:29:57 PM | NATGAS | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 3:29:41 PM | WTI | DOWN | 18 sec | — | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
