# 15-Minute 1¢ Study

*Updated Sat Oct 17, 1:01 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1723 finished bets | 1% | $74.75 | +39% | +4.34¢ | $32.55 / $42.20 |

*Expect about **91 buys a day** (~$13.59/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1587 | $37.95 | +22% |
| Momentum model ≥ 2%, hold to the close | 2681 | -$16.95 | -5% |
| Volatility model ≥ 5%, sell at 50¢ | 1723 | -$27.75 | -15% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 21631 | 21624 | 81 (0%) | 1.07% | -$1,495.80 (-57%) | Hold to the close: -$1,495.80 (-57%) |

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
| Volatility model | 13900 | 4.5% | 0.4% (55) | -659% | ❌ Worse |
| Momentum model | 13900 | 4.4% | 0.4% (55) | -683% | ❌ Worse |
| Mean-reversion model | 13900 | 7.5% | 0.4% (55) | -792% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13900 | 55 | -50% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 3134 | 24 | -11% | -79% | -78% | -75% |
| Volatility model ≥ 5% | 1723 | 19 | +39% | -74% | -73% | -69% |
| Volatility model ≥ 10% | 1007 | 11 | +56% | -66% | -66% | -63% |
| Momentum model ≥ 2% | 2681 | 21 | -5% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 1587 | 15 | +22% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1057 | 10 | +33% | -73% | -73% | -68% |
| Mean-reversion model ≥ 2% | 5289 | 35 | -28% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3652 | 27 | -18% | -82% | -82% | -79% |
| Mean-reversion model ≥ 10% | 2405 | 16 | -24% | -80% | -80% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 14098 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5309 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 21624 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 81 | 0% | -$1,495.80 | -57% | — |
| Sell at 2¢ | 774 | 4% | -$2,330.56 | -89% | 39 sec |
| Sell at 3¢ | 518 | 2% | -$2,329.78 | -89% | 47 sec |
| Sell at 5¢ | 372 | 2% | -$2,290.00 | -87% | 50 sec |
| Sell at 10¢ | 224 | 1% | -$2,210.36 | -84% | 63 sec |
| Sell at 25¢ | 127 | 1% | -$2,041.43 | -78% | 79 sec |
| Sell at 50¢ | 84 | 0% | -$1,824.80 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 739 | 5 | 10% | 3% | -36% | -82% | -85% |
| 2–5 min | 6989 | 38 | 7% | 3% | -46% | -88% | -87% |
| 1–2 min | 5624 | 20 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 8268 | 18 | 1% | 0% | -69% | -88% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1584 | 11 | 5% | 3% | -13% | -89% | -90% |
| HYPE | 1579 | 6 | 4% | 2% | -53% | -90% | -88% |
| ETH | 1570 | 8 | 6% | 3% | -38% | -87% | -87% |
| BNB | 1569 | 6 | 5% | 2% | -53% | -89% | -89% |
| DOGE | 1568 | 2 | 4% | 2% | -84% | -90% | -90% |
| SOL | 1566 | 2 | 3% | 2% | -84% | -92% | -92% |
| XRP | 1557 | 7 | 3% | 1% | -44% | -86% | -87% |
| NEAR | 1554 | 8 | 6% | 3% | -33% | -78% | -78% |
| BTC | 1551 | 7 | 5% | 2% | -40% | -88% | -91% |
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
| UP (bought YES) | 10905 | 41 | 4% | 2% | -57% | -89% | -89% |
| DOWN (bought NO) | 10719 | 40 | 4% | 2% | -57% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2360 | 11 | 2% | 1% | -22% | -80% | -80% |
| 0.05–0.1% | 2428 | 7 | 3% | 1% | -58% | -92% | -92% |
| 0.1–0.2% | 3553 | 12 | 4% | 2% | -58% | -90% | -90% |
| 0.2–0.5% | 4122 | 21 | 6% | 3% | -44% | -88% | -88% |
| Over 0.5% | 1632 | 6 | 6% | 3% | -62% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5393 | 21 | 4% | 2% | -56% | -87% | -88% |
| Morning (6am–12pm) | 5104 | 27 | 4% | 2% | -39% | -87% | -86% |
| Afternoon (12–6pm) | 5104 | 16 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 6023 | 17 | 3% | 2% | -68% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,493 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/17 12:59:46 AM | BTC | DOWN | 14 sec | +0.008% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 12:59:30 AM | DOGE | UP | 30 sec | -0.020% | 0¢ | ❌ Lost | $0.00 |
| 10/17 12:59:14 AM | XRP | DOWN | 46 sec | +0.046% | 0¢ | ❌ Lost | $0.00 |
| 10/17 12:58:58 AM | SOL | DOWN | 62 sec | +0.030% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:58:58 AM | HYPE | DOWN | 62 sec | +0.085% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:58:43 AM | ZEC | UP | 77 sec | -0.173% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 12:58:27 AM | BNB | DOWN | 1.6 min | +0.019% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:57:40 AM | NEAR | UP | 2.3 min | -0.403% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:56:52 AM | HYPE | UP | 3.1 min | -0.153% | 100¢ | ✅ Won | $13.85 |
| 10/17 12:44:43 AM | DOGE | DOWN | 16 sec | -0.021% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:44:43 AM | ZEC | DOWN | 16 sec | +0.059% | 0¢ | ❌ Lost | $0.00 |
| 10/17 12:44:27 AM | NEAR | DOWN | 32 sec | -0.012% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 12:44:27 AM | SOL | UP | 32 sec | -0.030% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 12:43:40 AM | ETH | DOWN | 79 sec | +0.053% | 2¢ | ❌ Lost | -$0.15 |
| 10/17 12:43:40 AM | BNB | DOWN | 79 sec | +0.013% | 0¢ | ❌ Lost | $0.00 |
| 10/17 12:43:08 AM | HYPE | DOWN | 1.9 min | +0.131% | 0¢ | ❌ Lost | $0.00 |
| 10/17 12:42:21 AM | XRP | UP | 2.6 min | -0.115% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:29:38 AM | DOGE | UP | 22 sec | -0.031% | 0¢ | ❌ Lost | $0.00 |
| 10/17 12:29:22 AM | BTC | DOWN | 38 sec | +0.026% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 12:29:22 AM | SOL | UP | 38 sec | -0.056% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 12:29:06 AM | ZEC | UP | 54 sec | -0.162% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:28:35 AM | ETH | DOWN | 85 sec | +0.059% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 12:28:35 AM | NEAR | UP | 85 sec | -0.283% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:28:35 AM | XRP | UP | 85 sec | -0.115% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:26:26 AM | BNB | UP | 3.5 min | -0.090% | 3¢ | ❌ Lost | -$0.15 |
| 10/17 12:14:41 AM | BTC | DOWN | 18 sec | +0.043% | 0¢ | ❌ Lost | $0.00 |
| 10/17 12:14:41 AM | SOL | DOWN | 18 sec | +0.046% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 12:14:09 AM | ZEC | DOWN | 50 sec | +0.131% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 12:13:53 AM | DOGE | DOWN | 67 sec | +0.056% | 0¢ | ❌ Lost | $0.00 |
| 10/17 12:13:53 AM | HYPE | DOWN | 67 sec | +0.067% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
