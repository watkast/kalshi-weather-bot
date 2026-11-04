# 15-Minute 1¢ Study

*Updated Wed Nov 4, 9:23 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3642 finished bets | 1% | $111.50 | +27% | +3.06¢ | $77.95 / $33.55 |

*Expect about **97 buys a day** (~$14.61/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3378 | $38.95 | +11% |
| Volatility model ≥ 2%, hold to the close | 6750 | $24.15 | +3% |
| Momentum model ≥ 2%, hold to the close | 5563 | -$53.85 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 45426 | 45416 | 168 (0%) | 1.07% | -$3,182.85 (-58%) | Hold to the close: -$3,182.85 (-58%) |

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
| Volatility model | 27759 | 4.7% | 0.4% (108) | -680% | ❌ Worse |
| Momentum model | 27759 | 4.6% | 0.4% (108) | -707% | ❌ Worse |
| Mean-reversion model | 27759 | 8.1% | 0.4% (108) | -829% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 27759 | 108 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6750 | 60 | +3% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3642 | 37 | +27% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2069 | 22 | +52% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5563 | 42 | -8% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 3378 | 29 | +11% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2203 | 19 | +21% | -75% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11486 | 78 | -26% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8073 | 67 | -8% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 5409 | 47 | -1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 27964 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10792 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6660 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 45416 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 168 | 0% | -$3,182.85 | -58% | — |
| Sell at 2¢ | 1782 | 4% | -$4,819.53 | -87% | 47 sec |
| Sell at 3¢ | 1220 | 3% | -$4,807.05 | -87% | 49 sec |
| Sell at 5¢ | 844 | 2% | -$4,706.25 | -85% | 63 sec |
| Sell at 10¢ | 510 | 1% | -$4,502.75 | -81% | 65 sec |
| Sell at 25¢ | 267 | 1% | -$4,175.08 | -75% | 83 sec |
| Sell at 50¢ | 171 | 0% | -$3,806.60 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2242 | 10 | 11% | 4% | -58% | -81% | -83% |
| 2–5 min | 14614 | 79 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 11445 | 39 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 17104 | 40 | 1% | 0% | -67% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3133 | 13 | 5% | 2% | -46% | -88% | -88% |
| SOL | 3127 | 12 | 4% | 2% | -51% | -90% | -90% |
| HYPE | 3119 | 9 | 5% | 2% | -64% | -89% | -87% |
| BNB | 3119 | 17 | 5% | 2% | -32% | -85% | -84% |
| DOGE | 3107 | 6 | 4% | 2% | -76% | -90% | -90% |
| ETH | 3101 | 12 | 7% | 3% | -53% | -85% | -85% |
| BTC | 3090 | 14 | 5% | 2% | -38% | -87% | -89% |
| NEAR | 3088 | 15 | 5% | 2% | -37% | -84% | -84% |
| XRP | 3080 | 12 | 3% | 1% | -52% | -89% | -89% |
| GOLD | 1672 | 5 | 5% | 2% | -64% | -81% | -83% |
| WTI | 1626 | 5 | 4% | 1% | -63% | -92% | -93% |
| SILVER | 1625 | 8 | 5% | 2% | -42% | -82% | -81% |
| PLATINUM | 1455 | 4 | 2% | 1% | -74% | -96% | -96% |
| EURUSD | 1401 | 3 | 2% | 1% | -80% | -89% | -89% |
| COPPER | 1373 | 6 | 2% | 1% | -59% | -70% | -70% |
| GBPUSD | 1326 | 3 | 2% | 1% | -79% | -96% | -96% |
| NATGAS | 1321 | 8 | 2% | 1% | -43% | -75% | -74% |
| USDJPY | 1309 | 5 | 2% | 1% | -64% | -97% | -97% |
| PALLADIUM | 1304 | 3 | 1% | 1% | -79% | -91% | -91% |
| AUDUSD | 857 | 4 | 2% | 1% | -56% | -86% | -86% |
| USDCAD | 825 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 416 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 256 | 1 | 5% | 2% | -64% | -55% | -53% |
| 30YRRATE | 235 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 234 | 2 | 3% | 0% | -20% | -14% | -14% |
| 5YRRATE | 217 | 1 | 5% | 2% | -57% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 23058 | 89 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 22358 | 79 | 4% | 2% | -59% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4510 | 21 | 2% | 1% | -19% | -83% | -82% |
| 0.05–0.1% | 4762 | 18 | 3% | 2% | -43% | -91% | -90% |
| 0.1–0.2% | 7211 | 25 | 4% | 2% | -57% | -90% | -89% |
| 0.2–0.5% | 8317 | 33 | 6% | 3% | -56% | -87% | -86% |
| Over 0.5% | 3156 | 13 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11276 | 40 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11339 | 49 | 4% | 2% | -51% | -86% | -85% |
| Afternoon (12–6pm) | 10598 | 39 | 4% | 2% | -57% | -86% | -86% |
| Evening (6pm–12am) | 12203 | 40 | 3% | 2% | -62% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,686 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/4 9:14:48 AM | WTI | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 9:14:48 AM | BRENT | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 9:14:32 AM | PALLADIUM | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 9:14:32 AM | GOLD | UP | 27 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/4 9:14:16 AM | GBPUSD | UP | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 9:13:32 AM | USDJPY | DOWN | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 9:13:16 AM | USDCAD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 9:13:00 AM | NEAR | DOWN | 2.0 min | +0.682% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 9:13:00 AM | COPPER | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 9:12:29 AM | EURUSD | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 9:11:57 AM | HYPE | DOWN | 3.0 min | +0.665% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 9:11:57 AM | AUDUSD | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 9:11:42 AM | XRP | DOWN | 3.3 min | +0.503% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 9:11:42 AM | ZEC | DOWN | 3.3 min | +0.907% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 9:11:11 AM | SOL | DOWN | 3.8 min | +0.614% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 9:10:39 AM | BNB | DOWN | 4.3 min | +0.391% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 9:10:24 AM | BTC | DOWN | 4.6 min | +0.546% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 9:10:24 AM | SILVER | UP | 4.6 min | — | 2¢ | ❌ Lost | -$0.15 |
| 11/4 9:10:08 AM | ETH | DOWN | 4.9 min | +0.819% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 9:09:52 AM | DOGE | DOWN | 5.1 min | +0.739% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 8:59:54 AM | BNB | UP | 6 sec | -0.142% | 0¢ | ❌ Lost | $0.00 |
| 11/4 8:59:54 AM | GBPUSD | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 8:59:54 AM | HYPE | DOWN | 6 sec | +0.271% | 0¢ | ❌ Lost | -$0.15 |
| 11/4 8:59:39 AM | 30YRRATE | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 8:59:39 AM | ZEC | UP | 21 sec | -0.109% | 0¢ | ❌ Lost | -$0.15 |
| 11/4 8:59:23 AM | AUDUSD | DOWN | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 8:59:23 AM | SOL | UP | 37 sec | -0.145% | 0¢ | ❌ Lost | $0.00 |
| 11/4 8:59:07 AM | ETH | UP | 53 sec | -0.189% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 8:59:07 AM | DOGE | UP | 53 sec | -0.263% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 8:59:07 AM | BTC | UP | 53 sec | -0.183% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
