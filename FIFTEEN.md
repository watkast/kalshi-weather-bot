# 15-Minute 1¢ Study

*Updated Tue Nov 3, 4:42 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3561 finished bets | 1% | $119.75 | +30% | +3.36¢ | $68.15 / $51.60 |

*Expect about **98 buys a day** (~$14.75/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3295 | $47.20 | +13% |
| Volatility model ≥ 2%, hold to the close | 6585 | $42.60 | +5% |
| Momentum model ≥ 2%, hold to the close | 5431 | -$39.75 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 43769 | 43752 | 162 (0%) | 1.07% | -$3,060.15 (-57%) | Hold to the close: -$3,060.15 (-57%) |

*In play or awaiting result: 16. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 27004 | 4.7% | 0.4% (106) | -683% | ❌ Worse |
| Momentum model | 27004 | 4.6% | 0.4% (106) | -707% | ❌ Worse |
| Mean-reversion model | 27004 | 8.1% | 0.4% (106) | -830% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 27004 | 106 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6585 | 60 | +5% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3561 | 37 | +30% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2021 | 22 | +55% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5431 | 42 | -6% | -81% | -81% | -77% |
| Momentum model ≥ 5% | 3295 | 29 | +13% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2152 | 19 | +23% | -74% | -73% | -69% |
| Mean-reversion model ≥ 2% | 11162 | 76 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7830 | 65 | -8% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 5238 | 46 | -0% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 27207 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10340 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6205 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 43752 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 162 | 0% | -$3,060.15 | -57% | — |
| Sell at 2¢ | 1724 | 4% | -$4,641.91 | -87% | 47 sec |
| Sell at 3¢ | 1182 | 3% | -$4,629.17 | -87% | 48 sec |
| Sell at 5¢ | 819 | 2% | -$4,529.80 | -85% | 63 sec |
| Sell at 10¢ | 492 | 1% | -$4,333.63 | -81% | 65 sec |
| Sell at 25¢ | 256 | 1% | -$4,018.79 | -75% | 82 sec |
| Sell at 50¢ | 167 | 0% | -$3,654.90 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2104 | 9 | 11% | 4% | -59% | -81% | -82% |
| 2–5 min | 14055 | 76 | 7% | 4% | -47% | -87% | -86% |
| 1–2 min | 11062 | 39 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 16520 | 38 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3049 | 13 | 5% | 3% | -45% | -88% | -88% |
| SOL | 3041 | 11 | 4% | 2% | -54% | -91% | -90% |
| BNB | 3037 | 17 | 5% | 2% | -30% | -85% | -84% |
| HYPE | 3034 | 9 | 5% | 2% | -63% | -89% | -87% |
| DOGE | 3022 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 3019 | 11 | 7% | 3% | -56% | -85% | -85% |
| BTC | 3005 | 14 | 5% | 2% | -37% | -88% | -89% |
| NEAR | 3004 | 15 | 5% | 2% | -35% | -84% | -84% |
| XRP | 2996 | 12 | 3% | 1% | -50% | -89% | -88% |
| GOLD | 1604 | 5 | 5% | 2% | -62% | -81% | -83% |
| SILVER | 1564 | 7 | 5% | 2% | -47% | -82% | -82% |
| WTI | 1562 | 4 | 3% | 1% | -69% | -92% | -93% |
| PLATINUM | 1393 | 3 | 2% | 1% | -80% | -96% | -96% |
| EURUSD | 1335 | 3 | 2% | 1% | -79% | -89% | -89% |
| COPPER | 1325 | 6 | 2% | 1% | -58% | -69% | -69% |
| NATGAS | 1274 | 7 | 2% | 1% | -49% | -82% | -81% |
| GBPUSD | 1264 | 3 | 2% | 1% | -78% | -96% | -96% |
| PALLADIUM | 1253 | 3 | 1% | 1% | -78% | -90% | -91% |
| USDJPY | 1243 | 5 | 2% | 1% | -62% | -97% | -96% |
| AUDUSD | 793 | 4 | 2% | 1% | -53% | -85% | -85% |
| USDCAD | 757 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 365 | 0 | 1% | 1% | -100% | -98% | -96% |
| 10YRRATE | 222 | 1 | 5% | 2% | -58% | -49% | -47% |
| 30YRRATE | 208 | 0 | 1% | 0% | -100% | -98% | -96% |
| 2YRRATE | 200 | 2 | 4% | 0% | -7% | +0% | +1% |
| 5YRRATE | 183 | 1 | 5% | 2% | -49% | -91% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 22235 | 87 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 21517 | 75 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4428 | 21 | 2% | 1% | -17% | -83% | -82% |
| 0.05–0.1% | 4663 | 18 | 3% | 2% | -42% | -91% | -90% |
| 0.1–0.2% | 7048 | 24 | 4% | 2% | -57% | -90% | -90% |
| 0.2–0.5% | 8056 | 33 | 7% | 3% | -55% | -86% | -86% |
| Over 0.5% | 3006 | 12 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11006 | 38 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 10804 | 48 | 4% | 2% | -49% | -85% | -85% |
| Afternoon (12–6pm) | 10198 | 38 | 4% | 2% | -56% | -85% | -85% |
| Evening (6pm–12am) | 11744 | 38 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,744 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/3 4:42:27 AM | SILVER | DOWN | 2.5 min | — | — | In play | — |
| 11/3 4:40:51 AM | BTC | UP | 4.2 min | -0.158% | — | In play | — |
| 11/3 4:40:19 AM | DOGE | UP | 4.7 min | -0.224% | — | In play | — |
| 11/3 4:40:19 AM | USDCAD | UP | 4.7 min | — | — | In play | — |
| 11/3 4:39:47 AM | BNB | UP | 5.2 min | -0.209% | — | In play | — |
| 11/3 4:39:31 AM | AUDUSD | DOWN | 5.5 min | — | — | In play | — |
| 11/3 4:39:15 AM | ETH | UP | 5.8 min | -0.210% | — | In play | — |
| 11/3 4:29:46 AM | USDCAD | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 4:29:30 AM | COPPER | UP | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 4:29:14 AM | BTC | UP | 45 sec | -0.061% | 0¢ | ❌ Lost | $0.00 |
| 11/3 4:29:14 AM | ZEC | DOWN | 45 sec | +0.180% | 0¢ | ❌ Lost | $0.00 |
| 11/3 4:29:14 AM | NEAR | UP | 45 sec | -0.223% | 0¢ | ❌ Lost | $0.00 |
| 11/3 4:28:58 AM | DOGE | UP | 62 sec | -0.138% | 0¢ | ❌ Lost | $0.00 |
| 11/3 4:28:58 AM | 5YRRATE | DOWN | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 4:28:58 AM | BRENT | DOWN | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 4:28:58 AM | PALLADIUM | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 4:28:42 AM | BNB | UP | 77 sec | -0.082% | 0¢ | ❌ Lost | $0.00 |
| 11/3 4:28:42 AM | HYPE | UP | 77 sec | -0.181% | 0¢ | ❌ Lost | -$0.15 |
| 11/3 4:28:42 AM | SOL | UP | 77 sec | -0.125% | 0¢ | ❌ Lost | $0.00 |
| 11/3 4:28:42 AM | ETH | UP | 77 sec | -0.086% | 0¢ | ❌ Lost | $0.00 |
| 11/3 4:28:42 AM | 2YRRATE | DOWN | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 4:28:10 AM | 10YRRATE | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 4:28:10 AM | WTI | DOWN | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 4:28:10 AM | 30YRRATE | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 4:28:10 AM | EURUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 4:27:54 AM | GBPUSD | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 4:26:17 AM | USDJPY | DOWN | 3.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 4:26:01 AM | GOLD | UP | 4.0 min | — | 3¢ | ❌ Lost | -$0.15 |
| 11/3 4:25:14 AM | PLATINUM | UP | 4.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 4:25:14 AM | SILVER | UP | 4.8 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
