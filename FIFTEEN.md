# 15-Minute 1¢ Study

*Updated Thu Oct 8, 6:40 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 818 finished bets | 1% | $37.35 | +42% | +4.57¢ | -$15.65 / $53.00 |

*Expect about **76 buys a day** (~$11.42/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 807 | $25.15 | +29% |
| 5+ min left, hold to the close | 354 | $3.80 | +7% |
| Volatility model ≥ 2%, hold to the close | 1502 | $0.50 | +0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 12267 | 12260 | 50 (0%) | 1.07% | -$789.50 (-53%) | Hold to the close: -$789.50 (-53%) |

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
| Volatility model | 7840 | 4.0% | 0.4% (34) | -567% | ❌ Worse |
| Momentum model | 7840 | 4.0% | 0.4% (34) | -600% | ❌ Worse |
| Mean-reversion model | 7840 | 6.7% | 0.4% (34) | -665% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7840 | 34 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 1502 | 13 | +0% | -74% | -74% | -70% |
| Volatility model ≥ 5% | 818 | 9 | +42% | -65% | -64% | -61% |
| Volatility model ≥ 10% | 502 | 7 | +105% | -48% | -49% | -44% |
| Momentum model ≥ 2% | 1328 | 11 | -0% | -75% | -77% | -74% |
| Momentum model ≥ 5% | 807 | 8 | +29% | -69% | -70% | -67% |
| Momentum model ≥ 10% | 550 | 6 | +56% | -59% | -60% | -56% |
| Mean-reversion model ≥ 2% | 2713 | 20 | -20% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1832 | 16 | -3% | -82% | -82% | -76% |
| Mean-reversion model ≥ 10% | 1209 | 12 | +14% | -80% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 8037 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3128 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1095 | 2% | 2% | 2% | 1% | 1% | 0% |
| **All** | 12260 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 50 | 0% | -$789.50 | -53% | — |
| Sell at 2¢ | 423 | 3% | -$1,337.52 | -90% | 33 sec |
| Sell at 3¢ | 279 | 2% | -$1,338.69 | -90% | 47 sec |
| Sell at 5¢ | 205 | 2% | -$1,314.25 | -88% | 50 sec |
| Sell at 10¢ | 134 | 1% | -$1,257.96 | -84% | 64 sec |
| Sell at 25¢ | 77 | 1% | -$1,150.63 | -77% | 81 sec |
| Sell at 50¢ | 50 | 0% | -$1,026.00 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 350 | 4 | 11% | 3% | +9% | -81% | -85% |
| 2–5 min | 3992 | 25 | 6% | 3% | -39% | -88% | -89% |
| 1–2 min | 3200 | 13 | 3% | 2% | -56% | -94% | -94% |
| Under 1 min | 4714 | 8 | 1% | 0% | -75% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 900 | 6 | 4% | 3% | -20% | -90% | -90% |
| HYPE | 899 | 3 | 5% | 2% | -59% | -89% | -88% |
| DOGE | 895 | 2 | 3% | 2% | -72% | -92% | -91% |
| BNB | 895 | 3 | 4% | 2% | -60% | -91% | -92% |
| ETH | 894 | 7 | 5% | 3% | -4% | -89% | -88% |
| NEAR | 890 | 5 | 6% | 2% | -26% | -72% | -73% |
| SOL | 889 | 0 | 3% | 1% | -100% | -94% | -92% |
| BTC | 888 | 4 | 5% | 2% | -41% | -87% | -90% |
| XRP | 887 | 6 | 2% | 1% | -15% | -82% | -82% |
| GOLD | 522 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 508 | 0 | 3% | 1% | -100% | -94% | -94% |
| WTI | 483 | 3 | 3% | 1% | -31% | -94% | -96% |
| COPPER | 444 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 407 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 387 | 3 | 3% | 2% | -28% | -95% | -93% |
| EURUSD | 378 | 3 | 3% | 2% | -26% | -70% | -68% |
| PALLADIUM | 377 | 1 | 1% | 1% | -75% | -98% | -99% |
| GBPUSD | 357 | 1 | 3% | 2% | -74% | -95% | -95% |
| USDJPY | 320 | 3 | 1% | 1% | -13% | -98% | -97% |
| USDCAD | 20 | 0 | 0% | 0% | -100% | -100% | -100% |
| AUDUSD | 20 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6233 | 26 | 4% | 2% | -52% | -89% | -88% |
| DOWN (bought NO) | 6027 | 24 | 3% | 2% | -54% | -91% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1299 | 8 | 2% | 1% | +6% | -68% | -67% |
| 0.05–0.1% | 1348 | 4 | 3% | 1% | -56% | -92% | -92% |
| 0.1–0.2% | 2038 | 7 | 4% | 2% | -57% | -91% | -92% |
| 0.2–0.5% | 2355 | 12 | 5% | 3% | -44% | -89% | -88% |
| Over 0.5% | 995 | 5 | 6% | 2% | -48% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3090 | 17 | 4% | 2% | -37% | -85% | -85% |
| Morning (6am–12pm) | 3025 | 17 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 2853 | 8 | 3% | 1% | -67% | -89% | -90% |
| Evening (6pm–12am) | 3292 | 8 | 3% | 1% | -72% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,056 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/8 6:29:53 PM | WTI | UP | 6 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 6:29:06 PM | SILVER | UP | 54 sec | — | 47¢ | ❌ Lost | -$0.15 |
| 10/8 6:28:18 PM | BTC | UP | 1.7 min | -0.138% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 6:28:18 PM | ZEC | UP | 1.7 min | -0.214% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 6:28:02 PM | GOLD | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 6:26:27 PM | ETH | UP | 3.5 min | -0.170% | 2¢ | ❌ Lost | -$0.15 |
| 10/8 6:26:11 PM | XRP | UP | 3.8 min | -0.354% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 6:25:39 PM | DOGE | UP | 4.3 min | -0.340% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 6:25:39 PM | HYPE | UP | 4.3 min | -0.395% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 6:25:07 PM | SOL | UP | 4.9 min | -0.738% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 6:25:07 PM | NEAR | UP | 4.9 min | -1.090% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 6:25:07 PM | BNB | UP | 4.9 min | -0.288% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 6:14:35 PM | COPPER | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 6:14:35 PM | GOLD | DOWN | 24 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/8 6:13:48 PM | EURUSD | DOWN | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 6:13:32 PM | SOL | DOWN | 88 sec | +0.157% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 6:13:16 PM | BTC | DOWN | 1.7 min | +0.137% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 6:13:16 PM | GBPUSD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 6:13:00 PM | HYPE | DOWN | 2.0 min | +0.264% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 6:12:45 PM | BNB | DOWN | 2.2 min | +0.110% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 6:12:13 PM | DOGE | DOWN | 2.8 min | +0.242% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 6:11:57 PM | ETH | DOWN | 3.0 min | +0.211% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 6:11:57 PM | ZEC | DOWN | 3.0 min | +0.567% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 6:10:53 PM | XRP | DOWN | 4.1 min | +0.413% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 6:10:22 PM | NEAR | DOWN | 4.6 min | +0.978% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 5:59:20 PM | COPPER | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 5:59:04 PM | SILVER | DOWN | 56 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/8 5:59:04 PM | GBPUSD | DOWN | 56 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 5:58:49 PM | NATGAS | DOWN | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 5:58:49 PM | EURUSD | DOWN | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
