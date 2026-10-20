# 15-Minute 1¢ Study

*Updated Tue Oct 20, 2:02 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2164 finished bets | 1% | $77.80 | +32% | +3.60¢ | $21.65 / $56.15 |

*Expect about **96 buys a day** (~$14.39/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2000 | $58.75 | +27% |
| Momentum model ≥ 2%, hold to the close | 3335 | -$28.40 | -7% |
| Volatility model ≥ 5%, sell at 50¢ | 2164 | -$39.20 | -16% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 25564 | 25557 | 92 (0%) | 1.07% | -$1,824.20 (-59%) | Hold to the close: -$1,824.20 (-59%) |

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
| Volatility model | 16652 | 4.6% | 0.4% (65) | -676% | ❌ Worse |
| Momentum model | 16652 | 4.5% | 0.4% (65) | -698% | ❌ Worse |
| Mean-reversion model | 16652 | 7.8% | 0.4% (65) | -818% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16652 | 65 | -51% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3946 | 31 | -10% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 2164 | 23 | +32% | -71% | -70% | -67% |
| Volatility model ≥ 10% | 1244 | 15 | +69% | -60% | -58% | -56% |
| Momentum model ≥ 2% | 3335 | 26 | -7% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 2000 | 20 | +27% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 1317 | 13 | +35% | -67% | -66% | -61% |
| Mean-reversion model ≥ 2% | 6544 | 42 | -30% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 4554 | 34 | -18% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3017 | 22 | -17% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16850 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6049 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2658 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 25557 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 92 | 0% | -$1,824.20 | -59% | — |
| Sell at 2¢ | 926 | 4% | -$2,745.44 | -88% | 46 sec |
| Sell at 3¢ | 628 | 2% | -$2,741.28 | -88% | 47 sec |
| Sell at 5¢ | 445 | 2% | -$2,696.95 | -87% | 51 sec |
| Sell at 10¢ | 271 | 1% | -$2,603.19 | -84% | 64 sec |
| Sell at 25¢ | 147 | 1% | -$2,415.63 | -78% | 80 sec |
| Sell at 50¢ | 95 | 0% | -$2,190.95 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1022 | 5 | 11% | 4% | -53% | -81% | -84% |
| 2–5 min | 8263 | 41 | 7% | 3% | -51% | -88% | -87% |
| 1–2 min | 6534 | 24 | 3% | 2% | -60% | -93% | -92% |
| Under 1 min | 9734 | 22 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1895 | 11 | 4% | 2% | -28% | -90% | -90% |
| HYPE | 1883 | 6 | 5% | 3% | -61% | -89% | -87% |
| BNB | 1882 | 9 | 5% | 2% | -42% | -83% | -82% |
| ETH | 1872 | 9 | 6% | 3% | -42% | -87% | -86% |
| DOGE | 1871 | 3 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1870 | 2 | 3% | 1% | -87% | -92% | -92% |
| XRP | 1863 | 7 | 3% | 1% | -54% | -87% | -88% |
| NEAR | 1858 | 10 | 6% | 3% | -31% | -79% | -79% |
| BTC | 1856 | 10 | 5% | 2% | -28% | -88% | -90% |
| GOLD | 993 | 1 | 4% | 1% | -88% | -92% | -94% |
| SILVER | 954 | 4 | 3% | 1% | -52% | -81% | -81% |
| WTI | 931 | 3 | 3% | 1% | -62% | -94% | -95% |
| COPPER | 831 | 3 | 2% | 1% | -66% | -75% | -74% |
| PLATINUM | 825 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 761 | 5 | 2% | 1% | -39% | -84% | -83% |
| EURUSD | 759 | 3 | 2% | 1% | -63% | -84% | -84% |
| PALLADIUM | 754 | 2 | 1% | 0% | -75% | -86% | -86% |
| GBPUSD | 717 | 1 | 2% | 1% | -87% | -97% | -97% |
| USDJPY | 668 | 3 | 1% | 1% | -58% | -99% | -98% |
| AUDUSD | 282 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 232 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12870 | 45 | 4% | 2% | -60% | -88% | -87% |
| DOWN (bought NO) | 12687 | 47 | 3% | 1% | -57% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2820 | 15 | 2% | 1% | -11% | -77% | -76% |
| 0.05–0.1% | 2918 | 10 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 4266 | 13 | 5% | 2% | -62% | -89% | -89% |
| 0.2–0.5% | 4930 | 23 | 6% | 3% | -49% | -88% | -87% |
| Over 0.5% | 1913 | 6 | 7% | 3% | -68% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6450 | 26 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6213 | 29 | 4% | 2% | -47% | -88% | -87% |
| Afternoon (12–6pm) | 5932 | 19 | 3% | 1% | -62% | -89% | -89% |
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
| 10/20 1:59:55 PM | GOLD | UP | 5 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/20 1:59:39 PM | BNB | DOWN | 21 sec | -0.029% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 1:59:39 PM | DOGE | DOWN | 21 sec | +0.041% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 1:59:23 PM | GBPUSD | UP | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 1:59:23 PM | BTC | UP | 37 sec | -0.048% | 0¢ | ❌ Lost | $0.00 |
| 10/20 1:59:23 PM | NEAR | UP | 37 sec | -0.304% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 1:59:07 PM | ETH | UP | 53 sec | -0.074% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 1:58:51 PM | USDCAD | UP | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 1:58:35 PM | HYPE | DOWN | 85 sec | +0.099% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 1:58:19 PM | SOL | DOWN | 1.7 min | +0.128% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 1:58:19 PM | USDJPY | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 1:58:19 PM | XRP | DOWN | 1.7 min | +0.151% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 1:52:13 PM | ZEC | DOWN | 7.8 min | +0.961% | 1¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
