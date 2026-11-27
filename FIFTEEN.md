# 15-Minute 1¢ Study

*Updated Thu Nov 26, 6:16 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4966 finished bets | 1% | $202.30 | +37% | +4.07¢ | $96.90 / $105.40 |

*Expect about **83 buys a day** (~$12.46/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4710 | $101.75 | +20% |
| Volatility model ≥ 2%, hold to the close | 9263 | $32.10 | +3% |
| Momentum model ≥ 2%, hold to the close | 7714 | -$47.90 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 68775 | 68741 | 257 (0%) | 1.07% | -$4,723.55 (-57%) | Hold to the close: -$4,723.55 (-57%) |

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
| Volatility model | 40637 | 4.5% | 0.4% (165) | -658% | ❌ Worse |
| Momentum model | 40637 | 4.4% | 0.4% (165) | -681% | ❌ Worse |
| Mean-reversion model | 40637 | 7.9% | 0.4% (165) | -797% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 40637 | 165 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 9263 | 81 | +3% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 4966 | 53 | +37% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 2878 | 32 | +65% | -65% | -63% | -60% |
| Momentum model ≥ 2% | 7714 | 59 | -5% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 4710 | 43 | +20% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 3068 | 28 | +32% | -68% | -68% | -64% |
| Mean-reversion model ≥ 2% | 16563 | 113 | -25% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11530 | 93 | -10% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7652 | 66 | -1% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 40843 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 16422 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 11476 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 68741 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 257 | 0% | -$4,723.55 | -57% | — |
| Sell at 2¢ | 2820 | 4% | -$7,280.35 | -87% | 47 sec |
| Sell at 3¢ | 1893 | 3% | -$7,275.28 | -87% | 48 sec |
| Sell at 5¢ | 1282 | 2% | -$7,152.25 | -86% | 62 sec |
| Sell at 10¢ | 784 | 1% | -$6,874.51 | -83% | 65 sec |
| Sell at 25¢ | 425 | 1% | -$6,340.80 | -76% | 80 sec |
| Sell at 50¢ | 271 | 0% | -$5,736.30 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3550 | 17 | 11% | 4% | -55% | -81% | -83% |
| 2–5 min | 22304 | 116 | 7% | 3% | -49% | -86% | -86% |
| 1–2 min | 17114 | 58 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 25760 | 66 | 1% | 0% | -63% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4569 | 20 | 5% | 2% | -41% | -88% | -87% |
| HYPE | 4562 | 16 | 5% | 2% | -55% | -89% | -88% |
| SOL | 4552 | 20 | 5% | 2% | -43% | -86% | -86% |
| DOGE | 4545 | 12 | 4% | 2% | -66% | -89% | -89% |
| BNB | 4545 | 22 | 5% | 2% | -38% | -86% | -85% |
| ETH | 4538 | 19 | 7% | 3% | -47% | -82% | -82% |
| BTC | 4517 | 24 | 5% | 2% | -27% | -86% | -88% |
| NEAR | 4512 | 18 | 5% | 2% | -48% | -86% | -86% |
| XRP | 4503 | 16 | 4% | 2% | -55% | -89% | -88% |
| GOLD | 2423 | 8 | 5% | 2% | -60% | -82% | -84% |
| WTI | 2412 | 9 | 4% | 2% | -54% | -86% | -87% |
| SILVER | 2372 | 9 | 5% | 2% | -54% | -83% | -83% |
| PLATINUM | 2150 | 5 | 3% | 1% | -78% | -95% | -95% |
| EURUSD | 2101 | 7 | 2% | 1% | -69% | -91% | -90% |
| GBPUSD | 2047 | 8 | 2% | 1% | -64% | -96% | -96% |
| COPPER | 2036 | 6 | 2% | 1% | -72% | -79% | -79% |
| USDJPY | 1997 | 6 | 2% | 1% | -72% | -97% | -96% |
| NATGAS | 1989 | 10 | 2% | 1% | -53% | -77% | -77% |
| PALLADIUM | 1936 | 4 | 1% | 1% | -81% | -93% | -93% |
| AUDUSD | 1569 | 7 | 2% | 1% | -58% | -90% | -90% |
| USDCAD | 1476 | 1 | 3% | 1% | -94% | -96% | -96% |
| BRENT | 1104 | 1 | 2% | 1% | -92% | -96% | -96% |
| 10YRRATE | 557 | 2 | 3% | 1% | -66% | -78% | -76% |
| 30YRRATE | 518 | 0 | 3% | 1% | -100% | -95% | -93% |
| 2YRRATE | 515 | 4 | 4% | 2% | -28% | -57% | -57% |
| 5YRRATE | 506 | 2 | 4% | 2% | -63% | -94% | -95% |
| INX | 139 | 1 | 2% | 1% | -33% | -96% | -96% |
| USDMXN | 51 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 35060 | 133 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 33681 | 124 | 4% | 2% | -57% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5917 | 25 | 2% | 1% | -22% | -79% | -78% |
| 0.05–0.1% | 6494 | 26 | 3% | 2% | -36% | -91% | -91% |
| 0.1–0.2% | 10114 | 36 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 12885 | 56 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 5424 | 24 | 7% | 3% | -54% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16499 | 51 | 4% | 2% | -65% | -87% | -88% |
| Morning (6am–12pm) | 16354 | 82 | 4% | 2% | -43% | -86% | -85% |
| Afternoon (12–6pm) | 16940 | 73 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 18948 | 51 | 4% | 2% | -69% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,081 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/26 6:14:57 PM | USDJPY | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 6:14:25 PM | HYPE | DOWN | 34 sec | +0.093% | 0¢ | ❌ Lost | $0.00 |
| 11/26 6:13:54 PM | ETH | DOWN | 66 sec | +0.077% | 8¢ | ❌ Lost | -$0.15 |
| 11/26 6:13:54 PM | EURUSD | DOWN | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 6:13:07 PM | WTI | DOWN | 1.9 min | — | 0¢ | ❌ Lost | $0.00 |
| 11/26 6:12:51 PM | ZEC | DOWN | 2.1 min | +0.494% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 6:12:51 PM | COPPER | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 6:12:35 PM | NEAR | DOWN | 2.4 min | +0.352% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 6:12:19 PM | XRP | DOWN | 2.7 min | +0.169% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 6:12:03 PM | USDMXN | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 6:12:03 PM | BTC | DOWN | 2.9 min | +0.211% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 6:11:31 PM | BNB | DOWN | 3.5 min | +0.059% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 6:11:31 PM | PALLADIUM | DOWN | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 6:11:31 PM | SOL | DOWN | 3.5 min | +0.233% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 6:11:31 PM | USDCAD | UP | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 6:11:31 PM | GBPUSD | DOWN | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 6:11:15 PM | PLATINUM | DOWN | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 6:11:15 PM | GOLD | DOWN | 3.8 min | — | 4¢ | ❌ Lost | -$0.15 |
| 11/26 6:10:43 PM | SILVER | DOWN | 4.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/26 6:10:27 PM | DOGE | DOWN | 4.5 min | +0.288% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 6:10:11 PM | NATGAS | UP | 4.8 min | — | 64¢ | ❌ Lost | -$0.15 |
| 11/26 6:10:11 PM | AUDUSD | DOWN | 4.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 6:09:21 PM | BRENT | DOWN | 5.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/26 5:59:49 PM | HYPE | DOWN | 11 sec | -0.028% | 0¢ | ❌ Lost | $0.00 |
| 11/26 5:59:49 PM | USDJPY | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 5:59:49 PM | BRENT | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 5:59:33 PM | XRP | DOWN | 27 sec | +0.064% | 0¢ | ❌ Lost | $0.00 |
| 11/26 5:59:33 PM | DOGE | UP | 27 sec | -0.071% | 0¢ | ❌ Lost | $0.00 |
| 11/26 5:59:33 PM | NATGAS | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 5:59:33 PM | BTC | UP | 27 sec | -0.055% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
