# 15-Minute 1¢ Study

*Updated Mon Oct 12, 6:48 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1219 finished bets | 1% | $49.40 | +37% | +4.05¢ | $32.30 / $17.10 |

*Expect about **83 buys a day** (~$12.39/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1163 | $29.05 | +23% |
| Volatility model ≥ 2%, hold to the close | 2147 | -$6.15 | -2% |
| Momentum model ≥ 2%, hold to the close | 1887 | -$7.50 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 16036 | 16029 | 63 (0%) | 1.07% | -$1,052.85 (-54%) | Hold to the close: -$1,052.85 (-54%) |

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
| Volatility model | 10633 | 4.5% | 0.4% (46) | -660% | ❌ Worse |
| Momentum model | 10633 | 4.5% | 0.4% (46) | -686% | ❌ Worse |
| Mean-reversion model | 10633 | 7.2% | 0.4% (46) | -768% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 10633 | 46 | -46% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2147 | 18 | -2% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1219 | 13 | +37% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 765 | 9 | +70% | -63% | -62% | -58% |
| Momentum model ≥ 2% | 1887 | 15 | -3% | -79% | -80% | -78% |
| Momentum model ≥ 5% | 1163 | 11 | +23% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 803 | 8 | +41% | -69% | -69% | -64% |
| Mean-reversion model ≥ 2% | 3752 | 27 | -21% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2564 | 20 | -13% | -83% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1701 | 14 | -4% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 10831 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3832 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1366 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 16029 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 63 | 0% | -$1,052.85 | -54% | — |
| Sell at 2¢ | 545 | 3% | -$1,751.15 | -91% | 33 sec |
| Sell at 3¢ | 361 | 2% | -$1,752.06 | -91% | 47 sec |
| Sell at 5¢ | 262 | 2% | -$1,722.55 | -89% | 50 sec |
| Sell at 10¢ | 172 | 1% | -$1,639.53 | -85% | 64 sec |
| Sell at 25¢ | 98 | 1% | -$1,512.47 | -78% | 80 sec |
| Sell at 50¢ | 64 | 0% | -$1,348.85 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 437 | 4 | 11% | 3% | -13% | -81% | -86% |
| 2–5 min | 5154 | 32 | 6% | 3% | -39% | -88% | -89% |
| 1–2 min | 4235 | 16 | 3% | 2% | -59% | -94% | -94% |
| Under 1 min | 6199 | 11 | 1% | 0% | -74% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1216 | 7 | 4% | 2% | -29% | -90% | -90% |
| HYPE | 1213 | 4 | 4% | 2% | -59% | -90% | -89% |
| DOGE | 1207 | 2 | 4% | 2% | -79% | -91% | -90% |
| BNB | 1205 | 5 | 4% | 1% | -49% | -91% | -92% |
| ETH | 1204 | 8 | 5% | 2% | -19% | -90% | -89% |
| SOL | 1204 | 2 | 3% | 1% | -79% | -93% | -92% |
| BTC | 1198 | 6 | 5% | 2% | -33% | -88% | -90% |
| NEAR | 1192 | 7 | 5% | 2% | -23% | -76% | -77% |
| XRP | 1192 | 7 | 2% | 1% | -27% | -85% | -85% |
| GOLD | 631 | 0 | 3% | 1% | -100% | -93% | -94% |
| SILVER | 613 | 1 | 3% | 1% | -81% | -94% | -94% |
| WTI | 588 | 3 | 3% | 1% | -42% | -94% | -96% |
| COPPER | 549 | 0 | 1% | 1% | -100% | -98% | -98% |
| PLATINUM | 506 | 0 | 0% | 0% | -100% | -100% | -99% |
| PALLADIUM | 473 | 1 | 1% | 0% | -80% | -98% | -98% |
| NATGAS | 472 | 3 | 3% | 2% | -41% | -96% | -94% |
| EURUSD | 454 | 3 | 3% | 2% | -38% | -75% | -74% |
| GBPUSD | 433 | 1 | 2% | 1% | -78% | -96% | -96% |
| USDJPY | 390 | 3 | 1% | 1% | -28% | -98% | -97% |
| AUDUSD | 46 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 43 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8116 | 34 | 3% | 2% | -51% | -90% | -89% |
| DOWN (bought NO) | 7913 | 29 | 3% | 2% | -57% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1939 | 10 | 2% | 1% | -14% | -77% | -76% |
| 0.05–0.1% | 1932 | 6 | 3% | 1% | -55% | -92% | -92% |
| 0.1–0.2% | 2765 | 9 | 4% | 2% | -60% | -91% | -92% |
| 0.2–0.5% | 3014 | 18 | 6% | 3% | -34% | -89% | -88% |
| Over 0.5% | 1178 | 5 | 6% | 2% | -56% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4019 | 20 | 4% | 2% | -43% | -86% | -86% |
| Morning (6am–12pm) | 3780 | 20 | 4% | 2% | -39% | -91% | -91% |
| Afternoon (12–6pm) | 3818 | 9 | 3% | 1% | -72% | -91% | -91% |
| Evening (6pm–12am) | 4412 | 14 | 3% | 2% | -64% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,537 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/12 6:44:52 PM | HYPE | UP | 7 sec | -0.249% | 0¢ | ❌ Lost | $0.00 |
| 10/12 6:44:52 PM | PLATINUM | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 6:44:52 PM | PALLADIUM | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 6:44:52 PM | GBPUSD | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 6:44:36 PM | BNB | DOWN | 23 sec | -0.015% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 6:44:36 PM | BTC | DOWN | 23 sec | +0.013% | 46¢ | ✅ Won | $13.85 |
| 10/12 6:44:36 PM | XRP | UP | 23 sec | -0.203% | 0¢ | ❌ Lost | $0.00 |
| 10/12 6:44:20 PM | AUDUSD | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 6:44:20 PM | GOLD | UP | 40 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 6:44:05 PM | ETH | DOWN | 55 sec | +0.118% | 0¢ | ❌ Lost | $0.00 |
| 10/12 6:44:05 PM | WTI | DOWN | 55 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/12 6:43:33 PM | ZEC | UP | 87 sec | -0.465% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 6:43:16 PM | SILVER | UP | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 6:43:16 PM | EURUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 6:43:01 PM | NEAR | UP | 2.0 min | -0.969% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 6:42:45 PM | DOGE | UP | 2.2 min | -0.362% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 6:42:45 PM | SOL | UP | 2.2 min | -0.406% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 6:29:54 PM | GOLD | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 6:29:38 PM | AUDUSD | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 6:29:22 PM | PLATINUM | DOWN | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 6:29:08 PM | COPPER | UP | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 6:28:37 PM | BTC | UP | 82 sec | -0.138% | 0¢ | ❌ Lost | $0.00 |
| 10/12 6:28:37 PM | SILVER | DOWN | 82 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 6:28:21 PM | ETH | UP | 1.6 min | -0.306% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 6:28:21 PM | USDJPY | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 6:28:21 PM | SOL | UP | 1.6 min | -0.513% | 0¢ | ❌ Lost | $0.00 |
| 10/12 6:28:05 PM | DOGE | UP | 1.9 min | -0.549% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 6:27:47 PM | WTI | UP | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 6:27:30 PM | HYPE | UP | 2.5 min | -0.407% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 6:27:30 PM | XRP | UP | 2.5 min | -0.583% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
