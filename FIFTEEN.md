# 15-Minute 1¢ Study

*Updated Tue Oct 13, 6:30 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1305 finished bets | 1% | $38.90 | +27% | +2.98¢ | $27.95 / $10.95 |

*Expect about **83 buys a day** (~$12.43/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1241 | $20.50 | +15% |
| 5+ min left, hold to the close | 496 | -$17.05 | -23% |
| Volatility model ≥ 5%, sell at 50¢ | 1305 | -$20.10 | -14% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 17071 | 17052 | 64 (0%) | 1.07% | -$1,167.10 (-57%) | Hold to the close: -$1,167.10 (-57%) |

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
| Volatility model | 11239 | 4.4% | 0.4% (46) | -658% | ❌ Worse |
| Momentum model | 11239 | 4.4% | 0.4% (46) | -686% | ❌ Worse |
| Mean-reversion model | 11239 | 7.2% | 0.4% (46) | -773% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 11239 | 46 | -49% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2328 | 18 | -10% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1305 | 13 | +27% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 800 | 9 | +61% | -64% | -63% | -60% |
| Momentum model ≥ 2% | 2038 | 15 | -11% | -80% | -80% | -78% |
| Momentum model ≥ 5% | 1241 | 11 | +15% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 845 | 8 | +34% | -70% | -69% | -65% |
| Mean-reversion model ≥ 2% | 4043 | 27 | -27% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2762 | 20 | -20% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 1821 | 14 | -11% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 11437 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4116 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1499 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 17052 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 64 | 0% | -$1,167.10 | -57% | — |
| Sell at 2¢ | 585 | 3% | -$1,869.00 | -91% | 33 sec |
| Sell at 3¢ | 388 | 2% | -$1,869.78 | -91% | 46 sec |
| Sell at 5¢ | 279 | 2% | -$1,839.75 | -89% | 48 sec |
| Sell at 10¢ | 177 | 1% | -$1,761.23 | -85% | 63 sec |
| Sell at 25¢ | 100 | 1% | -$1,634.10 | -79% | 78 sec |
| Sell at 50¢ | 65 | 0% | -$1,470.35 | -71% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 492 | 4 | 11% | 3% | -23% | -81% | -87% |
| 2–5 min | 5502 | 32 | 6% | 3% | -43% | -88% | -88% |
| 1–2 min | 4497 | 17 | 3% | 2% | -59% | -94% | -94% |
| Under 1 min | 6557 | 11 | 1% | 0% | -76% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1284 | 7 | 4% | 2% | -32% | -90% | -90% |
| HYPE | 1278 | 4 | 4% | 2% | -61% | -90% | -89% |
| BNB | 1275 | 5 | 4% | 1% | -52% | -91% | -91% |
| ETH | 1274 | 8 | 5% | 3% | -23% | -89% | -88% |
| DOGE | 1274 | 2 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1269 | 2 | 3% | 1% | -80% | -93% | -92% |
| BTC | 1263 | 6 | 5% | 2% | -37% | -88% | -91% |
| XRP | 1261 | 7 | 2% | 1% | -31% | -85% | -86% |
| NEAR | 1259 | 7 | 5% | 2% | -27% | -77% | -78% |
| GOLD | 674 | 1 | 4% | 1% | -83% | -92% | -94% |
| SILVER | 659 | 1 | 3% | 1% | -83% | -94% | -94% |
| WTI | 632 | 3 | 3% | 1% | -46% | -94% | -96% |
| COPPER | 580 | 0 | 1% | 1% | -100% | -98% | -97% |
| PLATINUM | 550 | 0 | 0% | 0% | -100% | -99% | -99% |
| PALLADIUM | 512 | 1 | 1% | 0% | -82% | -98% | -98% |
| NATGAS | 509 | 3 | 3% | 2% | -45% | -96% | -94% |
| EURUSD | 492 | 3 | 3% | 2% | -43% | -76% | -76% |
| GBPUSD | 465 | 1 | 2% | 1% | -80% | -96% | -96% |
| USDJPY | 419 | 3 | 1% | 1% | -33% | -98% | -98% |
| AUDUSD | 65 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 58 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8586 | 35 | 3% | 2% | -53% | -90% | -90% |
| DOWN (bought NO) | 8466 | 29 | 3% | 2% | -60% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2000 | 10 | 2% | 1% | -17% | -77% | -77% |
| 0.05–0.1% | 2030 | 6 | 3% | 1% | -57% | -92% | -92% |
| 0.1–0.2% | 2927 | 9 | 4% | 2% | -62% | -91% | -91% |
| 0.2–0.5% | 3224 | 18 | 5% | 3% | -39% | -89% | -89% |
| Over 0.5% | 1253 | 5 | 6% | 2% | -59% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4344 | 20 | 4% | 2% | -47% | -87% | -87% |
| Morning (6am–12pm) | 3923 | 20 | 4% | 2% | -41% | -91% | -91% |
| Afternoon (12–6pm) | 4113 | 10 | 3% | 1% | -71% | -91% | -91% |
| Evening (6pm–12am) | 4672 | 14 | 3% | 1% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,531 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/13 6:29:54 PM | USDJPY | DOWN | 5 sec | — | 0¢ | In play | — |
| 10/13 6:28:52 PM | EURUSD | UP | 67 sec | — | 0¢ | In play | — |
| 10/13 6:28:36 PM | GOLD | UP | 83 sec | — | 5¢ | In play | — |
| 10/13 6:28:36 PM | BTC | DOWN | 83 sec | +0.062% | 0¢ | In play | — |
| 10/13 6:28:20 PM | COPPER | UP | 1.6 min | — | 12¢ | In play | — |
| 10/13 6:28:04 PM | PLATINUM | UP | 1.9 min | — | 0¢ | In play | — |
| 10/13 6:28:04 PM | PALLADIUM | UP | 1.9 min | — | 1¢ | In play | — |
| 10/13 6:28:04 PM | WTI | DOWN | 1.9 min | — | 1¢ | In play | — |
| 10/13 6:27:48 PM | BNB | DOWN | 2.2 min | +0.063% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 6:26:59 PM | ETH | DOWN | 3.0 min | +0.137% | 0¢ | In play | — |
| 10/13 6:26:43 PM | DOGE | DOWN | 3.3 min | +0.180% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 6:25:55 PM | XRP | DOWN | 4.1 min | +0.205% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 6:25:55 PM | SOL | DOWN | 4.1 min | +0.246% | 1¢ | In play | — |
| 10/13 6:25:37 PM | ZEC | DOWN | 4.4 min | +0.356% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 6:25:37 PM | HYPE | DOWN | 4.4 min | +0.145% | 1¢ | In play | — |
| 10/13 6:24:17 PM | NEAR | DOWN | 5.7 min | +0.841% | 1¢ | In play | — |
| 10/13 6:14:53 PM | PLATINUM | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 6:14:05 PM | PALLADIUM | DOWN | 54 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 6:13:49 PM | GBPUSD | DOWN | 70 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 6:13:33 PM | USDCAD | UP | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 6:13:33 PM | AUDUSD | DOWN | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 6:13:01 PM | NATGAS | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 6:13:01 PM | EURUSD | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 6:11:57 PM | XRP | DOWN | 3.0 min | +0.257% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 6:11:25 PM | NEAR | DOWN | 3.6 min | +0.579% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 6:11:25 PM | SOL | DOWN | 3.6 min | +0.266% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 6:11:25 PM | HYPE | DOWN | 3.6 min | +0.241% | 0¢ | ❌ Lost | $0.00 |
| 10/13 6:11:09 PM | ZEC | DOWN | 3.9 min | +0.337% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 6:10:53 PM | BTC | DOWN | 4.1 min | +0.182% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 6:10:22 PM | BNB | DOWN | 4.6 min | +0.124% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
