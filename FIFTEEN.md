# 15-Minute 1¢ Study

*Updated Tue Nov 10, 4:25 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4178 finished bets | 1% | $179.60 | +39% | +4.30¢ | $87.85 / $91.75 |

*Expect about **96 buys a day** (~$14.34/day at risk); max loss per buy **15¢**.*

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
| 52615 | 52595 | 201 (0%) | 1.07% | -$3,595.65 (-56%) | Hold to the close: -$3,595.65 (-56%) |

*In play or awaiting result: 12. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 31797 | 4.7% | 0.4% (128) | -678% | ❌ Worse |
| Momentum model | 31797 | 4.6% | 0.4% (128) | -702% | ❌ Worse |
| Mean-reversion model | 31797 | 8.1% | 0.4% (128) | -821% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 31797 | 128 | -49% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7651 | 70 | +6% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4178 | 46 | +39% | -72% | -70% | -66% |
| Volatility model ≥ 10% | 2406 | 28 | +67% | -62% | -60% | -57% |
| Momentum model ≥ 2% | 6351 | 51 | -2% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3899 | 37 | +23% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2557 | 25 | +37% | -65% | -65% | -60% |
| Mean-reversion model ≥ 2% | 13161 | 91 | -24% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9222 | 78 | -6% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6163 | 56 | +3% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 32002 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12490 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8103 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 52595 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 201 | 0% | -$3,595.65 | -56% | — |
| Sell at 2¢ | 2091 | 4% | -$5,585.99 | -87% | 47 sec |
| Sell at 3¢ | 1422 | 3% | -$5,575.07 | -87% | 48 sec |
| Sell at 5¢ | 988 | 2% | -$5,459.45 | -85% | 63 sec |
| Sell at 10¢ | 598 | 1% | -$5,234.27 | -82% | 65 sec |
| Sell at 25¢ | 316 | 1% | -$4,859.69 | -76% | 82 sec |
| Sell at 50¢ | 207 | 0% | -$4,410.40 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2633 | 12 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 16998 | 93 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 13273 | 44 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 19679 | 52 | 1% | 0% | -62% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3582 | 15 | 5% | 2% | -46% | -88% | -88% |
| SOL | 3579 | 16 | 4% | 2% | -43% | -86% | -86% |
| HYPE | 3572 | 11 | 5% | 2% | -61% | -89% | -88% |
| BNB | 3564 | 19 | 5% | 2% | -33% | -86% | -85% |
| DOGE | 3560 | 8 | 4% | 2% | -72% | -90% | -90% |
| ETH | 3554 | 15 | 7% | 3% | -48% | -82% | -81% |
| BTC | 3535 | 17 | 5% | 2% | -34% | -87% | -88% |
| NEAR | 3533 | 16 | 5% | 2% | -41% | -85% | -85% |
| XRP | 3523 | 13 | 3% | 1% | -54% | -89% | -89% |
| GOLD | 1887 | 5 | 5% | 2% | -68% | -81% | -83% |
| WTI | 1870 | 6 | 4% | 2% | -61% | -91% | -92% |
| SILVER | 1840 | 8 | 5% | 2% | -49% | -83% | -82% |
| PLATINUM | 1669 | 4 | 2% | 1% | -78% | -96% | -95% |
| EURUSD | 1608 | 5 | 2% | 1% | -71% | -90% | -89% |
| COPPER | 1563 | 6 | 2% | 1% | -64% | -73% | -73% |
| NATGAS | 1531 | 8 | 2% | 1% | -51% | -78% | -78% |
| GBPUSD | 1525 | 5 | 2% | 1% | -69% | -96% | -96% |
| USDJPY | 1507 | 6 | 2% | 1% | -63% | -97% | -96% |
| PALLADIUM | 1500 | 4 | 1% | 1% | -75% | -92% | -92% |
| AUDUSD | 1069 | 6 | 2% | 1% | -48% | -88% | -88% |
| USDCAD | 1037 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 630 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 353 | 2 | 4% | 2% | -47% | -66% | -64% |
| 2YRRATE | 338 | 4 | 4% | 2% | +10% | -38% | -36% |
| 30YRRATE | 332 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 311 | 2 | 4% | 2% | -40% | -93% | -95% |
| INX | 23 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 26659 | 105 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 25936 | 96 | 4% | 2% | -58% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5117 | 25 | 2% | 1% | -14% | -77% | -76% |
| 0.05–0.1% | 5456 | 20 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 8220 | 30 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 9565 | 40 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 3636 | 15 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12908 | 43 | 4% | 2% | -62% | -88% | -88% |
| Morning (6am–12pm) | 12871 | 58 | 4% | 2% | -49% | -85% | -84% |
| Afternoon (12–6pm) | 12699 | 57 | 4% | 2% | -47% | -86% | -86% |
| Evening (6pm–12am) | 14117 | 43 | 4% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,869 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/10 4:25:37 PM | NEAR | DOWN | 4.4 min | +0.564% | — | In play | — |
| 11/10 4:25:21 PM | XRP | DOWN | 4.7 min | +0.362% | — | In play | — |
| 11/10 4:25:05 PM | SOL | DOWN | 4.9 min | +0.313% | — | In play | — |
| 11/10 4:14:59 PM | ETH | DOWN | 0 sec | +0.015% | 0¢ | ❌ Lost | $0.00 |
| 11/10 4:14:59 PM | ZEC | UP | 0 sec | -0.025% | 0¢ | ❌ Lost | $0.00 |
| 11/10 4:14:43 PM | WTI | UP | 16 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/10 4:14:27 PM | HYPE | DOWN | 32 sec | +0.066% | 0¢ | ❌ Lost | $0.00 |
| 11/10 4:13:52 PM | NEAR | UP | 68 sec | -0.186% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 4:13:20 PM | NATGAS | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 4:13:05 PM | BRENT | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 4:13:05 PM | AUDUSD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 4:13:05 PM | EURUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 4:12:47 PM | GBPUSD | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 4:12:15 PM | USDJPY | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 4:10:37 PM | DOGE | UP | 4.4 min | -0.382% | 2¢ | ❌ Lost | -$0.15 |
| 11/10 4:10:37 PM | BNB | UP | 4.4 min | -0.183% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 4:10:37 PM | BTC | UP | 4.4 min | -0.177% | 20¢ | ❌ Lost | -$0.15 |
| 11/10 4:10:21 PM | SOL | UP | 4.7 min | -0.373% | 4¢ | ❌ Lost | -$0.15 |
| 11/10 4:09:34 PM | XRP | UP | 5.4 min | -0.530% | 1¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
