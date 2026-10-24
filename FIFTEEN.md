# 15-Minute 1¢ Study

*Updated Fri Oct 23, 7:02 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2509 finished bets | 1% | $93.75 | +33% | +3.74¢ | $44.45 / $49.30 |

*Expect about **97 buys a day** (~$14.61/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2320 | $51.35 | +20% |
| Volatility model ≥ 2%, hold to the close | 4652 | $4.15 | +1% |
| Momentum model ≥ 2%, hold to the close | 3876 | -$21.85 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 30459 | 30451 | 117 (0%) | 1.07% | -$2,078.40 (-56%) | Hold to the close: -$2,078.40 (-56%) |

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
| Volatility model | 19261 | 4.6% | 0.4% (82) | -634% | ❌ Worse |
| Momentum model | 19261 | 4.5% | 0.4% (82) | -661% | ❌ Worse |
| Mean-reversion model | 19261 | 7.9% | 0.4% (82) | -765% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 19261 | 82 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4652 | 41 | +1% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2509 | 27 | +33% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 1430 | 17 | +67% | -64% | -62% | -59% |
| Momentum model ≥ 2% | 3876 | 31 | -5% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2320 | 22 | +20% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1523 | 15 | +36% | -69% | -68% | -63% |
| Mean-reversion model ≥ 2% | 7745 | 54 | -24% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5412 | 45 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3600 | 32 | +1% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 19461 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 7335 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3655 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 30451 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 117 | 0% | -$2,078.40 | -56% | — |
| Sell at 2¢ | 1138 | 4% | -$3,252.52 | -88% | 47 sec |
| Sell at 3¢ | 782 | 3% | -$3,243.42 | -87% | 48 sec |
| Sell at 5¢ | 547 | 2% | -$3,192.85 | -86% | 61 sec |
| Sell at 10¢ | 335 | 1% | -$3,067.55 | -83% | 64 sec |
| Sell at 25¢ | 185 | 1% | -$2,824.05 | -76% | 82 sec |
| Sell at 50¢ | 119 | 0% | -$2,549.15 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1306 | 7 | 11% | 4% | -49% | -80% | -82% |
| 2–5 min | 9747 | 53 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 7752 | 29 | 3% | 1% | -59% | -91% | -91% |
| Under 1 min | 11642 | 28 | 1% | 0% | -66% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2181 | 12 | 5% | 2% | -31% | -89% | -89% |
| HYPE | 2172 | 8 | 5% | 3% | -55% | -88% | -86% |
| BNB | 2172 | 12 | 5% | 2% | -32% | -83% | -82% |
| SOL | 2165 | 5 | 4% | 2% | -71% | -92% | -92% |
| ETH | 2162 | 10 | 6% | 3% | -44% | -86% | -85% |
| DOGE | 2158 | 4 | 4% | 2% | -77% | -90% | -89% |
| XRP | 2153 | 9 | 3% | 1% | -48% | -88% | -88% |
| NEAR | 2150 | 12 | 5% | 3% | -28% | -81% | -81% |
| BTC | 2148 | 12 | 5% | 2% | -25% | -88% | -89% |
| GOLD | 1190 | 4 | 4% | 2% | -60% | -81% | -83% |
| SILVER | 1156 | 5 | 4% | 1% | -50% | -82% | -82% |
| WTI | 1133 | 3 | 3% | 1% | -69% | -94% | -95% |
| PLATINUM | 1010 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 987 | 4 | 1% | 1% | -62% | -69% | -69% |
| EURUSD | 938 | 3 | 2% | 1% | -70% | -86% | -86% |
| NATGAS | 931 | 5 | 2% | 1% | -50% | -86% | -86% |
| PALLADIUM | 897 | 2 | 1% | 0% | -79% | -88% | -88% |
| GBPUSD | 884 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 866 | 5 | 1% | 1% | -46% | -98% | -97% |
| AUDUSD | 428 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 387 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 31 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 15384 | 64 | 4% | 2% | -52% | -87% | -86% |
| DOWN (bought NO) | 15067 | 53 | 4% | 2% | -60% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3193 | 17 | 2% | 1% | -10% | -79% | -78% |
| 0.05–0.1% | 3340 | 11 | 3% | 2% | -52% | -92% | -91% |
| 0.1–0.2% | 5013 | 18 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 5715 | 28 | 6% | 3% | -46% | -87% | -86% |
| Over 0.5% | 2196 | 10 | 7% | 3% | -53% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7532 | 31 | 4% | 2% | -53% | -84% | -84% |
| Morning (6am–12pm) | 7425 | 34 | 4% | 2% | -48% | -88% | -87% |
| Afternoon (12–6pm) | 7298 | 24 | 4% | 2% | -61% | -87% | -88% |
| Evening (6pm–12am) | 8196 | 28 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,616 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/23 6:59:51 PM | WTI | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 6:59:19 PM | BTC | DOWN | 41 sec | +0.025% | 21¢ | ❌ Lost | -$0.15 |
| 10/23 6:58:44 PM | ZEC | DOWN | 76 sec | +0.356% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 6:58:44 PM | BNB | DOWN | 76 sec | +0.080% | 0¢ | ❌ Lost | $0.00 |
| 10/23 6:58:44 PM | XRP | DOWN | 76 sec | +0.156% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 6:58:28 PM | DOGE | DOWN | 1.5 min | +0.189% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 6:58:28 PM | ETH | DOWN | 1.5 min | +0.163% | 0¢ | ❌ Lost | $0.00 |
| 10/23 6:58:28 PM | HYPE | DOWN | 1.5 min | +0.217% | 0¢ | ❌ Lost | $0.00 |
| 10/23 6:58:13 PM | SOL | DOWN | 1.8 min | +0.139% | 0¢ | ❌ Lost | $0.00 |
| 10/23 6:57:55 PM | NEAR | DOWN | 2.1 min | +0.484% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 6:43:19 PM | HYPE | UP | 1.7 min | -0.249% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 6:43:03 PM | DOGE | UP | 1.9 min | -0.310% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 6:42:47 PM | ETH | UP | 2.2 min | -0.236% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 6:42:31 PM | BTC | UP | 2.5 min | -0.191% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 6:42:31 PM | XRP | UP | 2.5 min | -0.295% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 6:41:33 PM | BNB | UP | 3.4 min | -0.216% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 6:41:01 PM | SOL | UP | 4.0 min | -0.322% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 6:40:44 PM | ZEC | UP | 4.2 min | -0.696% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 6:40:12 PM | NEAR | UP | 4.8 min | -1.042% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 6:24:47 PM | ETH | UP | 5.2 min | -0.392% | 3¢ | ❌ Lost | -$0.15 |
| 10/23 6:24:29 PM | BTC | UP | 5.5 min | -0.318% | 4¢ | ❌ Lost | -$0.15 |
| 10/23 6:24:29 PM | SOL | UP | 5.5 min | -0.389% | 11¢ | ❌ Lost | -$0.15 |
| 10/23 6:23:57 PM | XRP | UP | 6.0 min | -0.403% | 4¢ | ❌ Lost | -$0.15 |
| 10/23 6:23:42 PM | NEAR | UP | 6.3 min | -0.976% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 6:23:42 PM | HYPE | UP | 6.3 min | -0.721% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 6:14:51 PM | NEAR | UP | 9 sec | -0.271% | 0¢ | ❌ Lost | $0.00 |
| 10/23 6:14:04 PM | DOGE | UP | 55 sec | -0.134% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 6:13:48 PM | ZEC | UP | 71 sec | -0.285% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 6:13:32 PM | XRP | UP | 87 sec | -0.201% | 0¢ | ❌ Lost | $0.00 |
| 10/23 6:13:16 PM | BNB | UP | 1.7 min | -0.110% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
