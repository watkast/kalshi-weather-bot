# 15-Minute 1¢ Study

*Updated Tue Nov 3, 9:23 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3614 finished bets | 1% | $114.35 | +28% | +3.16¢ | $79.45 / $34.90 |

*Expect about **98 buys a day** (~$14.69/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3347 | $42.10 | +12% |
| Volatility model ≥ 2%, hold to the close | 6686 | $31.35 | +4% |
| Momentum model ≥ 2%, hold to the close | 5513 | -$48.60 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 44701 | 44691 | 165 (0%) | 1.07% | -$3,132.90 (-58%) | Hold to the close: -$3,132.90 (-58%) |

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
| Volatility model | 27450 | 4.7% | 0.4% (107) | -680% | ❌ Worse |
| Momentum model | 27450 | 4.6% | 0.4% (107) | -706% | ❌ Worse |
| Mean-reversion model | 27450 | 8.1% | 0.4% (107) | -829% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 27450 | 107 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6686 | 60 | +4% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3614 | 37 | +28% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2048 | 22 | +54% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5513 | 42 | -8% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 3347 | 29 | +12% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2181 | 19 | +22% | -74% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11353 | 77 | -26% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7973 | 66 | -8% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 5338 | 47 | -0% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 27655 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10583 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6453 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 44691 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 165 | 0% | -$3,132.90 | -58% | — |
| Sell at 2¢ | 1758 | 4% | -$4,747.82 | -87% | 47 sec |
| Sell at 3¢ | 1204 | 3% | -$4,735.34 | -87% | 49 sec |
| Sell at 5¢ | 834 | 2% | -$4,634.80 | -85% | 63 sec |
| Sell at 10¢ | 502 | 1% | -$4,435.28 | -81% | 66 sec |
| Sell at 25¢ | 263 | 1% | -$4,110.37 | -76% | 83 sec |
| Sell at 50¢ | 169 | 0% | -$3,742.15 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2172 | 9 | 11% | 4% | -61% | -81% | -82% |
| 2–5 min | 14378 | 79 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 11271 | 39 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 16859 | 38 | 1% | 0% | -68% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3098 | 13 | 5% | 3% | -46% | -88% | -88% |
| SOL | 3091 | 11 | 4% | 2% | -55% | -91% | -90% |
| BNB | 3085 | 17 | 5% | 2% | -31% | -85% | -84% |
| HYPE | 3084 | 9 | 5% | 2% | -64% | -89% | -87% |
| DOGE | 3072 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 3069 | 12 | 7% | 3% | -52% | -85% | -85% |
| NEAR | 3055 | 15 | 5% | 2% | -36% | -84% | -84% |
| BTC | 3055 | 14 | 5% | 2% | -38% | -88% | -89% |
| XRP | 3046 | 12 | 3% | 1% | -51% | -89% | -89% |
| GOLD | 1641 | 5 | 5% | 2% | -63% | -81% | -83% |
| WTI | 1598 | 5 | 3% | 1% | -62% | -92% | -93% |
| SILVER | 1597 | 7 | 5% | 2% | -48% | -82% | -81% |
| PLATINUM | 1428 | 4 | 2% | 1% | -74% | -96% | -96% |
| EURUSD | 1371 | 3 | 2% | 1% | -80% | -89% | -89% |
| COPPER | 1351 | 6 | 2% | 1% | -59% | -70% | -69% |
| GBPUSD | 1301 | 3 | 2% | 1% | -78% | -96% | -96% |
| NATGAS | 1300 | 7 | 2% | 1% | -50% | -82% | -81% |
| USDJPY | 1280 | 5 | 2% | 1% | -64% | -97% | -97% |
| PALLADIUM | 1278 | 3 | 1% | 1% | -78% | -91% | -91% |
| AUDUSD | 828 | 4 | 2% | 1% | -55% | -86% | -85% |
| USDCAD | 796 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 390 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 240 | 1 | 5% | 2% | -61% | -52% | -50% |
| 30YRRATE | 223 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 215 | 2 | 4% | 0% | -13% | -7% | -6% |
| 5YRRATE | 199 | 1 | 5% | 2% | -53% | -91% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 22730 | 88 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 21961 | 77 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4482 | 21 | 2% | 1% | -18% | -83% | -82% |
| 0.05–0.1% | 4719 | 18 | 3% | 2% | -42% | -91% | -90% |
| 0.1–0.2% | 7159 | 25 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 8207 | 33 | 6% | 3% | -55% | -87% | -86% |
| Over 0.5% | 3080 | 12 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11048 | 40 | 4% | 2% | -59% | -87% | -87% |
| Morning (6am–12pm) | 11054 | 48 | 4% | 2% | -51% | -85% | -85% |
| Afternoon (12–6pm) | 10598 | 39 | 4% | 2% | -57% | -86% | -86% |
| Evening (6pm–12am) | 11991 | 38 | 3% | 2% | -64% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,720 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/3 9:14:45 PM | USDCAD | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 9:14:13 PM | GBPUSD | DOWN | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 9:14:13 PM | AUDUSD | DOWN | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 9:14:13 PM | USDJPY | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 9:13:08 PM | COPPER | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 9:11:15 PM | HYPE | DOWN | 3.7 min | +0.763% | 0¢ | ❌ Lost | -$0.15 |
| 11/3 9:10:59 PM | XRP | DOWN | 4.0 min | +0.421% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 9:10:41 PM | BTC | DOWN | 4.3 min | +0.447% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 9:10:25 PM | ETH | DOWN | 4.6 min | +0.528% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 9:10:09 PM | PALLADIUM | DOWN | 4.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 9:10:09 PM | BRENT | UP | 4.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 9:09:54 PM | WTI | UP | 5.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 9:09:36 PM | BNB | DOWN | 5.4 min | +0.411% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 9:09:36 PM | DOGE | DOWN | 5.4 min | +0.413% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 9:09:36 PM | SOL | DOWN | 5.4 min | +0.570% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 9:09:36 PM | PLATINUM | DOWN | 5.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 9:09:20 PM | ZEC | DOWN | 5.7 min | +1.784% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 9:09:20 PM | SILVER | DOWN | 5.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 9:09:04 PM | GOLD | DOWN | 5.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 9:08:49 PM | NEAR | DOWN | 6.2 min | +1.281% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 8:59:58 PM | GBPUSD | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 8:59:58 PM | NATGAS | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 8:59:58 PM | GOLD | UP | 1 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/3 8:59:42 PM | USDCAD | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 8:59:10 PM | BNB | UP | 49 sec | -0.154% | 0¢ | ❌ Lost | $0.00 |
| 11/3 8:58:06 PM | USDJPY | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 8:57:35 PM | DOGE | DOWN | 2.4 min | +0.215% | 0¢ | ❌ Lost | $0.00 |
| 11/3 8:57:19 PM | COPPER | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 8:57:19 PM | ETH | DOWN | 2.7 min | +0.255% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 8:57:19 PM | SOL | DOWN | 2.7 min | +0.283% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
