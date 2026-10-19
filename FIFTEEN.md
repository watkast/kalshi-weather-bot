# 15-Minute 1¢ Study

*Updated Mon Oct 19, 2:04 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2039 finished bets | 1% | $93.10 | +41% | +4.57¢ | $29.00 / $64.10 |

*Expect about **95 buys a day** (~$14.19/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1879 | $73.30 | +35% |
| Momentum model ≥ 2%, hold to the close | 3127 | -$2.15 | -1% |
| Volatility model ≥ 5%, sell at 50¢ | 2039 | -$23.90 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 24079 | 24072 | 90 (0%) | 1.07% | -$1,662.30 (-57%) | Hold to the close: -$1,662.30 (-57%) |

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
| Volatility model | 15828 | 4.6% | 0.4% (64) | -663% | ❌ Worse |
| Momentum model | 15828 | 4.6% | 0.4% (64) | -687% | ❌ Worse |
| Mean-reversion model | 15828 | 7.7% | 0.4% (64) | -797% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 15828 | 64 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3686 | 30 | -7% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 2039 | 23 | +41% | -70% | -70% | -66% |
| Volatility model ≥ 10% | 1193 | 15 | +76% | -59% | -57% | -54% |
| Momentum model ≥ 2% | 3127 | 26 | -1% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 1879 | 20 | +35% | -73% | -73% | -68% |
| Momentum model ≥ 10% | 1248 | 13 | +43% | -65% | -65% | -60% |
| Mean-reversion model ≥ 2% | 6159 | 41 | -27% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 4282 | 33 | -15% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2833 | 22 | -11% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16026 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5629 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2417 | 1% | 1% | 1% | 0% | 0% | 0% |
| **All** | 24072 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 90 | 0% | -$1,662.30 | -57% | — |
| Sell at 2¢ | 863 | 4% | -$2,585.92 | -88% | 46 sec |
| Sell at 3¢ | 585 | 2% | -$2,582.15 | -88% | 47 sec |
| Sell at 5¢ | 419 | 2% | -$2,537.95 | -87% | 50 sec |
| Sell at 10¢ | 254 | 1% | -$2,449.56 | -84% | 64 sec |
| Sell at 25¢ | 141 | 1% | -$2,259.59 | -77% | 79 sec |
| Sell at 50¢ | 93 | 0% | -$2,028.55 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 902 | 5 | 10% | 3% | -47% | -82% | -85% |
| 2–5 min | 7836 | 40 | 7% | 3% | -50% | -88% | -88% |
| 1–2 min | 6165 | 24 | 3% | 2% | -58% | -92% | -92% |
| Under 1 min | 9165 | 21 | 1% | 0% | -67% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1801 | 11 | 4% | 2% | -24% | -90% | -90% |
| HYPE | 1791 | 6 | 5% | 2% | -59% | -90% | -88% |
| BNB | 1789 | 9 | 5% | 2% | -38% | -82% | -81% |
| DOGE | 1782 | 3 | 4% | 2% | -79% | -91% | -90% |
| ETH | 1780 | 9 | 6% | 3% | -39% | -87% | -87% |
| SOL | 1776 | 2 | 3% | 2% | -86% | -93% | -92% |
| XRP | 1772 | 7 | 3% | 1% | -51% | -87% | -87% |
| NEAR | 1768 | 9 | 6% | 3% | -34% | -79% | -79% |
| BTC | 1767 | 10 | 5% | 2% | -24% | -88% | -90% |
| GOLD | 921 | 1 | 3% | 1% | -87% | -93% | -94% |
| SILVER | 893 | 4 | 3% | 1% | -48% | -81% | -81% |
| WTI | 865 | 3 | 3% | 1% | -59% | -94% | -95% |
| COPPER | 779 | 2 | 2% | 1% | -76% | -85% | -85% |
| PLATINUM | 766 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 707 | 5 | 2% | 2% | -34% | -83% | -82% |
| EURUSD | 707 | 3 | 2% | 1% | -60% | -83% | -82% |
| PALLADIUM | 698 | 2 | 1% | 0% | -73% | -85% | -85% |
| GBPUSD | 658 | 1 | 2% | 1% | -86% | -97% | -97% |
| USDJPY | 613 | 3 | 1% | 0% | -54% | -99% | -98% |
| AUDUSD | 243 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 196 | 0 | 1% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12130 | 43 | 4% | 2% | -59% | -89% | -88% |
| DOWN (bought NO) | 11942 | 47 | 3% | 1% | -55% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2725 | 15 | 2% | 1% | -8% | -76% | -76% |
| 0.05–0.1% | 2777 | 10 | 3% | 2% | -48% | -91% | -91% |
| 0.1–0.2% | 4033 | 13 | 5% | 2% | -60% | -90% | -89% |
| 0.2–0.5% | 4671 | 22 | 6% | 3% | -48% | -88% | -88% |
| Over 0.5% | 1817 | 6 | 6% | 3% | -66% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6064 | 24 | 4% | 2% | -55% | -86% | -86% |
| Morning (6am–12pm) | 5814 | 29 | 4% | 2% | -43% | -87% | -86% |
| Afternoon (12–6pm) | 5601 | 19 | 3% | 1% | -60% | -88% | -89% |
| Evening (6pm–12am) | 6593 | 18 | 3% | 2% | -69% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,804 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/19 1:59:54 PM | WTI | UP | 5 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/19 1:59:37 PM | NATGAS | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 1:59:21 PM | USDCAD | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 1:59:21 PM | AUDUSD | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 1:58:34 PM | PALLADIUM | UP | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 1:57:30 PM | PLATINUM | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 1:57:14 PM | COPPER | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 1:56:58 PM | SILVER | UP | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 1:54:31 PM | ZEC | UP | 5.5 min | -1.187% | 0¢ | ❌ Lost | $0.00 |
| 10/19 1:54:31 PM | NEAR | UP | 5.5 min | -1.199% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 1:54:31 PM | ETH | UP | 5.5 min | -0.563% | 0¢ | ❌ Lost | $0.00 |
| 10/19 1:54:31 PM | HYPE | UP | 5.5 min | -0.616% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 1:54:31 PM | XRP | UP | 5.5 min | -0.476% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 1:54:31 PM | SOL | UP | 5.5 min | -0.604% | 0¢ | ❌ Lost | $0.00 |
| 10/19 1:54:31 PM | BNB | UP | 5.5 min | -0.219% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 1:54:31 PM | DOGE | UP | 5.5 min | -0.421% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 1:54:31 PM | BTC | UP | 5.5 min | -0.334% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 12:29:04 PM | SILVER | UP | 56 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/19 12:29:04 PM | NATGAS | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:28:32 PM | PLATINUM | UP | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:28:32 PM | PALLADIUM | UP | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:28:32 PM | GOLD | UP | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:27:59 PM | EURUSD | UP | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 12:27:25 PM | WTI | UP | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 12:26:55 PM | GBPUSD | UP | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:26:55 PM | COPPER | UP | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:26:39 PM | AUDUSD | UP | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:25:51 PM | DOGE | UP | 4.2 min | -0.335% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 12:25:51 PM | XRP | UP | 4.2 min | -0.338% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 12:25:18 PM | BNB | UP | 4.7 min | -0.173% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
