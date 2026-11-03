# 15-Minute 1¢ Study

*Updated Tue Nov 3, 3:30 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3553 finished bets | 1% | $120.95 | +30% | +3.40¢ | $68.60 / $52.35 |

*Expect about **98 buys a day** (~$14.75/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3285 | $48.40 | +14% |
| Volatility model ≥ 2%, hold to the close | 6575 | $43.80 | +6% |
| Momentum model ≥ 2%, hold to the close | 5420 | -$38.55 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 43676 | 43652 | 161 (0%) | 1.07% | -$3,062.60 (-58%) | Hold to the close: -$3,062.60 (-58%) |

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
| Volatility model | 26961 | 4.7% | 0.4% (106) | -682% | ❌ Worse |
| Momentum model | 26961 | 4.6% | 0.4% (106) | -706% | ❌ Worse |
| Mean-reversion model | 26961 | 8.1% | 0.4% (106) | -830% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26961 | 106 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6575 | 60 | +6% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3553 | 37 | +30% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2017 | 22 | +56% | -70% | -69% | -65% |
| Momentum model ≥ 2% | 5420 | 42 | -6% | -81% | -81% | -77% |
| Momentum model ≥ 5% | 3285 | 29 | +14% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2146 | 19 | +24% | -74% | -73% | -69% |
| Mean-reversion model ≥ 2% | 11147 | 76 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7820 | 65 | -8% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 5229 | 46 | -0% | -80% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 27164 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10312 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6176 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 43652 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 161 | 0% | -$3,062.60 | -58% | — |
| Sell at 2¢ | 1720 | 4% | -$4,631.40 | -87% | 47 sec |
| Sell at 3¢ | 1179 | 3% | -$4,618.79 | -87% | 48 sec |
| Sell at 5¢ | 816 | 2% | -$4,520.20 | -85% | 63 sec |
| Sell at 10¢ | 491 | 1% | -$4,323.39 | -81% | 65 sec |
| Sell at 25¢ | 255 | 1% | -$4,010.55 | -75% | 82 sec |
| Sell at 50¢ | 166 | 0% | -$3,650.10 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2101 | 9 | 11% | 4% | -59% | -81% | -82% |
| 2–5 min | 14027 | 75 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 11032 | 39 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 16481 | 38 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3044 | 13 | 5% | 3% | -45% | -88% | -88% |
| SOL | 3036 | 11 | 4% | 2% | -54% | -91% | -90% |
| BNB | 3032 | 17 | 5% | 2% | -30% | -85% | -84% |
| HYPE | 3031 | 9 | 5% | 2% | -63% | -89% | -87% |
| DOGE | 3017 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 3014 | 11 | 7% | 3% | -55% | -85% | -85% |
| BTC | 3000 | 14 | 5% | 2% | -37% | -88% | -89% |
| NEAR | 2999 | 15 | 5% | 2% | -35% | -83% | -84% |
| XRP | 2991 | 12 | 3% | 1% | -50% | -89% | -88% |
| GOLD | 1600 | 5 | 5% | 2% | -62% | -81% | -83% |
| SILVER | 1562 | 7 | 5% | 2% | -47% | -82% | -82% |
| WTI | 1557 | 4 | 3% | 1% | -69% | -92% | -94% |
| PLATINUM | 1388 | 3 | 2% | 1% | -80% | -96% | -96% |
| EURUSD | 1331 | 3 | 2% | 1% | -79% | -89% | -89% |
| COPPER | 1323 | 6 | 2% | 1% | -58% | -69% | -69% |
| NATGAS | 1272 | 7 | 2% | 1% | -49% | -82% | -81% |
| GBPUSD | 1260 | 2 | 2% | 1% | -85% | -96% | -96% |
| PALLADIUM | 1250 | 3 | 1% | 1% | -78% | -90% | -91% |
| USDJPY | 1240 | 5 | 2% | 1% | -62% | -97% | -96% |
| AUDUSD | 790 | 4 | 2% | 1% | -53% | -85% | -85% |
| USDCAD | 753 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 360 | 0 | 1% | 1% | -100% | -98% | -96% |
| 10YRRATE | 218 | 1 | 5% | 2% | -57% | -48% | -46% |
| 30YRRATE | 205 | 0 | 1% | 0% | -100% | -97% | -96% |
| 2YRRATE | 198 | 2 | 4% | 1% | -6% | +1% | +2% |
| 5YRRATE | 181 | 1 | 6% | 2% | -48% | -90% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 22198 | 87 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 21454 | 74 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4418 | 21 | 2% | 1% | -17% | -82% | -82% |
| 0.05–0.1% | 4652 | 18 | 3% | 2% | -42% | -91% | -90% |
| 0.1–0.2% | 7037 | 24 | 4% | 2% | -57% | -90% | -90% |
| 0.2–0.5% | 8048 | 33 | 7% | 3% | -55% | -86% | -86% |
| Over 0.5% | 3003 | 12 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10906 | 37 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 10804 | 48 | 4% | 2% | -49% | -85% | -85% |
| Afternoon (12–6pm) | 10198 | 38 | 4% | 2% | -56% | -85% | -85% |
| Evening (6pm–12am) | 11744 | 38 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,754 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/3 3:29:52 AM | GBPUSD | DOWN | 8 sec | — | 0¢ | In play | — |
| 11/3 3:29:36 AM | BTC | DOWN | 24 sec | +0.032% | 0¢ | In play | — |
| 11/3 3:29:36 AM | BRENT | DOWN | 24 sec | — | 0¢ | In play | — |
| 11/3 3:29:05 AM | GOLD | UP | 54 sec | — | 1¢ | In play | — |
| 11/3 3:28:49 AM | XRP | DOWN | 70 sec | +0.048% | 0¢ | In play | — |
| 11/3 3:28:33 AM | WTI | DOWN | 86 sec | — | 1¢ | In play | — |
| 11/3 3:28:33 AM | PLATINUM | DOWN | 86 sec | — | 0¢ | In play | — |
| 11/3 3:28:17 AM | AUDUSD | UP | 1.7 min | — | 0¢ | In play | — |
| 11/3 3:28:01 AM | NEAR | DOWN | 2.0 min | +0.199% | 1¢ | In play | — |
| 11/3 3:27:43 AM | ETH | DOWN | 2.3 min | +0.153% | 0¢ | In play | — |
| 11/3 3:27:27 AM | SOL | DOWN | 2.5 min | +0.158% | 1¢ | In play | — |
| 11/3 3:27:27 AM | BNB | DOWN | 2.5 min | +0.062% | 1¢ | In play | — |
| 11/3 3:26:56 AM | DOGE | DOWN | 3.0 min | +0.120% | 1¢ | In play | — |
| 11/3 3:25:35 AM | ZEC | DOWN | 4.4 min | +0.536% | 1¢ | In play | — |
| 11/3 3:14:37 AM | BNB | DOWN | 22 sec | -0.043% | 0¢ | ❌ Lost | $0.00 |
| 11/3 3:14:21 AM | 30YRRATE | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 3:14:21 AM | ZEC | UP | 38 sec | -0.151% | 0¢ | ❌ Lost | -$0.15 |
| 11/3 3:14:21 AM | DOGE | UP | 38 sec | -0.078% | 0¢ | ❌ Lost | $0.00 |
| 11/3 3:14:05 AM | 10YRRATE | DOWN | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 3:14:05 AM | 5YRRATE | DOWN | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 3:14:05 AM | PLATINUM | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 3:14:05 AM | EURUSD | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 3:14:05 AM | BTC | UP | 54 sec | -0.076% | 0¢ | ❌ Lost | $0.00 |
| 11/3 3:13:50 AM | ETH | UP | 70 sec | -0.120% | 0¢ | ❌ Lost | $0.00 |
| 11/3 3:13:50 AM | USDCAD | DOWN | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 3:13:50 AM | GOLD | UP | 70 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 3:13:50 AM | 2YRRATE | DOWN | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 3:13:33 AM | AUDUSD | UP | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 3:13:01 AM | NEAR | UP | 2.0 min | -0.394% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 3:13:01 AM | XRP | UP | 2.0 min | -0.120% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
