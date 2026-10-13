# 15-Minute 1¢ Study

*Updated Mon Oct 12, 7:39 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1223 finished bets | 1% | $48.80 | +37% | +3.99¢ | $32.00 / $16.80 |

*Expect about **83 buys a day** (~$12.40/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1169 | $28.15 | +22% |
| Volatility model ≥ 2%, hold to the close | 2160 | -$8.10 | -3% |
| Momentum model ≥ 2%, hold to the close | 1896 | -$8.85 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 16089 | 16082 | 63 (0%) | 1.07% | -$1,060.50 (-55%) | Hold to the close: -$1,060.50 (-55%) |

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
| Volatility model | 10658 | 4.5% | 0.4% (46) | -660% | ❌ Worse |
| Momentum model | 10658 | 4.5% | 0.4% (46) | -686% | ❌ Worse |
| Mean-reversion model | 10658 | 7.2% | 0.4% (46) | -768% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 10658 | 46 | -46% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2160 | 18 | -3% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1223 | 13 | +37% | -72% | -71% | -69% |
| Volatility model ≥ 10% | 768 | 9 | +69% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 1896 | 15 | -4% | -79% | -80% | -78% |
| Momentum model ≥ 5% | 1169 | 11 | +22% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 806 | 8 | +41% | -69% | -69% | -64% |
| Mean-reversion model ≥ 2% | 3769 | 27 | -22% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2577 | 20 | -14% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 1707 | 14 | -5% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 10856 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3848 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1378 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 16082 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 63 | 0% | -$1,060.50 | -55% | — |
| Sell at 2¢ | 547 | 3% | -$1,758.28 | -91% | 33 sec |
| Sell at 3¢ | 362 | 2% | -$1,759.32 | -91% | 46 sec |
| Sell at 5¢ | 263 | 2% | -$1,729.55 | -89% | 49 sec |
| Sell at 10¢ | 173 | 1% | -$1,645.87 | -85% | 63 sec |
| Sell at 25¢ | 98 | 1% | -$1,520.12 | -78% | 80 sec |
| Sell at 50¢ | 64 | 0% | -$1,356.50 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 440 | 4 | 11% | 3% | -14% | -81% | -86% |
| 2–5 min | 5183 | 32 | 6% | 3% | -39% | -88% | -89% |
| 1–2 min | 4248 | 16 | 3% | 2% | -59% | -94% | -94% |
| Under 1 min | 6207 | 11 | 1% | 0% | -74% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1219 | 7 | 4% | 2% | -29% | -90% | -90% |
| HYPE | 1215 | 4 | 4% | 2% | -59% | -90% | -89% |
| DOGE | 1210 | 2 | 4% | 2% | -79% | -91% | -90% |
| BNB | 1208 | 5 | 4% | 1% | -50% | -91% | -92% |
| ETH | 1207 | 8 | 5% | 2% | -19% | -90% | -89% |
| SOL | 1207 | 2 | 3% | 1% | -79% | -93% | -92% |
| BTC | 1200 | 6 | 5% | 2% | -33% | -88% | -90% |
| NEAR | 1195 | 7 | 5% | 2% | -23% | -76% | -77% |
| XRP | 1195 | 7 | 2% | 1% | -27% | -85% | -85% |
| GOLD | 634 | 0 | 3% | 1% | -100% | -93% | -94% |
| SILVER | 616 | 1 | 3% | 1% | -81% | -94% | -94% |
| WTI | 589 | 3 | 3% | 1% | -42% | -94% | -96% |
| COPPER | 552 | 0 | 1% | 1% | -100% | -98% | -97% |
| PLATINUM | 508 | 0 | 0% | 0% | -100% | -100% | -99% |
| PALLADIUM | 475 | 1 | 1% | 0% | -80% | -98% | -98% |
| NATGAS | 474 | 3 | 3% | 2% | -41% | -96% | -94% |
| EURUSD | 456 | 3 | 3% | 2% | -39% | -75% | -74% |
| GBPUSD | 436 | 1 | 2% | 1% | -79% | -96% | -96% |
| USDJPY | 393 | 3 | 1% | 1% | -29% | -98% | -97% |
| AUDUSD | 48 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 45 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8137 | 34 | 3% | 2% | -52% | -90% | -89% |
| DOWN (bought NO) | 7945 | 29 | 3% | 2% | -58% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1939 | 10 | 2% | 1% | -14% | -77% | -76% |
| 0.05–0.1% | 1933 | 6 | 3% | 1% | -55% | -92% | -92% |
| 0.1–0.2% | 2768 | 9 | 4% | 2% | -60% | -91% | -92% |
| 0.2–0.5% | 3020 | 18 | 5% | 3% | -35% | -89% | -88% |
| Over 0.5% | 1193 | 5 | 6% | 2% | -57% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4019 | 20 | 4% | 2% | -43% | -86% | -86% |
| Morning (6am–12pm) | 3780 | 20 | 4% | 2% | -39% | -91% | -91% |
| Afternoon (12–6pm) | 3818 | 9 | 3% | 1% | -72% | -91% | -91% |
| Evening (6pm–12am) | 4465 | 14 | 3% | 2% | -64% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,534 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/12 7:29:33 PM | NATGAS | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 7:29:33 PM | AUDUSD | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 7:29:17 PM | USDJPY | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 7:28:40 PM | HYPE | DOWN | 79 sec | +0.176% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 7:28:40 PM | GBPUSD | UP | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 7:28:40 PM | BNB | DOWN | 79 sec | +0.085% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 7:28:24 PM | SOL | DOWN | 1.6 min | +0.169% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 7:28:08 PM | PALLADIUM | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 7:28:08 PM | COPPER | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 7:27:52 PM | NEAR | DOWN | 2.1 min | +0.419% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 7:26:17 PM | BTC | DOWN | 3.7 min | +0.251% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 7:26:17 PM | ETH | DOWN | 3.7 min | +0.405% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 7:25:29 PM | DOGE | DOWN | 4.5 min | +0.707% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 7:25:29 PM | PLATINUM | UP | 4.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 7:25:13 PM | ZEC | DOWN | 4.8 min | +1.410% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 7:25:13 PM | GOLD | UP | 4.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 7:25:13 PM | XRP | DOWN | 4.8 min | +0.659% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 7:24:57 PM | SILVER | UP | 5.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 7:13:21 PM | PALLADIUM | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 7:13:21 PM | AUDUSD | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 7:12:34 PM | COPPER | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 7:12:18 PM | GOLD | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 7:11:28 PM | EURUSD | DOWN | 3.5 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/12 7:11:28 PM | HYPE | DOWN | 3.5 min | +0.730% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 7:11:28 PM | SILVER | DOWN | 3.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 7:11:28 PM | GBPUSD | DOWN | 3.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 7:11:28 PM | WTI | UP | 3.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 7:11:12 PM | BTC | DOWN | 3.8 min | +0.434% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 7:11:12 PM | ZEC | DOWN | 3.8 min | +1.209% | 0¢ | ❌ Lost | $0.00 |
| 10/12 7:11:12 PM | SOL | DOWN | 3.8 min | +0.838% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
