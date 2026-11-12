# 15-Minute 1¢ Study

*Updated Wed Nov 11, 11:00 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4232 finished bets | 1% | $174.50 | +37% | +4.12¢ | $84.25 / $90.25 |

*Expect about **94 buys a day** (~$14.12/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3968 | $102.25 | +24% |
| Volatility model ≥ 2%, hold to the close | 7779 | $44.15 | +5% |
| Momentum model ≥ 2%, hold to the close | 6464 | -$14.95 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 54432 | 54398 | 208 (0%) | 1.07% | -$3,723.55 (-56%) | Hold to the close: -$3,723.55 (-56%) |

*In play or awaiting result: 22. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 32674 | 4.7% | 0.4% (132) | -669% | ❌ Worse |
| Momentum model | 32674 | 4.6% | 0.4% (132) | -694% | ❌ Worse |
| Mean-reversion model | 32674 | 8.1% | 0.4% (132) | -811% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 32674 | 132 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7779 | 70 | +5% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4232 | 46 | +37% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2446 | 28 | +64% | -62% | -61% | -57% |
| Momentum model ≥ 2% | 6464 | 52 | -2% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 3968 | 38 | +24% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2601 | 25 | +35% | -66% | -65% | -61% |
| Mean-reversion model ≥ 2% | 13471 | 92 | -25% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 9416 | 78 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6288 | 56 | +1% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 32879 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 13051 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8468 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 54398 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 208 | 0% | -$3,723.55 | -56% | — |
| Sell at 2¢ | 2161 | 4% | -$5,779.69 | -87% | 47 sec |
| Sell at 3¢ | 1470 | 3% | -$5,768.25 | -87% | 48 sec |
| Sell at 5¢ | 1017 | 2% | -$5,652.50 | -85% | 63 sec |
| Sell at 10¢ | 615 | 1% | -$5,423.90 | -82% | 65 sec |
| Sell at 25¢ | 327 | 1% | -$5,035.18 | -76% | 82 sec |
| Sell at 50¢ | 214 | 0% | -$4,561.05 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2708 | 13 | 11% | 4% | -54% | -81% | -83% |
| 2–5 min | 17587 | 96 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 13737 | 45 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 20354 | 54 | 1% | 0% | -62% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3680 | 17 | 5% | 2% | -40% | -88% | -88% |
| SOL | 3676 | 16 | 4% | 2% | -45% | -86% | -86% |
| HYPE | 3669 | 11 | 5% | 2% | -62% | -89% | -88% |
| BNB | 3661 | 19 | 5% | 2% | -35% | -86% | -85% |
| DOGE | 3657 | 8 | 4% | 2% | -72% | -90% | -90% |
| ETH | 3652 | 16 | 7% | 3% | -46% | -82% | -81% |
| NEAR | 3633 | 17 | 5% | 2% | -39% | -85% | -85% |
| BTC | 3632 | 17 | 5% | 2% | -36% | -87% | -88% |
| XRP | 3619 | 13 | 3% | 1% | -55% | -89% | -89% |
| GOLD | 1960 | 5 | 5% | 2% | -69% | -82% | -83% |
| WTI | 1951 | 6 | 4% | 2% | -63% | -91% | -92% |
| SILVER | 1912 | 9 | 5% | 2% | -44% | -83% | -82% |
| PLATINUM | 1740 | 4 | 3% | 1% | -79% | -96% | -95% |
| EURUSD | 1679 | 5 | 2% | 1% | -72% | -90% | -90% |
| COPPER | 1626 | 6 | 2% | 1% | -66% | -74% | -74% |
| GBPUSD | 1607 | 6 | 2% | 1% | -65% | -96% | -96% |
| NATGAS | 1600 | 9 | 2% | 1% | -48% | -73% | -73% |
| USDJPY | 1582 | 6 | 2% | 1% | -65% | -97% | -96% |
| PALLADIUM | 1563 | 4 | 1% | 1% | -76% | -92% | -92% |
| AUDUSD | 1136 | 6 | 2% | 1% | -51% | -88% | -88% |
| USDCAD | 1098 | 0 | 2% | 1% | -100% | -96% | -96% |
| BRENT | 699 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 353 | 2 | 4% | 2% | -47% | -66% | -64% |
| 2YRRATE | 338 | 4 | 4% | 2% | +10% | -38% | -36% |
| 30YRRATE | 332 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 311 | 2 | 4% | 2% | -40% | -93% | -95% |
| INX | 32 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 27626 | 108 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 26772 | 100 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5203 | 25 | 2% | 1% | -15% | -77% | -77% |
| 0.05–0.1% | 5591 | 20 | 3% | 2% | -45% | -91% | -91% |
| 0.1–0.2% | 8435 | 31 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 9897 | 41 | 6% | 3% | -54% | -87% | -87% |
| Over 0.5% | 3745 | 17 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13236 | 43 | 4% | 2% | -63% | -88% | -88% |
| Morning (6am–12pm) | 13083 | 60 | 4% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 13132 | 58 | 4% | 2% | -48% | -86% | -86% |
| Evening (6pm–12am) | 14947 | 47 | 4% | 2% | -64% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,869 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/11 10:59:48 PM | NATGAS | UP | 11 sec | — | 0¢ | In play | — |
| 11/11 10:59:48 PM | BTC | DOWN | 11 sec | +0.023% | 0¢ | ❌ Lost | $0.00 |
| 11/11 10:59:48 PM | GBPUSD | DOWN | 11 sec | — | 0¢ | In play | — |
| 11/11 10:59:48 PM | USDJPY | UP | 11 sec | — | 0¢ | In play | — |
| 11/11 10:59:33 PM | ZEC | UP | 26 sec | -0.154% | 0¢ | ❌ Lost | $0.00 |
| 11/11 10:59:33 PM | BNB | UP | 26 sec | -0.070% | 0¢ | ❌ Lost | $0.00 |
| 11/11 10:59:33 PM | DOGE | UP | 26 sec | -0.072% | 0¢ | ❌ Lost | $0.00 |
| 11/11 10:59:33 PM | HYPE | UP | 26 sec | -0.074% | 0¢ | ❌ Lost | -$0.15 |
| 11/11 10:59:33 PM | COPPER | UP | 26 sec | — | 0¢ | In play | — |
| 11/11 10:59:14 PM | WTI | UP | 46 sec | — | 1¢ | In play | — |
| 11/11 10:59:14 PM | BRENT | UP | 46 sec | — | 0¢ | In play | — |
| 11/11 10:59:14 PM | SOL | UP | 46 sec | -0.085% | 0¢ | In play | — |
| 11/11 10:58:58 PM | NEAR | UP | 62 sec | -0.348% | 0¢ | ❌ Lost | $0.00 |
| 11/11 10:58:58 PM | XRP | UP | 62 sec | -0.182% | 0¢ | In play | — |
| 11/11 10:58:42 PM | AUDUSD | DOWN | 78 sec | — | 0¢ | In play | — |
| 11/11 10:57:02 PM | PALLADIUM | DOWN | 3.0 min | — | 0¢ | In play | — |
| 11/11 10:57:02 PM | ETH | DOWN | 3.0 min | +0.158% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 10:56:15 PM | SILVER | DOWN | 3.7 min | — | 1¢ | In play | — |
| 11/11 10:55:09 PM | GOLD | DOWN | 4.8 min | — | 1¢ | In play | — |
| 11/11 10:54:03 PM | PLATINUM | DOWN | 5.9 min | — | 0¢ | In play | — |
| 11/11 10:44:56 PM | NATGAS | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 10:44:41 PM | NEAR | DOWN | 18 sec | +0.000% | 0¢ | ❌ Lost | $0.00 |
| 11/11 10:44:41 PM | COPPER | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 10:44:41 PM | SOL | DOWN | 18 sec | +0.056% | 0¢ | ❌ Lost | $0.00 |
| 11/11 10:44:22 PM | BNB | DOWN | 37 sec | +0.015% | 0¢ | ❌ Lost | $0.00 |
| 11/11 10:44:22 PM | ETH | DOWN | 37 sec | +0.053% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 10:44:22 PM | XRP | DOWN | 37 sec | +0.067% | 0¢ | ❌ Lost | $0.00 |
| 11/11 10:44:06 PM | ZEC | DOWN | 53 sec | +0.220% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 10:44:06 PM | DOGE | UP | 53 sec | -0.079% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 10:43:50 PM | USDJPY | UP | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
