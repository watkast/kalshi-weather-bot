# 15-Minute 1¢ Study

*Updated Mon Oct 19, 9:27 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2019 finished bets | 1% | $95.80 | +42% | +4.74¢ | $30.05 / $65.75 |

*Expect about **95 buys a day** (~$14.21/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1863 | $75.25 | +37% |
| Momentum model ≥ 2%, hold to the close | 3098 | $1.60 | +0% |
| Volatility model ≥ 5%, sell at 50¢ | 2019 | -$21.20 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 23859 | 23840 | 90 (0%) | 1.07% | -$1,633.80 (-56%) | Hold to the close: -$1,633.80 (-56%) |

*In play or awaiting result: 18. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 15703 | 4.6% | 0.4% (64) | -661% | ❌ Worse |
| Momentum model | 15703 | 4.5% | 0.4% (64) | -683% | ❌ Worse |
| Mean-reversion model | 15703 | 7.7% | 0.4% (64) | -794% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 15703 | 64 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3645 | 30 | -5% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 2019 | 23 | +42% | -70% | -70% | -66% |
| Volatility model ≥ 10% | 1183 | 15 | +77% | -58% | -57% | -54% |
| Momentum model ≥ 2% | 3098 | 26 | +0% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 1863 | 20 | +37% | -73% | -73% | -68% |
| Momentum model ≥ 10% | 1237 | 13 | +44% | -65% | -65% | -60% |
| Mean-reversion model ≥ 2% | 6098 | 41 | -27% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 4234 | 33 | -14% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2804 | 22 | -10% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 15901 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5558 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2381 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 23840 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 90 | 0% | -$1,633.80 | -56% | — |
| Sell at 2¢ | 854 | 4% | -$2,559.76 | -88% | 45 sec |
| Sell at 3¢ | 581 | 2% | -$2,555.21 | -88% | 47 sec |
| Sell at 5¢ | 417 | 2% | -$2,510.75 | -87% | 50 sec |
| Sell at 10¢ | 253 | 1% | -$2,422.37 | -84% | 63 sec |
| Sell at 25¢ | 141 | 1% | -$2,231.09 | -77% | 79 sec |
| Sell at 50¢ | 93 | 0% | -$2,000.05 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 878 | 5 | 10% | 3% | -46% | -82% | -85% |
| 2–5 min | 7771 | 40 | 7% | 3% | -49% | -88% | -88% |
| 1–2 min | 6107 | 24 | 3% | 2% | -57% | -92% | -92% |
| Under 1 min | 9080 | 21 | 1% | 0% | -66% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1787 | 11 | 4% | 2% | -23% | -90% | -90% |
| HYPE | 1777 | 6 | 5% | 2% | -58% | -90% | -88% |
| BNB | 1775 | 9 | 5% | 2% | -38% | -82% | -81% |
| DOGE | 1768 | 3 | 4% | 2% | -79% | -91% | -90% |
| ETH | 1767 | 9 | 6% | 3% | -39% | -87% | -87% |
| SOL | 1762 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1758 | 7 | 3% | 1% | -51% | -87% | -88% |
| NEAR | 1754 | 9 | 6% | 3% | -34% | -79% | -79% |
| BTC | 1753 | 10 | 5% | 2% | -23% | -88% | -90% |
| GOLD | 910 | 1 | 3% | 1% | -87% | -93% | -94% |
| SILVER | 882 | 4 | 3% | 1% | -48% | -80% | -80% |
| WTI | 854 | 3 | 3% | 1% | -59% | -94% | -95% |
| COPPER | 769 | 2 | 2% | 1% | -76% | -85% | -84% |
| PLATINUM | 755 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 698 | 5 | 2% | 2% | -33% | -83% | -82% |
| EURUSD | 698 | 3 | 2% | 1% | -60% | -82% | -82% |
| PALLADIUM | 690 | 2 | 1% | 0% | -73% | -85% | -85% |
| GBPUSD | 650 | 1 | 2% | 1% | -86% | -97% | -97% |
| USDJPY | 607 | 3 | 1% | 0% | -54% | -99% | -98% |
| AUDUSD | 235 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 191 | 0 | 1% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12001 | 43 | 4% | 2% | -59% | -89% | -88% |
| DOWN (bought NO) | 11839 | 47 | 3% | 1% | -54% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2706 | 15 | 2% | 1% | -8% | -76% | -75% |
| 0.05–0.1% | 2769 | 10 | 3% | 2% | -47% | -91% | -91% |
| 0.1–0.2% | 4000 | 13 | 4% | 2% | -60% | -90% | -89% |
| 0.2–0.5% | 4627 | 22 | 6% | 3% | -48% | -88% | -88% |
| Over 0.5% | 1796 | 6 | 6% | 3% | -66% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6064 | 24 | 4% | 2% | -55% | -86% | -86% |
| Morning (6am–12pm) | 5634 | 29 | 4% | 2% | -41% | -87% | -86% |
| Afternoon (12–6pm) | 5549 | 19 | 3% | 1% | -59% | -88% | -89% |
| Evening (6pm–12am) | 6593 | 18 | 3% | 2% | -69% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,806 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/19 9:27:14 AM | ZEC | DOWN | 2.8 min | +0.800% | — | In play | — |
| 10/19 9:27:14 AM | XRP | DOWN | 2.8 min | +0.268% | — | In play | — |
| 10/19 9:27:14 AM | SILVER | DOWN | 2.8 min | — | — | In play | — |
| 10/19 9:26:59 AM | EURUSD | DOWN | 3.0 min | — | — | In play | — |
| 10/19 9:26:43 AM | SOL | DOWN | 3.3 min | +0.338% | — | In play | — |
| 10/19 9:26:27 AM | COPPER | DOWN | 3.5 min | — | — | In play | — |
| 10/19 9:25:22 AM | BNB | DOWN | 4.6 min | +0.193% | — | In play | — |
| 10/19 9:25:22 AM | DOGE | DOWN | 4.6 min | +0.436% | — | In play | — |
| 10/19 9:25:06 AM | BTC | DOWN | 4.9 min | +0.351% | — | In play | — |
| 10/19 9:24:51 AM | NEAR | DOWN | 5.1 min | +1.219% | — | In play | — |
| 10/19 9:24:51 AM | ETH | DOWN | 5.1 min | +0.455% | — | In play | — |
| 10/19 9:24:35 AM | HYPE | DOWN | 5.4 min | +0.690% | — | In play | — |
| 10/19 9:14:46 AM | ZEC | UP | 14 sec | -0.194% | 0¢ | ❌ Lost | $0.00 |
| 10/19 9:14:46 AM | GOLD | DOWN | 14 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/19 9:14:46 AM | DOGE | UP | 14 sec | -0.107% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 9:14:46 AM | ETH | DOWN | 14 sec | -0.022% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 9:14:14 AM | GBPUSD | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 9:14:14 AM | NEAR | UP | 46 sec | -0.491% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 9:14:14 AM | SILVER | DOWN | 46 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 9:13:58 AM | HYPE | DOWN | 62 sec | +0.170% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 9:13:58 AM | EURUSD | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 9:13:41 AM | PLATINUM | DOWN | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 9:13:41 AM | XRP | DOWN | 78 sec | +0.176% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 9:13:41 AM | SOL | DOWN | 78 sec | +0.191% | 0¢ | ❌ Lost | $0.00 |
| 10/19 9:13:25 AM | COPPER | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 9:12:53 AM | AUDUSD | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 9:12:05 AM | BNB | UP | 2.9 min | -0.117% | 13¢ | ❌ Lost | -$0.15 |
| 10/19 9:11:49 AM | USDCAD | DOWN | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 8:59:55 AM | SILVER | UP | 5 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 8:59:55 AM | GOLD | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
