# 15-Minute 1¢ Study

*Updated Wed Oct 28, 2:15 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3016 finished bets | 1% | $81.15 | +24% | +2.69¢ | $85.05 / -$3.90 |

*Expect about **99 buys a day** (~$14.80/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2800 | $43.10 | +14% |
| Volatility model ≥ 2%, hold to the close | 5583 | $6.50 | +1% |
| Momentum model ≥ 2%, hold to the close | 4617 | -$60.70 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 36891 | 36868 | 138 (0%) | 1.07% | -$2,566.20 (-57%) | Hold to the close: -$2,566.20 (-57%) |

*In play or awaiting result: 22. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 22955 | 4.7% | 0.4% (92) | -676% | ❌ Worse |
| Momentum model | 22955 | 4.6% | 0.4% (92) | -701% | ❌ Worse |
| Mean-reversion model | 22955 | 8.1% | 0.4% (92) | -820% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 22955 | 92 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5583 | 49 | +1% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 3016 | 30 | +24% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1709 | 19 | +58% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4617 | 34 | -11% | -81% | -80% | -78% |
| Momentum model ≥ 5% | 2800 | 25 | +14% | -78% | -77% | -74% |
| Momentum model ≥ 10% | 1836 | 17 | +28% | -72% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9382 | 63 | -27% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6578 | 53 | -11% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4397 | 38 | -2% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 23155 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8798 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4915 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 36868 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 138 | 0% | -$2,566.20 | -57% | — |
| Sell at 2¢ | 1406 | 4% | -$3,936.64 | -88% | 47 sec |
| Sell at 3¢ | 966 | 3% | -$3,925.46 | -87% | 48 sec |
| Sell at 5¢ | 670 | 2% | -$3,866.70 | -86% | 62 sec |
| Sell at 10¢ | 408 | 1% | -$3,711.72 | -83% | 65 sec |
| Sell at 25¢ | 218 | 1% | -$3,426.62 | -76% | 83 sec |
| Sell at 50¢ | 143 | 0% | -$3,098.95 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1643 | 8 | 11% | 4% | -54% | -80% | -81% |
| 2–5 min | 11771 | 66 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 9351 | 32 | 3% | 1% | -63% | -92% | -92% |
| Under 1 min | 14099 | 32 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2592 | 12 | 5% | 2% | -41% | -88% | -88% |
| HYPE | 2586 | 8 | 5% | 3% | -62% | -89% | -87% |
| BNB | 2585 | 15 | 5% | 2% | -27% | -85% | -84% |
| SOL | 2578 | 7 | 4% | 2% | -66% | -92% | -92% |
| ETH | 2573 | 11 | 7% | 3% | -48% | -85% | -85% |
| DOGE | 2571 | 5 | 4% | 2% | -76% | -90% | -90% |
| XRP | 2559 | 11 | 3% | 1% | -47% | -89% | -89% |
| BTC | 2556 | 13 | 5% | 2% | -32% | -88% | -89% |
| NEAR | 2555 | 12 | 5% | 2% | -39% | -82% | -82% |
| GOLD | 1389 | 5 | 4% | 2% | -57% | -82% | -83% |
| SILVER | 1360 | 6 | 4% | 2% | -48% | -82% | -81% |
| WTI | 1339 | 4 | 3% | 1% | -64% | -93% | -94% |
| PLATINUM | 1208 | 1 | 2% | 1% | -92% | -97% | -96% |
| COPPER | 1148 | 4 | 1% | 1% | -67% | -73% | -73% |
| EURUSD | 1129 | 3 | 2% | 1% | -75% | -88% | -88% |
| NATGAS | 1106 | 6 | 2% | 1% | -49% | -80% | -79% |
| PALLADIUM | 1070 | 2 | 1% | 0% | -83% | -89% | -90% |
| GBPUSD | 1070 | 2 | 2% | 1% | -83% | -96% | -96% |
| USDJPY | 1049 | 5 | 2% | 1% | -56% | -97% | -96% |
| AUDUSD | 609 | 4 | 1% | 1% | -39% | -82% | -81% |
| USDCAD | 574 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 178 | 0 | 1% | 1% | -100% | -99% | -99% |
| 10YRRATE | 129 | 0 | 4% | 1% | -100% | -93% | -92% |
| 30YRRATE | 122 | 0 | 1% | 0% | -100% | -99% | -98% |
| 2YRRATE | 120 | 1 | 4% | 1% | -22% | -15% | -14% |
| 5YRRATE | 113 | 1 | 5% | 3% | -17% | -91% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 18643 | 77 | 4% | 2% | -53% | -87% | -87% |
| DOWN (bought NO) | 18225 | 61 | 4% | 2% | -62% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3811 | 19 | 2% | 1% | -14% | -81% | -80% |
| 0.05–0.1% | 3985 | 14 | 3% | 2% | -48% | -92% | -91% |
| 0.1–0.2% | 6035 | 22 | 4% | 2% | -55% | -90% | -89% |
| 0.2–0.5% | 6806 | 29 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2514 | 10 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9229 | 35 | 4% | 2% | -57% | -86% | -86% |
| Morning (6am–12pm) | 9232 | 42 | 4% | 2% | -48% | -86% | -85% |
| Afternoon (12–6pm) | 8594 | 29 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 9813 | 32 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,554 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/28 2:14:47 PM | DOGE | DOWN | 13 sec | +0.095% | 0¢ | ❌ Lost | $0.00 |
| 10/28 2:14:47 PM | SILVER | UP | 13 sec | — | 0¢ | In play | — |
| 10/28 2:14:47 PM | BNB | DOWN | 13 sec | -0.015% | 0¢ | ❌ Lost | $0.00 |
| 10/28 2:14:31 PM | HYPE | UP | 29 sec | -0.122% | 0¢ | In play | — |
| 10/28 2:14:31 PM | ETH | UP | 29 sec | -0.047% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 2:14:31 PM | NEAR | UP | 29 sec | -0.306% | 0¢ | In play | — |
| 10/28 2:14:14 PM | NATGAS | DOWN | 45 sec | — | 0¢ | In play | — |
| 10/28 2:14:14 PM | USDCAD | DOWN | 45 sec | — | 0¢ | In play | — |
| 10/28 2:14:14 PM | XRP | UP | 45 sec | -0.210% | 0¢ | In play | — |
| 10/28 2:14:14 PM | BRENT | UP | 45 sec | — | 0¢ | In play | — |
| 10/28 2:13:58 PM | SOL | UP | 61 sec | -0.223% | 0¢ | In play | — |
| 10/28 2:13:42 PM | WTI | UP | 77 sec | — | 1¢ | In play | — |
| 10/28 2:13:42 PM | USDJPY | UP | 77 sec | — | 0¢ | In play | — |
| 10/28 2:13:26 PM | 10YRRATE | UP | 1.6 min | — | 0¢ | In play | — |
| 10/28 2:13:26 PM | GOLD | UP | 1.6 min | — | 1¢ | In play | — |
| 10/28 2:12:37 PM | BTC | UP | 2.4 min | -0.221% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 2:12:37 PM | 2YRRATE | UP | 2.4 min | — | 0¢ | In play | — |
| 10/28 2:09:55 PM | ZEC | DOWN | 5.1 min | +0.830% | 3¢ | In play | — |
| 10/28 2:08:50 PM | 5YRRATE | UP | 6.2 min | — | 4¢ | In play | — |
| 10/28 1:59:48 PM | AUDUSD | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 1:59:48 PM | WTI | UP | 11 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/28 1:59:16 PM | BRENT | UP | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 1:59:00 PM | COPPER | DOWN | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 1:58:44 PM | ZEC | DOWN | 75 sec | +0.160% | 0¢ | ❌ Lost | $0.00 |
| 10/28 1:58:28 PM | NATGAS | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 1:58:28 PM | PALLADIUM | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 1:57:54 PM | NEAR | DOWN | 2.1 min | +0.296% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 1:57:38 PM | HYPE | DOWN | 2.4 min | +0.245% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 1:57:38 PM | XRP | DOWN | 2.4 min | +0.278% | 0¢ | ❌ Lost | -$0.15 |
| 10/28 1:57:23 PM | GOLD | DOWN | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
