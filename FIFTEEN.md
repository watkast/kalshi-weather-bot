# 15-Minute 1¢ Study

*Updated Tue Nov 3, 12:13 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3532 finished bets | 1% | $123.50 | +31% | +3.50¢ | $69.50 / $54.00 |

*Expect about **98 buys a day** (~$14.71/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3265 | $50.80 | +14% |
| Volatility model ≥ 2%, hold to the close | 6543 | $47.85 | +6% |
| Momentum model ≥ 2%, hold to the close | 5396 | -$35.70 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 43413 | 43392 | 161 (0%) | 1.07% | -$3,029.45 (-57%) | Hold to the close: -$3,029.45 (-57%) |

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
| Volatility model | 26846 | 4.7% | 0.4% (106) | -677% | ❌ Worse |
| Momentum model | 26846 | 4.6% | 0.4% (106) | -701% | ❌ Worse |
| Mean-reversion model | 26846 | 8.1% | 0.4% (106) | -824% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26846 | 106 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6543 | 60 | +6% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3532 | 37 | +31% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2000 | 22 | +57% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 5396 | 42 | -6% | -81% | -81% | -77% |
| Momentum model ≥ 5% | 3265 | 29 | +14% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2133 | 19 | +25% | -74% | -73% | -69% |
| Mean-reversion model ≥ 2% | 11081 | 76 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7768 | 65 | -7% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 5191 | 46 | +1% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 27049 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10244 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6099 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 43392 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 161 | 0% | -$3,029.45 | -57% | — |
| Sell at 2¢ | 1713 | 4% | -$4,600.07 | -87% | 47 sec |
| Sell at 3¢ | 1175 | 3% | -$4,587.20 | -87% | 49 sec |
| Sell at 5¢ | 814 | 2% | -$4,488.35 | -85% | 63 sec |
| Sell at 10¢ | 490 | 1% | -$4,291.55 | -81% | 65 sec |
| Sell at 25¢ | 255 | 1% | -$3,977.40 | -75% | 82 sec |
| Sell at 50¢ | 166 | 0% | -$3,616.95 | -68% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2083 | 9 | 11% | 4% | -59% | -81% | -82% |
| 2–5 min | 13942 | 75 | 7% | 4% | -47% | -87% | -86% |
| 1–2 min | 10959 | 39 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 16397 | 38 | 1% | 0% | -67% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3031 | 13 | 5% | 3% | -45% | -88% | -87% |
| SOL | 3023 | 11 | 4% | 2% | -54% | -91% | -90% |
| BNB | 3020 | 17 | 5% | 2% | -30% | -85% | -84% |
| HYPE | 3018 | 9 | 5% | 2% | -63% | -89% | -87% |
| DOGE | 3004 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 3002 | 11 | 6% | 3% | -55% | -85% | -85% |
| BTC | 2987 | 14 | 5% | 2% | -37% | -88% | -89% |
| NEAR | 2986 | 15 | 5% | 2% | -35% | -83% | -84% |
| XRP | 2978 | 12 | 3% | 1% | -50% | -89% | -89% |
| GOLD | 1590 | 5 | 5% | 2% | -62% | -81% | -83% |
| SILVER | 1551 | 7 | 5% | 2% | -46% | -82% | -81% |
| WTI | 1547 | 4 | 3% | 1% | -69% | -92% | -93% |
| PLATINUM | 1381 | 3 | 2% | 1% | -80% | -96% | -96% |
| EURUSD | 1321 | 3 | 2% | 1% | -79% | -89% | -89% |
| COPPER | 1314 | 6 | 2% | 1% | -57% | -69% | -69% |
| NATGAS | 1265 | 7 | 2% | 1% | -48% | -82% | -81% |
| GBPUSD | 1251 | 2 | 2% | 1% | -85% | -96% | -96% |
| PALLADIUM | 1244 | 3 | 1% | 1% | -77% | -90% | -91% |
| USDJPY | 1231 | 5 | 2% | 1% | -62% | -97% | -96% |
| AUDUSD | 779 | 4 | 2% | 1% | -52% | -85% | -84% |
| USDCAD | 742 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 352 | 0 | 1% | 1% | -100% | -98% | -96% |
| 10YRRATE | 210 | 1 | 5% | 2% | -56% | -46% | -44% |
| 30YRRATE | 198 | 0 | 2% | 0% | -100% | -97% | -96% |
| 2YRRATE | 191 | 2 | 4% | 1% | -2% | +5% | +6% |
| 5YRRATE | 176 | 1 | 6% | 2% | -47% | -90% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 22089 | 87 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 21303 | 74 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4397 | 21 | 2% | 1% | -17% | -82% | -82% |
| 0.05–0.1% | 4637 | 18 | 3% | 2% | -42% | -91% | -90% |
| 0.1–0.2% | 7009 | 24 | 4% | 2% | -57% | -90% | -90% |
| 0.2–0.5% | 8007 | 33 | 7% | 3% | -54% | -86% | -86% |
| Over 0.5% | 2993 | 12 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10646 | 37 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 10804 | 48 | 4% | 2% | -49% | -85% | -85% |
| Afternoon (12–6pm) | 10198 | 38 | 4% | 2% | -56% | -85% | -85% |
| Evening (6pm–12am) | 11744 | 38 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,766 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/3 12:13:40 AM | NEAR | UP | 80 sec | -0.189% | — | In play | — |
| 11/3 12:13:40 AM | PALLADIUM | UP | 80 sec | — | — | In play | — |
| 11/3 12:13:24 AM | DOGE | DOWN | 1.6 min | +0.156% | — | In play | — |
| 11/3 12:13:24 AM | ETH | DOWN | 1.6 min | +0.074% | — | In play | — |
| 11/3 12:12:20 AM | SOL | DOWN | 2.7 min | +0.254% | — | In play | — |
| 11/3 12:12:04 AM | AUDUSD | DOWN | 2.9 min | — | — | In play | — |
| 11/3 12:12:04 AM | XRP | DOWN | 2.9 min | +0.208% | — | In play | — |
| 11/3 12:10:45 AM | USDCAD | UP | 4.2 min | — | — | In play | — |
| 11/3 12:10:12 AM | NATGAS | DOWN | 4.8 min | — | — | In play | — |
| 11/3 12:06:47 AM | BRENT | DOWN | 8.2 min | — | — | In play | — |
| 11/3 12:06:47 AM | WTI | DOWN | 8.2 min | — | — | In play | — |
| 11/2 11:59:54 PM | PLATINUM | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 11:59:38 PM | PALLADIUM | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 11:59:22 PM | ZEC | UP | 38 sec | -0.153% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 11:59:06 PM | XRP | UP | 54 sec | -0.128% | 0¢ | ❌ Lost | $0.00 |
| 11/2 11:58:50 PM | AUDUSD | UP | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 11:58:50 PM | DOGE | UP | 70 sec | -0.194% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 11:58:18 PM | NEAR | DOWN | 1.7 min | +0.253% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 11:58:02 PM | BTC | UP | 2.0 min | -0.123% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 11:57:46 PM | WTI | DOWN | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 11:57:14 PM | HYPE | UP | 2.8 min | -0.333% | 0¢ | ❌ Lost | $0.00 |
| 11/2 11:57:14 PM | SILVER | UP | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 11:56:58 PM | SOL | UP | 3.0 min | -0.341% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 11:56:43 PM | GOLD | UP | 3.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 11:56:27 PM | ETH | UP | 3.5 min | -0.220% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 11:56:11 PM | BRENT | DOWN | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 11:55:55 PM | COPPER | UP | 4.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 11:54:19 PM | BNB | UP | 5.7 min | -0.450% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 11:44:44 PM | BTC | DOWN | 15 sec | +0.009% | 0¢ | ❌ Lost | $0.00 |
| 11/2 11:44:44 PM | ETH | UP | 15 sec | -0.030% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
