# 15-Minute 1¢ Study

*Updated Fri Oct 30, 11:07 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3178 finished bets | 1% | $92.50 | +26% | +2.91¢ | $75.45 / $17.05 |

*Expect about **98 buys a day** (~$14.70/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2943 | $42.25 | +13% |
| Volatility model ≥ 2%, hold to the close | 5893 | $13.25 | +2% |
| Momentum model ≥ 2%, hold to the close | 4861 | -$59.70 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 39734 | 39724 | 146 (0%) | 1.07% | -$2,810.15 (-58%) | Hold to the close: -$2,810.15 (-58%) |

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
| Volatility model | 24277 | 4.6% | 0.4% (95) | -676% | ❌ Worse |
| Momentum model | 24277 | 4.5% | 0.4% (95) | -699% | ❌ Worse |
| Mean-reversion model | 24277 | 8.0% | 0.4% (95) | -824% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 24277 | 95 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5893 | 52 | +2% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3178 | 32 | +26% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1793 | 19 | +51% | -69% | -67% | -64% |
| Momentum model ≥ 2% | 4861 | 36 | -11% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2943 | 26 | +13% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1915 | 17 | +23% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9964 | 66 | -28% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 6974 | 56 | -11% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4646 | 39 | -5% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 24478 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9619 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5627 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 39724 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 146 | 0% | -$2,810.15 | -58% | — |
| Sell at 2¢ | 1530 | 4% | -$4,260.35 | -88% | 47 sec |
| Sell at 3¢ | 1055 | 3% | -$4,246.70 | -87% | 49 sec |
| Sell at 5¢ | 735 | 2% | -$4,166.40 | -86% | 63 sec |
| Sell at 10¢ | 443 | 1% | -$3,993.82 | -82% | 65 sec |
| Sell at 25¢ | 231 | 1% | -$3,697.54 | -76% | 83 sec |
| Sell at 50¢ | 150 | 0% | -$3,365.65 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1852 | 8 | 11% | 4% | -59% | -80% | -81% |
| 2–5 min | 12671 | 70 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10063 | 35 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 15127 | 33 | 1% | 0% | -69% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2739 | 13 | 5% | 3% | -39% | -88% | -88% |
| HYPE | 2733 | 8 | 5% | 3% | -64% | -89% | -87% |
| BNB | 2732 | 16 | 5% | 3% | -27% | -84% | -83% |
| SOL | 2727 | 7 | 4% | 2% | -68% | -91% | -91% |
| ETH | 2720 | 11 | 6% | 3% | -51% | -86% | -85% |
| DOGE | 2720 | 6 | 4% | 2% | -72% | -90% | -89% |
| BTC | 2703 | 13 | 5% | 2% | -35% | -88% | -89% |
| NEAR | 2702 | 12 | 5% | 2% | -42% | -83% | -83% |
| XRP | 2702 | 11 | 3% | 1% | -50% | -89% | -89% |
| GOLD | 1505 | 5 | 5% | 2% | -60% | -82% | -84% |
| SILVER | 1471 | 7 | 4% | 2% | -44% | -82% | -81% |
| WTI | 1451 | 4 | 3% | 1% | -67% | -92% | -93% |
| PLATINUM | 1307 | 3 | 2% | 1% | -79% | -96% | -96% |
| COPPER | 1245 | 5 | 1% | 1% | -63% | -75% | -75% |
| EURUSD | 1244 | 3 | 2% | 1% | -77% | -88% | -88% |
| NATGAS | 1201 | 7 | 2% | 1% | -46% | -81% | -80% |
| GBPUSD | 1179 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1170 | 2 | 1% | 0% | -84% | -90% | -90% |
| USDJPY | 1164 | 5 | 2% | 1% | -60% | -97% | -96% |
| AUDUSD | 701 | 4 | 2% | 1% | -47% | -84% | -83% |
| USDCAD | 676 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 269 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 179 | 0 | 6% | 2% | -100% | -90% | -88% |
| 30YRRATE | 171 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 164 | 1 | 5% | 1% | -43% | -35% | -34% |
| 5YRRATE | 149 | 1 | 6% | 3% | -37% | -90% | -91% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 20188 | 81 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 19536 | 65 | 4% | 2% | -62% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3907 | 19 | 2% | 1% | -16% | -81% | -81% |
| 0.05–0.1% | 4144 | 14 | 3% | 2% | -49% | -92% | -92% |
| 0.1–0.2% | 6287 | 22 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 7307 | 32 | 6% | 3% | -51% | -87% | -86% |
| Over 0.5% | 2829 | 10 | 7% | 3% | -64% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9916 | 36 | 4% | 2% | -59% | -86% | -86% |
| Morning (6am–12pm) | 10050 | 45 | 4% | 2% | -49% | -86% | -85% |
| Afternoon (12–6pm) | 9178 | 31 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 10580 | 34 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,452 |
| Time from buy to best bounce (bounced bets) | 52 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/30 10:59:51 AM | BNB | DOWN | 9 sec | +0.011% | 0¢ | ❌ Lost | $0.00 |
| 10/30 10:59:51 AM | EURUSD | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 10:59:51 AM | GOLD | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 10:59:35 AM | AUDUSD | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 10:59:18 AM | SILVER | DOWN | 41 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/30 10:58:59 AM | 30YRRATE | UP | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 10:58:27 AM | ETH | UP | 1.5 min | -0.238% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 10:58:27 AM | SOL | UP | 1.5 min | -0.296% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 10:58:27 AM | XRP | UP | 1.5 min | -0.361% | 0¢ | ❌ Lost | $0.00 |
| 10/30 10:58:12 AM | DOGE | UP | 1.8 min | -0.284% | 0¢ | ❌ Lost | $0.00 |
| 10/30 10:58:12 AM | NATGAS | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 10:58:12 AM | USDCAD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 10:58:12 AM | BTC | UP | 1.8 min | -0.236% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 10:58:12 AM | NEAR | UP | 1.8 min | -0.775% | 0¢ | ❌ Lost | $0.00 |
| 10/30 10:58:12 AM | PLATINUM | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 10:58:12 AM | GBPUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 10:57:55 AM | USDJPY | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 10:57:39 AM | COPPER | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 10:57:06 AM | WTI | DOWN | 2.9 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/30 10:55:41 AM | BRENT | DOWN | 4.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 10:55:41 AM | ZEC | UP | 4.3 min | -1.000% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 10:55:25 AM | HYPE | UP | 4.6 min | -0.704% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 10:52:09 AM | 10YRRATE | UP | 7.8 min | — | 5¢ | ❌ Lost | -$0.15 |
| 10/30 10:48:24 AM | 2YRRATE | UP | 11.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 10:48:24 AM | 5YRRATE | UP | 11.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/30 10:44:45 AM | GBPUSD | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 10:44:45 AM | NATGAS | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 10:44:28 AM | ZEC | DOWN | 31 sec | +0.103% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 10:43:54 AM | HYPE | DOWN | 65 sec | +0.311% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 10:43:54 AM | COPPER | UP | 65 sec | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
