# 15-Minute 1¢ Study

*Updated Sat Oct 24, 9:26 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2611 finished bets | 1% | $95.30 | +32% | +3.65¢ | $38.90 / $56.40 |

*Expect about **97 buys a day** (~$14.58/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2406 | $69.15 | +26% |
| Volatility model ≥ 2%, hold to the close | 4819 | $11.00 | +2% |
| Momentum model ≥ 2%, hold to the close | 4021 | -$11.10 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 31145 | 31137 | 119 (0%) | 1.07% | -$2,123.00 (-56%) | Hold to the close: -$2,123.00 (-56%) |

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
| Volatility model | 19930 | 4.6% | 0.4% (84) | -638% | ❌ Worse |
| Momentum model | 19930 | 4.5% | 0.4% (84) | -663% | ❌ Worse |
| Mean-reversion model | 19930 | 7.9% | 0.4% (84) | -772% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 19930 | 84 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4819 | 43 | +2% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 2611 | 28 | +32% | -74% | -73% | -69% |
| Volatility model ≥ 10% | 1485 | 18 | +69% | -65% | -63% | -60% |
| Momentum model ≥ 2% | 4021 | 33 | -2% | -80% | -79% | -76% |
| Momentum model ≥ 5% | 2406 | 24 | +26% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 1572 | 16 | +39% | -70% | -69% | -64% |
| Mean-reversion model ≥ 2% | 8010 | 55 | -25% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5607 | 46 | -10% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3729 | 33 | +0% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 20130 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 7352 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3655 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 31137 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 119 | 0% | -$2,123.00 | -56% | — |
| Sell at 2¢ | 1161 | 4% | -$3,319.14 | -88% | 47 sec |
| Sell at 3¢ | 797 | 3% | -$3,310.17 | -87% | 48 sec |
| Sell at 5¢ | 557 | 2% | -$3,258.95 | -86% | 61 sec |
| Sell at 10¢ | 344 | 1% | -$3,128.36 | -83% | 64 sec |
| Sell at 25¢ | 188 | 1% | -$2,886.72 | -76% | 82 sec |
| Sell at 50¢ | 121 | 0% | -$2,608.25 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1346 | 7 | 11% | 4% | -50% | -81% | -82% |
| 2–5 min | 9939 | 54 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 7902 | 30 | 3% | 1% | -59% | -92% | -91% |
| Under 1 min | 11946 | 28 | 1% | 0% | -66% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2258 | 12 | 5% | 2% | -33% | -89% | -89% |
| HYPE | 2249 | 8 | 5% | 3% | -56% | -88% | -86% |
| BNB | 2245 | 12 | 5% | 2% | -34% | -83% | -82% |
| SOL | 2240 | 6 | 4% | 2% | -67% | -92% | -92% |
| ETH | 2237 | 11 | 6% | 3% | -41% | -86% | -85% |
| DOGE | 2231 | 4 | 4% | 2% | -78% | -90% | -90% |
| XRP | 2228 | 9 | 3% | 1% | -50% | -88% | -88% |
| NEAR | 2225 | 12 | 5% | 3% | -30% | -81% | -81% |
| BTC | 2217 | 12 | 5% | 2% | -28% | -88% | -89% |
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
| UP (bought YES) | 15746 | 65 | 4% | 2% | -53% | -87% | -86% |
| DOWN (bought NO) | 15391 | 54 | 4% | 2% | -60% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3363 | 18 | 2% | 1% | -10% | -80% | -79% |
| 0.05–0.1% | 3478 | 11 | 3% | 2% | -53% | -92% | -91% |
| 0.1–0.2% | 5179 | 19 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 5855 | 28 | 6% | 3% | -47% | -87% | -86% |
| Over 0.5% | 2251 | 10 | 7% | 3% | -54% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7739 | 32 | 4% | 2% | -53% | -85% | -85% |
| Morning (6am–12pm) | 7570 | 34 | 4% | 2% | -49% | -88% | -87% |
| Afternoon (12–6pm) | 7332 | 24 | 4% | 2% | -61% | -87% | -88% |
| Evening (6pm–12am) | 8496 | 29 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,707 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/24 9:14:49 PM | BNB | UP | 10 sec | -0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/24 9:14:33 PM | DOGE | UP | 26 sec | -0.075% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 9:14:33 PM | ETH | DOWN | 26 sec | +0.045% | 0¢ | ❌ Lost | $0.00 |
| 10/24 9:14:17 PM | BTC | DOWN | 42 sec | +0.056% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 9:14:17 PM | SOL | DOWN | 42 sec | +0.069% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 9:13:45 PM | HYPE | DOWN | 75 sec | +0.070% | 0¢ | ❌ Lost | $0.00 |
| 10/24 9:13:13 PM | XRP | UP | 1.8 min | -0.183% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 9:13:13 PM | ZEC | DOWN | 1.8 min | +0.266% | 0¢ | ❌ Lost | $0.00 |
| 10/24 8:59:34 PM | DOGE | UP | 26 sec | -0.117% | 0¢ | ❌ Lost | $0.00 |
| 10/24 8:59:18 PM | BTC | UP | 42 sec | -0.062% | 0¢ | ❌ Lost | $0.00 |
| 10/24 8:59:18 PM | SOL | UP | 42 sec | -0.054% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 8:59:03 PM | ETH | UP | 56 sec | -0.057% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 8:58:46 PM | ZEC | UP | 74 sec | -0.306% | 0¢ | ❌ Lost | $0.00 |
| 10/24 8:58:30 PM | NEAR | UP | 1.5 min | -0.382% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 8:58:14 PM | HYPE | UP | 1.8 min | -0.187% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 8:57:43 PM | XRP | DOWN | 2.3 min | +0.176% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 8:44:33 PM | HYPE | UP | 26 sec | -0.046% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 8:44:33 PM | ZEC | UP | 26 sec | -0.159% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 8:40:50 PM | NEAR | DOWN | 4.2 min | +0.425% | 4¢ | ❌ Lost | -$0.15 |
| 10/24 8:40:18 PM | DOGE | DOWN | 4.7 min | +0.171% | 2¢ | ❌ Lost | -$0.15 |
| 10/24 8:40:18 PM | BTC | DOWN | 4.7 min | +0.176% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 8:40:02 PM | SOL | DOWN | 5.0 min | +0.250% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 8:39:46 PM | ETH | DOWN | 5.2 min | +0.267% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 8:39:46 PM | BNB | DOWN | 5.2 min | +0.242% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 8:38:58 PM | XRP | DOWN | 6.0 min | +0.314% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 8:29:50 PM | BNB | UP | 9 sec | -0.055% | 0¢ | ❌ Lost | $0.00 |
| 10/24 8:29:34 PM | ZEC | DOWN | 25 sec | +0.075% | 0¢ | ❌ Lost | $0.00 |
| 10/24 8:29:34 PM | HYPE | UP | 25 sec | -0.065% | 0¢ | ❌ Lost | $0.00 |
| 10/24 8:29:18 PM | ETH | DOWN | 41 sec | +0.014% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 8:29:18 PM | SOL | UP | 41 sec | -0.042% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
