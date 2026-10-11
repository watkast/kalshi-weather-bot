# 15-Minute 1¢ Study

*Updated Sun Oct 11, 5:26 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1144 finished bets | 1% | $43.95 | +35% | +3.84¢ | $22.35 / $21.60 |

*Expect about **84 buys a day** (~$12.53/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1093 | $23.00 | +20% |
| 5+ min left, hold to the close | 404 | -$3.70 | -6% |
| Volatility model ≥ 5%, sell at 50¢ | 1144 | -$15.05 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 14841 | 14831 | 59 (0%) | 1.07% | -$960.65 (-54%) | Hold to the close: -$960.65 (-54%) |

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
| Volatility model | 9949 | 4.5% | 0.4% (42) | -679% | ❌ Worse |
| Momentum model | 9949 | 4.5% | 0.4% (42) | -706% | ❌ Worse |
| Mean-reversion model | 9949 | 7.2% | 0.4% (42) | -783% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 9949 | 42 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1997 | 16 | -6% | -77% | -77% | -74% |
| Volatility model ≥ 5% | 1144 | 12 | +35% | -71% | -70% | -67% |
| Volatility model ≥ 10% | 724 | 8 | +60% | -61% | -60% | -57% |
| Momentum model ≥ 2% | 1761 | 13 | -10% | -78% | -79% | -77% |
| Momentum model ≥ 5% | 1093 | 10 | +20% | -74% | -75% | -72% |
| Momentum model ≥ 10% | 756 | 7 | +33% | -67% | -67% | -63% |
| Mean-reversion model ≥ 2% | 3490 | 25 | -21% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2379 | 19 | -11% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1598 | 13 | -5% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 10147 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3463 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1221 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 14831 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 59 | 0% | -$960.65 | -54% | — |
| Sell at 2¢ | 506 | 3% | -$1,613.09 | -90% | 33 sec |
| Sell at 3¢ | 333 | 2% | -$1,614.78 | -90% | 47 sec |
| Sell at 5¢ | 244 | 2% | -$1,586.05 | -89% | 50 sec |
| Sell at 10¢ | 161 | 1% | -$1,505.74 | -84% | 64 sec |
| Sell at 25¢ | 92 | 1% | -$1,384.13 | -77% | 81 sec |
| Sell at 50¢ | 60 | 0% | -$1,241.65 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 400 | 4 | 10% | 3% | -5% | -82% | -86% |
| 2–5 min | 4798 | 31 | 6% | 3% | -37% | -88% | -89% |
| 1–2 min | 3901 | 15 | 3% | 2% | -58% | -94% | -94% |
| Under 1 min | 5728 | 9 | 1% | 0% | -77% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1138 | 6 | 4% | 3% | -35% | -90% | -90% |
| HYPE | 1137 | 3 | 4% | 2% | -67% | -90% | -89% |
| DOGE | 1131 | 2 | 4% | 2% | -78% | -91% | -90% |
| BNB | 1129 | 5 | 4% | 2% | -46% | -91% | -92% |
| ETH | 1127 | 8 | 5% | 2% | -14% | -90% | -89% |
| SOL | 1126 | 2 | 3% | 1% | -78% | -93% | -92% |
| BTC | 1122 | 5 | 5% | 2% | -41% | -88% | -91% |
| XRP | 1119 | 7 | 2% | 1% | -22% | -84% | -84% |
| NEAR | 1118 | 6 | 5% | 2% | -30% | -75% | -77% |
| GOLD | 570 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 558 | 1 | 3% | 1% | -79% | -94% | -94% |
| WTI | 532 | 3 | 3% | 1% | -36% | -94% | -96% |
| COPPER | 492 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 454 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 435 | 3 | 3% | 2% | -36% | -95% | -93% |
| PALLADIUM | 422 | 1 | 1% | 0% | -78% | -98% | -99% |
| EURUSD | 416 | 3 | 3% | 2% | -33% | -73% | -71% |
| GBPUSD | 393 | 1 | 3% | 2% | -76% | -96% | -95% |
| USDJPY | 358 | 3 | 1% | 1% | -22% | -98% | -97% |
| USDCAD | 27 | 0 | 0% | 0% | -100% | -100% | -100% |
| AUDUSD | 27 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 7443 | 31 | 3% | 2% | -52% | -89% | -89% |
| DOWN (bought NO) | 7388 | 28 | 3% | 2% | -56% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1841 | 9 | 2% | 1% | -19% | -76% | -75% |
| 0.05–0.1% | 1809 | 6 | 3% | 1% | -53% | -92% | -92% |
| 0.1–0.2% | 2594 | 8 | 4% | 2% | -62% | -91% | -92% |
| 0.2–0.5% | 2786 | 16 | 5% | 3% | -37% | -89% | -88% |
| Over 0.5% | 1114 | 5 | 6% | 2% | -54% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3699 | 20 | 4% | 2% | -37% | -85% | -86% |
| Morning (6am–12pm) | 3615 | 20 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 3526 | 9 | 3% | 1% | -70% | -90% | -91% |
| Evening (6pm–12am) | 3991 | 10 | 3% | 1% | -71% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,519 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/11 5:25:45 PM | GOLD | DOWN | 4.2 min | — | — | In play | — |
| 10/11 5:25:30 PM | ZEC | DOWN | 4.5 min | +0.665% | — | In play | — |
| 10/11 5:24:58 PM | WTI | UP | 5.0 min | — | — | In play | — |
| 10/11 5:14:46 PM | NATGAS | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 5:14:14 PM | XRP | DOWN | 45 sec | +0.007% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 5:13:58 PM | PLATINUM | DOWN | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 5:13:58 PM | PALLADIUM | DOWN | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 5:13:41 PM | COPPER | DOWN | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 5:13:25 PM | SILVER | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/11 5:13:25 PM | GOLD | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/11 5:13:09 PM | BTC | DOWN | 1.9 min | +0.078% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 5:12:54 PM | SOL | DOWN | 2.1 min | +0.137% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 5:12:54 PM | HYPE | DOWN | 2.1 min | +0.103% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 5:12:54 PM | NEAR | DOWN | 2.1 min | +0.302% | 0¢ | ❌ Lost | $0.00 |
| 10/11 5:12:39 PM | ETH | DOWN | 2.3 min | +0.124% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 5:12:23 PM | DOGE | DOWN | 2.6 min | +0.132% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 5:12:07 PM | WTI | UP | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/11 5:11:51 PM | GBPUSD | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 5:11:51 PM | USDCAD | UP | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 5:11:51 PM | EURUSD | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 5:11:02 PM | BNB | DOWN | 4.0 min | +0.077% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 5:10:00 PM | ZEC | DOWN | 5.0 min | +0.501% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 4:59:47 PM | BNB | DOWN | 12 sec | -0.001% | 0¢ | ❌ Lost | $0.00 |
| 10/11 4:59:47 PM | COPPER | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 4:59:47 PM | USDJPY | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 4:59:15 PM | HYPE | UP | 44 sec | -0.093% | 0¢ | ❌ Lost | $0.00 |
| 10/11 4:59:15 PM | NEAR | DOWN | 44 sec | +0.053% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 4:59:15 PM | USDCAD | DOWN | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 4:59:15 PM | AUDUSD | UP | 44 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/11 4:58:59 PM | ETH | UP | 60 sec | -0.033% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
