# 15-Minute 1¢ Study

*Updated Mon Nov 2, 5:01 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3522 finished bets | 1% | $124.25 | +32% | +3.53¢ | $70.10 / $54.15 |

*Expect about **99 buys a day** (~$14.79/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3252 | $51.85 | +15% |
| Volatility model ≥ 2%, hold to the close | 6511 | $51.30 | +7% |
| Momentum model ≥ 2%, hold to the close | 5379 | -$34.35 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 43003 | 42993 | 159 (0%) | 1.07% | -$3,007.95 (-57%) | Hold to the close: -$3,007.95 (-57%) |

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
| Volatility model | 26660 | 4.7% | 0.4% (106) | -675% | ❌ Worse |
| Momentum model | 26660 | 4.6% | 0.4% (106) | -699% | ❌ Worse |
| Mean-reversion model | 26660 | 8.1% | 0.4% (106) | -822% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26660 | 106 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6511 | 60 | +7% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3522 | 37 | +32% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 1995 | 22 | +57% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 5379 | 42 | -6% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3252 | 29 | +15% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2123 | 19 | +25% | -74% | -73% | -69% |
| Mean-reversion model ≥ 2% | 11019 | 76 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7724 | 65 | -7% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 5165 | 46 | +1% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 26862 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10112 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6019 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 42993 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 159 | 0% | -$3,007.95 | -57% | — |
| Sell at 2¢ | 1687 | 4% | -$4,571.33 | -87% | 47 sec |
| Sell at 3¢ | 1160 | 3% | -$4,557.55 | -87% | 48 sec |
| Sell at 5¢ | 806 | 2% | -$4,458.05 | -85% | 63 sec |
| Sell at 10¢ | 487 | 1% | -$4,273.98 | -82% | 65 sec |
| Sell at 25¢ | 254 | 1% | -$3,959.21 | -76% | 82 sec |
| Sell at 50¢ | 165 | 0% | -$3,602.20 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2059 | 9 | 11% | 4% | -58% | -81% | -82% |
| 2–5 min | 13806 | 75 | 7% | 4% | -46% | -87% | -86% |
| 1–2 min | 10857 | 38 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 16260 | 37 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3010 | 13 | 5% | 3% | -44% | -88% | -88% |
| SOL | 3001 | 11 | 4% | 2% | -54% | -91% | -91% |
| BNB | 2998 | 17 | 5% | 2% | -29% | -85% | -84% |
| HYPE | 2996 | 9 | 5% | 2% | -63% | -89% | -87% |
| DOGE | 2984 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 2982 | 11 | 6% | 3% | -55% | -85% | -85% |
| BTC | 2965 | 14 | 5% | 2% | -36% | -88% | -89% |
| NEAR | 2964 | 15 | 5% | 2% | -34% | -83% | -84% |
| XRP | 2962 | 12 | 3% | 1% | -50% | -89% | -89% |
| GOLD | 1572 | 5 | 5% | 2% | -61% | -81% | -83% |
| SILVER | 1532 | 7 | 5% | 2% | -46% | -82% | -82% |
| WTI | 1530 | 4 | 3% | 1% | -68% | -93% | -93% |
| PLATINUM | 1362 | 3 | 2% | 1% | -79% | -96% | -96% |
| EURUSD | 1303 | 3 | 2% | 1% | -79% | -89% | -88% |
| COPPER | 1299 | 5 | 2% | 1% | -64% | -76% | -75% |
| NATGAS | 1254 | 7 | 2% | 1% | -48% | -81% | -81% |
| GBPUSD | 1233 | 2 | 2% | 1% | -85% | -96% | -96% |
| PALLADIUM | 1228 | 2 | 1% | 0% | -85% | -90% | -91% |
| USDJPY | 1220 | 5 | 2% | 1% | -62% | -97% | -96% |
| AUDUSD | 760 | 4 | 2% | 1% | -51% | -85% | -84% |
| USDCAD | 728 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 335 | 0 | 1% | 1% | -100% | -97% | -96% |
| 10YRRATE | 210 | 1 | 5% | 2% | -56% | -46% | -44% |
| 30YRRATE | 198 | 0 | 2% | 0% | -100% | -97% | -96% |
| 2YRRATE | 191 | 2 | 4% | 1% | -2% | +5% | +6% |
| 5YRRATE | 176 | 1 | 6% | 2% | -47% | -90% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 21866 | 87 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 21127 | 72 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4374 | 21 | 2% | 1% | -16% | -82% | -82% |
| 0.05–0.1% | 4611 | 18 | 3% | 2% | -41% | -91% | -91% |
| 0.1–0.2% | 6956 | 24 | 4% | 2% | -57% | -90% | -90% |
| 0.2–0.5% | 7938 | 33 | 7% | 3% | -54% | -86% | -86% |
| Over 0.5% | 2978 | 12 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10646 | 37 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 10804 | 48 | 4% | 2% | -49% | -85% | -85% |
| Afternoon (12–6pm) | 10119 | 37 | 4% | 2% | -57% | -87% | -86% |
| Evening (6pm–12am) | 11424 | 37 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,762 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/2 4:59:44 PM | GOLD | DOWN | 15 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/2 4:59:44 PM | ZEC | UP | 15 sec | -0.048% | 0¢ | ❌ Lost | $0.00 |
| 11/2 4:59:44 PM | NEAR | UP | 15 sec | -0.119% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 4:59:28 PM | BTC | UP | 31 sec | -0.017% | 0¢ | ❌ Lost | $0.00 |
| 11/2 4:59:28 PM | BNB | DOWN | 31 sec | -0.003% | 0¢ | ❌ Lost | $0.00 |
| 11/2 4:59:13 PM | DOGE | UP | 46 sec | -0.065% | 0¢ | ❌ Lost | $0.00 |
| 11/2 4:59:13 PM | XRP | DOWN | 46 sec | +0.032% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 4:59:13 PM | SOL | UP | 46 sec | -0.059% | 0¢ | ❌ Lost | $0.00 |
| 11/2 4:59:13 PM | BRENT | DOWN | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 4:59:13 PM | WTI | DOWN | 46 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 4:58:56 PM | AUDUSD | DOWN | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 4:57:19 PM | GBPUSD | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 4:56:12 PM | EURUSD | DOWN | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 4:44:34 PM | USDJPY | DOWN | 26 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 4:44:18 PM | HYPE | UP | 42 sec | -0.156% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 4:44:02 PM | WTI | UP | 58 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 4:43:46 PM | GOLD | DOWN | 74 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 4:43:30 PM | AUDUSD | DOWN | 89 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 4:43:30 PM | XRP | DOWN | 89 sec | +0.072% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 4:42:58 PM | DOGE | DOWN | 2.0 min | +0.109% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 4:42:58 PM | NEAR | DOWN | 2.0 min | +0.135% | 2¢ | ❌ Lost | -$0.15 |
| 11/2 4:42:09 PM | BTC | DOWN | 2.8 min | +0.126% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 4:41:05 PM | SOL | DOWN | 3.9 min | +0.224% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 4:40:49 PM | BNB | DOWN | 4.2 min | +0.146% | 1¢ | ❌ Lost | $0.00 |
| 11/2 4:40:24 PM | ETH | DOWN | 4.6 min | +0.163% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 2:12:11 PM | SILVER | DOWN | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 2:11:53 PM | 2YRRATE | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 2:11:53 PM | 5YRRATE | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 2:11:06 PM | 10YRRATE | DOWN | 3.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 2:10:49 PM | ZEC | DOWN | 4.2 min | +0.760% | 4¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
