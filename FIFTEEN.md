# 15-Minute 1¢ Study

*Updated Wed Oct 7, 6:24 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 749 finished bets | 1% | $31.60 | +39% | +4.22¢ | -$12.35 / $43.95 |

*Expect about **77 buys a day** (~$11.54/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 747 | $18.65 | +24% |
| 5+ min left, hold to the close | 290 | $12.95 | +30% |
| Volatility model ≥ 2%, hold to the close | 1378 | $2.55 | +2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 11165 | 11159 | 49 (0%) | 1.07% | -$665.80 (-49%) | Hold to the close: -$665.80 (-49%) |

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
| Volatility model | 7214 | 4.0% | 0.5% (33) | -558% | ❌ Worse |
| Momentum model | 7214 | 4.1% | 0.5% (33) | -588% | ❌ Worse |
| Mean-reversion model | 7214 | 6.7% | 0.5% (33) | -652% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7214 | 33 | -43% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 1378 | 12 | +2% | -73% | -73% | -69% |
| Volatility model ≥ 5% | 749 | 8 | +39% | -62% | -61% | -58% |
| Volatility model ≥ 10% | 468 | 6 | +90% | -45% | -45% | -40% |
| Momentum model ≥ 2% | 1225 | 10 | -1% | -73% | -75% | -72% |
| Momentum model ≥ 5% | 747 | 7 | +24% | -66% | -68% | -65% |
| Momentum model ≥ 10% | 516 | 6 | +68% | -55% | -56% | -52% |
| Mean-reversion model ≥ 2% | 2466 | 19 | -16% | -84% | -84% | -80% |
| Mean-reversion model ≥ 5% | 1668 | 15 | -0% | -81% | -81% | -75% |
| Mean-reversion model ≥ 10% | 1107 | 11 | +15% | -79% | -79% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7411 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2817 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 931 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 11159 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 49 | 0% | -$665.80 | -49% | — |
| Sell at 2¢ | 391 | 4% | -$1,208.14 | -89% | 34 sec |
| Sell at 3¢ | 260 | 2% | -$1,208.40 | -89% | 47 sec |
| Sell at 5¢ | 194 | 2% | -$1,183.70 | -88% | 56 sec |
| Sell at 10¢ | 130 | 1% | -$1,125.50 | -83% | 64 sec |
| Sell at 25¢ | 75 | 1% | -$1,019.55 | -75% | 82 sec |
| Sell at 50¢ | 49 | 0% | -$895.05 | -66% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 287 | 4 | 10% | 3% | +31% | -82% | -86% |
| 2–5 min | 3599 | 25 | 7% | 3% | -32% | -88% | -88% |
| 1–2 min | 2946 | 12 | 3% | 2% | -56% | -94% | -93% |
| Under 1 min | 4324 | 8 | 1% | 0% | -73% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| HYPE | 831 | 3 | 5% | 3% | -56% | -89% | -87% |
| ZEC | 830 | 6 | 5% | 3% | -14% | -90% | -90% |
| DOGE | 826 | 2 | 3% | 1% | -69% | -92% | -92% |
| ETH | 825 | 7 | 5% | 3% | +6% | -88% | -88% |
| BNB | 824 | 3 | 4% | 2% | -56% | -90% | -91% |
| NEAR | 820 | 5 | 6% | 3% | -20% | -70% | -71% |
| BTC | 819 | 4 | 5% | 2% | -36% | -88% | -90% |
| SOL | 819 | 0 | 3% | 1% | -100% | -94% | -93% |
| XRP | 817 | 5 | 2% | 1% | -23% | -81% | -81% |
| GOLD | 471 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 460 | 0 | 2% | 1% | -100% | -95% | -94% |
| WTI | 436 | 3 | 3% | 1% | -24% | -95% | -96% |
| COPPER | 401 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 360 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 350 | 3 | 3% | 2% | -20% | -95% | -93% |
| PALLADIUM | 339 | 1 | 1% | 1% | -72% | -97% | -98% |
| EURUSD | 336 | 3 | 4% | 2% | -17% | -66% | -64% |
| GBPUSD | 316 | 1 | 3% | 2% | -70% | -95% | -95% |
| USDJPY | 276 | 3 | 1% | 1% | +1% | -97% | -96% |
| USDCAD | 2 | 0 | 0% | 0% | -100% | -100% | -100% |
| AUDUSD | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5661 | 26 | 4% | 2% | -47% | -88% | -88% |
| DOWN (bought NO) | 5498 | 23 | 3% | 2% | -52% | -91% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1225 | 8 | 2% | 1% | +13% | -66% | -65% |
| 0.05–0.1% | 1273 | 4 | 3% | 1% | -54% | -91% | -92% |
| 0.1–0.2% | 1885 | 6 | 4% | 2% | -60% | -92% | -92% |
| 0.2–0.5% | 2164 | 12 | 6% | 3% | -39% | -89% | -88% |
| Over 0.5% | 862 | 5 | 6% | 3% | -41% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2890 | 17 | 4% | 2% | -32% | -84% | -84% |
| Morning (6am–12pm) | 2706 | 17 | 4% | 2% | -28% | -91% | -90% |
| Afternoon (12–6pm) | 2560 | 7 | 3% | 1% | -68% | -88% | -89% |
| Evening (6pm–12am) | 3003 | 8 | 3% | 1% | -69% | -95% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,084 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/7 6:14:57 PM | AUDUSD | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:14:57 PM | XRP | UP | 2 sec | -0.070% | 0¢ | ❌ Lost | $0.00 |
| 10/7 6:14:57 PM | GBPUSD | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:14:57 PM | NEAR | DOWN | 2 sec | +0.004% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:14:37 PM | GOLD | DOWN | 22 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/7 6:14:21 PM | SILVER | DOWN | 38 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:14:21 PM | DOGE | DOWN | 38 sec | +0.082% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:13:34 PM | BNB | DOWN | 85 sec | -0.004% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:12:48 PM | HYPE | UP | 2.2 min | -0.220% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:12:33 PM | BTC | UP | 2.4 min | -0.109% | 2¢ | ❌ Lost | -$0.15 |
| 10/7 6:12:17 PM | USDJPY | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:11:45 PM | COPPER | DOWN | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:11:14 PM | ETH | UP | 3.8 min | -0.128% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 5:59:57 PM | USDCAD | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 5:59:57 PM | PLATINUM | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 5:59:42 PM | HYPE | DOWN | 18 sec | +0.004% | 0¢ | ❌ Lost | $0.00 |
| 10/7 5:59:42 PM | ETH | UP | 18 sec | -0.025% | 0¢ | ❌ Lost | $0.00 |
| 10/7 5:59:42 PM | XRP | UP | 18 sec | -0.056% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 5:59:26 PM | NEAR | UP | 34 sec | -0.378% | 0¢ | ❌ Lost | $0.00 |
| 10/7 5:59:26 PM | EURUSD | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 5:59:10 PM | SOL | DOWN | 50 sec | +0.031% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 5:59:10 PM | COPPER | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 5:58:54 PM | WTI | DOWN | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 5:58:54 PM | GOLD | UP | 66 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 5:58:37 PM | SILVER | UP | 83 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 5:58:37 PM | NATGAS | DOWN | 83 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 5:58:37 PM | USDJPY | DOWN | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 5:58:21 PM | BTC | UP | 1.6 min | -0.067% | 29¢ | ❌ Lost | -$0.15 |
| 10/7 5:57:19 PM | DOGE | DOWN | 2.7 min | +0.118% | 0¢ | ❌ Lost | $0.00 |
| 10/7 5:57:03 PM | GBPUSD | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
