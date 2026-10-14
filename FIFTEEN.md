# 15-Minute 1¢ Study

*Updated Wed Oct 14, 1:33 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1414 finished bets | 1% | $67.85 | +43% | +4.80¢ | $36.10 / $31.75 |

*Expect about **86 buys a day** (~$12.83/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1328 | $38.75 | +27% |
| Momentum model ≥ 2%, hold to the close | 2195 | -$1.80 | -1% |
| Volatility model ≥ 2%, hold to the close | 2527 | -$10.95 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 18266 | 18259 | 69 (0%) | 1.07% | -$1,246.95 (-56%) | Hold to the close: -$1,246.95 (-56%) |

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
| Volatility model | 11901 | 4.5% | 0.4% (49) | -655% | ❌ Worse |
| Momentum model | 11901 | 4.4% | 0.4% (49) | -680% | ❌ Worse |
| Mean-reversion model | 11901 | 7.3% | 0.4% (49) | -777% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 11901 | 49 | -48% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2527 | 21 | -4% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 1414 | 16 | +43% | -73% | -71% | -66% |
| Volatility model ≥ 10% | 851 | 9 | +51% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 2195 | 18 | -1% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1328 | 13 | +27% | -77% | -77% | -74% |
| Momentum model ≥ 10% | 895 | 8 | +26% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 4363 | 30 | -25% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2990 | 23 | -15% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1972 | 14 | -18% | -80% | -80% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12099 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4467 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1693 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 18259 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 69 | 0% | -$1,246.95 | -56% | — |
| Sell at 2¢ | 635 | 3% | -$2,005.85 | -91% | 34 sec |
| Sell at 3¢ | 428 | 2% | -$2,004.03 | -91% | 46 sec |
| Sell at 5¢ | 313 | 2% | -$1,967.50 | -89% | 49 sec |
| Sell at 10¢ | 198 | 1% | -$1,883.57 | -85% | 64 sec |
| Sell at 25¢ | 114 | 1% | -$1,737.61 | -79% | 80 sec |
| Sell at 50¢ | 75 | 0% | -$1,538.70 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 574 | 4 | 10% | 2% | -34% | -82% | -88% |
| 2–5 min | 5893 | 34 | 7% | 3% | -43% | -88% | -88% |
| 1–2 min | 4777 | 18 | 3% | 2% | -59% | -94% | -93% |
| Under 1 min | 7011 | 13 | 1% | 0% | -73% | -92% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1356 | 9 | 5% | 3% | -17% | -89% | -90% |
| HYPE | 1352 | 4 | 4% | 2% | -63% | -90% | -89% |
| ETH | 1349 | 8 | 5% | 3% | -28% | -89% | -87% |
| DOGE | 1348 | 2 | 4% | 2% | -81% | -91% | -90% |
| BNB | 1348 | 5 | 5% | 2% | -55% | -90% | -89% |
| SOL | 1344 | 2 | 3% | 1% | -81% | -93% | -92% |
| BTC | 1335 | 6 | 5% | 2% | -40% | -88% | -91% |
| XRP | 1334 | 7 | 2% | 1% | -35% | -86% | -86% |
| NEAR | 1333 | 8 | 5% | 3% | -22% | -77% | -78% |
| GOLD | 724 | 1 | 4% | 1% | -84% | -91% | -93% |
| SILVER | 712 | 2 | 3% | 1% | -67% | -94% | -94% |
| WTI | 681 | 3 | 3% | 1% | -49% | -94% | -96% |
| COPPER | 631 | 1 | 2% | 1% | -85% | -97% | -96% |
| PLATINUM | 606 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 560 | 1 | 1% | 0% | -83% | -98% | -98% |
| NATGAS | 553 | 3 | 2% | 2% | -49% | -96% | -95% |
| EURUSD | 538 | 3 | 3% | 1% | -48% | -78% | -77% |
| GBPUSD | 505 | 1 | 2% | 1% | -82% | -97% | -96% |
| USDJPY | 460 | 3 | 1% | 1% | -39% | -98% | -98% |
| AUDUSD | 102 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 88 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9212 | 35 | 3% | 2% | -56% | -90% | -90% |
| DOWN (bought NO) | 9047 | 34 | 4% | 2% | -57% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2088 | 10 | 2% | 1% | -20% | -78% | -78% |
| 0.05–0.1% | 2134 | 7 | 3% | 1% | -53% | -92% | -91% |
| 0.1–0.2% | 3072 | 9 | 4% | 2% | -64% | -91% | -91% |
| 0.2–0.5% | 3453 | 20 | 6% | 3% | -36% | -88% | -88% |
| Over 0.5% | 1349 | 5 | 6% | 2% | -61% | -89% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4717 | 20 | 4% | 2% | -52% | -87% | -88% |
| Morning (6am–12pm) | 4329 | 23 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 4209 | 11 | 3% | 1% | -69% | -90% | -91% |
| Evening (6pm–12am) | 5004 | 15 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,503 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/14 1:29:45 PM | PLATINUM | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:29:29 PM | GBPUSD | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:29:29 PM | NEAR | DOWN | 31 sec | +0.204% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:29:14 PM | PALLADIUM | DOWN | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:29:14 PM | BTC | DOWN | 45 sec | +0.078% | 0¢ | ❌ Lost | $0.00 |
| 10/14 1:28:57 PM | XRP | DOWN | 62 sec | +0.068% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 1:28:25 PM | EURUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:27:50 PM | ZEC | DOWN | 2.2 min | +0.337% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 1:27:18 PM | NATGAS | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:27:18 PM | USDJPY | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:25:42 PM | DOGE | DOWN | 4.3 min | +0.289% | 2¢ | ❌ Lost | -$0.15 |
| 10/14 1:25:42 PM | ETH | DOWN | 4.3 min | +0.194% | 3¢ | ❌ Lost | -$0.15 |
| 10/14 1:25:10 PM | SOL | DOWN | 4.8 min | +0.405% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 1:25:10 PM | BNB | DOWN | 4.8 min | +0.129% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 1:24:54 PM | GOLD | DOWN | 5.1 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/14 1:24:54 PM | HYPE | DOWN | 5.1 min | +0.835% | 2¢ | ❌ Lost | -$0.15 |
| 10/14 1:24:54 PM | SILVER | DOWN | 5.1 min | — | 1¢ | ❌ Lost | $0.00 |
| 10/14 1:14:28 PM | AUDUSD | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:14:28 PM | EURUSD | DOWN | 32 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 1:14:28 PM | PALLADIUM | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:14:28 PM | ETH | UP | 32 sec | -0.050% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:14:13 PM | SOL | UP | 46 sec | -0.072% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:14:13 PM | HYPE | DOWN | 46 sec | +0.215% | 0¢ | ❌ Lost | $0.00 |
| 10/14 1:13:40 PM | BTC | DOWN | 79 sec | +0.054% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 1:13:24 PM | DOGE | UP | 1.6 min | -0.162% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:13:24 PM | SILVER | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 1:13:24 PM | PLATINUM | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:13:08 PM | GBPUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:12:02 PM | NEAR | UP | 3.0 min | -0.529% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:10:39 PM | BNB | UP | 4.3 min | -0.202% | 10¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
