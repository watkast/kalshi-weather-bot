# 15-Minute 1¢ Study

*Updated Fri Oct 30, 2:21 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3185 finished bets | 1% | $91.90 | +26% | +2.89¢ | $75.00 / $16.90 |

*Expect about **98 buys a day** (~$14.67/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2953 | $41.35 | +13% |
| Volatility model ≥ 2%, hold to the close | 5911 | $11.30 | +2% |
| Momentum model ≥ 2%, hold to the close | 4877 | -$61.05 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 39907 | 39897 | 148 (0%) | 1.07% | -$2,801.80 (-57%) | Hold to the close: -$2,801.80 (-57%) |

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
| Volatility model | 24357 | 4.6% | 0.4% (95) | -681% | ❌ Worse |
| Momentum model | 24357 | 4.5% | 0.4% (95) | -703% | ❌ Worse |
| Mean-reversion model | 24357 | 8.0% | 0.4% (95) | -829% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 24357 | 95 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5911 | 52 | +2% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3185 | 32 | +26% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1798 | 19 | +51% | -69% | -67% | -64% |
| Momentum model ≥ 2% | 4877 | 36 | -11% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2953 | 26 | +13% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1922 | 17 | +23% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9998 | 66 | -28% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7002 | 56 | -11% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4666 | 39 | -5% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 24558 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9668 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5671 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 39897 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 148 | 0% | -$2,801.80 | -57% | — |
| Sell at 2¢ | 1535 | 4% | -$4,250.70 | -87% | 47 sec |
| Sell at 3¢ | 1057 | 3% | -$4,237.57 | -87% | 49 sec |
| Sell at 5¢ | 736 | 2% | -$4,157.40 | -85% | 63 sec |
| Sell at 10¢ | 443 | 1% | -$3,985.47 | -82% | 65 sec |
| Sell at 25¢ | 231 | 1% | -$3,689.19 | -76% | 83 sec |
| Sell at 50¢ | 150 | 0% | -$3,357.30 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1861 | 8 | 11% | 4% | -59% | -80% | -81% |
| 2–5 min | 12714 | 70 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10107 | 35 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 15204 | 35 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2748 | 13 | 5% | 3% | -39% | -88% | -88% |
| HYPE | 2742 | 8 | 5% | 3% | -64% | -89% | -87% |
| BNB | 2741 | 16 | 5% | 3% | -27% | -85% | -83% |
| SOL | 2736 | 7 | 4% | 2% | -68% | -91% | -91% |
| DOGE | 2729 | 6 | 4% | 2% | -72% | -90% | -89% |
| ETH | 2728 | 11 | 6% | 3% | -51% | -86% | -85% |
| BTC | 2712 | 13 | 5% | 2% | -35% | -88% | -89% |
| NEAR | 2711 | 12 | 5% | 2% | -42% | -83% | -83% |
| XRP | 2711 | 11 | 3% | 1% | -50% | -89% | -89% |
| GOLD | 1512 | 5 | 5% | 2% | -60% | -82% | -84% |
| SILVER | 1478 | 7 | 4% | 2% | -44% | -82% | -81% |
| WTI | 1457 | 4 | 3% | 1% | -67% | -93% | -93% |
| PLATINUM | 1312 | 3 | 2% | 1% | -79% | -96% | -96% |
| COPPER | 1251 | 5 | 1% | 1% | -63% | -75% | -75% |
| EURUSD | 1247 | 3 | 2% | 1% | -78% | -88% | -88% |
| NATGAS | 1207 | 7 | 2% | 1% | -46% | -81% | -80% |
| GBPUSD | 1184 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1177 | 2 | 1% | 0% | -84% | -90% | -91% |
| USDJPY | 1168 | 5 | 2% | 1% | -60% | -97% | -96% |
| AUDUSD | 704 | 4 | 2% | 1% | -47% | -84% | -83% |
| USDCAD | 683 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 274 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 186 | 1 | 5% | 2% | -50% | -41% | -39% |
| 30YRRATE | 175 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 169 | 2 | 5% | 1% | +10% | +19% | +20% |
| 5YRRATE | 155 | 1 | 6% | 3% | -40% | -89% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 20276 | 81 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 19621 | 67 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3914 | 19 | 2% | 1% | -16% | -81% | -81% |
| 0.05–0.1% | 4161 | 14 | 3% | 2% | -49% | -92% | -92% |
| 0.1–0.2% | 6304 | 22 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 7338 | 32 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2837 | 10 | 7% | 3% | -64% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9916 | 36 | 4% | 2% | -59% | -86% | -86% |
| Morning (6am–12pm) | 10122 | 46 | 4% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 9279 | 32 | 4% | 2% | -60% | -87% | -87% |
| Evening (6pm–12am) | 10580 | 34 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,449 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/30 2:14:47 PM | XRP | UP | 13 sec | -0.064% | 0¢ | ❌ Lost | $0.00 |
| 10/30 2:14:47 PM | ZEC | UP | 13 sec | +0.036% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 2:14:47 PM | GOLD | UP | 13 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/30 2:14:31 PM | PALLADIUM | UP | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 2:14:31 PM | BNB | DOWN | 29 sec | +0.021% | 0¢ | ❌ Lost | $0.00 |
| 10/30 2:14:16 PM | NEAR | UP | 44 sec | -0.376% | 0¢ | ❌ Lost | $0.00 |
| 10/30 2:14:16 PM | SOL | DOWN | 44 sec | +0.133% | 0¢ | ❌ Lost | $0.00 |
| 10/30 2:14:16 PM | BTC | DOWN | 44 sec | +0.068% | 0¢ | ❌ Lost | $0.00 |
| 10/30 2:14:16 PM | NATGAS | UP | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 2:13:57 PM | DOGE | DOWN | 63 sec | +0.118% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 2:13:57 PM | ETH | DOWN | 63 sec | +0.085% | 0¢ | ❌ Lost | $0.00 |
| 10/30 2:13:41 PM | USDCAD | UP | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 2:13:25 PM | WTI | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/30 2:13:25 PM | BRENT | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 2:12:53 PM | SILVER | UP | 2.1 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/30 2:12:21 PM | HYPE | UP | 2.6 min | -0.469% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 2:12:04 PM | 2YRRATE | DOWN | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 2:08:31 PM | 5YRRATE | DOWN | 6.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 2:08:15 PM | 10YRRATE | DOWN | 6.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 2:08:15 PM | 30YRRATE | DOWN | 6.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 1:59:47 PM | NATGAS | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 1:59:31 PM | XRP | DOWN | 29 sec | +0.080% | 0¢ | ❌ Lost | $0.00 |
| 10/30 1:59:31 PM | 2YRRATE | DOWN | 29 sec | — | 0¢ | ✅ Won | $13.85 |
| 10/30 1:59:31 PM | HYPE | DOWN | 29 sec | +0.099% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 1:59:31 PM | GBPUSD | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 1:59:16 PM | WTI | DOWN | 44 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/30 1:58:43 PM | NEAR | DOWN | 76 sec | +0.550% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 1:58:27 PM | AUDUSD | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 1:58:10 PM | ETH | DOWN | 1.8 min | +0.241% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 1:56:16 PM | ZEC | DOWN | 3.7 min | +0.702% | 4¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
