# 15-Minute 1¢ Study

*Updated Mon Oct 19, 6:51 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2061 finished bets | 1% | $91.00 | +39% | +4.42¢ | $27.35 / $63.65 |

*Expect about **95 buys a day** (~$14.21/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1895 | $72.10 | +35% |
| Momentum model ≥ 2%, hold to the close | 3161 | -$6.05 | -2% |
| Volatility model ≥ 5%, sell at 50¢ | 2061 | -$26.00 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 24329 | 24322 | 90 (0%) | 1.07% | -$1,692.45 (-57%) | Hold to the close: -$1,692.45 (-57%) |

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
| Volatility model | 15991 | 4.6% | 0.4% (64) | -672% | ❌ Worse |
| Momentum model | 15991 | 4.6% | 0.4% (64) | -695% | ❌ Worse |
| Mean-reversion model | 15991 | 7.7% | 0.4% (64) | -809% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 15991 | 64 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3718 | 30 | -7% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 2061 | 23 | +39% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 1207 | 15 | +74% | -59% | -58% | -55% |
| Momentum model ≥ 2% | 3161 | 26 | -2% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 1895 | 20 | +35% | -73% | -73% | -68% |
| Momentum model ≥ 10% | 1260 | 13 | +42% | -66% | -65% | -60% |
| Mean-reversion model ≥ 2% | 6226 | 41 | -28% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4325 | 33 | -16% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2862 | 22 | -12% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16189 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5684 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2449 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 24322 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 90 | 0% | -$1,692.45 | -57% | — |
| Sell at 2¢ | 879 | 4% | -$2,611.91 | -88% | 46 sec |
| Sell at 3¢ | 596 | 2% | -$2,608.01 | -88% | 47 sec |
| Sell at 5¢ | 427 | 2% | -$2,562.90 | -87% | 50 sec |
| Sell at 10¢ | 260 | 1% | -$2,471.85 | -84% | 64 sec |
| Sell at 25¢ | 143 | 1% | -$2,283.12 | -77% | 79 sec |
| Sell at 50¢ | 93 | 0% | -$2,058.70 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 922 | 5 | 10% | 4% | -48% | -82% | -84% |
| 2–5 min | 7902 | 40 | 7% | 3% | -50% | -88% | -88% |
| 1–2 min | 6221 | 24 | 3% | 2% | -58% | -92% | -92% |
| Under 1 min | 9273 | 21 | 1% | 0% | -67% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1820 | 11 | 4% | 2% | -25% | -90% | -90% |
| HYPE | 1809 | 6 | 5% | 2% | -59% | -89% | -88% |
| BNB | 1808 | 9 | 5% | 2% | -39% | -82% | -81% |
| DOGE | 1800 | 3 | 4% | 2% | -79% | -91% | -90% |
| ETH | 1798 | 9 | 6% | 3% | -40% | -87% | -86% |
| SOL | 1795 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1788 | 7 | 3% | 1% | -52% | -87% | -87% |
| NEAR | 1786 | 9 | 6% | 3% | -35% | -79% | -79% |
| BTC | 1785 | 10 | 5% | 2% | -25% | -88% | -90% |
| GOLD | 930 | 1 | 3% | 1% | -87% | -92% | -94% |
| SILVER | 903 | 4 | 3% | 1% | -49% | -80% | -80% |
| WTI | 873 | 3 | 3% | 1% | -60% | -94% | -95% |
| COPPER | 784 | 2 | 2% | 1% | -76% | -85% | -85% |
| PLATINUM | 772 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 718 | 5 | 2% | 2% | -35% | -83% | -82% |
| EURUSD | 713 | 3 | 2% | 1% | -61% | -83% | -83% |
| PALLADIUM | 704 | 2 | 1% | 0% | -73% | -85% | -85% |
| GBPUSD | 668 | 1 | 2% | 1% | -86% | -97% | -96% |
| USDJPY | 620 | 3 | 1% | 1% | -55% | -99% | -98% |
| AUDUSD | 250 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 198 | 0 | 1% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12259 | 43 | 4% | 2% | -60% | -89% | -88% |
| DOWN (bought NO) | 12063 | 47 | 3% | 1% | -55% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2755 | 15 | 2% | 1% | -9% | -76% | -76% |
| 0.05–0.1% | 2812 | 10 | 3% | 2% | -48% | -91% | -91% |
| 0.1–0.2% | 4071 | 13 | 5% | 2% | -61% | -89% | -89% |
| 0.2–0.5% | 4716 | 22 | 6% | 3% | -49% | -88% | -88% |
| Over 0.5% | 1832 | 6 | 6% | 3% | -66% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6064 | 24 | 4% | 2% | -55% | -86% | -86% |
| Morning (6am–12pm) | 5814 | 29 | 4% | 2% | -43% | -87% | -86% |
| Afternoon (12–6pm) | 5807 | 19 | 3% | 1% | -61% | -89% | -89% |
| Evening (6pm–12am) | 6637 | 18 | 3% | 2% | -69% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,818 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/19 6:44:32 PM | AUDUSD | DOWN | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 6:44:16 PM | ETH | DOWN | 43 sec | +0.076% | 0¢ | ❌ Lost | $0.00 |
| 10/19 6:44:16 PM | BNB | DOWN | 43 sec | +0.021% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 6:44:16 PM | SILVER | DOWN | 43 sec | — | 5¢ | ❌ Lost | -$0.15 |
| 10/19 6:44:16 PM | PALLADIUM | DOWN | 43 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 6:43:44 PM | XRP | DOWN | 76 sec | +0.093% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 6:43:12 PM | NEAR | DOWN | 1.8 min | +0.322% | 4¢ | ❌ Lost | -$0.15 |
| 10/19 6:43:12 PM | ZEC | DOWN | 1.8 min | +0.451% | 0¢ | ❌ Lost | $0.00 |
| 10/19 6:42:55 PM | DOGE | DOWN | 2.1 min | +0.182% | 0¢ | ❌ Lost | $0.00 |
| 10/19 6:42:24 PM | BTC | DOWN | 2.6 min | +0.171% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 6:42:08 PM | SOL | DOWN | 2.9 min | +0.265% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 6:42:08 PM | NATGAS | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 6:42:08 PM | HYPE | DOWN | 2.9 min | +0.257% | 0¢ | ❌ Lost | $0.00 |
| 10/19 6:29:34 PM | PALLADIUM | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 6:29:18 PM | ZEC | UP | 42 sec | -0.201% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 6:28:47 PM | DOGE | UP | 72 sec | -0.166% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 6:28:47 PM | SILVER | UP | 72 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/19 6:28:31 PM | SOL | UP | 88 sec | -0.176% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 6:28:15 PM | XRP | UP | 1.7 min | -0.239% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 6:28:15 PM | AUDUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 6:28:15 PM | COPPER | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 6:27:27 PM | NEAR | UP | 2.5 min | -0.752% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 6:27:11 PM | BNB | UP | 2.8 min | -0.212% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 6:25:34 PM | WTI | DOWN | 4.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 6:23:07 PM | BTC | UP | 6.9 min | -0.385% | 24¢ | ❌ Lost | -$0.15 |
| 10/19 6:22:37 PM | ETH | UP | 7.4 min | -0.320% | 49¢ | ❌ Lost | -$0.15 |
| 10/19 6:21:33 PM | GBPUSD | UP | 8.4 min | — | 37¢ | ❌ Lost | -$0.15 |
| 10/19 6:14:51 PM | PALLADIUM | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 6:14:19 PM | AUDUSD | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 6:14:19 PM | NATGAS | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
