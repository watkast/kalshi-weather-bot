# 15-Minute 1¢ Study

*Updated Mon Oct 19, 5:29 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2056 finished bets | 1% | $91.45 | +40% | +4.45¢ | $27.65 / $63.80 |

*Expect about **95 buys a day** (~$14.22/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1892 | $72.25 | +35% |
| Momentum model ≥ 2%, hold to the close | 3155 | -$5.45 | -1% |
| Volatility model ≥ 5%, sell at 50¢ | 2056 | -$25.55 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 24249 | 24232 | 90 (0%) | 1.07% | -$1,680.90 (-57%) | Hold to the close: -$1,680.90 (-57%) |

*In play or awaiting result: 16. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 15939 | 4.6% | 0.4% (64) | -673% | ❌ Worse |
| Momentum model | 15939 | 4.6% | 0.4% (64) | -696% | ❌ Worse |
| Mean-reversion model | 15939 | 7.7% | 0.4% (64) | -808% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 15939 | 64 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3709 | 30 | -7% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 2056 | 23 | +40% | -70% | -70% | -66% |
| Volatility model ≥ 10% | 1203 | 15 | +75% | -59% | -58% | -55% |
| Momentum model ≥ 2% | 3155 | 26 | -1% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 1892 | 20 | +35% | -73% | -73% | -68% |
| Momentum model ≥ 10% | 1258 | 13 | +42% | -66% | -65% | -60% |
| Mean-reversion model ≥ 2% | 6199 | 41 | -28% | -83% | -83% | -79% |
| Mean-reversion model ≥ 5% | 4309 | 33 | -16% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2852 | 22 | -12% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16137 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5660 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2435 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 24232 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 90 | 0% | -$1,680.90 | -57% | — |
| Sell at 2¢ | 871 | 4% | -$2,602.44 | -88% | 46 sec |
| Sell at 3¢ | 590 | 2% | -$2,598.80 | -88% | 47 sec |
| Sell at 5¢ | 424 | 2% | -$2,553.30 | -87% | 50 sec |
| Sell at 10¢ | 257 | 1% | -$2,464.23 | -84% | 63 sec |
| Sell at 25¢ | 141 | 1% | -$2,278.19 | -77% | 79 sec |
| Sell at 50¢ | 93 | 0% | -$2,047.15 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 914 | 5 | 10% | 3% | -48% | -82% | -85% |
| 2–5 min | 7875 | 40 | 7% | 3% | -50% | -88% | -87% |
| 1–2 min | 6195 | 24 | 3% | 2% | -58% | -92% | -92% |
| Under 1 min | 9244 | 21 | 1% | 0% | -67% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1814 | 11 | 4% | 2% | -24% | -90% | -90% |
| HYPE | 1804 | 6 | 5% | 2% | -59% | -89% | -88% |
| BNB | 1802 | 9 | 5% | 2% | -39% | -82% | -81% |
| DOGE | 1794 | 3 | 4% | 2% | -79% | -91% | -90% |
| ETH | 1792 | 9 | 6% | 3% | -40% | -87% | -87% |
| SOL | 1789 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1783 | 7 | 3% | 1% | -52% | -87% | -87% |
| NEAR | 1780 | 9 | 6% | 3% | -35% | -79% | -79% |
| BTC | 1779 | 10 | 5% | 2% | -24% | -88% | -90% |
| GOLD | 927 | 1 | 3% | 1% | -87% | -93% | -94% |
| SILVER | 898 | 4 | 3% | 1% | -48% | -81% | -81% |
| WTI | 872 | 3 | 3% | 1% | -60% | -94% | -95% |
| COPPER | 781 | 2 | 2% | 1% | -76% | -85% | -85% |
| PLATINUM | 769 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 713 | 5 | 2% | 2% | -35% | -83% | -82% |
| EURUSD | 711 | 3 | 2% | 1% | -61% | -83% | -82% |
| PALLADIUM | 700 | 2 | 1% | 0% | -73% | -85% | -85% |
| GBPUSD | 665 | 1 | 2% | 1% | -86% | -97% | -97% |
| USDJPY | 617 | 3 | 1% | 1% | -55% | -99% | -98% |
| AUDUSD | 245 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 197 | 0 | 1% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12214 | 43 | 4% | 2% | -59% | -89% | -88% |
| DOWN (bought NO) | 12018 | 47 | 3% | 1% | -55% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2748 | 15 | 2% | 1% | -9% | -76% | -76% |
| 0.05–0.1% | 2807 | 10 | 3% | 2% | -48% | -91% | -91% |
| 0.1–0.2% | 4058 | 13 | 5% | 2% | -60% | -89% | -89% |
| 0.2–0.5% | 4694 | 22 | 6% | 3% | -49% | -88% | -88% |
| Over 0.5% | 1827 | 6 | 6% | 3% | -66% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6064 | 24 | 4% | 2% | -55% | -86% | -86% |
| Morning (6am–12pm) | 5814 | 29 | 4% | 2% | -43% | -87% | -86% |
| Afternoon (12–6pm) | 5761 | 19 | 3% | 1% | -61% | -89% | -89% |
| Evening (6pm–12am) | 6593 | 18 | 3% | 2% | -69% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,815 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/19 5:29:06 PM | PLATINUM | UP | 53 sec | — | — | In play | — |
| 10/19 5:29:06 PM | BNB | DOWN | 53 sec | +0.008% | — | In play | — |
| 10/19 5:29:06 PM | PALLADIUM | UP | 53 sec | — | — | In play | — |
| 10/19 5:29:06 PM | DOGE | DOWN | 53 sec | +0.054% | — | In play | — |
| 10/19 5:28:48 PM | AUDUSD | UP | 71 sec | — | — | In play | — |
| 10/19 5:28:16 PM | COPPER | UP | 1.7 min | — | — | In play | — |
| 10/19 5:28:01 PM | ZEC | DOWN | 2.0 min | +0.452% | — | In play | — |
| 10/19 5:28:01 PM | HYPE | DOWN | 2.0 min | +0.147% | — | In play | — |
| 10/19 5:28:01 PM | NEAR | DOWN | 2.0 min | +0.381% | — | In play | — |
| 10/19 5:27:43 PM | ETH | DOWN | 2.3 min | +0.127% | — | In play | — |
| 10/19 5:14:48 PM | PALLADIUM | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 5:14:48 PM | COPPER | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 5:14:48 PM | NATGAS | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 5:14:48 PM | HYPE | DOWN | 12 sec | +0.017% | 0¢ | ❌ Lost | $0.00 |
| 10/19 5:14:32 PM | AUDUSD | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 5:14:16 PM | BTC | UP | 44 sec | -0.045% | 0¢ | ❌ Lost | $0.00 |
| 10/19 5:14:01 PM | SOL | UP | 58 sec | -0.084% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 5:13:45 PM | NEAR | UP | 74 sec | -0.337% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 5:13:13 PM | USDJPY | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 5:13:13 PM | DOGE | UP | 1.8 min | -0.165% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 5:12:57 PM | BNB | DOWN | 2.0 min | +0.056% | 0¢ | ❌ Lost | $0.00 |
| 10/19 5:12:23 PM | GOLD | UP | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 5:11:34 PM | ZEC | UP | 3.4 min | -0.471% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 4:59:56 PM | GOLD | UP | 3 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/19 4:59:56 PM | AUDUSD | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 4:59:56 PM | WTI | UP | 3 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/19 4:59:24 PM | EURUSD | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 4:59:24 PM | SOL | DOWN | 35 sec | +0.049% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 4:59:24 PM | GBPUSD | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 4:59:24 PM | BTC | UP | 35 sec | -0.041% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
