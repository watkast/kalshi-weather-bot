# 15-Minute 1¢ Study

*Updated Mon Oct 19, 12:21 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2039 finished bets | 1% | $93.10 | +41% | +4.57¢ | $29.00 / $64.10 |

*Expect about **95 buys a day** (~$14.24/day at risk); max loss per buy **15¢**.*

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
| 24043 | 24036 | 90 (0%) | 1.07% | -$1,657.65 (-57%) | Hold to the close: -$1,657.65 (-57%) |

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
| Volatility model | 15810 | 4.6% | 0.4% (64) | -663% | ❌ Worse |
| Momentum model | 15810 | 4.6% | 0.4% (64) | -687% | ❌ Worse |
| Mean-reversion model | 15810 | 7.7% | 0.4% (64) | -797% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 15810 | 64 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3683 | 30 | -6% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 2039 | 23 | +41% | -70% | -70% | -66% |
| Volatility model ≥ 10% | 1193 | 15 | +76% | -59% | -57% | -54% |
| Momentum model ≥ 2% | 3127 | 26 | -1% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 1879 | 20 | +35% | -73% | -73% | -68% |
| Momentum model ≥ 10% | 1248 | 13 | +43% | -65% | -65% | -60% |
| Mean-reversion model ≥ 2% | 6145 | 41 | -27% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 4274 | 33 | -15% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2829 | 22 | -11% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16008 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5616 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2412 | 1% | 1% | 1% | 0% | 0% | 0% |
| **All** | 24036 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 90 | 0% | -$1,657.65 | -57% | — |
| Sell at 2¢ | 863 | 4% | -$2,581.27 | -88% | 46 sec |
| Sell at 3¢ | 585 | 2% | -$2,577.50 | -88% | 47 sec |
| Sell at 5¢ | 419 | 2% | -$2,533.30 | -87% | 50 sec |
| Sell at 10¢ | 254 | 1% | -$2,444.91 | -84% | 64 sec |
| Sell at 25¢ | 141 | 1% | -$2,254.94 | -77% | 79 sec |
| Sell at 50¢ | 93 | 0% | -$2,023.90 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 891 | 5 | 10% | 3% | -47% | -82% | -85% |
| 2–5 min | 7821 | 40 | 7% | 3% | -50% | -88% | -88% |
| 1–2 min | 6161 | 24 | 3% | 2% | -58% | -92% | -92% |
| Under 1 min | 9159 | 21 | 1% | 0% | -67% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1799 | 11 | 4% | 2% | -24% | -90% | -90% |
| HYPE | 1789 | 6 | 5% | 2% | -59% | -90% | -88% |
| BNB | 1787 | 9 | 5% | 2% | -38% | -82% | -81% |
| DOGE | 1780 | 3 | 4% | 2% | -79% | -91% | -90% |
| ETH | 1778 | 9 | 6% | 3% | -39% | -87% | -87% |
| SOL | 1774 | 2 | 3% | 2% | -86% | -93% | -92% |
| XRP | 1770 | 7 | 3% | 1% | -51% | -87% | -87% |
| NEAR | 1766 | 9 | 6% | 3% | -34% | -79% | -79% |
| BTC | 1765 | 10 | 5% | 2% | -24% | -88% | -90% |
| GOLD | 920 | 1 | 3% | 1% | -87% | -93% | -94% |
| SILVER | 891 | 4 | 3% | 1% | -48% | -81% | -81% |
| WTI | 863 | 3 | 3% | 1% | -59% | -94% | -95% |
| COPPER | 777 | 2 | 2% | 1% | -76% | -85% | -85% |
| PLATINUM | 764 | 0 | 1% | 0% | -100% | -99% | -99% |
| EURUSD | 706 | 3 | 2% | 1% | -60% | -83% | -82% |
| NATGAS | 705 | 5 | 2% | 2% | -34% | -83% | -82% |
| PALLADIUM | 696 | 2 | 1% | 0% | -73% | -85% | -85% |
| GBPUSD | 657 | 1 | 2% | 1% | -86% | -97% | -97% |
| USDJPY | 613 | 3 | 1% | 0% | -54% | -99% | -98% |
| AUDUSD | 241 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 195 | 0 | 1% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12095 | 43 | 4% | 2% | -59% | -89% | -88% |
| DOWN (bought NO) | 11941 | 47 | 3% | 1% | -55% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2725 | 15 | 2% | 1% | -8% | -76% | -76% |
| 0.05–0.1% | 2777 | 10 | 3% | 2% | -48% | -91% | -91% |
| 0.1–0.2% | 4032 | 13 | 5% | 2% | -60% | -90% | -89% |
| 0.2–0.5% | 4661 | 22 | 6% | 3% | -48% | -88% | -88% |
| Over 0.5% | 1810 | 6 | 6% | 3% | -66% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6064 | 24 | 4% | 2% | -55% | -86% | -86% |
| Morning (6am–12pm) | 5814 | 29 | 4% | 2% | -43% | -87% | -86% |
| Afternoon (12–6pm) | 5565 | 19 | 3% | 1% | -59% | -88% | -89% |
| Evening (6pm–12am) | 6593 | 18 | 3% | 2% | -69% | -92% | -92% |

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
| 10/19 12:14:29 PM | DOGE | DOWN | 31 sec | -0.013% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:14:29 PM | HYPE | DOWN | 31 sec | +0.011% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 12:14:29 PM | PALLADIUM | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:14:14 PM | AUDUSD | DOWN | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:14:14 PM | ZEC | DOWN | 45 sec | +0.162% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:13:58 PM | WTI | UP | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:13:58 PM | GOLD | DOWN | 61 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 12:13:42 PM | SOL | DOWN | 77 sec | +0.142% | 0¢ | ❌ Lost | $0.00 |
| 10/19 12:13:26 PM | SILVER | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 12:13:26 PM | COPPER | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:12:20 PM | NATGAS | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 12:10:44 PM | XRP | DOWN | 4.2 min | +0.262% | 10¢ | ❌ Lost | -$0.15 |
| 10/19 12:09:56 PM | BNB | DOWN | 5.1 min | +0.150% | 4¢ | ❌ Lost | -$0.15 |
| 10/19 12:09:56 PM | BTC | DOWN | 5.1 min | +0.267% | 2¢ | ❌ Lost | -$0.15 |
| 10/19 12:07:46 PM | ETH | DOWN | 7.2 min | +0.358% | 2¢ | ❌ Lost | -$0.15 |
| 10/19 12:07:27 PM | NEAR | DOWN | 7.5 min | +1.191% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 11:59:21 AM | USDCAD | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 11:59:21 AM | SOL | UP | 39 sec | -0.139% | 0¢ | ❌ Lost | $0.00 |
| 10/19 11:59:05 AM | NATGAS | DOWN | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 11:58:32 AM | WTI | DOWN | 87 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 11:58:16 AM | HYPE | UP | 1.7 min | -0.191% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 11:56:40 AM | NEAR | UP | 3.3 min | -0.658% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 11:56:40 AM | BTC | UP | 3.3 min | -0.160% | 2¢ | ❌ Lost | -$0.15 |
| 10/19 11:56:24 AM | XRP | UP | 3.6 min | -0.323% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 11:56:08 AM | ZEC | UP | 3.9 min | -0.590% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 11:56:08 AM | DOGE | UP | 3.9 min | -0.344% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 11:55:52 AM | ETH | UP | 4.1 min | -0.274% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 11:55:19 AM | BNB | UP | 4.7 min | -0.169% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 11:44:49 AM | HYPE | UP | 11 sec | -0.002% | 0¢ | ❌ Lost | $0.00 |
| 10/19 11:44:49 AM | NEAR | UP | 11 sec | -0.254% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
