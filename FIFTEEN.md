# 15-Minute 1¢ Study

*Updated Sat Nov 21, 11:23 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4691 finished bets | 1% | $200.10 | +39% | +4.27¢ | $71.55 / $128.55 |

*Expect about **85 buys a day** (~$12.80/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4452 | $96.55 | +20% |
| Volatility model ≥ 2%, hold to the close | 8775 | $41.70 | +4% |
| Momentum model ≥ 2%, hold to the close | 7310 | -$36.75 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 64337 | 64303 | 247 (0%) | 1.07% | -$4,341.10 (-56%) | Hold to the close: -$4,341.10 (-56%) |

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
| Volatility model | 38359 | 4.5% | 0.4% (159) | -636% | ❌ Worse |
| Momentum model | 38359 | 4.4% | 0.4% (159) | -661% | ❌ Worse |
| Mean-reversion model | 38359 | 7.8% | 0.4% (159) | -773% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 38359 | 159 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8775 | 78 | +4% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 4691 | 51 | +39% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 2701 | 30 | +63% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 7310 | 57 | -4% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4452 | 41 | +20% | -75% | -74% | -71% |
| Momentum model ≥ 10% | 2891 | 26 | +29% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 15615 | 109 | -23% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10849 | 89 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7207 | 64 | +1% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 38565 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15273 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10465 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 64303 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 247 | 0% | -$4,341.10 | -56% | — |
| Sell at 2¢ | 2609 | 4% | -$6,826.76 | -88% | 47 sec |
| Sell at 3¢ | 1754 | 3% | -$6,821.04 | -87% | 48 sec |
| Sell at 5¢ | 1193 | 2% | -$6,701.65 | -86% | 62 sec |
| Sell at 10¢ | 728 | 1% | -$6,439.42 | -83% | 65 sec |
| Sell at 25¢ | 392 | 1% | -$5,941.58 | -76% | 80 sec |
| Sell at 50¢ | 255 | 0% | -$5,363.85 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3323 | 17 | 11% | 4% | -51% | -81% | -83% |
| 2–5 min | 20866 | 110 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 16056 | 57 | 3% | 2% | -60% | -92% | -92% |
| Under 1 min | 24045 | 63 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4311 | 19 | 5% | 2% | -41% | -88% | -87% |
| HYPE | 4305 | 14 | 5% | 2% | -58% | -89% | -88% |
| SOL | 4304 | 19 | 4% | 2% | -43% | -86% | -87% |
| BNB | 4294 | 22 | 5% | 2% | -35% | -86% | -85% |
| DOGE | 4291 | 11 | 4% | 2% | -67% | -90% | -89% |
| ETH | 4287 | 19 | 7% | 3% | -44% | -82% | -82% |
| BTC | 4264 | 23 | 5% | 2% | -26% | -86% | -88% |
| NEAR | 4261 | 18 | 5% | 2% | -45% | -85% | -86% |
| XRP | 4248 | 16 | 3% | 2% | -52% | -89% | -88% |
| GOLD | 2265 | 8 | 5% | 2% | -57% | -82% | -84% |
| WTI | 2257 | 7 | 4% | 1% | -62% | -91% | -92% |
| SILVER | 2209 | 9 | 5% | 2% | -51% | -83% | -83% |
| PLATINUM | 2012 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 1968 | 7 | 3% | 1% | -67% | -91% | -90% |
| GBPUSD | 1900 | 8 | 2% | 1% | -61% | -96% | -95% |
| COPPER | 1895 | 6 | 2% | 1% | -70% | -77% | -77% |
| NATGAS | 1858 | 10 | 2% | 1% | -50% | -76% | -76% |
| USDJPY | 1855 | 6 | 2% | 1% | -70% | -96% | -96% |
| PALLADIUM | 1808 | 4 | 1% | 1% | -79% | -93% | -93% |
| AUDUSD | 1406 | 6 | 2% | 1% | -60% | -90% | -90% |
| USDCAD | 1340 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 969 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 499 | 2 | 3% | 1% | -63% | -76% | -74% |
| 2YRRATE | 476 | 4 | 4% | 2% | -22% | -54% | -53% |
| 30YRRATE | 462 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 451 | 2 | 4% | 2% | -59% | -94% | -95% |
| INX | 108 | 1 | 2% | 1% | -14% | -97% | -98% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 32886 | 128 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 31417 | 119 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5661 | 25 | 2% | 1% | -20% | -78% | -78% |
| 0.05–0.1% | 6186 | 25 | 3% | 2% | -36% | -91% | -91% |
| 0.1–0.2% | 9582 | 35 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12056 | 53 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 5071 | 23 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15401 | 48 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 15462 | 81 | 4% | 2% | -40% | -85% | -85% |
| Afternoon (12–6pm) | 15735 | 67 | 4% | 2% | -50% | -87% | -87% |
| Evening (6pm–12am) | 17705 | 51 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,122 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/21 11:14:16 PM | XRP | DOWN | 44 sec | +0.087% | 0¢ | ❌ Lost | $0.00 |
| 11/21 11:14:16 PM | SOL | DOWN | 44 sec | +0.081% | 0¢ | ❌ Lost | $0.00 |
| 11/21 11:14:00 PM | HYPE | DOWN | 60 sec | +0.050% | 0¢ | ❌ Lost | -$0.15 |
| 11/21 11:13:44 PM | NEAR | UP | 75 sec | -0.377% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 11:11:33 PM | ETH | DOWN | 3.4 min | +0.303% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 11:11:33 PM | ZEC | DOWN | 3.4 min | +0.766% | 1¢ | ❌ Lost | $0.00 |
| 11/21 11:11:17 PM | BNB | DOWN | 3.7 min | +0.259% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 11:11:17 PM | DOGE | DOWN | 3.7 min | +0.284% | 6¢ | ❌ Lost | -$0.15 |
| 11/21 11:09:56 PM | BTC | DOWN | 5.1 min | +0.423% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 10:58:43 PM | NEAR | DOWN | 77 sec | +0.196% | 0¢ | ❌ Lost | -$0.15 |
| 11/21 10:57:55 PM | HYPE | DOWN | 2.1 min | +0.294% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 10:57:07 PM | BTC | DOWN | 2.9 min | +0.233% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 10:56:20 PM | XRP | DOWN | 3.7 min | +0.296% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 10:56:20 PM | SOL | DOWN | 3.7 min | +0.293% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 10:55:16 PM | BNB | DOWN | 4.7 min | +0.216% | 3¢ | ❌ Lost | -$0.15 |
| 11/21 10:55:00 PM | DOGE | DOWN | 5.0 min | +0.430% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 10:55:00 PM | ZEC | DOWN | 5.0 min | +1.995% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 10:53:09 PM | ETH | DOWN | 6.8 min | +0.483% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 10:44:40 PM | ZEC | DOWN | 20 sec | +0.073% | 0¢ | ❌ Lost | $0.00 |
| 11/21 10:44:24 PM | HYPE | UP | 36 sec | -0.100% | 0¢ | ❌ Lost | -$0.15 |
| 11/21 10:43:20 PM | NEAR | UP | 1.6 min | -0.294% | 2¢ | ❌ Lost | -$0.15 |
| 11/21 10:43:20 PM | XRP | UP | 1.6 min | -0.230% | 0¢ | ❌ Lost | -$0.15 |
| 11/21 10:43:04 PM | BNB | UP | 1.9 min | -0.272% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 10:43:04 PM | SOL | UP | 1.9 min | -0.256% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 10:42:47 PM | DOGE | UP | 2.2 min | -0.288% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 10:42:31 PM | ETH | UP | 2.5 min | -0.271% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 10:42:31 PM | BTC | UP | 2.5 min | -0.300% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 10:28:31 PM | ZEC | UP | 88 sec | -0.317% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 10:28:31 PM | NEAR | UP | 88 sec | -0.355% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 10:28:15 PM | XRP | UP | 1.7 min | -0.229% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
