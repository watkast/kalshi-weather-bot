# 15-Minute 1¢ Study

*Updated Sun Oct 18, 7:44 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1973 finished bets | 1% | $87.50 | +40% | +4.43¢ | $32.45 / $55.05 |

*Expect about **95 buys a day** (~$14.24/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1812 | $67.40 | +34% |
| Momentum model ≥ 2%, hold to the close | 3018 | -$2.50 | -1% |
| Volatility model ≥ 2%, hold to the close | 3554 | -$25.70 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 23140 | 23119 | 88 (0%) | 1.07% | -$1,572.10 (-56%) | Hold to the close: -$1,572.10 (-56%) |

*In play or awaiting result: 20. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 15316 | 4.6% | 0.4% (62) | -670% | ❌ Worse |
| Momentum model | 15316 | 4.6% | 0.4% (62) | -692% | ❌ Worse |
| Mean-reversion model | 15316 | 7.7% | 0.4% (62) | -803% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 15316 | 62 | -49% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 3554 | 29 | -6% | -80% | -79% | -75% |
| Volatility model ≥ 5% | 1973 | 22 | +40% | -76% | -75% | -72% |
| Volatility model ≥ 10% | 1160 | 14 | +70% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 3018 | 25 | -1% | -82% | -82% | -78% |
| Momentum model ≥ 5% | 1812 | 19 | +34% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 1207 | 12 | +37% | -76% | -75% | -70% |
| Mean-reversion model ≥ 2% | 5940 | 40 | -27% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 4129 | 32 | -14% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 2733 | 21 | -12% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 15514 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5357 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2248 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 23119 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 88 | 0% | -$1,572.10 | -56% | — |
| Sell at 2¢ | 839 | 4% | -$2,487.96 | -89% | 44 sec |
| Sell at 3¢ | 569 | 2% | -$2,484.19 | -89% | 47 sec |
| Sell at 5¢ | 408 | 2% | -$2,440.90 | -87% | 50 sec |
| Sell at 10¢ | 247 | 1% | -$2,354.53 | -84% | 63 sec |
| Sell at 25¢ | 137 | 1% | -$2,168.63 | -77% | 77 sec |
| Sell at 50¢ | 91 | 0% | -$1,937.85 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 842 | 5 | 10% | 3% | -44% | -82% | -84% |
| 2–5 min | 7544 | 39 | 7% | 3% | -49% | -88% | -87% |
| 1–2 min | 5935 | 24 | 3% | 2% | -56% | -92% | -92% |
| Under 1 min | 8794 | 20 | 1% | 0% | -67% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1743 | 11 | 4% | 2% | -22% | -90% | -90% |
| BNB | 1733 | 8 | 5% | 2% | -43% | -89% | -88% |
| HYPE | 1732 | 6 | 5% | 2% | -57% | -90% | -88% |
| DOGE | 1727 | 3 | 4% | 2% | -78% | -90% | -90% |
| ETH | 1724 | 9 | 6% | 3% | -37% | -87% | -87% |
| SOL | 1721 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1715 | 7 | 3% | 1% | -50% | -87% | -87% |
| NEAR | 1710 | 9 | 6% | 3% | -32% | -79% | -79% |
| BTC | 1709 | 9 | 5% | 2% | -29% | -88% | -90% |
| GOLD | 873 | 1 | 3% | 1% | -86% | -92% | -94% |
| SILVER | 849 | 4 | 3% | 1% | -46% | -80% | -80% |
| WTI | 830 | 3 | 3% | 1% | -58% | -94% | -95% |
| COPPER | 739 | 2 | 2% | 1% | -75% | -84% | -84% |
| PLATINUM | 727 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 675 | 5 | 2% | 2% | -31% | -82% | -81% |
| EURUSD | 668 | 3 | 3% | 1% | -58% | -82% | -81% |
| PALLADIUM | 664 | 2 | 1% | 0% | -72% | -84% | -84% |
| GBPUSD | 621 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 581 | 3 | 1% | 1% | -52% | -99% | -98% |
| AUDUSD | 208 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 170 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 11627 | 42 | 4% | 2% | -58% | -89% | -88% |
| DOWN (bought NO) | 11492 | 46 | 3% | 2% | -54% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2657 | 14 | 2% | 1% | -12% | -82% | -81% |
| 0.05–0.1% | 2695 | 10 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 3888 | 13 | 4% | 2% | -59% | -90% | -89% |
| 0.2–0.5% | 4514 | 21 | 6% | 3% | -49% | -88% | -88% |
| Over 0.5% | 1757 | 6 | 6% | 3% | -65% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5767 | 23 | 4% | 2% | -55% | -87% | -88% |
| Morning (6am–12pm) | 5489 | 28 | 4% | 2% | -41% | -87% | -86% |
| Afternoon (12–6pm) | 5549 | 19 | 3% | 1% | -59% | -88% | -89% |
| Evening (6pm–12am) | 6314 | 18 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,854 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/18 7:44:33 PM | EURUSD | DOWN | 26 sec | — | — | In play | — |
| 10/18 7:44:19 PM | PALLADIUM | DOWN | 40 sec | — | — | In play | — |
| 10/18 7:44:19 PM | GBPUSD | DOWN | 40 sec | — | — | In play | — |
| 10/18 7:44:19 PM | SILVER | DOWN | 40 sec | — | — | In play | — |
| 10/18 7:44:18 PM | SOL | DOWN | 42 sec | +0.155% | — | In play | — |
| 10/18 7:44:18 PM | GOLD | DOWN | 42 sec | — | — | In play | — |
| 10/18 7:43:58 PM | BNB | DOWN | 62 sec | +0.041% | — | In play | — |
| 10/18 7:43:52 PM | BTC | DOWN | 68 sec | +0.065% | — | In play | — |
| 10/18 7:43:12 PM | DOGE | DOWN | 1.8 min | +0.182% | — | In play | — |
| 10/18 7:43:00 PM | XRP | DOWN | 2.0 min | +0.160% | — | In play | — |
| 10/18 7:42:44 PM | ETH | DOWN | 2.3 min | +0.206% | — | In play | — |
| 10/18 7:41:56 PM | WTI | UP | 3.0 min | — | — | In play | — |
| 10/18 7:41:44 PM | ZEC | DOWN | 3.2 min | +0.607% | — | In play | — |
| 10/18 7:40:35 PM | NEAR | DOWN | 4.4 min | +0.780% | — | In play | — |
| 10/18 7:29:56 PM | NATGAS | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 7:29:52 PM | BTC | DOWN | 7 sec | -0.011% | 0¢ | ❌ Lost | $0.00 |
| 10/18 7:29:48 PM | SILVER | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 7:29:44 PM | DOGE | DOWN | 15 sec | +0.011% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 7:29:44 PM | ETH | DOWN | 15 sec | +0.049% | 0¢ | ❌ Lost | $0.00 |
| 10/18 7:29:31 PM | XRP | DOWN | 28 sec | +0.015% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 7:29:13 PM | SOL | DOWN | 46 sec | +0.117% | 0¢ | ❌ Lost | $0.00 |
| 10/18 7:29:13 PM | WTI | UP | 46 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/18 7:28:55 PM | ZEC | DOWN | 64 sec | +0.230% | 0¢ | ❌ Lost | $0.00 |
| 10/18 7:28:55 PM | BNB | DOWN | 64 sec | +0.017% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 7:28:38 PM | HYPE | UP | 81 sec | -0.180% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 7:28:30 PM | GOLD | UP | 89 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/18 7:26:31 PM | USDJPY | DOWN | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 7:14:57 PM | SILVER | DOWN | 2 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/18 7:14:57 PM | AUDUSD | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 7:14:41 PM | GOLD | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
