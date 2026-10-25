# 15-Minute 1¢ Study

*Updated Sun Oct 25, 1:08 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2625 finished bets | 1% | $94.70 | +32% | +3.61¢ | $38.45 / $56.25 |

*Expect about **97 buys a day** (~$14.57/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2418 | $68.85 | +26% |
| Volatility model ≥ 2%, hold to the close | 4840 | $9.65 | +2% |
| Momentum model ≥ 2%, hold to the close | 4039 | -$12.00 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 31259 | 31251 | 119 (0%) | 1.07% | -$2,133.95 (-56%) | Hold to the close: -$2,133.95 (-56%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 20044 | 4.7% | 0.4% (84) | -645% | ❌ Worse |
| Momentum model | 20044 | 4.6% | 0.4% (84) | -671% | ❌ Worse |
| Mean-reversion model | 20044 | 7.9% | 0.4% (84) | -780% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 20044 | 84 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4840 | 43 | +2% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 2625 | 28 | +32% | -74% | -73% | -69% |
| Volatility model ≥ 10% | 1497 | 18 | +69% | -65% | -64% | -60% |
| Momentum model ≥ 2% | 4039 | 33 | -3% | -80% | -79% | -76% |
| Momentum model ≥ 5% | 2418 | 24 | +26% | -76% | -76% | -71% |
| Momentum model ≥ 10% | 1583 | 16 | +39% | -70% | -69% | -64% |
| Mean-reversion model ≥ 2% | 8052 | 55 | -26% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5640 | 46 | -10% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3754 | 33 | -0% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 20244 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7352 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3655 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 31251 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 119 | 0% | -$2,133.95 | -56% | — |
| Sell at 2¢ | 1162 | 4% | -$3,329.83 | -88% | 47 sec |
| Sell at 3¢ | 797 | 3% | -$3,321.12 | -87% | 48 sec |
| Sell at 5¢ | 557 | 2% | -$3,269.90 | -86% | 61 sec |
| Sell at 10¢ | 344 | 1% | -$3,139.31 | -83% | 64 sec |
| Sell at 25¢ | 188 | 1% | -$2,897.67 | -76% | 82 sec |
| Sell at 50¢ | 121 | 0% | -$2,619.20 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1353 | 7 | 11% | 4% | -51% | -81% | -82% |
| 2–5 min | 9973 | 54 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 7927 | 30 | 3% | 1% | -59% | -92% | -91% |
| Under 1 min | 11994 | 28 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2269 | 12 | 5% | 2% | -33% | -89% | -89% |
| HYPE | 2262 | 8 | 5% | 3% | -56% | -88% | -86% |
| BNB | 2259 | 12 | 5% | 2% | -34% | -84% | -83% |
| SOL | 2254 | 6 | 4% | 2% | -67% | -92% | -92% |
| ETH | 2250 | 11 | 6% | 3% | -41% | -86% | -86% |
| DOGE | 2243 | 4 | 4% | 2% | -78% | -90% | -90% |
| XRP | 2240 | 9 | 3% | 1% | -50% | -88% | -88% |
| NEAR | 2238 | 12 | 5% | 3% | -30% | -81% | -81% |
| BTC | 2229 | 12 | 5% | 2% | -28% | -88% | -89% |
| GOLD | 1190 | 4 | 4% | 2% | -60% | -81% | -83% |
| SILVER | 1156 | 5 | 4% | 1% | -50% | -82% | -82% |
| WTI | 1143 | 3 | 3% | 1% | -69% | -94% | -95% |
| PLATINUM | 1010 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 987 | 4 | 1% | 1% | -62% | -69% | -69% |
| EURUSD | 938 | 3 | 2% | 1% | -70% | -86% | -86% |
| NATGAS | 933 | 5 | 2% | 1% | -50% | -86% | -86% |
| PALLADIUM | 897 | 2 | 1% | 0% | -79% | -88% | -88% |
| GBPUSD | 884 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 866 | 5 | 1% | 1% | -46% | -98% | -97% |
| AUDUSD | 428 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 387 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 36 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 15828 | 65 | 4% | 2% | -53% | -87% | -87% |
| DOWN (bought NO) | 15423 | 54 | 4% | 2% | -60% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3393 | 18 | 2% | 1% | -11% | -80% | -79% |
| 0.05–0.1% | 3492 | 11 | 3% | 2% | -54% | -92% | -92% |
| 0.1–0.2% | 5218 | 19 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 5879 | 28 | 6% | 3% | -48% | -87% | -86% |
| Over 0.5% | 2258 | 10 | 7% | 3% | -54% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7774 | 32 | 4% | 2% | -53% | -85% | -85% |
| Morning (6am–12pm) | 7570 | 34 | 4% | 2% | -49% | -88% | -87% |
| Afternoon (12–6pm) | 7332 | 24 | 4% | 2% | -61% | -87% | -88% |
| Evening (6pm–12am) | 8575 | 29 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,730 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/25 12:59:10 AM | BTC | UP | 50 sec | -0.060% | 0¢ | ❌ Lost | $0.00 |
| 10/25 12:58:51 AM | HYPE | UP | 68 sec | -0.140% | 0¢ | ❌ Lost | $0.00 |
| 10/25 12:58:35 AM | DOGE | UP | 84 sec | -0.171% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 12:58:35 AM | NEAR | UP | 84 sec | -0.272% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 12:58:04 AM | BNB | UP | 1.9 min | -0.235% | 0¢ | ❌ Lost | $0.00 |
| 10/25 12:57:14 AM | XRP | UP | 2.8 min | -0.247% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 12:56:41 AM | ETH | UP | 3.3 min | -0.224% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 12:56:25 AM | SOL | UP | 3.6 min | -0.268% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 12:55:22 AM | ZEC | UP | 4.6 min | -0.578% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 12:43:55 AM | NEAR | UP | 64 sec | -0.235% | 0¢ | ❌ Lost | $0.00 |
| 10/25 12:43:55 AM | BNB | UP | 64 sec | -0.103% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 12:43:39 AM | XRP | UP | 80 sec | -0.146% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 12:43:23 AM | BTC | UP | 1.6 min | -0.111% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 12:43:23 AM | HYPE | UP | 1.6 min | -0.129% | 0¢ | ❌ Lost | $0.00 |
| 10/25 12:42:35 AM | DOGE | UP | 2.4 min | -0.229% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 12:41:46 AM | ETH | UP | 3.2 min | -0.172% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 12:41:30 AM | SOL | UP | 3.5 min | -0.197% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 12:39:20 AM | ZEC | UP | 5.7 min | -0.612% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 12:29:57 AM | ETH | UP | 3 sec | -0.016% | 0¢ | ❌ Lost | $0.00 |
| 10/25 12:29:57 AM | HYPE | UP | 3 sec | +0.047% | 0¢ | ❌ Lost | $0.00 |
| 10/25 12:29:57 AM | BTC | DOWN | 3 sec | -0.003% | 0¢ | ❌ Lost | $0.00 |
| 10/25 12:29:41 AM | BNB | DOWN | 19 sec | +0.028% | 0¢ | ❌ Lost | $0.00 |
| 10/25 12:29:25 AM | SOL | DOWN | 35 sec | +0.050% | 0¢ | ❌ Lost | $0.00 |
| 10/25 12:29:25 AM | DOGE | DOWN | 35 sec | +0.033% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 12:29:10 AM | NEAR | DOWN | 49 sec | +0.229% | 0¢ | ❌ Lost | $0.00 |
| 10/25 12:28:38 AM | ZEC | DOWN | 81 sec | +0.144% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 12:28:06 AM | XRP | DOWN | 1.9 min | +0.139% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 12:14:08 AM | ETH | UP | 51 sec | -0.086% | 0¢ | ❌ Lost | $0.00 |
| 10/25 12:14:08 AM | BTC | DOWN | 51 sec | +0.036% | 0¢ | ❌ Lost | $0.00 |
| 10/25 12:14:08 AM | BNB | DOWN | 51 sec | +0.038% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
