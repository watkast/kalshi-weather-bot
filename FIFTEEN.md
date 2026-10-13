# 15-Minute 1¢ Study

*Updated Mon Oct 12, 7:08 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1219 finished bets | 1% | $49.40 | +37% | +4.05¢ | $32.30 / $17.10 |

*Expect about **83 buys a day** (~$12.38/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1163 | $29.05 | +23% |
| Volatility model ≥ 2%, hold to the close | 2148 | -$6.30 | -2% |
| Momentum model ≥ 2%, hold to the close | 1889 | -$7.80 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 16051 | 16044 | 63 (0%) | 1.07% | -$1,054.95 (-54%) | Hold to the close: -$1,054.95 (-54%) |

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
| Volatility model | 10640 | 4.5% | 0.4% (46) | -660% | ❌ Worse |
| Momentum model | 10640 | 4.5% | 0.4% (46) | -686% | ❌ Worse |
| Mean-reversion model | 10640 | 7.2% | 0.4% (46) | -768% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 10640 | 46 | -46% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2148 | 18 | -2% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1219 | 13 | +37% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 765 | 9 | +70% | -63% | -62% | -58% |
| Momentum model ≥ 2% | 1889 | 15 | -4% | -79% | -80% | -78% |
| Momentum model ≥ 5% | 1163 | 11 | +23% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 803 | 8 | +41% | -69% | -69% | -64% |
| Mean-reversion model ≥ 2% | 3755 | 27 | -21% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2567 | 20 | -13% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 1702 | 14 | -5% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 10838 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3836 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1370 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 16044 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 63 | 0% | -$1,054.95 | -54% | — |
| Sell at 2¢ | 546 | 3% | -$1,752.99 | -91% | 33 sec |
| Sell at 3¢ | 362 | 2% | -$1,753.77 | -91% | 46 sec |
| Sell at 5¢ | 263 | 2% | -$1,724.00 | -89% | 49 sec |
| Sell at 10¢ | 173 | 1% | -$1,640.32 | -85% | 63 sec |
| Sell at 25¢ | 98 | 1% | -$1,514.57 | -78% | 80 sec |
| Sell at 50¢ | 64 | 0% | -$1,350.95 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 437 | 4 | 11% | 3% | -13% | -81% | -86% |
| 2–5 min | 5159 | 32 | 6% | 3% | -39% | -88% | -89% |
| 1–2 min | 4240 | 16 | 3% | 2% | -59% | -94% | -94% |
| Under 1 min | 6204 | 11 | 1% | 0% | -74% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1217 | 7 | 4% | 2% | -29% | -90% | -90% |
| HYPE | 1213 | 4 | 4% | 2% | -59% | -90% | -89% |
| DOGE | 1208 | 2 | 4% | 2% | -79% | -91% | -90% |
| BNB | 1206 | 5 | 4% | 1% | -49% | -91% | -92% |
| ETH | 1205 | 8 | 5% | 2% | -19% | -90% | -89% |
| SOL | 1205 | 2 | 3% | 1% | -79% | -93% | -92% |
| BTC | 1198 | 6 | 5% | 2% | -33% | -88% | -90% |
| NEAR | 1193 | 7 | 5% | 2% | -23% | -76% | -77% |
| XRP | 1193 | 7 | 2% | 1% | -27% | -85% | -85% |
| GOLD | 632 | 0 | 3% | 1% | -100% | -93% | -94% |
| SILVER | 614 | 1 | 3% | 1% | -81% | -94% | -94% |
| WTI | 588 | 3 | 3% | 1% | -42% | -94% | -96% |
| COPPER | 550 | 0 | 1% | 1% | -100% | -98% | -97% |
| PLATINUM | 506 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 473 | 3 | 3% | 2% | -41% | -96% | -94% |
| PALLADIUM | 473 | 1 | 1% | 0% | -80% | -98% | -98% |
| EURUSD | 455 | 3 | 3% | 2% | -38% | -75% | -74% |
| GBPUSD | 434 | 1 | 2% | 1% | -78% | -96% | -96% |
| USDJPY | 391 | 3 | 1% | 1% | -28% | -98% | -97% |
| AUDUSD | 46 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 44 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8127 | 34 | 3% | 2% | -52% | -90% | -89% |
| DOWN (bought NO) | 7917 | 29 | 3% | 2% | -58% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1939 | 10 | 2% | 1% | -14% | -77% | -76% |
| 0.05–0.1% | 1932 | 6 | 3% | 1% | -55% | -92% | -92% |
| 0.1–0.2% | 2766 | 9 | 4% | 2% | -60% | -91% | -92% |
| 0.2–0.5% | 3016 | 18 | 6% | 3% | -34% | -89% | -88% |
| Over 0.5% | 1182 | 5 | 6% | 2% | -56% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4019 | 20 | 4% | 2% | -43% | -86% | -86% |
| Morning (6am–12pm) | 3780 | 20 | 4% | 2% | -39% | -91% | -91% |
| Afternoon (12–6pm) | 3818 | 9 | 3% | 1% | -72% | -91% | -91% |
| Evening (6pm–12am) | 4427 | 14 | 3% | 2% | -64% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,534 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/12 6:59:53 PM | USDCAD | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 6:59:38 PM | ZEC | DOWN | 22 sec | +0.469% | 0¢ | ❌ Lost | $0.00 |
| 10/12 6:59:22 PM | NATGAS | UP | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 6:59:06 PM | GBPUSD | DOWN | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 6:59:06 PM | BNB | UP | 54 sec | -0.158% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 6:58:49 PM | SILVER | UP | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 6:58:34 PM | EURUSD | DOWN | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 6:58:02 PM | USDJPY | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 6:58:02 PM | ETH | UP | 2.0 min | -0.343% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 6:58:02 PM | GOLD | UP | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 6:57:46 PM | XRP | UP | 2.2 min | -0.701% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 6:57:29 PM | NEAR | UP | 2.5 min | -0.976% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 6:57:13 PM | DOGE | UP | 2.8 min | -0.912% | 2¢ | ❌ Lost | -$0.15 |
| 10/12 6:56:57 PM | SOL | UP | 3.0 min | -0.946% | 2¢ | ❌ Lost | -$0.15 |
| 10/12 6:56:28 PM | COPPER | UP | 3.5 min | — | 12¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
