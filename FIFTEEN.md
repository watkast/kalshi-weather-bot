# 15-Minute 1¢ Study

*Updated Sun Oct 18, 5:16 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1884 finished bets | 1% | $84.45 | +40% | +4.48¢ | $37.25 / $47.20 |

*Expect about **93 buys a day** (~$14.00/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1731 | $63.00 | +33% |
| Momentum model ≥ 2%, hold to the close | 2896 | -$1.35 | -0% |
| Volatility model ≥ 5%, sell at 50¢ | 1884 | -$32.55 | -16% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 22604 | 22597 | 86 (0%) | 1.07% | -$1,538.90 (-56%) | Hold to the close: -$1,538.90 (-56%) |

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
| Volatility model | 14873 | 4.6% | 0.4% (60) | -667% | ❌ Worse |
| Momentum model | 14873 | 4.5% | 0.4% (60) | -690% | ❌ Worse |
| Mean-reversion model | 14873 | 7.6% | 0.4% (60) | -799% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 14873 | 60 | -50% | -88% | -88% | -85% |
| Volatility model ≥ 2% | 3410 | 27 | -9% | -79% | -79% | -75% |
| Volatility model ≥ 5% | 1884 | 21 | +40% | -75% | -75% | -71% |
| Volatility model ≥ 10% | 1114 | 13 | +65% | -69% | -68% | -66% |
| Momentum model ≥ 2% | 2896 | 24 | -0% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 1731 | 18 | +33% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 1153 | 12 | +45% | -75% | -74% | -69% |
| Mean-reversion model ≥ 2% | 5724 | 38 | -28% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3971 | 30 | -16% | -82% | -82% | -79% |
| Mean-reversion model ≥ 10% | 2633 | 19 | -17% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 15071 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5309 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 22597 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 86 | 0% | -$1,538.90 | -56% | — |
| Sell at 2¢ | 825 | 4% | -$2,430.40 | -89% | 43 sec |
| Sell at 3¢ | 557 | 2% | -$2,427.67 | -89% | 47 sec |
| Sell at 5¢ | 403 | 2% | -$2,382.95 | -87% | 50 sec |
| Sell at 10¢ | 243 | 1% | -$2,298.57 | -84% | 63 sec |
| Sell at 25¢ | 136 | 1% | -$2,124.74 | -77% | 78 sec |
| Sell at 50¢ | 90 | 0% | -$1,897.40 | -69% | 1.5 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 809 | 5 | 11% | 3% | -41% | -81% | -84% |
| 2–5 min | 7339 | 38 | 7% | 3% | -49% | -87% | -87% |
| 1–2 min | 5824 | 23 | 3% | 2% | -57% | -92% | -92% |
| Under 1 min | 8621 | 20 | 1% | 0% | -66% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1693 | 11 | 4% | 2% | -19% | -90% | -90% |
| HYPE | 1683 | 6 | 5% | 2% | -56% | -90% | -88% |
| BNB | 1681 | 7 | 5% | 2% | -49% | -89% | -88% |
| DOGE | 1677 | 3 | 4% | 2% | -78% | -91% | -90% |
| ETH | 1676 | 9 | 6% | 3% | -35% | -87% | -86% |
| SOL | 1671 | 2 | 3% | 2% | -85% | -92% | -92% |
| XRP | 1666 | 7 | 3% | 1% | -48% | -87% | -87% |
| NEAR | 1663 | 9 | 6% | 3% | -30% | -78% | -78% |
| BTC | 1661 | 8 | 5% | 2% | -35% | -88% | -90% |
| GOLD | 864 | 1 | 3% | 1% | -86% | -92% | -94% |
| SILVER | 841 | 4 | 3% | 1% | -45% | -80% | -80% |
| WTI | 821 | 3 | 3% | 1% | -57% | -94% | -95% |
| COPPER | 735 | 2 | 2% | 1% | -75% | -84% | -84% |
| PLATINUM | 722 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 667 | 5 | 2% | 2% | -30% | -82% | -81% |
| PALLADIUM | 659 | 2 | 1% | 0% | -72% | -84% | -84% |
| EURUSD | 659 | 3 | 3% | 1% | -58% | -81% | -81% |
| GBPUSD | 615 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 574 | 3 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 200 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 169 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 11377 | 42 | 4% | 2% | -58% | -89% | -88% |
| DOWN (bought NO) | 11220 | 44 | 4% | 2% | -55% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2596 | 14 | 2% | 1% | -11% | -82% | -81% |
| 0.05–0.1% | 2630 | 8 | 3% | 2% | -56% | -92% | -91% |
| 0.1–0.2% | 3784 | 13 | 5% | 2% | -58% | -90% | -89% |
| 0.2–0.5% | 4350 | 21 | 6% | 3% | -47% | -88% | -88% |
| Over 0.5% | 1708 | 6 | 7% | 3% | -64% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5740 | 23 | 4% | 2% | -54% | -87% | -87% |
| Morning (6am–12pm) | 5315 | 27 | 4% | 2% | -42% | -87% | -86% |
| Afternoon (12–6pm) | 5311 | 19 | 3% | 1% | -57% | -88% | -89% |
| Evening (6pm–12am) | 6231 | 17 | 3% | 2% | -69% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,750 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/18 5:14:28 AM | DOGE | UP | 31 sec | -0.049% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 5:14:28 AM | SOL | DOWN | 31 sec | +0.029% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 5:14:12 AM | ETH | UP | 47 sec | -0.072% | 0¢ | ❌ Lost | $0.00 |
| 10/18 5:14:12 AM | XRP | UP | 47 sec | -0.139% | 0¢ | ❌ Lost | $0.00 |
| 10/18 5:13:43 AM | ZEC | UP | 77 sec | -0.236% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 5:12:55 AM | NEAR | UP | 2.1 min | -0.455% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 5:10:31 AM | BNB | DOWN | 4.5 min | +0.073% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 4:58:43 AM | DOGE | UP | 76 sec | -0.102% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 4:58:11 AM | XRP | UP | 1.8 min | -0.131% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 4:57:40 AM | BNB | UP | 2.3 min | -0.093% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 4:57:24 AM | NEAR | UP | 2.6 min | -0.348% | 8¢ | ❌ Lost | -$0.15 |
| 10/18 4:57:24 AM | SOL | UP | 2.6 min | -0.180% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 4:57:08 AM | ETH | UP | 2.9 min | -0.129% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 4:56:36 AM | BTC | UP | 3.4 min | -0.089% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 4:56:17 AM | HYPE | UP | 3.7 min | -0.182% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 4:55:29 AM | ZEC | UP | 4.5 min | -0.385% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 4:44:56 AM | HYPE | DOWN | 4 sec | -0.017% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 4:44:56 AM | XRP | DOWN | 4 sec | -0.015% | 0¢ | ❌ Lost | $0.00 |
| 10/18 4:44:24 AM | ZEC | DOWN | 35 sec | +0.099% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 4:44:24 AM | SOL | UP | 35 sec | -0.063% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 4:44:24 AM | BNB | DOWN | 35 sec | -0.025% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 4:44:08 AM | DOGE | UP | 51 sec | -0.084% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 4:44:08 AM | BTC | UP | 51 sec | -0.057% | 0¢ | ❌ Lost | $0.00 |
| 10/18 4:44:08 AM | NEAR | UP | 51 sec | -0.395% | 0¢ | ❌ Lost | $0.00 |
| 10/18 4:43:05 AM | ETH | UP | 1.9 min | -0.099% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 4:29:53 AM | DOGE | UP | 7 sec | -0.052% | 0¢ | ❌ Lost | $0.00 |
| 10/18 4:29:53 AM | HYPE | DOWN | 7 sec | +0.018% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 4:29:36 AM | ETH | DOWN | 24 sec | +0.003% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 4:29:36 AM | ZEC | UP | 24 sec | -0.106% | 0¢ | ❌ Lost | $0.00 |
| 10/18 4:29:36 AM | NEAR | UP | 24 sec | -0.156% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
