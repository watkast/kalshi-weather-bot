# 15-Minute 1¢ Study

*Updated Sun Oct 25, 12:07 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2621 finished bets | 1% | $94.85 | +32% | +3.62¢ | $38.60 / $56.25 |

*Expect about **97 buys a day** (~$14.57/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2415 | $69.00 | +26% |
| Volatility model ≥ 2%, hold to the close | 4833 | $10.10 | +2% |
| Momentum model ≥ 2%, hold to the close | 4034 | -$11.55 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 31224 | 31216 | 119 (0%) | 1.07% | -$2,130.95 (-56%) | Hold to the close: -$2,130.95 (-56%) |

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
| Volatility model | 20009 | 4.7% | 0.4% (84) | -642% | ❌ Worse |
| Momentum model | 20009 | 4.5% | 0.4% (84) | -668% | ❌ Worse |
| Mean-reversion model | 20009 | 7.9% | 0.4% (84) | -777% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 20009 | 84 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4833 | 43 | +2% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 2621 | 28 | +32% | -74% | -73% | -69% |
| Volatility model ≥ 10% | 1495 | 18 | +69% | -65% | -64% | -60% |
| Momentum model ≥ 2% | 4034 | 33 | -2% | -80% | -79% | -76% |
| Momentum model ≥ 5% | 2415 | 24 | +26% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 1580 | 16 | +39% | -70% | -69% | -64% |
| Mean-reversion model ≥ 2% | 8036 | 55 | -25% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5628 | 46 | -10% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3747 | 33 | -0% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 20209 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7352 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3655 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 31216 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 119 | 0% | -$2,130.95 | -56% | — |
| Sell at 2¢ | 1162 | 4% | -$3,326.83 | -88% | 47 sec |
| Sell at 3¢ | 797 | 3% | -$3,318.12 | -87% | 48 sec |
| Sell at 5¢ | 557 | 2% | -$3,266.90 | -86% | 61 sec |
| Sell at 10¢ | 344 | 1% | -$3,136.31 | -83% | 64 sec |
| Sell at 25¢ | 188 | 1% | -$2,894.67 | -76% | 82 sec |
| Sell at 50¢ | 121 | 0% | -$2,616.20 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1352 | 7 | 11% | 4% | -51% | -81% | -82% |
| 2–5 min | 9963 | 54 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 7915 | 30 | 3% | 1% | -59% | -92% | -91% |
| Under 1 min | 11982 | 28 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2265 | 12 | 5% | 2% | -33% | -89% | -89% |
| HYPE | 2258 | 8 | 5% | 3% | -56% | -88% | -86% |
| BNB | 2255 | 12 | 5% | 2% | -34% | -84% | -83% |
| SOL | 2250 | 6 | 4% | 2% | -67% | -92% | -92% |
| ETH | 2246 | 11 | 6% | 3% | -41% | -86% | -86% |
| DOGE | 2239 | 4 | 4% | 2% | -78% | -90% | -90% |
| XRP | 2237 | 9 | 3% | 1% | -50% | -88% | -88% |
| NEAR | 2234 | 12 | 5% | 3% | -30% | -81% | -81% |
| BTC | 2225 | 12 | 5% | 2% | -28% | -88% | -89% |
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
| UP (bought YES) | 15802 | 65 | 4% | 2% | -53% | -87% | -86% |
| DOWN (bought NO) | 15414 | 54 | 4% | 2% | -60% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3385 | 18 | 2% | 1% | -11% | -80% | -79% |
| 0.05–0.1% | 3490 | 11 | 3% | 2% | -54% | -92% | -92% |
| 0.1–0.2% | 5205 | 19 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 5871 | 28 | 6% | 3% | -47% | -87% | -86% |
| Over 0.5% | 2254 | 10 | 7% | 3% | -54% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7739 | 32 | 4% | 2% | -53% | -85% | -85% |
| Morning (6am–12pm) | 7570 | 34 | 4% | 2% | -49% | -88% | -87% |
| Afternoon (12–6pm) | 7332 | 24 | 4% | 2% | -61% | -87% | -88% |
| Evening (6pm–12am) | 8575 | 29 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,720 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/24 11:59:58 PM | SOL | DOWN | 1 sec | +0.003% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 11:59:42 PM | ETH | UP | 17 sec | -0.023% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 11:59:42 PM | HYPE | UP | 17 sec | -0.015% | 0¢ | ❌ Lost | $0.00 |
| 10/24 11:59:26 PM | DOGE | UP | 33 sec | -0.150% | 0¢ | ❌ Lost | $0.00 |
| 10/24 11:58:05 PM | NEAR | UP | 1.9 min | -0.375% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 11:56:25 PM | XRP | UP | 3.6 min | -0.292% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 11:54:33 PM | BNB | UP | 5.4 min | -0.310% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 11:42:35 PM | BNB | UP | 2.4 min | -0.204% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 11:40:13 PM | XRP | UP | 4.8 min | -0.405% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 11:40:13 PM | HYPE | UP | 4.8 min | -0.404% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 11:40:13 PM | NEAR | UP | 4.8 min | -0.578% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 11:40:13 PM | DOGE | UP | 4.8 min | -0.586% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 11:39:44 PM | BTC | UP | 5.3 min | -0.260% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 11:39:28 PM | SOL | UP | 5.5 min | -0.332% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 11:38:45 PM | ZEC | UP | 6.2 min | -0.532% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 11:36:53 PM | ETH | UP | 8.1 min | -0.260% | 2¢ | ❌ Lost | -$0.15 |
| 10/24 11:29:23 PM | NEAR | UP | 36 sec | -0.163% | 0¢ | ❌ Lost | $0.00 |
| 10/24 11:29:07 PM | HYPE | UP | 53 sec | -0.112% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 11:28:49 PM | DOGE | UP | 71 sec | -0.160% | 0¢ | ❌ Lost | $0.00 |
| 10/24 11:28:33 PM | BNB | UP | 87 sec | -0.088% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 11:28:33 PM | ZEC | UP | 87 sec | -0.230% | 0¢ | ❌ Lost | $0.00 |
| 10/24 11:28:02 PM | SOL | UP | 2.0 min | -0.116% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 11:27:44 PM | BTC | UP | 2.3 min | -0.074% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 11:27:44 PM | XRP | UP | 2.3 min | -0.175% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 11:26:57 PM | ETH | UP | 3.0 min | -0.107% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 11:14:52 PM | ETH | UP | 8 sec | -0.021% | 0¢ | ❌ Lost | $0.00 |
| 10/24 11:14:20 PM | BTC | UP | 40 sec | -0.025% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 11:14:20 PM | BNB | UP | 40 sec | -0.076% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 11:14:05 PM | NEAR | UP | 55 sec | -0.196% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 11:14:05 PM | SOL | UP | 55 sec | -0.091% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
