# 15-Minute 1¢ Study

*Updated Thu Oct 8, 12:06 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 761 finished bets | 1% | $30.10 | +37% | +3.96¢ | -$12.80 / $42.90 |

*Expect about **76 buys a day** (~$11.44/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 758 | $17.30 | +21% |
| 5+ min left, hold to the close | 302 | $11.30 | +25% |
| Volatility model ≥ 2%, hold to the close | 1396 | $0.15 | +0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 11430 | 11423 | 49 (0%) | 1.07% | -$699.85 (-50%) | Hold to the close: -$699.85 (-50%) |

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
| Volatility model | 7362 | 4.0% | 0.4% (33) | -564% | ❌ Worse |
| Momentum model | 7362 | 4.1% | 0.4% (33) | -596% | ❌ Worse |
| Mean-reversion model | 7362 | 6.7% | 0.4% (33) | -658% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7362 | 33 | -44% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 1396 | 12 | +0% | -73% | -73% | -69% |
| Volatility model ≥ 5% | 761 | 8 | +37% | -63% | -61% | -58% |
| Volatility model ≥ 10% | 476 | 6 | +85% | -46% | -47% | -42% |
| Momentum model ≥ 2% | 1240 | 10 | -3% | -74% | -75% | -73% |
| Momentum model ≥ 5% | 758 | 7 | +21% | -67% | -69% | -66% |
| Momentum model ≥ 10% | 525 | 6 | +64% | -56% | -57% | -54% |
| Mean-reversion model ≥ 2% | 2522 | 19 | -18% | -84% | -85% | -80% |
| Mean-reversion model ≥ 5% | 1705 | 15 | -3% | -81% | -81% | -76% |
| Mean-reversion model ≥ 10% | 1127 | 11 | +12% | -80% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7559 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2893 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 971 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 11423 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 49 | 0% | -$699.85 | -50% | — |
| Sell at 2¢ | 399 | 3% | -$1,240.11 | -89% | 33 sec |
| Sell at 3¢ | 266 | 2% | -$1,240.11 | -89% | 47 sec |
| Sell at 5¢ | 197 | 2% | -$1,215.80 | -88% | 51 sec |
| Sell at 10¢ | 131 | 1% | -$1,158.24 | -84% | 64 sec |
| Sell at 25¢ | 75 | 1% | -$1,053.60 | -76% | 82 sec |
| Sell at 50¢ | 49 | 0% | -$929.10 | -67% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 298 | 4 | 11% | 4% | +27% | -81% | -85% |
| 2–5 min | 3695 | 25 | 7% | 3% | -34% | -88% | -88% |
| 1–2 min | 3008 | 12 | 3% | 2% | -57% | -94% | -94% |
| Under 1 min | 4418 | 8 | 1% | 0% | -73% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 847 | 6 | 5% | 3% | -16% | -90% | -90% |
| HYPE | 847 | 3 | 5% | 3% | -56% | -89% | -87% |
| DOGE | 842 | 2 | 3% | 1% | -70% | -92% | -92% |
| BNB | 841 | 3 | 4% | 2% | -57% | -90% | -92% |
| ETH | 840 | 7 | 5% | 3% | +3% | -88% | -88% |
| NEAR | 837 | 5 | 6% | 3% | -22% | -71% | -72% |
| SOL | 836 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 835 | 4 | 5% | 2% | -37% | -88% | -90% |
| XRP | 834 | 5 | 2% | 1% | -25% | -81% | -81% |
| GOLD | 484 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 470 | 0 | 3% | 1% | -100% | -95% | -94% |
| WTI | 448 | 3 | 2% | 1% | -27% | -95% | -97% |
| COPPER | 412 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 375 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 355 | 3 | 3% | 2% | -21% | -95% | -93% |
| PALLADIUM | 349 | 1 | 1% | 1% | -73% | -98% | -99% |
| EURUSD | 346 | 3 | 3% | 2% | -19% | -67% | -66% |
| GBPUSD | 327 | 1 | 3% | 2% | -71% | -95% | -95% |
| USDJPY | 290 | 3 | 1% | 1% | -3% | -98% | -96% |
| AUDUSD | 5 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 3 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5809 | 26 | 4% | 2% | -48% | -88% | -88% |
| DOWN (bought NO) | 5614 | 23 | 3% | 2% | -53% | -91% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1244 | 8 | 2% | 1% | +11% | -66% | -66% |
| 0.05–0.1% | 1298 | 4 | 3% | 1% | -55% | -91% | -92% |
| 0.1–0.2% | 1929 | 6 | 4% | 2% | -61% | -92% | -92% |
| 0.2–0.5% | 2209 | 12 | 6% | 3% | -40% | -89% | -88% |
| Over 0.5% | 877 | 5 | 6% | 3% | -42% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2890 | 17 | 4% | 2% | -32% | -84% | -84% |
| Morning (6am–12pm) | 2706 | 17 | 4% | 2% | -28% | -91% | -90% |
| Afternoon (12–6pm) | 2560 | 7 | 3% | 1% | -68% | -88% | -89% |
| Evening (6pm–12am) | 3267 | 8 | 3% | 1% | -72% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,100 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/7 11:59:50 PM | NATGAS | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 11:59:34 PM | USDJPY | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 11:59:18 PM | ZEC | UP | 42 sec | -0.071% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 11:58:15 PM | NEAR | UP | 1.7 min | -0.748% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 11:58:15 PM | WTI | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 11:57:25 PM | PLATINUM | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 11:57:09 PM | HYPE | UP | 2.9 min | -0.326% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 11:57:09 PM | BTC | UP | 2.9 min | -0.208% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 11:56:54 PM | PALLADIUM | UP | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 11:56:54 PM | XRP | UP | 3.1 min | -0.271% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 11:56:54 PM | SILVER | UP | 3.1 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/7 11:56:54 PM | DOGE | UP | 3.1 min | -0.369% | 0¢ | ❌ Lost | $0.00 |
| 10/7 11:56:54 PM | GOLD | UP | 3.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 11:56:54 PM | SOL | UP | 3.1 min | -0.314% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 11:56:54 PM | AUDUSD | UP | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 11:56:54 PM | GBPUSD | UP | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 11:56:54 PM | EURUSD | UP | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 11:56:54 PM | ETH | UP | 3.1 min | -0.266% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 11:56:54 PM | COPPER | UP | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 11:56:54 PM | BNB | UP | 3.1 min | -0.312% | 0¢ | ❌ Lost | $0.00 |
| 10/7 10:23:47 PM | ZEC | UP | 6.2 min | -3.869% | — | ❌ Lost | -$0.15 |
| 10/7 10:14:50 PM | EURUSD | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 10:14:33 PM | NEAR | UP | 27 sec | -0.369% | 0¢ | ❌ Lost | $0.00 |
| 10/7 10:14:33 PM | GBPUSD | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 10:14:17 PM | PLATINUM | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 10:14:17 PM | PALLADIUM | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 10:14:17 PM | ETH | UP | 43 sec | -0.071% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 10:14:01 PM | DOGE | UP | 59 sec | -0.113% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 10:13:46 PM | ZEC | UP | 73 sec | -0.321% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 10:13:46 PM | BTC | UP | 73 sec | -0.120% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
