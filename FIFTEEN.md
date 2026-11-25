# 15-Minute 1¢ Study

*Updated Wed Nov 25, 12:19 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4896 finished bets | 1% | $208.75 | +39% | +4.26¢ | $87.25 / $121.50 |

*Expect about **84 buys a day** (~$12.55/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4637 | $108.20 | +22% |
| Volatility model ≥ 2%, hold to the close | 9125 | $46.95 | +4% |
| Momentum model ≥ 2%, hold to the close | 7588 | -$35.30 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 67717 | 67683 | 256 (0%) | 1.07% | -$4,610.95 (-56%) | Hold to the close: -$4,610.95 (-56%) |

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
| Volatility model | 40115 | 4.5% | 0.4% (165) | -646% | ❌ Worse |
| Momentum model | 40115 | 4.4% | 0.4% (165) | -669% | ❌ Worse |
| Mean-reversion model | 40115 | 7.9% | 0.4% (165) | -786% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 40115 | 165 | -46% | -87% | -86% | -84% |
| Volatility model ≥ 2% | 9125 | 81 | +4% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 4896 | 53 | +39% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 2832 | 32 | +67% | -65% | -63% | -59% |
| Momentum model ≥ 2% | 7588 | 59 | -4% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 4637 | 43 | +22% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 3022 | 28 | +34% | -68% | -68% | -63% |
| Mean-reversion model ≥ 2% | 16336 | 113 | -24% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11379 | 93 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7555 | 66 | -0% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 40321 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 16110 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 11252 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 67683 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 256 | 0% | -$4,610.95 | -56% | — |
| Sell at 2¢ | 2772 | 4% | -$7,180.23 | -88% | 47 sec |
| Sell at 3¢ | 1861 | 3% | -$7,175.16 | -88% | 48 sec |
| Sell at 5¢ | 1260 | 2% | -$7,053.95 | -86% | 62 sec |
| Sell at 10¢ | 769 | 1% | -$6,781.56 | -83% | 65 sec |
| Sell at 25¢ | 415 | 1% | -$6,261.30 | -76% | 79 sec |
| Sell at 50¢ | 266 | 0% | -$5,657.45 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3497 | 17 | 11% | 4% | -54% | -81% | -83% |
| 2–5 min | 21949 | 116 | 7% | 3% | -48% | -86% | -86% |
| 1–2 min | 16880 | 58 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 25344 | 65 | 1% | 0% | -63% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4509 | 20 | 5% | 2% | -41% | -88% | -87% |
| HYPE | 4503 | 16 | 5% | 2% | -54% | -89% | -88% |
| SOL | 4496 | 20 | 4% | 2% | -42% | -86% | -86% |
| BNB | 4490 | 22 | 5% | 2% | -37% | -86% | -85% |
| DOGE | 4486 | 12 | 4% | 2% | -65% | -89% | -89% |
| ETH | 4480 | 19 | 7% | 3% | -47% | -82% | -82% |
| BTC | 4459 | 24 | 6% | 2% | -26% | -86% | -87% |
| NEAR | 4455 | 18 | 5% | 2% | -47% | -85% | -86% |
| XRP | 4443 | 16 | 4% | 2% | -54% | -89% | -88% |
| GOLD | 2383 | 8 | 5% | 2% | -59% | -83% | -84% |
| WTI | 2371 | 8 | 4% | 2% | -59% | -91% | -92% |
| SILVER | 2324 | 9 | 5% | 2% | -54% | -83% | -84% |
| PLATINUM | 2110 | 5 | 3% | 1% | -78% | -95% | -95% |
| EURUSD | 2063 | 7 | 3% | 1% | -68% | -91% | -90% |
| GBPUSD | 2005 | 8 | 2% | 1% | -63% | -96% | -96% |
| COPPER | 2000 | 6 | 2% | 1% | -72% | -78% | -78% |
| USDJPY | 1963 | 6 | 2% | 1% | -71% | -96% | -96% |
| NATGAS | 1959 | 10 | 2% | 1% | -52% | -77% | -77% |
| PALLADIUM | 1896 | 4 | 1% | 1% | -80% | -93% | -93% |
| AUDUSD | 1526 | 7 | 2% | 1% | -57% | -90% | -90% |
| USDCAD | 1436 | 1 | 3% | 1% | -94% | -96% | -96% |
| BRENT | 1067 | 1 | 2% | 1% | -91% | -96% | -97% |
| 10YRRATE | 555 | 2 | 3% | 1% | -66% | -78% | -76% |
| 30YRRATE | 516 | 0 | 3% | 1% | -100% | -95% | -93% |
| 2YRRATE | 514 | 4 | 4% | 2% | -27% | -57% | -57% |
| 5YRRATE | 504 | 2 | 4% | 2% | -63% | -94% | -95% |
| INX | 137 | 1 | 2% | 1% | -32% | -96% | -96% |
| USDMXN | 33 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 34586 | 132 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 33097 | 124 | 4% | 2% | -57% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5850 | 25 | 2% | 1% | -21% | -79% | -78% |
| 0.05–0.1% | 6403 | 26 | 3% | 2% | -35% | -91% | -91% |
| 0.1–0.2% | 10004 | 36 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12707 | 56 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 5348 | 24 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16330 | 50 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 16129 | 82 | 4% | 2% | -42% | -86% | -85% |
| Afternoon (12–6pm) | 16659 | 73 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 18565 | 51 | 4% | 2% | -68% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,092 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/25 12:14:51 PM | BRENT | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 12:14:51 PM | WTI | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 12:14:51 PM | USDMXN | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 12:14:51 PM | INX | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 12:14:51 PM | USDCAD | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 12:14:35 PM | 10YRRATE | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 12:14:35 PM | NATGAS | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 12:14:16 PM | 30YRRATE | UP | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 12:14:16 PM | EURUSD | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 12:14:00 PM | GBPUSD | DOWN | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 12:14:00 PM | NEAR | DOWN | 59 sec | +0.238% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 12:14:00 PM | ZEC | DOWN | 59 sec | +0.416% | 0¢ | ❌ Lost | -$0.15 |
| 11/25 12:12:52 PM | ETH | DOWN | 2.1 min | +0.256% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 12:12:21 PM | SOL | DOWN | 2.6 min | +0.329% | 1¢ | ❌ Lost | $0.00 |
| 11/25 12:12:03 PM | BTC | DOWN | 3.0 min | +0.391% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 12:11:31 PM | COPPER | DOWN | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 12:11:31 PM | HYPE | DOWN | 3.5 min | +0.602% | 0¢ | ❌ Lost | -$0.15 |
| 11/25 12:11:15 PM | AUDUSD | DOWN | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 12:11:15 PM | PALLADIUM | DOWN | 3.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/25 12:10:39 PM | DOGE | DOWN | 4.3 min | +0.594% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 12:10:08 PM | BNB | DOWN | 4.9 min | +0.392% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 12:10:08 PM | XRP | DOWN | 4.9 min | +0.700% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 12:10:08 PM | PLATINUM | DOWN | 4.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 12:10:08 PM | GOLD | DOWN | 4.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/25 12:09:48 PM | SILVER | DOWN | 5.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/25 11:59:55 AM | AUDUSD | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 11:59:55 AM | 30YRRATE | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 11:59:39 AM | ETH | DOWN | 20 sec | +0.034% | 0¢ | ❌ Lost | -$0.15 |
| 11/25 11:59:39 AM | HYPE | DOWN | 20 sec | +0.036% | 0¢ | ❌ Lost | $0.00 |
| 11/25 11:59:23 AM | GBPUSD | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
