# 15-Minute 1¢ Study

*Updated Thu Oct 29, 1:58 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3091 finished bets | 1% | $87.35 | +25% | +2.83¢ | $80.85 / $6.50 |

*Expect about **98 buys a day** (~$14.70/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2868 | $36.05 | +11% |
| Volatility model ≥ 2%, hold to the close | 5726 | $4.60 | +1% |
| Volatility model ≥ 5%, sell at 50¢ | 3091 | -$66.90 | -19% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 38206 | 38181 | 141 (0%) | 1.07% | -$2,687.40 (-58%) | Hold to the close: -$2,687.40 (-58%) |

*In play or awaiting result: 24. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 23554 | 4.7% | 0.4% (93) | -679% | ❌ Worse |
| Momentum model | 23554 | 4.6% | 0.4% (93) | -702% | ❌ Worse |
| Mean-reversion model | 23554 | 8.0% | 0.4% (93) | -826% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 23554 | 93 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5726 | 50 | +1% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 3091 | 31 | +25% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1751 | 19 | +54% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4733 | 34 | -13% | -81% | -81% | -77% |
| Momentum model ≥ 5% | 2868 | 25 | +11% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1875 | 17 | +26% | -72% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9630 | 64 | -27% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6752 | 54 | -12% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4506 | 39 | -2% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 23755 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9166 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5260 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 38181 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 141 | 0% | -$2,687.40 | -58% | — |
| Sell at 2¢ | 1454 | 4% | -$4,087.36 | -88% | 47 sec |
| Sell at 3¢ | 1001 | 3% | -$4,075.01 | -87% | 48 sec |
| Sell at 5¢ | 697 | 2% | -$4,012.35 | -86% | 63 sec |
| Sell at 10¢ | 421 | 1% | -$3,857.89 | -83% | 65 sec |
| Sell at 25¢ | 224 | 1% | -$3,555.96 | -76% | 82 sec |
| Sell at 50¢ | 146 | 0% | -$3,227.90 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 8 | 0 | 38% | 25% | -100% | -35% | -3% |
| 5–10 min | 1748 | 8 | 11% | 4% | -56% | -80% | -81% |
| 2–5 min | 12164 | 68 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 9672 | 32 | 3% | 1% | -64% | -92% | -92% |
| Under 1 min | 14589 | 33 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2658 | 12 | 5% | 2% | -42% | -88% | -88% |
| HYPE | 2654 | 8 | 5% | 3% | -63% | -89% | -87% |
| BNB | 2652 | 15 | 4% | 2% | -29% | -85% | -84% |
| SOL | 2645 | 7 | 4% | 2% | -67% | -92% | -91% |
| DOGE | 2640 | 6 | 4% | 2% | -72% | -90% | -90% |
| ETH | 2639 | 11 | 6% | 3% | -49% | -85% | -85% |
| XRP | 2624 | 11 | 3% | 1% | -48% | -89% | -89% |
| BTC | 2622 | 13 | 5% | 2% | -34% | -88% | -89% |
| NEAR | 2621 | 12 | 5% | 2% | -40% | -82% | -82% |
| GOLD | 1441 | 5 | 4% | 2% | -58% | -82% | -84% |
| SILVER | 1410 | 6 | 4% | 2% | -50% | -82% | -81% |
| WTI | 1394 | 4 | 3% | 1% | -66% | -93% | -94% |
| PLATINUM | 1247 | 2 | 2% | 1% | -85% | -97% | -96% |
| COPPER | 1189 | 4 | 1% | 1% | -69% | -74% | -74% |
| EURUSD | 1184 | 3 | 2% | 1% | -76% | -88% | -88% |
| NATGAS | 1151 | 7 | 2% | 1% | -43% | -80% | -79% |
| GBPUSD | 1122 | 2 | 2% | 1% | -83% | -96% | -96% |
| PALLADIUM | 1114 | 2 | 1% | 0% | -83% | -90% | -90% |
| USDJPY | 1101 | 5 | 2% | 1% | -58% | -97% | -96% |
| AUDUSD | 656 | 4 | 1% | 1% | -43% | -84% | -83% |
| USDCAD | 620 | 0 | 2% | 0% | -100% | -97% | -97% |
| BRENT | 220 | 0 | 0% | 0% | -100% | -99% | -99% |
| 10YRRATE | 154 | 0 | 5% | 1% | -100% | -92% | -90% |
| 30YRRATE | 148 | 0 | 1% | 0% | -100% | -99% | -98% |
| 2YRRATE | 143 | 1 | 4% | 1% | -35% | -27% | -26% |
| 5YRRATE | 132 | 1 | 6% | 2% | -29% | -89% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 19366 | 77 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 18815 | 64 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3870 | 19 | 2% | 1% | -15% | -81% | -81% |
| 0.05–0.1% | 4081 | 14 | 3% | 2% | -49% | -92% | -92% |
| 0.1–0.2% | 6172 | 22 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 7017 | 30 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2611 | 10 | 7% | 3% | -61% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9458 | 35 | 4% | 2% | -58% | -86% | -86% |
| Morning (6am–12pm) | 9668 | 43 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 8893 | 29 | 4% | 2% | -62% | -88% | -88% |
| Evening (6pm–12am) | 10162 | 34 | 3% | 2% | -62% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,496 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/29 1:58:13 PM | PLATINUM | DOWN | 1.8 min | — | — | In play | — |
| 10/29 1:58:13 PM | 2YRRATE | DOWN | 1.8 min | — | — | In play | — |
| 10/29 1:58:13 PM | 30YRRATE | DOWN | 1.8 min | — | — | In play | — |
| 10/29 1:58:13 PM | 5YRRATE | DOWN | 1.8 min | — | — | In play | — |
| 10/29 1:58:13 PM | 10YRRATE | DOWN | 1.8 min | — | — | In play | — |
| 10/29 1:58:13 PM | GBPUSD | UP | 1.8 min | — | — | In play | — |
| 10/29 1:57:43 PM | XRP | UP | 2.3 min | -0.163% | — | In play | — |
| 10/29 1:57:11 PM | EURUSD | UP | 2.8 min | — | — | In play | — |
| 10/29 1:56:55 PM | GOLD | DOWN | 3.1 min | — | — | In play | — |
| 10/29 1:56:38 PM | HYPE | UP | 3.4 min | -0.418% | — | In play | — |
| 10/29 1:56:06 PM | USDJPY | DOWN | 3.9 min | — | — | In play | — |
| 10/29 1:55:36 PM | USDCAD | DOWN | 4.4 min | — | — | In play | — |
| 10/29 1:55:36 PM | BRENT | DOWN | 4.4 min | — | — | In play | — |
| 10/29 1:54:31 PM | SILVER | DOWN | 5.5 min | — | — | In play | — |
| 10/29 1:54:15 PM | WTI | DOWN | 5.8 min | — | — | In play | — |
| 10/29 1:44:51 PM | PALLADIUM | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 1:44:35 PM | NATGAS | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 1:44:35 PM | EURUSD | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 1:44:19 PM | HYPE | DOWN | 40 sec | +0.206% | 0¢ | ❌ Lost | $0.00 |
| 10/29 1:44:19 PM | USDCAD | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 1:44:19 PM | NEAR | UP | 40 sec | -0.255% | 0¢ | ❌ Lost | $0.00 |
| 10/29 1:44:02 PM | 2YRRATE | UP | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 1:44:02 PM | SOL | UP | 57 sec | -0.117% | 0¢ | ❌ Lost | -$0.15 |
| 10/29 1:44:02 PM | AUDUSD | DOWN | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 1:43:46 PM | PLATINUM | DOWN | 73 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 1:43:46 PM | BTC | DOWN | 73 sec | +0.056% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 1:43:46 PM | GOLD | DOWN | 73 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 1:42:40 PM | 5YRRATE | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 1:42:25 PM | 30YRRATE | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 1:42:25 PM | 10YRRATE | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
