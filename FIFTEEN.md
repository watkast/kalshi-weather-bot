# 15-Minute 1¢ Study

*Updated Mon Oct 19, 8:05 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2005 finished bets | 1% | $97.60 | +43% | +4.87¢ | $30.65 / $66.95 |

*Expect about **94 buys a day** (~$14.11/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1847 | $77.20 | +38% |
| Momentum model ≥ 2%, hold to the close | 3080 | $3.85 | +1% |
| Volatility model ≥ 5%, sell at 50¢ | 2005 | -$19.40 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 23768 | 23761 | 89 (0%) | 1.07% | -$1,637.90 (-57%) | Hold to the close: -$1,637.90 (-57%) |

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
| Volatility model | 15661 | 4.6% | 0.4% (63) | -666% | ❌ Worse |
| Momentum model | 15661 | 4.5% | 0.4% (63) | -689% | ❌ Worse |
| Mean-reversion model | 15661 | 7.7% | 0.4% (63) | -801% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 15661 | 63 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3627 | 30 | -5% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 2005 | 23 | +43% | -70% | -69% | -66% |
| Volatility model ≥ 10% | 1180 | 15 | +78% | -58% | -57% | -54% |
| Momentum model ≥ 2% | 3080 | 26 | +1% | -78% | -78% | -75% |
| Momentum model ≥ 5% | 1847 | 20 | +38% | -73% | -73% | -68% |
| Momentum model ≥ 10% | 1225 | 13 | +46% | -65% | -64% | -59% |
| Mean-reversion model ≥ 2% | 6080 | 41 | -26% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 4223 | 33 | -14% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2799 | 22 | -10% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 15859 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5535 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2367 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 23761 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 89 | 0% | -$1,637.90 | -57% | — |
| Sell at 2¢ | 850 | 4% | -$2,550.90 | -88% | 44 sec |
| Sell at 3¢ | 577 | 2% | -$2,546.87 | -88% | 47 sec |
| Sell at 5¢ | 413 | 2% | -$2,503.45 | -87% | 50 sec |
| Sell at 10¢ | 249 | 1% | -$2,417.71 | -84% | 63 sec |
| Sell at 25¢ | 139 | 1% | -$2,227.81 | -77% | 77 sec |
| Sell at 50¢ | 92 | 0% | -$1,996.90 | -69% | 1.5 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 876 | 5 | 10% | 3% | -46% | -82% | -85% |
| 2–5 min | 7747 | 39 | 7% | 3% | -50% | -88% | -88% |
| 1–2 min | 6090 | 24 | 3% | 2% | -57% | -92% | -92% |
| Under 1 min | 9044 | 21 | 1% | 0% | -66% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1782 | 11 | 4% | 2% | -23% | -90% | -90% |
| HYPE | 1772 | 6 | 5% | 2% | -58% | -90% | -88% |
| BNB | 1770 | 9 | 5% | 2% | -37% | -82% | -81% |
| DOGE | 1764 | 3 | 4% | 2% | -79% | -91% | -90% |
| ETH | 1762 | 9 | 6% | 3% | -39% | -87% | -87% |
| SOL | 1759 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1753 | 7 | 3% | 1% | -51% | -87% | -88% |
| NEAR | 1749 | 9 | 6% | 3% | -34% | -79% | -79% |
| BTC | 1748 | 9 | 5% | 2% | -31% | -88% | -90% |
| GOLD | 906 | 1 | 3% | 1% | -87% | -92% | -94% |
| SILVER | 878 | 4 | 3% | 1% | -47% | -80% | -80% |
| WTI | 851 | 3 | 3% | 1% | -59% | -94% | -95% |
| COPPER | 764 | 2 | 2% | 1% | -76% | -85% | -84% |
| PLATINUM | 751 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 696 | 5 | 2% | 2% | -33% | -83% | -82% |
| EURUSD | 696 | 3 | 2% | 1% | -60% | -82% | -82% |
| PALLADIUM | 689 | 2 | 1% | 0% | -73% | -85% | -85% |
| GBPUSD | 648 | 1 | 2% | 1% | -86% | -97% | -97% |
| USDJPY | 604 | 3 | 1% | 0% | -54% | -99% | -98% |
| AUDUSD | 231 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 188 | 0 | 1% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 11957 | 42 | 4% | 2% | -60% | -89% | -88% |
| DOWN (bought NO) | 11804 | 47 | 3% | 1% | -54% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2703 | 15 | 2% | 1% | -8% | -76% | -75% |
| 0.05–0.1% | 2767 | 10 | 3% | 2% | -47% | -91% | -91% |
| 0.1–0.2% | 3983 | 13 | 4% | 2% | -60% | -90% | -89% |
| 0.2–0.5% | 4614 | 21 | 6% | 3% | -50% | -88% | -88% |
| Over 0.5% | 1789 | 6 | 6% | 3% | -65% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6064 | 24 | 4% | 2% | -55% | -86% | -86% |
| Morning (6am–12pm) | 5555 | 28 | 4% | 2% | -42% | -87% | -86% |
| Afternoon (12–6pm) | 5549 | 19 | 3% | 1% | -59% | -88% | -89% |
| Evening (6pm–12am) | 6593 | 18 | 3% | 2% | -69% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,812 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/19 7:59:48 AM | PALLADIUM | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:59:48 AM | EURUSD | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:59:32 AM | GBPUSD | DOWN | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:59:32 AM | COPPER | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:59:16 AM | BNB | UP | 43 sec | -0.107% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:59:00 AM | USDCAD | UP | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:59:00 AM | NEAR | UP | 60 sec | -0.657% | 0¢ | ❌ Lost | $0.00 |
| 10/19 7:59:00 AM | NATGAS | UP | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:58:10 AM | XRP | UP | 1.8 min | -0.307% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:58:10 AM | BTC | UP | 1.8 min | -0.193% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:57:55 AM | HYPE | UP | 2.1 min | -0.359% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 7:57:55 AM | DOGE | UP | 2.1 min | -0.288% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 7:57:06 AM | AUDUSD | DOWN | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:57:06 AM | WTI | UP | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 7:55:14 AM | ZEC | UP | 4.8 min | -0.790% | 3¢ | ❌ Lost | -$0.15 |
| 10/19 7:55:14 AM | ETH | UP | 4.8 min | -0.422% | 2¢ | ❌ Lost | -$0.15 |
| 10/19 7:55:14 AM | SOL | UP | 4.8 min | -0.547% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 7:44:58 AM | COPPER | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:44:38 AM | NEAR | UP | 22 sec | -0.456% | 0¢ | ❌ Lost | $0.00 |
| 10/19 7:44:38 AM | NATGAS | UP | 22 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 7:43:50 AM | USDJPY | DOWN | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:43:34 AM | EURUSD | UP | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:43:18 AM | GBPUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:43:18 AM | AUDUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:43:18 AM | USDCAD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:43:02 AM | PALLADIUM | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:43:02 AM | PLATINUM | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:43:02 AM | WTI | DOWN | 2.0 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/19 7:43:02 AM | HYPE | UP | 2.0 min | -0.324% | 4¢ | ❌ Lost | -$0.15 |
| 10/19 7:42:46 AM | GOLD | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
