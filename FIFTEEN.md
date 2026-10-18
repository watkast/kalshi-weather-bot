# 15-Minute 1¢ Study

*Updated Sun Oct 18, 7:45 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1892 finished bets | 1% | $83.25 | +40% | +4.40¢ | $36.95 / $46.30 |

*Expect about **93 buys a day** (~$13.98/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1742 | $61.50 | +32% |
| Momentum model ≥ 2%, hold to the close | 2913 | -$3.75 | -1% |
| Volatility model ≥ 5%, sell at 50¢ | 1892 | -$33.75 | -16% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 22690 | 22678 | 86 (0%) | 1.07% | -$1,549.40 (-56%) | Hold to the close: -$1,549.40 (-56%) |

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
| Volatility model | 14954 | 4.6% | 0.4% (60) | -667% | ❌ Worse |
| Momentum model | 14954 | 4.5% | 0.4% (60) | -690% | ❌ Worse |
| Mean-reversion model | 14954 | 7.7% | 0.4% (60) | -800% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 14954 | 60 | -50% | -88% | -88% | -85% |
| Volatility model ≥ 2% | 3430 | 27 | -9% | -79% | -79% | -75% |
| Volatility model ≥ 5% | 1892 | 21 | +40% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 1119 | 13 | +64% | -69% | -68% | -66% |
| Momentum model ≥ 2% | 2913 | 24 | -1% | -81% | -82% | -78% |
| Momentum model ≥ 5% | 1742 | 18 | +32% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 1159 | 12 | +44% | -75% | -75% | -70% |
| Mean-reversion model ≥ 2% | 5754 | 38 | -28% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3994 | 30 | -17% | -82% | -82% | -79% |
| Mean-reversion model ≥ 10% | 2650 | 19 | -18% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 15152 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5309 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 22678 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 86 | 0% | -$1,549.40 | -56% | — |
| Sell at 2¢ | 828 | 4% | -$2,440.12 | -89% | 44 sec |
| Sell at 3¢ | 559 | 2% | -$2,437.39 | -89% | 47 sec |
| Sell at 5¢ | 404 | 2% | -$2,392.80 | -87% | 50 sec |
| Sell at 10¢ | 243 | 1% | -$2,309.07 | -84% | 63 sec |
| Sell at 25¢ | 136 | 1% | -$2,135.24 | -78% | 78 sec |
| Sell at 50¢ | 90 | 0% | -$1,907.90 | -69% | 1.5 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 813 | 5 | 11% | 4% | -42% | -81% | -84% |
| 2–5 min | 7378 | 38 | 7% | 3% | -49% | -87% | -87% |
| 1–2 min | 5844 | 23 | 3% | 2% | -57% | -92% | -92% |
| Under 1 min | 8639 | 20 | 1% | 0% | -66% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1701 | 11 | 4% | 2% | -20% | -90% | -90% |
| HYPE | 1692 | 6 | 5% | 2% | -56% | -90% | -88% |
| BNB | 1690 | 7 | 5% | 2% | -49% | -89% | -88% |
| DOGE | 1687 | 3 | 4% | 2% | -78% | -91% | -90% |
| ETH | 1686 | 9 | 6% | 3% | -36% | -87% | -86% |
| SOL | 1680 | 2 | 3% | 2% | -85% | -92% | -92% |
| XRP | 1675 | 7 | 3% | 1% | -48% | -87% | -87% |
| NEAR | 1672 | 9 | 6% | 3% | -30% | -78% | -78% |
| BTC | 1669 | 8 | 5% | 2% | -35% | -88% | -90% |
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
| UP (bought YES) | 11424 | 42 | 4% | 2% | -58% | -89% | -88% |
| DOWN (bought NO) | 11254 | 44 | 4% | 2% | -55% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2612 | 14 | 2% | 1% | -11% | -82% | -81% |
| 0.05–0.1% | 2643 | 8 | 3% | 2% | -56% | -92% | -91% |
| 0.1–0.2% | 3804 | 13 | 5% | 2% | -58% | -90% | -89% |
| 0.2–0.5% | 4375 | 21 | 6% | 3% | -47% | -88% | -88% |
| Over 0.5% | 1715 | 6 | 7% | 3% | -64% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5767 | 23 | 4% | 2% | -55% | -87% | -88% |
| Morning (6am–12pm) | 5369 | 27 | 4% | 2% | -42% | -87% | -86% |
| Afternoon (12–6pm) | 5311 | 19 | 3% | 1% | -57% | -88% | -89% |
| Evening (6pm–12am) | 6231 | 17 | 3% | 2% | -69% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,770 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/18 7:44:40 AM | ZEC | DOWN | 20 sec | +0.097% | 0¢ | In play | — |
| 10/18 7:44:24 AM | SOL | UP | 36 sec | -0.080% | 0¢ | ❌ Lost | $0.00 |
| 10/18 7:44:09 AM | XRP | UP | 50 sec | -0.117% | 0¢ | In play | — |
| 10/18 7:43:53 AM | BTC | UP | 66 sec | -0.061% | 1¢ | In play | — |
| 10/18 7:43:53 AM | ETH | UP | 66 sec | -0.126% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 7:43:21 AM | HYPE | UP | 1.6 min | -0.304% | 1¢ | In play | — |
| 10/18 7:41:26 AM | BNB | UP | 3.5 min | -0.202% | 1¢ | In play | — |
| 10/18 7:41:26 AM | DOGE | UP | 3.5 min | -0.594% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 7:41:10 AM | NEAR | UP | 3.8 min | -1.060% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 7:28:11 AM | NEAR | UP | 1.8 min | -0.636% | 0¢ | ❌ Lost | $0.00 |
| 10/18 7:27:22 AM | ZEC | UP | 2.6 min | -0.539% | 2¢ | ❌ Lost | -$0.15 |
| 10/18 7:26:49 AM | HYPE | UP | 3.2 min | -0.346% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 7:26:33 AM | BNB | UP | 3.4 min | -0.224% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 7:26:33 AM | DOGE | UP | 3.4 min | -0.430% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 7:26:01 AM | BTC | UP | 4.0 min | -0.237% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 7:26:01 AM | XRP | UP | 4.0 min | -0.340% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 7:26:01 AM | ETH | UP | 4.0 min | -0.246% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 7:25:12 AM | SOL | UP | 4.8 min | -0.493% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 7:14:17 AM | XRP | UP | 42 sec | -0.077% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 7:13:26 AM | BTC | UP | 1.6 min | -0.061% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 7:13:26 AM | DOGE | UP | 1.6 min | -0.129% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 7:13:26 AM | HYPE | UP | 1.6 min | -0.195% | 0¢ | ❌ Lost | $0.00 |
| 10/18 7:13:11 AM | BNB | UP | 1.8 min | -0.101% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 7:12:38 AM | SOL | UP | 2.4 min | -0.200% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 7:10:43 AM | ETH | UP | 4.3 min | -0.182% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 7:10:43 AM | ZEC | UP | 4.3 min | -0.531% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 7:09:36 AM | NEAR | UP | 5.4 min | -0.775% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 6:59:44 AM | XRP | DOWN | 16 sec | +0.008% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 6:59:13 AM | BTC | DOWN | 46 sec | +0.031% | 0¢ | ❌ Lost | $0.00 |
| 10/18 6:58:56 AM | BNB | DOWN | 63 sec | +0.030% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
