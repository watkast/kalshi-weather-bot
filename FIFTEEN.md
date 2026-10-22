# 15-Minute 1¢ Study

*Updated Thu Oct 22, 5:09 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2400 finished bets | 1% | $78.50 | +29% | +3.27¢ | $37.80 / $40.70 |

*Expect about **97 buys a day** (~$14.58/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2216 | $48.15 | +20% |
| Volatility model ≥ 2%, hold to the close | 4429 | $3.00 | +1% |
| Momentum model ≥ 2%, hold to the close | 3703 | -$30.35 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 28773 | 28765 | 109 (0%) | 1.07% | -$1,982.50 (-57%) | Hold to the close: -$1,982.50 (-57%) |

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
| Volatility model | 18377 | 4.7% | 0.4% (79) | -640% | ❌ Worse |
| Momentum model | 18377 | 4.6% | 0.4% (79) | -666% | ❌ Worse |
| Mean-reversion model | 18377 | 7.9% | 0.4% (79) | -772% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 18377 | 79 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4429 | 39 | +1% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 2400 | 25 | +29% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 1365 | 16 | +65% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 3703 | 29 | -7% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2216 | 21 | +20% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 1458 | 14 | +31% | -69% | -68% | -64% |
| Mean-reversion model ≥ 2% | 7360 | 52 | -23% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 5146 | 43 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3420 | 30 | -0% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 18576 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 6911 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 3278 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 28765 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 109 | 0% | -$1,982.50 | -57% | — |
| Sell at 2¢ | 1058 | 4% | -$3,093.42 | -88% | 47 sec |
| Sell at 3¢ | 722 | 3% | -$3,086.92 | -88% | 48 sec |
| Sell at 5¢ | 507 | 2% | -$3,038.95 | -87% | 61 sec |
| Sell at 10¢ | 311 | 1% | -$2,933.09 | -84% | 64 sec |
| Sell at 25¢ | 172 | 1% | -$2,701.18 | -77% | 82 sec |
| Sell at 50¢ | 113 | 0% | -$2,437.75 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1212 | 7 | 11% | 4% | -45% | -81% | -83% |
| 2–5 min | 9265 | 52 | 7% | 3% | -45% | -87% | -87% |
| 1–2 min | 7305 | 27 | 3% | 1% | -60% | -93% | -93% |
| Under 1 min | 10979 | 23 | 1% | 0% | -70% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2082 | 12 | 5% | 2% | -28% | -89% | -89% |
| BNB | 2077 | 12 | 5% | 3% | -29% | -83% | -82% |
| HYPE | 2074 | 8 | 5% | 3% | -52% | -89% | -87% |
| ETH | 2064 | 10 | 6% | 3% | -42% | -86% | -85% |
| SOL | 2064 | 3 | 3% | 2% | -82% | -92% | -92% |
| DOGE | 2060 | 4 | 4% | 2% | -76% | -90% | -89% |
| XRP | 2055 | 8 | 3% | 1% | -52% | -88% | -88% |
| NEAR | 2051 | 12 | 6% | 3% | -24% | -80% | -80% |
| BTC | 2049 | 12 | 5% | 2% | -22% | -88% | -90% |
| GOLD | 1128 | 3 | 4% | 1% | -69% | -82% | -83% |
| SILVER | 1091 | 4 | 3% | 1% | -58% | -82% | -83% |
| WTI | 1070 | 3 | 3% | 1% | -67% | -94% | -95% |
| PLATINUM | 947 | 0 | 1% | 0% | -100% | -99% | -98% |
| COPPER | 940 | 3 | 1% | 1% | -70% | -78% | -77% |
| EURUSD | 879 | 3 | 2% | 1% | -68% | -85% | -86% |
| NATGAS | 874 | 5 | 2% | 1% | -47% | -86% | -85% |
| PALLADIUM | 849 | 2 | 1% | 0% | -78% | -87% | -87% |
| GBPUSD | 826 | 1 | 2% | 1% | -89% | -97% | -97% |
| USDJPY | 799 | 4 | 1% | 1% | -53% | -99% | -98% |
| AUDUSD | 374 | 0 | 0% | 0% | -100% | -100% | -99% |
| USDCAD | 332 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 21 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 12 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 11 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 14538 | 58 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 14227 | 51 | 3% | 1% | -59% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3081 | 15 | 2% | 1% | -18% | -79% | -78% |
| 0.05–0.1% | 3184 | 11 | 3% | 2% | -49% | -92% | -91% |
| 0.1–0.2% | 4756 | 17 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 5446 | 28 | 6% | 3% | -43% | -87% | -87% |
| Over 0.5% | 2105 | 10 | 7% | 3% | -51% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7128 | 30 | 4% | 2% | -52% | -86% | -85% |
| Morning (6am–12pm) | 7002 | 33 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6893 | 21 | 4% | 2% | -64% | -89% | -89% |
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
| 10/22 4:59:59 PM | ETH | DOWN | 1 sec | +0.019% | 0¢ | ❌ Lost | $0.00 |
| 10/22 4:59:43 PM | SILVER | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 4:59:43 PM | PLATINUM | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 4:59:43 PM | XRP | DOWN | 16 sec | +0.015% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 4:59:43 PM | BNB | DOWN | 16 sec | -0.042% | 0¢ | ❌ Lost | $0.00 |
| 10/22 4:59:43 PM | WTI | DOWN | 16 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/22 4:59:27 PM | SOL | UP | 32 sec | -0.021% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 4:59:27 PM | GBPUSD | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 4:59:27 PM | NEAR | DOWN | 32 sec | +0.080% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 4:59:27 PM | BTC | DOWN | 32 sec | +0.032% | 0¢ | ❌ Lost | $0.00 |
| 10/22 4:58:13 PM | EURUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 4:57:57 PM | DOGE | UP | 2.0 min | -0.144% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 4:57:57 PM | HYPE | UP | 2.0 min | -0.173% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 4:57:42 PM | USDCAD | DOWN | 2.3 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/22 4:57:42 PM | ZEC | UP | 2.3 min | -0.387% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 4:57:10 PM | USDJPY | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 4:56:22 PM | GOLD | UP | 3.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 4:44:32 PM | DOGE | UP | 28 sec | -0.037% | 0¢ | ❌ Lost | $0.00 |
| 10/22 4:44:32 PM | GOLD | DOWN | 28 sec | — | 6¢ | ❌ Lost | -$0.15 |
| 10/22 4:44:16 PM | ZEC | UP | 44 sec | -0.151% | 0¢ | ❌ Lost | $0.00 |
| 10/22 4:44:01 PM | SILVER | UP | 58 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/22 4:43:30 PM | ETH | UP | 89 sec | -0.084% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 4:43:30 PM | GBPUSD | DOWN | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 4:43:30 PM | USDJPY | UP | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 4:43:30 PM | BTC | UP | 89 sec | -0.085% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 4:43:14 PM | EURUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 4:43:14 PM | COPPER | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 4:42:58 PM | XRP | UP | 2.0 min | -0.176% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 4:42:58 PM | HYPE | UP | 2.0 min | -0.158% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 4:42:42 PM | SOL | UP | 2.3 min | -0.186% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
