# 15-Minute 1¢ Study

*Updated Sun Nov 8, 10:52 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4066 finished bets | 1% | $191.90 | +42% | +4.72¢ | $93.85 / $98.05 |

*Expect about **97 buys a day** (~$14.53/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3772 | $109.70 | +27% |
| Volatility model ≥ 2%, hold to the close | 7445 | $83.90 | +9% |
| Momentum model ≥ 2%, hold to the close | 6144 | $8.10 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 50332 | 50315 | 186 (0%) | 1.07% | -$3,516.15 (-57%) | Hold to the close: -$3,516.15 (-57%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 30800 | 4.8% | 0.4% (121) | -691% | ❌ Worse |
| Momentum model | 30800 | 4.6% | 0.4% (121) | -717% | ❌ Worse |
| Mean-reversion model | 30800 | 8.1% | 0.4% (121) | -835% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 30800 | 121 | -50% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7445 | 70 | +9% | -76% | -75% | -71% |
| Volatility model ≥ 5% | 4066 | 46 | +42% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2339 | 28 | +71% | -61% | -59% | -56% |
| Momentum model ≥ 2% | 6144 | 51 | +1% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3772 | 37 | +27% | -73% | -73% | -69% |
| Momentum model ≥ 10% | 2473 | 25 | +42% | -64% | -64% | -59% |
| Mean-reversion model ≥ 2% | 12734 | 89 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 8929 | 77 | -4% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 5970 | 56 | +7% | -76% | -76% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31005 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11833 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7477 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 50315 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 186 | 0% | -$3,516.15 | -57% | — |
| Sell at 2¢ | 1976 | 4% | -$5,326.39 | -87% | 47 sec |
| Sell at 3¢ | 1346 | 3% | -$5,315.21 | -87% | 48 sec |
| Sell at 5¢ | 940 | 2% | -$5,201.15 | -85% | 63 sec |
| Sell at 10¢ | 566 | 1% | -$4,986.69 | -81% | 65 sec |
| Sell at 25¢ | 296 | 1% | -$4,636.39 | -76% | 83 sec |
| Sell at 50¢ | 190 | 0% | -$4,235.65 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2491 | 12 | 11% | 4% | -54% | -81% | -82% |
| 2–5 min | 16241 | 87 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 12705 | 41 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 18866 | 46 | 1% | 0% | -65% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3475 | 13 | 5% | 2% | -51% | -88% | -88% |
| SOL | 3468 | 15 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3459 | 11 | 5% | 2% | -60% | -89% | -88% |
| BNB | 3452 | 18 | 5% | 2% | -34% | -86% | -85% |
| DOGE | 3451 | 7 | 4% | 2% | -74% | -90% | -90% |
| ETH | 3444 | 14 | 7% | 3% | -50% | -81% | -81% |
| NEAR | 3424 | 16 | 5% | 2% | -40% | -85% | -85% |
| BTC | 3421 | 16 | 5% | 2% | -36% | -88% | -89% |
| XRP | 3411 | 13 | 3% | 1% | -52% | -89% | -89% |
| GOLD | 1803 | 5 | 6% | 2% | -66% | -81% | -83% |
| WTI | 1774 | 6 | 4% | 1% | -59% | -92% | -92% |
| SILVER | 1756 | 8 | 5% | 2% | -46% | -82% | -82% |
| PLATINUM | 1586 | 4 | 2% | 1% | -76% | -96% | -96% |
| EURUSD | 1524 | 4 | 2% | 1% | -76% | -90% | -89% |
| COPPER | 1489 | 6 | 2% | 1% | -62% | -72% | -72% |
| NATGAS | 1451 | 8 | 2% | 1% | -49% | -77% | -76% |
| GBPUSD | 1445 | 4 | 2% | 1% | -74% | -96% | -96% |
| PALLADIUM | 1428 | 3 | 1% | 0% | -80% | -92% | -92% |
| USDJPY | 1428 | 5 | 2% | 1% | -67% | -97% | -96% |
| AUDUSD | 983 | 5 | 2% | 1% | -53% | -87% | -87% |
| USDCAD | 953 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 546 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 303 | 1 | 4% | 1% | -69% | -62% | -60% |
| 2YRRATE | 287 | 3 | 4% | 1% | -2% | -28% | -27% |
| 30YRRATE | 285 | 0 | 2% | 1% | -100% | -96% | -95% |
| 5YRRATE | 262 | 1 | 4% | 2% | -64% | -93% | -95% |
| INX | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 25515 | 95 | 4% | 2% | -57% | -88% | -87% |
| DOWN (bought NO) | 24800 | 91 | 4% | 2% | -58% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5044 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5319 | 19 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 7984 | 27 | 4% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 9200 | 38 | 6% | 3% | -54% | -87% | -86% |
| Over 0.5% | 3450 | 14 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12179 | 42 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12223 | 54 | 4% | 2% | -50% | -84% | -84% |
| Afternoon (12–6pm) | 12200 | 47 | 4% | 2% | -55% | -86% | -86% |
| Evening (6pm–12am) | 13713 | 43 | 3% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,947 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/8 10:44:48 PM | NEAR | DOWN | 12 sec | -0.028% | 0¢ | ❌ Lost | $0.00 |
| 11/8 10:44:48 PM | HYPE | DOWN | 12 sec | -0.007% | 0¢ | ❌ Lost | $0.00 |
| 11/8 10:44:32 PM | PALLADIUM | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 10:44:17 PM | WTI | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 10:44:17 PM | GBPUSD | UP | 42 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/8 10:43:59 PM | BRENT | UP | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 10:43:43 PM | USDCAD | DOWN | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 10:43:43 PM | COPPER | DOWN | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 10:43:43 PM | ETH | UP | 77 sec | -0.164% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 10:42:38 PM | ZEC | DOWN | 2.4 min | +0.532% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 10:42:07 PM | SOL | UP | 2.9 min | -0.317% | 6¢ | ❌ Lost | -$0.15 |
| 11/8 10:41:26 PM | XRP | UP | 3.6 min | -0.463% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 10:41:26 PM | DOGE | UP | 3.6 min | -0.323% | 7¢ | ❌ Lost | -$0.15 |
| 11/8 10:41:26 PM | BNB | UP | 3.6 min | -0.226% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 10:41:26 PM | BTC | UP | 3.6 min | -0.274% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 10:40:55 PM | SILVER | UP | 4.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/8 10:40:39 PM | USDJPY | DOWN | 4.3 min | — | 2¢ | ❌ Lost | -$0.15 |
| 11/8 10:29:48 PM | PALLADIUM | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 10:29:32 PM | PLATINUM | DOWN | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 10:29:16 PM | WTI | UP | 44 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/8 10:29:16 PM | COPPER | DOWN | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 10:29:16 PM | SILVER | DOWN | 44 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/8 10:28:41 PM | GBPUSD | DOWN | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 10:28:41 PM | USDCAD | UP | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 10:28:10 PM | ZEC | UP | 1.8 min | -0.416% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 10:28:10 PM | SOL | UP | 1.8 min | -0.250% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 10:28:10 PM | XRP | UP | 1.8 min | -0.299% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 10:28:10 PM | BTC | UP | 1.8 min | -0.152% | 0¢ | ❌ Lost | $0.00 |
| 11/8 10:28:10 PM | HYPE | UP | 1.8 min | -0.339% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 10:27:53 PM | DOGE | UP | 2.1 min | -0.278% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
