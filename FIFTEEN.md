# 15-Minute 1¢ Study

*Updated Mon Nov 2, 9:39 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3529 finished bets | 1% | $123.65 | +31% | +3.50¢ | $69.80 / $53.85 |

*Expect about **98 buys a day** (~$14.74/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3261 | $50.95 | +14% |
| Volatility model ≥ 2%, hold to the close | 6537 | $48.30 | +6% |
| Momentum model ≥ 2%, hold to the close | 5392 | -$35.55 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 43335 | 43325 | 161 (0%) | 1.07% | -$3,020.90 (-57%) | Hold to the close: -$3,020.90 (-57%) |

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
| Volatility model | 26813 | 4.7% | 0.4% (106) | -677% | ❌ Worse |
| Momentum model | 26813 | 4.6% | 0.4% (106) | -702% | ❌ Worse |
| Mean-reversion model | 26813 | 8.1% | 0.4% (106) | -824% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26813 | 106 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6537 | 60 | +6% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3529 | 37 | +31% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 1998 | 22 | +57% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 5392 | 42 | -6% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3261 | 29 | +14% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2129 | 19 | +25% | -74% | -73% | -69% |
| Mean-reversion model ≥ 2% | 11073 | 76 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7762 | 65 | -7% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 5189 | 46 | +1% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 27016 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10222 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6087 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 43325 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 161 | 0% | -$3,020.90 | -57% | — |
| Sell at 2¢ | 1711 | 4% | -$4,592.04 | -87% | 47 sec |
| Sell at 3¢ | 1173 | 3% | -$4,579.43 | -87% | 49 sec |
| Sell at 5¢ | 813 | 2% | -$4,480.45 | -85% | 63 sec |
| Sell at 10¢ | 490 | 1% | -$4,283.00 | -81% | 65 sec |
| Sell at 25¢ | 255 | 1% | -$3,968.85 | -75% | 82 sec |
| Sell at 50¢ | 166 | 0% | -$3,608.40 | -68% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2082 | 9 | 11% | 4% | -59% | -81% | -82% |
| 2–5 min | 13919 | 75 | 7% | 4% | -47% | -86% | -86% |
| 1–2 min | 10937 | 39 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 16376 | 38 | 1% | 0% | -67% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3028 | 13 | 5% | 3% | -45% | -88% | -87% |
| SOL | 3019 | 11 | 4% | 2% | -54% | -91% | -90% |
| BNB | 3016 | 17 | 5% | 2% | -29% | -85% | -84% |
| HYPE | 3014 | 9 | 5% | 2% | -63% | -89% | -87% |
| DOGE | 3001 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 2998 | 11 | 7% | 3% | -55% | -85% | -85% |
| BTC | 2983 | 14 | 5% | 2% | -37% | -88% | -89% |
| NEAR | 2982 | 15 | 5% | 2% | -35% | -83% | -84% |
| XRP | 2975 | 12 | 3% | 1% | -50% | -89% | -89% |
| GOLD | 1587 | 5 | 5% | 2% | -62% | -81% | -83% |
| SILVER | 1547 | 7 | 5% | 2% | -46% | -82% | -82% |
| WTI | 1544 | 4 | 3% | 1% | -69% | -92% | -93% |
| PLATINUM | 1378 | 3 | 2% | 1% | -80% | -96% | -96% |
| EURUSD | 1318 | 3 | 2% | 1% | -79% | -89% | -89% |
| COPPER | 1312 | 6 | 2% | 1% | -57% | -69% | -69% |
| NATGAS | 1264 | 7 | 2% | 1% | -48% | -82% | -81% |
| GBPUSD | 1249 | 2 | 2% | 1% | -85% | -96% | -96% |
| PALLADIUM | 1241 | 3 | 1% | 1% | -77% | -90% | -91% |
| USDJPY | 1230 | 5 | 2% | 1% | -62% | -97% | -96% |
| AUDUSD | 775 | 4 | 2% | 1% | -52% | -85% | -84% |
| USDCAD | 740 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 349 | 0 | 1% | 1% | -100% | -98% | -96% |
| 10YRRATE | 210 | 1 | 5% | 2% | -56% | -46% | -44% |
| 30YRRATE | 198 | 0 | 2% | 0% | -100% | -97% | -96% |
| 2YRRATE | 191 | 2 | 4% | 1% | -2% | +5% | +6% |
| 5YRRATE | 176 | 1 | 6% | 2% | -47% | -90% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 22045 | 87 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 21280 | 74 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4390 | 21 | 2% | 1% | -17% | -82% | -82% |
| 0.05–0.1% | 4633 | 18 | 3% | 2% | -42% | -91% | -90% |
| 0.1–0.2% | 6997 | 24 | 4% | 2% | -57% | -90% | -90% |
| 0.2–0.5% | 7999 | 33 | 7% | 3% | -54% | -86% | -86% |
| Over 0.5% | 2991 | 12 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10646 | 37 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 10804 | 48 | 4% | 2% | -49% | -85% | -85% |
| Afternoon (12–6pm) | 10198 | 38 | 4% | 2% | -56% | -85% | -85% |
| Evening (6pm–12am) | 11677 | 38 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,765 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/2 9:29:55 PM | SILVER | UP | 5 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 9:29:55 PM | NATGAS | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 9:29:39 PM | PALLADIUM | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 9:29:00 PM | WTI | DOWN | 60 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 9:29:00 PM | BRENT | DOWN | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 9:29:00 PM | USDCAD | DOWN | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 9:29:00 PM | PLATINUM | UP | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 9:28:44 PM | BNB | DOWN | 76 sec | +0.119% | 0¢ | ❌ Lost | $0.00 |
| 11/2 9:28:44 PM | AUDUSD | DOWN | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 9:28:28 PM | EURUSD | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 9:28:13 PM | BTC | DOWN | 1.8 min | +0.146% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 9:27:56 PM | GBPUSD | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 9:27:56 PM | ZEC | DOWN | 2.0 min | +0.360% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 9:27:40 PM | ETH | DOWN | 2.3 min | +0.152% | 0¢ | ❌ Lost | $0.00 |
| 11/2 9:27:40 PM | SOL | DOWN | 2.3 min | +0.211% | 0¢ | ❌ Lost | $0.00 |
| 11/2 9:27:24 PM | HYPE | DOWN | 2.6 min | +0.219% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 9:27:08 PM | DOGE | DOWN | 2.9 min | +0.222% | 0¢ | ❌ Lost | $0.00 |
| 11/2 9:26:49 PM | NEAR | DOWN | 3.2 min | +0.627% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 9:25:28 PM | XRP | DOWN | 4.5 min | +0.232% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 9:14:47 PM | PALLADIUM | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 9:14:47 PM | COPPER | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 9:14:47 PM | NEAR | DOWN | 12 sec | -0.034% | 0¢ | ❌ Lost | $0.00 |
| 11/2 9:14:32 PM | SILVER | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 9:14:32 PM | GBPUSD | DOWN | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 9:14:32 PM | BTC | UP | 27 sec | -0.041% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 9:14:13 PM | WTI | DOWN | 46 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 9:14:13 PM | BRENT | DOWN | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 9:14:13 PM | BNB | UP | 46 sec | -0.115% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 9:14:13 PM | HYPE | DOWN | 46 sec | +0.136% | 0¢ | ❌ Lost | $0.00 |
| 11/2 9:14:13 PM | SOL | DOWN | 46 sec | +0.092% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
