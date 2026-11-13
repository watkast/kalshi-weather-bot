# 15-Minute 1¢ Study

*Updated Fri Nov 13, 3:05 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4294 finished bets | 1% | $167.30 | +35% | +3.90¢ | $80.05 / $87.25 |

*Expect about **92 buys a day** (~$13.81/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4036 | $94.45 | +22% |
| Volatility model ≥ 2%, hold to the close | 7939 | $24.05 | +3% |
| Momentum model ≥ 2%, hold to the close | 6590 | -$29.65 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 56446 | 56425 | 214 (0%) | 1.07% | -$3,890.95 (-56%) | Hold to the close: -$3,890.95 (-56%) |

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
| Volatility model | 33588 | 4.6% | 0.4% (135) | -663% | ❌ Worse |
| Momentum model | 33588 | 4.5% | 0.4% (135) | -689% | ❌ Worse |
| Mean-reversion model | 33588 | 8.0% | 0.4% (135) | -805% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 33588 | 135 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 7939 | 70 | +3% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4294 | 46 | +35% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 2485 | 28 | +62% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6590 | 52 | -4% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4036 | 38 | +22% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2645 | 25 | +33% | -66% | -66% | -61% |
| Mean-reversion model ≥ 2% | 13815 | 94 | -25% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 9635 | 79 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6424 | 56 | -1% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 33793 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 13622 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9010 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 56425 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 214 | 0% | -$3,890.95 | -56% | — |
| Sell at 2¢ | 2249 | 4% | -$6,008.21 | -87% | 47 sec |
| Sell at 3¢ | 1520 | 3% | -$6,000.15 | -87% | 48 sec |
| Sell at 5¢ | 1045 | 2% | -$5,885.70 | -85% | 63 sec |
| Sell at 10¢ | 635 | 1% | -$5,649.10 | -82% | 65 sec |
| Sell at 25¢ | 332 | 1% | -$5,256.03 | -76% | 82 sec |
| Sell at 50¢ | 219 | 0% | -$4,764.70 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2812 | 13 | 11% | 4% | -56% | -81% | -82% |
| 2–5 min | 18173 | 98 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 14227 | 47 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 21200 | 56 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3782 | 17 | 5% | 2% | -41% | -88% | -87% |
| SOL | 3780 | 17 | 4% | 2% | -43% | -86% | -87% |
| HYPE | 3773 | 11 | 5% | 2% | -63% | -89% | -88% |
| DOGE | 3759 | 8 | 4% | 2% | -73% | -90% | -90% |
| BNB | 3758 | 19 | 5% | 2% | -36% | -86% | -85% |
| ETH | 3754 | 16 | 7% | 3% | -47% | -81% | -81% |
| BTC | 3734 | 18 | 5% | 2% | -34% | -87% | -88% |
| NEAR | 3733 | 17 | 5% | 2% | -41% | -85% | -85% |
| XRP | 3720 | 14 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 2047 | 5 | 5% | 2% | -70% | -82% | -84% |
| WTI | 2020 | 7 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 1988 | 9 | 5% | 2% | -46% | -83% | -83% |
| PLATINUM | 1809 | 4 | 3% | 1% | -79% | -95% | -95% |
| EURUSD | 1754 | 6 | 3% | 1% | -68% | -90% | -90% |
| COPPER | 1699 | 6 | 2% | 1% | -67% | -75% | -75% |
| GBPUSD | 1679 | 6 | 2% | 1% | -67% | -96% | -96% |
| NATGAS | 1665 | 9 | 2% | 1% | -50% | -74% | -74% |
| USDJPY | 1646 | 6 | 2% | 1% | -66% | -97% | -96% |
| PALLADIUM | 1626 | 4 | 1% | 0% | -77% | -92% | -93% |
| AUDUSD | 1199 | 6 | 2% | 1% | -53% | -89% | -89% |
| USDCAD | 1162 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 768 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 401 | 2 | 4% | 1% | -53% | -70% | -68% |
| 2YRRATE | 384 | 4 | 4% | 2% | -3% | -45% | -43% |
| 30YRRATE | 376 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 355 | 2 | 4% | 2% | -47% | -93% | -95% |
| INX | 54 | 0 | 2% | 0% | -100% | -97% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 28674 | 110 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 27751 | 104 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5292 | 25 | 2% | 1% | -16% | -77% | -77% |
| 0.05–0.1% | 5691 | 20 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 8616 | 32 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 10258 | 42 | 6% | 3% | -54% | -87% | -86% |
| Over 0.5% | 3928 | 18 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13733 | 44 | 4% | 2% | -63% | -88% | -88% |
| Morning (6am–12pm) | 13638 | 63 | 4% | 2% | -48% | -85% | -85% |
| Afternoon (12–6pm) | 13690 | 60 | 4% | 2% | -49% | -86% | -87% |
| Evening (6pm–12am) | 15364 | 47 | 4% | 2% | -65% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,811 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/13 2:59:45 PM | 2YRRATE | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 2:59:45 PM | SOL | UP | 14 sec | -0.095% | 0¢ | ❌ Lost | -$0.15 |
| 11/13 2:59:28 PM | COPPER | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 2:58:55 PM | USDJPY | UP | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 2:58:39 PM | HYPE | DOWN | 80 sec | +0.157% | 0¢ | ❌ Lost | -$0.15 |
| 11/13 2:58:39 PM | DOGE | DOWN | 80 sec | +0.140% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 2:58:23 PM | EURUSD | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/13 2:58:23 PM | SILVER | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/13 2:57:49 PM | GOLD | DOWN | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/13 2:57:16 PM | BRENT | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 2:57:16 PM | ZEC | DOWN | 2.7 min | +0.404% | 4¢ | ❌ Lost | -$0.15 |
| 11/13 2:56:43 PM | NEAR | DOWN | 3.3 min | +0.440% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 2:56:10 PM | WTI | UP | 3.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/13 2:55:51 PM | ETH | DOWN | 4.2 min | +0.432% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 2:55:19 PM | XRP | DOWN | 4.7 min | +0.486% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 2:55:04 PM | BNB | DOWN | 4.9 min | +0.317% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 2:54:06 PM | BTC | DOWN | 5.9 min | +0.394% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 2:44:56 PM | USDJPY | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 2:44:41 PM | XRP | UP | 19 sec | -0.218% | 0¢ | ❌ Lost | $0.00 |
| 11/13 2:44:41 PM | USDCAD | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 2:44:41 PM | GOLD | DOWN | 19 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/13 2:43:50 PM | EURUSD | UP | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 2:43:34 PM | PALLADIUM | UP | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 2:43:34 PM | BRENT | DOWN | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 2:43:18 PM | 10YRRATE | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 2:43:18 PM | 30YRRATE | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 2:42:58 PM | SOL | UP | 2.0 min | -0.481% | 0¢ | ❌ Lost | $0.00 |
| 11/13 2:42:42 PM | HYPE | UP | 2.3 min | -0.467% | 0¢ | ❌ Lost | -$0.15 |
| 11/13 2:42:42 PM | 5YRRATE | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 2:42:26 PM | DOGE | UP | 2.5 min | -0.378% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
