# 15-Minute 1¢ Study

*Updated Mon Oct 19, 6:10 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2060 finished bets | 1% | $91.15 | +39% | +4.42¢ | $27.35 / $63.80 |

*Expect about **95 buys a day** (~$14.22/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1895 | $72.10 | +35% |
| Momentum model ≥ 2%, hold to the close | 3159 | -$5.75 | -2% |
| Volatility model ≥ 5%, sell at 50¢ | 2060 | -$25.85 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 24291 | 24278 | 90 (0%) | 1.07% | -$1,686.60 (-57%) | Hold to the close: -$1,686.60 (-57%) |

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
| Volatility model | 15965 | 4.6% | 0.4% (64) | -673% | ❌ Worse |
| Momentum model | 15965 | 4.6% | 0.4% (64) | -696% | ❌ Worse |
| Mean-reversion model | 15965 | 7.7% | 0.4% (64) | -809% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 15965 | 64 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3715 | 30 | -7% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 2060 | 23 | +39% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 1206 | 15 | +74% | -59% | -58% | -55% |
| Momentum model ≥ 2% | 3159 | 26 | -2% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 1895 | 20 | +35% | -73% | -73% | -68% |
| Momentum model ≥ 10% | 1260 | 13 | +42% | -66% | -65% | -60% |
| Mean-reversion model ≥ 2% | 6214 | 41 | -28% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 4318 | 33 | -16% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2859 | 22 | -12% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16163 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5673 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2442 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 24278 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 90 | 0% | -$1,686.60 | -57% | — |
| Sell at 2¢ | 873 | 4% | -$2,607.62 | -88% | 46 sec |
| Sell at 3¢ | 590 | 2% | -$2,604.50 | -88% | 47 sec |
| Sell at 5¢ | 424 | 2% | -$2,559.00 | -87% | 50 sec |
| Sell at 10¢ | 257 | 1% | -$2,469.93 | -84% | 63 sec |
| Sell at 25¢ | 141 | 1% | -$2,283.89 | -78% | 79 sec |
| Sell at 50¢ | 93 | 0% | -$2,052.85 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 917 | 5 | 10% | 3% | -48% | -82% | -85% |
| 2–5 min | 7885 | 40 | 7% | 3% | -50% | -88% | -87% |
| 1–2 min | 6209 | 24 | 3% | 2% | -58% | -92% | -92% |
| Under 1 min | 9263 | 21 | 1% | 0% | -67% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1817 | 11 | 4% | 2% | -25% | -90% | -90% |
| HYPE | 1807 | 6 | 5% | 2% | -59% | -89% | -88% |
| BNB | 1805 | 9 | 5% | 2% | -39% | -82% | -81% |
| DOGE | 1797 | 3 | 4% | 2% | -79% | -91% | -90% |
| ETH | 1795 | 9 | 6% | 3% | -40% | -87% | -87% |
| SOL | 1792 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1785 | 7 | 3% | 1% | -52% | -87% | -87% |
| NEAR | 1783 | 9 | 6% | 3% | -35% | -79% | -79% |
| BTC | 1782 | 10 | 5% | 2% | -25% | -88% | -90% |
| GOLD | 929 | 1 | 3% | 1% | -87% | -92% | -94% |
| SILVER | 900 | 4 | 3% | 1% | -49% | -81% | -81% |
| WTI | 872 | 3 | 3% | 1% | -60% | -94% | -95% |
| COPPER | 783 | 2 | 2% | 1% | -76% | -85% | -85% |
| PLATINUM | 772 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 716 | 5 | 2% | 2% | -35% | -83% | -82% |
| EURUSD | 712 | 3 | 2% | 1% | -61% | -83% | -83% |
| PALLADIUM | 701 | 2 | 1% | 0% | -73% | -85% | -85% |
| GBPUSD | 666 | 1 | 2% | 1% | -86% | -97% | -97% |
| USDJPY | 620 | 3 | 1% | 1% | -55% | -99% | -98% |
| AUDUSD | 247 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 197 | 0 | 1% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12233 | 43 | 4% | 2% | -60% | -89% | -88% |
| DOWN (bought NO) | 12045 | 47 | 3% | 1% | -55% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2754 | 15 | 2% | 1% | -9% | -76% | -76% |
| 0.05–0.1% | 2810 | 10 | 3% | 2% | -48% | -91% | -91% |
| 0.1–0.2% | 4067 | 13 | 5% | 2% | -61% | -89% | -89% |
| 0.2–0.5% | 4700 | 22 | 6% | 3% | -49% | -88% | -88% |
| Over 0.5% | 1829 | 6 | 6% | 3% | -66% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6064 | 24 | 4% | 2% | -55% | -86% | -86% |
| Morning (6am–12pm) | 5814 | 29 | 4% | 2% | -43% | -87% | -86% |
| Afternoon (12–6pm) | 5807 | 19 | 3% | 1% | -61% | -89% | -89% |
| Evening (6pm–12am) | 6593 | 18 | 3% | 2% | -69% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,813 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/19 6:10:18 PM | NEAR | UP | 4.7 min | -1.242% | — | In play | — |
| 10/19 6:10:18 PM | ZEC | UP | 4.7 min | -0.843% | — | In play | — |
| 10/19 6:10:18 PM | GOLD | DOWN | 4.7 min | — | — | In play | — |
| 10/19 6:10:18 PM | HYPE | UP | 4.7 min | -0.455% | — | In play | — |
| 10/19 6:08:57 PM | ETH | UP | 6.0 min | -0.227% | — | In play | — |
| 10/19 6:08:57 PM | BNB | UP | 6.0 min | -0.316% | — | In play | — |
| 10/19 5:59:51 PM | COPPER | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 5:59:51 PM | NATGAS | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 5:59:51 PM | PLATINUM | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 5:59:19 PM | SILVER | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 5:58:31 PM | DOGE | UP | 88 sec | -0.100% | 0¢ | ❌ Lost | $0.00 |
| 10/19 5:58:15 PM | XRP | UP | 1.7 min | -0.138% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 5:57:59 PM | USDJPY | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 5:57:41 PM | ZEC | UP | 2.3 min | -0.344% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 5:56:53 PM | ETH | UP | 3.1 min | -0.130% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 5:56:53 PM | NEAR | UP | 3.1 min | -0.581% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 5:56:53 PM | BTC | UP | 3.1 min | -0.150% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 5:56:53 PM | SOL | UP | 3.1 min | -0.209% | 0¢ | ❌ Lost | $0.00 |
| 10/19 5:56:21 PM | GOLD | UP | 3.6 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/19 5:54:33 PM | HYPE | UP | 5.4 min | -0.256% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 5:53:29 PM | BNB | UP | 6.5 min | -0.300% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 5:44:58 PM | PLATINUM | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 5:44:58 PM | GOLD | DOWN | 1 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/19 5:44:42 PM | NATGAS | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 5:44:42 PM | NEAR | DOWN | 17 sec | +0.002% | 0¢ | ❌ Lost | $0.00 |
| 10/19 5:44:26 PM | AUDUSD | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 5:44:10 PM | USDJPY | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 5:43:54 PM | SILVER | DOWN | 65 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 5:43:54 PM | GBPUSD | DOWN | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 5:43:38 PM | EURUSD | DOWN | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
