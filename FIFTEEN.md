# 15-Minute 1¢ Study

*Updated Sat Oct 10, 9:06 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1032 finished bets | 1% | $27.05 | +24% | +2.62¢ | $0.65 / $26.40 |

*Expect about **80 buys a day** (~$12.05/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 998 | $3.70 | +3% |
| 5+ min left, hold to the close | 391 | -$1.75 | -3% |
| Volatility model ≥ 5%, sell at 50¢ | 1032 | -$17.45 | -15% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 14173 | 14166 | 56 (0%) | 1.07% | -$929.15 (-54%) | Hold to the close: -$929.15 (-54%) |

*In play or awaiting result: 6. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 9321 | 4.3% | 0.4% (39) | -636% | ❌ Worse |
| Momentum model | 9321 | 4.3% | 0.4% (39) | -664% | ❌ Worse |
| Mean-reversion model | 9321 | 7.0% | 0.4% (39) | -739% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 9321 | 39 | -48% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1826 | 14 | -11% | -76% | -76% | -72% |
| Volatility model ≥ 5% | 1032 | 10 | +24% | -70% | -69% | -65% |
| Volatility model ≥ 10% | 648 | 8 | +77% | -57% | -57% | -52% |
| Momentum model ≥ 2% | 1613 | 11 | -18% | -78% | -79% | -77% |
| Momentum model ≥ 5% | 998 | 8 | +3% | -73% | -74% | -71% |
| Momentum model ≥ 10% | 691 | 6 | +22% | -65% | -66% | -62% |
| Mean-reversion model ≥ 2% | 3241 | 23 | -23% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2204 | 17 | -15% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1465 | 13 | +2% | -81% | -81% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 9519 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3444 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1203 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 14166 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 56 | 0% | -$929.15 | -54% | — |
| Sell at 2¢ | 480 | 3% | -$1,546.35 | -90% | 33 sec |
| Sell at 3¢ | 318 | 2% | -$1,547.13 | -90% | 47 sec |
| Sell at 5¢ | 233 | 2% | -$1,519.70 | -89% | 50 sec |
| Sell at 10¢ | 152 | 1% | -$1,444.03 | -84% | 64 sec |
| Sell at 25¢ | 87 | 1% | -$1,327.18 | -77% | 81 sec |
| Sell at 50¢ | 57 | 0% | -$1,188.40 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 387 | 4 | 11% | 3% | -2% | -81% | -86% |
| 2–5 min | 4572 | 28 | 6% | 3% | -40% | -89% | -89% |
| 1–2 min | 3717 | 15 | 3% | 2% | -56% | -94% | -94% |
| Under 1 min | 5486 | 9 | 1% | 0% | -76% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1066 | 6 | 4% | 3% | -32% | -90% | -90% |
| HYPE | 1065 | 3 | 4% | 2% | -65% | -90% | -89% |
| DOGE | 1063 | 2 | 4% | 2% | -76% | -91% | -91% |
| BNB | 1061 | 5 | 4% | 2% | -43% | -91% | -92% |
| ETH | 1056 | 8 | 5% | 3% | -7% | -89% | -88% |
| SOL | 1055 | 1 | 3% | 1% | -88% | -94% | -93% |
| BTC | 1053 | 4 | 5% | 2% | -50% | -88% | -91% |
| NEAR | 1051 | 6 | 6% | 2% | -26% | -74% | -75% |
| XRP | 1049 | 6 | 2% | 1% | -29% | -83% | -83% |
| GOLD | 568 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 555 | 1 | 3% | 1% | -79% | -94% | -94% |
| WTI | 529 | 3 | 3% | 1% | -35% | -94% | -96% |
| COPPER | 490 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 451 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 431 | 3 | 3% | 2% | -35% | -95% | -93% |
| PALLADIUM | 420 | 1 | 1% | 0% | -78% | -98% | -99% |
| EURUSD | 412 | 3 | 3% | 2% | -32% | -72% | -71% |
| GBPUSD | 389 | 1 | 3% | 2% | -76% | -96% | -95% |
| USDJPY | 353 | 3 | 1% | 1% | -21% | -98% | -97% |
| AUDUSD | 25 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 24 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 7129 | 29 | 3% | 2% | -53% | -89% | -89% |
| DOWN (bought NO) | 7037 | 27 | 3% | 1% | -56% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1672 | 9 | 2% | 1% | -10% | -74% | -73% |
| 0.05–0.1% | 1689 | 5 | 3% | 1% | -57% | -92% | -92% |
| 0.1–0.2% | 2424 | 8 | 4% | 2% | -59% | -91% | -92% |
| 0.2–0.5% | 2657 | 14 | 5% | 3% | -42% | -89% | -88% |
| Over 0.5% | 1074 | 5 | 6% | 2% | -52% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3525 | 19 | 4% | 2% | -38% | -85% | -86% |
| Morning (6am–12pm) | 3425 | 18 | 4% | 2% | -40% | -91% | -91% |
| Afternoon (12–6pm) | 3332 | 9 | 3% | 1% | -68% | -90% | -90% |
| Evening (6pm–12am) | 3884 | 10 | 3% | 1% | -71% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,358 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/10 8:58:48 PM | NEAR | UP | 72 sec | -0.303% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:58:48 PM | BTC | UP | 72 sec | -0.043% | 0¢ | ❌ Lost | $0.00 |
| 10/10 8:58:33 PM | ZEC | DOWN | 87 sec | +0.273% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 8:58:17 PM | ETH | UP | 1.7 min | -0.032% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:57:45 PM | HYPE | UP | 2.2 min | -0.182% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:57:29 PM | XRP | UP | 2.5 min | -0.114% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:56:57 PM | BNB | UP | 3.0 min | -0.072% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:56:27 PM | SOL | UP | 3.5 min | -0.131% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 8:55:24 PM | DOGE | UP | 4.6 min | -0.190% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:44:03 PM | ZEC | UP | 56 sec | -0.051% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 8:43:00 PM | XRP | DOWN | 2.0 min | +0.093% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:42:44 PM | DOGE | DOWN | 2.3 min | +0.097% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 8:42:29 PM | NEAR | DOWN | 2.5 min | +0.274% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:42:13 PM | HYPE | DOWN | 2.8 min | +0.259% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 8:41:57 PM | SOL | DOWN | 3.0 min | +0.187% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:41:57 PM | BTC | DOWN | 3.0 min | +0.102% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:41:25 PM | BNB | DOWN | 3.6 min | +0.108% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:41:25 PM | ETH | DOWN | 3.6 min | +0.135% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:29:52 PM | XRP | UP | 8 sec | -0.029% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 8:29:52 PM | SOL | DOWN | 8 sec | +0.033% | 0¢ | ❌ Lost | $0.00 |
| 10/10 8:29:52 PM | BTC | DOWN | 8 sec | +0.002% | 0¢ | ❌ Lost | $0.00 |
| 10/10 8:29:35 PM | BNB | UP | 25 sec | -0.017% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:29:35 PM | ETH | DOWN | 25 sec | +0.024% | 0¢ | ❌ Lost | $0.00 |
| 10/10 8:28:17 PM | NEAR | UP | 1.7 min | -0.429% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:28:17 PM | HYPE | DOWN | 1.7 min | +0.090% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:25:21 PM | ZEC | DOWN | 4.7 min | +0.559% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:25:21 PM | DOGE | DOWN | 4.7 min | +0.114% | 39¢ | ❌ Lost | -$0.15 |
| 10/10 8:14:36 PM | XRP | DOWN | 23 sec | +0.014% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 8:14:36 PM | BTC | DOWN | 23 sec | +0.014% | 0¢ | ❌ Lost | $0.00 |
| 10/10 8:14:20 PM | SOL | UP | 39 sec | -0.037% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
