# 15-Minute 1¢ Study

*Updated Mon Nov 9, 2:35 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4107 finished bets | 1% | $187.40 | +41% | +4.56¢ | $91.75 / $95.65 |

*Expect about **96 buys a day** (~$14.45/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3815 | $105.05 | +25% |
| Volatility model ≥ 2%, hold to the close | 7518 | $75.05 | +8% |
| Momentum model ≥ 2%, hold to the close | 6215 | $0.30 | +0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 51200 | 51182 | 195 (0%) | 1.07% | -$3,500.10 (-56%) | Hold to the close: -$3,500.10 (-56%) |

*In play or awaiting result: 10. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 31160 | 4.8% | 0.4% (124) | -685% | ❌ Worse |
| Momentum model | 31160 | 4.6% | 0.4% (124) | -711% | ❌ Worse |
| Mean-reversion model | 31160 | 8.1% | 0.4% (124) | -828% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 31160 | 124 | -49% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7518 | 70 | +8% | -77% | -75% | -71% |
| Volatility model ≥ 5% | 4107 | 46 | +41% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2363 | 28 | +70% | -61% | -60% | -56% |
| Momentum model ≥ 2% | 6215 | 51 | +0% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3815 | 37 | +25% | -73% | -73% | -68% |
| Momentum model ≥ 10% | 2501 | 25 | +41% | -65% | -64% | -59% |
| Mean-reversion model ≥ 2% | 12883 | 90 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9033 | 77 | -5% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6035 | 56 | +6% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31365 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12091 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7726 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 51182 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 195 | 0% | -$3,500.10 | -56% | — |
| Sell at 2¢ | 2031 | 4% | -$5,422.04 | -87% | 47 sec |
| Sell at 3¢ | 1383 | 3% | -$5,410.73 | -87% | 48 sec |
| Sell at 5¢ | 968 | 2% | -$5,292.90 | -85% | 62 sec |
| Sell at 10¢ | 587 | 1% | -$5,069.13 | -81% | 65 sec |
| Sell at 25¢ | 308 | 1% | -$4,706.62 | -76% | 83 sec |
| Sell at 50¢ | 201 | 0% | -$4,271.35 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2533 | 12 | 11% | 4% | -55% | -81% | -82% |
| 2–5 min | 16528 | 89 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 12944 | 44 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 19165 | 50 | 1% | 0% | -63% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3514 | 15 | 5% | 2% | -45% | -88% | -88% |
| SOL | 3508 | 15 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3499 | 11 | 5% | 2% | -61% | -89% | -88% |
| BNB | 3493 | 19 | 5% | 2% | -31% | -86% | -85% |
| DOGE | 3490 | 7 | 4% | 2% | -75% | -90% | -89% |
| ETH | 3484 | 14 | 7% | 3% | -50% | -81% | -81% |
| NEAR | 3463 | 16 | 5% | 2% | -40% | -85% | -85% |
| BTC | 3462 | 16 | 5% | 2% | -36% | -87% | -89% |
| XRP | 3452 | 13 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1840 | 5 | 6% | 2% | -67% | -81% | -83% |
| WTI | 1808 | 6 | 4% | 1% | -60% | -92% | -92% |
| SILVER | 1789 | 8 | 5% | 2% | -47% | -82% | -82% |
| PLATINUM | 1622 | 4 | 2% | 1% | -77% | -96% | -95% |
| EURUSD | 1553 | 5 | 2% | 1% | -70% | -90% | -89% |
| COPPER | 1518 | 6 | 2% | 1% | -63% | -72% | -72% |
| NATGAS | 1478 | 8 | 2% | 1% | -49% | -77% | -77% |
| GBPUSD | 1474 | 5 | 2% | 1% | -68% | -96% | -96% |
| PALLADIUM | 1458 | 3 | 1% | 0% | -81% | -92% | -92% |
| USDJPY | 1456 | 6 | 2% | 1% | -62% | -97% | -96% |
| AUDUSD | 1014 | 5 | 2% | 1% | -54% | -87% | -87% |
| USDCAD | 980 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 578 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 330 | 2 | 5% | 2% | -43% | -64% | -61% |
| 2YRRATE | 313 | 4 | 4% | 2% | +19% | -33% | -31% |
| 30YRRATE | 307 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 289 | 2 | 4% | 2% | -35% | -92% | -95% |
| INX | 10 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 25937 | 100 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 25245 | 95 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5061 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5355 | 19 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 8065 | 27 | 5% | 2% | -58% | -89% | -89% |
| 0.2–0.5% | 9358 | 40 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 3518 | 15 | 7% | 3% | -56% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12671 | 43 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12425 | 56 | 4% | 2% | -49% | -84% | -84% |
| Afternoon (12–6pm) | 12284 | 53 | 4% | 2% | -49% | -86% | -86% |
| Evening (6pm–12am) | 13802 | 43 | 4% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,907 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/9 2:29:56 PM | PLATINUM | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 2:29:56 PM | COPPER | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 2:29:56 PM | 2YRRATE | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 2:29:56 PM | SILVER | DOWN | 3 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/9 2:29:56 PM | 5YRRATE | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 2:29:40 PM | PALLADIUM | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 2:29:40 PM | SOL | DOWN | 19 sec | +0.168% | 0¢ | ❌ Lost | $0.00 |
| 11/9 2:29:40 PM | GOLD | DOWN | 19 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/9 2:29:40 PM | USDCAD | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 2:29:25 PM | BTC | DOWN | 34 sec | +0.051% | 0¢ | ❌ Lost | $0.00 |
| 11/9 2:29:25 PM | 2YRRATE | DOWN | 34 sec | — | 99¢ | ✅ Won | $13.85 |
| 11/9 2:29:25 PM | BNB | DOWN | 34 sec | -0.007% | 0¢ | ❌ Lost | $0.00 |
| 11/9 2:29:25 PM | 5YRRATE | DOWN | 34 sec | — | 99¢ | ✅ Won | $13.85 |
| 11/9 2:29:06 PM | USDJPY | DOWN | 53 sec | — | 59¢ | ✅ Won | $13.85 |
| 11/9 2:29:06 PM | GBPUSD | UP | 53 sec | — | 84¢ | ✅ Won | $13.85 |
| 11/9 2:28:50 PM | XRP | DOWN | 69 sec | +0.239% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 2:28:50 PM | DOGE | DOWN | 69 sec | +0.057% | 0¢ | ❌ Lost | $0.00 |
| 11/9 2:28:34 PM | ETH | DOWN | 85 sec | +0.102% | 0¢ | ❌ Lost | $0.00 |
| 11/9 2:28:20 PM | 10YRRATE | DOWN | 1.7 min | — | 98¢ | ✅ Won | $13.85 |
| 11/9 2:28:03 PM | ZEC | DOWN | 1.9 min | +0.587% | 0¢ | ❌ Lost | $0.00 |
| 11/9 2:27:31 PM | 30YRRATE | DOWN | 2.5 min | — | 69¢ | ❌ Lost | -$0.15 |
| 11/9 2:26:56 PM | EURUSD | UP | 3.0 min | — | 53¢ | ✅ Won | $13.85 |
| 11/9 2:26:09 PM | NEAR | DOWN | 3.8 min | +0.486% | 2¢ | ❌ Lost | -$0.15 |
| 11/9 2:25:19 PM | HYPE | DOWN | 4.7 min | +0.351% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 2:14:52 PM | BTC | UP | 7 sec | -0.021% | 0¢ | ❌ Lost | $0.00 |
| 11/9 2:14:52 PM | EURUSD | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 2:14:52 PM | GBPUSD | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 2:14:36 PM | PALLADIUM | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 2:14:17 PM | BNB | UP | 43 sec | +0.012% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 2:13:59 PM | ZEC | UP | 60 sec | -0.424% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
