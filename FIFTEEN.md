# 15-Minute 1¢ Study

*Updated Tue Oct 6, 2:32 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 674 finished bets | 1% | $39.85 | +55% | +5.91¢ | -$8.75 / $48.60 |

*Expect about **79 buys a day** (~$11.79/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 674 | $26.45 | +37% |
| Mean-reversion model ≥ 5%, hold to the close | 1484 | $23.40 | +13% |
| 5+ min left, hold to the close | 251 | $18.80 | +51% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 9831 | 9825 | 46 (0%) | 1.07% | -$540.70 (-46%) | Hold to the close: -$540.70 (-46%) |

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
| Volatility model | 6405 | 4.1% | 0.5% (33) | -535% | ❌ Worse |
| Momentum model | 6405 | 4.1% | 0.5% (33) | -564% | ❌ Worse |
| Mean-reversion model | 6405 | 6.7% | 0.5% (33) | -617% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6405 | 33 | -35% | -86% | -86% | -83% |
| Volatility model ≥ 2% | 1248 | 12 | +12% | -72% | -72% | -67% |
| Volatility model ≥ 5% | 674 | 8 | +55% | -60% | -59% | -55% |
| Volatility model ≥ 10% | 415 | 6 | +117% | -42% | -43% | -37% |
| Momentum model ≥ 2% | 1111 | 10 | +9% | -73% | -74% | -72% |
| Momentum model ≥ 5% | 674 | 7 | +37% | -65% | -67% | -64% |
| Momentum model ≥ 10% | 465 | 6 | +87% | -53% | -53% | -50% |
| Mean-reversion model ≥ 2% | 2199 | 19 | -6% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1484 | 15 | +13% | -80% | -80% | -74% |
| Mean-reversion model ≥ 10% | 976 | 11 | +31% | -79% | -79% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6602 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2437 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 786 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 9825 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 46 | 0% | -$540.70 | -46% | — |
| Sell at 2¢ | 358 | 4% | -$1,063.62 | -90% | 33 sec |
| Sell at 3¢ | 237 | 2% | -$1,064.27 | -90% | 47 sec |
| Sell at 5¢ | 177 | 2% | -$1,041.65 | -88% | 50 sec |
| Sell at 10¢ | 121 | 1% | -$984.19 | -83% | 65 sec |
| Sell at 25¢ | 70 | 1% | -$883.00 | -75% | 82 sec |
| Sell at 50¢ | 46 | 0% | -$762.20 | -64% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 248 | 4 | 10% | 4% | +52% | -82% | -87% |
| 2–5 min | 3173 | 24 | 7% | 3% | -26% | -87% | -87% |
| 1–2 min | 2593 | 11 | 3% | 2% | -54% | -94% | -93% |
| Under 1 min | 3808 | 7 | 1% | 0% | -72% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 748 | 6 | 5% | 3% | -4% | -89% | -89% |
| HYPE | 738 | 3 | 5% | 3% | -50% | -89% | -87% |
| DOGE | 737 | 2 | 4% | 1% | -65% | -92% | -91% |
| ETH | 734 | 7 | 5% | 3% | +19% | -87% | -87% |
| BNB | 732 | 3 | 4% | 2% | -50% | -91% | -92% |
| SOL | 730 | 0 | 3% | 1% | -100% | -93% | -92% |
| NEAR | 728 | 5 | 6% | 3% | -10% | -67% | -68% |
| BTC | 728 | 4 | 5% | 3% | -28% | -87% | -89% |
| XRP | 727 | 5 | 2% | 1% | -13% | -79% | -79% |
| GOLD | 410 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 394 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 372 | 2 | 2% | 1% | -41% | -95% | -97% |
| COPPER | 352 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 311 | 0 | 0% | 0% | -100% | -99% | -99% |
| NATGAS | 300 | 3 | 3% | 2% | -7% | -94% | -92% |
| PALLADIUM | 298 | 1 | 2% | 1% | -69% | -97% | -98% |
| EURUSD | 284 | 1 | 4% | 2% | -67% | -93% | -92% |
| GBPUSD | 272 | 1 | 3% | 2% | -66% | -94% | -94% |
| USDJPY | 230 | 3 | 2% | 1% | +22% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4951 | 24 | 4% | 2% | -43% | -89% | -89% |
| DOWN (bought NO) | 4874 | 22 | 3% | 2% | -48% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1084 | 8 | 2% | 1% | +27% | -62% | -62% |
| 0.05–0.1% | 1130 | 4 | 3% | 1% | -48% | -91% | -92% |
| 0.1–0.2% | 1667 | 6 | 4% | 2% | -55% | -91% | -92% |
| 0.2–0.5% | 1941 | 12 | 6% | 3% | -32% | -88% | -87% |
| Over 0.5% | 778 | 5 | 7% | 3% | -34% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2570 | 15 | 4% | 2% | -32% | -87% | -88% |
| Morning (6am–12pm) | 2536 | 17 | 5% | 3% | -24% | -90% | -89% |
| Afternoon (12–6pm) | 2083 | 7 | 3% | 1% | -60% | -87% | -88% |
| Evening (6pm–12am) | 2636 | 7 | 3% | 1% | -69% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,044 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/6 2:29:48 PM | PLATINUM | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:29:48 PM | COPPER | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:29:48 PM | BTC | UP | 12 sec | -0.009% | 0¢ | ❌ Lost | $0.00 |
| 10/6 2:29:16 PM | ETH | DOWN | 44 sec | +0.059% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:29:16 PM | BNB | DOWN | 44 sec | +0.012% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:28:45 PM | NATGAS | UP | 75 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 2:26:57 PM | ZEC | DOWN | 3.0 min | +0.283% | 54¢ | ❌ Lost | -$0.15 |
| 10/6 2:26:57 PM | HYPE | DOWN | 3.0 min | +0.205% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 2:26:25 PM | SILVER | UP | 3.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 2:26:13 PM | DOGE | DOWN | 3.8 min | +0.225% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 2:26:13 PM | GOLD | UP | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:25:57 PM | NEAR | DOWN | 4.0 min | +0.606% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 2:25:57 PM | XRP | DOWN | 4.0 min | +0.186% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 2:25:17 PM | SOL | DOWN | 4.7 min | +0.269% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 2:14:53 PM | SOL | DOWN | 6 sec | -0.008% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:14:37 PM | NEAR | UP | 22 sec | +0.016% | 94¢ | ✅ Won | $13.85 |
| 10/6 2:14:37 PM | COPPER | DOWN | 22 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 2:14:21 PM | DOGE | UP | 38 sec | -0.095% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:14:21 PM | GOLD | UP | 38 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 2:13:15 PM | XRP | UP | 1.8 min | -0.120% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 2:13:00 PM | USDJPY | UP | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 2:12:42 PM | WTI | DOWN | 2.3 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/6 2:12:10 PM | ZEC | UP | 2.8 min | -0.486% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 2:12:10 PM | BNB | UP | 2.8 min | -0.137% | 0¢ | ❌ Lost | $0.00 |
| 10/6 2:11:55 PM | HYPE | UP | 3.1 min | -0.162% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 1:59:51 PM | NATGAS | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 1:59:35 PM | ZEC | UP | 25 sec | -0.210% | 0¢ | ❌ Lost | $0.00 |
| 10/6 1:59:19 PM | EURUSD | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 1:59:03 PM | SILVER | UP | 57 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 1:58:45 PM | BNB | DOWN | 75 sec | +0.033% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
