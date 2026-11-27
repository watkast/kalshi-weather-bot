# 15-Minute 1¢ Study

*Updated Thu Nov 26, 11:41 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4985 finished bets | 1% | $201.25 | +37% | +4.04¢ | $96.15 / $105.10 |

*Expect about **83 buys a day** (~$12.47/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4726 | $101.15 | +20% |
| Volatility model ≥ 2%, hold to the close | 9296 | $29.25 | +3% |
| Momentum model ≥ 2%, hold to the close | 7740 | -$49.70 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 69062 | 69024 | 257 (0%) | 1.07% | -$4,758.35 (-57%) | Hold to the close: -$4,758.35 (-57%) |

*In play or awaiting result: 10. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 40772 | 4.5% | 0.4% (165) | -659% | ❌ Worse |
| Momentum model | 40772 | 4.4% | 0.4% (165) | -682% | ❌ Worse |
| Mean-reversion model | 40772 | 7.9% | 0.4% (165) | -799% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 40772 | 165 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 9296 | 81 | +3% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 4985 | 53 | +37% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 2893 | 32 | +65% | -65% | -64% | -60% |
| Momentum model ≥ 2% | 7740 | 59 | -6% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 4726 | 43 | +20% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 3084 | 28 | +32% | -68% | -68% | -64% |
| Mean-reversion model ≥ 2% | 16627 | 113 | -25% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11579 | 93 | -10% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7682 | 66 | -2% | -78% | -78% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 40978 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 16501 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 11545 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 69024 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 257 | 0% | -$4,758.35 | -57% | — |
| Sell at 2¢ | 2829 | 4% | -$7,312.81 | -88% | 47 sec |
| Sell at 3¢ | 1901 | 3% | -$7,306.96 | -87% | 48 sec |
| Sell at 5¢ | 1287 | 2% | -$7,183.80 | -86% | 62 sec |
| Sell at 10¢ | 786 | 1% | -$6,906.69 | -83% | 65 sec |
| Sell at 25¢ | 425 | 1% | -$6,375.60 | -76% | 80 sec |
| Sell at 50¢ | 271 | 0% | -$5,771.10 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3579 | 17 | 10% | 4% | -55% | -82% | -83% |
| 2–5 min | 22392 | 116 | 7% | 3% | -49% | -86% | -86% |
| 1–2 min | 17171 | 58 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 25869 | 66 | 1% | 0% | -63% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4584 | 20 | 5% | 2% | -42% | -87% | -87% |
| HYPE | 4575 | 16 | 5% | 2% | -55% | -89% | -88% |
| SOL | 4568 | 20 | 4% | 2% | -43% | -86% | -86% |
| BNB | 4561 | 22 | 5% | 2% | -38% | -86% | -85% |
| DOGE | 4559 | 12 | 4% | 2% | -66% | -89% | -89% |
| ETH | 4554 | 19 | 7% | 3% | -47% | -82% | -82% |
| BTC | 4531 | 24 | 5% | 2% | -27% | -86% | -88% |
| NEAR | 4527 | 18 | 5% | 2% | -48% | -86% | -86% |
| XRP | 4519 | 16 | 4% | 2% | -55% | -88% | -88% |
| GOLD | 2437 | 8 | 5% | 2% | -60% | -83% | -84% |
| WTI | 2421 | 9 | 4% | 2% | -54% | -86% | -87% |
| SILVER | 2385 | 9 | 5% | 2% | -55% | -83% | -83% |
| PLATINUM | 2161 | 5 | 3% | 1% | -78% | -95% | -95% |
| EURUSD | 2113 | 7 | 2% | 1% | -69% | -91% | -91% |
| GBPUSD | 2059 | 8 | 2% | 1% | -64% | -96% | -96% |
| COPPER | 2045 | 6 | 2% | 1% | -73% | -79% | -79% |
| USDJPY | 2009 | 6 | 2% | 1% | -72% | -97% | -96% |
| NATGAS | 1998 | 10 | 2% | 1% | -53% | -77% | -77% |
| PALLADIUM | 1947 | 4 | 1% | 1% | -81% | -93% | -93% |
| AUDUSD | 1583 | 7 | 2% | 1% | -59% | -90% | -90% |
| USDCAD | 1489 | 1 | 3% | 1% | -94% | -95% | -95% |
| BRENT | 1107 | 1 | 2% | 1% | -92% | -96% | -96% |
| 10YRRATE | 557 | 2 | 3% | 1% | -66% | -78% | -76% |
| 30YRRATE | 518 | 0 | 3% | 1% | -100% | -95% | -93% |
| 2YRRATE | 515 | 4 | 4% | 2% | -28% | -57% | -57% |
| 5YRRATE | 506 | 2 | 4% | 2% | -63% | -94% | -95% |
| INX | 139 | 1 | 2% | 1% | -33% | -96% | -96% |
| USDMXN | 57 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 35160 | 133 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 33864 | 124 | 4% | 2% | -58% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5941 | 25 | 2% | 1% | -22% | -79% | -78% |
| 0.05–0.1% | 6507 | 26 | 3% | 2% | -36% | -91% | -91% |
| 0.1–0.2% | 10144 | 36 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 12924 | 56 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 5453 | 24 | 7% | 3% | -54% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16499 | 51 | 4% | 2% | -65% | -87% | -88% |
| Morning (6am–12pm) | 16354 | 82 | 4% | 2% | -43% | -86% | -85% |
| Afternoon (12–6pm) | 16940 | 73 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 19231 | 51 | 4% | 2% | -69% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,081 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/26 11:40:31 PM | EURUSD | UP | 4.5 min | — | — | In play | — |
| 11/26 11:40:15 PM | AUDUSD | UP | 4.8 min | — | — | In play | — |
| 11/26 11:39:56 PM | NEAR | UP | 5.1 min | -0.760% | — | In play | — |
| 11/26 11:39:56 PM | ZEC | UP | 5.1 min | -0.971% | — | In play | — |
| 11/26 11:29:57 PM | NATGAS | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 11:29:42 PM | GBPUSD | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 11:29:24 PM | WTI | UP | 36 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/26 11:29:24 PM | PLATINUM | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 11:29:24 PM | GOLD | DOWN | 36 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/26 11:29:08 PM | HYPE | UP | 52 sec | -0.197% | 0¢ | ❌ Lost | -$0.15 |
| 11/26 11:29:08 PM | XRP | UP | 52 sec | -0.093% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 11:28:52 PM | SILVER | DOWN | 68 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/26 11:28:52 PM | COPPER | DOWN | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 11:28:52 PM | USDCAD | UP | 68 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/26 11:28:52 PM | BRENT | UP | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 11:28:35 PM | EURUSD | DOWN | 84 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 11:28:16 PM | NEAR | UP | 1.7 min | -0.384% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 11:27:28 PM | AUDUSD | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 11:27:09 PM | DOGE | UP | 2.8 min | -0.249% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 11:26:21 PM | BTC | UP | 3.6 min | -0.368% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 11:26:21 PM | ETH | UP | 3.6 min | -0.348% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 11:26:02 PM | SOL | UP | 4.0 min | -0.341% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 11:25:30 PM | BNB | UP | 4.5 min | -0.365% | 2¢ | ❌ Lost | -$0.15 |
| 11/26 11:24:23 PM | ZEC | UP | 5.6 min | -1.080% | 0¢ | ❌ Lost | -$0.15 |
| 11/26 11:14:45 PM | NEAR | UP | 15 sec | -0.173% | 0¢ | ❌ Lost | -$0.15 |
| 11/26 11:14:45 PM | SILVER | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 11:14:26 PM | AUDUSD | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 11:14:26 PM | USDJPY | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 11:14:26 PM | GOLD | DOWN | 33 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/26 11:14:10 PM | ZEC | DOWN | 49 sec | +0.195% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
