# 15-Minute 1¢ Study

*Updated Sat Nov 21, 5:10 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4671 finished bets | 1% | $201.90 | +39% | +4.32¢ | $72.60 / $129.30 |

*Expect about **85 buys a day** (~$12.81/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4428 | $99.25 | +21% |
| Volatility model ≥ 2%, hold to the close | 8739 | $45.45 | +4% |
| Momentum model ≥ 2%, hold to the close | 7272 | -$33.15 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 64117 | 64083 | 246 (0%) | 1.07% | -$4,330.95 (-56%) | Hold to the close: -$4,330.95 (-56%) |

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
| Volatility model | 38139 | 4.5% | 0.4% (158) | -638% | ❌ Worse |
| Momentum model | 38139 | 4.4% | 0.4% (158) | -663% | ❌ Worse |
| Mean-reversion model | 38139 | 7.8% | 0.4% (158) | -775% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 38139 | 158 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8739 | 78 | +4% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 4671 | 51 | +39% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 2691 | 30 | +64% | -64% | -62% | -59% |
| Momentum model ≥ 2% | 7272 | 57 | -4% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4428 | 41 | +21% | -75% | -74% | -71% |
| Momentum model ≥ 10% | 2880 | 26 | +29% | -67% | -67% | -63% |
| Mean-reversion model ≥ 2% | 15533 | 109 | -23% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10790 | 89 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7169 | 64 | +2% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 38345 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15273 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10465 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 64083 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 246 | 0% | -$4,330.95 | -56% | — |
| Sell at 2¢ | 2590 | 4% | -$6,807.55 | -88% | 47 sec |
| Sell at 3¢ | 1743 | 3% | -$6,801.18 | -87% | 48 sec |
| Sell at 5¢ | 1187 | 2% | -$6,681.40 | -86% | 62 sec |
| Sell at 10¢ | 725 | 1% | -$6,419.20 | -83% | 65 sec |
| Sell at 25¢ | 389 | 1% | -$5,927.36 | -76% | 80 sec |
| Sell at 50¢ | 252 | 0% | -$5,359.95 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3313 | 17 | 10% | 4% | -51% | -82% | -83% |
| 2–5 min | 20765 | 110 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 16008 | 56 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 23984 | 63 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4286 | 19 | 5% | 2% | -41% | -88% | -87% |
| SOL | 4280 | 19 | 4% | 2% | -43% | -86% | -87% |
| HYPE | 4280 | 14 | 5% | 2% | -58% | -89% | -88% |
| DOGE | 4268 | 11 | 4% | 2% | -67% | -90% | -89% |
| BNB | 4268 | 21 | 5% | 2% | -37% | -86% | -85% |
| ETH | 4262 | 19 | 7% | 3% | -44% | -82% | -82% |
| BTC | 4241 | 23 | 5% | 2% | -26% | -86% | -88% |
| NEAR | 4237 | 18 | 5% | 2% | -44% | -86% | -86% |
| XRP | 4223 | 16 | 3% | 2% | -52% | -89% | -88% |
| GOLD | 2265 | 8 | 5% | 2% | -57% | -82% | -84% |
| WTI | 2257 | 7 | 4% | 1% | -62% | -91% | -92% |
| SILVER | 2209 | 9 | 5% | 2% | -51% | -83% | -83% |
| PLATINUM | 2012 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 1968 | 7 | 3% | 1% | -67% | -91% | -90% |
| GBPUSD | 1900 | 8 | 2% | 1% | -61% | -96% | -95% |
| COPPER | 1895 | 6 | 2% | 1% | -70% | -77% | -77% |
| NATGAS | 1858 | 10 | 2% | 1% | -50% | -76% | -76% |
| USDJPY | 1855 | 6 | 2% | 1% | -70% | -96% | -96% |
| PALLADIUM | 1808 | 4 | 1% | 1% | -79% | -93% | -93% |
| AUDUSD | 1406 | 6 | 2% | 1% | -60% | -90% | -90% |
| USDCAD | 1340 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 969 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 499 | 2 | 3% | 1% | -63% | -76% | -74% |
| 2YRRATE | 476 | 4 | 4% | 2% | -22% | -54% | -53% |
| 30YRRATE | 462 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 451 | 2 | 4% | 2% | -59% | -94% | -95% |
| INX | 108 | 1 | 2% | 1% | -14% | -97% | -98% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 32756 | 127 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 31327 | 119 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5637 | 25 | 2% | 1% | -19% | -78% | -78% |
| 0.05–0.1% | 6149 | 24 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 9543 | 35 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 11954 | 53 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 5053 | 23 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15401 | 48 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 15462 | 81 | 4% | 2% | -40% | -85% | -85% |
| Afternoon (12–6pm) | 15699 | 67 | 4% | 2% | -50% | -87% | -87% |
| Evening (6pm–12am) | 17521 | 50 | 4% | 2% | -67% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,084 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/21 4:58:48 PM | HYPE | DOWN | 72 sec | +0.147% | 1¢ | ❌ Lost | $0.00 |
| 11/21 4:58:32 PM | XRP | UP | 88 sec | -0.140% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 4:58:32 PM | DOGE | DOWN | 88 sec | +0.118% | 0¢ | ❌ Lost | -$0.15 |
| 11/21 4:58:16 PM | BNB | DOWN | 1.7 min | +0.093% | 0¢ | ❌ Lost | -$0.15 |
| 11/21 4:57:45 PM | NEAR | UP | 2.2 min | -0.245% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 4:56:09 PM | ETH | DOWN | 3.8 min | +0.142% | 2¢ | ❌ Lost | -$0.15 |
| 11/21 4:44:57 PM | ETH | DOWN | 3 sec | -0.002% | 0¢ | ❌ Lost | $0.00 |
| 11/21 4:44:25 PM | BTC | UP | 35 sec | -0.068% | 0¢ | ❌ Lost | $0.00 |
| 11/21 4:44:25 PM | SOL | DOWN | 35 sec | +0.058% | 0¢ | ❌ Lost | $0.00 |
| 11/21 4:43:53 PM | NEAR | UP | 67 sec | -0.241% | 0¢ | ❌ Lost | $0.00 |
| 11/21 4:43:37 PM | HYPE | UP | 83 sec | -0.193% | 0¢ | ❌ Lost | -$0.15 |
| 11/21 4:43:37 PM | ZEC | UP | 83 sec | -0.178% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 4:43:05 PM | BNB | UP | 1.9 min | -0.166% | 0¢ | ❌ Lost | -$0.15 |
| 11/21 4:42:34 PM | XRP | DOWN | 2.4 min | +0.204% | 8¢ | ❌ Lost | -$0.15 |
| 11/21 4:42:34 PM | DOGE | DOWN | 2.4 min | +0.158% | 2¢ | ❌ Lost | -$0.15 |
| 11/21 4:29:47 PM | BNB | DOWN | 13 sec | -0.022% | 0¢ | ❌ Lost | $0.00 |
| 11/21 4:29:47 PM | BTC | UP | 13 sec | -0.077% | 0¢ | ❌ Lost | $0.00 |
| 11/21 4:29:47 PM | ETH | UP | 13 sec | -0.036% | 0¢ | ❌ Lost | $0.00 |
| 11/21 4:29:47 PM | DOGE | DOWN | 13 sec | +0.016% | 0¢ | ❌ Lost | $0.00 |
| 11/21 4:29:31 PM | SOL | UP | 29 sec | -0.075% | 0¢ | ❌ Lost | $0.00 |
| 11/21 4:28:19 PM | XRP | DOWN | 1.7 min | +0.215% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 4:28:19 PM | HYPE | DOWN | 1.7 min | +0.241% | 0¢ | ❌ Lost | $0.00 |
| 11/21 4:27:46 PM | NEAR | DOWN | 2.2 min | +0.311% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 4:26:24 PM | ZEC | UP | 3.6 min | -0.476% | 2¢ | ❌ Lost | -$0.15 |
| 11/21 4:13:53 PM | HYPE | DOWN | 66 sec | +0.049% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 4:13:05 PM | ZEC | DOWN | 1.9 min | +0.357% | 3¢ | ❌ Lost | -$0.15 |
| 11/21 4:13:05 PM | DOGE | DOWN | 1.9 min | +0.189% | 0¢ | ❌ Lost | $0.00 |
| 11/21 4:13:05 PM | NEAR | DOWN | 1.9 min | +0.239% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 4:12:48 PM | SOL | DOWN | 2.2 min | +0.194% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 4:12:32 PM | BTC | DOWN | 2.5 min | +0.259% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
