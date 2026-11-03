# 15-Minute 1¢ Study

*Updated Mon Nov 2, 5:52 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3524 finished bets | 1% | $123.95 | +31% | +3.52¢ | $69.95 / $54.00 |

*Expect about **99 buys a day** (~$14.78/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3256 | $51.25 | +14% |
| Volatility model ≥ 2%, hold to the close | 6517 | $50.40 | +6% |
| Momentum model ≥ 2%, hold to the close | 5383 | -$34.95 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 43062 | 43052 | 159 (0%) | 1.07% | -$3,015.75 (-58%) | Hold to the close: -$3,015.75 (-58%) |

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
| Volatility model | 26685 | 4.7% | 0.4% (106) | -675% | ❌ Worse |
| Momentum model | 26685 | 4.6% | 0.4% (106) | -699% | ❌ Worse |
| Mean-reversion model | 26685 | 8.1% | 0.4% (106) | -822% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26685 | 106 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6517 | 60 | +6% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3524 | 37 | +31% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 1995 | 22 | +57% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 5383 | 42 | -6% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3256 | 29 | +14% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2125 | 19 | +25% | -74% | -73% | -69% |
| Mean-reversion model ≥ 2% | 11029 | 76 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7732 | 65 | -7% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 5170 | 46 | +1% | -80% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 26887 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 10134 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6031 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 43052 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 159 | 0% | -$3,015.75 | -58% | — |
| Sell at 2¢ | 1689 | 4% | -$4,578.61 | -87% | 47 sec |
| Sell at 3¢ | 1161 | 3% | -$4,564.96 | -87% | 48 sec |
| Sell at 5¢ | 807 | 2% | -$4,465.20 | -85% | 63 sec |
| Sell at 10¢ | 488 | 1% | -$4,280.47 | -82% | 65 sec |
| Sell at 25¢ | 255 | 1% | -$3,963.70 | -76% | 82 sec |
| Sell at 50¢ | 166 | 0% | -$3,603.25 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2065 | 9 | 11% | 4% | -59% | -81% | -82% |
| 2–5 min | 13831 | 75 | 7% | 4% | -47% | -87% | -86% |
| 1–2 min | 10869 | 38 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 16276 | 37 | 1% | 0% | -67% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3013 | 13 | 5% | 3% | -45% | -88% | -88% |
| SOL | 3004 | 11 | 4% | 2% | -54% | -91% | -91% |
| BNB | 3001 | 17 | 5% | 2% | -29% | -85% | -84% |
| HYPE | 2999 | 9 | 5% | 2% | -63% | -89% | -87% |
| DOGE | 2987 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 2984 | 11 | 6% | 3% | -55% | -85% | -85% |
| BTC | 2968 | 14 | 5% | 2% | -36% | -88% | -89% |
| NEAR | 2967 | 15 | 5% | 2% | -34% | -83% | -84% |
| XRP | 2964 | 12 | 3% | 1% | -50% | -89% | -89% |
| GOLD | 1575 | 5 | 5% | 2% | -62% | -81% | -83% |
| SILVER | 1535 | 7 | 5% | 2% | -46% | -82% | -82% |
| WTI | 1533 | 4 | 3% | 1% | -68% | -93% | -93% |
| PLATINUM | 1365 | 3 | 2% | 1% | -79% | -96% | -96% |
| EURUSD | 1305 | 3 | 2% | 1% | -79% | -89% | -88% |
| COPPER | 1301 | 5 | 2% | 1% | -64% | -76% | -75% |
| NATGAS | 1256 | 7 | 2% | 1% | -48% | -81% | -81% |
| GBPUSD | 1236 | 2 | 2% | 1% | -85% | -96% | -96% |
| PALLADIUM | 1231 | 2 | 1% | 0% | -85% | -90% | -91% |
| USDJPY | 1222 | 5 | 2% | 1% | -62% | -97% | -96% |
| AUDUSD | 763 | 4 | 2% | 1% | -51% | -85% | -84% |
| USDCAD | 730 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 338 | 0 | 1% | 1% | -100% | -97% | -96% |
| 10YRRATE | 210 | 1 | 5% | 2% | -56% | -46% | -44% |
| 30YRRATE | 198 | 0 | 2% | 0% | -100% | -97% | -96% |
| 2YRRATE | 191 | 2 | 4% | 1% | -2% | +5% | +6% |
| 5YRRATE | 176 | 1 | 6% | 2% | -47% | -90% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 21889 | 87 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 21163 | 72 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4375 | 21 | 2% | 1% | -16% | -82% | -82% |
| 0.05–0.1% | 4618 | 18 | 3% | 2% | -41% | -91% | -90% |
| 0.1–0.2% | 6961 | 24 | 4% | 2% | -57% | -90% | -90% |
| 0.2–0.5% | 7947 | 33 | 7% | 3% | -54% | -86% | -86% |
| Over 0.5% | 2981 | 12 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10646 | 37 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 10804 | 48 | 4% | 2% | -49% | -85% | -85% |
| Afternoon (12–6pm) | 10178 | 37 | 4% | 2% | -57% | -87% | -86% |
| Evening (6pm–12am) | 11424 | 37 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,762 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/2 5:44:49 PM | SOL | UP | 10 sec | -0.024% | 0¢ | ❌ Lost | $0.00 |
| 11/2 5:44:17 PM | BNB | UP | 42 sec | -0.096% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 5:44:01 PM | GOLD | UP | 58 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/2 5:44:01 PM | NEAR | UP | 58 sec | -0.396% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:44:01 PM | DOGE | UP | 58 sec | -0.090% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 5:44:01 PM | ZEC | UP | 58 sec | -0.292% | 0¢ | ❌ Lost | $0.00 |
| 11/2 5:44:01 PM | HYPE | UP | 58 sec | -0.183% | 0¢ | ❌ Lost | $0.00 |
| 11/2 5:44:01 PM | ETH | UP | 58 sec | -0.094% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:43:29 PM | BTC | DOWN | 1.5 min | +0.099% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 5:43:13 PM | BRENT | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:42:57 PM | PLATINUM | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:42:57 PM | COPPER | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:42:41 PM | USDJPY | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:42:41 PM | PALLADIUM | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:42:41 PM | WTI | DOWN | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 5:42:41 PM | SILVER | UP | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 5:42:16 PM | NATGAS | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:42:16 PM | USDCAD | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:42:16 PM | GBPUSD | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:41:59 PM | EURUSD | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:41:43 PM | AUDUSD | UP | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:40:06 PM | XRP | UP | 4.9 min | -0.280% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 5:29:45 PM | GBPUSD | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:29:45 PM | AUDUSD | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:29:45 PM | BRENT | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:29:45 PM | WTI | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:28:55 PM | NATGAS | DOWN | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:28:39 PM | HYPE | DOWN | 81 sec | +0.119% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 5:28:08 PM | SILVER | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:27:36 PM | NEAR | DOWN | 2.4 min | +0.165% | 2¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
