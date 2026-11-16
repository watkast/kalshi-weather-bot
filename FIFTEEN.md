# 15-Minute 1¢ Study

*Updated Mon Nov 16, 12:22 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4428 finished bets | 1% | $223.65 | +46% | +5.05¢ | $85.95 / $137.70 |

*Expect about **89 buys a day** (~$13.41/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4181 | $121.75 | +27% |
| Volatility model ≥ 2%, hold to the close | 8241 | $86.20 | +9% |
| Momentum model ≥ 2%, hold to the close | 6855 | $10.95 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 58736 | 58702 | 227 (0%) | 1.07% | -$3,961.40 (-55%) | Hold to the close: -$3,961.40 (-55%) |

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
| Volatility model | 35368 | 4.6% | 0.4% (148) | -634% | ❌ Worse |
| Momentum model | 35368 | 4.5% | 0.4% (148) | -659% | ❌ Worse |
| Mean-reversion model | 35368 | 7.9% | 0.4% (148) | -769% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 35368 | 148 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8241 | 77 | +9% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4428 | 51 | +46% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2546 | 30 | +70% | -63% | -61% | -57% |
| Momentum model ≥ 2% | 6855 | 57 | +1% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4181 | 41 | +27% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2722 | 26 | +35% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14476 | 103 | -22% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10071 | 85 | -6% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6678 | 61 | +4% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 35574 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 13905 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9223 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 58702 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 227 | 0% | -$3,961.40 | -55% | — |
| Sell at 2¢ | 2359 | 4% | -$6,232.06 | -87% | 47 sec |
| Sell at 3¢ | 1589 | 3% | -$6,225.69 | -87% | 48 sec |
| Sell at 5¢ | 1088 | 2% | -$6,110.20 | -86% | 62 sec |
| Sell at 10¢ | 665 | 1% | -$5,862.25 | -82% | 65 sec |
| Sell at 25¢ | 351 | 1% | -$5,445.59 | -76% | 80 sec |
| Sell at 50¢ | 234 | 0% | -$4,901.90 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2932 | 13 | 11% | 4% | -58% | -81% | -83% |
| 2–5 min | 18987 | 104 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 14793 | 51 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 21977 | 59 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3982 | 19 | 5% | 2% | -38% | -88% | -87% |
| SOL | 3976 | 18 | 4% | 2% | -42% | -86% | -86% |
| HYPE | 3969 | 12 | 4% | 2% | -62% | -89% | -88% |
| DOGE | 3961 | 11 | 4% | 2% | -65% | -90% | -89% |
| BNB | 3958 | 20 | 5% | 2% | -36% | -86% | -85% |
| ETH | 3949 | 17 | 6% | 3% | -46% | -82% | -82% |
| BTC | 3932 | 21 | 5% | 2% | -27% | -86% | -88% |
| NEAR | 3930 | 17 | 5% | 2% | -44% | -85% | -86% |
| XRP | 3917 | 15 | 3% | 2% | -52% | -89% | -88% |
| GOLD | 2080 | 5 | 5% | 2% | -71% | -82% | -84% |
| WTI | 2064 | 7 | 4% | 2% | -59% | -91% | -92% |
| SILVER | 2023 | 9 | 5% | 2% | -47% | -83% | -83% |
| PLATINUM | 1845 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1793 | 6 | 2% | 1% | -69% | -91% | -90% |
| COPPER | 1728 | 6 | 2% | 1% | -68% | -75% | -75% |
| GBPUSD | 1717 | 6 | 2% | 1% | -67% | -96% | -96% |
| NATGAS | 1702 | 9 | 2% | 1% | -51% | -75% | -74% |
| USDJPY | 1679 | 6 | 2% | 1% | -67% | -97% | -96% |
| PALLADIUM | 1655 | 4 | 1% | 0% | -77% | -92% | -93% |
| AUDUSD | 1238 | 6 | 2% | 1% | -55% | -89% | -89% |
| USDCAD | 1185 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 808 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 410 | 2 | 4% | 1% | -54% | -71% | -69% |
| 2YRRATE | 395 | 4 | 4% | 2% | -5% | -46% | -45% |
| 30YRRATE | 382 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 367 | 2 | 4% | 2% | -49% | -93% | -95% |
| INX | 57 | 0 | 2% | 0% | -100% | -97% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 29867 | 113 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 28835 | 114 | 4% | 2% | -55% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5400 | 25 | 2% | 1% | -17% | -78% | -77% |
| 0.05–0.1% | 5842 | 24 | 3% | 2% | -36% | -91% | -91% |
| 0.1–0.2% | 8935 | 34 | 5% | 2% | -51% | -89% | -89% |
| 0.2–0.5% | 10973 | 48 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4415 | 19 | 7% | 3% | -55% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14411 | 45 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13940 | 70 | 4% | 2% | -43% | -85% | -84% |
| Afternoon (12–6pm) | 14294 | 63 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 16057 | 49 | 4% | 2% | -65% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,081 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/16 12:14:59 PM | 10YRRATE | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:14:59 PM | NATGAS | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:14:59 PM | USDJPY | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:14:43 PM | EURUSD | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:14:43 PM | AUDUSD | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:14:43 PM | 5YRRATE | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:14:27 PM | GBPUSD | DOWN | 33 sec | — | 3¢ | ❌ Lost | -$0.15 |
| 11/16 12:14:27 PM | HYPE | UP | 33 sec | -0.125% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:14:27 PM | COPPER | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:14:27 PM | 30YRRATE | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:14:11 PM | GOLD | DOWN | 49 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/16 12:14:11 PM | SILVER | DOWN | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:13:40 PM | PLATINUM | DOWN | 80 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:13:08 PM | INX | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:13:08 PM | BTC | UP | 1.9 min | -0.164% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 12:12:52 PM | BNB | UP | 2.1 min | -0.205% | 1¢ | ❌ Lost | $0.00 |
| 11/16 12:12:52 PM | ZEC | UP | 2.1 min | -0.508% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:11:26 PM | ETH | UP | 3.5 min | -0.332% | 2¢ | ❌ Lost | -$0.15 |
| 11/16 12:11:26 PM | NEAR | UP | 3.5 min | -0.558% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 12:11:26 PM | DOGE | UP | 3.5 min | -0.367% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 12:11:10 PM | SOL | UP | 3.8 min | -0.396% | 2¢ | ❌ Lost | -$0.15 |
| 11/16 12:10:54 PM | XRP | UP | 4.1 min | -0.469% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 11:59:45 AM | USDJPY | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 11:59:29 AM | DOGE | DOWN | 30 sec | +0.115% | 0¢ | ❌ Lost | $0.00 |
| 11/16 11:59:13 AM | NATGAS | DOWN | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 11:58:56 AM | XRP | DOWN | 63 sec | +0.146% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 11:58:24 AM | AUDUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 11:58:08 AM | PALLADIUM | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 11:58:08 AM | BTC | DOWN | 1.9 min | +0.169% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 11:57:51 AM | COPPER | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
