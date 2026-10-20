# 15-Minute 1¢ Study

*Updated Tue Oct 20, 4:09 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2105 finished bets | 1% | $85.90 | +36% | +4.08¢ | $24.65 / $61.25 |

*Expect about **95 buys a day** (~$14.26/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1936 | $67.30 | +32% |
| Momentum model ≥ 2%, hold to the close | 3227 | -$14.30 | -4% |
| Volatility model ≥ 2%, hold to the close | 3811 | -$30.55 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 24913 | 24906 | 92 (0%) | 1.07% | -$1,738.25 (-57%) | Hold to the close: -$1,738.25 (-57%) |

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
| Volatility model | 16306 | 4.6% | 0.4% (65) | -672% | ❌ Worse |
| Momentum model | 16306 | 4.6% | 0.4% (65) | -695% | ❌ Worse |
| Mean-reversion model | 16306 | 7.8% | 0.4% (65) | -810% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16306 | 65 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3811 | 31 | -7% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2105 | 23 | +36% | -71% | -70% | -67% |
| Volatility model ≥ 10% | 1224 | 15 | +72% | -59% | -58% | -55% |
| Momentum model ≥ 2% | 3227 | 26 | -4% | -78% | -78% | -75% |
| Momentum model ≥ 5% | 1936 | 20 | +32% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 1282 | 13 | +39% | -66% | -66% | -61% |
| Mean-reversion model ≥ 2% | 6362 | 42 | -28% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 4427 | 34 | -15% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2927 | 22 | -14% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16504 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5861 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2541 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 24906 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 92 | 0% | -$1,738.25 | -57% | — |
| Sell at 2¢ | 894 | 4% | -$2,667.81 | -88% | 46 sec |
| Sell at 3¢ | 605 | 2% | -$2,664.30 | -88% | 47 sec |
| Sell at 5¢ | 431 | 2% | -$2,620.10 | -87% | 51 sec |
| Sell at 10¢ | 262 | 1% | -$2,529.03 | -84% | 64 sec |
| Sell at 25¢ | 144 | 1% | -$2,339.61 | -77% | 80 sec |
| Sell at 50¢ | 94 | 0% | -$2,111.75 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 966 | 5 | 10% | 3% | -51% | -82% | -84% |
| 2–5 min | 8078 | 41 | 7% | 3% | -50% | -88% | -88% |
| 1–2 min | 6357 | 24 | 3% | 2% | -59% | -92% | -92% |
| Under 1 min | 9501 | 22 | 1% | 0% | -66% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1855 | 11 | 4% | 2% | -26% | -90% | -90% |
| HYPE | 1844 | 6 | 5% | 2% | -60% | -89% | -88% |
| BNB | 1844 | 9 | 5% | 2% | -40% | -82% | -82% |
| ETH | 1834 | 9 | 6% | 3% | -41% | -87% | -86% |
| DOGE | 1833 | 3 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1830 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1824 | 7 | 3% | 1% | -53% | -87% | -88% |
| NEAR | 1820 | 10 | 6% | 3% | -29% | -79% | -79% |
| BTC | 1820 | 10 | 5% | 2% | -26% | -88% | -90% |
| GOLD | 961 | 1 | 3% | 1% | -88% | -93% | -94% |
| SILVER | 930 | 4 | 3% | 1% | -50% | -81% | -81% |
| WTI | 904 | 3 | 3% | 1% | -61% | -94% | -96% |
| COPPER | 806 | 3 | 2% | 1% | -65% | -74% | -74% |
| PLATINUM | 796 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 738 | 5 | 2% | 1% | -37% | -84% | -83% |
| EURUSD | 734 | 3 | 2% | 1% | -62% | -83% | -83% |
| PALLADIUM | 726 | 2 | 1% | 0% | -74% | -85% | -85% |
| GBPUSD | 690 | 1 | 2% | 1% | -86% | -97% | -97% |
| USDJPY | 640 | 3 | 1% | 1% | -56% | -99% | -98% |
| AUDUSD | 265 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 212 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12581 | 45 | 4% | 2% | -59% | -88% | -87% |
| DOWN (bought NO) | 12325 | 47 | 3% | 1% | -56% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2796 | 15 | 2% | 1% | -10% | -77% | -76% |
| 0.05–0.1% | 2869 | 10 | 3% | 2% | -49% | -92% | -91% |
| 0.1–0.2% | 4168 | 13 | 5% | 2% | -62% | -90% | -89% |
| 0.2–0.5% | 4810 | 23 | 6% | 3% | -48% | -88% | -88% |
| Over 0.5% | 1858 | 6 | 6% | 3% | -67% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6323 | 26 | 4% | 2% | -53% | -85% | -85% |
| Morning (6am–12pm) | 5814 | 29 | 4% | 2% | -43% | -87% | -86% |
| Afternoon (12–6pm) | 5807 | 19 | 3% | 1% | -61% | -89% | -89% |
| Evening (6pm–12am) | 6962 | 18 | 3% | 2% | -70% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,799 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/20 3:59:29 AM | NEAR | UP | 30 sec | -0.210% | 0¢ | ❌ Lost | $0.00 |
| 10/20 3:59:29 AM | ZEC | DOWN | 30 sec | +0.033% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:59:13 AM | GBPUSD | DOWN | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:58:59 AM | ETH | DOWN | 61 sec | +0.075% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:58:59 AM | SOL | DOWN | 61 sec | +0.109% | 0¢ | ❌ Lost | $0.00 |
| 10/20 3:58:36 AM | BTC | DOWN | 83 sec | +0.108% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:58:36 AM | BNB | DOWN | 83 sec | -0.008% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 3:58:36 AM | XRP | DOWN | 83 sec | +0.108% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 3:58:36 AM | WTI | UP | 83 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 3:58:20 AM | HYPE | DOWN | 1.6 min | +0.116% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 3:58:20 AM | DOGE | DOWN | 1.6 min | +0.095% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:56:45 AM | SILVER | UP | 3.2 min | — | 11¢ | ❌ Lost | -$0.15 |
| 10/20 3:56:13 AM | GOLD | UP | 3.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 3:44:59 AM | GOLD | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:44:59 AM | USDJPY | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:44:59 AM | USDCAD | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:44:59 AM | EURUSD | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:44:59 AM | COPPER | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:44:59 AM | GBPUSD | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:44:43 AM | BTC | UP | 17 sec | -0.021% | 0¢ | ❌ Lost | $0.00 |
| 10/20 3:44:43 AM | NEAR | UP | 17 sec | -0.144% | 0¢ | ❌ Lost | $0.00 |
| 10/20 3:44:27 AM | ZEC | DOWN | 33 sec | +0.064% | 0¢ | ❌ Lost | $0.00 |
| 10/20 3:44:11 AM | SILVER | UP | 49 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 3:43:54 AM | PLATINUM | UP | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:43:22 AM | ETH | UP | 1.6 min | -0.099% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 3:43:22 AM | SOL | UP | 1.6 min | -0.145% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 3:43:22 AM | DOGE | UP | 1.6 min | -0.155% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 3:42:49 AM | XRP | UP | 2.2 min | -0.216% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:42:33 AM | HYPE | UP | 2.5 min | -0.205% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 3:40:23 AM | WTI | DOWN | 4.6 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
