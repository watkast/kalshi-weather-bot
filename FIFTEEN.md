# 15-Minute 1¢ Study

*Updated Tue Nov 10, 12:02 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4145 finished bets | 1% | $183.35 | +40% | +4.42¢ | $89.50 / $93.85 |

*Expect about **96 buys a day** (~$14.45/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3851 | $101.30 | +24% |
| Volatility model ≥ 2%, hold to the close | 7578 | $68.00 | +7% |
| Momentum model ≥ 2%, hold to the close | 6271 | -$6.00 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 51765 | 51748 | 199 (0%) | 1.07% | -$3,516.85 (-56%) | Hold to the close: -$3,516.85 (-56%) |

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
| Volatility model | 31431 | 4.8% | 0.4% (128) | -678% | ❌ Worse |
| Momentum model | 31431 | 4.6% | 0.4% (128) | -702% | ❌ Worse |
| Mean-reversion model | 31431 | 8.1% | 0.4% (128) | -820% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 31431 | 128 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7578 | 70 | +7% | -77% | -76% | -71% |
| Volatility model ≥ 5% | 4145 | 46 | +40% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2388 | 28 | +68% | -62% | -60% | -56% |
| Momentum model ≥ 2% | 6271 | 51 | -1% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3851 | 37 | +24% | -73% | -73% | -68% |
| Momentum model ≥ 10% | 2527 | 25 | +39% | -65% | -64% | -60% |
| Mean-reversion model ≥ 2% | 13010 | 91 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9125 | 78 | -5% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6101 | 56 | +4% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31636 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12268 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7844 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 51748 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 199 | 0% | -$3,516.85 | -56% | — |
| Sell at 2¢ | 2066 | 4% | -$5,485.69 | -87% | 47 sec |
| Sell at 3¢ | 1407 | 3% | -$5,474.12 | -87% | 48 sec |
| Sell at 5¢ | 982 | 2% | -$5,356.55 | -85% | 63 sec |
| Sell at 10¢ | 595 | 1% | -$5,131.40 | -81% | 65 sec |
| Sell at 25¢ | 314 | 1% | -$4,759.51 | -76% | 83 sec |
| Sell at 50¢ | 205 | 0% | -$4,317.10 | -68% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2574 | 12 | 11% | 4% | -56% | -81% | -82% |
| 2–5 min | 16721 | 93 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 13080 | 44 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 19361 | 50 | 1% | 0% | -63% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3543 | 15 | 5% | 2% | -45% | -88% | -88% |
| SOL | 3539 | 16 | 4% | 2% | -42% | -87% | -87% |
| HYPE | 3530 | 11 | 5% | 2% | -61% | -89% | -88% |
| BNB | 3523 | 19 | 5% | 2% | -32% | -86% | -85% |
| DOGE | 3519 | 8 | 4% | 2% | -71% | -90% | -89% |
| ETH | 3514 | 15 | 7% | 3% | -47% | -81% | -81% |
| NEAR | 3493 | 16 | 5% | 2% | -41% | -85% | -85% |
| BTC | 3493 | 17 | 5% | 2% | -33% | -87% | -88% |
| XRP | 3482 | 13 | 3% | 1% | -53% | -89% | -88% |
| GOLD | 1860 | 5 | 6% | 2% | -67% | -81% | -83% |
| WTI | 1834 | 6 | 4% | 2% | -61% | -91% | -92% |
| SILVER | 1812 | 8 | 5% | 2% | -48% | -83% | -82% |
| PLATINUM | 1641 | 4 | 2% | 1% | -77% | -96% | -95% |
| EURUSD | 1576 | 5 | 2% | 1% | -70% | -90% | -89% |
| COPPER | 1540 | 6 | 2% | 1% | -64% | -73% | -72% |
| NATGAS | 1503 | 8 | 2% | 1% | -50% | -78% | -77% |
| GBPUSD | 1496 | 5 | 2% | 1% | -69% | -96% | -96% |
| PALLADIUM | 1478 | 3 | 1% | 0% | -81% | -92% | -92% |
| USDJPY | 1475 | 6 | 2% | 1% | -62% | -96% | -96% |
| AUDUSD | 1036 | 5 | 2% | 1% | -55% | -87% | -87% |
| USDCAD | 1005 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 600 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 331 | 2 | 5% | 2% | -44% | -64% | -62% |
| 2YRRATE | 314 | 4 | 4% | 2% | +19% | -33% | -31% |
| 30YRRATE | 309 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 291 | 2 | 4% | 2% | -36% | -92% | -95% |
| INX | 11 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 26230 | 104 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 25518 | 95 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5092 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5408 | 20 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 8134 | 30 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 9453 | 40 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 3541 | 15 | 7% | 3% | -56% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12671 | 43 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12425 | 56 | 4% | 2% | -49% | -84% | -84% |
| Afternoon (12–6pm) | 12535 | 57 | 4% | 2% | -47% | -86% | -86% |
| Evening (6pm–12am) | 14117 | 43 | 4% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,908 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/9 11:59:50 PM | HYPE | DOWN | 9 sec | +0.012% | 0¢ | ❌ Lost | $0.00 |
| 11/9 11:59:50 PM | ETH | UP | 9 sec | -0.016% | 0¢ | ❌ Lost | $0.00 |
| 11/9 11:59:34 PM | NEAR | DOWN | 25 sec | -0.008% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 11:59:34 PM | SOL | DOWN | 25 sec | +0.022% | 0¢ | ❌ Lost | $0.00 |
| 11/9 11:59:18 PM | DOGE | UP | 41 sec | -0.137% | 0¢ | ❌ Lost | $0.00 |
| 11/9 11:59:02 PM | XRP | UP | 57 sec | -0.073% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 11:58:47 PM | SILVER | UP | 73 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 11:58:47 PM | BNB | DOWN | 73 sec | +0.048% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 11:58:47 PM | USDJPY | DOWN | 73 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 11:58:31 PM | GBPUSD | UP | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 11:58:15 PM | WTI | DOWN | 1.8 min | — | 0¢ | ❌ Lost | $0.00 |
| 11/9 11:58:15 PM | BRENT | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 11:57:59 PM | USDCAD | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 11:57:59 PM | PALLADIUM | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 11:57:59 PM | NATGAS | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 11:57:27 PM | BTC | UP | 2.5 min | -0.121% | 3¢ | ❌ Lost | -$0.15 |
| 11/9 11:57:27 PM | COPPER | UP | 2.5 min | — | 2¢ | ❌ Lost | -$0.15 |
| 11/9 11:57:27 PM | ZEC | UP | 2.5 min | -0.378% | 4¢ | ❌ Lost | -$0.15 |
| 11/9 11:56:07 PM | AUDUSD | UP | 3.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 11:44:57 PM | GOLD | DOWN | 2 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 11:44:57 PM | PLATINUM | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 11:44:57 PM | SOL | DOWN | 2 sec | -0.004% | 0¢ | ❌ Lost | $0.00 |
| 11/9 11:44:41 PM | SILVER | UP | 18 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 11:44:25 PM | USDCAD | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 11:44:25 PM | HYPE | DOWN | 34 sec | +0.031% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 11:44:25 PM | DOGE | DOWN | 34 sec | +0.023% | 0¢ | ❌ Lost | $0.00 |
| 11/9 11:44:25 PM | AUDUSD | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 11:44:09 PM | ZEC | DOWN | 50 sec | +0.116% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 11:44:09 PM | XRP | DOWN | 50 sec | +0.082% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 11:44:09 PM | EURUSD | DOWN | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
