# 15-Minute 1¢ Study

*Updated Thu Nov 26, 4:12 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4954 finished bets | 1% | $203.05 | +38% | +4.10¢ | $83.80 / $119.25 |

*Expect about **83 buys a day** (~$12.45/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4702 | $101.90 | +20% |
| Volatility model ≥ 2%, hold to the close | 9238 | $34.65 | +3% |
| Momentum model ≥ 2%, hold to the close | 7695 | -$46.40 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 68632 | 68591 | 257 (0%) | 1.07% | -$4,706.60 (-57%) | Hold to the close: -$4,706.60 (-57%) |

*In play or awaiting result: 13. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 40560 | 4.5% | 0.4% (165) | -655% | ❌ Worse |
| Momentum model | 40560 | 4.4% | 0.4% (165) | -678% | ❌ Worse |
| Mean-reversion model | 40560 | 7.9% | 0.4% (165) | -794% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 40560 | 165 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 9238 | 81 | +3% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 4954 | 53 | +38% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 2871 | 32 | +65% | -65% | -63% | -60% |
| Momentum model ≥ 2% | 7695 | 59 | -5% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 4702 | 43 | +20% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 3062 | 28 | +32% | -68% | -68% | -64% |
| Mean-reversion model ≥ 2% | 16531 | 113 | -25% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11507 | 93 | -10% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 7636 | 66 | -1% | -78% | -78% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 40766 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 16381 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 11444 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 68591 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 257 | 0% | -$4,706.60 | -57% | — |
| Sell at 2¢ | 2807 | 4% | -$7,266.78 | -88% | 47 sec |
| Sell at 3¢ | 1882 | 3% | -$7,262.62 | -87% | 48 sec |
| Sell at 5¢ | 1274 | 2% | -$7,140.50 | -86% | 62 sec |
| Sell at 10¢ | 780 | 1% | -$6,862.80 | -83% | 65 sec |
| Sell at 25¢ | 422 | 1% | -$6,333.78 | -76% | 80 sec |
| Sell at 50¢ | 269 | 0% | -$5,732.85 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3547 | 17 | 11% | 4% | -55% | -81% | -83% |
| 2–5 min | 22246 | 116 | 7% | 3% | -49% | -86% | -86% |
| 1–2 min | 17086 | 58 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 25699 | 66 | 1% | 0% | -63% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4560 | 20 | 5% | 2% | -41% | -88% | -87% |
| HYPE | 4553 | 16 | 5% | 2% | -54% | -89% | -88% |
| SOL | 4544 | 20 | 4% | 2% | -43% | -86% | -86% |
| BNB | 4538 | 22 | 5% | 2% | -38% | -86% | -85% |
| DOGE | 4536 | 12 | 4% | 2% | -66% | -89% | -89% |
| ETH | 4529 | 19 | 7% | 3% | -47% | -82% | -82% |
| BTC | 4508 | 24 | 6% | 2% | -27% | -86% | -87% |
| NEAR | 4504 | 18 | 5% | 2% | -48% | -86% | -86% |
| XRP | 4494 | 16 | 4% | 2% | -54% | -89% | -88% |
| GOLD | 2420 | 8 | 5% | 2% | -59% | -83% | -84% |
| WTI | 2404 | 9 | 4% | 2% | -54% | -86% | -87% |
| SILVER | 2365 | 9 | 5% | 2% | -54% | -83% | -83% |
| PLATINUM | 2145 | 5 | 3% | 1% | -78% | -95% | -95% |
| EURUSD | 2096 | 7 | 2% | 1% | -69% | -91% | -90% |
| GBPUSD | 2042 | 8 | 2% | 1% | -63% | -96% | -96% |
| COPPER | 2031 | 6 | 2% | 1% | -72% | -79% | -79% |
| USDJPY | 1991 | 6 | 2% | 1% | -72% | -97% | -96% |
| NATGAS | 1986 | 10 | 2% | 1% | -53% | -77% | -77% |
| PALLADIUM | 1931 | 4 | 1% | 1% | -81% | -93% | -93% |
| AUDUSD | 1562 | 7 | 2% | 1% | -58% | -90% | -90% |
| USDCAD | 1469 | 1 | 3% | 1% | -94% | -96% | -96% |
| BRENT | 1099 | 1 | 2% | 1% | -92% | -96% | -96% |
| 10YRRATE | 557 | 2 | 3% | 1% | -66% | -78% | -76% |
| 30YRRATE | 518 | 0 | 3% | 1% | -100% | -95% | -93% |
| 2YRRATE | 515 | 4 | 4% | 2% | -28% | -57% | -57% |
| 5YRRATE | 506 | 2 | 4% | 2% | -63% | -94% | -95% |
| INX | 139 | 1 | 2% | 1% | -33% | -96% | -96% |
| USDMXN | 49 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 35004 | 133 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 33587 | 124 | 4% | 2% | -57% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5905 | 25 | 2% | 1% | -22% | -79% | -78% |
| 0.05–0.1% | 6477 | 26 | 3% | 2% | -36% | -91% | -91% |
| 0.1–0.2% | 10099 | 36 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 12858 | 56 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 5418 | 24 | 7% | 3% | -54% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16499 | 51 | 4% | 2% | -65% | -87% | -88% |
| Morning (6am–12pm) | 16354 | 82 | 4% | 2% | -43% | -86% | -85% |
| Afternoon (12–6pm) | 16813 | 73 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 18925 | 51 | 4% | 2% | -69% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,080 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/26 4:12:12 PM | HYPE | UP | 2.8 min | -0.352% | — | In play | — |
| 11/26 4:12:12 PM | ETH | UP | 2.8 min | -0.322% | — | In play | — |
| 11/26 4:11:56 PM | USDJPY | DOWN | 3.1 min | — | — | In play | — |
| 11/26 4:11:40 PM | NEAR | UP | 3.3 min | -0.673% | — | In play | — |
| 11/26 4:10:20 PM | DOGE | UP | 4.7 min | -0.450% | — | In play | — |
| 11/26 4:09:48 PM | XRP | UP | 5.2 min | -0.423% | — | In play | — |
| 11/26 4:09:32 PM | ZEC | UP | 5.5 min | -1.809% | — | In play | — |
| 11/26 3:58:46 PM | DOGE | UP | 73 sec | -0.186% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 3:57:58 PM | NEAR | UP | 2.0 min | -0.440% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 3:57:10 PM | BTC | UP | 2.8 min | -0.247% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 3:56:54 PM | HYPE | UP | 3.1 min | -0.383% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 3:56:38 PM | XRP | UP | 3.4 min | -0.285% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 3:56:06 PM | ETH | UP | 3.9 min | -0.385% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 3:56:06 PM | SOL | UP | 3.9 min | -0.417% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 3:55:50 PM | BNB | UP | 4.2 min | -0.222% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 3:55:02 PM | ZEC | UP | 5.0 min | -1.072% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 3:44:55 PM | AUDUSD | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 3:44:39 PM | ZEC | DOWN | 20 sec | +0.188% | 0¢ | ❌ Lost | $0.00 |
| 11/26 3:44:39 PM | ETH | UP | 20 sec | -0.024% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 3:44:23 PM | NEAR | UP | 36 sec | -0.098% | 0¢ | ❌ Lost | -$0.15 |
| 11/26 3:44:07 PM | BNB | UP | 52 sec | -0.070% | 0¢ | ❌ Lost | -$0.15 |
| 11/26 3:43:51 PM | HYPE | UP | 68 sec | -0.187% | 0¢ | ❌ Lost | $0.00 |
| 11/26 3:43:35 PM | DOGE | UP | 84 sec | -0.111% | 3¢ | ❌ Lost | -$0.15 |
| 11/26 3:43:19 PM | EURUSD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 3:42:15 PM | XRP | UP | 2.7 min | -0.200% | 2¢ | ❌ Lost | -$0.15 |
| 11/26 3:29:28 PM | EURUSD | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 3:29:13 PM | NATGAS | DOWN | 46 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/26 3:28:57 PM | DOGE | DOWN | 62 sec | +0.104% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 3:28:41 PM | ETH | DOWN | 78 sec | +0.103% | 0¢ | ❌ Lost | -$0.15 |
| 11/26 3:28:25 PM | BTC | DOWN | 1.6 min | +0.105% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
