# 15-Minute 1¢ Study

*Updated Wed Oct 7, 10:06 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 760 finished bets | 1% | $30.25 | +37% | +3.98¢ | -$12.80 / $43.05 |

*Expect about **77 buys a day** (~$11.52/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 757 | $17.45 | +22% |
| 5+ min left, hold to the close | 302 | $11.30 | +25% |
| Volatility model ≥ 2%, hold to the close | 1395 | $0.30 | +0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 11392 | 11386 | 49 (0%) | 1.07% | -$695.05 (-50%) | Hold to the close: -$695.05 (-50%) |

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
| Volatility model | 7344 | 4.1% | 0.4% (33) | -565% | ❌ Worse |
| Momentum model | 7344 | 4.1% | 0.4% (33) | -597% | ❌ Worse |
| Mean-reversion model | 7344 | 6.7% | 0.4% (33) | -659% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7344 | 33 | -44% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 1395 | 12 | +0% | -73% | -73% | -69% |
| Volatility model ≥ 5% | 760 | 8 | +37% | -63% | -61% | -58% |
| Volatility model ≥ 10% | 476 | 6 | +85% | -46% | -47% | -42% |
| Momentum model ≥ 2% | 1239 | 10 | -2% | -74% | -75% | -73% |
| Momentum model ≥ 5% | 757 | 7 | +22% | -67% | -69% | -66% |
| Momentum model ≥ 10% | 524 | 6 | +65% | -56% | -57% | -53% |
| Mean-reversion model ≥ 2% | 2515 | 19 | -18% | -84% | -85% | -80% |
| Mean-reversion model ≥ 5% | 1704 | 15 | -2% | -81% | -81% | -76% |
| Mean-reversion model ≥ 10% | 1127 | 11 | +12% | -80% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7541 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2881 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 964 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 11386 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 49 | 0% | -$695.05 | -50% | — |
| Sell at 2¢ | 398 | 3% | -$1,235.57 | -89% | 33 sec |
| Sell at 3¢ | 265 | 2% | -$1,235.70 | -89% | 47 sec |
| Sell at 5¢ | 197 | 2% | -$1,211.00 | -88% | 51 sec |
| Sell at 10¢ | 131 | 1% | -$1,153.44 | -84% | 64 sec |
| Sell at 25¢ | 75 | 1% | -$1,048.80 | -76% | 82 sec |
| Sell at 50¢ | 49 | 0% | -$924.30 | -67% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 298 | 4 | 11% | 4% | +27% | -81% | -85% |
| 2–5 min | 3674 | 25 | 7% | 3% | -34% | -88% | -88% |
| 1–2 min | 3002 | 12 | 3% | 2% | -57% | -94% | -94% |
| Under 1 min | 4408 | 8 | 1% | 0% | -73% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 845 | 6 | 5% | 3% | -16% | -90% | -90% |
| HYPE | 845 | 3 | 5% | 3% | -56% | -89% | -87% |
| DOGE | 840 | 2 | 3% | 1% | -70% | -92% | -92% |
| BNB | 839 | 3 | 4% | 2% | -57% | -90% | -92% |
| ETH | 838 | 7 | 5% | 3% | +4% | -88% | -88% |
| NEAR | 835 | 5 | 6% | 3% | -21% | -71% | -72% |
| SOL | 834 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 833 | 4 | 5% | 2% | -37% | -88% | -90% |
| XRP | 832 | 5 | 2% | 1% | -25% | -81% | -81% |
| GOLD | 482 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 468 | 0 | 3% | 1% | -100% | -95% | -94% |
| WTI | 447 | 3 | 2% | 1% | -26% | -95% | -97% |
| COPPER | 411 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 373 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 353 | 3 | 3% | 2% | -21% | -95% | -93% |
| PALLADIUM | 347 | 1 | 1% | 1% | -73% | -98% | -99% |
| EURUSD | 344 | 3 | 3% | 2% | -19% | -67% | -65% |
| GBPUSD | 325 | 1 | 3% | 2% | -71% | -95% | -95% |
| USDJPY | 288 | 3 | 1% | 1% | -3% | -98% | -96% |
| AUDUSD | 4 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 3 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5778 | 26 | 4% | 2% | -48% | -88% | -88% |
| DOWN (bought NO) | 5608 | 23 | 3% | 2% | -53% | -91% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1244 | 8 | 2% | 1% | +11% | -66% | -66% |
| 0.05–0.1% | 1296 | 4 | 3% | 1% | -55% | -91% | -92% |
| 0.1–0.2% | 1926 | 6 | 4% | 2% | -61% | -92% | -92% |
| 0.2–0.5% | 2197 | 12 | 6% | 3% | -40% | -89% | -88% |
| Over 0.5% | 876 | 5 | 6% | 3% | -41% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2890 | 17 | 4% | 2% | -32% | -84% | -84% |
| Morning (6am–12pm) | 2706 | 17 | 4% | 2% | -28% | -91% | -90% |
| Afternoon (12–6pm) | 2560 | 7 | 3% | 1% | -68% | -88% | -89% |
| Evening (6pm–12am) | 3230 | 8 | 3% | 1% | -72% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,098 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/7 9:59:45 PM | USDJPY | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 9:59:13 PM | PALLADIUM | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 9:58:57 PM | BTC | UP | 62 sec | -0.105% | 0¢ | ❌ Lost | $0.00 |
| 10/7 9:58:57 PM | ETH | UP | 62 sec | -0.118% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 9:58:57 PM | BNB | UP | 62 sec | -0.096% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 9:58:57 PM | DOGE | UP | 62 sec | -0.134% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 9:58:26 PM | NEAR | UP | 1.6 min | -0.605% | 0¢ | ❌ Lost | $0.00 |
| 10/7 9:58:10 PM | HYPE | UP | 1.8 min | -0.172% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 9:58:10 PM | SOL | UP | 1.8 min | -0.133% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 9:58:10 PM | XRP | UP | 1.8 min | -0.254% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 9:57:07 PM | WTI | DOWN | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 9:56:35 PM | ZEC | UP | 3.4 min | -0.418% | 2¢ | ❌ Lost | -$0.15 |
| 10/7 9:44:48 PM | XRP | UP | 11 sec | -0.106% | 0¢ | ❌ Lost | $0.00 |
| 10/7 9:44:34 PM | GOLD | DOWN | 26 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/7 9:44:34 PM | HYPE | UP | 26 sec | -0.043% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 9:44:18 PM | SOL | UP | 42 sec | -0.046% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 9:44:18 PM | DOGE | UP | 42 sec | -0.054% | 0¢ | ❌ Lost | $0.00 |
| 10/7 9:44:18 PM | ZEC | UP | 42 sec | -0.290% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 9:44:18 PM | USDJPY | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 9:44:02 PM | NEAR | UP | 58 sec | -0.288% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 9:43:46 PM | WTI | UP | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 9:43:13 PM | BTC | UP | 1.8 min | -0.156% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 9:43:13 PM | BNB | UP | 1.8 min | -0.135% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 9:43:13 PM | COPPER | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 9:42:57 PM | ETH | UP | 2.0 min | -0.155% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 9:42:10 PM | GBPUSD | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 9:41:24 PM | EURUSD | DOWN | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 9:29:35 PM | BTC | DOWN | 25 sec | +0.044% | 0¢ | ❌ Lost | $0.00 |
| 10/7 9:29:35 PM | XRP | DOWN | 25 sec | +0.021% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 9:29:19 PM | PLATINUM | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
