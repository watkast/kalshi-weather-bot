# 15-Minute 1¢ Study

*Updated Fri Oct 16, 5:06 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1669 finished bets | 1% | $80.60 | +43% | +4.83¢ | $35.55 / $45.05 |

*Expect about **89 buys a day** (~$13.40/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1534 | $43.95 | +26% |
| Momentum model ≥ 2%, hold to the close | 2605 | -$7.80 | -3% |
| Volatility model ≥ 5%, sell at 50¢ | 1669 | -$21.90 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 21339 | 21332 | 80 (0%) | 1.07% | -$1,478.00 (-57%) | Hold to the close: -$1,478.00 (-57%) |

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
| Volatility model | 13623 | 4.4% | 0.4% (54) | -642% | ❌ Worse |
| Momentum model | 13623 | 4.4% | 0.4% (54) | -665% | ❌ Worse |
| Mean-reversion model | 13623 | 7.4% | 0.4% (54) | -775% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13623 | 54 | -50% | -88% | -88% | -85% |
| Volatility model ≥ 2% | 3058 | 24 | -9% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1669 | 19 | +43% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 964 | 11 | +63% | -65% | -64% | -61% |
| Momentum model ≥ 2% | 2605 | 21 | -3% | -80% | -81% | -77% |
| Momentum model ≥ 5% | 1534 | 15 | +26% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1022 | 10 | +38% | -72% | -72% | -66% |
| Mean-reversion model ≥ 2% | 5166 | 34 | -28% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3567 | 27 | -16% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2340 | 16 | -22% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13821 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5294 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 21332 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 80 | 0% | -$1,478.00 | -57% | — |
| Sell at 2¢ | 763 | 4% | -$2,301.62 | -89% | 41 sec |
| Sell at 3¢ | 513 | 2% | -$2,299.93 | -89% | 47 sec |
| Sell at 5¢ | 370 | 2% | -$2,259.50 | -87% | 50 sec |
| Sell at 10¢ | 222 | 1% | -$2,181.18 | -84% | 63 sec |
| Sell at 25¢ | 126 | 1% | -$2,012.94 | -77% | 80 sec |
| Sell at 50¢ | 83 | 0% | -$1,799.75 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 730 | 5 | 10% | 3% | -35% | -82% | -85% |
| 2–5 min | 6904 | 37 | 7% | 3% | -47% | -88% | -88% |
| 1–2 min | 5553 | 20 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 8141 | 18 | 1% | 0% | -68% | -88% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1552 | 11 | 5% | 3% | -12% | -89% | -90% |
| HYPE | 1547 | 5 | 4% | 2% | -60% | -90% | -89% |
| ETH | 1541 | 8 | 6% | 3% | -37% | -87% | -87% |
| BNB | 1538 | 6 | 5% | 2% | -52% | -89% | -89% |
| DOGE | 1537 | 2 | 4% | 2% | -84% | -91% | -90% |
| SOL | 1535 | 2 | 3% | 2% | -84% | -92% | -92% |
| XRP | 1526 | 7 | 2% | 1% | -43% | -86% | -87% |
| BTC | 1523 | 7 | 5% | 2% | -39% | -88% | -91% |
| NEAR | 1522 | 8 | 6% | 3% | -31% | -77% | -77% |
| GOLD | 864 | 1 | 3% | 1% | -86% | -92% | -94% |
| SILVER | 841 | 4 | 3% | 1% | -45% | -80% | -80% |
| WTI | 810 | 3 | 3% | 1% | -57% | -94% | -95% |
| COPPER | 735 | 2 | 2% | 1% | -75% | -84% | -84% |
| PLATINUM | 722 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 663 | 5 | 2% | 2% | -30% | -82% | -81% |
| PALLADIUM | 659 | 2 | 1% | 0% | -72% | -84% | -84% |
| EURUSD | 659 | 3 | 3% | 1% | -58% | -81% | -81% |
| GBPUSD | 615 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 574 | 3 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 200 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 169 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10760 | 40 | 4% | 2% | -57% | -89% | -88% |
| DOWN (bought NO) | 10572 | 40 | 4% | 2% | -56% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2273 | 11 | 2% | 1% | -18% | -79% | -79% |
| 0.05–0.1% | 2363 | 7 | 3% | 1% | -57% | -92% | -91% |
| 0.1–0.2% | 3484 | 11 | 4% | 2% | -61% | -90% | -90% |
| 0.2–0.5% | 4079 | 21 | 6% | 3% | -43% | -88% | -88% |
| Over 0.5% | 1619 | 6 | 7% | 3% | -62% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5359 | 20 | 4% | 2% | -58% | -87% | -88% |
| Morning (6am–12pm) | 5104 | 27 | 4% | 2% | -39% | -87% | -86% |
| Afternoon (12–6pm) | 5067 | 16 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 5802 | 17 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,433 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/16 4:59:52 PM | XRP | UP | 7 sec | -0.023% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 4:59:52 PM | WTI | UP | 7 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/16 4:59:36 PM | SOL | UP | 23 sec | -0.031% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 4:59:20 PM | HYPE | UP | 39 sec | -0.063% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 4:59:20 PM | ETH | UP | 39 sec | -0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/16 4:59:20 PM | BNB | DOWN | 39 sec | -0.014% | 0¢ | ❌ Lost | $0.00 |
| 10/16 4:58:48 PM | DOGE | DOWN | 72 sec | +0.114% | 0¢ | ❌ Lost | $0.00 |
| 10/16 4:58:48 PM | ZEC | DOWN | 72 sec | +0.230% | 0¢ | ❌ Lost | $0.00 |
| 10/16 4:57:42 PM | NEAR | DOWN | 2.3 min | +0.250% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 4:44:55 PM | HYPE | DOWN | 5 sec | +0.044% | 0¢ | ❌ Lost | $0.00 |
| 10/16 4:44:55 PM | ZEC | DOWN | 5 sec | -0.060% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 4:44:55 PM | BNB | DOWN | 5 sec | -0.019% | 0¢ | ❌ Lost | $0.00 |
| 10/16 4:44:55 PM | WTI | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 4:44:39 PM | NEAR | DOWN | 21 sec | +0.035% | 0¢ | ❌ Lost | $0.00 |
| 10/16 4:44:23 PM | SOL | UP | 37 sec | -0.042% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 4:44:08 PM | XRP | DOWN | 51 sec | +0.023% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 4:43:47 PM | ETH | DOWN | 72 sec | +0.074% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 4:43:15 PM | DOGE | DOWN | 1.7 min | +0.140% | 0¢ | ❌ Lost | $0.00 |
| 10/16 4:29:52 PM | XRP | UP | 7 sec | -0.046% | 0¢ | ❌ Lost | $0.00 |
| 10/16 4:29:52 PM | BTC | DOWN | 7 sec | +0.038% | 0¢ | ❌ Lost | $0.00 |
| 10/16 4:29:20 PM | DOGE | UP | 39 sec | -0.086% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 4:29:20 PM | SOL | UP | 39 sec | -0.026% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 4:29:20 PM | ETH | UP | 39 sec | -0.032% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 4:29:04 PM | HYPE | DOWN | 56 sec | +0.089% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 4:28:30 PM | ZEC | UP | 1.5 min | -0.184% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 4:28:14 PM | BNB | UP | 1.8 min | -0.079% | 0¢ | ❌ Lost | $0.00 |
| 10/16 4:24:47 PM | NEAR | DOWN | 5.2 min | +0.806% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 4:14:04 PM | HYPE | UP | 55 sec | -0.110% | 0¢ | ❌ Lost | $0.00 |
| 10/16 4:13:32 PM | WTI | UP | 88 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 4:13:16 PM | BTC | DOWN | 1.7 min | +0.121% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
