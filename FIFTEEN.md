# 15-Minute 1¢ Study

*Updated Thu Oct 8, 5:39 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 817 finished bets | 1% | $37.50 | +42% | +4.59¢ | -$15.50 / $53.00 |

*Expect about **76 buys a day** (~$11.45/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 805 | $25.45 | +29% |
| 5+ min left, hold to the close | 352 | $4.10 | +8% |
| Volatility model ≥ 2%, hold to the close | 1498 | $1.10 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 12212 | 12205 | 50 (0%) | 1.07% | -$782.00 (-53%) | Hold to the close: -$782.00 (-53%) |

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
| Volatility model | 7805 | 4.0% | 0.4% (34) | -568% | ❌ Worse |
| Momentum model | 7805 | 4.1% | 0.4% (34) | -601% | ❌ Worse |
| Mean-reversion model | 7805 | 6.7% | 0.4% (34) | -666% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7805 | 34 | -45% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 1498 | 13 | +1% | -74% | -74% | -70% |
| Volatility model ≥ 5% | 817 | 9 | +42% | -65% | -64% | -61% |
| Volatility model ≥ 10% | 501 | 7 | +105% | -48% | -49% | -43% |
| Momentum model ≥ 2% | 1325 | 11 | -0% | -75% | -77% | -74% |
| Momentum model ≥ 5% | 805 | 8 | +29% | -69% | -70% | -67% |
| Momentum model ≥ 10% | 549 | 6 | +56% | -58% | -59% | -56% |
| Mean-reversion model ≥ 2% | 2706 | 20 | -20% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1828 | 16 | -3% | -82% | -82% | -76% |
| Mean-reversion model ≥ 10% | 1208 | 12 | +14% | -80% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 8002 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3115 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1088 | 2% | 2% | 2% | 1% | 1% | 0% |
| **All** | 12205 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 50 | 0% | -$782.00 | -53% | — |
| Sell at 2¢ | 420 | 3% | -$1,330.80 | -90% | 33 sec |
| Sell at 3¢ | 277 | 2% | -$1,331.97 | -90% | 47 sec |
| Sell at 5¢ | 204 | 2% | -$1,307.40 | -88% | 50 sec |
| Sell at 10¢ | 133 | 1% | -$1,251.77 | -84% | 64 sec |
| Sell at 25¢ | 76 | 1% | -$1,146.44 | -77% | 82 sec |
| Sell at 50¢ | 50 | 0% | -$1,018.50 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 348 | 4 | 11% | 3% | +9% | -81% | -85% |
| 2–5 min | 3971 | 25 | 6% | 3% | -38% | -88% | -89% |
| 1–2 min | 3182 | 13 | 3% | 2% | -56% | -94% | -94% |
| Under 1 min | 4700 | 8 | 1% | 0% | -75% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 897 | 6 | 4% | 3% | -19% | -90% | -90% |
| HYPE | 895 | 3 | 5% | 2% | -59% | -89% | -88% |
| DOGE | 891 | 2 | 3% | 2% | -72% | -92% | -91% |
| BNB | 891 | 3 | 4% | 2% | -60% | -91% | -92% |
| ETH | 890 | 7 | 5% | 3% | -3% | -89% | -88% |
| NEAR | 886 | 5 | 6% | 2% | -26% | -72% | -73% |
| SOL | 885 | 0 | 3% | 1% | -100% | -94% | -92% |
| BTC | 884 | 4 | 5% | 2% | -40% | -87% | -90% |
| XRP | 883 | 6 | 2% | 1% | -15% | -82% | -81% |
| GOLD | 519 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 505 | 0 | 3% | 1% | -100% | -95% | -94% |
| WTI | 482 | 3 | 3% | 1% | -31% | -94% | -96% |
| COPPER | 442 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 405 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 386 | 3 | 3% | 2% | -27% | -95% | -93% |
| PALLADIUM | 376 | 1 | 1% | 1% | -75% | -98% | -99% |
| EURUSD | 375 | 3 | 3% | 2% | -25% | -70% | -68% |
| GBPUSD | 354 | 1 | 3% | 2% | -74% | -95% | -95% |
| USDJPY | 319 | 3 | 1% | 1% | -12% | -98% | -97% |
| USDCAD | 20 | 0 | 0% | 0% | -100% | -100% | -100% |
| AUDUSD | 20 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6203 | 26 | 3% | 2% | -52% | -89% | -88% |
| DOWN (bought NO) | 6002 | 24 | 3% | 2% | -54% | -91% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1298 | 8 | 2% | 1% | +6% | -67% | -67% |
| 0.05–0.1% | 1345 | 4 | 3% | 1% | -56% | -92% | -92% |
| 0.1–0.2% | 2027 | 7 | 4% | 2% | -57% | -92% | -92% |
| 0.2–0.5% | 2340 | 12 | 5% | 3% | -44% | -89% | -88% |
| Over 0.5% | 990 | 5 | 6% | 2% | -48% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3090 | 17 | 4% | 2% | -37% | -85% | -85% |
| Morning (6am–12pm) | 3025 | 17 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 2823 | 8 | 3% | 1% | -66% | -89% | -90% |
| Evening (6pm–12am) | 3267 | 8 | 3% | 1% | -72% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,048 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/8 5:29:47 PM | BNB | DOWN | 12 sec | -0.022% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 5:29:47 PM | NATGAS | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 5:29:47 PM | NEAR | DOWN | 12 sec | -0.040% | 0¢ | ❌ Lost | $0.00 |
| 10/8 5:28:58 PM | GOLD | DOWN | 62 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 10/8 5:28:43 PM | SOL | DOWN | 77 sec | +0.096% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 5:28:43 PM | ETH | DOWN | 77 sec | +0.082% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 5:28:43 PM | COPPER | DOWN | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 5:28:27 PM | PLATINUM | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 5:28:27 PM | PALLADIUM | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 5:28:27 PM | ZEC | DOWN | 1.6 min | +0.226% | 1¢ | ❌ Lost | $0.00 |
| 10/8 5:28:27 PM | HYPE | DOWN | 1.6 min | +0.052% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 5:27:39 PM | USDJPY | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 5:27:23 PM | XRP | DOWN | 2.6 min | +0.166% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 5:25:48 PM | SILVER | DOWN | 4.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 5:25:48 PM | WTI | DOWN | 4.2 min | — | 4¢ | ❌ Lost | -$0.15 |
| 10/8 5:14:29 PM | ETH | DOWN | 31 sec | +0.031% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 5:14:29 PM | ZEC | UP | 31 sec | -0.088% | 0¢ | ❌ Lost | $0.00 |
| 10/8 5:14:13 PM | GOLD | DOWN | 47 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 5:14:13 PM | HYPE | UP | 47 sec | -0.183% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 5:14:13 PM | EURUSD | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 5:13:57 PM | BTC | UP | 63 sec | -0.046% | 0¢ | ❌ Lost | $0.00 |
| 10/8 5:13:42 PM | DOGE | DOWN | 78 sec | +0.120% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 5:13:26 PM | XRP | DOWN | 1.6 min | +0.123% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 5:12:39 PM | NEAR | UP | 2.4 min | -0.656% | 1¢ | ❌ Lost | $0.00 |
| 10/8 5:12:07 PM | BNB | DOWN | 2.9 min | +0.106% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 5:10:00 PM | USDJPY | DOWN | 5.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 4:59:37 PM | ZEC | DOWN | 23 sec | +0.082% | 0¢ | ❌ Lost | $0.00 |
| 10/8 4:59:37 PM | AUDUSD | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 4:59:21 PM | BNB | UP | 39 sec | -0.039% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 4:59:21 PM | GOLD | UP | 39 sec | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
