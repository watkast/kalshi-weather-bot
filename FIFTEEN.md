# 15-Minute 1¢ Study

*Updated Thu Nov 12, 11:23 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4270 finished bets | 1% | $170.00 | +36% | +3.98¢ | $81.70 / $88.30 |

*Expect about **93 buys a day** (~$13.93/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4010 | $97.15 | +22% |
| Volatility model ≥ 2%, hold to the close | 7880 | $31.55 | +3% |
| Momentum model ≥ 2%, hold to the close | 6540 | -$23.50 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 55645 | 55621 | 212 (0%) | 1.07% | -$3,818.45 (-56%) | Hold to the close: -$3,818.45 (-56%) |

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
| Volatility model | 33233 | 4.7% | 0.4% (133) | -670% | ❌ Worse |
| Momentum model | 33233 | 4.6% | 0.4% (133) | -697% | ❌ Worse |
| Mean-reversion model | 33233 | 8.0% | 0.4% (133) | -812% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 33233 | 133 | -49% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7880 | 70 | +3% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4270 | 46 | +36% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2471 | 28 | +63% | -62% | -61% | -58% |
| Momentum model ≥ 2% | 6540 | 52 | -3% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 4010 | 38 | +22% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2629 | 25 | +34% | -66% | -65% | -61% |
| Mean-reversion model ≥ 2% | 13690 | 93 | -26% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9553 | 79 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6368 | 56 | -0% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 33438 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 13404 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8779 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 55621 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 212 | 0% | -$3,818.45 | -56% | — |
| Sell at 2¢ | 2221 | 4% | -$5,914.99 | -87% | 47 sec |
| Sell at 3¢ | 1509 | 3% | -$5,903.94 | -87% | 49 sec |
| Sell at 5¢ | 1037 | 2% | -$5,790.40 | -85% | 63 sec |
| Sell at 10¢ | 629 | 1% | -$5,556.46 | -82% | 65 sec |
| Sell at 25¢ | 330 | 1% | -$5,162.15 | -76% | 82 sec |
| Sell at 50¢ | 217 | 0% | -$4,677.70 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2763 | 13 | 11% | 4% | -55% | -81% | -82% |
| 2–5 min | 17951 | 97 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 14018 | 46 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 20876 | 56 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3743 | 17 | 5% | 3% | -41% | -88% | -87% |
| SOL | 3738 | 16 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3733 | 11 | 5% | 2% | -63% | -89% | -88% |
| BNB | 3721 | 19 | 5% | 2% | -36% | -86% | -85% |
| DOGE | 3719 | 8 | 4% | 2% | -73% | -90% | -90% |
| ETH | 3714 | 16 | 7% | 3% | -46% | -82% | -81% |
| BTC | 3696 | 18 | 5% | 2% | -33% | -87% | -88% |
| NEAR | 3694 | 17 | 5% | 2% | -40% | -85% | -85% |
| XRP | 3680 | 13 | 3% | 1% | -56% | -89% | -89% |
| GOLD | 2015 | 5 | 5% | 2% | -70% | -82% | -84% |
| WTI | 1994 | 7 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 1954 | 9 | 5% | 2% | -45% | -83% | -83% |
| PLATINUM | 1782 | 4 | 3% | 1% | -79% | -96% | -95% |
| EURUSD | 1729 | 6 | 3% | 1% | -68% | -90% | -89% |
| COPPER | 1672 | 6 | 2% | 1% | -67% | -74% | -74% |
| GBPUSD | 1655 | 6 | 2% | 1% | -66% | -96% | -96% |
| NATGAS | 1645 | 9 | 2% | 1% | -49% | -74% | -73% |
| USDJPY | 1622 | 6 | 2% | 1% | -65% | -96% | -96% |
| PALLADIUM | 1597 | 4 | 1% | 1% | -77% | -92% | -92% |
| AUDUSD | 1174 | 6 | 2% | 1% | -52% | -89% | -89% |
| USDCAD | 1137 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 745 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 375 | 2 | 4% | 2% | -50% | -68% | -66% |
| 2YRRATE | 360 | 4 | 4% | 2% | +4% | -41% | -40% |
| 30YRRATE | 356 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 330 | 2 | 4% | 2% | -43% | -93% | -94% |
| INX | 41 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 28285 | 110 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 27336 | 102 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5253 | 25 | 2% | 1% | -16% | -77% | -77% |
| 0.05–0.1% | 5654 | 20 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 8547 | 31 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 10114 | 41 | 6% | 3% | -55% | -87% | -86% |
| Over 0.5% | 3862 | 18 | 7% | 3% | -52% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13478 | 44 | 4% | 2% | -63% | -88% | -88% |
| Morning (6am–12pm) | 13343 | 62 | 4% | 2% | -47% | -85% | -84% |
| Afternoon (12–6pm) | 13453 | 59 | 4% | 2% | -49% | -86% | -87% |
| Evening (6pm–12am) | 15347 | 47 | 4% | 2% | -65% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,831 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/12 11:23:32 PM | ZEC | DOWN | 6.5 min | +1.770% | — | In play | — |
| 11/12 11:23:32 PM | NEAR | DOWN | 6.5 min | +1.682% | — | In play | — |
| 11/12 11:23:32 PM | XRP | DOWN | 6.5 min | +0.838% | — | In play | — |
| 11/12 11:14:55 PM | USDCAD | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 11:14:55 PM | SILVER | UP | 5 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/12 11:14:55 PM | EURUSD | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 11:14:39 PM | GBPUSD | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 11:14:23 PM | AUDUSD | UP | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 11:14:23 PM | XRP | DOWN | 37 sec | +0.089% | 0¢ | ❌ Lost | $0.00 |
| 11/12 11:14:07 PM | BNB | DOWN | 53 sec | +0.120% | 0¢ | ❌ Lost | -$0.15 |
| 11/12 11:14:07 PM | PALLADIUM | UP | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 11:13:52 PM | BTC | DOWN | 68 sec | +0.220% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 11:13:52 PM | PLATINUM | UP | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 11:13:36 PM | ETH | DOWN | 84 sec | +0.207% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 11:13:36 PM | GOLD | UP | 84 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/12 11:13:36 PM | DOGE | DOWN | 84 sec | +0.267% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 11:12:54 PM | SOL | DOWN | 2.1 min | +0.282% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 11:11:50 PM | HYPE | UP | 3.1 min | -0.835% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 11:11:19 PM | NEAR | DOWN | 3.7 min | +1.073% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 11:11:03 PM | ZEC | DOWN | 3.9 min | +1.961% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 11:11:03 PM | USDJPY | DOWN | 3.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 11:10:47 PM | WTI | DOWN | 4.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/12 11:10:31 PM | BRENT | DOWN | 4.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 10:59:48 PM | HYPE | UP | 12 sec | -0.164% | 0¢ | ❌ Lost | $0.00 |
| 11/12 10:59:48 PM | EURUSD | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 10:59:48 PM | USDCAD | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 10:59:32 PM | DOGE | UP | 28 sec | -0.196% | 0¢ | ❌ Lost | $0.00 |
| 11/12 10:59:16 PM | SOL | UP | 44 sec | -0.394% | 0¢ | ❌ Lost | $0.00 |
| 11/12 10:59:16 PM | NATGAS | UP | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 10:59:00 PM | GOLD | UP | 60 sec | — | 1¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
