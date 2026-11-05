# 15-Minute 1¢ Study

*Updated Thu Nov 5, 2:58 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3687 finished bets | 1% | $135.45 | +33% | +3.67¢ | $89.25 / $46.20 |

*Expect about **97 buys a day** (~$14.50/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3426 | $62.90 | +17% |
| Volatility model ≥ 2%, hold to the close | 6829 | $44.05 | +5% |
| Momentum model ≥ 2%, hold to the close | 5636 | -$32.75 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 46295 | 46284 | 170 (0%) | 1.07% | -$3,263.90 (-58%) | Hold to the close: -$3,263.90 (-58%) |

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
| Volatility model | 28170 | 4.7% | 0.4% (110) | -680% | ❌ Worse |
| Momentum model | 28170 | 4.6% | 0.4% (110) | -707% | ❌ Worse |
| Mean-reversion model | 28170 | 8.1% | 0.4% (110) | -828% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 28170 | 110 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6829 | 62 | +5% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3687 | 39 | +33% | -77% | -75% | -71% |
| Volatility model ≥ 10% | 2102 | 24 | +64% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5636 | 44 | -5% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 3426 | 31 | +17% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2237 | 20 | +25% | -75% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11660 | 80 | -25% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8183 | 69 | -7% | -81% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5482 | 49 | +2% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 28375 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11059 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6850 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 46284 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 170 | 0% | -$3,263.90 | -58% | — |
| Sell at 2¢ | 1817 | 4% | -$4,919.48 | -87% | 47 sec |
| Sell at 3¢ | 1241 | 3% | -$4,907.91 | -87% | 48 sec |
| Sell at 5¢ | 858 | 2% | -$4,806.20 | -85% | 63 sec |
| Sell at 10¢ | 519 | 1% | -$4,600.01 | -82% | 65 sec |
| Sell at 25¢ | 269 | 1% | -$4,277.51 | -76% | 83 sec |
| Sell at 50¢ | 173 | 0% | -$3,902.15 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2290 | 10 | 10% | 4% | -58% | -81% | -83% |
| 2–5 min | 14914 | 79 | 7% | 3% | -48% | -87% | -86% |
| 1–2 min | 11649 | 39 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 17420 | 42 | 1% | 0% | -66% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3178 | 13 | 5% | 2% | -47% | -88% | -88% |
| SOL | 3173 | 12 | 4% | 2% | -52% | -90% | -90% |
| HYPE | 3167 | 9 | 5% | 2% | -64% | -89% | -87% |
| BNB | 3167 | 17 | 5% | 2% | -33% | -85% | -85% |
| DOGE | 3154 | 6 | 4% | 2% | -76% | -90% | -90% |
| ETH | 3148 | 12 | 7% | 3% | -53% | -85% | -85% |
| NEAR | 3132 | 16 | 5% | 2% | -34% | -84% | -84% |
| BTC | 3132 | 15 | 5% | 2% | -35% | -88% | -89% |
| XRP | 3124 | 12 | 3% | 1% | -52% | -89% | -89% |
| GOLD | 1709 | 5 | 5% | 2% | -64% | -81% | -83% |
| SILVER | 1662 | 8 | 5% | 2% | -43% | -82% | -82% |
| WTI | 1661 | 5 | 4% | 1% | -64% | -92% | -93% |
| PLATINUM | 1489 | 4 | 2% | 1% | -75% | -96% | -96% |
| EURUSD | 1431 | 3 | 2% | 1% | -80% | -89% | -89% |
| COPPER | 1407 | 6 | 2% | 1% | -60% | -71% | -70% |
| GBPUSD | 1358 | 3 | 2% | 1% | -79% | -96% | -96% |
| NATGAS | 1347 | 8 | 2% | 1% | -45% | -76% | -75% |
| USDJPY | 1339 | 5 | 2% | 1% | -65% | -97% | -97% |
| PALLADIUM | 1336 | 3 | 1% | 1% | -79% | -91% | -91% |
| AUDUSD | 888 | 4 | 2% | 1% | -58% | -86% | -86% |
| USDCAD | 862 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 448 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 260 | 1 | 5% | 2% | -64% | -56% | -54% |
| 30YRRATE | 244 | 0 | 2% | 1% | -100% | -96% | -95% |
| 2YRRATE | 243 | 2 | 3% | 0% | -23% | -17% | -17% |
| 5YRRATE | 225 | 1 | 4% | 2% | -59% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 23476 | 90 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 22808 | 80 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4557 | 22 | 2% | 1% | -15% | -83% | -82% |
| 0.05–0.1% | 4832 | 18 | 3% | 2% | -43% | -91% | -90% |
| 0.1–0.2% | 7314 | 26 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 8464 | 33 | 6% | 3% | -57% | -87% | -86% |
| Over 0.5% | 3200 | 13 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11276 | 40 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11422 | 50 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 10960 | 39 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 12626 | 41 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,685 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/4 11:44:46 PM | WTI | DOWN | 14 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/4 11:44:30 PM | NEAR | DOWN | 30 sec | -0.052% | 0¢ | ❌ Lost | $0.00 |
| 11/4 11:44:15 PM | PALLADIUM | DOWN | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 11:44:15 PM | SOL | UP | 45 sec | -0.079% | 0¢ | ❌ Lost | $0.00 |
| 11/4 11:44:15 PM | ZEC | DOWN | 45 sec | +0.185% | 0¢ | ❌ Lost | $0.00 |
| 11/4 11:43:57 PM | USDCAD | DOWN | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 11:43:57 PM | USDJPY | DOWN | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 11:43:57 PM | GBPUSD | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 11:43:57 PM | NATGAS | DOWN | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 11:43:57 PM | DOGE | UP | 62 sec | -0.094% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 11:43:41 PM | XRP | UP | 78 sec | -0.138% | 0¢ | ❌ Lost | -$0.15 |
| 11/4 11:43:41 PM | GOLD | UP | 78 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/4 11:43:41 PM | AUDUSD | DOWN | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 11:43:25 PM | ETH | UP | 1.6 min | -0.073% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 11:43:10 PM | BNB | UP | 1.8 min | -0.153% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 11:43:10 PM | HYPE | UP | 1.8 min | -0.220% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 11:43:10 PM | COPPER | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 11:42:36 PM | BTC | UP | 2.4 min | -0.114% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 11:41:32 PM | EURUSD | UP | 3.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/4 11:29:49 PM | PLATINUM | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 11:29:31 PM | BNB | DOWN | 29 sec | -0.017% | 0¢ | ❌ Lost | -$0.15 |
| 11/4 11:29:31 PM | COPPER | UP | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 11:29:15 PM | HYPE | DOWN | 45 sec | +0.053% | 0¢ | ❌ Lost | $0.00 |
| 11/4 11:28:59 PM | BRENT | UP | 61 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/4 11:28:59 PM | DOGE | DOWN | 61 sec | +0.084% | 0¢ | ❌ Lost | -$0.15 |
| 11/4 11:28:43 PM | NEAR | DOWN | 77 sec | +0.097% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 11:28:43 PM | WTI | UP | 77 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/4 11:28:43 PM | ZEC | DOWN | 77 sec | +0.291% | 0¢ | ❌ Lost | $0.00 |
| 11/4 11:28:43 PM | BTC | DOWN | 77 sec | +0.086% | 0¢ | ❌ Lost | $0.00 |
| 11/4 11:28:43 PM | ETH | DOWN | 77 sec | +0.083% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
