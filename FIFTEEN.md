# 15-Minute 1¢ Study

*Updated Thu Oct 22, 5:40 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2401 finished bets | 1% | $78.35 | +29% | +3.26¢ | $37.80 / $40.55 |

*Expect about **97 buys a day** (~$14.58/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2219 | $47.85 | +19% |
| Volatility model ≥ 2%, hold to the close | 4434 | $2.40 | +0% |
| Momentum model ≥ 2%, hold to the close | 3706 | -$30.65 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 28804 | 28796 | 109 (0%) | 1.07% | -$1,985.65 (-57%) | Hold to the close: -$1,985.65 (-57%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 18392 | 4.7% | 0.4% (79) | -640% | ❌ Worse |
| Momentum model | 18392 | 4.6% | 0.4% (79) | -666% | ❌ Worse |
| Mean-reversion model | 18392 | 7.9% | 0.4% (79) | -772% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 18392 | 79 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4434 | 39 | +0% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 2401 | 25 | +29% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 1366 | 16 | +65% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 3706 | 29 | -7% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2219 | 21 | +19% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 1459 | 14 | +31% | -69% | -68% | -64% |
| Mean-reversion model ≥ 2% | 7363 | 52 | -23% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 5149 | 43 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3423 | 30 | -1% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 18591 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 6919 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 3286 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 28796 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 109 | 0% | -$1,985.65 | -57% | — |
| Sell at 2¢ | 1058 | 4% | -$3,096.57 | -88% | 47 sec |
| Sell at 3¢ | 722 | 3% | -$3,090.07 | -88% | 48 sec |
| Sell at 5¢ | 507 | 2% | -$3,042.10 | -87% | 61 sec |
| Sell at 10¢ | 311 | 1% | -$2,936.24 | -84% | 64 sec |
| Sell at 25¢ | 172 | 1% | -$2,704.33 | -77% | 82 sec |
| Sell at 50¢ | 113 | 0% | -$2,440.90 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1212 | 7 | 11% | 4% | -45% | -81% | -83% |
| 2–5 min | 9271 | 52 | 7% | 3% | -45% | -87% | -87% |
| 1–2 min | 7313 | 27 | 3% | 1% | -60% | -93% | -93% |
| Under 1 min | 10996 | 23 | 1% | 0% | -70% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2084 | 12 | 5% | 2% | -28% | -89% | -89% |
| BNB | 2077 | 12 | 5% | 3% | -29% | -83% | -82% |
| HYPE | 2075 | 8 | 5% | 3% | -52% | -89% | -87% |
| ETH | 2066 | 10 | 6% | 3% | -42% | -86% | -85% |
| SOL | 2066 | 3 | 3% | 2% | -82% | -92% | -92% |
| DOGE | 2062 | 4 | 4% | 2% | -76% | -90% | -89% |
| XRP | 2057 | 8 | 3% | 1% | -52% | -88% | -88% |
| NEAR | 2053 | 12 | 6% | 3% | -24% | -80% | -80% |
| BTC | 2051 | 12 | 5% | 2% | -22% | -88% | -90% |
| GOLD | 1130 | 3 | 4% | 1% | -69% | -82% | -83% |
| SILVER | 1091 | 4 | 3% | 1% | -58% | -82% | -83% |
| WTI | 1072 | 3 | 3% | 1% | -67% | -94% | -95% |
| PLATINUM | 949 | 0 | 1% | 0% | -100% | -99% | -98% |
| COPPER | 940 | 3 | 1% | 1% | -70% | -78% | -77% |
| EURUSD | 881 | 3 | 2% | 1% | -68% | -85% | -86% |
| NATGAS | 875 | 5 | 2% | 1% | -47% | -86% | -85% |
| PALLADIUM | 849 | 2 | 1% | 0% | -78% | -87% | -87% |
| GBPUSD | 828 | 1 | 2% | 1% | -89% | -97% | -97% |
| USDJPY | 801 | 4 | 1% | 1% | -53% | -99% | -98% |
| AUDUSD | 374 | 0 | 0% | 0% | -100% | -100% | -99% |
| USDCAD | 334 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 21 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 13 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 11 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 14551 | 58 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 14245 | 51 | 3% | 1% | -59% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3084 | 15 | 2% | 1% | -18% | -79% | -78% |
| 0.05–0.1% | 3189 | 11 | 3% | 2% | -49% | -92% | -91% |
| 0.1–0.2% | 4762 | 17 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 5447 | 28 | 6% | 3% | -43% | -87% | -87% |
| Over 0.5% | 2105 | 10 | 7% | 3% | -51% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7128 | 30 | 4% | 2% | -52% | -86% | -85% |
| Morning (6am–12pm) | 7002 | 33 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6924 | 21 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 7742 | 25 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,682 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/22 5:29:36 PM | NEAR | UP | 23 sec | -0.164% | 0¢ | ❌ Lost | $0.00 |
| 10/22 5:29:36 PM | NATGAS | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 5:29:36 PM | USDCAD | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 5:29:36 PM | GBPUSD | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 5:29:20 PM | EURUSD | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 5:29:20 PM | ZEC | UP | 39 sec | -0.145% | 0¢ | ❌ Lost | $0.00 |
| 10/22 5:29:20 PM | BTC | UP | 39 sec | -0.078% | 0¢ | ❌ Lost | $0.00 |
| 10/22 5:29:20 PM | GOLD | DOWN | 39 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/22 5:29:20 PM | ETH | UP | 39 sec | -0.067% | 0¢ | ❌ Lost | $0.00 |
| 10/22 5:29:04 PM | SOL | UP | 55 sec | -0.088% | 0¢ | ❌ Lost | $0.00 |
| 10/22 5:28:49 PM | XRP | UP | 71 sec | -0.130% | 0¢ | ❌ Lost | $0.00 |
| 10/22 5:28:49 PM | BRENT | DOWN | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 5:28:33 PM | PLATINUM | UP | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 5:28:16 PM | USDJPY | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 5:28:16 PM | DOGE | DOWN | 1.7 min | +0.057% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 5:26:26 PM | WTI | DOWN | 3.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 5:14:48 PM | GOLD | UP | 11 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 5:14:48 PM | ETH | DOWN | 11 sec | +0.025% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 5:14:32 PM | BTC | DOWN | 27 sec | +0.029% | 0¢ | ❌ Lost | $0.00 |
| 10/22 5:14:32 PM | DOGE | DOWN | 27 sec | +0.017% | 0¢ | ❌ Lost | $0.00 |
| 10/22 5:14:16 PM | NEAR | DOWN | 43 sec | +0.105% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 5:14:00 PM | WTI | DOWN | 59 sec | — | 1¢ | ❌ Lost | $0.00 |
| 10/22 5:14:00 PM | SOL | DOWN | 59 sec | +0.068% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 5:13:45 PM | PLATINUM | UP | 75 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 5:13:45 PM | EURUSD | DOWN | 75 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 5:13:45 PM | GBPUSD | DOWN | 75 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 5:12:57 PM | ZEC | DOWN | 2.0 min | +0.288% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 5:12:41 PM | USDCAD | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 5:12:25 PM | XRP | DOWN | 2.6 min | +0.115% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 5:12:09 PM | USDJPY | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
