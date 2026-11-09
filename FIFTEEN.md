# 15-Minute 1¢ Study

*Updated Mon Nov 9, 7:45 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4104 finished bets | 1% | $187.55 | +41% | +4.57¢ | $91.90 / $95.65 |

*Expect about **97 buys a day** (~$14.54/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3809 | $105.50 | +26% |
| Volatility model ≥ 2%, hold to the close | 7511 | $75.65 | +8% |
| Momentum model ≥ 2%, hold to the close | 6204 | $1.20 | +0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 51072 | 51039 | 189 (0%) | 1.07% | -$3,566.70 (-57%) | Hold to the close: -$3,566.70 (-57%) |

*In play or awaiting result: 25. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 31110 | 4.8% | 0.4% (124) | -685% | ❌ Worse |
| Momentum model | 31110 | 4.6% | 0.4% (124) | -711% | ❌ Worse |
| Mean-reversion model | 31110 | 8.1% | 0.4% (124) | -828% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 31110 | 124 | -49% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7511 | 70 | +8% | -77% | -75% | -71% |
| Volatility model ≥ 5% | 4104 | 46 | +41% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2361 | 28 | +70% | -61% | -60% | -56% |
| Momentum model ≥ 2% | 6204 | 51 | +0% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3809 | 37 | +26% | -73% | -73% | -68% |
| Momentum model ≥ 10% | 2498 | 25 | +41% | -65% | -64% | -59% |
| Mean-reversion model ≥ 2% | 12869 | 90 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9023 | 77 | -5% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6031 | 56 | +6% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31315 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12048 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7676 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 51039 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 189 | 0% | -$3,566.70 | -57% | — |
| Sell at 2¢ | 2017 | 4% | -$5,408.28 | -87% | 47 sec |
| Sell at 3¢ | 1372 | 3% | -$5,397.62 | -87% | 48 sec |
| Sell at 5¢ | 958 | 2% | -$5,282.00 | -85% | 62 sec |
| Sell at 10¢ | 578 | 1% | -$5,063.52 | -82% | 65 sec |
| Sell at 25¢ | 301 | 1% | -$4,712.39 | -76% | 83 sec |
| Sell at 50¢ | 194 | 0% | -$4,301.20 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2529 | 12 | 11% | 4% | -55% | -81% | -82% |
| 2–5 min | 16495 | 88 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 12903 | 43 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 19100 | 46 | 1% | 0% | -66% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3510 | 15 | 5% | 2% | -45% | -88% | -88% |
| SOL | 3502 | 15 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3493 | 11 | 5% | 2% | -61% | -89% | -88% |
| BNB | 3487 | 19 | 5% | 2% | -31% | -86% | -85% |
| DOGE | 3485 | 7 | 4% | 2% | -75% | -90% | -90% |
| ETH | 3479 | 14 | 7% | 3% | -50% | -81% | -81% |
| NEAR | 3457 | 16 | 5% | 2% | -40% | -85% | -85% |
| BTC | 3456 | 16 | 5% | 2% | -36% | -87% | -89% |
| XRP | 3446 | 13 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1834 | 5 | 6% | 2% | -67% | -81% | -83% |
| WTI | 1803 | 6 | 4% | 1% | -60% | -92% | -92% |
| SILVER | 1783 | 8 | 5% | 2% | -47% | -82% | -82% |
| PLATINUM | 1616 | 4 | 2% | 1% | -77% | -96% | -95% |
| EURUSD | 1548 | 4 | 2% | 1% | -76% | -90% | -89% |
| COPPER | 1513 | 6 | 2% | 1% | -63% | -72% | -72% |
| NATGAS | 1475 | 8 | 2% | 1% | -49% | -77% | -77% |
| GBPUSD | 1469 | 4 | 2% | 1% | -75% | -96% | -96% |
| PALLADIUM | 1451 | 3 | 1% | 0% | -81% | -92% | -92% |
| USDJPY | 1451 | 5 | 2% | 1% | -68% | -97% | -96% |
| AUDUSD | 1010 | 5 | 2% | 1% | -54% | -87% | -87% |
| USDCAD | 976 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 573 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 325 | 1 | 4% | 2% | -71% | -64% | -62% |
| 2YRRATE | 306 | 3 | 4% | 1% | -8% | -32% | -31% |
| 30YRRATE | 302 | 0 | 2% | 1% | -100% | -97% | -95% |
| 5YRRATE | 282 | 1 | 4% | 1% | -67% | -93% | -95% |
| INX | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 25882 | 98 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 25157 | 91 | 4% | 2% | -58% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5057 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5350 | 19 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 8054 | 27 | 5% | 2% | -58% | -89% | -89% |
| 0.2–0.5% | 9336 | 40 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 3510 | 15 | 7% | 3% | -56% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12671 | 43 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12366 | 56 | 4% | 2% | -48% | -84% | -84% |
| Afternoon (12–6pm) | 12200 | 47 | 4% | 2% | -55% | -86% | -86% |
| Evening (6pm–12am) | 13802 | 43 | 4% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,918 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/9 7:44:48 AM | EURUSD | UP | 11 sec | — | 0¢ | In play | — |
| 11/9 7:44:48 AM | ETH | DOWN | 11 sec | +0.193% | 0¢ | ❌ Lost | $0.00 |
| 11/9 7:44:48 AM | XRP | DOWN | 11 sec | +0.265% | 0¢ | ❌ Lost | $0.00 |
| 11/9 7:44:32 AM | USDCAD | DOWN | 28 sec | — | 0¢ | In play | — |
| 11/9 7:44:32 AM | COPPER | DOWN | 28 sec | — | 0¢ | In play | — |
| 11/9 7:44:32 AM | GBPUSD | UP | 28 sec | — | 0¢ | In play | — |
| 11/9 7:44:32 AM | PALLADIUM | DOWN | 28 sec | — | 0¢ | In play | — |
| 11/9 7:44:32 AM | SOL | DOWN | 28 sec | +0.297% | 0¢ | ❌ Lost | $0.00 |
| 11/9 7:44:12 AM | BRENT | DOWN | 47 sec | — | 0¢ | In play | — |
| 11/9 7:44:12 AM | SILVER | DOWN | 47 sec | — | 0¢ | In play | — |
| 11/9 7:43:56 AM | 2YRRATE | DOWN | 63 sec | — | 0¢ | In play | — |
| 11/9 7:43:40 AM | NEAR | DOWN | 79 sec | +0.543% | 1¢ | In play | — |
| 11/9 7:43:40 AM | DOGE | DOWN | 79 sec | +0.266% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 7:43:25 AM | WTI | DOWN | 1.6 min | — | 0¢ | In play | — |
| 11/9 7:43:25 AM | 30YRRATE | DOWN | 1.6 min | — | 0¢ | In play | — |
| 11/9 7:43:25 AM | BNB | UP | 1.6 min | -0.228% | 85¢ | ✅ Won | $13.85 |
| 11/9 7:43:25 AM | 10YRRATE | DOWN | 1.6 min | — | 0¢ | In play | — |
| 11/9 7:43:06 AM | ZEC | UP | 1.9 min | -0.657% | 73¢ | ✅ Won | $13.85 |
| 11/9 7:42:50 AM | GOLD | UP | 2.2 min | — | 1¢ | In play | — |
| 11/9 7:42:19 AM | HYPE | DOWN | 2.7 min | +0.517% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 7:42:19 AM | BTC | UP | 2.7 min | -0.363% | 6¢ | ❌ Lost | -$0.15 |
| 11/9 7:41:12 AM | AUDUSD | DOWN | 3.8 min | — | 0¢ | In play | — |
| 11/9 7:40:06 AM | USDJPY | DOWN | 4.9 min | — | 0¢ | In play | — |
| 11/9 7:37:18 AM | 5YRRATE | DOWN | 7.7 min | — | 2¢ | In play | — |
| 11/9 7:29:59 AM | USDJPY | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 7:29:59 AM | 2YRRATE | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 7:29:59 AM | SILVER | UP | 0 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/9 7:29:43 AM | USDCAD | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 7:29:43 AM | AUDUSD | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 7:29:26 AM | GBPUSD | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
