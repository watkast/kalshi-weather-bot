# 15-Minute 1¢ Study

*Updated Mon Oct 19, 8:22 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2067 finished bets | 1% | $90.10 | +39% | +4.36¢ | $26.90 / $63.20 |

*Expect about **95 buys a day** (~$14.21/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1900 | $71.35 | +34% |
| Momentum model ≥ 2%, hold to the close | 3172 | -$7.70 | -2% |
| Volatility model ≥ 5%, sell at 50¢ | 2067 | -$26.90 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 24421 | 24414 | 90 (0%) | 1.07% | -$1,704.60 (-57%) | Hold to the close: -$1,704.60 (-57%) |

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
| Volatility model | 16036 | 4.6% | 0.4% (64) | -673% | ❌ Worse |
| Momentum model | 16036 | 4.6% | 0.4% (64) | -695% | ❌ Worse |
| Mean-reversion model | 16036 | 7.7% | 0.4% (64) | -809% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16036 | 64 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3734 | 30 | -8% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2067 | 23 | +39% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 1209 | 15 | +74% | -59% | -58% | -55% |
| Momentum model ≥ 2% | 3172 | 26 | -2% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 1900 | 20 | +34% | -73% | -73% | -69% |
| Momentum model ≥ 10% | 1263 | 13 | +41% | -66% | -65% | -60% |
| Mean-reversion model ≥ 2% | 6251 | 41 | -29% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 4342 | 33 | -16% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2872 | 22 | -13% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16234 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5714 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2466 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 24414 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 90 | 0% | -$1,704.60 | -57% | — |
| Sell at 2¢ | 882 | 4% | -$2,623.28 | -88% | 46 sec |
| Sell at 3¢ | 598 | 2% | -$2,619.38 | -88% | 47 sec |
| Sell at 5¢ | 427 | 2% | -$2,575.05 | -87% | 50 sec |
| Sell at 10¢ | 260 | 1% | -$2,484.00 | -84% | 64 sec |
| Sell at 25¢ | 143 | 1% | -$2,295.27 | -77% | 79 sec |
| Sell at 50¢ | 93 | 0% | -$2,070.85 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 931 | 5 | 10% | 4% | -49% | -82% | -84% |
| 2–5 min | 7927 | 40 | 7% | 3% | -50% | -88% | -87% |
| 1–2 min | 6235 | 24 | 3% | 2% | -58% | -92% | -92% |
| Under 1 min | 9317 | 21 | 1% | 0% | -67% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1825 | 11 | 4% | 2% | -25% | -90% | -90% |
| HYPE | 1814 | 6 | 5% | 2% | -59% | -89% | -88% |
| BNB | 1813 | 9 | 5% | 2% | -39% | -82% | -81% |
| ETH | 1804 | 9 | 6% | 3% | -40% | -87% | -86% |
| DOGE | 1804 | 3 | 4% | 2% | -79% | -91% | -90% |
| SOL | 1800 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1793 | 7 | 3% | 1% | -52% | -87% | -87% |
| NEAR | 1791 | 9 | 6% | 3% | -35% | -79% | -79% |
| BTC | 1790 | 10 | 5% | 2% | -25% | -88% | -90% |
| GOLD | 935 | 1 | 3% | 1% | -87% | -92% | -94% |
| SILVER | 908 | 4 | 3% | 1% | -49% | -81% | -81% |
| WTI | 878 | 3 | 3% | 1% | -60% | -94% | -96% |
| COPPER | 787 | 2 | 2% | 1% | -76% | -85% | -85% |
| PLATINUM | 776 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 721 | 5 | 2% | 2% | -35% | -83% | -82% |
| EURUSD | 717 | 3 | 3% | 1% | -61% | -83% | -83% |
| PALLADIUM | 709 | 2 | 1% | 0% | -74% | -85% | -85% |
| GBPUSD | 671 | 1 | 2% | 1% | -86% | -97% | -97% |
| USDJPY | 623 | 3 | 1% | 1% | -55% | -99% | -98% |
| AUDUSD | 254 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 201 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12306 | 43 | 4% | 2% | -60% | -89% | -88% |
| DOWN (bought NO) | 12108 | 47 | 3% | 1% | -55% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2760 | 15 | 2% | 1% | -9% | -76% | -76% |
| 0.05–0.1% | 2820 | 10 | 3% | 2% | -48% | -91% | -91% |
| 0.1–0.2% | 4076 | 13 | 5% | 2% | -61% | -89% | -89% |
| 0.2–0.5% | 4734 | 22 | 6% | 3% | -49% | -88% | -88% |
| Over 0.5% | 1841 | 6 | 6% | 3% | -66% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6064 | 24 | 4% | 2% | -55% | -86% | -86% |
| Morning (6am–12pm) | 5814 | 29 | 4% | 2% | -43% | -87% | -86% |
| Afternoon (12–6pm) | 5807 | 19 | 3% | 1% | -61% | -89% | -89% |
| Evening (6pm–12am) | 6729 | 18 | 3% | 2% | -69% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,818 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/19 8:14:50 PM | NATGAS | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 8:14:35 PM | BNB | DOWN | 25 sec | -0.022% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 8:14:35 PM | GOLD | DOWN | 25 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/19 8:14:19 PM | WTI | UP | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 8:14:03 PM | GBPUSD | DOWN | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 8:14:03 PM | EURUSD | DOWN | 57 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 10/19 8:14:03 PM | ZEC | UP | 57 sec | -0.180% | 2¢ | ❌ Lost | -$0.15 |
| 10/19 8:13:47 PM | SILVER | DOWN | 73 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 8:13:47 PM | USDJPY | UP | 73 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 8:13:32 PM | PALLADIUM | DOWN | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 8:12:28 PM | PLATINUM | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 8:12:28 PM | HYPE | UP | 2.5 min | -0.355% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 8:12:12 PM | SOL | UP | 2.8 min | -0.273% | 4¢ | ❌ Lost | -$0.15 |
| 10/19 8:12:12 PM | XRP | UP | 2.8 min | -0.277% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 8:11:56 PM | ETH | UP | 3.0 min | -0.348% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 8:11:27 PM | BTC | UP | 3.5 min | -0.198% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 8:07:30 PM | NEAR | UP | 7.5 min | -1.359% | 1¢ | ❌ Lost | $0.00 |
| 10/19 7:59:59 PM | COPPER | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:59:59 PM | USDJPY | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:59:59 PM | WTI | UP | 1 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/19 7:59:59 PM | HYPE | UP | 1 sec | -0.011% | 0¢ | ❌ Lost | $0.00 |
| 10/19 7:59:44 PM | NATGAS | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:59:44 PM | DOGE | UP | 15 sec | -0.053% | 0¢ | ❌ Lost | $0.00 |
| 10/19 7:59:44 PM | ETH | DOWN | 15 sec | +0.039% | 0¢ | ❌ Lost | $0.00 |
| 10/19 7:59:44 PM | AUDUSD | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:59:44 PM | XRP | DOWN | 15 sec | +0.023% | 0¢ | ❌ Lost | $0.00 |
| 10/19 7:59:28 PM | BNB | UP | 31 sec | -0.052% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 7:59:28 PM | GOLD | DOWN | 31 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 7:59:12 PM | GBPUSD | DOWN | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:59:12 PM | SOL | DOWN | 47 sec | +0.082% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
