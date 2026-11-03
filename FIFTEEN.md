# 15-Minute 1¢ Study

*Updated Tue Nov 3, 2:59 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3549 finished bets | 1% | $121.10 | +31% | +3.41¢ | $68.60 / $52.50 |

*Expect about **98 buys a day** (~$14.74/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3281 | $48.55 | +14% |
| Volatility model ≥ 2%, hold to the close | 6570 | $44.10 | +6% |
| Momentum model ≥ 2%, hold to the close | 5416 | -$38.40 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 43635 | 43612 | 161 (0%) | 1.07% | -$3,058.10 (-58%) | Hold to the close: -$3,058.10 (-58%) |

*In play or awaiting result: 22. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 26944 | 4.7% | 0.4% (106) | -679% | ❌ Worse |
| Momentum model | 26944 | 4.6% | 0.4% (106) | -703% | ❌ Worse |
| Mean-reversion model | 26944 | 8.1% | 0.4% (106) | -827% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26944 | 106 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6570 | 60 | +6% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3549 | 37 | +31% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2013 | 22 | +56% | -70% | -69% | -65% |
| Momentum model ≥ 2% | 5416 | 42 | -6% | -81% | -81% | -77% |
| Momentum model ≥ 5% | 3281 | 29 | +14% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2143 | 19 | +24% | -74% | -73% | -69% |
| Mean-reversion model ≥ 2% | 11139 | 76 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7815 | 65 | -8% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 5224 | 46 | -0% | -80% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 27147 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10305 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6160 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 43612 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 161 | 0% | -$3,058.10 | -58% | — |
| Sell at 2¢ | 1720 | 4% | -$4,626.90 | -87% | 47 sec |
| Sell at 3¢ | 1179 | 3% | -$4,614.29 | -87% | 48 sec |
| Sell at 5¢ | 816 | 2% | -$4,515.70 | -85% | 63 sec |
| Sell at 10¢ | 491 | 1% | -$4,318.89 | -81% | 65 sec |
| Sell at 25¢ | 255 | 1% | -$4,006.05 | -75% | 82 sec |
| Sell at 50¢ | 166 | 0% | -$3,645.60 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2100 | 9 | 11% | 4% | -59% | -81% | -82% |
| 2–5 min | 14018 | 75 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 11019 | 39 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 16464 | 38 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3042 | 13 | 5% | 3% | -45% | -88% | -87% |
| SOL | 3034 | 11 | 4% | 2% | -54% | -90% | -90% |
| BNB | 3030 | 17 | 5% | 2% | -30% | -85% | -84% |
| HYPE | 3029 | 9 | 5% | 2% | -63% | -89% | -87% |
| DOGE | 3015 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 3013 | 11 | 7% | 3% | -55% | -85% | -85% |
| BTC | 2998 | 14 | 5% | 2% | -37% | -88% | -89% |
| NEAR | 2997 | 15 | 5% | 2% | -35% | -83% | -84% |
| XRP | 2989 | 12 | 3% | 1% | -50% | -89% | -88% |
| GOLD | 1599 | 5 | 5% | 2% | -62% | -81% | -83% |
| SILVER | 1560 | 7 | 5% | 2% | -47% | -82% | -82% |
| WTI | 1556 | 4 | 3% | 1% | -69% | -92% | -94% |
| PLATINUM | 1387 | 3 | 2% | 1% | -80% | -96% | -96% |
| EURUSD | 1329 | 3 | 2% | 1% | -79% | -89% | -89% |
| COPPER | 1322 | 6 | 2% | 1% | -58% | -69% | -69% |
| NATGAS | 1272 | 7 | 2% | 1% | -49% | -82% | -81% |
| GBPUSD | 1258 | 2 | 2% | 1% | -85% | -96% | -96% |
| PALLADIUM | 1250 | 3 | 1% | 1% | -78% | -90% | -91% |
| USDJPY | 1238 | 5 | 2% | 1% | -62% | -97% | -96% |
| AUDUSD | 788 | 4 | 2% | 1% | -53% | -85% | -85% |
| USDCAD | 751 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 359 | 0 | 1% | 1% | -100% | -98% | -96% |
| 10YRRATE | 216 | 1 | 5% | 2% | -57% | -48% | -46% |
| 30YRRATE | 204 | 0 | 1% | 0% | -100% | -97% | -96% |
| 2YRRATE | 196 | 2 | 4% | 1% | -5% | +2% | +3% |
| 5YRRATE | 180 | 1 | 6% | 2% | -48% | -90% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 22179 | 87 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 21433 | 74 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4413 | 21 | 2% | 1% | -17% | -82% | -82% |
| 0.05–0.1% | 4649 | 18 | 3% | 2% | -42% | -91% | -90% |
| 0.1–0.2% | 7033 | 24 | 4% | 2% | -57% | -90% | -90% |
| 0.2–0.5% | 8043 | 33 | 7% | 3% | -54% | -86% | -86% |
| Over 0.5% | 3003 | 12 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10866 | 37 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 10804 | 48 | 4% | 2% | -49% | -85% | -85% |
| Afternoon (12–6pm) | 10198 | 38 | 4% | 2% | -56% | -85% | -85% |
| Evening (6pm–12am) | 11744 | 38 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,760 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/3 2:59:01 AM | GBPUSD | DOWN | 58 sec | — | — | In play | — |
| 11/3 2:59:01 AM | USDJPY | UP | 58 sec | — | — | In play | — |
| 11/3 2:58:44 AM | WTI | UP | 76 sec | — | — | In play | — |
| 11/3 2:58:44 AM | SILVER | DOWN | 76 sec | — | — | In play | — |
| 11/3 2:58:28 AM | ZEC | DOWN | 1.5 min | +0.224% | — | In play | — |
| 11/3 2:58:28 AM | NEAR | DOWN | 1.5 min | +0.220% | — | In play | — |
| 11/3 2:58:12 AM | USDCAD | DOWN | 1.8 min | — | — | In play | — |
| 11/3 2:57:57 AM | BNB | DOWN | 2.0 min | +0.020% | — | In play | — |
| 11/3 2:57:57 AM | BRENT | UP | 2.0 min | — | — | In play | — |
| 11/3 2:57:40 AM | AUDUSD | DOWN | 2.3 min | — | — | In play | — |
| 11/3 2:57:40 AM | COPPER | DOWN | 2.3 min | — | — | In play | — |
| 11/3 2:56:53 AM | HYPE | DOWN | 3.1 min | +0.199% | — | In play | — |
| 11/3 2:56:53 AM | EURUSD | DOWN | 3.1 min | — | — | In play | — |
| 11/3 2:44:32 AM | NATGAS | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 2:44:16 AM | WTI | UP | 44 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/3 2:44:16 AM | USDJPY | DOWN | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 2:44:16 AM | DOGE | DOWN | 44 sec | -0.007% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 2:44:16 AM | EURUSD | UP | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 2:44:16 AM | SILVER | DOWN | 44 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/3 2:44:16 AM | BRENT | UP | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 2:43:46 AM | HYPE | DOWN | 74 sec | +0.053% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 2:43:46 AM | SOL | DOWN | 74 sec | +0.098% | 0¢ | ❌ Lost | $0.00 |
| 11/3 2:43:46 AM | PALLADIUM | DOWN | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 2:43:14 AM | BNB | DOWN | 1.8 min | +0.014% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 2:42:58 AM | XRP | DOWN | 2.0 min | +0.080% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 2:42:58 AM | PLATINUM | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 2:42:43 AM | AUDUSD | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 2:42:11 AM | GOLD | DOWN | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 2:41:23 AM | ETH | DOWN | 3.6 min | +0.187% | 3¢ | ❌ Lost | -$0.15 |
| 11/3 2:41:23 AM | BTC | DOWN | 3.6 min | +0.219% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
