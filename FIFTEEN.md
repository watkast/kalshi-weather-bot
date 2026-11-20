# 15-Minute 1¢ Study

*Updated Thu Nov 19, 5:32 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4579 finished bets | 1% | $210.15 | +42% | +4.59¢ | $77.25 / $132.90 |

*Expect about **87 buys a day** (~$13.03/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4318 | $110.05 | +24% |
| Volatility model ≥ 2%, hold to the close | 8546 | $65.85 | +6% |
| Momentum model ≥ 2%, hold to the close | 7092 | -$14.25 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 62360 | 62326 | 241 (0%) | 1.07% | -$4,207.15 (-55%) | Hold to the close: -$4,207.15 (-55%) |

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
| Volatility model | 37015 | 4.5% | 0.4% (155) | -636% | ❌ Worse |
| Momentum model | 37015 | 4.4% | 0.4% (155) | -662% | ❌ Worse |
| Mean-reversion model | 37015 | 7.9% | 0.4% (155) | -772% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 37015 | 155 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8546 | 78 | +6% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4579 | 51 | +42% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 2635 | 30 | +66% | -63% | -62% | -58% |
| Momentum model ≥ 2% | 7092 | 57 | -2% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4318 | 41 | +24% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2817 | 26 | +32% | -67% | -66% | -62% |
| Mean-reversion model ≥ 2% | 15120 | 109 | -21% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10516 | 89 | -6% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6991 | 64 | +4% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 37221 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14923 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10182 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 62326 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 241 | 0% | -$4,207.15 | -55% | — |
| Sell at 2¢ | 2528 | 4% | -$6,629.87 | -87% | 47 sec |
| Sell at 3¢ | 1706 | 3% | -$6,621.81 | -87% | 48 sec |
| Sell at 5¢ | 1167 | 2% | -$6,500.60 | -86% | 63 sec |
| Sell at 10¢ | 714 | 1% | -$6,239.81 | -82% | 65 sec |
| Sell at 25¢ | 382 | 1% | -$5,756.73 | -76% | 80 sec |
| Sell at 50¢ | 248 | 0% | -$5,207.15 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3189 | 17 | 11% | 4% | -49% | -81% | -82% |
| 2–5 min | 20196 | 109 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 15596 | 52 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 23332 | 63 | 1% | 0% | -61% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4162 | 19 | 5% | 2% | -40% | -88% | -87% |
| SOL | 4159 | 19 | 4% | 2% | -41% | -86% | -87% |
| HYPE | 4151 | 12 | 4% | 2% | -63% | -89% | -88% |
| DOGE | 4141 | 11 | 4% | 2% | -66% | -90% | -89% |
| BNB | 4140 | 21 | 5% | 2% | -36% | -85% | -85% |
| ETH | 4136 | 19 | 7% | 3% | -43% | -82% | -82% |
| BTC | 4118 | 22 | 5% | 2% | -27% | -86% | -88% |
| NEAR | 4115 | 18 | 5% | 2% | -43% | -85% | -86% |
| XRP | 4099 | 16 | 3% | 2% | -50% | -89% | -88% |
| GOLD | 2224 | 6 | 5% | 2% | -67% | -82% | -84% |
| WTI | 2203 | 7 | 4% | 1% | -61% | -91% | -92% |
| SILVER | 2164 | 9 | 5% | 2% | -50% | -83% | -83% |
| PLATINUM | 1971 | 5 | 3% | 1% | -76% | -95% | -95% |
| EURUSD | 1931 | 7 | 3% | 1% | -66% | -91% | -90% |
| GBPUSD | 1862 | 8 | 2% | 1% | -60% | -96% | -95% |
| COPPER | 1853 | 6 | 2% | 1% | -70% | -76% | -76% |
| USDJPY | 1814 | 6 | 2% | 1% | -69% | -96% | -96% |
| NATGAS | 1812 | 10 | 2% | 1% | -48% | -76% | -75% |
| PALLADIUM | 1770 | 4 | 1% | 0% | -79% | -93% | -93% |
| AUDUSD | 1366 | 6 | 2% | 1% | -59% | -90% | -90% |
| USDCAD | 1304 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 926 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 480 | 2 | 3% | 1% | -61% | -75% | -73% |
| 2YRRATE | 456 | 4 | 4% | 2% | -18% | -52% | -51% |
| 30YRRATE | 441 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 431 | 2 | 4% | 2% | -57% | -94% | -95% |
| INX | 97 | 1 | 2% | 1% | -4% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 31796 | 124 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 30530 | 117 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5549 | 25 | 2% | 1% | -19% | -78% | -78% |
| 0.05–0.1% | 6039 | 24 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 9330 | 34 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 11580 | 51 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 4714 | 23 | 7% | 3% | -49% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15189 | 47 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 14806 | 79 | 5% | 2% | -39% | -85% | -84% |
| Afternoon (12–6pm) | 15404 | 66 | 4% | 2% | -50% | -87% | -87% |
| Evening (6pm–12am) | 16927 | 49 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,003 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/19 5:29:50 PM | COPPER | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 5:29:34 PM | WTI | UP | 25 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/19 5:29:34 PM | BRENT | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 5:29:18 PM | BTC | DOWN | 41 sec | +0.069% | 0¢ | ❌ Lost | $0.00 |
| 11/19 5:29:18 PM | HYPE | UP | 41 sec | -0.430% | 0¢ | ❌ Lost | $0.00 |
| 11/19 5:29:07 PM | DOGE | UP | 52 sec | -0.203% | 0¢ | ❌ Lost | -$0.15 |
| 11/19 5:29:07 PM | BNB | UP | 52 sec | -0.165% | 0¢ | ❌ Lost | $0.00 |
| 11/19 5:29:07 PM | XRP | UP | 52 sec | -0.135% | 0¢ | ❌ Lost | -$0.15 |
| 11/19 5:28:51 PM | ETH | UP | 69 sec | -0.144% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 5:28:35 PM | SILVER | UP | 85 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/19 5:28:35 PM | SOL | UP | 85 sec | -0.192% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 5:28:19 PM | GOLD | UP | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/19 5:27:48 PM | AUDUSD | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 5:27:16 PM | ZEC | UP | 2.7 min | -0.469% | 0¢ | ❌ Lost | $0.00 |
| 11/19 5:27:00 PM | NEAR | UP | 3.0 min | -0.513% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 5:24:04 PM | USDJPY | UP | 5.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 5:14:31 PM | BTC | DOWN | 28 sec | +0.077% | 0¢ | ❌ Lost | $0.00 |
| 11/19 5:14:31 PM | USDCAD | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 5:14:31 PM | SOL | DOWN | 28 sec | +0.044% | 0¢ | ❌ Lost | -$0.15 |
| 11/19 5:14:14 PM | ETH | DOWN | 45 sec | +0.030% | 0¢ | ❌ Lost | -$0.15 |
| 11/19 5:14:14 PM | HYPE | DOWN | 45 sec | +0.165% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 5:14:14 PM | USDJPY | DOWN | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 5:13:58 PM | ZEC | DOWN | 61 sec | +0.152% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 5:13:42 PM | NEAR | DOWN | 77 sec | +0.118% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 5:12:54 PM | DOGE | DOWN | 2.1 min | +0.227% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 5:12:54 PM | BNB | DOWN | 2.1 min | +0.164% | 0¢ | ❌ Lost | $0.00 |
| 11/19 5:12:54 PM | GBPUSD | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 5:12:38 PM | WTI | DOWN | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/19 5:12:38 PM | AUDUSD | DOWN | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/19 5:12:38 PM | BRENT | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
