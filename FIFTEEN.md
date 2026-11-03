# 15-Minute 1¢ Study

*Updated Mon Nov 2, 7:25 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3526 finished bets | 1% | $123.80 | +31% | +3.51¢ | $69.95 / $53.85 |

*Expect about **98 buys a day** (~$14.76/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3259 | $50.95 | +14% |
| Volatility model ≥ 2%, hold to the close | 6521 | $49.95 | +6% |
| Momentum model ≥ 2%, hold to the close | 5386 | -$35.25 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 43167 | 43157 | 160 (0%) | 1.07% | -$3,014.05 (-57%) | Hold to the close: -$3,014.05 (-57%) |

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
| Volatility model | 26738 | 4.7% | 0.4% (106) | -676% | ❌ Worse |
| Momentum model | 26738 | 4.6% | 0.4% (106) | -700% | ❌ Worse |
| Mean-reversion model | 26738 | 8.1% | 0.4% (106) | -822% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26738 | 106 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6521 | 60 | +6% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3526 | 37 | +31% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 1996 | 22 | +57% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 5386 | 42 | -6% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3259 | 29 | +14% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2127 | 19 | +25% | -74% | -73% | -69% |
| Mean-reversion model ≥ 2% | 11044 | 76 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7742 | 65 | -7% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 5175 | 46 | +1% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 26940 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 10165 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6052 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 43157 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 160 | 0% | -$3,014.05 | -57% | — |
| Sell at 2¢ | 1702 | 4% | -$4,573.53 | -87% | 47 sec |
| Sell at 3¢ | 1168 | 3% | -$4,560.53 | -87% | 48 sec |
| Sell at 5¢ | 812 | 2% | -$4,460.25 | -85% | 63 sec |
| Sell at 10¢ | 490 | 1% | -$4,276.15 | -81% | 65 sec |
| Sell at 25¢ | 255 | 1% | -$3,962.00 | -75% | 82 sec |
| Sell at 50¢ | 166 | 0% | -$3,601.55 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2073 | 9 | 11% | 4% | -59% | -81% | -82% |
| 2–5 min | 13869 | 75 | 7% | 4% | -47% | -86% | -86% |
| 1–2 min | 10890 | 38 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 16314 | 38 | 1% | 0% | -67% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3019 | 13 | 5% | 3% | -45% | -88% | -87% |
| SOL | 3010 | 11 | 4% | 2% | -54% | -91% | -90% |
| BNB | 3007 | 17 | 5% | 2% | -29% | -85% | -84% |
| HYPE | 3005 | 9 | 5% | 2% | -63% | -89% | -87% |
| DOGE | 2993 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 2990 | 11 | 6% | 3% | -55% | -85% | -85% |
| BTC | 2974 | 14 | 5% | 2% | -36% | -88% | -89% |
| NEAR | 2973 | 15 | 5% | 2% | -35% | -83% | -84% |
| XRP | 2969 | 12 | 3% | 1% | -50% | -89% | -89% |
| GOLD | 1580 | 5 | 5% | 2% | -62% | -81% | -83% |
| SILVER | 1539 | 7 | 5% | 2% | -46% | -82% | -82% |
| WTI | 1538 | 4 | 3% | 1% | -69% | -93% | -93% |
| PLATINUM | 1369 | 3 | 2% | 1% | -80% | -96% | -96% |
| EURUSD | 1310 | 3 | 2% | 1% | -79% | -89% | -89% |
| COPPER | 1306 | 6 | 2% | 1% | -57% | -69% | -68% |
| NATGAS | 1257 | 7 | 2% | 1% | -48% | -81% | -81% |
| GBPUSD | 1241 | 2 | 2% | 1% | -85% | -96% | -96% |
| PALLADIUM | 1234 | 2 | 1% | 0% | -85% | -90% | -91% |
| USDJPY | 1225 | 5 | 2% | 1% | -62% | -97% | -96% |
| AUDUSD | 767 | 4 | 2% | 1% | -51% | -85% | -84% |
| USDCAD | 734 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 342 | 0 | 1% | 1% | -100% | -97% | -96% |
| 10YRRATE | 210 | 1 | 5% | 2% | -56% | -46% | -44% |
| 30YRRATE | 198 | 0 | 2% | 0% | -100% | -97% | -96% |
| 2YRRATE | 191 | 2 | 4% | 1% | -2% | +5% | +6% |
| 5YRRATE | 176 | 1 | 6% | 2% | -47% | -90% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 21954 | 87 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 21203 | 73 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4384 | 21 | 2% | 1% | -17% | -82% | -82% |
| 0.05–0.1% | 4626 | 18 | 3% | 2% | -41% | -91% | -90% |
| 0.1–0.2% | 6971 | 24 | 4% | 2% | -57% | -90% | -90% |
| 0.2–0.5% | 7968 | 33 | 7% | 3% | -54% | -86% | -86% |
| Over 0.5% | 2986 | 12 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10646 | 37 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 10804 | 48 | 4% | 2% | -49% | -85% | -85% |
| Afternoon (12–6pm) | 10198 | 38 | 4% | 2% | -56% | -85% | -85% |
| Evening (6pm–12am) | 11509 | 37 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,768 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/2 7:14:30 PM | EURUSD | UP | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 7:14:30 PM | USDCAD | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 7:13:41 PM | WTI | UP | 78 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 7:13:09 PM | BRENT | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 7:12:34 PM | BTC | UP | 2.4 min | -0.221% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 7:12:18 PM | AUDUSD | UP | 2.7 min | — | 2¢ | ❌ Lost | -$0.15 |
| 11/2 7:12:18 PM | NEAR | UP | 2.7 min | -0.687% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 7:10:57 PM | XRP | UP | 4.0 min | -0.208% | 10¢ | ❌ Lost | -$0.15 |
| 11/2 7:10:57 PM | ZEC | UP | 4.0 min | -0.650% | 4¢ | ❌ Lost | $0.00 |
| 11/2 7:10:38 PM | COPPER | UP | 4.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 7:10:22 PM | GOLD | UP | 4.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 7:09:52 PM | SOL | UP | 5.1 min | -0.388% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 7:09:52 PM | ETH | UP | 5.1 min | -0.264% | 2¢ | ❌ Lost | -$0.15 |
| 11/2 7:09:52 PM | DOGE | UP | 5.1 min | -0.372% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 7:09:33 PM | BNB | UP | 5.5 min | -0.321% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 7:09:33 PM | HYPE | UP | 5.5 min | -0.512% | 5¢ | ❌ Lost | -$0.15 |
| 11/2 6:59:48 PM | BTC | UP | 12 sec | -0.033% | 0¢ | ❌ Lost | $0.00 |
| 11/2 6:59:48 PM | EURUSD | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 6:59:32 PM | GBPUSD | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 6:59:32 PM | BNB | UP | 28 sec | -0.100% | 0¢ | ❌ Lost | $0.00 |
| 11/2 6:59:32 PM | DOGE | UP | 28 sec | -0.061% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 6:59:17 PM | USDCAD | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 6:59:17 PM | ETH | DOWN | 43 sec | +0.040% | 0¢ | ❌ Lost | $0.00 |
| 11/2 6:58:42 PM | AUDUSD | UP | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 6:58:42 PM | ZEC | UP | 78 sec | -0.353% | 0¢ | ❌ Lost | $0.00 |
| 11/2 6:57:55 PM | HYPE | UP | 2.1 min | -0.253% | 0¢ | ❌ Lost | $0.00 |
| 11/2 6:57:39 PM | NEAR | UP | 2.3 min | -0.472% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 6:57:39 PM | COPPER | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 6:55:12 PM | SOL | DOWN | 4.8 min | +0.207% | 12¢ | ❌ Lost | -$0.15 |
| 11/2 6:44:48 PM | GBPUSD | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
