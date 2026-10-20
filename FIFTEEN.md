# 15-Minute 1¢ Study

*Updated Mon Oct 19, 10:15 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2075 finished bets | 1% | $89.20 | +38% | +4.30¢ | $26.60 / $62.60 |

*Expect about **95 buys a day** (~$14.22/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1912 | $70.00 | +33% |
| Momentum model ≥ 2%, hold to the close | 3192 | -$10.25 | -3% |
| Volatility model ≥ 5%, sell at 50¢ | 2075 | -$27.80 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 24544 | 24526 | 90 (0%) | 1.07% | -$1,718.55 (-58%) | Hold to the close: -$1,718.55 (-58%) |

*In play or awaiting result: 17. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 16100 | 4.6% | 0.4% (64) | -672% | ❌ Worse |
| Momentum model | 16100 | 4.6% | 0.4% (64) | -695% | ❌ Worse |
| Mean-reversion model | 16100 | 7.7% | 0.4% (64) | -809% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16100 | 64 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3760 | 30 | -8% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2075 | 23 | +38% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 1211 | 15 | +73% | -59% | -58% | -55% |
| Momentum model ≥ 2% | 3192 | 26 | -3% | -78% | -78% | -75% |
| Momentum model ≥ 5% | 1912 | 20 | +33% | -73% | -73% | -69% |
| Momentum model ≥ 10% | 1269 | 13 | +41% | -66% | -65% | -60% |
| Mean-reversion model ≥ 2% | 6277 | 41 | -29% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 4364 | 33 | -17% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2885 | 22 | -13% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16298 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5746 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2482 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 24526 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 90 | 0% | -$1,718.55 | -58% | — |
| Sell at 2¢ | 886 | 4% | -$2,636.19 | -89% | 45 sec |
| Sell at 3¢ | 598 | 2% | -$2,633.33 | -88% | 47 sec |
| Sell at 5¢ | 427 | 2% | -$2,589.00 | -87% | 50 sec |
| Sell at 10¢ | 260 | 1% | -$2,497.95 | -84% | 64 sec |
| Sell at 25¢ | 143 | 1% | -$2,309.22 | -78% | 79 sec |
| Sell at 50¢ | 93 | 0% | -$2,084.80 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 944 | 5 | 10% | 3% | -49% | -82% | -84% |
| 2–5 min | 7954 | 40 | 7% | 3% | -50% | -88% | -88% |
| 1–2 min | 6261 | 24 | 3% | 2% | -58% | -92% | -92% |
| Under 1 min | 9363 | 21 | 1% | 0% | -68% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1832 | 11 | 4% | 2% | -25% | -90% | -90% |
| HYPE | 1821 | 6 | 5% | 2% | -59% | -89% | -88% |
| BNB | 1821 | 9 | 5% | 2% | -39% | -82% | -81% |
| ETH | 1811 | 9 | 6% | 3% | -40% | -87% | -86% |
| DOGE | 1811 | 3 | 4% | 2% | -79% | -91% | -90% |
| SOL | 1807 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1800 | 7 | 3% | 1% | -52% | -87% | -87% |
| NEAR | 1798 | 9 | 6% | 3% | -36% | -79% | -79% |
| BTC | 1797 | 10 | 5% | 2% | -25% | -88% | -90% |
| GOLD | 942 | 1 | 3% | 1% | -87% | -93% | -94% |
| SILVER | 913 | 4 | 3% | 1% | -49% | -81% | -81% |
| WTI | 884 | 3 | 3% | 1% | -60% | -94% | -96% |
| COPPER | 791 | 2 | 2% | 1% | -76% | -85% | -85% |
| PLATINUM | 780 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 724 | 5 | 2% | 2% | -36% | -84% | -82% |
| EURUSD | 720 | 3 | 2% | 1% | -61% | -83% | -83% |
| PALLADIUM | 712 | 2 | 1% | 0% | -74% | -85% | -85% |
| GBPUSD | 676 | 1 | 2% | 1% | -86% | -97% | -97% |
| USDJPY | 628 | 3 | 1% | 1% | -55% | -99% | -98% |
| AUDUSD | 256 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 202 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12346 | 43 | 4% | 2% | -60% | -89% | -88% |
| DOWN (bought NO) | 12180 | 47 | 3% | 1% | -55% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2768 | 15 | 2% | 1% | -10% | -76% | -76% |
| 0.05–0.1% | 2833 | 10 | 3% | 2% | -49% | -92% | -91% |
| 0.1–0.2% | 4091 | 13 | 5% | 2% | -61% | -89% | -89% |
| 0.2–0.5% | 4757 | 22 | 6% | 3% | -49% | -88% | -88% |
| Over 0.5% | 1846 | 6 | 6% | 3% | -67% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6064 | 24 | 4% | 2% | -55% | -86% | -86% |
| Morning (6am–12pm) | 5814 | 29 | 4% | 2% | -43% | -87% | -86% |
| Afternoon (12–6pm) | 5807 | 19 | 3% | 1% | -61% | -89% | -89% |
| Evening (6pm–12am) | 6841 | 18 | 3% | 2% | -70% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,819 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/19 10:14:49 PM | SILVER | UP | 11 sec | — | 0¢ | In play | — |
| 10/19 10:14:34 PM | SOL | DOWN | 25 sec | +0.042% | 0¢ | In play | — |
| 10/19 10:14:34 PM | NATGAS | UP | 25 sec | — | 0¢ | In play | — |
| 10/19 10:14:34 PM | AUDUSD | UP | 25 sec | — | 0¢ | In play | — |
| 10/19 10:14:18 PM | GOLD | UP | 41 sec | — | 1¢ | In play | — |
| 10/19 10:14:02 PM | HYPE | UP | 57 sec | -0.133% | 1¢ | In play | — |
| 10/19 10:12:59 PM | BNB | UP | 2.0 min | -0.069% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 10:12:43 PM | ETH | UP | 2.3 min | -0.143% | 1¢ | In play | — |
| 10/19 10:12:26 PM | XRP | UP | 2.6 min | -0.192% | 1¢ | In play | — |
| 10/19 10:11:39 PM | NEAR | UP | 3.3 min | -0.702% | 0¢ | In play | — |
| 10/19 10:11:24 PM | DOGE | UP | 3.6 min | -0.134% | 1¢ | In play | — |
| 10/19 10:09:02 PM | ZEC | UP | 6.0 min | -0.648% | 1¢ | In play | — |
| 10/19 9:59:54 PM | WTI | UP | 6 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/19 9:59:54 PM | COPPER | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 9:59:22 PM | SOL | DOWN | 38 sec | +0.067% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 9:59:22 PM | GOLD | DOWN | 38 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/19 9:59:22 PM | USDJPY | UP | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 9:59:06 PM | ZEC | DOWN | 54 sec | +0.179% | 0¢ | ❌ Lost | $0.00 |
| 10/19 9:58:50 PM | USDCAD | UP | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 9:58:03 PM | NEAR | DOWN | 1.9 min | +0.285% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 9:57:47 PM | XRP | DOWN | 2.2 min | +0.138% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 9:57:15 PM | ETH | DOWN | 2.7 min | +0.188% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 9:57:15 PM | BTC | DOWN | 2.7 min | +0.130% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 9:57:15 PM | BNB | DOWN | 2.7 min | +0.056% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 9:56:59 PM | DOGE | DOWN | 3.0 min | +0.144% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 9:53:15 PM | HYPE | DOWN | 6.7 min | +0.241% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 9:44:57 PM | NATGAS | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 9:44:42 PM | PALLADIUM | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 9:44:42 PM | USDJPY | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 9:44:42 PM | AUDUSD | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
