# 15-Minute 1¢ Study

*Updated Thu Oct 8, 10:25 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 784 finished bets | 1% | $27.55 | +33% | +3.51¢ | -$13.55 / $41.10 |

*Expect about **75 buys a day** (~$11.30/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 777 | $15.20 | +18% |
| 5+ min left, hold to the close | 332 | $6.95 | +14% |
| Volatility model ≥ 5%, sell at 50¢ | 784 | -$2.45 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 11836 | 11828 | 49 (0%) | 1.07% | -$751.30 (-52%) | Hold to the close: -$751.30 (-52%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 7584 | 4.0% | 0.4% (33) | -568% | ❌ Worse |
| Momentum model | 7584 | 4.1% | 0.4% (33) | -599% | ❌ Worse |
| Mean-reversion model | 7584 | 6.7% | 0.4% (33) | -665% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7584 | 33 | -45% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 1442 | 12 | -3% | -74% | -74% | -70% |
| Volatility model ≥ 5% | 784 | 8 | +33% | -64% | -63% | -60% |
| Volatility model ≥ 10% | 488 | 6 | +82% | -47% | -48% | -43% |
| Momentum model ≥ 2% | 1278 | 10 | -6% | -74% | -76% | -73% |
| Momentum model ≥ 5% | 777 | 7 | +18% | -68% | -69% | -67% |
| Momentum model ≥ 10% | 535 | 6 | +62% | -57% | -58% | -54% |
| Mean-reversion model ≥ 2% | 2614 | 19 | -21% | -84% | -85% | -80% |
| Mean-reversion model ≥ 5% | 1765 | 15 | -6% | -82% | -81% | -76% |
| Mean-reversion model ≥ 10% | 1166 | 11 | +9% | -80% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7781 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3015 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1032 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 11828 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 49 | 0% | -$751.30 | -52% | — |
| Sell at 2¢ | 411 | 3% | -$1,288.44 | -90% | 33 sec |
| Sell at 3¢ | 272 | 2% | -$1,289.22 | -90% | 47 sec |
| Sell at 5¢ | 201 | 2% | -$1,264.65 | -88% | 50 sec |
| Sell at 10¢ | 131 | 1% | -$1,209.69 | -84% | 64 sec |
| Sell at 25¢ | 75 | 1% | -$1,105.05 | -77% | 82 sec |
| Sell at 50¢ | 49 | 0% | -$980.55 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 328 | 4 | 11% | 4% | +16% | -81% | -84% |
| 2–5 min | 3856 | 25 | 7% | 3% | -37% | -88% | -89% |
| 1–2 min | 3100 | 12 | 3% | 2% | -58% | -94% | -94% |
| Under 1 min | 4540 | 8 | 1% | 0% | -74% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 872 | 6 | 5% | 3% | -18% | -90% | -90% |
| HYPE | 871 | 3 | 5% | 3% | -57% | -89% | -87% |
| DOGE | 867 | 2 | 3% | 1% | -71% | -92% | -91% |
| BNB | 866 | 3 | 4% | 2% | -58% | -91% | -92% |
| ETH | 865 | 7 | 5% | 3% | +0% | -89% | -88% |
| NEAR | 861 | 5 | 6% | 3% | -24% | -71% | -73% |
| SOL | 861 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 860 | 4 | 5% | 2% | -39% | -88% | -90% |
| XRP | 858 | 5 | 2% | 1% | -27% | -81% | -81% |
| GOLD | 503 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 491 | 0 | 3% | 1% | -100% | -94% | -94% |
| WTI | 465 | 3 | 3% | 1% | -29% | -95% | -97% |
| COPPER | 431 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 394 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 369 | 3 | 3% | 2% | -24% | -95% | -93% |
| PALLADIUM | 362 | 1 | 1% | 1% | -74% | -98% | -99% |
| EURUSD | 361 | 3 | 3% | 2% | -22% | -68% | -67% |
| GBPUSD | 342 | 1 | 3% | 2% | -73% | -95% | -95% |
| USDJPY | 306 | 3 | 1% | 1% | -8% | -98% | -97% |
| AUDUSD | 13 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 10 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6039 | 26 | 4% | 2% | -50% | -89% | -88% |
| DOWN (bought NO) | 5789 | 23 | 3% | 2% | -54% | -91% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1264 | 8 | 2% | 1% | +9% | -67% | -66% |
| 0.05–0.1% | 1312 | 4 | 3% | 1% | -55% | -91% | -92% |
| 0.1–0.2% | 1970 | 6 | 4% | 2% | -62% | -92% | -92% |
| 0.2–0.5% | 2294 | 12 | 5% | 3% | -43% | -89% | -88% |
| Over 0.5% | 939 | 5 | 6% | 2% | -45% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3090 | 17 | 4% | 2% | -37% | -85% | -85% |
| Morning (6am–12pm) | 2911 | 17 | 4% | 2% | -34% | -91% | -90% |
| Afternoon (12–6pm) | 2560 | 7 | 3% | 1% | -68% | -88% | -89% |
| Evening (6pm–12am) | 3267 | 8 | 3% | 1% | -72% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,056 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/8 10:24:22 AM | WTI | UP | 5.6 min | — | — | In play | — |
| 10/8 10:14:56 AM | SILVER | UP | 3 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/8 10:14:56 AM | BTC | DOWN | 3 sec | -0.018% | 0¢ | ❌ Lost | $0.00 |
| 10/8 10:14:41 AM | PLATINUM | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 10:14:25 AM | NATGAS | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 10:14:25 AM | USDJPY | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 10:14:25 AM | SOL | UP | 34 sec | -0.217% | 0¢ | ❌ Lost | $0.00 |
| 10/8 10:14:09 AM | ETH | UP | 50 sec | -0.279% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 10:14:09 AM | BNB | UP | 50 sec | -0.198% | 0¢ | ❌ Lost | $0.00 |
| 10/8 10:13:38 AM | NEAR | DOWN | 81 sec | +1.034% | 0¢ | ❌ Lost | $0.00 |
| 10/8 10:13:38 AM | DOGE | DOWN | 81 sec | +0.433% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 10:12:19 AM | WTI | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 10:11:47 AM | XRP | DOWN | 3.2 min | +0.632% | 7¢ | ❌ Lost | -$0.15 |
| 10/8 10:11:15 AM | HYPE | DOWN | 3.7 min | +0.762% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 10:10:43 AM | ZEC | DOWN | 4.3 min | +1.932% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 9:59:51 AM | USDCAD | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 9:59:04 AM | SILVER | UP | 56 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 9:59:04 AM | HYPE | UP | 56 sec | -0.205% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 9:58:48 AM | WTI | UP | 72 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 9:58:33 AM | XRP | UP | 87 sec | -0.540% | 0¢ | ❌ Lost | $0.00 |
| 10/8 9:58:33 AM | NEAR | UP | 87 sec | -1.113% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 9:58:33 AM | GBPUSD | UP | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 9:58:33 AM | SOL | UP | 87 sec | -0.487% | 0¢ | ❌ Lost | $0.00 |
| 10/8 9:58:17 AM | BTC | UP | 1.7 min | -0.213% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 9:58:01 AM | NATGAS | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 9:56:57 AM | ETH | UP | 3.0 min | -0.838% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 9:56:57 AM | DOGE | UP | 3.0 min | -1.055% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 9:56:57 AM | GOLD | UP | 3.0 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/8 9:56:41 AM | EURUSD | UP | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 9:56:26 AM | BNB | UP | 3.5 min | -0.454% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
