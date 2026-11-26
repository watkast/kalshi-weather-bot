# 15-Minute 1¢ Study

*Updated Wed Nov 25, 6:32 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4906 finished bets | 1% | $207.40 | +39% | +4.23¢ | $86.50 / $120.90 |

*Expect about **83 buys a day** (~$12.52/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4648 | $106.85 | +22% |
| Volatility model ≥ 2%, hold to the close | 9142 | $44.85 | +4% |
| Momentum model ≥ 2%, hold to the close | 7602 | -$37.10 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 67853 | 67819 | 256 (0%) | 1.07% | -$4,628.50 (-56%) | Hold to the close: -$4,628.50 (-56%) |

*In play or awaiting result: 6. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 40175 | 4.5% | 0.4% (165) | -647% | ❌ Worse |
| Momentum model | 40175 | 4.4% | 0.4% (165) | -670% | ❌ Worse |
| Mean-reversion model | 40175 | 7.9% | 0.4% (165) | -786% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 40175 | 165 | -47% | -87% | -86% | -85% |
| Volatility model ≥ 2% | 9142 | 81 | +4% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 4906 | 53 | +39% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 2836 | 32 | +67% | -65% | -63% | -60% |
| Momentum model ≥ 2% | 7602 | 59 | -4% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 4648 | 43 | +22% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 3026 | 28 | +34% | -68% | -68% | -63% |
| Mean-reversion model ≥ 2% | 16364 | 113 | -24% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11396 | 93 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7563 | 66 | -0% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 40381 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 16150 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 11288 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 67819 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 256 | 0% | -$4,628.50 | -56% | — |
| Sell at 2¢ | 2778 | 4% | -$7,196.22 | -88% | 47 sec |
| Sell at 3¢ | 1865 | 3% | -$7,191.15 | -88% | 48 sec |
| Sell at 5¢ | 1261 | 2% | -$7,070.85 | -86% | 62 sec |
| Sell at 10¢ | 770 | 1% | -$6,797.80 | -83% | 65 sec |
| Sell at 25¢ | 416 | 1% | -$6,275.54 | -76% | 80 sec |
| Sell at 50¢ | 266 | 0% | -$5,675.00 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3504 | 17 | 11% | 4% | -54% | -81% | -83% |
| 2–5 min | 21988 | 116 | 7% | 3% | -48% | -86% | -86% |
| 1–2 min | 16918 | 58 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 25396 | 65 | 1% | 0% | -63% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4516 | 20 | 5% | 2% | -41% | -88% | -87% |
| HYPE | 4509 | 16 | 5% | 2% | -54% | -89% | -88% |
| SOL | 4502 | 20 | 4% | 2% | -42% | -86% | -86% |
| BNB | 4496 | 22 | 5% | 2% | -38% | -86% | -85% |
| DOGE | 4493 | 12 | 4% | 2% | -66% | -89% | -89% |
| ETH | 4487 | 19 | 7% | 3% | -47% | -82% | -82% |
| BTC | 4466 | 24 | 6% | 2% | -26% | -86% | -87% |
| NEAR | 4462 | 18 | 5% | 2% | -47% | -85% | -86% |
| XRP | 4450 | 16 | 4% | 2% | -54% | -89% | -88% |
| GOLD | 2388 | 8 | 5% | 2% | -59% | -83% | -84% |
| WTI | 2375 | 8 | 4% | 2% | -59% | -91% | -92% |
| SILVER | 2330 | 9 | 5% | 2% | -54% | -83% | -84% |
| PLATINUM | 2115 | 5 | 3% | 1% | -78% | -95% | -95% |
| EURUSD | 2068 | 7 | 3% | 1% | -68% | -91% | -90% |
| GBPUSD | 2010 | 8 | 2% | 1% | -63% | -96% | -96% |
| COPPER | 2005 | 6 | 2% | 1% | -72% | -78% | -78% |
| USDJPY | 1967 | 6 | 2% | 1% | -72% | -96% | -96% |
| NATGAS | 1964 | 10 | 2% | 1% | -52% | -77% | -77% |
| PALLADIUM | 1902 | 4 | 1% | 1% | -80% | -93% | -93% |
| AUDUSD | 1533 | 7 | 2% | 1% | -57% | -90% | -90% |
| USDCAD | 1441 | 1 | 3% | 1% | -94% | -96% | -96% |
| BRENT | 1071 | 1 | 2% | 1% | -91% | -96% | -97% |
| 10YRRATE | 557 | 2 | 3% | 1% | -66% | -78% | -76% |
| 30YRRATE | 518 | 0 | 3% | 1% | -100% | -95% | -93% |
| 2YRRATE | 515 | 4 | 4% | 2% | -28% | -57% | -57% |
| 5YRRATE | 506 | 2 | 4% | 2% | -63% | -94% | -95% |
| INX | 139 | 1 | 2% | 1% | -33% | -96% | -96% |
| USDMXN | 34 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 34661 | 132 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 33158 | 124 | 4% | 2% | -57% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5855 | 25 | 2% | 1% | -22% | -79% | -78% |
| 0.05–0.1% | 6408 | 26 | 3% | 2% | -35% | -91% | -91% |
| 0.1–0.2% | 10010 | 36 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12732 | 56 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 5367 | 24 | 7% | 3% | -53% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16330 | 50 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 16129 | 82 | 4% | 2% | -42% | -86% | -85% |
| Afternoon (12–6pm) | 16751 | 73 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 18609 | 51 | 4% | 2% | -68% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,090 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/25 6:29:54 PM | COPPER | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 6:29:54 PM | USDMXN | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 6:29:32 PM | SILVER | UP | 28 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/25 6:29:32 PM | HYPE | DOWN | 28 sec | -0.061% | 0¢ | ❌ Lost | -$0.15 |
| 11/25 6:29:32 PM | BTC | UP | 28 sec | -0.053% | 0¢ | ❌ Lost | $0.00 |
| 11/25 6:29:32 PM | PLATINUM | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 6:29:32 PM | PALLADIUM | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 6:29:16 PM | ZEC | DOWN | 44 sec | +0.294% | 0¢ | ❌ Lost | $0.00 |
| 11/25 6:29:16 PM | BRENT | UP | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 6:29:00 PM | SOL | UP | 60 sec | -0.212% | 0¢ | ❌ Lost | -$0.15 |
| 11/25 6:29:00 PM | EURUSD | UP | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 6:29:00 PM | XRP | UP | 60 sec | -0.170% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 6:28:45 PM | DOGE | UP | 75 sec | -0.295% | 0¢ | ❌ Lost | -$0.15 |
| 11/25 6:28:45 PM | ETH | UP | 75 sec | -0.191% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 6:28:45 PM | GOLD | UP | 75 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/25 6:28:24 PM | GBPUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 6:28:24 PM | BNB | UP | 1.6 min | -0.190% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 6:28:24 PM | AUDUSD | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/25 6:28:24 PM | WTI | UP | 1.6 min | — | 1¢ | ❌ Lost | $0.00 |
| 11/25 6:27:18 PM | USDCAD | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 6:27:18 PM | NEAR | UP | 2.7 min | -0.653% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 6:26:30 PM | NATGAS | UP | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 6:14:54 PM | USDCAD | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 6:14:35 PM | HYPE | UP | 25 sec | -0.125% | 0¢ | ❌ Lost | -$0.15 |
| 11/25 6:14:35 PM | AUDUSD | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 6:14:35 PM | SILVER | DOWN | 25 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/25 6:14:35 PM | GBPUSD | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 6:14:19 PM | ZEC | DOWN | 41 sec | +0.099% | 0¢ | ❌ Lost | -$0.15 |
| 11/25 6:14:03 PM | EURUSD | UP | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 6:14:03 PM | WTI | DOWN | 57 sec | — | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
