# 15-Minute 1¢ Study

*Updated Wed Oct 7, 9:46 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 760 finished bets | 1% | $30.25 | +37% | +3.98¢ | -$12.80 / $43.05 |

*Expect about **77 buys a day** (~$11.54/day at risk); max loss per buy **15¢**.*

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
| 11380 | 11374 | 49 (0%) | 1.07% | -$693.55 (-50%) | Hold to the close: -$693.55 (-50%) |

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
| Volatility model | 7335 | 4.1% | 0.4% (33) | -565% | ❌ Worse |
| Momentum model | 7335 | 4.1% | 0.4% (33) | -597% | ❌ Worse |
| Mean-reversion model | 7335 | 6.7% | 0.4% (33) | -659% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7335 | 33 | -44% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 1395 | 12 | +0% | -73% | -73% | -69% |
| Volatility model ≥ 5% | 760 | 8 | +37% | -63% | -61% | -58% |
| Volatility model ≥ 10% | 476 | 6 | +85% | -46% | -47% | -42% |
| Momentum model ≥ 2% | 1239 | 10 | -2% | -74% | -75% | -73% |
| Momentum model ≥ 5% | 757 | 7 | +22% | -67% | -69% | -66% |
| Momentum model ≥ 10% | 524 | 6 | +65% | -56% | -57% | -53% |
| Mean-reversion model ≥ 2% | 2512 | 19 | -18% | -84% | -85% | -80% |
| Mean-reversion model ≥ 5% | 1702 | 15 | -2% | -81% | -81% | -76% |
| Mean-reversion model ≥ 10% | 1127 | 11 | +12% | -80% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7532 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2879 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 963 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 11374 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 49 | 0% | -$693.55 | -50% | — |
| Sell at 2¢ | 398 | 3% | -$1,234.07 | -89% | 33 sec |
| Sell at 3¢ | 265 | 2% | -$1,234.20 | -89% | 47 sec |
| Sell at 5¢ | 197 | 2% | -$1,209.50 | -88% | 51 sec |
| Sell at 10¢ | 131 | 1% | -$1,151.94 | -84% | 64 sec |
| Sell at 25¢ | 75 | 1% | -$1,047.30 | -76% | 82 sec |
| Sell at 50¢ | 49 | 0% | -$922.80 | -67% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 298 | 4 | 11% | 4% | +27% | -81% | -85% |
| 2–5 min | 3672 | 25 | 7% | 3% | -34% | -88% | -88% |
| 1–2 min | 2994 | 12 | 3% | 2% | -57% | -94% | -93% |
| Under 1 min | 4406 | 8 | 1% | 0% | -73% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 844 | 6 | 5% | 3% | -15% | -90% | -90% |
| HYPE | 844 | 3 | 5% | 3% | -56% | -89% | -87% |
| DOGE | 839 | 2 | 3% | 1% | -70% | -92% | -92% |
| BNB | 838 | 3 | 4% | 2% | -57% | -90% | -92% |
| ETH | 837 | 7 | 5% | 3% | +4% | -88% | -88% |
| NEAR | 834 | 5 | 6% | 3% | -21% | -71% | -72% |
| SOL | 833 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 832 | 4 | 5% | 2% | -37% | -88% | -90% |
| XRP | 831 | 5 | 2% | 1% | -24% | -81% | -81% |
| GOLD | 482 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 468 | 0 | 3% | 1% | -100% | -95% | -94% |
| WTI | 446 | 3 | 2% | 1% | -26% | -95% | -97% |
| COPPER | 411 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 373 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 353 | 3 | 3% | 2% | -21% | -95% | -93% |
| PALLADIUM | 346 | 1 | 1% | 1% | -73% | -97% | -98% |
| EURUSD | 344 | 3 | 3% | 2% | -19% | -67% | -65% |
| GBPUSD | 325 | 1 | 3% | 2% | -71% | -95% | -95% |
| USDJPY | 287 | 3 | 1% | 1% | -2% | -98% | -96% |
| AUDUSD | 4 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 3 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5767 | 26 | 4% | 2% | -48% | -88% | -88% |
| DOWN (bought NO) | 5607 | 23 | 3% | 2% | -53% | -91% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1244 | 8 | 2% | 1% | +11% | -66% | -66% |
| 0.05–0.1% | 1295 | 4 | 3% | 1% | -55% | -91% | -92% |
| 0.1–0.2% | 1921 | 6 | 4% | 2% | -61% | -92% | -92% |
| 0.2–0.5% | 2195 | 12 | 6% | 3% | -40% | -89% | -88% |
| Over 0.5% | 875 | 5 | 6% | 3% | -41% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2890 | 17 | 4% | 2% | -32% | -84% | -84% |
| Morning (6am–12pm) | 2706 | 17 | 4% | 2% | -28% | -91% | -90% |
| Afternoon (12–6pm) | 2560 | 7 | 3% | 1% | -68% | -88% | -89% |
| Evening (6pm–12am) | 3218 | 8 | 3% | 1% | -71% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,097 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
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
| 10/7 9:29:19 PM | ZEC | UP | 41 sec | -0.229% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 9:29:19 PM | EURUSD | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 9:29:19 PM | WTI | UP | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 9:29:03 PM | SOL | DOWN | 57 sec | +0.105% | 0¢ | ❌ Lost | $0.00 |
| 10/7 9:29:03 PM | ETH | DOWN | 57 sec | +0.064% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 9:28:48 PM | BNB | UP | 71 sec | -0.146% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 9:28:48 PM | NATGAS | UP | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 9:28:32 PM | HYPE | DOWN | 88 sec | +0.140% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 9:26:57 PM | NEAR | DOWN | 3.0 min | +1.193% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 9:24:20 PM | GOLD | DOWN | 5.7 min | — | 13¢ | ❌ Lost | -$0.15 |
| 10/7 9:14:56 PM | USDJPY | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 9:14:25 PM | PLATINUM | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
