# 15-Minute 1¢ Study

*Updated Tue Nov 3, 10:15 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3565 finished bets | 1% | $119.45 | +30% | +3.35¢ | $68.00 / $51.45 |

*Expect about **98 buys a day** (~$14.67/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3297 | $47.05 | +13% |
| Volatility model ≥ 2%, hold to the close | 6593 | $42.15 | +5% |
| Momentum model ≥ 2%, hold to the close | 5434 | -$39.90 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 43903 | 43879 | 164 (0%) | 1.07% | -$3,046.85 (-57%) | Hold to the close: -$3,046.85 (-57%) |

*In play or awaiting result: 23. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 27059 | 4.7% | 0.4% (106) | -682% | ❌ Worse |
| Momentum model | 27059 | 4.6% | 0.4% (106) | -706% | ❌ Worse |
| Mean-reversion model | 27059 | 8.1% | 0.4% (106) | -830% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 27059 | 106 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6593 | 60 | +5% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3565 | 37 | +30% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2023 | 22 | +55% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5434 | 42 | -6% | -81% | -81% | -77% |
| Momentum model ≥ 5% | 3297 | 29 | +13% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2153 | 19 | +23% | -74% | -73% | -69% |
| Mean-reversion model ≥ 2% | 11193 | 76 | -26% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7853 | 65 | -8% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 5254 | 46 | -1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 27263 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10369 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6247 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 43879 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 164 | 0% | -$3,046.85 | -57% | — |
| Sell at 2¢ | 1732 | 4% | -$4,654.53 | -87% | 47 sec |
| Sell at 3¢ | 1188 | 3% | -$4,641.53 | -87% | 49 sec |
| Sell at 5¢ | 825 | 2% | -$4,540.60 | -85% | 63 sec |
| Sell at 10¢ | 497 | 1% | -$4,341.78 | -81% | 66 sec |
| Sell at 25¢ | 261 | 1% | -$4,016.94 | -75% | 83 sec |
| Sell at 50¢ | 168 | 0% | -$3,648.85 | -68% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2117 | 9 | 11% | 4% | -60% | -81% | -82% |
| 2–5 min | 14092 | 78 | 7% | 4% | -45% | -86% | -86% |
| 1–2 min | 11094 | 39 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 16565 | 38 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3054 | 13 | 5% | 3% | -45% | -88% | -88% |
| SOL | 3048 | 11 | 4% | 2% | -54% | -91% | -90% |
| BNB | 3043 | 17 | 5% | 2% | -30% | -85% | -84% |
| HYPE | 3041 | 9 | 5% | 2% | -63% | -89% | -87% |
| DOGE | 3028 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 3024 | 11 | 7% | 3% | -56% | -85% | -85% |
| NEAR | 3011 | 15 | 5% | 2% | -35% | -84% | -84% |
| BTC | 3011 | 14 | 5% | 2% | -37% | -88% | -89% |
| XRP | 3003 | 12 | 3% | 1% | -50% | -89% | -88% |
| GOLD | 1609 | 5 | 5% | 2% | -62% | -81% | -83% |
| SILVER | 1569 | 7 | 5% | 2% | -47% | -82% | -82% |
| WTI | 1566 | 5 | 3% | 1% | -61% | -92% | -93% |
| PLATINUM | 1398 | 4 | 2% | 1% | -73% | -96% | -96% |
| EURUSD | 1340 | 3 | 2% | 1% | -79% | -89% | -89% |
| COPPER | 1326 | 6 | 2% | 1% | -58% | -69% | -69% |
| NATGAS | 1277 | 7 | 2% | 1% | -49% | -82% | -81% |
| GBPUSD | 1269 | 3 | 2% | 1% | -78% | -96% | -96% |
| PALLADIUM | 1257 | 3 | 1% | 1% | -78% | -90% | -91% |
| USDJPY | 1245 | 5 | 2% | 1% | -63% | -97% | -96% |
| AUDUSD | 800 | 4 | 2% | 1% | -53% | -86% | -85% |
| USDCAD | 761 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 367 | 0 | 1% | 1% | -100% | -98% | -96% |
| 10YRRATE | 227 | 1 | 5% | 2% | -59% | -50% | -49% |
| 30YRRATE | 213 | 0 | 1% | 0% | -100% | -98% | -96% |
| 2YRRATE | 204 | 2 | 4% | 0% | -8% | -2% | -1% |
| 5YRRATE | 188 | 1 | 5% | 2% | -50% | -91% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 22298 | 88 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 21581 | 76 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4438 | 21 | 2% | 1% | -18% | -83% | -82% |
| 0.05–0.1% | 4666 | 18 | 3% | 2% | -42% | -91% | -90% |
| 0.1–0.2% | 7057 | 24 | 4% | 2% | -58% | -90% | -90% |
| 0.2–0.5% | 8080 | 33 | 7% | 3% | -55% | -86% | -86% |
| Over 0.5% | 3015 | 12 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11048 | 40 | 4% | 2% | -59% | -87% | -87% |
| Morning (6am–12pm) | 10889 | 48 | 4% | 2% | -50% | -85% | -85% |
| Afternoon (12–6pm) | 10198 | 38 | 4% | 2% | -56% | -85% | -85% |
| Evening (6pm–12am) | 11744 | 38 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,735 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/3 10:14:54 AM | SOL | DOWN | 5 sec | +0.042% | 0¢ | ❌ Lost | $0.00 |
| 11/3 10:14:54 AM | 5YRRATE | DOWN | 5 sec | — | 0¢ | In play | — |
| 11/3 10:14:54 AM | BTC | DOWN | 5 sec | +0.011% | 0¢ | ❌ Lost | $0.00 |
| 11/3 10:14:38 AM | PLATINUM | DOWN | 21 sec | — | 0¢ | In play | — |
| 11/3 10:14:38 AM | USDCAD | UP | 21 sec | — | 0¢ | In play | — |
| 11/3 10:14:38 AM | ETH | DOWN | 21 sec | +0.067% | 0¢ | In play | — |
| 11/3 10:14:38 AM | AUDUSD | DOWN | 21 sec | — | 0¢ | In play | — |
| 11/3 10:14:38 AM | GOLD | DOWN | 21 sec | — | 0¢ | In play | — |
| 11/3 10:14:23 AM | NEAR | DOWN | 37 sec | +0.039% | 0¢ | ❌ Lost | $0.00 |
| 11/3 10:14:23 AM | ZEC | DOWN | 37 sec | +0.206% | 0¢ | In play | — |
| 11/3 10:14:23 AM | BNB | DOWN | 37 sec | +0.004% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 10:14:23 AM | DOGE | DOWN | 37 sec | +0.025% | 0¢ | ❌ Lost | $0.00 |
| 11/3 10:14:23 AM | BRENT | UP | 37 sec | — | 0¢ | In play | — |
| 11/3 10:14:05 AM | COPPER | UP | 54 sec | — | 0¢ | In play | — |
| 11/3 10:13:33 AM | NATGAS | UP | 86 sec | — | 1¢ | In play | — |
| 11/3 10:13:33 AM | HYPE | UP | 86 sec | -0.223% | 0¢ | In play | — |
| 11/3 10:13:33 AM | 2YRRATE | DOWN | 86 sec | — | 0¢ | In play | — |
| 11/3 10:13:16 AM | GBPUSD | DOWN | 1.7 min | — | 0¢ | In play | — |
| 11/3 10:12:24 AM | XRP | DOWN | 2.6 min | +0.188% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 10:12:09 AM | WTI | UP | 2.8 min | — | 2¢ | In play | — |
| 11/3 9:59:54 AM | 2YRRATE | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 9:59:38 AM | AUDUSD | DOWN | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 9:59:21 AM | NATGAS | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 9:59:21 AM | GBPUSD | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 9:59:21 AM | 5YRRATE | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 9:59:03 AM | PLATINUM | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 9:58:31 AM | 10YRRATE | DOWN | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 9:58:14 AM | PALLADIUM | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 9:57:55 AM | GOLD | UP | 2.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 9:57:23 AM | BNB | DOWN | 2.6 min | +0.129% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
