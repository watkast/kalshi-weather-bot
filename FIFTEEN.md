# 15-Minute 1¢ Study

*Updated Sun Oct 18, 10:28 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1920 finished bets | 1% | $79.35 | +37% | +4.13¢ | $35.30 / $44.05 |

*Expect about **94 buys a day** (~$14.12/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1771 | $57.75 | +30% |
| Momentum model ≥ 2%, hold to the close | 2953 | -$9.15 | -3% |
| Volatility model ≥ 5%, sell at 50¢ | 1920 | -$37.65 | -18% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 22784 | 22772 | 86 (0%) | 1.07% | -$1,561.40 (-56%) | Hold to the close: -$1,561.40 (-56%) |

*In play or awaiting result: 11. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 15048 | 4.6% | 0.4% (60) | -669% | ❌ Worse |
| Momentum model | 15048 | 4.5% | 0.4% (60) | -691% | ❌ Worse |
| Mean-reversion model | 15048 | 7.7% | 0.4% (60) | -803% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 15048 | 60 | -50% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 3472 | 27 | -10% | -80% | -79% | -75% |
| Volatility model ≥ 5% | 1920 | 21 | +37% | -76% | -75% | -72% |
| Volatility model ≥ 10% | 1130 | 13 | +62% | -70% | -69% | -66% |
| Momentum model ≥ 2% | 2953 | 24 | -3% | -81% | -82% | -78% |
| Momentum model ≥ 5% | 1771 | 18 | +30% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 1176 | 12 | +41% | -75% | -75% | -70% |
| Mean-reversion model ≥ 2% | 5812 | 38 | -29% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 4033 | 30 | -18% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 2677 | 19 | -19% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 15246 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5309 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 22772 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 86 | 0% | -$1,561.40 | -56% | — |
| Sell at 2¢ | 830 | 4% | -$2,451.60 | -89% | 44 sec |
| Sell at 3¢ | 560 | 2% | -$2,449.00 | -89% | 47 sec |
| Sell at 5¢ | 404 | 2% | -$2,404.80 | -87% | 50 sec |
| Sell at 10¢ | 243 | 1% | -$2,321.07 | -84% | 63 sec |
| Sell at 25¢ | 136 | 1% | -$2,147.24 | -78% | 78 sec |
| Sell at 50¢ | 90 | 0% | -$1,919.90 | -69% | 1.5 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 821 | 5 | 11% | 4% | -42% | -81% | -84% |
| 2–5 min | 7425 | 38 | 7% | 3% | -50% | -88% | -87% |
| 1–2 min | 5867 | 23 | 3% | 2% | -57% | -92% | -92% |
| Under 1 min | 8655 | 20 | 1% | 0% | -66% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1712 | 11 | 4% | 2% | -20% | -90% | -90% |
| HYPE | 1703 | 6 | 5% | 2% | -57% | -90% | -88% |
| BNB | 1701 | 7 | 5% | 2% | -50% | -89% | -88% |
| DOGE | 1697 | 3 | 4% | 2% | -78% | -91% | -90% |
| ETH | 1696 | 9 | 6% | 3% | -36% | -87% | -86% |
| SOL | 1690 | 2 | 3% | 2% | -85% | -92% | -92% |
| XRP | 1686 | 7 | 3% | 1% | -49% | -87% | -87% |
| NEAR | 1681 | 9 | 6% | 3% | -31% | -78% | -79% |
| BTC | 1680 | 8 | 5% | 2% | -36% | -88% | -90% |
| GOLD | 864 | 1 | 3% | 1% | -86% | -92% | -94% |
| SILVER | 841 | 4 | 3% | 1% | -45% | -80% | -80% |
| WTI | 821 | 3 | 3% | 1% | -57% | -94% | -95% |
| COPPER | 735 | 2 | 2% | 1% | -75% | -84% | -84% |
| PLATINUM | 722 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 667 | 5 | 2% | 2% | -30% | -82% | -81% |
| PALLADIUM | 659 | 2 | 1% | 0% | -72% | -84% | -84% |
| EURUSD | 659 | 3 | 3% | 1% | -58% | -81% | -81% |
| GBPUSD | 615 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 574 | 3 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 200 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 169 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 11472 | 42 | 4% | 2% | -58% | -89% | -88% |
| DOWN (bought NO) | 11300 | 44 | 4% | 2% | -55% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2618 | 14 | 2% | 1% | -11% | -82% | -81% |
| 0.05–0.1% | 2652 | 8 | 3% | 2% | -56% | -92% | -91% |
| 0.1–0.2% | 3825 | 13 | 5% | 2% | -58% | -90% | -89% |
| 0.2–0.5% | 4419 | 21 | 6% | 3% | -48% | -88% | -88% |
| Over 0.5% | 1729 | 6 | 7% | 3% | -64% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5767 | 23 | 4% | 2% | -55% | -87% | -88% |
| Morning (6am–12pm) | 5463 | 27 | 4% | 2% | -43% | -87% | -86% |
| Afternoon (12–6pm) | 5311 | 19 | 3% | 1% | -57% | -88% | -89% |
| Evening (6pm–12am) | 6231 | 17 | 3% | 2% | -69% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,803 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/18 10:28:09 AM | XRP | DOWN | 1.8 min | +0.126% | — | In play | — |
| 10/18 10:28:09 AM | ETH | UP | 1.8 min | -0.203% | — | In play | — |
| 10/18 10:27:52 AM | BTC | DOWN | 2.1 min | +0.093% | — | In play | — |
| 10/18 10:27:36 AM | ZEC | DOWN | 2.4 min | +0.392% | — | In play | — |
| 10/18 10:27:20 AM | NEAR | DOWN | 2.6 min | +0.492% | — | In play | — |
| 10/18 10:14:31 AM | NEAR | UP | 28 sec | -0.215% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 10:14:14 AM | BTC | UP | 45 sec | -0.034% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 10:14:14 AM | DOGE | DOWN | 45 sec | +0.065% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 10:13:58 AM | SOL | UP | 62 sec | -0.123% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 10:12:07 AM | ZEC | UP | 2.9 min | -0.579% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 10:11:51 AM | XRP | UP | 3.1 min | -0.251% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 10:10:15 AM | BNB | UP | 4.8 min | -0.234% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 10:10:15 AM | HYPE | UP | 4.8 min | -0.394% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 10:09:59 AM | ETH | UP | 5.0 min | -0.344% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 9:58:06 AM | HYPE | DOWN | 1.9 min | +0.193% | 0¢ | ❌ Lost | $0.00 |
| 10/18 9:57:49 AM | NEAR | DOWN | 2.2 min | +0.314% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 9:57:49 AM | ZEC | DOWN | 2.2 min | +0.521% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 9:57:17 AM | BNB | DOWN | 2.7 min | +0.122% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 9:57:01 AM | DOGE | DOWN | 3.0 min | +0.180% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 9:56:46 AM | BTC | DOWN | 3.2 min | +0.103% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 9:55:58 AM | ETH | DOWN | 4.0 min | +0.190% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 9:55:42 AM | SOL | DOWN | 4.3 min | +0.257% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 9:54:54 AM | XRP | DOWN | 5.1 min | +0.284% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 9:43:57 AM | NEAR | DOWN | 62 sec | +0.132% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 9:43:25 AM | HYPE | UP | 1.6 min | -0.220% | 0¢ | ❌ Lost | $0.00 |
| 10/18 9:43:09 AM | XRP | UP | 1.9 min | -0.275% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 9:41:14 AM | ETH | UP | 3.8 min | -0.340% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 9:41:14 AM | SOL | UP | 3.8 min | -0.429% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 9:40:58 AM | BTC | UP | 4.0 min | -0.216% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 9:40:41 AM | BNB | UP | 4.3 min | -0.262% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
