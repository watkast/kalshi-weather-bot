# 15-Minute 1¢ Study

*Updated Sun Oct 18, 4:52 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1955 finished bets | 1% | $75.00 | +34% | +3.84¢ | $33.20 / $41.80 |

*Expect about **95 buys a day** (~$14.18/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1796 | $54.90 | +28% |
| Momentum model ≥ 2%, hold to the close | 2996 | -$14.55 | -4% |
| Volatility model ≥ 2%, hold to the close | 3528 | -$37.30 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 22983 | 22976 | 87 (0%) | 1.07% | -$1,572.30 (-56%) | Hold to the close: -$1,572.30 (-56%) |

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
| Volatility model | 15232 | 4.6% | 0.4% (61) | -674% | ❌ Worse |
| Momentum model | 15232 | 4.6% | 0.4% (61) | -697% | ❌ Worse |
| Mean-reversion model | 15232 | 7.7% | 0.4% (61) | -808% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 15232 | 61 | -50% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 3528 | 28 | -9% | -80% | -79% | -75% |
| Volatility model ≥ 5% | 1955 | 21 | +34% | -76% | -75% | -72% |
| Volatility model ≥ 10% | 1148 | 13 | +59% | -70% | -68% | -66% |
| Momentum model ≥ 2% | 2996 | 24 | -4% | -82% | -82% | -78% |
| Momentum model ≥ 5% | 1796 | 18 | +28% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 1195 | 12 | +39% | -75% | -75% | -70% |
| Mean-reversion model ≥ 2% | 5904 | 39 | -28% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 4102 | 31 | -17% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 2716 | 20 | -16% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 15430 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5318 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2228 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 22976 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 87 | 0% | -$1,572.30 | -56% | — |
| Sell at 2¢ | 835 | 4% | -$2,475.20 | -89% | 44 sec |
| Sell at 3¢ | 565 | 2% | -$2,471.95 | -89% | 47 sec |
| Sell at 5¢ | 407 | 2% | -$2,427.75 | -87% | 50 sec |
| Sell at 10¢ | 246 | 1% | -$2,342.04 | -84% | 63 sec |
| Sell at 25¢ | 137 | 1% | -$2,168.83 | -78% | 77 sec |
| Sell at 50¢ | 91 | 0% | -$1,938.05 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 840 | 5 | 10% | 3% | -43% | -82% | -85% |
| 2–5 min | 7514 | 39 | 7% | 3% | -49% | -88% | -87% |
| 1–2 min | 5898 | 23 | 3% | 2% | -57% | -92% | -92% |
| Under 1 min | 8720 | 20 | 1% | 0% | -67% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1733 | 11 | 4% | 2% | -21% | -90% | -90% |
| HYPE | 1724 | 6 | 5% | 2% | -57% | -90% | -88% |
| BNB | 1722 | 7 | 5% | 2% | -50% | -89% | -89% |
| DOGE | 1718 | 3 | 4% | 2% | -78% | -90% | -90% |
| ETH | 1713 | 9 | 6% | 3% | -37% | -87% | -87% |
| SOL | 1711 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1705 | 7 | 3% | 1% | -50% | -87% | -88% |
| NEAR | 1702 | 9 | 6% | 3% | -32% | -78% | -79% |
| BTC | 1702 | 9 | 5% | 2% | -29% | -88% | -90% |
| GOLD | 865 | 1 | 3% | 1% | -86% | -92% | -94% |
| SILVER | 842 | 4 | 3% | 1% | -45% | -80% | -80% |
| WTI | 824 | 3 | 3% | 1% | -58% | -94% | -95% |
| COPPER | 735 | 2 | 2% | 1% | -75% | -84% | -84% |
| PLATINUM | 723 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 669 | 5 | 2% | 2% | -30% | -82% | -81% |
| EURUSD | 663 | 3 | 3% | 1% | -58% | -81% | -81% |
| PALLADIUM | 660 | 2 | 1% | 0% | -72% | -84% | -84% |
| GBPUSD | 617 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 576 | 3 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 203 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 169 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 11554 | 42 | 4% | 2% | -58% | -89% | -88% |
| DOWN (bought NO) | 11422 | 45 | 4% | 2% | -54% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2639 | 14 | 2% | 1% | -12% | -82% | -81% |
| 0.05–0.1% | 2681 | 9 | 3% | 2% | -51% | -91% | -91% |
| 0.1–0.2% | 3867 | 13 | 4% | 2% | -59% | -90% | -89% |
| 0.2–0.5% | 4486 | 21 | 6% | 3% | -49% | -88% | -88% |
| Over 0.5% | 1754 | 6 | 6% | 3% | -65% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5767 | 23 | 4% | 2% | -55% | -87% | -88% |
| Morning (6am–12pm) | 5489 | 28 | 4% | 2% | -41% | -87% | -86% |
| Afternoon (12–6pm) | 5489 | 19 | 3% | 1% | -59% | -88% | -89% |
| Evening (6pm–12am) | 6231 | 17 | 3% | 2% | -69% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,856 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/18 4:44:59 PM | NATGAS | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 4:44:43 PM | USDJPY | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 4:44:11 PM | PLATINUM | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 4:44:11 PM | PALLADIUM | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 4:43:55 PM | HYPE | DOWN | 65 sec | +0.060% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 4:43:55 PM | GBPUSD | UP | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 4:43:39 PM | XRP | DOWN | 81 sec | +0.154% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 4:43:13 PM | AUDUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 4:42:58 PM | SOL | DOWN | 2.0 min | +0.346% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 4:42:58 PM | EURUSD | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 4:42:24 PM | WTI | UP | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/18 4:42:24 PM | ZEC | DOWN | 2.6 min | +0.591% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 4:42:09 PM | ETH | DOWN | 2.9 min | +0.261% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 4:41:52 PM | BTC | DOWN | 3.1 min | +0.201% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 4:41:35 PM | DOGE | DOWN | 3.4 min | +0.385% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 4:41:35 PM | BNB | DOWN | 3.4 min | +0.212% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 4:41:19 PM | NEAR | DOWN | 3.7 min | +0.911% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 4:29:53 PM | BNB | DOWN | 7 sec | +0.004% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 4:29:37 PM | AUDUSD | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 4:29:37 PM | SOL | DOWN | 23 sec | +0.058% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 4:29:21 PM | DOGE | UP | 39 sec | -0.055% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 4:29:21 PM | NEAR | DOWN | 39 sec | -0.004% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 4:29:21 PM | ETH | UP | 39 sec | -0.111% | 0¢ | ❌ Lost | $0.00 |
| 10/18 4:29:05 PM | BTC | UP | 55 sec | -0.094% | 0¢ | ❌ Lost | $0.00 |
| 10/18 4:29:05 PM | ZEC | DOWN | 55 sec | +0.272% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 4:28:50 PM | HYPE | DOWN | 69 sec | +0.165% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 4:28:50 PM | WTI | DOWN | 69 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/18 4:28:18 PM | GOLD | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/18 4:28:18 PM | SILVER | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/18 4:25:22 PM | XRP | DOWN | 4.6 min | +0.682% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
