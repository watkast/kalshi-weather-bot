# 15-Minute 1¢ Study

*Updated Mon Oct 19, 8:25 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2006 finished bets | 1% | $97.45 | +43% | +4.86¢ | $30.65 / $66.80 |

*Expect about **94 buys a day** (~$14.11/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1847 | $77.20 | +38% |
| Momentum model ≥ 2%, hold to the close | 3081 | $3.70 | +1% |
| Volatility model ≥ 5%, sell at 50¢ | 2006 | -$19.55 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 23788 | 23781 | 90 (0%) | 1.07% | -$1,626.75 (-56%) | Hold to the close: -$1,626.75 (-56%) |

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
| Volatility model | 15671 | 4.6% | 0.4% (64) | -660% | ❌ Worse |
| Momentum model | 15671 | 4.5% | 0.4% (64) | -682% | ❌ Worse |
| Mean-reversion model | 15671 | 7.7% | 0.4% (64) | -793% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 15671 | 64 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3628 | 30 | -5% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 2006 | 23 | +43% | -70% | -69% | -66% |
| Volatility model ≥ 10% | 1180 | 15 | +78% | -58% | -57% | -54% |
| Momentum model ≥ 2% | 3081 | 26 | +1% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 1847 | 20 | +38% | -73% | -73% | -68% |
| Momentum model ≥ 10% | 1225 | 13 | +46% | -65% | -64% | -59% |
| Mean-reversion model ≥ 2% | 6081 | 41 | -27% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 4224 | 33 | -14% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2800 | 22 | -10% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 15869 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5541 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2371 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 23781 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 90 | 0% | -$1,626.75 | -56% | — |
| Sell at 2¢ | 853 | 4% | -$2,552.97 | -88% | 45 sec |
| Sell at 3¢ | 580 | 2% | -$2,548.55 | -88% | 47 sec |
| Sell at 5¢ | 416 | 2% | -$2,504.35 | -87% | 50 sec |
| Sell at 10¢ | 252 | 1% | -$2,416.63 | -84% | 63 sec |
| Sell at 25¢ | 141 | 1% | -$2,224.04 | -77% | 79 sec |
| Sell at 50¢ | 93 | 0% | -$1,993.00 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 877 | 5 | 10% | 3% | -46% | -82% | -85% |
| 2–5 min | 7757 | 40 | 7% | 3% | -49% | -88% | -88% |
| 1–2 min | 6095 | 24 | 3% | 2% | -57% | -92% | -92% |
| Under 1 min | 9048 | 21 | 1% | 0% | -66% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1783 | 11 | 4% | 2% | -23% | -90% | -90% |
| HYPE | 1773 | 6 | 5% | 2% | -58% | -90% | -88% |
| BNB | 1771 | 9 | 5% | 2% | -38% | -82% | -81% |
| DOGE | 1765 | 3 | 4% | 2% | -79% | -91% | -90% |
| ETH | 1763 | 9 | 6% | 3% | -39% | -87% | -87% |
| SOL | 1760 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1754 | 7 | 3% | 1% | -51% | -87% | -88% |
| NEAR | 1750 | 9 | 6% | 3% | -34% | -79% | -79% |
| BTC | 1750 | 10 | 5% | 2% | -23% | -88% | -90% |
| GOLD | 907 | 1 | 3% | 1% | -87% | -92% | -94% |
| SILVER | 879 | 4 | 3% | 1% | -47% | -80% | -80% |
| WTI | 852 | 3 | 3% | 1% | -59% | -94% | -95% |
| COPPER | 765 | 2 | 2% | 1% | -76% | -85% | -84% |
| PLATINUM | 752 | 0 | 1% | 0% | -100% | -99% | -99% |
| EURUSD | 697 | 3 | 2% | 1% | -60% | -82% | -82% |
| NATGAS | 696 | 5 | 2% | 2% | -33% | -83% | -82% |
| PALLADIUM | 690 | 2 | 1% | 0% | -73% | -85% | -85% |
| GBPUSD | 649 | 1 | 2% | 1% | -86% | -97% | -97% |
| USDJPY | 605 | 3 | 1% | 0% | -54% | -99% | -98% |
| AUDUSD | 232 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 188 | 0 | 1% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 11974 | 43 | 4% | 2% | -59% | -89% | -88% |
| DOWN (bought NO) | 11807 | 47 | 3% | 1% | -54% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2704 | 15 | 2% | 1% | -8% | -76% | -75% |
| 0.05–0.1% | 2767 | 10 | 3% | 2% | -47% | -91% | -91% |
| 0.1–0.2% | 3985 | 13 | 4% | 2% | -60% | -90% | -89% |
| 0.2–0.5% | 4617 | 22 | 6% | 3% | -48% | -88% | -88% |
| Over 0.5% | 1793 | 6 | 6% | 3% | -66% | -88% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6064 | 24 | 4% | 2% | -55% | -86% | -86% |
| Morning (6am–12pm) | 5575 | 29 | 4% | 2% | -40% | -87% | -86% |
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
| 10/19 8:14:57 AM | BTC | DOWN | 2 sec | +0.101% | 0¢ | ❌ Lost | $0.00 |
| 10/19 8:14:41 AM | DOGE | UP | 18 sec | -0.125% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 8:14:25 AM | BNB | UP | 34 sec | -0.021% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 8:14:25 AM | AUDUSD | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 8:13:37 AM | PLATINUM | UP | 82 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 8:13:21 AM | EURUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 8:13:21 AM | NEAR | UP | 1.6 min | -0.596% | 11¢ | ❌ Lost | -$0.15 |
| 10/19 8:13:21 AM | GBPUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 8:13:05 AM | USDJPY | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 8:12:33 AM | BTC | UP | 2.4 min | -0.227% | 100¢ | ✅ Won | $13.85 |
| 10/19 8:12:33 AM | ZEC | UP | 2.4 min | -0.795% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 8:12:33 AM | SOL | UP | 2.4 min | -0.459% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 8:12:17 AM | XRP | UP | 2.7 min | -0.569% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 8:12:17 AM | COPPER | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 8:11:45 AM | PALLADIUM | UP | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 8:11:45 AM | ETH | UP | 3.2 min | -0.462% | 28¢ | ❌ Lost | -$0.15 |
| 10/19 8:11:45 AM | SILVER | UP | 3.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 8:11:29 AM | GOLD | UP | 3.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 8:11:13 AM | WTI | DOWN | 3.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 8:09:35 AM | HYPE | UP | 5.4 min | -0.967% | 1¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
