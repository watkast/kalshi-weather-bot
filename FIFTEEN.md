# 15-Minute 1¢ Study

*Updated Sun Nov 1, 11:58 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3469 finished bets | 1% | $130.25 | +34% | +3.75¢ | $73.85 / $56.40 |

*Expect about **99 buys a day** (~$14.87/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3200 | $57.55 | +17% |
| Volatility model ≥ 2%, hold to the close | 6406 | $50.05 | +6% |
| Momentum model ≥ 2%, hold to the close | 5280 | -$36.95 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 42165 | 42146 | 158 (0%) | 1.07% | -$2,917.25 (-57%) | Hold to the close: -$2,917.25 (-57%) |

*In play or awaiting result: 18. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 26285 | 4.7% | 0.4% (105) | -676% | ❌ Worse |
| Momentum model | 26285 | 4.6% | 0.4% (105) | -698% | ❌ Worse |
| Mean-reversion model | 26285 | 8.1% | 0.4% (105) | -824% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26285 | 105 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6406 | 59 | +6% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3469 | 37 | +34% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1966 | 22 | +60% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 5280 | 41 | -6% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3200 | 29 | +17% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 2089 | 19 | +27% | -74% | -73% | -68% |
| Mean-reversion model ≥ 2% | 10858 | 75 | -24% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7614 | 64 | -7% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 5090 | 46 | +3% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 26487 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9875 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5784 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 42146 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 158 | 0% | -$2,917.25 | -57% | — |
| Sell at 2¢ | 1651 | 4% | -$4,475.99 | -87% | 47 sec |
| Sell at 3¢ | 1133 | 3% | -$4,463.38 | -87% | 48 sec |
| Sell at 5¢ | 787 | 2% | -$4,365.70 | -85% | 63 sec |
| Sell at 10¢ | 474 | 1% | -$4,186.31 | -82% | 65 sec |
| Sell at 25¢ | 250 | 1% | -$3,867.75 | -75% | 83 sec |
| Sell at 50¢ | 163 | 0% | -$3,511.00 | -68% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2002 | 9 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 13533 | 75 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 10657 | 37 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 15943 | 37 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2967 | 13 | 5% | 3% | -44% | -88% | -87% |
| SOL | 2958 | 11 | 4% | 2% | -53% | -91% | -91% |
| BNB | 2955 | 17 | 5% | 2% | -28% | -85% | -84% |
| HYPE | 2954 | 9 | 5% | 3% | -62% | -89% | -87% |
| DOGE | 2942 | 6 | 4% | 2% | -74% | -90% | -90% |
| ETH | 2941 | 11 | 6% | 3% | -55% | -85% | -85% |
| BTC | 2925 | 14 | 5% | 2% | -35% | -88% | -89% |
| NEAR | 2923 | 15 | 5% | 2% | -33% | -83% | -83% |
| XRP | 2922 | 11 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1540 | 5 | 5% | 2% | -61% | -82% | -84% |
| SILVER | 1502 | 7 | 5% | 2% | -45% | -82% | -82% |
| WTI | 1499 | 4 | 3% | 1% | -68% | -93% | -94% |
| PLATINUM | 1333 | 3 | 2% | 1% | -79% | -96% | -96% |
| COPPER | 1273 | 5 | 1% | 1% | -63% | -76% | -75% |
| EURUSD | 1269 | 3 | 2% | 1% | -78% | -89% | -89% |
| NATGAS | 1228 | 7 | 2% | 1% | -47% | -81% | -80% |
| GBPUSD | 1201 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1195 | 2 | 1% | 0% | -84% | -90% | -91% |
| USDJPY | 1193 | 5 | 2% | 1% | -61% | -97% | -96% |
| AUDUSD | 726 | 4 | 2% | 1% | -49% | -85% | -84% |
| USDCAD | 703 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 305 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 188 | 1 | 5% | 2% | -50% | -41% | -39% |
| 30YRRATE | 177 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 170 | 2 | 5% | 1% | +10% | +18% | +19% |
| 5YRRATE | 157 | 1 | 6% | 3% | -41% | -89% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 21400 | 87 | 4% | 2% | -53% | -88% | -87% |
| DOWN (bought NO) | 20746 | 71 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4323 | 21 | 2% | 1% | -16% | -82% | -81% |
| 0.05–0.1% | 4555 | 17 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 6860 | 24 | 4% | 2% | -56% | -90% | -90% |
| 0.2–0.5% | 7809 | 33 | 7% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2935 | 12 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10303 | 36 | 4% | 2% | -60% | -86% | -86% |
| Morning (6am–12pm) | 10513 | 48 | 5% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 9923 | 37 | 4% | 2% | -56% | -87% | -87% |
| Evening (6pm–12am) | 11407 | 37 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,815 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/1 11:57:10 PM | EURUSD | DOWN | 2.8 min | — | — | In play | — |
| 11/1 11:57:10 PM | DOGE | DOWN | 2.8 min | +0.101% | — | In play | — |
| 11/1 11:56:54 PM | GBPUSD | DOWN | 3.1 min | — | — | In play | — |
| 11/1 11:56:38 PM | SOL | DOWN | 3.4 min | +0.215% | — | In play | — |
| 11/1 11:56:38 PM | XRP | DOWN | 3.4 min | +0.161% | — | In play | — |
| 11/1 11:56:06 PM | USDCAD | UP | 3.9 min | — | — | In play | — |
| 11/1 11:56:06 PM | HYPE | UP | 3.9 min | -0.593% | — | In play | — |
| 11/1 11:55:18 PM | NEAR | UP | 4.7 min | -0.911% | — | In play | — |
| 11/1 11:55:18 PM | NATGAS | UP | 4.7 min | — | — | In play | — |
| 11/1 11:44:59 PM | COPPER | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 11:44:43 PM | WTI | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 11:44:43 PM | AUDUSD | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 11:44:43 PM | GOLD | UP | 16 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/1 11:44:43 PM | USDJPY | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 11:44:27 PM | USDCAD | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 11:44:27 PM | SILVER | DOWN | 32 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/1 11:44:27 PM | BRENT | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 11:44:11 PM | NATGAS | DOWN | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 11:43:55 PM | BTC | UP | 64 sec | -0.064% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 11:43:55 PM | ZEC | UP | 64 sec | -0.123% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 11:43:39 PM | ETH | UP | 80 sec | -0.103% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 11:43:23 PM | GBPUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 11:43:23 PM | BNB | DOWN | 1.6 min | +0.034% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 11:43:07 PM | EURUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 11:42:51 PM | DOGE | UP | 2.1 min | -0.188% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 11:42:35 PM | NEAR | UP | 2.4 min | -0.505% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 11:41:47 PM | SOL | UP | 3.2 min | -0.231% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 11:41:16 PM | XRP | UP | 3.7 min | -0.280% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 11:41:00 PM | HYPE | UP | 4.0 min | -0.385% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 11:29:51 PM | WTI | DOWN | 9 sec | — | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
