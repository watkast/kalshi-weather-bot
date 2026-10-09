# 15-Minute 1¢ Study

*Updated Thu Oct 8, 7:00 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 819 finished bets | 1% | $37.35 | +42% | +4.56¢ | -$15.65 / $53.00 |

*Expect about **76 buys a day** (~$11.43/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 808 | $25.15 | +29% |
| 5+ min left, hold to the close | 354 | $3.80 | +7% |
| Volatility model ≥ 2%, hold to the close | 1503 | $0.50 | +0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 12296 | 12279 | 50 (0%) | 1.07% | -$791.45 (-53%) | Hold to the close: -$791.45 (-53%) |

*In play or awaiting result: 16. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 7854 | 4.0% | 0.4% (34) | -571% | ❌ Worse |
| Momentum model | 7854 | 4.1% | 0.4% (34) | -604% | ❌ Worse |
| Mean-reversion model | 7854 | 6.7% | 0.4% (34) | -669% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7854 | 34 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 1503 | 13 | +0% | -74% | -74% | -70% |
| Volatility model ≥ 5% | 819 | 9 | +42% | -65% | -64% | -61% |
| Volatility model ≥ 10% | 503 | 7 | +105% | -48% | -49% | -44% |
| Momentum model ≥ 2% | 1331 | 11 | -0% | -75% | -77% | -74% |
| Momentum model ≥ 5% | 808 | 8 | +29% | -69% | -70% | -67% |
| Momentum model ≥ 10% | 551 | 6 | +56% | -59% | -60% | -56% |
| Mean-reversion model ≥ 2% | 2716 | 20 | -20% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1835 | 16 | -3% | -82% | -82% | -76% |
| Mean-reversion model ≥ 10% | 1212 | 12 | +14% | -80% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 8051 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3133 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1095 | 2% | 2% | 2% | 1% | 1% | 0% |
| **All** | 12279 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 50 | 0% | -$791.45 | -53% | — |
| Sell at 2¢ | 423 | 3% | -$1,339.47 | -90% | 33 sec |
| Sell at 3¢ | 279 | 2% | -$1,340.64 | -90% | 47 sec |
| Sell at 5¢ | 205 | 2% | -$1,316.20 | -88% | 50 sec |
| Sell at 10¢ | 134 | 1% | -$1,259.91 | -84% | 64 sec |
| Sell at 25¢ | 77 | 1% | -$1,152.58 | -77% | 81 sec |
| Sell at 50¢ | 50 | 0% | -$1,027.95 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 350 | 4 | 11% | 3% | +9% | -81% | -85% |
| 2–5 min | 3998 | 25 | 6% | 3% | -39% | -88% | -89% |
| 1–2 min | 3206 | 13 | 3% | 2% | -56% | -94% | -94% |
| Under 1 min | 4721 | 8 | 1% | 0% | -75% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 902 | 6 | 4% | 3% | -20% | -90% | -90% |
| HYPE | 900 | 3 | 5% | 2% | -59% | -89% | -88% |
| DOGE | 897 | 2 | 3% | 2% | -72% | -92% | -91% |
| ETH | 896 | 7 | 5% | 3% | -4% | -89% | -88% |
| BNB | 896 | 3 | 4% | 2% | -60% | -91% | -92% |
| NEAR | 892 | 5 | 6% | 2% | -27% | -72% | -73% |
| SOL | 890 | 0 | 3% | 1% | -100% | -94% | -92% |
| BTC | 889 | 4 | 5% | 2% | -41% | -87% | -90% |
| XRP | 889 | 6 | 2% | 1% | -16% | -82% | -82% |
| GOLD | 523 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 509 | 0 | 3% | 1% | -100% | -94% | -94% |
| WTI | 484 | 3 | 3% | 1% | -31% | -94% | -96% |
| COPPER | 445 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 408 | 0 | 0% | 0% | -100% | -100% | -99% |
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
| UP (bought YES) | 6238 | 26 | 4% | 2% | -52% | -89% | -88% |
| DOWN (bought NO) | 6041 | 24 | 3% | 2% | -54% | -91% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1301 | 8 | 2% | 1% | +6% | -68% | -67% |
| 0.05–0.1% | 1350 | 4 | 3% | 1% | -56% | -92% | -92% |
| 0.1–0.2% | 2041 | 7 | 4% | 2% | -57% | -91% | -92% |
| 0.2–0.5% | 2360 | 12 | 5% | 3% | -44% | -89% | -88% |
| Over 0.5% | 997 | 5 | 6% | 2% | -48% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3090 | 17 | 4% | 2% | -37% | -85% | -85% |
| Morning (6am–12pm) | 3025 | 17 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 2853 | 8 | 3% | 1% | -67% | -89% | -90% |
| Evening (6pm–12am) | 3311 | 8 | 3% | 1% | -72% | -94% | -94% |

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
| 10/8 6:59:42 PM | AUDUSD | DOWN | 18 sec | — | 0¢ | In play | — |
| 10/8 6:59:42 PM | DOGE | UP | 18 sec | -0.033% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 6:59:42 PM | XRP | UP | 18 sec | -0.050% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 6:59:26 PM | BTC | UP | 34 sec | -0.031% | 0¢ | In play | — |
| 10/8 6:59:10 PM | ETH | UP | 50 sec | -0.125% | 0¢ | ❌ Lost | $0.00 |
| 10/8 6:59:10 PM | USDJPY | UP | 50 sec | — | 0¢ | In play | — |
| 10/8 6:59:10 PM | GOLD | UP | 50 sec | — | 0¢ | In play | — |
| 10/8 6:59:10 PM | WTI | DOWN | 50 sec | — | 1¢ | In play | — |
| 10/8 6:58:55 PM | BNB | UP | 64 sec | -0.128% | 1¢ | In play | — |
| 10/8 6:58:40 PM | GBPUSD | DOWN | 79 sec | — | 1¢ | In play | — |
| 10/8 6:58:24 PM | ZEC | UP | 1.6 min | -0.318% | 0¢ | ❌ Lost | $0.00 |
| 10/8 6:58:24 PM | EURUSD | DOWN | 1.6 min | — | 0¢ | In play | — |
| 10/8 6:57:52 PM | HYPE | DOWN | 2.1 min | +0.148% | 13¢ | In play | — |
| 10/8 6:56:16 PM | NEAR | DOWN | 3.7 min | +0.733% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 6:56:00 PM | SOL | DOWN | 4.0 min | +0.328% | 1¢ | In play | — |
| 10/8 6:44:57 PM | COPPER | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 6:44:57 PM | SILVER | DOWN | 2 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/8 6:44:57 PM | BNB | DOWN | 2 sec | -0.022% | 0¢ | ❌ Lost | $0.00 |
| 10/8 6:44:57 PM | WTI | UP | 2 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/8 6:43:54 PM | ETH | DOWN | 65 sec | +0.088% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 6:43:38 PM | ZEC | DOWN | 81 sec | +0.294% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 6:43:22 PM | SOL | DOWN | 1.6 min | +0.236% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 6:43:22 PM | BTC | DOWN | 1.6 min | +0.133% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 6:43:22 PM | XRP | DOWN | 1.6 min | +0.224% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 6:42:51 PM | DOGE | DOWN | 2.1 min | +0.165% | 2¢ | ❌ Lost | $0.00 |
| 10/8 6:42:35 PM | HYPE | DOWN | 2.4 min | +0.231% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 6:42:19 PM | PLATINUM | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 6:41:47 PM | GOLD | DOWN | 3.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 6:41:15 PM | NEAR | DOWN | 3.8 min | +0.824% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 6:29:53 PM | WTI | UP | 6 sec | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
