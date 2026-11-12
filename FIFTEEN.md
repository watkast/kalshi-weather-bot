# 15-Minute 1¢ Study

*Updated Wed Nov 11, 8:55 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4227 finished bets | 1% | $174.80 | +37% | +4.14¢ | $84.70 / $90.10 |

*Expect about **94 buys a day** (~$14.13/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3957 | $103.60 | +24% |
| Volatility model ≥ 2%, hold to the close | 7769 | $45.05 | +5% |
| Momentum model ≥ 2%, hold to the close | 6450 | -$13.15 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 54263 | 54242 | 208 (0%) | 1.07% | -$3,704.65 (-56%) | Hold to the close: -$3,704.65 (-56%) |

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
| Volatility model | 32595 | 4.7% | 0.4% (132) | -668% | ❌ Worse |
| Momentum model | 32595 | 4.6% | 0.4% (132) | -693% | ❌ Worse |
| Mean-reversion model | 32595 | 8.1% | 0.4% (132) | -810% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 32595 | 132 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7769 | 70 | +5% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4227 | 46 | +37% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2442 | 28 | +65% | -62% | -61% | -57% |
| Momentum model ≥ 2% | 6450 | 52 | -2% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3957 | 38 | +24% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2595 | 25 | +36% | -66% | -65% | -61% |
| Mean-reversion model ≥ 2% | 13459 | 92 | -25% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 9409 | 78 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6283 | 56 | +1% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 32800 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 13009 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8433 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 54242 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 208 | 0% | -$3,704.65 | -56% | — |
| Sell at 2¢ | 2158 | 4% | -$5,761.57 | -87% | 47 sec |
| Sell at 3¢ | 1468 | 3% | -$5,750.13 | -87% | 48 sec |
| Sell at 5¢ | 1016 | 2% | -$5,634.25 | -85% | 63 sec |
| Sell at 10¢ | 614 | 1% | -$5,406.31 | -82% | 65 sec |
| Sell at 25¢ | 327 | 1% | -$5,016.28 | -76% | 82 sec |
| Sell at 50¢ | 214 | 0% | -$4,542.15 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2706 | 13 | 11% | 4% | -54% | -81% | -83% |
| 2–5 min | 17555 | 96 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 13695 | 45 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 20274 | 54 | 1% | 0% | -62% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3671 | 17 | 5% | 2% | -40% | -88% | -87% |
| SOL | 3668 | 16 | 4% | 2% | -44% | -86% | -86% |
| HYPE | 3660 | 11 | 5% | 2% | -62% | -89% | -88% |
| BNB | 3652 | 19 | 5% | 2% | -35% | -86% | -85% |
| DOGE | 3648 | 8 | 4% | 2% | -72% | -90% | -90% |
| ETH | 3643 | 16 | 7% | 3% | -45% | -82% | -81% |
| NEAR | 3624 | 17 | 5% | 2% | -39% | -85% | -85% |
| BTC | 3623 | 17 | 5% | 2% | -36% | -87% | -88% |
| XRP | 3611 | 13 | 3% | 1% | -55% | -89% | -89% |
| GOLD | 1954 | 5 | 5% | 2% | -69% | -82% | -83% |
| WTI | 1946 | 6 | 4% | 2% | -63% | -91% | -92% |
| SILVER | 1906 | 9 | 5% | 2% | -44% | -83% | -83% |
| PLATINUM | 1736 | 4 | 3% | 1% | -78% | -96% | -95% |
| EURUSD | 1672 | 5 | 2% | 1% | -72% | -90% | -90% |
| COPPER | 1621 | 6 | 2% | 1% | -65% | -74% | -74% |
| GBPUSD | 1600 | 6 | 2% | 1% | -65% | -96% | -96% |
| NATGAS | 1593 | 9 | 2% | 1% | -47% | -73% | -73% |
| USDJPY | 1574 | 6 | 2% | 1% | -64% | -97% | -96% |
| PALLADIUM | 1559 | 4 | 1% | 1% | -76% | -92% | -92% |
| AUDUSD | 1128 | 6 | 2% | 1% | -50% | -88% | -88% |
| USDCAD | 1093 | 0 | 2% | 1% | -100% | -96% | -96% |
| BRENT | 694 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 353 | 2 | 4% | 2% | -47% | -66% | -64% |
| 2YRRATE | 338 | 4 | 4% | 2% | +10% | -38% | -36% |
| 30YRRATE | 332 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 311 | 2 | 4% | 2% | -40% | -93% | -95% |
| INX | 32 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 27533 | 108 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 26709 | 100 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5191 | 25 | 2% | 1% | -15% | -77% | -77% |
| 0.05–0.1% | 5564 | 20 | 3% | 2% | -45% | -91% | -91% |
| 0.1–0.2% | 8417 | 31 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 9877 | 41 | 6% | 3% | -54% | -87% | -86% |
| Over 0.5% | 3743 | 17 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13236 | 43 | 4% | 2% | -63% | -88% | -88% |
| Morning (6am–12pm) | 13083 | 60 | 4% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 13132 | 58 | 4% | 2% | -48% | -86% | -86% |
| Evening (6pm–12am) | 14791 | 47 | 4% | 2% | -64% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,872 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/11 8:44:56 PM | USDJPY | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 8:44:40 PM | NEAR | UP | 19 sec | -0.172% | 0¢ | ❌ Lost | $0.00 |
| 11/11 8:44:40 PM | BRENT | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 8:44:23 PM | GBPUSD | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 8:44:23 PM | EURUSD | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 8:44:23 PM | SOL | UP | 36 sec | -0.106% | 0¢ | ❌ Lost | -$0.15 |
| 11/11 8:44:23 PM | PALLADIUM | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 8:43:50 PM | PLATINUM | UP | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 8:43:50 PM | ETH | UP | 69 sec | -0.115% | 2¢ | ❌ Lost | -$0.15 |
| 11/11 8:43:50 PM | ZEC | UP | 69 sec | -0.344% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 8:43:50 PM | DOGE | UP | 69 sec | -0.149% | 0¢ | ❌ Lost | -$0.15 |
| 11/11 8:43:34 PM | HYPE | UP | 85 sec | -0.251% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 8:43:34 PM | WTI | DOWN | 85 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/11 8:43:34 PM | GOLD | UP | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 8:43:34 PM | BNB | UP | 85 sec | -0.165% | 0¢ | ❌ Lost | $0.00 |
| 11/11 8:43:17 PM | COPPER | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 8:43:17 PM | BTC | UP | 1.7 min | -0.111% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 8:42:42 PM | XRP | UP | 2.3 min | -0.210% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 8:29:53 PM | PLATINUM | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 8:29:37 PM | DOGE | DOWN | 22 sec | +0.015% | 0¢ | ❌ Lost | $0.00 |
| 11/11 8:29:22 PM | PALLADIUM | UP | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 8:29:22 PM | ETH | DOWN | 37 sec | +0.038% | 0¢ | ❌ Lost | -$0.15 |
| 11/11 8:29:22 PM | USDCAD | UP | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 8:29:22 PM | ZEC | UP | 37 sec | -0.253% | 0¢ | ❌ Lost | $0.00 |
| 11/11 8:29:03 PM | BNB | DOWN | 57 sec | +0.007% | 1¢ | ❌ Lost | $0.00 |
| 11/11 8:29:03 PM | SOL | DOWN | 57 sec | +0.086% | 0¢ | ❌ Lost | -$0.15 |
| 11/11 8:29:03 PM | GBPUSD | DOWN | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 8:29:03 PM | HYPE | DOWN | 57 sec | +0.101% | 0¢ | ❌ Lost | $0.00 |
| 11/11 8:29:03 PM | EURUSD | DOWN | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 8:28:47 PM | BTC | DOWN | 73 sec | +0.136% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
