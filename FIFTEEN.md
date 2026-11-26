# 15-Minute 1¢ Study

*Updated Wed Nov 25, 8:16 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4912 finished bets | 1% | $206.95 | +39% | +4.21¢ | $86.20 / $120.75 |

*Expect about **83 buys a day** (~$12.52/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4654 | $106.40 | +21% |
| Volatility model ≥ 2%, hold to the close | 9155 | $43.95 | +4% |
| Momentum model ≥ 2%, hold to the close | 7613 | -$37.85 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 67991 | 67957 | 256 (0%) | 1.07% | -$4,643.65 (-56%) | Hold to the close: -$4,643.65 (-56%) |

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
| Volatility model | 40237 | 4.5% | 0.4% (165) | -648% | ❌ Worse |
| Momentum model | 40237 | 4.4% | 0.4% (165) | -671% | ❌ Worse |
| Mean-reversion model | 40237 | 7.9% | 0.4% (165) | -787% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 40237 | 165 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 9155 | 81 | +4% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 4912 | 53 | +39% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 2839 | 32 | +67% | -65% | -63% | -60% |
| Momentum model ≥ 2% | 7613 | 59 | -4% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 4654 | 43 | +21% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 3031 | 28 | +33% | -68% | -68% | -63% |
| Mean-reversion model ≥ 2% | 16392 | 113 | -24% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11410 | 93 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7575 | 66 | -0% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 40443 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 16196 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 11318 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 67957 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 256 | 0% | -$4,643.65 | -56% | — |
| Sell at 2¢ | 2782 | 4% | -$7,210.33 | -88% | 47 sec |
| Sell at 3¢ | 1868 | 3% | -$7,205.13 | -88% | 48 sec |
| Sell at 5¢ | 1262 | 2% | -$7,085.35 | -86% | 62 sec |
| Sell at 10¢ | 771 | 1% | -$6,811.64 | -83% | 65 sec |
| Sell at 25¢ | 416 | 1% | -$6,290.69 | -76% | 80 sec |
| Sell at 50¢ | 266 | 0% | -$5,690.15 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3515 | 17 | 11% | 4% | -54% | -81% | -83% |
| 2–5 min | 22035 | 116 | 7% | 3% | -48% | -86% | -86% |
| 1–2 min | 16949 | 58 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 25445 | 65 | 1% | 0% | -63% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4523 | 20 | 5% | 2% | -41% | -88% | -87% |
| HYPE | 4516 | 16 | 5% | 2% | -54% | -89% | -88% |
| SOL | 4509 | 20 | 4% | 2% | -42% | -86% | -86% |
| BNB | 4503 | 22 | 5% | 2% | -38% | -86% | -85% |
| DOGE | 4500 | 12 | 4% | 2% | -66% | -89% | -89% |
| ETH | 4493 | 19 | 7% | 3% | -47% | -82% | -82% |
| BTC | 4473 | 24 | 6% | 2% | -26% | -86% | -87% |
| NEAR | 4469 | 18 | 5% | 2% | -47% | -85% | -86% |
| XRP | 4457 | 16 | 4% | 2% | -54% | -89% | -88% |
| GOLD | 2394 | 8 | 5% | 2% | -59% | -83% | -84% |
| WTI | 2380 | 8 | 4% | 2% | -59% | -91% | -92% |
| SILVER | 2337 | 9 | 5% | 2% | -54% | -83% | -84% |
| PLATINUM | 2122 | 5 | 3% | 1% | -78% | -95% | -94% |
| EURUSD | 2074 | 7 | 3% | 1% | -68% | -91% | -90% |
| GBPUSD | 2016 | 8 | 2% | 1% | -63% | -96% | -96% |
| COPPER | 2011 | 6 | 2% | 1% | -72% | -78% | -78% |
| USDJPY | 1970 | 6 | 2% | 1% | -72% | -96% | -96% |
| NATGAS | 1968 | 10 | 2% | 1% | -53% | -77% | -77% |
| PALLADIUM | 1908 | 4 | 1% | 1% | -80% | -93% | -93% |
| AUDUSD | 1539 | 7 | 2% | 1% | -58% | -90% | -90% |
| USDCAD | 1447 | 1 | 3% | 1% | -94% | -95% | -96% |
| BRENT | 1076 | 1 | 2% | 1% | -91% | -96% | -97% |
| 10YRRATE | 557 | 2 | 3% | 1% | -66% | -78% | -76% |
| 30YRRATE | 518 | 0 | 3% | 1% | -100% | -95% | -93% |
| 2YRRATE | 515 | 4 | 4% | 2% | -28% | -57% | -57% |
| 5YRRATE | 506 | 2 | 4% | 2% | -63% | -94% | -95% |
| INX | 139 | 1 | 2% | 1% | -33% | -96% | -96% |
| USDMXN | 37 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 34711 | 132 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 33246 | 124 | 4% | 2% | -57% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5866 | 25 | 2% | 1% | -22% | -79% | -78% |
| 0.05–0.1% | 6414 | 26 | 3% | 2% | -35% | -91% | -91% |
| 0.1–0.2% | 10028 | 36 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 12752 | 56 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 5374 | 24 | 7% | 3% | -53% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16330 | 50 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 16129 | 82 | 4% | 2% | -42% | -86% | -85% |
| Afternoon (12–6pm) | 16751 | 73 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 18747 | 51 | 4% | 2% | -69% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,088 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/25 8:14:57 PM | PLATINUM | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:14:37 PM | ETH | DOWN | 22 sec | -0.010% | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:14:21 PM | DOGE | DOWN | 38 sec | +0.175% | 0¢ | ❌ Lost | $0.00 |
| 11/25 8:14:05 PM | SOL | DOWN | 54 sec | +0.136% | 0¢ | ❌ Lost | $0.00 |
| 11/25 8:14:05 PM | BTC | DOWN | 54 sec | +0.113% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 8:14:05 PM | NEAR | DOWN | 54 sec | +0.117% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 8:13:49 PM | XRP | DOWN | 71 sec | +0.105% | 0¢ | ❌ Lost | $0.00 |
| 11/25 8:13:49 PM | COPPER | UP | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:13:49 PM | WTI | DOWN | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:13:49 PM | ZEC | DOWN | 71 sec | +0.249% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 8:13:29 PM | BNB | DOWN | 1.5 min | +0.097% | 0¢ | ❌ Lost | $0.00 |
| 11/25 8:13:29 PM | BRENT | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:13:13 PM | GOLD | UP | 1.8 min | — | 0¢ | ❌ Lost | $0.00 |
| 11/25 8:13:13 PM | EURUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:12:41 PM | GBPUSD | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:11:14 PM | USDCAD | DOWN | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:11:14 PM | SILVER | UP | 3.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/25 8:10:42 PM | HYPE | DOWN | 4.3 min | +0.507% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 7:59:58 PM | USDJPY | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 7:59:58 PM | WTI | DOWN | 2 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/25 7:59:37 PM | USDMXN | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 7:59:05 PM | NATGAS | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 7:59:05 PM | DOGE | UP | 54 sec | -0.169% | 0¢ | ❌ Lost | $0.00 |
| 11/25 7:57:58 PM | USDCAD | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 7:57:21 PM | AUDUSD | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 7:57:05 PM | XRP | UP | 2.9 min | -0.386% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 7:56:05 PM | PLATINUM | UP | 3.9 min | — | 3¢ | ❌ Lost | -$0.15 |
| 11/25 7:55:49 PM | EURUSD | UP | 4.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 7:55:33 PM | SOL | UP | 4.4 min | -0.409% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 7:55:18 PM | ETH | UP | 4.7 min | -0.499% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
