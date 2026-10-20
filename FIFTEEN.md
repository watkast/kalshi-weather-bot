# 15-Minute 1¢ Study

*Updated Tue Oct 20, 1:51 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2162 finished bets | 1% | $78.10 | +32% | +3.61¢ | $21.80 / $56.30 |

*Expect about **96 buys a day** (~$14.38/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1998 | $59.05 | +27% |
| Momentum model ≥ 2%, hold to the close | 3333 | -$28.10 | -7% |
| Volatility model ≥ 5%, sell at 50¢ | 2162 | -$38.90 | -16% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 25551 | 25544 | 92 (0%) | 1.07% | -$1,822.55 (-59%) | Hold to the close: -$1,822.55 (-59%) |

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
| Volatility model | 16643 | 4.6% | 0.4% (65) | -674% | ❌ Worse |
| Momentum model | 16643 | 4.5% | 0.4% (65) | -696% | ❌ Worse |
| Mean-reversion model | 16643 | 7.8% | 0.4% (65) | -816% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16643 | 65 | -51% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3943 | 31 | -10% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 2162 | 23 | +32% | -71% | -70% | -67% |
| Volatility model ≥ 10% | 1243 | 15 | +69% | -60% | -58% | -56% |
| Momentum model ≥ 2% | 3333 | 26 | -7% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 1998 | 20 | +27% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 1315 | 13 | +35% | -67% | -66% | -61% |
| Mean-reversion model ≥ 2% | 6541 | 42 | -30% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4552 | 34 | -18% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3015 | 22 | -17% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16841 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6048 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2655 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 25544 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 92 | 0% | -$1,822.55 | -59% | — |
| Sell at 2¢ | 926 | 4% | -$2,743.79 | -88% | 46 sec |
| Sell at 3¢ | 628 | 2% | -$2,739.63 | -88% | 47 sec |
| Sell at 5¢ | 445 | 2% | -$2,695.30 | -87% | 51 sec |
| Sell at 10¢ | 271 | 1% | -$2,601.54 | -84% | 64 sec |
| Sell at 25¢ | 147 | 1% | -$2,413.98 | -78% | 80 sec |
| Sell at 50¢ | 95 | 0% | -$2,189.30 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1021 | 5 | 11% | 4% | -53% | -81% | -84% |
| 2–5 min | 8263 | 41 | 7% | 3% | -51% | -88% | -87% |
| 1–2 min | 6529 | 24 | 3% | 2% | -60% | -93% | -92% |
| Under 1 min | 9727 | 22 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1894 | 11 | 4% | 2% | -28% | -90% | -90% |
| HYPE | 1882 | 6 | 5% | 3% | -61% | -89% | -87% |
| BNB | 1881 | 9 | 5% | 2% | -41% | -83% | -82% |
| ETH | 1871 | 9 | 6% | 3% | -42% | -87% | -86% |
| DOGE | 1870 | 3 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1869 | 2 | 3% | 1% | -87% | -92% | -92% |
| XRP | 1862 | 7 | 3% | 1% | -54% | -87% | -88% |
| NEAR | 1857 | 10 | 6% | 3% | -31% | -79% | -79% |
| BTC | 1855 | 10 | 5% | 2% | -28% | -88% | -90% |
| GOLD | 992 | 1 | 4% | 1% | -88% | -92% | -94% |
| SILVER | 954 | 4 | 3% | 1% | -52% | -81% | -81% |
| WTI | 931 | 3 | 3% | 1% | -62% | -94% | -95% |
| COPPER | 831 | 3 | 2% | 1% | -66% | -75% | -74% |
| PLATINUM | 825 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 761 | 5 | 2% | 1% | -39% | -84% | -83% |
| EURUSD | 759 | 3 | 2% | 1% | -63% | -84% | -84% |
| PALLADIUM | 754 | 2 | 1% | 0% | -75% | -86% | -86% |
| GBPUSD | 716 | 1 | 2% | 1% | -87% | -97% | -97% |
| USDJPY | 667 | 3 | 1% | 1% | -58% | -99% | -98% |
| AUDUSD | 282 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 231 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12864 | 45 | 4% | 2% | -60% | -88% | -87% |
| DOWN (bought NO) | 12680 | 47 | 3% | 1% | -57% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2817 | 15 | 2% | 1% | -11% | -77% | -76% |
| 0.05–0.1% | 2916 | 10 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 4264 | 13 | 5% | 2% | -62% | -89% | -89% |
| 0.2–0.5% | 4929 | 23 | 6% | 3% | -49% | -88% | -87% |
| Over 0.5% | 1912 | 6 | 7% | 3% | -68% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6450 | 26 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6213 | 29 | 4% | 2% | -47% | -88% | -87% |
| Afternoon (12–6pm) | 5919 | 19 | 3% | 1% | -62% | -89% | -89% |
| Evening (6pm–12am) | 6962 | 18 | 3% | 2% | -70% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,761 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/20 1:44:56 PM | PLATINUM | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 1:44:40 PM | PALLADIUM | DOWN | 19 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 1:43:52 PM | GBPUSD | DOWN | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 1:43:20 PM | NATGAS | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 1:41:40 PM | ZEC | DOWN | 3.3 min | +0.465% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 1:41:08 PM | GOLD | UP | 3.9 min | — | 4¢ | ❌ Lost | -$0.15 |
| 10/20 1:40:53 PM | BTC | DOWN | 4.1 min | +0.164% | 0¢ | ❌ Lost | $0.00 |
| 10/20 1:40:19 PM | NEAR | DOWN | 4.7 min | +0.636% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 1:40:03 PM | BNB | DOWN | 4.9 min | +0.140% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 1:39:49 PM | ETH | DOWN | 5.2 min | +0.233% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 1:39:17 PM | XRP | DOWN | 5.7 min | +0.387% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 1:38:29 PM | HYPE | DOWN | 6.5 min | +0.388% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 1:38:13 PM | SOL | DOWN | 6.8 min | +0.345% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 1:37:57 PM | DOGE | DOWN | 7.0 min | +0.363% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 1:29:59 PM | PALLADIUM | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 1:29:59 PM | USDJPY | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 1:29:43 PM | GOLD | DOWN | 17 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 10/20 1:29:43 PM | AUDUSD | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 1:29:27 PM | PLATINUM | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 1:29:27 PM | WTI | DOWN | 33 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/20 1:29:11 PM | NATGAS | DOWN | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 1:28:07 PM | HYPE | UP | 1.9 min | -0.263% | 0¢ | ❌ Lost | $0.00 |
| 10/20 1:28:07 PM | EURUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 1:26:14 PM | BTC | UP | 3.8 min | -0.165% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 1:25:42 PM | NEAR | UP | 4.3 min | -0.825% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 1:25:26 PM | BNB | UP | 4.5 min | -0.162% | 5¢ | ❌ Lost | -$0.15 |
| 10/20 1:24:54 PM | DOGE | UP | 5.1 min | -0.452% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 1:24:38 PM | SOL | UP | 5.3 min | -0.455% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 1:24:22 PM | XRP | UP | 5.6 min | -0.446% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 1:23:18 PM | ETH | UP | 6.7 min | -0.362% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
