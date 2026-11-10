# 15-Minute 1¢ Study

*Updated Mon Nov 9, 6:02 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4127 finished bets | 1% | $185.30 | +40% | +4.49¢ | $90.70 / $94.60 |

*Expect about **97 buys a day** (~$14.48/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3835 | $102.95 | +25% |
| Volatility model ≥ 2%, hold to the close | 7548 | $71.75 | +8% |
| Momentum model ≥ 2%, hold to the close | 6243 | -$2.55 | -0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 51450 | 51433 | 199 (0%) | 1.07% | -$3,474.85 (-56%) | Hold to the close: -$3,474.85 (-56%) |

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
| Volatility model | 31287 | 4.8% | 0.4% (128) | -677% | ❌ Worse |
| Momentum model | 31287 | 4.6% | 0.4% (128) | -701% | ❌ Worse |
| Mean-reversion model | 31287 | 8.1% | 0.4% (128) | -818% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 31287 | 128 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7548 | 70 | +8% | -77% | -75% | -71% |
| Volatility model ≥ 5% | 4127 | 46 | +40% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2377 | 28 | +69% | -61% | -60% | -56% |
| Momentum model ≥ 2% | 6243 | 51 | -0% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3835 | 37 | +25% | -73% | -73% | -68% |
| Momentum model ≥ 10% | 2518 | 25 | +40% | -65% | -64% | -60% |
| Mean-reversion model ≥ 2% | 12944 | 91 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9080 | 78 | -5% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6067 | 56 | +5% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31492 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 12163 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7778 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 51433 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 199 | 0% | -$3,474.85 | -56% | — |
| Sell at 2¢ | 2048 | 4% | -$5,448.37 | -87% | 47 sec |
| Sell at 3¢ | 1393 | 3% | -$5,437.58 | -87% | 48 sec |
| Sell at 5¢ | 975 | 2% | -$5,319.10 | -85% | 63 sec |
| Sell at 10¢ | 591 | 1% | -$5,094.64 | -81% | 65 sec |
| Sell at 25¢ | 312 | 1% | -$4,724.13 | -75% | 83 sec |
| Sell at 50¢ | 205 | 0% | -$4,275.10 | -68% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2552 | 12 | 11% | 4% | -55% | -81% | -82% |
| 2–5 min | 16600 | 93 | 7% | 3% | -45% | -87% | -87% |
| 1–2 min | 13002 | 44 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 19267 | 50 | 1% | 0% | -63% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3527 | 15 | 5% | 2% | -45% | -88% | -88% |
| SOL | 3522 | 16 | 4% | 2% | -42% | -87% | -87% |
| HYPE | 3513 | 11 | 5% | 2% | -61% | -89% | -88% |
| BNB | 3507 | 19 | 5% | 2% | -32% | -86% | -84% |
| DOGE | 3505 | 8 | 4% | 2% | -71% | -90% | -89% |
| ETH | 3498 | 15 | 7% | 3% | -47% | -81% | -81% |
| NEAR | 3477 | 16 | 5% | 2% | -40% | -85% | -85% |
| BTC | 3477 | 17 | 5% | 2% | -33% | -87% | -88% |
| XRP | 3466 | 13 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1849 | 5 | 6% | 2% | -67% | -81% | -83% |
| WTI | 1820 | 6 | 4% | 2% | -60% | -91% | -92% |
| SILVER | 1797 | 8 | 5% | 2% | -47% | -82% | -82% |
| PLATINUM | 1629 | 4 | 2% | 1% | -77% | -96% | -95% |
| EURUSD | 1562 | 5 | 2% | 1% | -70% | -90% | -89% |
| COPPER | 1527 | 6 | 2% | 1% | -63% | -72% | -72% |
| NATGAS | 1488 | 8 | 2% | 1% | -50% | -77% | -77% |
| GBPUSD | 1484 | 5 | 2% | 1% | -69% | -96% | -96% |
| PALLADIUM | 1464 | 3 | 1% | 0% | -81% | -92% | -92% |
| USDJPY | 1461 | 6 | 2% | 1% | -62% | -97% | -96% |
| AUDUSD | 1024 | 5 | 2% | 1% | -54% | -87% | -88% |
| USDCAD | 991 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 589 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 331 | 2 | 5% | 2% | -44% | -64% | -62% |
| 2YRRATE | 314 | 4 | 4% | 2% | +19% | -33% | -31% |
| 30YRRATE | 309 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 291 | 2 | 4% | 2% | -36% | -92% | -95% |
| INX | 11 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 26078 | 104 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 25355 | 95 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5079 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5385 | 20 | 3% | 2% | -43% | -91% | -91% |
| 0.1–0.2% | 8096 | 30 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 9396 | 40 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 3528 | 15 | 7% | 3% | -56% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12671 | 43 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12425 | 56 | 4% | 2% | -49% | -84% | -84% |
| Afternoon (12–6pm) | 12535 | 57 | 4% | 2% | -47% | -86% | -86% |
| Evening (6pm–12am) | 13802 | 43 | 4% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,909 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/9 5:59:44 PM | WTI | DOWN | 16 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/9 5:59:44 PM | BRENT | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:59:44 PM | DOGE | DOWN | 16 sec | -0.017% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 5:59:44 PM | BTC | DOWN | 16 sec | +0.035% | 0¢ | ❌ Lost | $0.00 |
| 11/9 5:59:28 PM | NEAR | DOWN | 32 sec | -0.033% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 5:59:13 PM | XRP | DOWN | 47 sec | +0.128% | 0¢ | ❌ Lost | $0.00 |
| 11/9 5:59:13 PM | HYPE | DOWN | 47 sec | +0.155% | 0¢ | ❌ Lost | $0.00 |
| 11/9 5:58:55 PM | NATGAS | UP | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:58:39 PM | AUDUSD | UP | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:57:52 PM | COPPER | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:57:52 PM | BTC | UP | 2.1 min | -0.081% | 100¢ | ✅ Won | $13.85 |
| 11/9 5:57:36 PM | SOL | UP | 2.4 min | -0.146% | 98¢ | ✅ Won | $13.85 |
| 11/9 5:57:36 PM | ETH | UP | 2.4 min | -0.138% | 80¢ | ✅ Won | $13.85 |
| 11/9 5:57:20 PM | BNB | UP | 2.7 min | -0.154% | 5¢ | ❌ Lost | $0.00 |
| 11/9 5:57:20 PM | PLATINUM | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:57:20 PM | GOLD | UP | 2.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 5:57:20 PM | DOGE | UP | 2.7 min | -0.175% | 99¢ | ✅ Won | $13.85 |
| 11/9 5:56:33 PM | SILVER | UP | 3.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 5:56:17 PM | USDCAD | UP | 3.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:56:17 PM | GBPUSD | DOWN | 3.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:53:37 PM | EURUSD | DOWN | 6.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:44:44 PM | DOGE | UP | 16 sec | -0.060% | 0¢ | ❌ Lost | $0.00 |
| 11/9 5:44:28 PM | NATGAS | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:44:28 PM | GOLD | UP | 32 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/9 5:44:28 PM | NEAR | DOWN | 32 sec | -0.028% | 0¢ | ❌ Lost | $0.00 |
| 11/9 5:44:13 PM | SOL | UP | 47 sec | -0.065% | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:44:13 PM | ZEC | DOWN | 47 sec | +0.226% | 0¢ | ❌ Lost | $0.00 |
| 11/9 5:44:03 PM | USDCAD | DOWN | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:43:47 PM | BNB | UP | 73 sec | -0.115% | 0¢ | ❌ Lost | -$0.15 |
| 11/9 5:43:47 PM | ETH | UP | 73 sec | -0.102% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
