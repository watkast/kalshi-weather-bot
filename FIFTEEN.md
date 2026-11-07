# 15-Minute 1¢ Study

*Updated Fri Nov 6, 7:51 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3824 finished bets | 1% | $121.95 | +29% | +3.19¢ | $80.40 / $41.55 |

*Expect about **96 buys a day** (~$14.40/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3553 | $50.90 | +13% |
| Volatility model ≥ 2%, hold to the close | 7054 | $19.60 | +2% |
| Momentum model ≥ 2%, hold to the close | 5820 | -$51.50 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 48445 | 48428 | 175 (0%) | 1.07% | -$3,454.45 (-59%) | Hold to the close: -$3,454.45 (-59%) |

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
| Volatility model | 29194 | 4.7% | 0.4% (111) | -701% | ❌ Worse |
| Momentum model | 29194 | 4.6% | 0.4% (111) | -727% | ❌ Worse |
| Mean-reversion model | 29194 | 8.1% | 0.4% (111) | -850% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 29194 | 111 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 7054 | 62 | +2% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3824 | 39 | +29% | -77% | -75% | -72% |
| Volatility model ≥ 10% | 2189 | 24 | +58% | -72% | -70% | -67% |
| Momentum model ≥ 2% | 5820 | 44 | -8% | -82% | -81% | -78% |
| Momentum model ≥ 5% | 3553 | 31 | +13% | -80% | -79% | -75% |
| Momentum model ≥ 10% | 2322 | 20 | +22% | -75% | -75% | -71% |
| Mean-reversion model ≥ 2% | 12079 | 80 | -27% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8465 | 69 | -9% | -82% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5664 | 49 | -1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 29399 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11661 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7368 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 48428 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 175 | 0% | -$3,454.45 | -59% | — |
| Sell at 2¢ | 1902 | 4% | -$5,157.93 | -87% | 47 sec |
| Sell at 3¢ | 1296 | 3% | -$5,147.01 | -87% | 48 sec |
| Sell at 5¢ | 899 | 2% | -$5,040.10 | -85% | 63 sec |
| Sell at 10¢ | 541 | 1% | -$4,831.74 | -82% | 66 sec |
| Sell at 25¢ | 282 | 1% | -$4,495.03 | -76% | 83 sec |
| Sell at 50¢ | 180 | 0% | -$4,115.45 | -70% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2393 | 10 | 11% | 4% | -60% | -81% | -83% |
| 2–5 min | 15564 | 83 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 12198 | 40 | 3% | 1% | -64% | -92% | -92% |
| Under 1 min | 18261 | 42 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3295 | 13 | 5% | 2% | -49% | -88% | -88% |
| SOL | 3289 | 12 | 4% | 2% | -53% | -90% | -90% |
| HYPE | 3278 | 10 | 5% | 2% | -62% | -89% | -87% |
| BNB | 3278 | 17 | 5% | 2% | -34% | -85% | -84% |
| DOGE | 3268 | 6 | 4% | 2% | -77% | -90% | -90% |
| ETH | 3265 | 12 | 7% | 3% | -55% | -85% | -85% |
| NEAR | 3245 | 16 | 5% | 2% | -36% | -84% | -85% |
| BTC | 3243 | 15 | 5% | 2% | -37% | -88% | -89% |
| XRP | 3238 | 12 | 3% | 1% | -54% | -89% | -89% |
| GOLD | 1783 | 5 | 5% | 2% | -66% | -81% | -83% |
| WTI | 1747 | 6 | 4% | 1% | -59% | -92% | -92% |
| SILVER | 1733 | 8 | 5% | 2% | -45% | -82% | -81% |
| PLATINUM | 1567 | 4 | 2% | 1% | -76% | -96% | -96% |
| EURUSD | 1503 | 4 | 2% | 1% | -75% | -90% | -89% |
| COPPER | 1471 | 6 | 2% | 1% | -62% | -72% | -71% |
| NATGAS | 1431 | 8 | 2% | 1% | -48% | -77% | -76% |
| GBPUSD | 1426 | 4 | 2% | 1% | -74% | -96% | -96% |
| PALLADIUM | 1408 | 3 | 1% | 0% | -80% | -91% | -92% |
| USDJPY | 1406 | 5 | 2% | 1% | -67% | -97% | -96% |
| AUDUSD | 960 | 4 | 2% | 1% | -61% | -87% | -87% |
| USDCAD | 929 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 521 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 303 | 1 | 4% | 1% | -69% | -62% | -60% |
| 2YRRATE | 287 | 3 | 4% | 1% | -2% | -28% | -27% |
| 30YRRATE | 285 | 0 | 2% | 1% | -100% | -96% | -95% |
| 5YRRATE | 262 | 1 | 4% | 2% | -64% | -93% | -95% |
| INX | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 24555 | 94 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 23873 | 81 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4699 | 22 | 2% | 1% | -17% | -83% | -82% |
| 0.05–0.1% | 4987 | 18 | 3% | 2% | -45% | -91% | -91% |
| 0.1–0.2% | 7565 | 26 | 5% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 8799 | 34 | 6% | 3% | -57% | -87% | -86% |
| Over 0.5% | 3341 | 13 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11768 | 41 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11949 | 51 | 4% | 2% | -51% | -86% | -85% |
| Afternoon (12–6pm) | 11694 | 42 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 13017 | 41 | 3% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,647 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/6 7:44:43 PM | HYPE | UP | 16 sec | -0.057% | 0¢ | ❌ Lost | $0.00 |
| 11/6 7:44:43 PM | WTI | DOWN | 16 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/6 7:44:27 PM | SOL | UP | 32 sec | -0.066% | 0¢ | ❌ Lost | $0.00 |
| 11/6 7:44:27 PM | BTC | UP | 32 sec | -0.029% | 0¢ | ❌ Lost | $0.00 |
| 11/6 7:44:27 PM | BNB | DOWN | 32 sec | -0.007% | 0¢ | ❌ Lost | -$0.15 |
| 11/6 7:42:51 PM | ETH | UP | 2.1 min | -0.078% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 7:42:03 PM | XRP | UP | 2.9 min | -0.341% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 7:41:27 PM | DOGE | UP | 3.5 min | -0.232% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 7:41:11 PM | NEAR | UP | 3.8 min | -0.506% | 0¢ | ❌ Lost | -$0.15 |
| 11/6 7:28:49 PM | BTC | UP | 70 sec | -0.056% | 0¢ | ❌ Lost | $0.00 |
| 11/6 7:28:49 PM | HYPE | DOWN | 70 sec | +0.093% | 0¢ | ❌ Lost | -$0.15 |
| 11/6 7:28:01 PM | ETH | UP | 2.0 min | -0.085% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 7:27:28 PM | NEAR | UP | 2.5 min | -0.433% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 7:27:28 PM | BNB | UP | 2.5 min | -0.129% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 7:26:42 PM | SOL | UP | 3.3 min | -0.166% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 7:26:10 PM | DOGE | UP | 3.8 min | -0.187% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 7:25:04 PM | ZEC | UP | 4.9 min | -0.646% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 7:24:34 PM | XRP | UP | 5.4 min | -0.408% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 7:14:12 PM | XRP | DOWN | 48 sec | +0.043% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 7:13:56 PM | NATGAS | UP | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 7:13:40 PM | DOGE | DOWN | 79 sec | +0.055% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 7:13:24 PM | SOL | DOWN | 1.6 min | +0.075% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 7:12:52 PM | BTC | DOWN | 2.1 min | +0.076% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 7:12:52 PM | HYPE | DOWN | 2.1 min | +0.122% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 7:12:04 PM | NEAR | DOWN | 2.9 min | +0.376% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 7:12:04 PM | ETH | DOWN | 2.9 min | +0.147% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 7:11:00 PM | ZEC | DOWN | 4.0 min | +0.746% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 7:08:21 PM | BNB | DOWN | 6.7 min | +0.106% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 6:59:49 PM | WTI | UP | 11 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/6 6:59:49 PM | BNB | DOWN | 11 sec | -0.032% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
