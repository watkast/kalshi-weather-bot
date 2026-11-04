# 15-Minute 1¢ Study

*Updated Wed Nov 4, 4:31 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3660 finished bets | 1% | $123.70 | +30% | +3.38¢ | $77.05 / $46.65 |

*Expect about **97 buys a day** (~$14.56/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3394 | $51.45 | +14% |
| Volatility model ≥ 2%, hold to the close | 6786 | $33.95 | +4% |
| Momentum model ≥ 2%, hold to the close | 5593 | -$43.15 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 45764 | 45742 | 169 (0%) | 1.07% | -$3,210.85 (-58%) | Hold to the close: -$3,210.85 (-58%) |

*In play or awaiting result: 20. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 27923 | 4.7% | 0.4% (109) | -679% | ❌ Worse |
| Momentum model | 27923 | 4.6% | 0.4% (109) | -706% | ❌ Worse |
| Mean-reversion model | 27923 | 8.1% | 0.4% (109) | -828% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 27923 | 109 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6786 | 61 | +4% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3660 | 38 | +30% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2081 | 23 | +58% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5593 | 43 | -7% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 3394 | 30 | +14% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2215 | 19 | +20% | -75% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11566 | 79 | -25% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8119 | 68 | -7% | -81% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5442 | 48 | +0% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 28128 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10871 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6743 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 45742 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 169 | 0% | -$3,210.85 | -58% | — |
| Sell at 2¢ | 1800 | 4% | -$4,856.85 | -87% | 47 sec |
| Sell at 3¢ | 1230 | 3% | -$4,845.15 | -87% | 48 sec |
| Sell at 5¢ | 853 | 2% | -$4,742.40 | -85% | 63 sec |
| Sell at 10¢ | 514 | 1% | -$4,539.51 | -81% | 65 sec |
| Sell at 25¢ | 268 | 1% | -$4,213.77 | -76% | 83 sec |
| Sell at 50¢ | 172 | 0% | -$3,841.85 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2264 | 10 | 11% | 4% | -58% | -81% | -83% |
| 2–5 min | 14738 | 79 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 11511 | 39 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 17218 | 41 | 1% | 0% | -66% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3150 | 13 | 5% | 2% | -47% | -88% | -88% |
| SOL | 3146 | 12 | 4% | 2% | -52% | -90% | -90% |
| BNB | 3138 | 17 | 5% | 2% | -32% | -85% | -85% |
| HYPE | 3137 | 9 | 5% | 2% | -64% | -89% | -87% |
| DOGE | 3125 | 6 | 4% | 2% | -76% | -90% | -90% |
| ETH | 3120 | 12 | 7% | 3% | -53% | -85% | -85% |
| BTC | 3108 | 15 | 5% | 2% | -34% | -87% | -89% |
| NEAR | 3105 | 15 | 5% | 2% | -37% | -84% | -84% |
| XRP | 3099 | 12 | 3% | 1% | -52% | -89% | -89% |
| GOLD | 1684 | 5 | 5% | 2% | -64% | -81% | -83% |
| WTI | 1638 | 5 | 4% | 1% | -63% | -92% | -92% |
| SILVER | 1635 | 8 | 5% | 2% | -42% | -82% | -81% |
| PLATINUM | 1466 | 4 | 2% | 1% | -75% | -96% | -96% |
| EURUSD | 1412 | 3 | 2% | 1% | -80% | -89% | -89% |
| COPPER | 1381 | 6 | 2% | 1% | -59% | -70% | -70% |
| GBPUSD | 1336 | 3 | 2% | 1% | -79% | -96% | -96% |
| NATGAS | 1328 | 8 | 2% | 1% | -44% | -75% | -75% |
| USDJPY | 1320 | 5 | 2% | 1% | -65% | -97% | -96% |
| PALLADIUM | 1313 | 3 | 1% | 1% | -79% | -91% | -91% |
| AUDUSD | 865 | 4 | 2% | 1% | -57% | -86% | -86% |
| USDCAD | 838 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 426 | 0 | 1% | 1% | -100% | -98% | -96% |
| 10YRRATE | 260 | 1 | 5% | 2% | -64% | -56% | -54% |
| 30YRRATE | 244 | 0 | 2% | 1% | -100% | -96% | -95% |
| 2YRRATE | 243 | 2 | 3% | 0% | -23% | -17% | -17% |
| 5YRRATE | 225 | 1 | 4% | 2% | -59% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 23213 | 90 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 22529 | 79 | 4% | 2% | -60% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4526 | 22 | 2% | 1% | -15% | -83% | -82% |
| 0.05–0.1% | 4785 | 18 | 3% | 2% | -43% | -91% | -90% |
| 0.1–0.2% | 7247 | 25 | 4% | 2% | -57% | -90% | -89% |
| 0.2–0.5% | 8379 | 33 | 6% | 3% | -56% | -87% | -86% |
| Over 0.5% | 3183 | 13 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11276 | 40 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11422 | 50 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 10841 | 39 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 12203 | 40 | 3% | 2% | -62% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,687 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/4 4:29:57 PM | BRENT | UP | 3 sec | — | 0¢ | In play | — |
| 11/4 4:29:41 PM | BNB | UP | 19 sec | -0.107% | 0¢ | ❌ Lost | $0.00 |
| 11/4 4:29:41 PM | XRP | UP | 19 sec | -0.061% | 0¢ | ❌ Lost | $0.00 |
| 11/4 4:29:41 PM | GBPUSD | DOWN | 19 sec | — | 0¢ | In play | — |
| 11/4 4:29:41 PM | WTI | UP | 19 sec | — | 0¢ | In play | — |
| 11/4 4:29:41 PM | DOGE | UP | 19 sec | -0.067% | 0¢ | In play | — |
| 11/4 4:29:41 PM | EURUSD | DOWN | 19 sec | — | 0¢ | In play | — |
| 11/4 4:29:25 PM | NEAR | UP | 35 sec | -0.267% | 0¢ | ❌ Lost | $0.00 |
| 11/4 4:29:10 PM | ETH | UP | 49 sec | -0.091% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 4:29:10 PM | AUDUSD | DOWN | 49 sec | — | 0¢ | In play | — |
| 11/4 4:29:10 PM | SOL | UP | 49 sec | -0.075% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 4:29:10 PM | COPPER | DOWN | 49 sec | — | 0¢ | In play | — |
| 11/4 4:28:38 PM | GOLD | DOWN | 81 sec | — | 0¢ | In play | — |
| 11/4 4:28:22 PM | ZEC | UP | 1.6 min | -0.350% | 0¢ | In play | — |
| 11/4 4:27:49 PM | HYPE | UP | 2.2 min | -0.358% | 0¢ | In play | — |
| 11/4 4:27:49 PM | SILVER | DOWN | 2.2 min | — | 1¢ | In play | — |
| 11/4 4:14:45 PM | USDCAD | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 4:14:29 PM | USDJPY | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 4:14:13 PM | GBPUSD | DOWN | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 4:14:13 PM | WTI | DOWN | 47 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/4 4:12:37 PM | EURUSD | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 4:11:17 PM | HYPE | UP | 3.7 min | -0.535% | 0¢ | ❌ Lost | -$0.15 |
| 11/4 4:10:46 PM | XRP | UP | 4.2 min | -0.320% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 4:10:46 PM | DOGE | UP | 4.2 min | -0.437% | 0¢ | ❌ Lost | -$0.15 |
| 11/4 4:10:22 PM | SOL | UP | 4.6 min | -0.527% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 4:09:33 PM | ZEC | UP | 5.5 min | -0.883% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 4:09:33 PM | NEAR | UP | 5.5 min | -0.858% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 4:09:17 PM | ETH | UP | 5.7 min | -0.315% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 4:09:01 PM | BTC | UP | 6.0 min | -0.372% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 4:09:01 PM | BNB | UP | 6.0 min | -0.413% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
