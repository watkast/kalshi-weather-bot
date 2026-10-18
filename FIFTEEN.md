# 15-Minute 1¢ Study

*Updated Sun Oct 18, 8:36 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1904 finished bets | 1% | $81.45 | +38% | +4.28¢ | $36.50 / $44.95 |

*Expect about **94 buys a day** (~$14.05/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1753 | $59.85 | +31% |
| Momentum model ≥ 2%, hold to the close | 2927 | -$5.85 | -2% |
| Volatility model ≥ 5%, sell at 50¢ | 1904 | -$35.55 | -17% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 22716 | 22709 | 86 (0%) | 1.07% | -$1,553.75 (-56%) | Hold to the close: -$1,553.75 (-56%) |

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
| Volatility model | 14985 | 4.6% | 0.4% (60) | -667% | ❌ Worse |
| Momentum model | 14985 | 4.5% | 0.4% (60) | -690% | ❌ Worse |
| Mean-reversion model | 14985 | 7.7% | 0.4% (60) | -801% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 14985 | 60 | -50% | -88% | -88% | -85% |
| Volatility model ≥ 2% | 3445 | 27 | -10% | -79% | -79% | -75% |
| Volatility model ≥ 5% | 1904 | 21 | +38% | -76% | -75% | -72% |
| Volatility model ≥ 10% | 1123 | 13 | +63% | -69% | -68% | -66% |
| Momentum model ≥ 2% | 2927 | 24 | -2% | -81% | -82% | -78% |
| Momentum model ≥ 5% | 1753 | 18 | +31% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 1165 | 12 | +43% | -75% | -75% | -70% |
| Mean-reversion model ≥ 2% | 5774 | 38 | -28% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 4007 | 30 | -17% | -82% | -82% | -79% |
| Mean-reversion model ≥ 10% | 2662 | 19 | -18% | -80% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 15183 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5309 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 22709 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 86 | 0% | -$1,553.75 | -56% | — |
| Sell at 2¢ | 830 | 4% | -$2,443.95 | -89% | 44 sec |
| Sell at 3¢ | 560 | 2% | -$2,441.35 | -89% | 47 sec |
| Sell at 5¢ | 404 | 2% | -$2,397.15 | -87% | 50 sec |
| Sell at 10¢ | 243 | 1% | -$2,313.42 | -84% | 63 sec |
| Sell at 25¢ | 136 | 1% | -$2,139.59 | -78% | 78 sec |
| Sell at 50¢ | 90 | 0% | -$1,912.25 | -69% | 1.5 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 815 | 5 | 11% | 4% | -42% | -81% | -84% |
| 2–5 min | 7398 | 38 | 7% | 3% | -49% | -87% | -87% |
| 1–2 min | 5851 | 23 | 3% | 2% | -57% | -92% | -92% |
| Under 1 min | 8641 | 20 | 1% | 0% | -66% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1705 | 11 | 4% | 2% | -20% | -90% | -90% |
| HYPE | 1696 | 6 | 5% | 2% | -57% | -90% | -88% |
| BNB | 1694 | 7 | 5% | 2% | -50% | -89% | -88% |
| DOGE | 1690 | 3 | 4% | 2% | -78% | -91% | -90% |
| ETH | 1689 | 9 | 6% | 3% | -36% | -87% | -86% |
| SOL | 1683 | 2 | 3% | 2% | -85% | -92% | -92% |
| XRP | 1679 | 7 | 3% | 1% | -49% | -87% | -87% |
| NEAR | 1674 | 9 | 6% | 3% | -30% | -78% | -78% |
| BTC | 1673 | 8 | 5% | 2% | -36% | -88% | -90% |
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
| UP (bought YES) | 11438 | 42 | 4% | 2% | -58% | -89% | -88% |
| DOWN (bought NO) | 11271 | 44 | 4% | 2% | -55% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2612 | 14 | 2% | 1% | -11% | -82% | -81% |
| 0.05–0.1% | 2646 | 8 | 3% | 2% | -56% | -92% | -91% |
| 0.1–0.2% | 3811 | 13 | 5% | 2% | -58% | -90% | -89% |
| 0.2–0.5% | 4390 | 21 | 6% | 3% | -47% | -88% | -88% |
| Over 0.5% | 1721 | 6 | 7% | 3% | -64% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5767 | 23 | 4% | 2% | -55% | -87% | -88% |
| Morning (6am–12pm) | 5400 | 27 | 4% | 2% | -43% | -87% | -86% |
| Afternoon (12–6pm) | 5311 | 19 | 3% | 1% | -57% | -88% | -89% |
| Evening (6pm–12am) | 6231 | 17 | 3% | 2% | -69% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,789 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/18 8:26:28 AM | ZEC | DOWN | 3.5 min | +0.456% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 8:26:12 AM | ETH | DOWN | 3.8 min | +0.207% | 4¢ | ❌ Lost | -$0.15 |
| 10/18 8:25:57 AM | XRP | DOWN | 4.0 min | +0.337% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 8:25:39 AM | BTC | DOWN | 4.3 min | +0.203% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 8:25:39 AM | SOL | DOWN | 4.3 min | +0.330% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 8:25:23 AM | BNB | DOWN | 4.6 min | +0.196% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 8:25:07 AM | HYPE | DOWN | 4.9 min | +0.504% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 8:24:19 AM | DOGE | DOWN | 5.7 min | +0.421% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 8:11:40 AM | HYPE | UP | 3.3 min | -0.446% | 0¢ | ❌ Lost | $0.00 |
| 10/18 8:11:40 AM | NEAR | UP | 3.3 min | -1.179% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 8:11:40 AM | BNB | UP | 3.3 min | -0.242% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 8:11:24 AM | ZEC | UP | 3.6 min | -0.891% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 8:11:24 AM | SOL | UP | 3.6 min | -0.529% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 8:11:24 AM | ETH | UP | 3.6 min | -0.389% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 8:11:24 AM | DOGE | UP | 3.6 min | -0.585% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 8:10:53 AM | BTC | UP | 4.1 min | -0.265% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 8:08:12 AM | XRP | UP | 6.8 min | -0.585% | 2¢ | ❌ Lost | -$0.15 |
| 10/18 7:58:53 AM | NEAR | UP | 66 sec | -0.267% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 7:58:37 AM | BNB | DOWN | 82 sec | +0.086% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 7:58:37 AM | XRP | DOWN | 82 sec | +0.133% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 7:58:37 AM | DOGE | DOWN | 82 sec | +0.101% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 7:58:21 AM | ZEC | DOWN | 1.6 min | +0.302% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 7:57:46 AM | BTC | DOWN | 2.2 min | +0.105% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 7:57:46 AM | SOL | DOWN | 2.2 min | +0.181% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 7:57:46 AM | ETH | DOWN | 2.2 min | +0.134% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 7:57:14 AM | HYPE | DOWN | 2.8 min | +0.267% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 7:44:40 AM | ZEC | DOWN | 20 sec | +0.097% | 0¢ | ❌ Lost | $0.00 |
| 10/18 7:44:24 AM | SOL | UP | 36 sec | -0.080% | 0¢ | ❌ Lost | $0.00 |
| 10/18 7:44:09 AM | XRP | UP | 50 sec | -0.117% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 7:43:53 AM | BTC | UP | 66 sec | -0.061% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
