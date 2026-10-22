# 15-Minute 1¢ Study

*Updated Thu Oct 22, 3:57 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2397 finished bets | 1% | $78.80 | +29% | +3.29¢ | $38.10 / $40.70 |

*Expect about **97 buys a day** (~$14.59/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2213 | $48.45 | +20% |
| Volatility model ≥ 2%, hold to the close | 4416 | $4.80 | +1% |
| Momentum model ≥ 2%, hold to the close | 3699 | -$29.90 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 28702 | 28694 | 109 (0%) | 1.07% | -$1,974.40 (-56%) | Hold to the close: -$1,974.40 (-56%) |

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
| Volatility model | 18333 | 4.7% | 0.4% (79) | -639% | ❌ Worse |
| Momentum model | 18333 | 4.6% | 0.4% (79) | -665% | ❌ Worse |
| Mean-reversion model | 18333 | 7.9% | 0.4% (79) | -770% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 18333 | 79 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4416 | 39 | +1% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 2397 | 25 | +29% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 1362 | 16 | +65% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 3699 | 29 | -7% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2213 | 21 | +20% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 1455 | 14 | +32% | -69% | -68% | -64% |
| Mean-reversion model ≥ 2% | 7339 | 52 | -23% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 5130 | 43 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3412 | 30 | -0% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 18532 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 6895 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 3267 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 28694 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 109 | 0% | -$1,974.40 | -56% | — |
| Sell at 2¢ | 1055 | 4% | -$3,086.10 | -88% | 47 sec |
| Sell at 3¢ | 720 | 3% | -$3,079.60 | -88% | 48 sec |
| Sell at 5¢ | 506 | 2% | -$3,031.50 | -87% | 61 sec |
| Sell at 10¢ | 311 | 1% | -$2,924.99 | -84% | 64 sec |
| Sell at 25¢ | 172 | 1% | -$2,693.08 | -77% | 82 sec |
| Sell at 50¢ | 113 | 0% | -$2,429.65 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1212 | 7 | 11% | 4% | -45% | -81% | -83% |
| 2–5 min | 9240 | 52 | 7% | 3% | -44% | -87% | -87% |
| 1–2 min | 7287 | 27 | 3% | 1% | -60% | -93% | -93% |
| Under 1 min | 10951 | 23 | 1% | 0% | -70% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2077 | 12 | 5% | 2% | -28% | -89% | -89% |
| BNB | 2072 | 12 | 5% | 3% | -29% | -83% | -82% |
| HYPE | 2069 | 8 | 5% | 3% | -52% | -88% | -87% |
| ETH | 2059 | 10 | 6% | 3% | -42% | -86% | -85% |
| SOL | 2059 | 3 | 3% | 2% | -82% | -92% | -92% |
| DOGE | 2055 | 4 | 4% | 2% | -76% | -90% | -90% |
| XRP | 2050 | 8 | 3% | 1% | -52% | -88% | -88% |
| NEAR | 2046 | 12 | 6% | 3% | -24% | -80% | -80% |
| BTC | 2045 | 12 | 5% | 2% | -22% | -88% | -90% |
| GOLD | 1125 | 3 | 4% | 1% | -68% | -82% | -84% |
| SILVER | 1088 | 4 | 3% | 1% | -57% | -82% | -83% |
| WTI | 1066 | 3 | 3% | 1% | -67% | -94% | -95% |
| PLATINUM | 945 | 0 | 1% | 0% | -100% | -99% | -98% |
| COPPER | 938 | 3 | 1% | 1% | -70% | -78% | -77% |
| EURUSD | 877 | 3 | 2% | 1% | -68% | -85% | -86% |
| NATGAS | 873 | 5 | 2% | 1% | -47% | -86% | -85% |
| PALLADIUM | 848 | 2 | 1% | 0% | -78% | -87% | -87% |
| GBPUSD | 822 | 1 | 2% | 1% | -89% | -97% | -97% |
| USDJPY | 796 | 4 | 1% | 1% | -53% | -99% | -98% |
| AUDUSD | 374 | 0 | 0% | 0% | -100% | -100% | -99% |
| USDCAD | 330 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 21 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 12 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 11 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 14495 | 58 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 14199 | 51 | 3% | 1% | -59% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3070 | 15 | 2% | 1% | -18% | -79% | -78% |
| 0.05–0.1% | 3176 | 11 | 3% | 2% | -49% | -92% | -91% |
| 0.1–0.2% | 4741 | 17 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 5439 | 28 | 6% | 3% | -43% | -87% | -87% |
| Over 0.5% | 2102 | 10 | 7% | 3% | -51% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7128 | 30 | 4% | 2% | -52% | -86% | -85% |
| Morning (6am–12pm) | 7002 | 33 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6822 | 21 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 7742 | 25 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,679 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/22 3:44:47 PM | BTC | UP | 13 sec | -0.020% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 3:44:47 PM | ETH | UP | 13 sec | -0.025% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:44:15 PM | USDJPY | DOWN | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 3:43:59 PM | GBPUSD | DOWN | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 3:43:25 PM | NEAR | UP | 1.6 min | -0.409% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:43:25 PM | BNB | UP | 1.6 min | -0.164% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:42:55 PM | DOGE | UP | 2.1 min | -0.104% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:42:40 PM | ZEC | UP | 2.3 min | -0.359% | 0¢ | ❌ Lost | $0.00 |
| 10/22 3:42:24 PM | XRP | UP | 2.6 min | -0.191% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 3:42:08 PM | HYPE | UP | 2.9 min | -0.252% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:41:51 PM | SOL | UP | 3.1 min | -0.237% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:29:59 PM | NEAR | DOWN | 0 sec | -0.039% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 3:29:59 PM | WTI | DOWN | 0 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/22 3:29:28 PM | BRENT | DOWN | 32 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:29:12 PM | HYPE | DOWN | 48 sec | +0.073% | 0¢ | ❌ Lost | $0.00 |
| 10/22 3:26:48 PM | BTC | DOWN | 3.2 min | +0.129% | 3¢ | ❌ Lost | -$0.15 |
| 10/22 3:25:17 PM | XRP | DOWN | 4.7 min | +0.276% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:25:17 PM | ZEC | DOWN | 4.7 min | +0.512% | 6¢ | ❌ Lost | -$0.15 |
| 10/22 3:25:17 PM | SOL | DOWN | 4.7 min | +0.243% | 4¢ | ❌ Lost | -$0.15 |
| 10/22 3:24:45 PM | DOGE | DOWN | 5.2 min | +0.263% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:23:57 PM | ETH | DOWN | 6.0 min | +0.271% | 4¢ | ❌ Lost | -$0.15 |
| 10/22 3:23:10 PM | BNB | DOWN | 6.8 min | +0.164% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:14:29 PM | NATGAS | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 3:13:58 PM | WTI | UP | 61 sec | — | 2¢ | ❌ Lost | $0.00 |
| 10/22 3:11:04 PM | BTC | DOWN | 3.9 min | +0.188% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:10:48 PM | BNB | DOWN | 4.2 min | +0.144% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:10:30 PM | ETH | DOWN | 4.5 min | +0.312% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:09:58 PM | SOL | DOWN | 5.0 min | +0.288% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:09:43 PM | NEAR | DOWN | 5.3 min | +0.589% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 3:09:43 PM | DOGE | DOWN | 5.3 min | +0.415% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
