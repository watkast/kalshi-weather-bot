# 15-Minute 1¢ Study

*Updated Mon Oct 19, 8:02 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2065 finished bets | 1% | $90.40 | +39% | +4.38¢ | $27.05 / $63.35 |

*Expect about **95 buys a day** (~$14.20/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1898 | $71.65 | +34% |
| Momentum model ≥ 2%, hold to the close | 3168 | -$7.10 | -2% |
| Volatility model ≥ 5%, sell at 50¢ | 2065 | -$26.60 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 24404 | 24397 | 90 (0%) | 1.07% | -$1,702.35 (-57%) | Hold to the close: -$1,702.35 (-57%) |

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
| Volatility model | 16028 | 4.6% | 0.4% (64) | -672% | ❌ Worse |
| Momentum model | 16028 | 4.6% | 0.4% (64) | -695% | ❌ Worse |
| Mean-reversion model | 16028 | 7.7% | 0.4% (64) | -808% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16028 | 64 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3729 | 30 | -8% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2065 | 23 | +39% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 1208 | 15 | +74% | -59% | -58% | -55% |
| Momentum model ≥ 2% | 3168 | 26 | -2% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 1898 | 20 | +34% | -73% | -73% | -68% |
| Momentum model ≥ 10% | 1262 | 13 | +42% | -66% | -65% | -60% |
| Mean-reversion model ≥ 2% | 6245 | 41 | -28% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 4338 | 33 | -16% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2869 | 22 | -13% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16226 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5708 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2463 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 24397 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 90 | 0% | -$1,702.35 | -57% | — |
| Sell at 2¢ | 880 | 4% | -$2,621.55 | -88% | 46 sec |
| Sell at 3¢ | 597 | 2% | -$2,617.52 | -88% | 47 sec |
| Sell at 5¢ | 427 | 2% | -$2,572.80 | -87% | 50 sec |
| Sell at 10¢ | 260 | 1% | -$2,481.75 | -84% | 64 sec |
| Sell at 25¢ | 143 | 1% | -$2,293.02 | -77% | 79 sec |
| Sell at 50¢ | 93 | 0% | -$2,068.60 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 930 | 5 | 10% | 4% | -49% | -82% | -84% |
| 2–5 min | 7921 | 40 | 7% | 3% | -50% | -88% | -88% |
| 1–2 min | 6232 | 24 | 3% | 2% | -58% | -92% | -92% |
| Under 1 min | 9310 | 21 | 1% | 0% | -67% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1824 | 11 | 4% | 2% | -25% | -90% | -90% |
| HYPE | 1813 | 6 | 5% | 2% | -59% | -89% | -88% |
| BNB | 1812 | 9 | 5% | 2% | -39% | -82% | -81% |
| DOGE | 1804 | 3 | 4% | 2% | -79% | -91% | -90% |
| ETH | 1803 | 9 | 6% | 3% | -40% | -87% | -86% |
| SOL | 1799 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1792 | 7 | 3% | 1% | -52% | -87% | -87% |
| NEAR | 1790 | 9 | 6% | 3% | -35% | -79% | -79% |
| BTC | 1789 | 10 | 5% | 2% | -25% | -88% | -90% |
| GOLD | 934 | 1 | 3% | 1% | -87% | -92% | -94% |
| SILVER | 907 | 4 | 3% | 1% | -49% | -81% | -80% |
| WTI | 877 | 3 | 3% | 1% | -60% | -94% | -96% |
| COPPER | 787 | 2 | 2% | 1% | -76% | -85% | -85% |
| PLATINUM | 775 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 720 | 5 | 2% | 2% | -35% | -83% | -82% |
| EURUSD | 716 | 3 | 2% | 1% | -61% | -83% | -83% |
| PALLADIUM | 708 | 2 | 1% | 0% | -74% | -85% | -85% |
| GBPUSD | 670 | 1 | 2% | 1% | -86% | -97% | -97% |
| USDJPY | 622 | 3 | 1% | 1% | -55% | -99% | -98% |
| AUDUSD | 254 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 201 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12297 | 43 | 4% | 2% | -60% | -89% | -88% |
| DOWN (bought NO) | 12100 | 47 | 3% | 1% | -55% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2759 | 15 | 2% | 1% | -9% | -76% | -76% |
| 0.05–0.1% | 2820 | 10 | 3% | 2% | -48% | -91% | -91% |
| 0.1–0.2% | 4074 | 13 | 5% | 2% | -61% | -89% | -89% |
| 0.2–0.5% | 4730 | 22 | 6% | 3% | -49% | -88% | -88% |
| Over 0.5% | 1840 | 6 | 6% | 3% | -66% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6064 | 24 | 4% | 2% | -55% | -86% | -86% |
| Morning (6am–12pm) | 5814 | 29 | 4% | 2% | -43% | -87% | -86% |
| Afternoon (12–6pm) | 5807 | 19 | 3% | 1% | -61% | -89% | -89% |
| Evening (6pm–12am) | 6712 | 18 | 3% | 2% | -69% | -92% | -91% |

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
| 10/19 7:59:12 PM | ZEC | UP | 47 sec | -0.234% | 0¢ | ❌ Lost | $0.00 |
| 10/19 7:58:56 PM | NEAR | UP | 64 sec | -0.396% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 7:58:56 PM | PALLADIUM | DOWN | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:58:39 PM | EURUSD | DOWN | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:58:23 PM | USDCAD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:57:37 PM | PLATINUM | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:56:49 PM | SILVER | DOWN | 3.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 7:56:18 PM | BTC | DOWN | 3.7 min | +0.173% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 7:44:57 PM | SILVER | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:44:57 PM | AUDUSD | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:44:42 PM | PLATINUM | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:44:26 PM | NATGAS | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:44:26 PM | COPPER | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:44:26 PM | USDCAD | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:44:26 PM | PALLADIUM | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:43:54 PM | WTI | UP | 66 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 7:42:20 PM | BNB | DOWN | 2.7 min | +0.136% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
