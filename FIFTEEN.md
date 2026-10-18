# 15-Minute 1¢ Study

*Updated Sun Oct 18, 5:52 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1967 finished bets | 1% | $73.80 | +34% | +3.75¢ | $32.60 / $41.20 |

*Expect about **95 buys a day** (~$14.24/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1805 | $54.00 | +27% |
| Momentum model ≥ 2%, hold to the close | 3010 | -$15.90 | -5% |
| Volatility model ≥ 2%, hold to the close | 3544 | -$38.95 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 23027 | 23020 | 87 (0%) | 1.07% | -$1,576.65 (-56%) | Hold to the close: -$1,576.65 (-56%) |

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
| Volatility model | 15260 | 4.6% | 0.4% (61) | -674% | ❌ Worse |
| Momentum model | 15260 | 4.6% | 0.4% (61) | -697% | ❌ Worse |
| Mean-reversion model | 15260 | 7.7% | 0.4% (61) | -808% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 15260 | 61 | -50% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 3544 | 28 | -9% | -80% | -79% | -75% |
| Volatility model ≥ 5% | 1967 | 21 | +34% | -76% | -75% | -72% |
| Volatility model ≥ 10% | 1155 | 13 | +58% | -70% | -69% | -66% |
| Momentum model ≥ 2% | 3010 | 24 | -5% | -82% | -82% | -78% |
| Momentum model ≥ 5% | 1805 | 18 | +27% | -80% | -79% | -75% |
| Momentum model ≥ 10% | 1202 | 12 | +38% | -76% | -75% | -70% |
| Mean-reversion model ≥ 2% | 5922 | 39 | -28% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 4117 | 31 | -17% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 2726 | 20 | -16% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 15458 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5329 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2233 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 23020 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 87 | 0% | -$1,576.65 | -56% | — |
| Sell at 2¢ | 837 | 4% | -$2,479.03 | -89% | 44 sec |
| Sell at 3¢ | 567 | 2% | -$2,475.52 | -89% | 47 sec |
| Sell at 5¢ | 407 | 2% | -$2,432.10 | -87% | 50 sec |
| Sell at 10¢ | 246 | 1% | -$2,346.39 | -84% | 63 sec |
| Sell at 25¢ | 137 | 1% | -$2,173.18 | -78% | 77 sec |
| Sell at 50¢ | 91 | 0% | -$1,942.40 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 842 | 5 | 10% | 3% | -44% | -82% | -84% |
| 2–5 min | 7521 | 39 | 7% | 3% | -49% | -88% | -87% |
| 1–2 min | 5909 | 23 | 3% | 2% | -58% | -92% | -92% |
| Under 1 min | 8744 | 20 | 1% | 0% | -67% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1736 | 11 | 4% | 2% | -21% | -90% | -90% |
| HYPE | 1727 | 6 | 5% | 2% | -57% | -90% | -88% |
| BNB | 1726 | 7 | 5% | 2% | -50% | -89% | -89% |
| DOGE | 1721 | 3 | 4% | 2% | -78% | -90% | -90% |
| ETH | 1717 | 9 | 6% | 3% | -37% | -87% | -87% |
| SOL | 1714 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1708 | 7 | 3% | 1% | -50% | -87% | -87% |
| NEAR | 1705 | 9 | 6% | 3% | -32% | -78% | -79% |
| BTC | 1704 | 9 | 5% | 2% | -29% | -88% | -90% |
| GOLD | 867 | 1 | 3% | 1% | -86% | -92% | -94% |
| SILVER | 845 | 4 | 3% | 1% | -45% | -80% | -80% |
| WTI | 826 | 3 | 3% | 1% | -58% | -94% | -95% |
| COPPER | 735 | 2 | 2% | 1% | -75% | -84% | -84% |
| PLATINUM | 725 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 670 | 5 | 2% | 2% | -30% | -82% | -81% |
| EURUSD | 665 | 3 | 3% | 1% | -58% | -82% | -81% |
| PALLADIUM | 661 | 2 | 1% | 0% | -72% | -84% | -84% |
| GBPUSD | 619 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 577 | 3 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 203 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 169 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 11582 | 42 | 4% | 2% | -58% | -89% | -88% |
| DOWN (bought NO) | 11438 | 45 | 3% | 2% | -55% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2648 | 14 | 2% | 1% | -12% | -82% | -81% |
| 0.05–0.1% | 2685 | 9 | 3% | 2% | -51% | -91% | -91% |
| 0.1–0.2% | 3873 | 13 | 4% | 2% | -59% | -90% | -89% |
| 0.2–0.5% | 4495 | 21 | 6% | 3% | -49% | -88% | -88% |
| Over 0.5% | 1754 | 6 | 6% | 3% | -65% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5767 | 23 | 4% | 2% | -55% | -87% | -88% |
| Morning (6am–12pm) | 5489 | 28 | 4% | 2% | -41% | -87% | -86% |
| Afternoon (12–6pm) | 5533 | 19 | 3% | 1% | -59% | -88% | -89% |
| Evening (6pm–12am) | 6231 | 17 | 3% | 2% | -69% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,862 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/18 5:44:46 PM | SOL | UP | 13 sec | -0.037% | 0¢ | ❌ Lost | $0.00 |
| 10/18 5:44:46 PM | ETH | UP | 13 sec | -0.045% | 0¢ | ❌ Lost | $0.00 |
| 10/18 5:44:46 PM | PLATINUM | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 5:44:30 PM | GBPUSD | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 5:44:30 PM | DOGE | UP | 29 sec | -0.015% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 5:44:30 PM | BNB | DOWN | 29 sec | +0.008% | 0¢ | ❌ Lost | $0.00 |
| 10/18 5:44:30 PM | BTC | UP | 29 sec | -0.033% | 0¢ | ❌ Lost | $0.00 |
| 10/18 5:44:30 PM | GOLD | UP | 29 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/18 5:44:14 PM | HYPE | DOWN | 45 sec | +0.017% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 5:43:58 PM | NEAR | DOWN | 61 sec | +0.260% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 5:43:42 PM | ZEC | UP | 77 sec | -0.297% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 5:43:26 PM | WTI | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/18 5:43:10 PM | EURUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 5:42:22 PM | XRP | UP | 2.6 min | -0.222% | 3¢ | ❌ Lost | -$0.15 |
| 10/18 5:39:15 PM | SILVER | UP | 5.8 min | — | 3¢ | ❌ Lost | -$0.15 |
| 10/18 5:25:15 PM | BNB | DOWN | 4.8 min | +0.170% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 5:24:27 PM | ETH | DOWN | 5.5 min | +0.417% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 5:14:46 PM | ZEC | UP | 14 sec | -0.161% | 0¢ | ❌ Lost | $0.00 |
| 10/18 5:14:46 PM | SOL | UP | 14 sec | -0.022% | 0¢ | ❌ Lost | $0.00 |
| 10/18 5:14:30 PM | HYPE | UP | 30 sec | -0.079% | 0¢ | ❌ Lost | $0.00 |
| 10/18 5:14:13 PM | NEAR | DOWN | 46 sec | +0.119% | 0¢ | ❌ Lost | $0.00 |
| 10/18 5:14:13 PM | SILVER | UP | 46 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/18 5:14:13 PM | PALLADIUM | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 5:13:23 PM | NATGAS | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 5:13:23 PM | BNB | UP | 1.6 min | -0.076% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 5:12:53 PM | ETH | UP | 2.1 min | -0.192% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 5:12:37 PM | DOGE | UP | 2.4 min | -0.174% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 5:11:24 PM | XRP | UP | 3.6 min | -0.269% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 4:59:55 PM | USDJPY | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 4:59:55 PM | WTI | UP | 4 sec | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
