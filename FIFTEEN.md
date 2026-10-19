# 15-Minute 1¢ Study

*Updated Sun Oct 18, 10:58 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1983 finished bets | 1% | $86.60 | +39% | +4.37¢ | $31.85 / $54.75 |

*Expect about **95 buys a day** (~$14.22/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1823 | $66.35 | +33% |
| Momentum model ≥ 2%, hold to the close | 3036 | -$4.45 | -1% |
| Volatility model ≥ 2%, hold to the close | 3583 | -$29.45 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 23322 | 23309 | 88 (0%) | 1.07% | -$1,594.00 (-56%) | Hold to the close: -$1,594.00 (-56%) |

*In play or awaiting result: 12. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 15425 | 4.6% | 0.4% (62) | -673% | ❌ Worse |
| Momentum model | 15425 | 4.6% | 0.4% (62) | -696% | ❌ Worse |
| Mean-reversion model | 15425 | 7.7% | 0.4% (62) | -807% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 15425 | 62 | -50% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 3583 | 29 | -7% | -80% | -79% | -75% |
| Volatility model ≥ 5% | 1983 | 22 | +39% | -76% | -75% | -72% |
| Volatility model ≥ 10% | 1166 | 14 | +69% | -70% | -68% | -66% |
| Momentum model ≥ 2% | 3036 | 25 | -1% | -82% | -82% | -78% |
| Momentum model ≥ 5% | 1823 | 19 | +33% | -80% | -79% | -75% |
| Momentum model ≥ 10% | 1215 | 12 | +36% | -76% | -75% | -70% |
| Mean-reversion model ≥ 2% | 5991 | 40 | -27% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 4164 | 32 | -15% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 2757 | 21 | -13% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 15623 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5409 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2277 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 23309 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 88 | 0% | -$1,594.00 | -56% | — |
| Sell at 2¢ | 840 | 4% | -$2,509.60 | -89% | 44 sec |
| Sell at 3¢ | 569 | 2% | -$2,506.09 | -89% | 47 sec |
| Sell at 5¢ | 408 | 2% | -$2,462.80 | -87% | 50 sec |
| Sell at 10¢ | 247 | 1% | -$2,376.43 | -84% | 63 sec |
| Sell at 25¢ | 137 | 1% | -$2,190.53 | -78% | 77 sec |
| Sell at 50¢ | 91 | 0% | -$1,959.75 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 857 | 5 | 10% | 3% | -45% | -82% | -85% |
| 2–5 min | 7602 | 39 | 7% | 3% | -49% | -88% | -88% |
| 1–2 min | 5974 | 24 | 3% | 2% | -56% | -92% | -92% |
| Under 1 min | 8872 | 20 | 1% | 0% | -67% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1755 | 11 | 4% | 2% | -22% | -90% | -90% |
| HYPE | 1745 | 6 | 5% | 2% | -58% | -90% | -88% |
| BNB | 1745 | 8 | 5% | 2% | -44% | -89% | -88% |
| DOGE | 1740 | 3 | 4% | 2% | -79% | -91% | -90% |
| ETH | 1735 | 9 | 6% | 3% | -38% | -87% | -87% |
| SOL | 1732 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1727 | 7 | 3% | 1% | -50% | -87% | -88% |
| NEAR | 1723 | 9 | 6% | 3% | -33% | -79% | -79% |
| BTC | 1721 | 9 | 5% | 2% | -30% | -89% | -90% |
| GOLD | 883 | 1 | 4% | 1% | -87% | -92% | -94% |
| SILVER | 858 | 4 | 3% | 1% | -46% | -80% | -80% |
| WTI | 835 | 3 | 3% | 1% | -58% | -94% | -95% |
| COPPER | 747 | 2 | 2% | 1% | -75% | -84% | -84% |
| PLATINUM | 733 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 681 | 5 | 2% | 2% | -31% | -82% | -81% |
| EURUSD | 677 | 3 | 3% | 1% | -59% | -82% | -82% |
| PALLADIUM | 672 | 2 | 1% | 0% | -72% | -84% | -85% |
| GBPUSD | 628 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 586 | 3 | 1% | 1% | -52% | -99% | -98% |
| AUDUSD | 215 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 171 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 11713 | 42 | 4% | 2% | -59% | -89% | -88% |
| DOWN (bought NO) | 11596 | 46 | 3% | 2% | -54% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2672 | 14 | 2% | 1% | -13% | -82% | -81% |
| 0.05–0.1% | 2717 | 10 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 3913 | 13 | 4% | 2% | -59% | -90% | -89% |
| 0.2–0.5% | 4548 | 21 | 6% | 3% | -49% | -88% | -88% |
| Over 0.5% | 1770 | 6 | 6% | 3% | -65% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5767 | 23 | 4% | 2% | -55% | -87% | -88% |
| Morning (6am–12pm) | 5489 | 28 | 4% | 2% | -41% | -87% | -86% |
| Afternoon (12–6pm) | 5549 | 19 | 3% | 1% | -59% | -88% | -89% |
| Evening (6pm–12am) | 6504 | 18 | 3% | 2% | -68% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,861 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/18 10:58:33 PM | ZEC | UP | 86 sec | -0.294% | — | In play | — |
| 10/18 10:58:33 PM | PALLADIUM | DOWN | 86 sec | — | — | In play | — |
| 10/18 10:58:11 PM | SILVER | DOWN | 1.8 min | — | — | In play | — |
| 10/18 10:57:30 PM | GOLD | DOWN | 2.5 min | — | — | In play | — |
| 10/18 10:57:26 PM | BNB | DOWN | 2.6 min | +0.033% | — | In play | — |
| 10/18 10:52:33 PM | HYPE | DOWN | 7.4 min | +0.562% | — | In play | — |
| 10/18 10:44:56 PM | PALLADIUM | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 10:44:40 PM | PLATINUM | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 10:44:24 PM | NATGAS | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 10:44:20 PM | AUDUSD | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 10:43:22 PM | SILVER | DOWN | 1.6 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/18 10:42:29 PM | GBPUSD | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 10:40:58 PM | EURUSD | DOWN | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 10:40:43 PM | NEAR | DOWN | 4.3 min | +0.680% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 10:40:43 PM | ZEC | DOWN | 4.3 min | +0.556% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 10:40:35 PM | DOGE | DOWN | 4.4 min | +0.192% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 10:40:33 PM | BTC | DOWN | 4.4 min | +0.241% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 10:40:27 PM | XRP | DOWN | 4.5 min | +0.199% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 10:40:13 PM | BNB | DOWN | 4.8 min | +0.094% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 10:39:57 PM | HYPE | DOWN | 5.0 min | +0.319% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 10:39:41 PM | SOL | DOWN | 5.3 min | +0.331% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 10:39:21 PM | ETH | DOWN | 5.6 min | +0.225% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 10:37:26 PM | GOLD | DOWN | 7.5 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/18 10:29:58 PM | BNB | DOWN | 2 sec | -0.054% | 0¢ | ❌ Lost | $0.00 |
| 10/18 10:29:40 PM | SOL | UP | 20 sec | -0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/18 10:29:32 PM | AUDUSD | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 10:29:20 PM | NEAR | UP | 39 sec | -0.207% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 10:29:20 PM | PALLADIUM | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 10:29:20 PM | GBPUSD | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 10:29:20 PM | EURUSD | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
