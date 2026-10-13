# 15-Minute 1¢ Study

*Updated Mon Oct 12, 10:11 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1242 finished bets | 1% | $46.10 | +34% | +3.71¢ | $31.10 / $15.00 |

*Expect about **83 buys a day** (~$12.51/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1185 | $26.20 | +21% |
| 5+ min left, hold to the close | 444 | -$9.70 | -15% |
| Volatility model ≥ 2%, hold to the close | 2193 | -$12.45 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 16258 | 16251 | 63 (0%) | 1.07% | -$1,082.55 (-55%) | Hold to the close: -$1,082.55 (-55%) |

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
| Volatility model | 10745 | 4.5% | 0.4% (46) | -660% | ❌ Worse |
| Momentum model | 10745 | 4.5% | 0.4% (46) | -687% | ❌ Worse |
| Mean-reversion model | 10745 | 7.2% | 0.4% (46) | -769% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 10745 | 46 | -46% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2193 | 18 | -5% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1242 | 13 | +34% | -72% | -71% | -69% |
| Volatility model ≥ 10% | 776 | 9 | +66% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 1929 | 15 | -6% | -79% | -80% | -78% |
| Momentum model ≥ 5% | 1185 | 11 | +21% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 812 | 8 | +39% | -69% | -69% | -64% |
| Mean-reversion model ≥ 2% | 3815 | 27 | -23% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2611 | 20 | -15% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 1728 | 14 | -6% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 10943 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3896 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1412 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 16251 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 63 | 0% | -$1,082.55 | -55% | — |
| Sell at 2¢ | 550 | 3% | -$1,779.55 | -91% | 33 sec |
| Sell at 3¢ | 364 | 2% | -$1,780.59 | -91% | 46 sec |
| Sell at 5¢ | 264 | 2% | -$1,750.95 | -89% | 49 sec |
| Sell at 10¢ | 174 | 1% | -$1,666.61 | -85% | 63 sec |
| Sell at 25¢ | 99 | 1% | -$1,538.86 | -78% | 79 sec |
| Sell at 50¢ | 64 | 0% | -$1,378.55 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 440 | 4 | 11% | 3% | -14% | -81% | -86% |
| 2–5 min | 5253 | 32 | 6% | 3% | -40% | -88% | -89% |
| 1–2 min | 4291 | 16 | 3% | 2% | -60% | -94% | -94% |
| Under 1 min | 6263 | 11 | 1% | 0% | -74% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1228 | 7 | 4% | 2% | -30% | -90% | -90% |
| HYPE | 1225 | 4 | 4% | 2% | -60% | -90% | -89% |
| DOGE | 1219 | 2 | 4% | 2% | -79% | -91% | -90% |
| BNB | 1218 | 5 | 4% | 1% | -50% | -91% | -91% |
| ETH | 1217 | 8 | 5% | 2% | -20% | -90% | -89% |
| SOL | 1217 | 2 | 3% | 1% | -79% | -93% | -92% |
| BTC | 1210 | 6 | 5% | 2% | -34% | -88% | -90% |
| XRP | 1205 | 7 | 2% | 1% | -28% | -85% | -85% |
| NEAR | 1204 | 7 | 5% | 2% | -24% | -76% | -77% |
| GOLD | 641 | 0 | 3% | 1% | -100% | -93% | -94% |
| SILVER | 624 | 1 | 3% | 1% | -82% | -94% | -94% |
| WTI | 597 | 3 | 3% | 1% | -43% | -94% | -96% |
| COPPER | 558 | 0 | 1% | 1% | -100% | -98% | -97% |
| PLATINUM | 515 | 0 | 0% | 0% | -100% | -100% | -99% |
| PALLADIUM | 483 | 1 | 1% | 0% | -81% | -98% | -98% |
| NATGAS | 478 | 3 | 3% | 2% | -41% | -96% | -94% |
| EURUSD | 465 | 3 | 3% | 2% | -40% | -75% | -74% |
| GBPUSD | 444 | 1 | 2% | 1% | -79% | -96% | -96% |
| USDJPY | 401 | 3 | 1% | 1% | -30% | -98% | -97% |
| AUDUSD | 52 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 50 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8181 | 34 | 3% | 2% | -52% | -90% | -89% |
| DOWN (bought NO) | 8070 | 29 | 3% | 2% | -58% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1942 | 10 | 2% | 1% | -14% | -77% | -76% |
| 0.05–0.1% | 1943 | 6 | 3% | 1% | -55% | -92% | -92% |
| 0.1–0.2% | 2792 | 9 | 4% | 2% | -60% | -91% | -92% |
| 0.2–0.5% | 3066 | 18 | 5% | 3% | -36% | -89% | -89% |
| Over 0.5% | 1197 | 5 | 6% | 2% | -57% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4019 | 20 | 4% | 2% | -43% | -86% | -86% |
| Morning (6am–12pm) | 3780 | 20 | 4% | 2% | -39% | -91% | -91% |
| Afternoon (12–6pm) | 3818 | 9 | 3% | 1% | -72% | -91% | -91% |
| Evening (6pm–12am) | 4634 | 14 | 3% | 1% | -65% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,526 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/12 9:59:52 PM | USDJPY | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 9:59:52 PM | WTI | UP | 7 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/12 9:59:37 PM | GBPUSD | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 9:59:37 PM | PALLADIUM | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 9:59:21 PM | BNB | DOWN | 38 sec | -0.036% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 9:59:05 PM | EURUSD | DOWN | 54 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 9:59:05 PM | SILVER | DOWN | 54 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 9:59:05 PM | DOGE | DOWN | 54 sec | +0.070% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 9:59:05 PM | HYPE | DOWN | 54 sec | +0.071% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 9:58:49 PM | BTC | DOWN | 71 sec | +0.123% | 0¢ | ❌ Lost | $0.00 |
| 10/12 9:58:32 PM | ETH | DOWN | 88 sec | +0.125% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 9:58:32 PM | XRP | UP | 88 sec | -0.197% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 9:58:32 PM | GOLD | DOWN | 88 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 9:58:32 PM | ZEC | DOWN | 88 sec | +0.342% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 9:58:32 PM | SOL | DOWN | 88 sec | +0.105% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 9:58:01 PM | NEAR | DOWN | 2.0 min | +0.384% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 9:56:11 PM | PLATINUM | DOWN | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 9:44:58 PM | PALLADIUM | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 9:44:58 PM | PLATINUM | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 9:44:58 PM | USDJPY | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 9:44:58 PM | NATGAS | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 9:44:58 PM | SILVER | DOWN | 2 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/12 9:44:26 PM | NEAR | UP | 34 sec | -0.381% | 0¢ | ❌ Lost | $0.00 |
| 10/12 9:43:55 PM | COPPER | DOWN | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 9:43:39 PM | EURUSD | UP | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 9:43:07 PM | WTI | DOWN | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 9:42:51 PM | XRP | DOWN | 2.1 min | +0.264% | 0¢ | ❌ Lost | $0.00 |
| 10/12 9:42:51 PM | ZEC | DOWN | 2.1 min | +0.391% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 9:42:51 PM | HYPE | DOWN | 2.1 min | +0.213% | 1¢ | ❌ Lost | $0.00 |
| 10/12 9:42:51 PM | BNB | DOWN | 2.1 min | +0.157% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
