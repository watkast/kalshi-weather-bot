# 15-Minute 1¢ Study

*Updated Wed Oct 14, 4:41 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1432 finished bets | 1% | $79.75 | +50% | +5.57¢ | $35.20 / $44.55 |

*Expect about **86 buys a day** (~$12.89/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1345 | $50.80 | +35% |
| Momentum model ≥ 2%, hold to the close | 2223 | $8.60 | +3% |
| Volatility model ≥ 2%, hold to the close | 2565 | -$1.75 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 18446 | 18439 | 71 (0%) | 1.07% | -$1,240.10 (-56%) | Hold to the close: -$1,240.10 (-56%) |

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
| Volatility model | 12007 | 4.5% | 0.4% (51) | -645% | ❌ Worse |
| Momentum model | 12007 | 4.4% | 0.4% (51) | -671% | ❌ Worse |
| Mean-reversion model | 12007 | 7.3% | 0.4% (51) | -765% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12007 | 51 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2565 | 22 | -1% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1432 | 17 | +50% | -73% | -71% | -67% |
| Volatility model ≥ 10% | 861 | 10 | +65% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 2223 | 19 | +3% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1345 | 14 | +35% | -77% | -77% | -74% |
| Momentum model ≥ 10% | 908 | 9 | +40% | -70% | -70% | -66% |
| Mean-reversion model ≥ 2% | 4413 | 31 | -23% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 3025 | 24 | -12% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1992 | 14 | -19% | -80% | -80% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12205 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4511 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1723 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 18439 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 71 | 0% | -$1,240.10 | -56% | — |
| Sell at 2¢ | 647 | 4% | -$2,023.88 | -91% | 34 sec |
| Sell at 3¢ | 434 | 2% | -$2,022.84 | -91% | 46 sec |
| Sell at 5¢ | 317 | 2% | -$1,986.05 | -89% | 49 sec |
| Sell at 10¢ | 200 | 1% | -$1,902.10 | -85% | 64 sec |
| Sell at 25¢ | 116 | 1% | -$1,752.14 | -78% | 80 sec |
| Sell at 50¢ | 77 | 0% | -$1,546.35 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 578 | 5 | 10% | 3% | -18% | -82% | -87% |
| 2–5 min | 5942 | 35 | 7% | 3% | -42% | -88% | -88% |
| 1–2 min | 4815 | 18 | 3% | 2% | -59% | -94% | -93% |
| Under 1 min | 7100 | 13 | 1% | 0% | -73% | -92% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1369 | 11 | 5% | 3% | +0% | -89% | -89% |
| HYPE | 1363 | 4 | 4% | 2% | -64% | -90% | -89% |
| ETH | 1360 | 8 | 5% | 3% | -28% | -88% | -87% |
| DOGE | 1360 | 2 | 4% | 2% | -82% | -91% | -90% |
| BNB | 1359 | 5 | 4% | 2% | -55% | -90% | -90% |
| SOL | 1356 | 2 | 3% | 1% | -82% | -93% | -92% |
| BTC | 1347 | 6 | 5% | 2% | -40% | -88% | -91% |
| XRP | 1346 | 7 | 2% | 1% | -36% | -86% | -86% |
| NEAR | 1345 | 8 | 5% | 3% | -22% | -77% | -78% |
| GOLD | 731 | 1 | 4% | 1% | -84% | -91% | -93% |
| SILVER | 718 | 2 | 3% | 1% | -68% | -94% | -94% |
| WTI | 690 | 3 | 3% | 1% | -50% | -94% | -96% |
| COPPER | 637 | 1 | 2% | 2% | -85% | -97% | -96% |
| PLATINUM | 609 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 565 | 1 | 1% | 0% | -83% | -98% | -98% |
| NATGAS | 561 | 3 | 2% | 2% | -50% | -96% | -95% |
| EURUSD | 544 | 3 | 3% | 1% | -49% | -78% | -78% |
| GBPUSD | 511 | 1 | 2% | 1% | -82% | -97% | -96% |
| USDJPY | 465 | 3 | 1% | 1% | -40% | -99% | -98% |
| AUDUSD | 106 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 97 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9307 | 35 | 3% | 2% | -57% | -90% | -90% |
| DOWN (bought NO) | 9132 | 36 | 4% | 2% | -54% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2100 | 10 | 2% | 1% | -20% | -78% | -78% |
| 0.05–0.1% | 2150 | 7 | 3% | 1% | -53% | -92% | -91% |
| 0.1–0.2% | 3100 | 10 | 4% | 2% | -60% | -91% | -91% |
| 0.2–0.5% | 3499 | 20 | 6% | 3% | -37% | -88% | -88% |
| Over 0.5% | 1353 | 6 | 6% | 2% | -54% | -89% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4717 | 20 | 4% | 2% | -52% | -87% | -88% |
| Morning (6am–12pm) | 4329 | 23 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 4389 | 13 | 3% | 1% | -65% | -90% | -91% |
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
| 10/14 4:29:45 PM | GOLD | DOWN | 15 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/14 4:29:45 PM | SILVER | DOWN | 15 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/14 4:29:45 PM | WTI | UP | 15 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/14 4:29:45 PM | BNB | UP | 15 sec | -0.008% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:29:45 PM | COPPER | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:29:26 PM | NEAR | DOWN | 33 sec | +0.165% | 0¢ | ❌ Lost | $0.00 |
| 10/14 4:29:10 PM | GBPUSD | DOWN | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:29:10 PM | DOGE | DOWN | 49 sec | +0.099% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 4:29:10 PM | USDJPY | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:28:54 PM | HYPE | UP | 65 sec | -0.142% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 4:28:54 PM | XRP | DOWN | 65 sec | +0.068% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:28:38 PM | USDCAD | UP | 82 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:28:02 PM | BTC | UP | 2.0 min | -0.162% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 4:28:02 PM | ZEC | DOWN | 2.0 min | +0.359% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 4:27:46 PM | SOL | UP | 2.2 min | -0.248% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:27:31 PM | EURUSD | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:14:53 PM | NEAR | UP | 7 sec | -0.215% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:14:34 PM | USDJPY | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:14:34 PM | NATGAS | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:14:34 PM | WTI | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:13:26 PM | EURUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:12:38 PM | GBPUSD | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:12:04 PM | BTC | UP | 2.9 min | -0.215% | 3¢ | ❌ Lost | -$0.15 |
| 10/14 4:12:04 PM | ZEC | UP | 2.9 min | -0.715% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 4:11:48 PM | SOL | UP | 3.2 min | -0.350% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 4:11:48 PM | XRP | UP | 3.2 min | -0.352% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 4:11:33 PM | HYPE | UP | 3.4 min | -0.402% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:11:07 PM | DOGE | UP | 3.9 min | -0.359% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 4:11:07 PM | ETH | UP | 3.9 min | -0.328% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 4:10:51 PM | BNB | UP | 4.2 min | -0.202% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
