# 15-Minute 1¢ Study

*Updated Wed Oct 14, 12:52 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1408 finished bets | 1% | $68.60 | +44% | +4.87¢ | $36.55 / $32.05 |

*Expect about **85 buys a day** (~$12.79/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1323 | $39.35 | +28% |
| Momentum model ≥ 2%, hold to the close | 2189 | -$1.05 | -0% |
| Volatility model ≥ 2%, hold to the close | 2516 | -$9.45 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 18222 | 18215 | 69 (0%) | 1.07% | -$1,240.95 (-56%) | Hold to the close: -$1,240.95 (-56%) |

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
| Volatility model | 11875 | 4.5% | 0.4% (49) | -655% | ❌ Worse |
| Momentum model | 11875 | 4.4% | 0.4% (49) | -681% | ❌ Worse |
| Mean-reversion model | 11875 | 7.3% | 0.4% (49) | -776% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 11875 | 49 | -48% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2516 | 21 | -3% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1408 | 16 | +44% | -73% | -71% | -67% |
| Volatility model ≥ 10% | 850 | 9 | +51% | -65% | -63% | -60% |
| Momentum model ≥ 2% | 2189 | 18 | -0% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1323 | 13 | +28% | -77% | -77% | -74% |
| Momentum model ≥ 10% | 894 | 8 | +26% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 4348 | 30 | -24% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2979 | 23 | -14% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1962 | 14 | -18% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12073 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4456 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1686 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 18215 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 69 | 0% | -$1,240.95 | -56% | — |
| Sell at 2¢ | 629 | 3% | -$2,001.41 | -91% | 33 sec |
| Sell at 3¢ | 425 | 2% | -$1,999.20 | -91% | 46 sec |
| Sell at 5¢ | 311 | 2% | -$1,962.80 | -89% | 49 sec |
| Sell at 10¢ | 198 | 1% | -$1,877.57 | -85% | 64 sec |
| Sell at 25¢ | 114 | 1% | -$1,731.61 | -78% | 80 sec |
| Sell at 50¢ | 75 | 0% | -$1,532.70 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 567 | 4 | 10% | 2% | -33% | -83% | -88% |
| 2–5 min | 5879 | 34 | 6% | 3% | -43% | -88% | -88% |
| 1–2 min | 4768 | 18 | 3% | 2% | -59% | -94% | -93% |
| Under 1 min | 6997 | 13 | 1% | 0% | -73% | -92% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1353 | 9 | 5% | 3% | -17% | -89% | -90% |
| HYPE | 1349 | 4 | 4% | 2% | -63% | -90% | -89% |
| ETH | 1346 | 8 | 5% | 3% | -27% | -89% | -88% |
| DOGE | 1345 | 2 | 4% | 2% | -81% | -91% | -90% |
| BNB | 1345 | 5 | 4% | 2% | -55% | -90% | -90% |
| SOL | 1341 | 2 | 3% | 1% | -81% | -93% | -92% |
| BTC | 1332 | 6 | 5% | 2% | -40% | -88% | -91% |
| XRP | 1332 | 7 | 2% | 1% | -35% | -86% | -86% |
| NEAR | 1330 | 8 | 5% | 3% | -22% | -77% | -78% |
| GOLD | 722 | 1 | 4% | 1% | -84% | -92% | -93% |
| SILVER | 710 | 2 | 3% | 1% | -67% | -94% | -94% |
| WTI | 680 | 3 | 3% | 1% | -49% | -94% | -96% |
| COPPER | 631 | 1 | 2% | 1% | -85% | -97% | -96% |
| PLATINUM | 603 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 558 | 1 | 1% | 0% | -83% | -98% | -98% |
| NATGAS | 552 | 3 | 2% | 2% | -49% | -96% | -95% |
| EURUSD | 536 | 3 | 3% | 1% | -48% | -78% | -77% |
| GBPUSD | 503 | 1 | 2% | 1% | -81% | -97% | -96% |
| USDJPY | 459 | 3 | 1% | 1% | -39% | -98% | -98% |
| AUDUSD | 101 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 87 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9199 | 35 | 3% | 2% | -56% | -90% | -90% |
| DOWN (bought NO) | 9016 | 34 | 3% | 2% | -56% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2088 | 10 | 2% | 1% | -20% | -78% | -78% |
| 0.05–0.1% | 2129 | 7 | 3% | 1% | -52% | -92% | -91% |
| 0.1–0.2% | 3067 | 9 | 4% | 2% | -64% | -91% | -91% |
| 0.2–0.5% | 3441 | 20 | 6% | 3% | -36% | -88% | -88% |
| Over 0.5% | 1345 | 5 | 6% | 2% | -61% | -89% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4717 | 20 | 4% | 2% | -52% | -87% | -88% |
| Morning (6am–12pm) | 4329 | 23 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 4165 | 11 | 3% | 1% | -69% | -90% | -91% |
| Evening (6pm–12am) | 5004 | 15 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,496 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/14 12:44:46 PM | SILVER | UP | 13 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/14 12:44:46 PM | WTI | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 12:44:46 PM | GBPUSD | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 12:44:30 PM | NEAR | UP | 29 sec | -0.187% | 0¢ | ❌ Lost | $0.00 |
| 10/14 12:44:30 PM | EURUSD | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 12:44:30 PM | BTC | UP | 29 sec | -0.042% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 12:44:16 PM | USDJPY | UP | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 12:43:59 PM | USDCAD | UP | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 12:43:43 PM | HYPE | DOWN | 76 sec | +0.150% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 12:43:27 PM | SOL | UP | 1.5 min | -0.163% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 12:43:11 PM | COPPER | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 12:43:11 PM | PLATINUM | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 12:42:52 PM | ETH | UP | 2.1 min | -0.163% | 0¢ | ❌ Lost | $0.00 |
| 10/14 12:42:36 PM | BNB | UP | 2.4 min | -0.130% | 5¢ | ❌ Lost | -$0.15 |
| 10/14 12:42:20 PM | DOGE | UP | 2.7 min | -0.277% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 12:42:04 PM | XRP | UP | 2.9 min | -0.332% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 12:41:15 PM | ZEC | UP | 3.7 min | -0.401% | 3¢ | ❌ Lost | -$0.15 |
| 10/14 12:29:48 PM | NATGAS | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 12:29:32 PM | BTC | UP | 27 sec | -0.031% | 0¢ | ❌ Lost | $0.00 |
| 10/14 12:29:32 PM | HYPE | UP | 27 sec | -0.067% | 0¢ | ❌ Lost | $0.00 |
| 10/14 12:29:16 PM | WTI | UP | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 12:29:16 PM | COPPER | UP | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 12:29:16 PM | DOGE | UP | 44 sec | -0.081% | 0¢ | ❌ Lost | $0.00 |
| 10/14 12:29:16 PM | GOLD | DOWN | 44 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/14 12:28:10 PM | NEAR | UP | 1.8 min | -0.434% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 12:27:51 PM | GBPUSD | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 12:27:19 PM | USDJPY | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 12:27:04 PM | XRP | UP | 2.9 min | -0.301% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 12:27:04 PM | EURUSD | DOWN | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 12:27:04 PM | ETH | UP | 2.9 min | -0.192% | 4¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
