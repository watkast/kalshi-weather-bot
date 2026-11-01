# 15-Minute 1¢ Study

*Updated Sun Nov 1, 12:59 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3364 finished bets | 1% | $114.40 | +30% | +3.40¢ | $79.25 / $35.15 |

*Expect about **99 buys a day** (~$14.84/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3110 | $53.60 | +16% |
| Volatility model ≥ 2%, hold to the close | 6207 | $32.80 | +4% |
| Momentum model ≥ 2%, hold to the close | 5125 | -$46.20 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 41132 | 41114 | 153 (0%) | 1.07% | -$2,863.65 (-57%) | Hold to the close: -$2,863.65 (-57%) |

*In play or awaiting result: 17. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 25513 | 4.7% | 0.4% (100) | -694% | ❌ Worse |
| Momentum model | 25513 | 4.6% | 0.4% (100) | -717% | ❌ Worse |
| Mean-reversion model | 25513 | 8.1% | 0.4% (100) | -842% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 25513 | 100 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6207 | 56 | +4% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3364 | 35 | +30% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1906 | 21 | +58% | -69% | -67% | -64% |
| Momentum model ≥ 2% | 5125 | 39 | -8% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3110 | 28 | +16% | -78% | -78% | -73% |
| Momentum model ≥ 10% | 2032 | 19 | +30% | -73% | -72% | -67% |
| Mean-reversion model ≥ 2% | 10499 | 71 | -26% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7355 | 61 | -8% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4919 | 43 | -1% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 25715 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9712 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5687 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 41114 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 153 | 0% | -$2,863.65 | -57% | — |
| Sell at 2¢ | 1600 | 4% | -$4,365.65 | -87% | 47 sec |
| Sell at 3¢ | 1099 | 3% | -$4,353.04 | -87% | 48 sec |
| Sell at 5¢ | 761 | 2% | -$4,273.00 | -85% | 63 sec |
| Sell at 10¢ | 456 | 1% | -$4,100.29 | -82% | 65 sec |
| Sell at 25¢ | 240 | 1% | -$3,791.25 | -76% | 82 sec |
| Sell at 50¢ | 157 | 0% | -$3,441.90 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1931 | 9 | 11% | 4% | -56% | -80% | -81% |
| 2–5 min | 13135 | 72 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10412 | 35 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 15625 | 37 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2880 | 13 | 5% | 3% | -42% | -88% | -88% |
| SOL | 2868 | 9 | 4% | 2% | -60% | -91% | -91% |
| HYPE | 2868 | 8 | 5% | 2% | -65% | -89% | -87% |
| BNB | 2867 | 17 | 5% | 2% | -26% | -85% | -84% |
| DOGE | 2858 | 6 | 4% | 2% | -74% | -90% | -89% |
| ETH | 2857 | 11 | 7% | 3% | -53% | -85% | -85% |
| NEAR | 2840 | 14 | 5% | 2% | -36% | -83% | -83% |
| BTC | 2839 | 13 | 5% | 2% | -38% | -88% | -89% |
| XRP | 2838 | 11 | 3% | 1% | -52% | -89% | -89% |
| GOLD | 1515 | 5 | 5% | 2% | -60% | -82% | -83% |
| SILVER | 1481 | 7 | 4% | 2% | -44% | -82% | -81% |
| WTI | 1476 | 4 | 3% | 1% | -67% | -93% | -93% |
| PLATINUM | 1314 | 3 | 2% | 1% | -79% | -96% | -96% |
| COPPER | 1253 | 5 | 1% | 1% | -63% | -75% | -75% |
| EURUSD | 1249 | 3 | 2% | 1% | -78% | -89% | -88% |
| NATGAS | 1212 | 7 | 2% | 1% | -46% | -81% | -80% |
| GBPUSD | 1185 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1178 | 2 | 1% | 0% | -84% | -90% | -91% |
| USDJPY | 1171 | 5 | 2% | 1% | -60% | -97% | -96% |
| AUDUSD | 705 | 4 | 2% | 1% | -47% | -84% | -83% |
| USDCAD | 685 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 283 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 188 | 1 | 5% | 2% | -50% | -41% | -39% |
| 30YRRATE | 177 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 170 | 2 | 5% | 1% | +10% | +18% | +19% |
| 5YRRATE | 157 | 1 | 6% | 3% | -41% | -89% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 20865 | 83 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 20249 | 70 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4180 | 21 | 2% | 1% | -13% | -82% | -81% |
| 0.05–0.1% | 4402 | 15 | 3% | 2% | -49% | -92% | -91% |
| 0.1–0.2% | 6639 | 22 | 4% | 2% | -59% | -90% | -90% |
| 0.2–0.5% | 7602 | 33 | 7% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2887 | 11 | 7% | 3% | -61% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10143 | 36 | 4% | 2% | -60% | -86% | -86% |
| Morning (6am–12pm) | 10310 | 46 | 4% | 2% | -49% | -85% | -84% |
| Afternoon (12–6pm) | 9655 | 34 | 4% | 2% | -59% | -87% | -87% |
| Evening (6pm–12am) | 11006 | 37 | 3% | 2% | -61% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,676 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/1 12:57:58 AM | BNB | DOWN | 2.0 min | +0.126% | — | In play | — |
| 11/1 12:57:58 AM | NEAR | DOWN | 2.0 min | +0.121% | — | In play | — |
| 11/1 12:57:11 AM | DOGE | DOWN | 2.8 min | +0.095% | — | In play | — |
| 11/1 12:55:49 AM | BTC | DOWN | 4.2 min | +0.116% | — | In play | — |
| 11/1 12:55:17 AM | XRP | DOWN | 4.7 min | +0.152% | — | In play | — |
| 11/1 12:55:02 AM | SOL | DOWN | 5.0 min | +0.161% | — | In play | — |
| 11/1 12:54:46 AM | ETH | DOWN | 5.2 min | +0.121% | — | In play | — |
| 11/1 12:54:30 AM | HYPE | DOWN | 5.5 min | +0.347% | — | In play | — |
| 11/1 12:44:35 AM | BNB | DOWN | 24 sec | +0.014% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 12:43:45 AM | HYPE | UP | 75 sec | -0.122% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 12:42:43 AM | BTC | UP | 2.3 min | -0.071% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 12:41:38 AM | ZEC | UP | 3.4 min | -0.295% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 12:41:22 AM | SOL | UP | 3.6 min | -0.135% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 12:41:22 AM | XRP | UP | 3.6 min | -0.112% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 12:40:18 AM | NEAR | UP | 4.7 min | -0.519% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 12:40:18 AM | ETH | UP | 4.7 min | -0.134% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 12:40:02 AM | DOGE | UP | 5.0 min | -0.165% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 12:28:30 AM | BNB | UP | 89 sec | -0.095% | 0¢ | ❌ Lost | $0.00 |
| 11/1 12:28:30 AM | BTC | UP | 89 sec | -0.067% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 12:28:30 AM | ZEC | UP | 89 sec | -0.248% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 12:28:14 AM | DOGE | UP | 1.8 min | -0.136% | 0¢ | ❌ Lost | $0.00 |
| 11/1 12:28:14 AM | XRP | UP | 1.8 min | -0.112% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 12:27:57 AM | NEAR | UP | 2.0 min | -0.436% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 12:26:54 AM | ETH | UP | 3.1 min | -0.102% | 2¢ | ❌ Lost | -$0.15 |
| 11/1 12:25:17 AM | HYPE | UP | 4.7 min | -0.354% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 12:22:22 AM | SOL | UP | 7.6 min | -0.209% | 3¢ | ❌ Lost | -$0.15 |
| 11/1 12:14:05 AM | XRP | DOWN | 55 sec | +0.072% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 12:13:33 AM | HYPE | DOWN | 87 sec | +0.181% | 0¢ | ❌ Lost | $0.00 |
| 11/1 12:12:46 AM | BNB | DOWN | 2.2 min | +0.095% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 12:12:30 AM | DOGE | DOWN | 2.5 min | +0.104% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
