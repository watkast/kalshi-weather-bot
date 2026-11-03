# 15-Minute 1¢ Study

*Updated Tue Nov 3, 1:07 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3575 finished bets | 1% | $118.55 | +30% | +3.32¢ | $67.55 / $51.00 |

*Expect about **98 buys a day** (~$14.67/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3314 | $45.25 | +13% |
| Volatility model ≥ 2%, hold to the close | 6611 | $40.20 | +5% |
| Momentum model ≥ 2%, hold to the close | 5457 | -$42.45 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 44126 | 44116 | 164 (0%) | 1.07% | -$3,075.65 (-57%) | Hold to the close: -$3,075.65 (-57%) |

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
| Volatility model | 27159 | 4.7% | 0.4% (106) | -683% | ❌ Worse |
| Momentum model | 27159 | 4.6% | 0.4% (106) | -708% | ❌ Worse |
| Mean-reversion model | 27159 | 8.1% | 0.4% (106) | -831% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 27159 | 106 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6611 | 60 | +5% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3575 | 37 | +30% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2029 | 22 | +55% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5457 | 42 | -7% | -81% | -81% | -77% |
| Momentum model ≥ 5% | 3314 | 29 | +13% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2164 | 19 | +23% | -74% | -74% | -69% |
| Mean-reversion model ≥ 2% | 11228 | 76 | -26% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7876 | 65 | -9% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 5269 | 46 | -1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 27363 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10428 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6325 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 44116 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 164 | 0% | -$3,075.65 | -57% | — |
| Sell at 2¢ | 1738 | 4% | -$4,681.77 | -87% | 47 sec |
| Sell at 3¢ | 1192 | 3% | -$4,668.77 | -87% | 48 sec |
| Sell at 5¢ | 826 | 2% | -$4,568.75 | -85% | 63 sec |
| Sell at 10¢ | 498 | 1% | -$4,369.27 | -81% | 66 sec |
| Sell at 25¢ | 261 | 1% | -$4,045.74 | -75% | 83 sec |
| Sell at 50¢ | 168 | 0% | -$3,677.65 | -68% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2123 | 9 | 11% | 4% | -60% | -81% | -82% |
| 2–5 min | 14164 | 78 | 7% | 4% | -46% | -86% | -86% |
| 1–2 min | 11148 | 39 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 16670 | 38 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3066 | 13 | 5% | 3% | -45% | -88% | -88% |
| SOL | 3058 | 11 | 4% | 2% | -55% | -90% | -90% |
| HYPE | 3053 | 9 | 5% | 2% | -63% | -89% | -87% |
| BNB | 3053 | 17 | 5% | 2% | -30% | -85% | -84% |
| DOGE | 3039 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 3036 | 11 | 7% | 3% | -56% | -85% | -85% |
| NEAR | 3022 | 15 | 5% | 2% | -36% | -84% | -84% |
| BTC | 3022 | 14 | 5% | 2% | -37% | -88% | -89% |
| XRP | 3014 | 12 | 3% | 1% | -51% | -89% | -88% |
| GOLD | 1619 | 5 | 5% | 2% | -63% | -81% | -83% |
| SILVER | 1577 | 7 | 5% | 2% | -47% | -82% | -81% |
| WTI | 1575 | 5 | 3% | 1% | -61% | -92% | -93% |
| PLATINUM | 1407 | 4 | 2% | 1% | -73% | -96% | -96% |
| EURUSD | 1350 | 3 | 2% | 1% | -79% | -89% | -89% |
| COPPER | 1331 | 6 | 2% | 1% | -58% | -69% | -69% |
| NATGAS | 1284 | 7 | 2% | 1% | -49% | -82% | -81% |
| GBPUSD | 1278 | 3 | 2% | 1% | -78% | -96% | -96% |
| PALLADIUM | 1262 | 3 | 1% | 1% | -78% | -90% | -91% |
| USDJPY | 1255 | 5 | 2% | 1% | -63% | -97% | -96% |
| AUDUSD | 810 | 4 | 2% | 1% | -54% | -86% | -85% |
| USDCAD | 769 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 373 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 236 | 1 | 5% | 2% | -60% | -52% | -49% |
| 30YRRATE | 220 | 0 | 1% | 0% | -100% | -98% | -96% |
| 2YRRATE | 211 | 2 | 4% | 0% | -12% | -5% | -4% |
| 5YRRATE | 196 | 1 | 5% | 2% | -52% | -91% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 22434 | 88 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 21682 | 76 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4453 | 21 | 2% | 1% | -18% | -83% | -82% |
| 0.05–0.1% | 4685 | 18 | 3% | 2% | -42% | -91% | -90% |
| 0.1–0.2% | 7089 | 24 | 4% | 2% | -58% | -90% | -89% |
| 0.2–0.5% | 8105 | 33 | 7% | 3% | -55% | -87% | -86% |
| Over 0.5% | 3024 | 12 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11048 | 40 | 4% | 2% | -59% | -87% | -87% |
| Morning (6am–12pm) | 11054 | 48 | 4% | 2% | -51% | -85% | -85% |
| Afternoon (12–6pm) | 10270 | 38 | 4% | 2% | -57% | -85% | -85% |
| Evening (6pm–12am) | 11744 | 38 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,718 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/3 12:59:48 PM | USDJPY | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 12:59:48 PM | 10YRRATE | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 12:59:33 PM | BTC | DOWN | 27 sec | +0.048% | 0¢ | ❌ Lost | $0.00 |
| 11/3 12:59:33 PM | ZEC | UP | 27 sec | -0.104% | 0¢ | ❌ Lost | -$0.15 |
| 11/3 12:59:33 PM | NEAR | DOWN | 27 sec | +0.107% | 0¢ | ❌ Lost | $0.00 |
| 11/3 12:59:33 PM | DOGE | DOWN | 27 sec | +0.043% | 0¢ | ❌ Lost | $0.00 |
| 11/3 12:59:14 PM | SOL | DOWN | 46 sec | +0.053% | 0¢ | ❌ Lost | -$0.15 |
| 11/3 12:59:14 PM | XRP | DOWN | 46 sec | +0.047% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 12:58:58 PM | HYPE | UP | 62 sec | -0.148% | 0¢ | ❌ Lost | $0.00 |
| 11/3 12:57:52 PM | NATGAS | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 12:57:36 PM | GOLD | UP | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 12:57:22 PM | PALLADIUM | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 12:57:22 PM | PLATINUM | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 12:57:22 PM | SILVER | UP | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 12:57:03 PM | BRENT | DOWN | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 12:55:59 PM | ETH | UP | 4.0 min | -0.194% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 12:55:10 PM | WTI | DOWN | 4.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 12:44:49 PM | BTC | UP | 11 sec | -0.008% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 12:44:33 PM | AUDUSD | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 12:44:33 PM | EURUSD | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 12:44:33 PM | COPPER | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 12:44:33 PM | WTI | DOWN | 27 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 12:44:18 PM | ETH | UP | 42 sec | -0.046% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 12:44:18 PM | 30YRRATE | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 12:44:18 PM | USDJPY | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 12:44:18 PM | NEAR | UP | 42 sec | -0.298% | 0¢ | ❌ Lost | $0.00 |
| 11/3 12:44:18 PM | 10YRRATE | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 12:43:58 PM | NATGAS | DOWN | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 12:43:42 PM | ZEC | UP | 77 sec | -0.251% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 12:43:42 PM | XRP | UP | 77 sec | -0.133% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
