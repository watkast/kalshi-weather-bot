# 15-Minute 1¢ Study

*Updated Tue Oct 13, 1:05 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1244 finished bets | 1% | $45.95 | +34% | +3.69¢ | $31.10 / $14.85 |

*Expect about **83 buys a day** (~$12.43/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1189 | $25.90 | +20% |
| 5+ min left, hold to the close | 444 | -$9.70 | -15% |
| Volatility model ≥ 5%, sell at 50¢ | 1244 | -$13.05 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 16291 | 16284 | 63 (0%) | 1.07% | -$1,086.75 (-55%) | Hold to the close: -$1,086.75 (-55%) |

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
| Volatility model | 10762 | 4.5% | 0.4% (46) | -661% | ❌ Worse |
| Momentum model | 10762 | 4.5% | 0.4% (46) | -688% | ❌ Worse |
| Mean-reversion model | 10762 | 7.2% | 0.4% (46) | -769% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 10762 | 46 | -46% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2200 | 18 | -5% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1244 | 13 | +34% | -73% | -71% | -69% |
| Volatility model ≥ 10% | 778 | 9 | +66% | -63% | -63% | -59% |
| Momentum model ≥ 2% | 1935 | 15 | -6% | -79% | -80% | -78% |
| Momentum model ≥ 5% | 1189 | 11 | +20% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 815 | 8 | +39% | -69% | -69% | -64% |
| Mean-reversion model ≥ 2% | 3823 | 27 | -23% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2615 | 20 | -15% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 1730 | 14 | -6% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 10960 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3907 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1417 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 16284 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 63 | 0% | -$1,086.75 | -55% | — |
| Sell at 2¢ | 551 | 3% | -$1,783.49 | -91% | 33 sec |
| Sell at 3¢ | 365 | 2% | -$1,784.40 | -91% | 46 sec |
| Sell at 5¢ | 264 | 2% | -$1,755.15 | -89% | 49 sec |
| Sell at 10¢ | 174 | 1% | -$1,670.81 | -85% | 63 sec |
| Sell at 25¢ | 99 | 1% | -$1,543.06 | -78% | 79 sec |
| Sell at 50¢ | 64 | 0% | -$1,382.75 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 440 | 4 | 11% | 3% | -14% | -81% | -86% |
| 2–5 min | 5257 | 32 | 6% | 3% | -40% | -88% | -89% |
| 1–2 min | 4302 | 16 | 3% | 2% | -60% | -94% | -94% |
| Under 1 min | 6281 | 11 | 1% | 0% | -74% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1230 | 7 | 4% | 2% | -30% | -90% | -90% |
| HYPE | 1227 | 4 | 4% | 2% | -60% | -90% | -89% |
| DOGE | 1221 | 2 | 4% | 2% | -79% | -91% | -91% |
| BNB | 1220 | 5 | 4% | 1% | -50% | -91% | -91% |
| ETH | 1219 | 8 | 5% | 2% | -20% | -90% | -89% |
| SOL | 1219 | 2 | 3% | 1% | -79% | -93% | -92% |
| BTC | 1211 | 6 | 5% | 2% | -34% | -88% | -90% |
| XRP | 1207 | 7 | 2% | 1% | -28% | -85% | -85% |
| NEAR | 1206 | 7 | 5% | 2% | -24% | -76% | -77% |
| GOLD | 642 | 0 | 3% | 1% | -100% | -93% | -94% |
| SILVER | 625 | 1 | 3% | 1% | -82% | -94% | -94% |
| WTI | 599 | 3 | 3% | 1% | -43% | -94% | -96% |
| COPPER | 560 | 0 | 1% | 1% | -100% | -98% | -97% |
| PLATINUM | 517 | 0 | 0% | 0% | -100% | -100% | -99% |
| PALLADIUM | 485 | 1 | 1% | 0% | -81% | -98% | -98% |
| NATGAS | 479 | 3 | 3% | 2% | -42% | -96% | -94% |
| EURUSD | 466 | 3 | 3% | 2% | -40% | -75% | -74% |
| GBPUSD | 445 | 1 | 2% | 1% | -79% | -96% | -96% |
| USDJPY | 403 | 3 | 1% | 1% | -31% | -98% | -97% |
| AUDUSD | 52 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 51 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8193 | 34 | 3% | 2% | -52% | -90% | -89% |
| DOWN (bought NO) | 8091 | 29 | 3% | 2% | -58% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1948 | 10 | 2% | 1% | -14% | -77% | -76% |
| 0.05–0.1% | 1946 | 6 | 3% | 1% | -55% | -92% | -92% |
| 0.1–0.2% | 2796 | 9 | 4% | 2% | -60% | -91% | -92% |
| 0.2–0.5% | 3070 | 18 | 5% | 3% | -36% | -89% | -89% |
| Over 0.5% | 1197 | 5 | 6% | 2% | -57% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4036 | 20 | 4% | 2% | -43% | -86% | -86% |
| Morning (6am–12pm) | 3780 | 20 | 4% | 2% | -39% | -91% | -91% |
| Afternoon (12–6pm) | 3818 | 9 | 3% | 1% | -72% | -91% | -91% |
| Evening (6pm–12am) | 4650 | 14 | 3% | 1% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,522 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/13 12:59:46 AM | USDJPY | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 12:59:46 AM | WTI | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 12:59:46 AM | NEAR | UP | 14 sec | -0.040% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 12:59:46 AM | SOL | DOWN | 14 sec | +0.030% | 0¢ | ❌ Lost | $0.00 |
| 10/13 12:59:46 AM | PLATINUM | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 12:59:30 AM | NATGAS | DOWN | 30 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 12:59:14 AM | XRP | DOWN | 46 sec | +0.029% | 0¢ | ❌ Lost | $0.00 |
| 10/13 12:59:14 AM | DOGE | DOWN | 46 sec | +0.084% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 12:58:58 AM | BNB | DOWN | 62 sec | +0.017% | 0¢ | ❌ Lost | $0.00 |
| 10/13 12:58:58 AM | BTC | DOWN | 62 sec | +0.059% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 12:58:43 AM | SILVER | DOWN | 77 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 12:58:43 AM | HYPE | DOWN | 77 sec | +0.114% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 12:58:11 AM | COPPER | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 12:58:11 AM | PALLADIUM | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 12:57:55 AM | ZEC | UP | 2.1 min | -0.226% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 12:57:23 AM | ETH | DOWN | 2.6 min | +0.087% | 4¢ | ❌ Lost | -$0.15 |
| 10/13 12:56:20 AM | GOLD | DOWN | 3.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 10:14:56 PM | GBPUSD | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 10:14:56 PM | USDJPY | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 10:14:40 PM | USDCAD | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 10:14:40 PM | BNB | DOWN | 19 sec | +0.015% | 0¢ | ❌ Lost | $0.00 |
| 10/12 10:14:24 PM | XRP | UP | 35 sec | -0.102% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 10:14:24 PM | COPPER | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 10:14:24 PM | NEAR | DOWN | 35 sec | -0.041% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 10:14:24 PM | PLATINUM | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 10:14:08 PM | WTI | UP | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 10:14:08 PM | PALLADIUM | UP | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 10:13:52 PM | EURUSD | UP | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 10:13:52 PM | DOGE | DOWN | 67 sec | +0.127% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 10:13:37 PM | ETH | DOWN | 82 sec | +0.108% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
