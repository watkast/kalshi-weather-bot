# 15-Minute 1¢ Study

*Updated Tue Nov 3, 1:57 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3540 finished bets | 1% | $122.30 | +31% | +3.45¢ | $69.05 / $53.25 |

*Expect about **98 buys a day** (~$14.72/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3273 | $49.60 | +14% |
| Volatility model ≥ 2%, hold to the close | 6558 | $45.75 | +6% |
| Momentum model ≥ 2%, hold to the close | 5406 | -$37.05 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 43553 | 43532 | 161 (0%) | 1.07% | -$3,047.45 (-57%) | Hold to the close: -$3,047.45 (-57%) |

*In play or awaiting result: 20. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 26908 | 4.7% | 0.4% (106) | -678% | ❌ Worse |
| Momentum model | 26908 | 4.6% | 0.4% (106) | -702% | ❌ Worse |
| Mean-reversion model | 26908 | 8.1% | 0.4% (106) | -825% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26908 | 106 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6558 | 60 | +6% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3540 | 37 | +31% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 2005 | 22 | +57% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 5406 | 42 | -6% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3273 | 29 | +14% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2137 | 19 | +24% | -74% | -73% | -69% |
| Mean-reversion model ≥ 2% | 11113 | 76 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7795 | 65 | -8% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 5209 | 46 | +0% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 27111 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10285 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6136 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 43532 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 161 | 0% | -$3,047.45 | -57% | — |
| Sell at 2¢ | 1718 | 4% | -$4,616.77 | -87% | 47 sec |
| Sell at 3¢ | 1178 | 3% | -$4,604.03 | -87% | 48 sec |
| Sell at 5¢ | 816 | 2% | -$4,505.05 | -85% | 63 sec |
| Sell at 10¢ | 491 | 1% | -$4,308.24 | -81% | 65 sec |
| Sell at 25¢ | 255 | 1% | -$3,995.40 | -75% | 82 sec |
| Sell at 50¢ | 166 | 0% | -$3,634.95 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2096 | 9 | 11% | 4% | -59% | -81% | -82% |
| 2–5 min | 13992 | 75 | 7% | 4% | -47% | -87% | -86% |
| 1–2 min | 10992 | 39 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 16441 | 38 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3038 | 13 | 5% | 3% | -45% | -88% | -87% |
| SOL | 3030 | 11 | 4% | 2% | -54% | -90% | -90% |
| BNB | 3026 | 17 | 5% | 2% | -30% | -85% | -84% |
| HYPE | 3025 | 9 | 5% | 2% | -63% | -89% | -87% |
| DOGE | 3011 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 3009 | 11 | 7% | 3% | -55% | -85% | -85% |
| BTC | 2994 | 14 | 5% | 2% | -37% | -88% | -89% |
| NEAR | 2993 | 15 | 5% | 2% | -35% | -83% | -84% |
| XRP | 2985 | 12 | 3% | 1% | -50% | -89% | -88% |
| GOLD | 1595 | 5 | 5% | 2% | -62% | -81% | -83% |
| SILVER | 1557 | 7 | 5% | 2% | -47% | -82% | -82% |
| WTI | 1554 | 4 | 3% | 1% | -69% | -92% | -93% |
| PLATINUM | 1385 | 3 | 2% | 1% | -80% | -96% | -96% |
| EURUSD | 1326 | 3 | 2% | 1% | -79% | -89% | -89% |
| COPPER | 1319 | 6 | 2% | 1% | -58% | -69% | -69% |
| NATGAS | 1269 | 7 | 2% | 1% | -49% | -82% | -81% |
| GBPUSD | 1255 | 2 | 2% | 1% | -85% | -96% | -96% |
| PALLADIUM | 1249 | 3 | 1% | 1% | -78% | -90% | -91% |
| USDJPY | 1234 | 5 | 2% | 1% | -62% | -97% | -96% |
| AUDUSD | 785 | 4 | 2% | 1% | -52% | -85% | -84% |
| USDCAD | 749 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 357 | 0 | 1% | 1% | -100% | -98% | -96% |
| 10YRRATE | 213 | 1 | 5% | 2% | -56% | -47% | -45% |
| 30YRRATE | 202 | 0 | 1% | 0% | -100% | -97% | -96% |
| 2YRRATE | 194 | 2 | 4% | 1% | -4% | +3% | +4% |
| 5YRRATE | 178 | 1 | 6% | 2% | -48% | -90% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 22162 | 87 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 21370 | 74 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4405 | 21 | 2% | 1% | -17% | -82% | -82% |
| 0.05–0.1% | 4642 | 18 | 3% | 2% | -42% | -91% | -90% |
| 0.1–0.2% | 7028 | 24 | 4% | 2% | -57% | -90% | -90% |
| 0.2–0.5% | 8032 | 33 | 7% | 3% | -54% | -86% | -86% |
| Over 0.5% | 2998 | 12 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10786 | 37 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 10804 | 48 | 4% | 2% | -49% | -85% | -85% |
| Afternoon (12–6pm) | 10198 | 38 | 4% | 2% | -56% | -85% | -85% |
| Evening (6pm–12am) | 11744 | 38 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,762 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/3 1:57:20 AM | NATGAS | DOWN | 2.6 min | — | — | In play | — |
| 11/3 1:57:04 AM | SILVER | UP | 2.9 min | — | — | In play | — |
| 11/3 1:57:04 AM | BTC | DOWN | 2.9 min | +0.101% | — | In play | — |
| 11/3 1:56:48 AM | GOLD | UP | 3.2 min | — | — | In play | — |
| 11/3 1:55:42 AM | BNB | DOWN | 4.3 min | +0.075% | — | In play | — |
| 11/3 1:55:42 AM | ETH | DOWN | 4.3 min | +0.197% | — | In play | — |
| 11/3 1:55:42 AM | DOGE | DOWN | 4.3 min | +0.232% | — | In play | — |
| 11/3 1:55:26 AM | SOL | DOWN | 4.6 min | +0.288% | — | In play | — |
| 11/3 1:55:26 AM | NEAR | DOWN | 4.6 min | +0.472% | — | In play | — |
| 11/3 1:54:38 AM | HYPE | DOWN | 5.4 min | +0.382% | — | In play | — |
| 11/3 1:53:51 AM | COPPER | UP | 6.1 min | — | — | In play | — |
| 11/3 1:44:48 AM | 30YRRATE | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 1:44:48 AM | GBPUSD | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 1:44:48 AM | USDCAD | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 1:44:32 AM | SOL | UP | 28 sec | -0.117% | 0¢ | ❌ Lost | $0.00 |
| 11/3 1:44:16 AM | NEAR | DOWN | 44 sec | +0.190% | 0¢ | ❌ Lost | $0.00 |
| 11/3 1:44:01 AM | HYPE | DOWN | 58 sec | +0.114% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 1:44:01 AM | PALLADIUM | UP | 58 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 1:43:44 AM | WTI | DOWN | 76 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/3 1:43:28 AM | BRENT | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 1:43:28 AM | BNB | DOWN | 1.5 min | +0.017% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 1:43:28 AM | DOGE | UP | 1.5 min | -0.152% | 3¢ | ❌ Lost | -$0.15 |
| 11/3 1:43:28 AM | GOLD | UP | 1.5 min | — | 0¢ | ❌ Lost | $0.00 |
| 11/3 1:42:41 AM | ZEC | UP | 2.3 min | -0.416% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 1:42:41 AM | ETH | UP | 2.3 min | -0.178% | 0¢ | ❌ Lost | $0.00 |
| 11/3 1:42:09 AM | AUDUSD | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 1:41:53 AM | BTC | UP | 3.1 min | -0.170% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 1:41:53 AM | SILVER | UP | 3.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 1:41:21 AM | NATGAS | DOWN | 3.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 1:41:21 AM | PLATINUM | UP | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
