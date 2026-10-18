# 15-Minute 1¢ Study

*Updated Sat Oct 17, 6:23 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1845 finished bets | 1% | $88.95 | +43% | +4.82¢ | $39.65 / $49.30 |

*Expect about **93 buys a day** (~$14.02/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1688 | $54.25 | +30% |
| Momentum model ≥ 2%, hold to the close | 2829 | -$6.80 | -2% |
| Volatility model ≥ 2%, hold to the close | 3324 | -$24.75 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 22231 | 22224 | 85 (0%) | 1.07% | -$1,508.35 (-56%) | Hold to the close: -$1,508.35 (-56%) |

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
| Volatility model | 14500 | 4.6% | 0.4% (59) | -653% | ❌ Worse |
| Momentum model | 14500 | 4.5% | 0.4% (59) | -676% | ❌ Worse |
| Mean-reversion model | 14500 | 7.6% | 0.4% (59) | -784% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 14500 | 59 | -49% | -88% | -88% | -85% |
| Volatility model ≥ 2% | 3324 | 27 | -6% | -79% | -79% | -75% |
| Volatility model ≥ 5% | 1845 | 21 | +43% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1080 | 13 | +71% | -68% | -67% | -64% |
| Momentum model ≥ 2% | 2829 | 23 | -2% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 1688 | 17 | +30% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 1126 | 12 | +49% | -74% | -74% | -69% |
| Mean-reversion model ≥ 2% | 5568 | 38 | -25% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3851 | 30 | -14% | -82% | -82% | -79% |
| Mean-reversion model ≥ 10% | 2550 | 19 | -14% | -80% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 14698 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5309 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 22224 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 85 | 0% | -$1,508.35 | -56% | — |
| Sell at 2¢ | 808 | 4% | -$2,390.27 | -89% | 42 sec |
| Sell at 3¢ | 546 | 2% | -$2,387.41 | -88% | 47 sec |
| Sell at 5¢ | 395 | 2% | -$2,343.60 | -87% | 50 sec |
| Sell at 10¢ | 241 | 1% | -$2,256.64 | -84% | 64 sec |
| Sell at 25¢ | 134 | 1% | -$2,086.81 | -77% | 79 sec |
| Sell at 50¢ | 88 | 0% | -$1,866.35 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 783 | 5 | 10% | 3% | -39% | -82% | -84% |
| 2–5 min | 7195 | 38 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 5754 | 23 | 3% | 2% | -56% | -92% | -92% |
| Under 1 min | 8488 | 19 | 1% | 0% | -68% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1651 | 11 | 4% | 2% | -17% | -90% | -90% |
| HYPE | 1644 | 6 | 5% | 3% | -55% | -89% | -88% |
| ETH | 1638 | 9 | 6% | 3% | -34% | -87% | -86% |
| BNB | 1638 | 7 | 5% | 2% | -48% | -89% | -88% |
| DOGE | 1635 | 2 | 4% | 2% | -85% | -91% | -90% |
| SOL | 1629 | 2 | 4% | 2% | -85% | -92% | -91% |
| XRP | 1623 | 7 | 3% | 1% | -47% | -86% | -87% |
| NEAR | 1621 | 9 | 6% | 3% | -28% | -78% | -78% |
| BTC | 1619 | 8 | 5% | 2% | -33% | -88% | -90% |
| GOLD | 864 | 1 | 3% | 1% | -86% | -92% | -94% |
| SILVER | 841 | 4 | 3% | 1% | -45% | -80% | -80% |
| WTI | 821 | 3 | 3% | 1% | -57% | -94% | -95% |
| COPPER | 735 | 2 | 2% | 1% | -75% | -84% | -84% |
| PLATINUM | 722 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 667 | 5 | 2% | 2% | -30% | -82% | -81% |
| PALLADIUM | 659 | 2 | 1% | 0% | -72% | -84% | -84% |
| EURUSD | 659 | 3 | 3% | 1% | -58% | -81% | -81% |
| GBPUSD | 615 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 574 | 3 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 200 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 169 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 11195 | 41 | 4% | 2% | -58% | -89% | -88% |
| DOWN (bought NO) | 11029 | 44 | 4% | 2% | -54% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2519 | 13 | 2% | 1% | -14% | -81% | -81% |
| 0.05–0.1% | 2555 | 8 | 3% | 2% | -55% | -91% | -91% |
| 0.1–0.2% | 3684 | 13 | 5% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 4260 | 21 | 6% | 3% | -46% | -88% | -88% |
| Over 0.5% | 1677 | 6 | 6% | 3% | -63% | -88% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5566 | 22 | 4% | 2% | -55% | -87% | -88% |
| Morning (6am–12pm) | 5315 | 27 | 4% | 2% | -42% | -87% | -86% |
| Afternoon (12–6pm) | 5311 | 19 | 3% | 1% | -57% | -88% | -89% |
| Evening (6pm–12am) | 6032 | 17 | 3% | 2% | -68% | -91% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,653 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/17 6:14:23 PM | DOGE | UP | 37 sec | -0.097% | 0¢ | ❌ Lost | $0.00 |
| 10/17 6:14:23 PM | XRP | DOWN | 37 sec | +0.000% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 6:14:07 PM | NEAR | DOWN | 53 sec | +0.142% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 6:12:25 PM | SOL | UP | 2.6 min | -0.228% | 9¢ | ❌ Lost | -$0.15 |
| 10/17 6:12:25 PM | ZEC | UP | 2.6 min | -0.487% | 2¢ | ❌ Lost | -$0.15 |
| 10/17 6:12:09 PM | HYPE | UP | 2.8 min | -0.297% | 18¢ | ❌ Lost | -$0.15 |
| 10/17 6:12:09 PM | BNB | UP | 2.8 min | -0.181% | 24¢ | ❌ Lost | -$0.15 |
| 10/17 6:11:53 PM | BTC | UP | 3.1 min | -0.094% | 12¢ | ❌ Lost | -$0.15 |
| 10/17 6:10:03 PM | ETH | UP | 5.0 min | -0.195% | 2¢ | ❌ Lost | -$0.15 |
| 10/17 5:59:38 PM | ZEC | DOWN | 21 sec | +0.040% | 0¢ | ❌ Lost | $0.00 |
| 10/17 5:59:22 PM | HYPE | DOWN | 37 sec | +0.073% | 0¢ | ❌ Lost | $0.00 |
| 10/17 5:59:22 PM | NEAR | DOWN | 37 sec | +0.060% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 5:59:10 PM | DOGE | DOWN | 49 sec | +0.054% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 5:59:10 PM | XRP | DOWN | 49 sec | +0.054% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 5:58:23 PM | SOL | DOWN | 1.6 min | +0.202% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 5:57:16 PM | BNB | DOWN | 2.7 min | +0.101% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 5:56:05 PM | ETH | DOWN | 3.9 min | +0.148% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 5:56:05 PM | BTC | DOWN | 3.9 min | +0.157% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 5:44:33 PM | ETH | DOWN | 27 sec | +0.077% | 0¢ | ❌ Lost | $0.00 |
| 10/17 5:44:17 PM | SOL | DOWN | 43 sec | +0.114% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 5:43:46 PM | ZEC | DOWN | 74 sec | +0.230% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 5:43:46 PM | NEAR | DOWN | 74 sec | +0.226% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 5:43:29 PM | BTC | DOWN | 1.5 min | +0.111% | 0¢ | ❌ Lost | $0.00 |
| 10/17 5:43:29 PM | HYPE | DOWN | 1.5 min | +0.077% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 5:43:13 PM | DOGE | DOWN | 1.8 min | +0.143% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 5:42:57 PM | XRP | DOWN | 2.0 min | +0.163% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 5:42:26 PM | BNB | DOWN | 2.6 min | +0.053% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 5:29:46 PM | ETH | DOWN | 14 sec | +0.028% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 5:29:30 PM | SOL | UP | 30 sec | -0.121% | 0¢ | ❌ Lost | $0.00 |
| 10/17 5:28:26 PM | BTC | UP | 1.6 min | -0.061% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
