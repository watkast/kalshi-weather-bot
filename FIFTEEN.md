# 15-Minute 1¢ Study

*Updated Mon Oct 12, 2:00 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1202 finished bets | 1% | $37.50 | +29% | +3.12¢ | $33.05 / $4.45 |

*Expect about **83 buys a day** (~$12.39/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1152 | $16.40 | +13% |
| 5+ min left, hold to the close | 432 | -$7.90 | -12% |
| Volatility model ≥ 2%, hold to the close | 2120 | -$16.85 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 15854 | 15836 | 62 (0%) | 1.07% | -$1,041.95 (-55%) | Hold to the close: -$1,041.95 (-55%) |

*In play or awaiting result: 17. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 10532 | 4.5% | 0.4% (45) | -672% | ❌ Worse |
| Momentum model | 10532 | 4.5% | 0.4% (45) | -698% | ❌ Worse |
| Mean-reversion model | 10532 | 7.2% | 0.4% (45) | -778% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 10532 | 45 | -46% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2120 | 17 | -7% | -77% | -77% | -74% |
| Volatility model ≥ 5% | 1202 | 12 | +29% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 758 | 8 | +53% | -62% | -62% | -59% |
| Momentum model ≥ 2% | 1865 | 14 | -9% | -79% | -80% | -78% |
| Momentum model ≥ 5% | 1152 | 10 | +13% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 795 | 7 | +25% | -68% | -69% | -65% |
| Mean-reversion model ≥ 2% | 3694 | 26 | -23% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2527 | 20 | -12% | -83% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1679 | 14 | -3% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 10730 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3774 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1332 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 15836 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 62 | 0% | -$1,041.95 | -55% | — |
| Sell at 2¢ | 538 | 3% | -$1,728.07 | -90% | 33 sec |
| Sell at 3¢ | 357 | 2% | -$1,728.72 | -91% | 47 sec |
| Sell at 5¢ | 261 | 2% | -$1,698.30 | -89% | 50 sec |
| Sell at 10¢ | 171 | 1% | -$1,615.94 | -85% | 64 sec |
| Sell at 25¢ | 97 | 1% | -$1,490.88 | -78% | 80 sec |
| Sell at 50¢ | 64 | 0% | -$1,337.95 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 428 | 4 | 11% | 3% | -12% | -82% | -86% |
| 2–5 min | 5087 | 32 | 6% | 3% | -38% | -88% | -89% |
| 1–2 min | 4191 | 16 | 3% | 2% | -59% | -94% | -94% |
| Under 1 min | 6126 | 10 | 1% | 0% | -76% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1205 | 7 | 4% | 2% | -29% | -90% | -90% |
| HYPE | 1202 | 4 | 4% | 2% | -59% | -90% | -89% |
| DOGE | 1196 | 2 | 4% | 2% | -79% | -91% | -90% |
| BNB | 1194 | 5 | 4% | 2% | -49% | -91% | -92% |
| ETH | 1192 | 8 | 5% | 2% | -18% | -90% | -89% |
| SOL | 1192 | 2 | 3% | 1% | -79% | -93% | -92% |
| BTC | 1187 | 5 | 5% | 2% | -44% | -88% | -91% |
| NEAR | 1181 | 7 | 5% | 2% | -22% | -76% | -77% |
| XRP | 1181 | 7 | 2% | 1% | -26% | -85% | -85% |
| GOLD | 620 | 0 | 3% | 1% | -100% | -93% | -94% |
| SILVER | 604 | 1 | 3% | 1% | -81% | -94% | -94% |
| WTI | 580 | 3 | 3% | 1% | -41% | -94% | -96% |
| COPPER | 542 | 0 | 1% | 1% | -100% | -98% | -98% |
| PLATINUM | 497 | 0 | 0% | 0% | -100% | -100% | -99% |
| PALLADIUM | 466 | 1 | 1% | 0% | -80% | -98% | -98% |
| NATGAS | 465 | 3 | 3% | 2% | -40% | -96% | -94% |
| EURUSD | 445 | 3 | 3% | 2% | -37% | -74% | -73% |
| GBPUSD | 426 | 1 | 2% | 1% | -78% | -96% | -96% |
| USDJPY | 384 | 3 | 1% | 1% | -27% | -98% | -97% |
| USDCAD | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| AUDUSD | 38 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 7989 | 34 | 3% | 2% | -51% | -90% | -89% |
| DOWN (bought NO) | 7847 | 28 | 3% | 2% | -59% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1927 | 9 | 2% | 1% | -22% | -77% | -76% |
| 0.05–0.1% | 1918 | 6 | 3% | 1% | -55% | -92% | -92% |
| 0.1–0.2% | 2749 | 9 | 4% | 2% | -60% | -91% | -92% |
| 0.2–0.5% | 2980 | 18 | 5% | 3% | -34% | -89% | -88% |
| Over 0.5% | 1153 | 5 | 6% | 2% | -55% | -89% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4019 | 20 | 4% | 2% | -43% | -86% | -86% |
| Morning (6am–12pm) | 3780 | 20 | 4% | 2% | -39% | -91% | -91% |
| Afternoon (12–6pm) | 3678 | 9 | 3% | 1% | -71% | -90% | -91% |
| Evening (6pm–12am) | 4359 | 13 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,525 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/12 1:59:56 PM | USDCAD | DOWN | 3 sec | — | 0¢ | In play | — |
| 10/12 1:59:40 PM | NATGAS | UP | 19 sec | — | 0¢ | In play | — |
| 10/12 1:59:24 PM | ZEC | DOWN | 36 sec | +0.023% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 1:59:24 PM | HYPE | UP | 36 sec | -0.084% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 1:59:07 PM | NEAR | UP | 52 sec | -0.354% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 1:59:07 PM | GBPUSD | UP | 52 sec | — | 0¢ | In play | — |
| 10/12 1:58:35 PM | BNB | DOWN | 84 sec | +0.034% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 1:58:35 PM | EURUSD | UP | 84 sec | — | 0¢ | In play | — |
| 10/12 1:58:35 PM | XRP | DOWN | 84 sec | +0.103% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 1:58:19 PM | GOLD | DOWN | 1.7 min | — | 0¢ | In play | — |
| 10/12 1:58:19 PM | BTC | DOWN | 1.7 min | +0.095% | 0¢ | In play | — |
| 10/12 1:58:00 PM | SOL | DOWN | 2.0 min | +0.120% | 0¢ | In play | — |
| 10/12 1:57:28 PM | DOGE | DOWN | 2.5 min | +0.201% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 1:57:28 PM | SILVER | DOWN | 2.5 min | — | 1¢ | In play | — |
| 10/12 1:57:13 PM | COPPER | DOWN | 2.8 min | — | 0¢ | In play | — |
| 10/12 1:57:13 PM | PLATINUM | DOWN | 2.8 min | — | 0¢ | In play | — |
| 10/12 1:57:13 PM | ETH | DOWN | 2.8 min | +0.135% | 1¢ | In play | — |
| 10/12 1:44:59 PM | COPPER | DOWN | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 1:44:59 PM | XRP | DOWN | 0 sec | +0.007% | 0¢ | ❌ Lost | $0.00 |
| 10/12 1:44:59 PM | PLATINUM | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 1:44:59 PM | GBPUSD | DOWN | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 1:44:43 PM | DOGE | DOWN | 16 sec | +0.074% | 0¢ | ❌ Lost | $0.00 |
| 10/12 1:44:43 PM | SOL | DOWN | 16 sec | +0.070% | 0¢ | ❌ Lost | $0.00 |
| 10/12 1:44:27 PM | NEAR | DOWN | 32 sec | +0.035% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 1:43:54 PM | ETH | UP | 65 sec | -0.060% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 1:43:38 PM | BTC | DOWN | 81 sec | +0.048% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 1:43:06 PM | WTI | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 1:43:06 PM | SILVER | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 1:42:51 PM | ZEC | DOWN | 2.1 min | +0.242% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 1:42:51 PM | HYPE | DOWN | 2.1 min | +0.201% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
