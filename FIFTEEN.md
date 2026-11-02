# 15-Minute 1¢ Study

*Updated Mon Nov 2, 11:38 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3507 finished bets | 1% | $125.75 | +32% | +3.59¢ | $71.30 / $54.45 |

*Expect about **99 buys a day** (~$14.82/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 2%, hold to the close | 6483 | $54.60 | +7% |
| Momentum model ≥ 5%, hold to the close | 3238 | $53.20 | +15% |
| Momentum model ≥ 2%, hold to the close | 5349 | -$31.05 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 42766 | 42756 | 159 (0%) | 1.07% | -$2,978.85 (-57%) | Hold to the close: -$2,978.85 (-57%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 26555 | 4.7% | 0.4% (106) | -674% | ❌ Worse |
| Momentum model | 26555 | 4.6% | 0.4% (106) | -697% | ❌ Worse |
| Mean-reversion model | 26555 | 8.1% | 0.4% (106) | -821% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26555 | 106 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6483 | 60 | +7% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3507 | 37 | +32% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1988 | 22 | +58% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 5349 | 42 | -5% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3238 | 29 | +15% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2115 | 19 | +25% | -74% | -73% | -69% |
| Mean-reversion model ≥ 2% | 10981 | 76 | -24% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7696 | 65 | -7% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 5144 | 46 | +1% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 26757 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10047 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5952 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 42756 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 159 | 0% | -$2,978.85 | -57% | — |
| Sell at 2¢ | 1670 | 4% | -$4,546.65 | -87% | 47 sec |
| Sell at 3¢ | 1145 | 3% | -$4,534.30 | -87% | 48 sec |
| Sell at 5¢ | 795 | 2% | -$4,436.10 | -85% | 63 sec |
| Sell at 10¢ | 480 | 1% | -$4,254.05 | -82% | 65 sec |
| Sell at 25¢ | 251 | 1% | -$3,940.04 | -76% | 83 sec |
| Sell at 50¢ | 164 | 0% | -$3,579.85 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2045 | 9 | 11% | 4% | -58% | -81% | -82% |
| 2–5 min | 13726 | 75 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10805 | 38 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 16169 | 37 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2998 | 13 | 5% | 3% | -44% | -88% | -88% |
| SOL | 2989 | 11 | 4% | 2% | -54% | -91% | -91% |
| BNB | 2986 | 17 | 5% | 2% | -29% | -85% | -84% |
| HYPE | 2984 | 9 | 5% | 2% | -63% | -89% | -87% |
| DOGE | 2972 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 2971 | 11 | 6% | 3% | -55% | -86% | -85% |
| BTC | 2954 | 14 | 5% | 2% | -36% | -88% | -89% |
| NEAR | 2952 | 15 | 5% | 2% | -34% | -83% | -83% |
| XRP | 2951 | 12 | 3% | 1% | -50% | -89% | -89% |
| GOLD | 1564 | 5 | 5% | 2% | -61% | -81% | -83% |
| SILVER | 1522 | 7 | 5% | 2% | -45% | -82% | -82% |
| WTI | 1520 | 4 | 3% | 1% | -68% | -93% | -94% |
| PLATINUM | 1355 | 3 | 2% | 1% | -79% | -96% | -96% |
| EURUSD | 1296 | 3 | 2% | 1% | -78% | -89% | -89% |
| COPPER | 1292 | 5 | 2% | 1% | -64% | -76% | -75% |
| NATGAS | 1247 | 7 | 2% | 1% | -48% | -81% | -80% |
| GBPUSD | 1225 | 2 | 2% | 1% | -85% | -96% | -96% |
| PALLADIUM | 1220 | 2 | 1% | 0% | -85% | -90% | -91% |
| USDJPY | 1212 | 5 | 2% | 1% | -61% | -97% | -96% |
| AUDUSD | 750 | 4 | 1% | 1% | -50% | -85% | -84% |
| USDCAD | 723 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 327 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 202 | 1 | 5% | 2% | -54% | -45% | -43% |
| 30YRRATE | 190 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 185 | 2 | 4% | 1% | +1% | +8% | +9% |
| 5YRRATE | 169 | 1 | 6% | 2% | -45% | -90% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 21746 | 87 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 21010 | 72 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4360 | 21 | 2% | 1% | -16% | -82% | -81% |
| 0.05–0.1% | 4601 | 18 | 3% | 2% | -41% | -91% | -91% |
| 0.1–0.2% | 6933 | 24 | 4% | 2% | -57% | -90% | -90% |
| 0.2–0.5% | 7897 | 33 | 7% | 3% | -54% | -87% | -86% |
| Over 0.5% | 2961 | 12 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10646 | 37 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 10763 | 48 | 4% | 2% | -49% | -85% | -85% |
| Afternoon (12–6pm) | 9923 | 37 | 4% | 2% | -56% | -87% | -87% |
| Evening (6pm–12am) | 11424 | 37 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,783 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/2 11:29:43 AM | PLATINUM | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 11:29:08 AM | 30YRRATE | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 11:29:08 AM | 5YRRATE | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 11:29:08 AM | 10YRRATE | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 11:29:08 AM | 2YRRATE | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 11:28:52 AM | GOLD | UP | 68 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 11:28:52 AM | USDCAD | DOWN | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 11:28:36 AM | GBPUSD | UP | 84 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 11:28:21 AM | SOL | UP | 1.6 min | -0.228% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 11:28:21 AM | USDJPY | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 11:28:21 AM | PALLADIUM | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 11:28:21 AM | COPPER | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 11:27:52 AM | DOGE | UP | 2.1 min | -0.367% | 0¢ | ❌ Lost | $0.00 |
| 11/2 11:27:52 AM | NATGAS | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 11:27:36 AM | BRENT | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 11:27:36 AM | SILVER | UP | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 11:27:20 AM | AUDUSD | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 11:27:05 AM | XRP | UP | 2.9 min | -0.266% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 11:26:47 AM | WTI | DOWN | 3.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 11:26:31 AM | ETH | UP | 3.5 min | -0.289% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 11:26:31 AM | BNB | UP | 3.5 min | -0.253% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 11:26:15 AM | ZEC | UP | 3.8 min | -0.753% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 11:26:15 AM | NEAR | UP | 3.8 min | -0.574% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 11:26:00 AM | BTC | UP | 4.0 min | -0.276% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 11:26:00 AM | EURUSD | UP | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 11:24:37 AM | HYPE | UP | 5.4 min | -0.903% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 11:14:46 AM | EURUSD | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 11:14:46 AM | 2YRRATE | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 11:14:30 AM | XRP | DOWN | 29 sec | +0.008% | 0¢ | ❌ Lost | $0.00 |
| 11/2 11:14:30 AM | USDCAD | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
