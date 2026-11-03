# 15-Minute 1¢ Study

*Updated Tue Nov 3, 12:45 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3534 finished bets | 1% | $123.20 | +31% | +3.49¢ | $69.35 / $53.85 |

*Expect about **98 buys a day** (~$14.71/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3268 | $50.35 | +14% |
| Volatility model ≥ 2%, hold to the close | 6548 | $47.10 | +6% |
| Momentum model ≥ 2%, hold to the close | 5400 | -$36.30 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 43455 | 43429 | 161 (0%) | 1.07% | -$3,034.40 (-57%) | Hold to the close: -$3,034.40 (-57%) |

*In play or awaiting result: 25. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 26864 | 4.7% | 0.4% (106) | -678% | ❌ Worse |
| Momentum model | 26864 | 4.6% | 0.4% (106) | -703% | ❌ Worse |
| Mean-reversion model | 26864 | 8.1% | 0.4% (106) | -825% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26864 | 106 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6548 | 60 | +6% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3534 | 37 | +31% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2002 | 22 | +57% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 5400 | 42 | -6% | -81% | -81% | -77% |
| Momentum model ≥ 5% | 3268 | 29 | +14% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2134 | 19 | +25% | -74% | -73% | -69% |
| Mean-reversion model ≥ 2% | 11092 | 76 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7776 | 65 | -7% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 5196 | 46 | +0% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 27067 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10256 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6106 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 43429 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 161 | 0% | -$3,034.40 | -57% | — |
| Sell at 2¢ | 1714 | 4% | -$4,604.76 | -87% | 47 sec |
| Sell at 3¢ | 1175 | 3% | -$4,592.15 | -87% | 49 sec |
| Sell at 5¢ | 814 | 2% | -$4,493.30 | -85% | 63 sec |
| Sell at 10¢ | 490 | 1% | -$4,296.50 | -81% | 65 sec |
| Sell at 25¢ | 255 | 1% | -$3,982.35 | -75% | 82 sec |
| Sell at 50¢ | 166 | 0% | -$3,621.90 | -68% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2088 | 9 | 11% | 4% | -59% | -81% | -82% |
| 2–5 min | 13958 | 75 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 10965 | 39 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 16407 | 38 | 1% | 0% | -67% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3033 | 13 | 5% | 3% | -45% | -88% | -87% |
| SOL | 3025 | 11 | 4% | 2% | -54% | -91% | -90% |
| BNB | 3022 | 17 | 5% | 2% | -30% | -85% | -84% |
| HYPE | 3020 | 9 | 5% | 2% | -63% | -89% | -87% |
| DOGE | 3006 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 3004 | 11 | 7% | 3% | -55% | -85% | -85% |
| BTC | 2989 | 14 | 5% | 2% | -37% | -88% | -89% |
| NEAR | 2988 | 15 | 5% | 2% | -35% | -83% | -84% |
| XRP | 2980 | 12 | 3% | 1% | -50% | -89% | -89% |
| GOLD | 1591 | 5 | 5% | 2% | -62% | -81% | -83% |
| SILVER | 1553 | 7 | 5% | 2% | -47% | -82% | -82% |
| WTI | 1549 | 4 | 3% | 1% | -69% | -92% | -93% |
| PLATINUM | 1382 | 3 | 2% | 1% | -80% | -96% | -96% |
| EURUSD | 1323 | 3 | 2% | 1% | -79% | -89% | -89% |
| COPPER | 1316 | 6 | 2% | 1% | -57% | -69% | -69% |
| NATGAS | 1266 | 7 | 2% | 1% | -48% | -82% | -81% |
| GBPUSD | 1252 | 2 | 2% | 1% | -85% | -96% | -96% |
| PALLADIUM | 1245 | 3 | 1% | 1% | -78% | -90% | -91% |
| USDJPY | 1231 | 5 | 2% | 1% | -62% | -97% | -96% |
| AUDUSD | 781 | 4 | 2% | 1% | -52% | -85% | -84% |
| USDCAD | 744 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 354 | 0 | 1% | 1% | -100% | -98% | -96% |
| 10YRRATE | 210 | 1 | 5% | 2% | -56% | -46% | -44% |
| 30YRRATE | 198 | 0 | 2% | 0% | -100% | -97% | -96% |
| 2YRRATE | 191 | 2 | 4% | 1% | -2% | +5% | +6% |
| 5YRRATE | 176 | 1 | 6% | 2% | -47% | -90% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 22098 | 87 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 21331 | 74 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4399 | 21 | 2% | 1% | -17% | -82% | -82% |
| 0.05–0.1% | 4638 | 18 | 3% | 2% | -42% | -91% | -90% |
| 0.1–0.2% | 7014 | 24 | 4% | 2% | -57% | -90% | -90% |
| 0.2–0.5% | 8015 | 33 | 7% | 3% | -54% | -86% | -86% |
| Over 0.5% | 2995 | 12 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10683 | 37 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 10804 | 48 | 4% | 2% | -49% | -85% | -85% |
| Afternoon (12–6pm) | 10198 | 38 | 4% | 2% | -56% | -85% | -85% |
| Evening (6pm–12am) | 11744 | 38 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,768 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/3 12:44:45 AM | WTI | UP | 14 sec | — | — | In play | — |
| 11/3 12:44:45 AM | USDCAD | DOWN | 14 sec | — | — | In play | — |
| 11/3 12:44:29 AM | USDJPY | UP | 30 sec | — | — | In play | — |
| 11/3 12:44:29 AM | BTC | UP | 30 sec | -0.049% | — | In play | — |
| 11/3 12:44:29 AM | ETH | UP | 30 sec | -0.056% | — | In play | — |
| 11/3 12:43:57 AM | ZEC | UP | 63 sec | -0.355% | — | In play | — |
| 11/3 12:43:57 AM | GOLD | UP | 63 sec | — | — | In play | — |
| 11/3 12:43:43 AM | NEAR | UP | 76 sec | -0.295% | — | In play | — |
| 11/3 12:41:19 AM | DOGE | UP | 3.7 min | -0.208% | — | In play | — |
| 11/3 12:41:19 AM | SOL | UP | 3.7 min | -0.258% | — | In play | — |
| 11/3 12:40:15 AM | HYPE | UP | 4.8 min | -0.343% | — | In play | — |
| 11/3 12:40:15 AM | PLATINUM | UP | 4.8 min | — | — | In play | — |
| 11/3 12:40:15 AM | XRP | UP | 4.8 min | -0.223% | — | In play | — |
| 11/3 12:39:59 AM | PALLADIUM | UP | 5.0 min | — | — | In play | — |
| 11/3 12:39:59 AM | SILVER | UP | 5.0 min | — | — | In play | — |
| 11/3 12:39:26 AM | COPPER | UP | 5.5 min | — | — | In play | — |
| 11/3 12:29:44 AM | GOLD | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 12:29:12 AM | COPPER | DOWN | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 12:29:12 AM | PLATINUM | DOWN | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 12:28:39 AM | USDCAD | UP | 80 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 12:28:09 AM | BRENT | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 12:27:53 AM | SILVER | DOWN | 2.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 12:27:37 AM | WTI | UP | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 12:26:49 AM | XRP | DOWN | 3.2 min | +0.192% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 12:26:31 AM | HYPE | DOWN | 3.5 min | +0.241% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 12:26:31 AM | DOGE | DOWN | 3.5 min | +0.271% | 0¢ | ❌ Lost | -$0.15 |
| 11/3 12:26:31 AM | ZEC | DOWN | 3.5 min | +0.547% | 0¢ | ❌ Lost | -$0.15 |
| 11/3 12:26:15 AM | SOL | DOWN | 3.8 min | +0.330% | 0¢ | ❌ Lost | -$0.15 |
| 11/3 12:25:44 AM | BTC | DOWN | 4.2 min | +0.219% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 12:25:12 AM | EURUSD | DOWN | 4.8 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
