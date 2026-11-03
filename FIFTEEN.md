# 15-Minute 1¢ Study

*Updated Mon Nov 2, 5:42 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3524 finished bets | 1% | $123.95 | +31% | +3.52¢ | $69.95 / $54.00 |

*Expect about **99 buys a day** (~$14.79/day at risk); max loss per buy **15¢**.*

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
| 43046 | 43030 | 159 (0%) | 1.07% | -$3,013.05 (-58%) | Hold to the close: -$3,013.05 (-58%) |

*In play or awaiting result: 15. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 26676 | 4.7% | 0.4% (106) | -675% | ❌ Worse |
| Momentum model | 26676 | 4.6% | 0.4% (106) | -699% | ❌ Worse |
| Mean-reversion model | 26676 | 8.1% | 0.4% (106) | -823% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26676 | 106 | -50% | -88% | -87% | -85% |
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
| Crypto | 26878 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 10126 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6026 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 43030 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 159 | 0% | -$3,013.05 | -58% | — |
| Sell at 2¢ | 1689 | 4% | -$4,575.91 | -87% | 47 sec |
| Sell at 3¢ | 1161 | 3% | -$4,562.26 | -87% | 48 sec |
| Sell at 5¢ | 807 | 2% | -$4,462.50 | -85% | 63 sec |
| Sell at 10¢ | 488 | 1% | -$4,277.77 | -82% | 65 sec |
| Sell at 25¢ | 255 | 1% | -$3,961.00 | -76% | 82 sec |
| Sell at 50¢ | 166 | 0% | -$3,600.55 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2065 | 9 | 11% | 4% | -59% | -81% | -82% |
| 2–5 min | 13819 | 75 | 7% | 4% | -46% | -87% | -86% |
| 1–2 min | 10867 | 38 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 16268 | 37 | 1% | 0% | -67% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3012 | 13 | 5% | 3% | -45% | -88% | -88% |
| SOL | 3003 | 11 | 4% | 2% | -54% | -91% | -91% |
| BNB | 3000 | 17 | 5% | 2% | -29% | -85% | -84% |
| HYPE | 2998 | 9 | 5% | 2% | -63% | -89% | -87% |
| DOGE | 2986 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 2983 | 11 | 6% | 3% | -55% | -85% | -85% |
| BTC | 2967 | 14 | 5% | 2% | -36% | -88% | -89% |
| NEAR | 2966 | 15 | 5% | 2% | -34% | -83% | -84% |
| XRP | 2963 | 12 | 3% | 1% | -50% | -89% | -89% |
| GOLD | 1574 | 5 | 5% | 2% | -62% | -81% | -83% |
| SILVER | 1534 | 7 | 5% | 2% | -46% | -82% | -82% |
| WTI | 1532 | 4 | 3% | 1% | -68% | -93% | -93% |
| PLATINUM | 1364 | 3 | 2% | 1% | -79% | -96% | -96% |
| EURUSD | 1304 | 3 | 2% | 1% | -79% | -89% | -88% |
| COPPER | 1300 | 5 | 2% | 1% | -64% | -76% | -75% |
| NATGAS | 1255 | 7 | 2% | 1% | -48% | -81% | -81% |
| GBPUSD | 1235 | 2 | 2% | 1% | -85% | -96% | -96% |
| PALLADIUM | 1230 | 2 | 1% | 0% | -85% | -90% | -91% |
| USDJPY | 1221 | 5 | 2% | 1% | -62% | -97% | -96% |
| AUDUSD | 762 | 4 | 2% | 1% | -51% | -85% | -84% |
| USDCAD | 729 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 337 | 0 | 1% | 1% | -100% | -97% | -96% |
| 10YRRATE | 210 | 1 | 5% | 2% | -56% | -46% | -44% |
| 30YRRATE | 198 | 0 | 2% | 0% | -100% | -97% | -96% |
| 2YRRATE | 191 | 2 | 4% | 1% | -2% | +5% | +6% |
| 5YRRATE | 176 | 1 | 6% | 2% | -47% | -90% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 21873 | 87 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 21157 | 72 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4374 | 21 | 2% | 1% | -16% | -82% | -82% |
| 0.05–0.1% | 4614 | 18 | 3% | 2% | -41% | -91% | -90% |
| 0.1–0.2% | 6960 | 24 | 4% | 2% | -57% | -90% | -90% |
| 0.2–0.5% | 7944 | 33 | 7% | 3% | -54% | -86% | -86% |
| Over 0.5% | 2981 | 12 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10646 | 37 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 10804 | 48 | 4% | 2% | -49% | -85% | -85% |
| Afternoon (12–6pm) | 10156 | 37 | 4% | 2% | -57% | -87% | -86% |
| Evening (6pm–12am) | 11424 | 37 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,766 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/2 5:42:16 PM | NATGAS | DOWN | 2.7 min | — | — | In play | — |
| 11/2 5:42:16 PM | USDCAD | DOWN | 2.7 min | — | — | In play | — |
| 11/2 5:42:16 PM | GBPUSD | UP | 2.7 min | — | — | In play | — |
| 11/2 5:41:59 PM | EURUSD | UP | 3.0 min | — | — | In play | — |
| 11/2 5:41:43 PM | AUDUSD | UP | 3.3 min | — | — | In play | — |
| 11/2 5:40:06 PM | XRP | UP | 4.9 min | -0.280% | — | In play | — |
| 11/2 5:29:45 PM | GBPUSD | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:29:45 PM | AUDUSD | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:29:45 PM | BRENT | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:29:45 PM | WTI | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:28:55 PM | NATGAS | DOWN | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:28:39 PM | HYPE | DOWN | 81 sec | +0.119% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 5:28:08 PM | SILVER | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:27:36 PM | NEAR | DOWN | 2.4 min | +0.165% | 2¢ | ❌ Lost | -$0.15 |
| 11/2 5:26:01 PM | BTC | DOWN | 4.0 min | +0.260% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 5:26:01 PM | PLATINUM | DOWN | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:25:46 PM | PALLADIUM | DOWN | 4.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 5:25:14 PM | XRP | DOWN | 4.8 min | +0.280% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 5:24:27 PM | BNB | DOWN | 5.5 min | +0.190% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 5:24:11 PM | SOL | DOWN | 5.8 min | +0.373% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 5:23:40 PM | GOLD | DOWN | 6.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 5:23:40 PM | ETH | DOWN | 6.3 min | +0.278% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 5:23:08 PM | DOGE | DOWN | 6.9 min | +0.312% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 5:22:36 PM | ZEC | DOWN | 7.4 min | +1.300% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 5:14:48 PM | DOGE | UP | 12 sec | -0.080% | 0¢ | ❌ Lost | $0.00 |
| 11/2 5:14:32 PM | WTI | UP | 28 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/2 5:14:17 PM | AUDUSD | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:14:17 PM | BRENT | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:13:58 PM | GOLD | DOWN | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 5:13:58 PM | USDCAD | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
