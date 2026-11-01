# 15-Minute 1¢ Study

*Updated Sun Nov 1, 12:18 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3363 finished bets | 1% | $114.55 | +31% | +3.41¢ | $79.40 / $35.15 |

*Expect about **99 buys a day** (~$14.84/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3108 | $53.75 | +16% |
| Volatility model ≥ 2%, hold to the close | 6205 | $33.10 | +4% |
| Momentum model ≥ 2%, hold to the close | 5122 | -$45.90 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 41106 | 41096 | 153 (0%) | 1.07% | -$2,861.25 (-57%) | Hold to the close: -$2,861.25 (-57%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 25495 | 4.7% | 0.4% (100) | -694% | ❌ Worse |
| Momentum model | 25495 | 4.6% | 0.4% (100) | -717% | ❌ Worse |
| Mean-reversion model | 25495 | 8.1% | 0.4% (100) | -842% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 25495 | 100 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6205 | 56 | +4% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3363 | 35 | +31% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1906 | 21 | +58% | -69% | -67% | -64% |
| Momentum model ≥ 2% | 5122 | 39 | -8% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3108 | 28 | +16% | -78% | -78% | -73% |
| Momentum model ≥ 10% | 2032 | 19 | +30% | -73% | -72% | -67% |
| Mean-reversion model ≥ 2% | 10490 | 71 | -26% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7350 | 61 | -8% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4918 | 43 | -1% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 25697 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9712 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5687 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 41096 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 153 | 0% | -$2,861.25 | -57% | — |
| Sell at 2¢ | 1598 | 4% | -$4,363.77 | -87% | 47 sec |
| Sell at 3¢ | 1099 | 3% | -$4,350.64 | -87% | 48 sec |
| Sell at 5¢ | 761 | 2% | -$4,270.60 | -85% | 63 sec |
| Sell at 10¢ | 456 | 1% | -$4,097.89 | -82% | 65 sec |
| Sell at 25¢ | 240 | 1% | -$3,788.85 | -76% | 82 sec |
| Sell at 50¢ | 157 | 0% | -$3,439.50 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1930 | 9 | 11% | 4% | -56% | -80% | -81% |
| 2–5 min | 13125 | 72 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10406 | 35 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 15624 | 37 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2878 | 13 | 5% | 3% | -42% | -88% | -88% |
| SOL | 2866 | 9 | 4% | 2% | -60% | -91% | -91% |
| HYPE | 2866 | 8 | 5% | 2% | -65% | -89% | -87% |
| BNB | 2865 | 17 | 5% | 2% | -26% | -85% | -84% |
| DOGE | 2856 | 6 | 4% | 2% | -74% | -90% | -89% |
| ETH | 2855 | 11 | 6% | 3% | -53% | -85% | -85% |
| NEAR | 2838 | 14 | 5% | 2% | -36% | -83% | -83% |
| BTC | 2837 | 13 | 5% | 2% | -38% | -88% | -89% |
| XRP | 2836 | 11 | 3% | 1% | -52% | -89% | -89% |
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
| UP (bought YES) | 20848 | 83 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 20248 | 70 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4179 | 21 | 2% | 1% | -13% | -82% | -81% |
| 0.05–0.1% | 4399 | 15 | 3% | 2% | -49% | -92% | -91% |
| 0.1–0.2% | 6631 | 22 | 4% | 2% | -59% | -90% | -90% |
| 0.2–0.5% | 7597 | 33 | 7% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2886 | 11 | 7% | 3% | -61% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10125 | 36 | 4% | 2% | -59% | -86% | -86% |
| Morning (6am–12pm) | 10310 | 46 | 4% | 2% | -49% | -85% | -84% |
| Afternoon (12–6pm) | 9655 | 34 | 4% | 2% | -59% | -87% | -87% |
| Evening (6pm–12am) | 11006 | 37 | 3% | 2% | -61% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,672 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/1 12:14:05 AM | XRP | DOWN | 55 sec | +0.072% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 12:13:33 AM | HYPE | DOWN | 87 sec | +0.181% | 0¢ | ❌ Lost | $0.00 |
| 11/1 12:12:46 AM | BNB | DOWN | 2.2 min | +0.095% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 12:12:30 AM | DOGE | DOWN | 2.5 min | +0.104% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 12:12:14 AM | SOL | DOWN | 2.8 min | +0.156% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 12:12:14 AM | BTC | DOWN | 2.8 min | +0.073% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 12:10:54 AM | NEAR | DOWN | 4.1 min | +0.292% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 12:09:51 AM | ZEC | DOWN | 5.1 min | +0.339% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 12:09:51 AM | ETH | DOWN | 5.1 min | +0.180% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 11:58:56 PM | BNB | UP | 63 sec | -0.121% | 0¢ | ❌ Lost | $0.00 |
| 10/31 11:58:46 PM | NEAR | DOWN | 73 sec | +0.021% | 0¢ | ❌ Lost | $0.00 |
| 10/31 11:57:59 PM | SOL | DOWN | 2.0 min | +0.142% | 0¢ | ❌ Lost | $0.00 |
| 10/31 11:57:59 PM | BTC | DOWN | 2.0 min | +0.096% | 0¢ | ❌ Lost | $0.00 |
| 10/31 11:57:59 PM | HYPE | DOWN | 2.0 min | +0.155% | 0¢ | ❌ Lost | $0.00 |
| 10/31 11:57:59 PM | ZEC | DOWN | 2.0 min | +0.352% | 0¢ | ❌ Lost | $0.00 |
| 10/31 11:57:59 PM | DOGE | DOWN | 2.0 min | +0.048% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 11:57:59 PM | XRP | DOWN | 2.0 min | +0.168% | 0¢ | ❌ Lost | $0.00 |
| 10/31 11:57:59 PM | ETH | DOWN | 2.0 min | +0.142% | 0¢ | ❌ Lost | $0.00 |
| 10/31 11:29:58 PM | SOL | DOWN | 2 sec | +0.007% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 11:29:42 PM | BTC | DOWN | 18 sec | -0.006% | 0¢ | ❌ Lost | $0.00 |
| 10/31 11:29:27 PM | HYPE | DOWN | 33 sec | +0.036% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 11:28:51 PM | ETH | UP | 69 sec | -0.015% | 7¢ | ❌ Lost | -$0.15 |
| 10/31 11:28:35 PM | BNB | DOWN | 85 sec | +0.077% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 11:28:20 PM | ZEC | UP | 1.6 min | -0.113% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 11:27:14 PM | XRP | DOWN | 2.8 min | +0.104% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 11:26:25 PM | NEAR | UP | 3.6 min | -0.466% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 11:25:04 PM | DOGE | DOWN | 4.9 min | +0.107% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 11:14:40 PM | DOGE | DOWN | 20 sec | -0.030% | 0¢ | ❌ Lost | $0.00 |
| 10/31 11:14:09 PM | BNB | DOWN | 51 sec | +0.040% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 11:13:53 PM | NEAR | DOWN | 67 sec | +0.269% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
