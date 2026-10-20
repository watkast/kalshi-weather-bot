# 15-Minute 1¢ Study

*Updated Mon Oct 19, 7:21 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2062 finished bets | 1% | $90.85 | +39% | +4.41¢ | $27.20 / $63.65 |

*Expect about **95 buys a day** (~$14.20/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1895 | $72.10 | +35% |
| Momentum model ≥ 2%, hold to the close | 3163 | -$6.35 | -2% |
| Volatility model ≥ 5%, sell at 50¢ | 2062 | -$26.15 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 24364 | 24357 | 90 (0%) | 1.07% | -$1,697.25 (-57%) | Hold to the close: -$1,697.25 (-57%) |

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
| Volatility model | 16009 | 4.6% | 0.4% (64) | -672% | ❌ Worse |
| Momentum model | 16009 | 4.6% | 0.4% (64) | -695% | ❌ Worse |
| Mean-reversion model | 16009 | 7.7% | 0.4% (64) | -808% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16009 | 64 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3721 | 30 | -7% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 2062 | 23 | +39% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 1207 | 15 | +74% | -59% | -58% | -55% |
| Momentum model ≥ 2% | 3163 | 26 | -2% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 1895 | 20 | +35% | -73% | -73% | -68% |
| Momentum model ≥ 10% | 1260 | 13 | +42% | -66% | -65% | -60% |
| Mean-reversion model ≥ 2% | 6235 | 41 | -28% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 4331 | 33 | -16% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2866 | 22 | -13% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16207 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5694 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2456 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 24357 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 90 | 0% | -$1,697.25 | -57% | — |
| Sell at 2¢ | 880 | 4% | -$2,616.45 | -88% | 46 sec |
| Sell at 3¢ | 597 | 2% | -$2,612.42 | -88% | 47 sec |
| Sell at 5¢ | 427 | 2% | -$2,567.70 | -87% | 50 sec |
| Sell at 10¢ | 260 | 1% | -$2,476.65 | -84% | 64 sec |
| Sell at 25¢ | 143 | 1% | -$2,287.92 | -77% | 79 sec |
| Sell at 50¢ | 93 | 0% | -$2,063.50 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 928 | 5 | 10% | 4% | -49% | -82% | -84% |
| 2–5 min | 7909 | 40 | 7% | 3% | -50% | -88% | -87% |
| 1–2 min | 6227 | 24 | 3% | 2% | -58% | -92% | -92% |
| Under 1 min | 9289 | 21 | 1% | 0% | -67% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1822 | 11 | 4% | 2% | -25% | -90% | -90% |
| HYPE | 1811 | 6 | 5% | 2% | -59% | -89% | -88% |
| BNB | 1810 | 9 | 5% | 2% | -39% | -82% | -81% |
| DOGE | 1802 | 3 | 4% | 2% | -79% | -91% | -90% |
| ETH | 1800 | 9 | 6% | 3% | -40% | -87% | -86% |
| SOL | 1797 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1790 | 7 | 3% | 1% | -52% | -87% | -87% |
| NEAR | 1788 | 9 | 6% | 3% | -35% | -79% | -79% |
| BTC | 1787 | 10 | 5% | 2% | -25% | -88% | -90% |
| GOLD | 932 | 1 | 3% | 1% | -87% | -92% | -94% |
| SILVER | 905 | 4 | 3% | 1% | -49% | -81% | -80% |
| WTI | 875 | 3 | 3% | 1% | -60% | -94% | -96% |
| COPPER | 785 | 2 | 2% | 1% | -76% | -85% | -85% |
| PLATINUM | 773 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 718 | 5 | 2% | 2% | -35% | -83% | -82% |
| EURUSD | 715 | 3 | 2% | 1% | -61% | -83% | -83% |
| PALLADIUM | 706 | 2 | 1% | 0% | -74% | -85% | -85% |
| GBPUSD | 669 | 1 | 2% | 1% | -86% | -97% | -97% |
| USDJPY | 621 | 3 | 1% | 1% | -55% | -99% | -98% |
| AUDUSD | 252 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 199 | 0 | 1% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12287 | 43 | 4% | 2% | -60% | -89% | -88% |
| DOWN (bought NO) | 12070 | 47 | 3% | 1% | -55% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2756 | 15 | 2% | 1% | -9% | -76% | -76% |
| 0.05–0.1% | 2817 | 10 | 3% | 2% | -48% | -91% | -91% |
| 0.1–0.2% | 4072 | 13 | 5% | 2% | -61% | -89% | -89% |
| 0.2–0.5% | 4721 | 22 | 6% | 3% | -49% | -88% | -88% |
| Over 0.5% | 1838 | 6 | 6% | 3% | -66% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6064 | 24 | 4% | 2% | -55% | -86% | -86% |
| Morning (6am–12pm) | 5814 | 29 | 4% | 2% | -43% | -87% | -86% |
| Afternoon (12–6pm) | 5807 | 19 | 3% | 1% | -61% | -89% | -89% |
| Evening (6pm–12am) | 6672 | 18 | 3% | 2% | -69% | -92% | -91% |

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
| 10/19 7:14:52 PM | PALLADIUM | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:14:36 PM | EURUSD | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:14:36 PM | USDCAD | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:13:46 PM | USDJPY | UP | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:13:30 PM | NEAR | UP | 1.5 min | -0.626% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:13:30 PM | AUDUSD | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 7:13:14 PM | WTI | DOWN | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 7:12:59 PM | GOLD | UP | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 7:11:39 PM | SILVER | UP | 3.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 7:10:03 PM | ZEC | UP | 4.9 min | -0.954% | 3¢ | ❌ Lost | -$0.15 |
| 10/19 7:10:03 PM | BTC | UP | 4.9 min | -0.520% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 7:09:47 PM | SOL | UP | 5.2 min | -0.709% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 7:09:29 PM | DOGE | UP | 5.5 min | -0.464% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 7:09:29 PM | BNB | UP | 5.5 min | -0.321% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 7:09:29 PM | HYPE | UP | 5.5 min | -0.544% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 7:09:29 PM | XRP | UP | 5.5 min | -0.493% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 7:08:42 PM | ETH | UP | 6.3 min | -0.444% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 6:59:51 PM | SILVER | UP | 8 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 6:59:51 PM | PALLADIUM | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 6:59:35 PM | WTI | DOWN | 24 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 6:59:35 PM | EURUSD | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 6:59:35 PM | ZEC | UP | 24 sec | -0.077% | 0¢ | ❌ Lost | $0.00 |
| 10/19 6:59:35 PM | AUDUSD | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 6:59:35 PM | XRP | UP | 24 sec | -0.062% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 6:59:35 PM | SOL | UP | 24 sec | -0.086% | 0¢ | ❌ Lost | $0.00 |
| 10/19 6:59:35 PM | BTC | DOWN | 24 sec | +0.020% | 0¢ | ❌ Lost | $0.00 |
| 10/19 6:59:19 PM | GOLD | UP | 40 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 6:59:19 PM | PLATINUM | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 6:59:03 PM | ETH | DOWN | 57 sec | +0.068% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 6:59:03 PM | GBPUSD | UP | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
