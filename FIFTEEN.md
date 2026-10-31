# 15-Minute 1¢ Study

*Updated Sat Oct 31, 9:15 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3296 finished bets | 1% | $93.15 | +25% | +2.83¢ | $83.15 / $10.00 |

*Expect about **99 buys a day** (~$14.83/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3055 | $44.40 | +13% |
| Volatility model ≥ 2%, hold to the close | 6089 | $4.00 | +1% |
| Momentum model ≥ 2%, hold to the close | 5028 | -$64.15 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 40617 | 40604 | 150 (0%) | 1.07% | -$2,851.50 (-58%) | Hold to the close: -$2,851.50 (-58%) |

*In play or awaiting result: 12. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 25004 | 4.7% | 0.4% (97) | -696% | ❌ Worse |
| Momentum model | 25004 | 4.6% | 0.4% (97) | -719% | ❌ Worse |
| Mean-reversion model | 25004 | 8.1% | 0.4% (97) | -845% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 25004 | 97 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6089 | 53 | +1% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3296 | 33 | +25% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1867 | 20 | +53% | -69% | -68% | -64% |
| Momentum model ≥ 2% | 5028 | 37 | -11% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3055 | 27 | +13% | -78% | -78% | -73% |
| Momentum model ≥ 10% | 1994 | 18 | +25% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 10287 | 68 | -28% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7209 | 58 | -11% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4819 | 40 | -6% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 25205 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9712 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5687 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 40604 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 150 | 0% | -$2,851.50 | -58% | — |
| Sell at 2¢ | 1571 | 4% | -$4,319.04 | -87% | 47 sec |
| Sell at 3¢ | 1081 | 3% | -$4,305.91 | -87% | 48 sec |
| Sell at 5¢ | 750 | 2% | -$4,226.00 | -85% | 63 sec |
| Sell at 10¢ | 450 | 1% | -$4,054.00 | -82% | 65 sec |
| Sell at 25¢ | 235 | 1% | -$3,753.65 | -76% | 83 sec |
| Sell at 50¢ | 154 | 0% | -$3,408.00 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1899 | 9 | 11% | 4% | -55% | -80% | -81% |
| 2–5 min | 12955 | 70 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 10272 | 35 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 15467 | 36 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2822 | 13 | 5% | 3% | -41% | -88% | -88% |
| HYPE | 2813 | 8 | 5% | 2% | -65% | -89% | -87% |
| BNB | 2811 | 16 | 5% | 2% | -29% | -85% | -84% |
| SOL | 2808 | 8 | 4% | 2% | -64% | -91% | -91% |
| DOGE | 2802 | 6 | 4% | 2% | -73% | -90% | -90% |
| ETH | 2800 | 11 | 6% | 3% | -52% | -85% | -85% |
| NEAR | 2785 | 13 | 5% | 2% | -39% | -83% | -83% |
| BTC | 2782 | 13 | 5% | 2% | -37% | -88% | -89% |
| XRP | 2782 | 11 | 3% | 1% | -51% | -89% | -89% |
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
| UP (bought YES) | 20610 | 82 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 19994 | 68 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4049 | 20 | 2% | 1% | -14% | -82% | -81% |
| 0.05–0.1% | 4294 | 14 | 3% | 2% | -51% | -92% | -91% |
| 0.1–0.2% | 6480 | 22 | 4% | 2% | -58% | -90% | -89% |
| 0.2–0.5% | 7501 | 32 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2877 | 11 | 7% | 3% | -61% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10116 | 36 | 4% | 2% | -59% | -86% | -86% |
| Morning (6am–12pm) | 10223 | 46 | 4% | 2% | -49% | -85% | -84% |
| Afternoon (12–6pm) | 9463 | 33 | 4% | 2% | -59% | -87% | -87% |
| Evening (6pm–12am) | 10802 | 35 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,560 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/31 9:14:49 AM | NEAR | DOWN | 11 sec | +0.050% | 0¢ | ❌ Lost | $0.00 |
| 10/31 9:14:49 AM | BTC | DOWN | 11 sec | -0.001% | 0¢ | In play | — |
| 10/31 9:14:02 AM | XRP | UP | 57 sec | -0.056% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 9:14:02 AM | ZEC | UP | 57 sec | -0.166% | 0¢ | ❌ Lost | $0.00 |
| 10/31 9:13:46 AM | HYPE | DOWN | 73 sec | +0.149% | 1¢ | In play | — |
| 10/31 9:13:46 AM | BNB | UP | 73 sec | -0.093% | 0¢ | ❌ Lost | $0.00 |
| 10/31 9:13:30 AM | ETH | DOWN | 89 sec | +0.066% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 9:13:14 AM | SOL | DOWN | 1.8 min | +0.098% | 1¢ | In play | — |
| 10/31 9:12:10 AM | DOGE | DOWN | 2.8 min | +0.105% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 8:59:33 AM | SOL | UP | 26 sec | -0.091% | 0¢ | ❌ Lost | $0.00 |
| 10/31 8:59:33 AM | DOGE | UP | 26 sec | -0.110% | 0¢ | ❌ Lost | $0.00 |
| 10/31 8:59:01 AM | ZEC | UP | 58 sec | -0.135% | 0¢ | ❌ Lost | $0.00 |
| 10/31 8:58:45 AM | XRP | DOWN | 75 sec | +0.056% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 8:58:45 AM | HYPE | UP | 75 sec | -0.216% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 8:58:13 AM | BTC | UP | 1.8 min | -0.129% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 8:57:41 AM | NEAR | UP | 2.3 min | -0.536% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 8:56:04 AM | ETH | UP | 3.9 min | -0.240% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 8:52:50 AM | BNB | DOWN | 7.2 min | +0.547% | 2¢ | ❌ Lost | -$0.15 |
| 10/31 8:44:56 AM | ZEC | UP | 3 sec | +0.059% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 8:44:20 AM | NEAR | DOWN | 40 sec | +0.023% | 0¢ | ❌ Lost | $0.00 |
| 10/31 8:43:01 AM | SOL | DOWN | 2.0 min | +0.145% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 8:42:43 AM | BTC | DOWN | 2.3 min | +0.064% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 8:42:11 AM | DOGE | DOWN | 2.8 min | +0.148% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 8:42:11 AM | HYPE | DOWN | 2.8 min | +0.321% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 8:41:56 AM | ETH | DOWN | 3.0 min | +0.122% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 8:41:56 AM | BNB | DOWN | 3.0 min | +0.122% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 8:41:24 AM | XRP | DOWN | 3.6 min | +0.137% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 8:29:31 AM | ZEC | UP | 29 sec | -0.047% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 8:29:15 AM | ETH | UP | 45 sec | -0.042% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 8:29:15 AM | HYPE | UP | 45 sec | -0.152% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
