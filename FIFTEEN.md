# 15-Minute 1¢ Study

*Updated Tue Nov 3, 8:52 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3608 finished bets | 1% | $114.95 | +29% | +3.19¢ | $79.60 / $35.35 |

*Expect about **98 buys a day** (~$14.67/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3343 | $42.40 | +12% |
| Volatility model ≥ 2%, hold to the close | 6676 | $32.55 | +4% |
| Momentum model ≥ 2%, hold to the close | 5506 | -$47.85 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 44664 | 44654 | 165 (0%) | 1.07% | -$3,127.95 (-58%) | Hold to the close: -$3,127.95 (-58%) |

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
| Volatility model | 27432 | 4.7% | 0.4% (107) | -680% | ❌ Worse |
| Momentum model | 27432 | 4.6% | 0.4% (107) | -706% | ❌ Worse |
| Mean-reversion model | 27432 | 8.1% | 0.4% (107) | -828% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 27432 | 107 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6676 | 60 | +4% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3608 | 37 | +29% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2047 | 22 | +54% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5506 | 42 | -8% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 3343 | 29 | +12% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2181 | 19 | +22% | -74% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11337 | 77 | -26% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7959 | 66 | -8% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 5327 | 47 | +0% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 27637 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10573 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6444 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 44654 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 165 | 0% | -$3,127.95 | -58% | — |
| Sell at 2¢ | 1758 | 4% | -$4,742.87 | -87% | 47 sec |
| Sell at 3¢ | 1204 | 3% | -$4,730.39 | -87% | 49 sec |
| Sell at 5¢ | 834 | 2% | -$4,629.85 | -85% | 63 sec |
| Sell at 10¢ | 502 | 1% | -$4,430.33 | -81% | 66 sec |
| Sell at 25¢ | 263 | 1% | -$4,105.42 | -75% | 83 sec |
| Sell at 50¢ | 169 | 0% | -$3,737.20 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2163 | 9 | 11% | 4% | -60% | -81% | -82% |
| 2–5 min | 14361 | 79 | 7% | 3% | -46% | -86% | -86% |
| 1–2 min | 11269 | 39 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 16850 | 38 | 1% | 0% | -68% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3096 | 13 | 5% | 3% | -46% | -88% | -88% |
| SOL | 3089 | 11 | 4% | 2% | -55% | -91% | -90% |
| BNB | 3083 | 17 | 5% | 2% | -31% | -85% | -84% |
| HYPE | 3082 | 9 | 5% | 2% | -63% | -89% | -87% |
| DOGE | 3070 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 3067 | 12 | 7% | 3% | -52% | -85% | -85% |
| NEAR | 3053 | 15 | 5% | 2% | -36% | -84% | -84% |
| BTC | 3053 | 14 | 5% | 2% | -38% | -88% | -89% |
| XRP | 3044 | 12 | 3% | 1% | -51% | -89% | -89% |
| GOLD | 1639 | 5 | 5% | 2% | -63% | -81% | -83% |
| WTI | 1597 | 5 | 3% | 1% | -62% | -92% | -93% |
| SILVER | 1596 | 7 | 5% | 2% | -48% | -82% | -81% |
| PLATINUM | 1427 | 4 | 2% | 1% | -74% | -96% | -96% |
| EURUSD | 1370 | 3 | 2% | 1% | -80% | -89% | -89% |
| COPPER | 1349 | 6 | 2% | 1% | -58% | -69% | -69% |
| NATGAS | 1299 | 7 | 2% | 1% | -50% | -82% | -81% |
| GBPUSD | 1299 | 3 | 2% | 1% | -78% | -96% | -96% |
| USDJPY | 1278 | 5 | 2% | 1% | -63% | -97% | -97% |
| PALLADIUM | 1277 | 3 | 1% | 1% | -78% | -91% | -91% |
| AUDUSD | 826 | 4 | 2% | 1% | -55% | -86% | -85% |
| USDCAD | 794 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 389 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 240 | 1 | 5% | 2% | -61% | -52% | -50% |
| 30YRRATE | 223 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 215 | 2 | 4% | 0% | -13% | -7% | -6% |
| 5YRRATE | 199 | 1 | 5% | 2% | -53% | -91% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 22720 | 88 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 21934 | 77 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4482 | 21 | 2% | 1% | -18% | -83% | -82% |
| 0.05–0.1% | 4719 | 18 | 3% | 2% | -42% | -91% | -90% |
| 0.1–0.2% | 7158 | 25 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 8198 | 33 | 6% | 3% | -55% | -87% | -86% |
| Over 0.5% | 3072 | 12 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11048 | 40 | 4% | 2% | -59% | -87% | -87% |
| Morning (6am–12pm) | 11054 | 48 | 4% | 2% | -51% | -85% | -85% |
| Afternoon (12–6pm) | 10598 | 39 | 4% | 2% | -57% | -86% | -86% |
| Evening (6pm–12am) | 11954 | 38 | 3% | 2% | -63% | -91% | -90% |

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
| 11/3 8:44:56 PM | XRP | DOWN | 3 sec | +0.000% | 0¢ | ❌ Lost | $0.00 |
| 11/3 8:44:40 PM | HYPE | UP | 19 sec | -0.156% | 0¢ | ❌ Lost | $0.00 |
| 11/3 8:44:40 PM | GOLD | UP | 19 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/3 8:44:40 PM | PALLADIUM | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 8:44:40 PM | BTC | UP | 19 sec | -0.071% | 0¢ | ❌ Lost | $0.00 |
| 11/3 8:44:24 PM | ZEC | UP | 35 sec | -0.259% | 0¢ | ❌ Lost | $0.00 |
| 11/3 8:44:24 PM | ETH | UP | 35 sec | -0.099% | 0¢ | ❌ Lost | $0.00 |
| 11/3 8:44:24 PM | SILVER | UP | 35 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 8:44:24 PM | PLATINUM | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 8:43:36 PM | BNB | UP | 84 sec | -0.202% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 8:43:20 PM | WTI | DOWN | 1.7 min | — | 0¢ | ❌ Lost | $0.00 |
| 11/3 8:43:20 PM | BRENT | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 8:42:48 PM | DOGE | UP | 2.2 min | -0.295% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 8:42:27 PM | NEAR | UP | 2.5 min | -0.736% | 0¢ | ❌ Lost | -$0.15 |
| 11/3 8:42:11 PM | USDCAD | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 8:41:05 PM | GBPUSD | DOWN | 3.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 8:41:05 PM | SOL | UP | 3.9 min | -0.482% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 8:41:05 PM | USDJPY | UP | 3.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 8:40:50 PM | COPPER | UP | 4.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 8:38:58 PM | EURUSD | DOWN | 6.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 8:29:46 PM | GOLD | DOWN | 13 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/3 8:28:08 PM | BRENT | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 8:27:37 PM | WTI | DOWN | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 8:27:05 PM | NEAR | DOWN | 2.9 min | +0.648% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 8:26:33 PM | SOL | DOWN | 3.5 min | +0.512% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 8:26:15 PM | HYPE | DOWN | 3.8 min | +0.708% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 8:26:15 PM | DOGE | DOWN | 3.8 min | +0.486% | 0¢ | ❌ Lost | -$0.15 |
| 11/3 8:26:15 PM | USDCAD | DOWN | 3.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 8:25:59 PM | GBPUSD | UP | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 8:25:59 PM | BTC | DOWN | 4.0 min | +0.405% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
