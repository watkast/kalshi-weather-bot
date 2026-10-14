# 15-Minute 1¢ Study

*Updated Wed Oct 14, 2:08 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1414 finished bets | 1% | $67.85 | +43% | +4.80¢ | $36.10 / $31.75 |

*Expect about **85 buys a day** (~$12.81/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1329 | $38.60 | +27% |
| Momentum model ≥ 2%, hold to the close | 2197 | -$2.10 | -1% |
| Volatility model ≥ 2%, hold to the close | 2534 | -$12.00 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 18303 | 18296 | 69 (0%) | 1.07% | -$1,251.60 (-56%) | Hold to the close: -$1,251.60 (-56%) |

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
| Volatility model | 11918 | 4.5% | 0.4% (49) | -655% | ❌ Worse |
| Momentum model | 11918 | 4.4% | 0.4% (49) | -680% | ❌ Worse |
| Mean-reversion model | 11918 | 7.3% | 0.4% (49) | -777% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 11918 | 49 | -48% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2534 | 21 | -4% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1414 | 16 | +43% | -73% | -71% | -66% |
| Volatility model ≥ 10% | 851 | 9 | +51% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 2197 | 18 | -1% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1329 | 13 | +27% | -77% | -77% | -74% |
| Momentum model ≥ 10% | 895 | 8 | +26% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 4372 | 30 | -25% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2994 | 23 | -15% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1973 | 14 | -18% | -80% | -80% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12116 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4479 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1701 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 18296 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 69 | 0% | -$1,251.60 | -56% | — |
| Sell at 2¢ | 637 | 3% | -$2,009.98 | -91% | 34 sec |
| Sell at 3¢ | 430 | 2% | -$2,007.90 | -91% | 46 sec |
| Sell at 5¢ | 314 | 2% | -$1,971.50 | -89% | 49 sec |
| Sell at 10¢ | 198 | 1% | -$1,888.22 | -85% | 64 sec |
| Sell at 25¢ | 114 | 1% | -$1,742.26 | -79% | 80 sec |
| Sell at 50¢ | 75 | 0% | -$1,543.35 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 576 | 4 | 10% | 2% | -34% | -82% | -88% |
| 2–5 min | 5901 | 34 | 7% | 3% | -43% | -88% | -88% |
| 1–2 min | 4783 | 18 | 3% | 2% | -59% | -94% | -93% |
| Under 1 min | 7032 | 13 | 1% | 0% | -73% | -92% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1358 | 9 | 5% | 3% | -17% | -89% | -90% |
| HYPE | 1354 | 4 | 4% | 2% | -63% | -90% | -89% |
| ETH | 1351 | 8 | 5% | 3% | -28% | -88% | -87% |
| DOGE | 1350 | 2 | 4% | 2% | -81% | -91% | -90% |
| BNB | 1349 | 5 | 5% | 2% | -55% | -90% | -89% |
| SOL | 1346 | 2 | 3% | 1% | -82% | -93% | -92% |
| BTC | 1337 | 6 | 5% | 2% | -40% | -88% | -91% |
| XRP | 1336 | 7 | 2% | 1% | -35% | -86% | -86% |
| NEAR | 1335 | 8 | 5% | 3% | -22% | -77% | -78% |
| GOLD | 726 | 1 | 4% | 1% | -84% | -91% | -93% |
| SILVER | 714 | 2 | 3% | 1% | -67% | -94% | -94% |
| WTI | 682 | 3 | 3% | 1% | -49% | -94% | -96% |
| COPPER | 633 | 1 | 2% | 2% | -85% | -97% | -96% |
| PLATINUM | 607 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 562 | 1 | 1% | 0% | -83% | -98% | -98% |
| NATGAS | 555 | 3 | 2% | 2% | -50% | -96% | -95% |
| EURUSD | 540 | 3 | 3% | 1% | -48% | -78% | -77% |
| GBPUSD | 507 | 1 | 2% | 1% | -82% | -97% | -96% |
| USDJPY | 461 | 3 | 1% | 1% | -39% | -98% | -98% |
| AUDUSD | 103 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 90 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9235 | 35 | 3% | 2% | -56% | -90% | -89% |
| DOWN (bought NO) | 9061 | 34 | 3% | 2% | -57% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2089 | 10 | 2% | 1% | -20% | -78% | -78% |
| 0.05–0.1% | 2138 | 7 | 3% | 1% | -53% | -92% | -91% |
| 0.1–0.2% | 3076 | 9 | 4% | 2% | -64% | -91% | -91% |
| 0.2–0.5% | 3461 | 20 | 6% | 3% | -36% | -88% | -88% |
| Over 0.5% | 1349 | 5 | 6% | 2% | -61% | -89% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4717 | 20 | 4% | 2% | -52% | -87% | -88% |
| Morning (6am–12pm) | 4329 | 23 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 4246 | 11 | 3% | 1% | -69% | -90% | -91% |
| Evening (6pm–12am) | 5004 | 15 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,494 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/14 1:59:48 PM | BTC | DOWN | 11 sec | +0.044% | 0¢ | ❌ Lost | $0.00 |
| 10/14 1:59:48 PM | SILVER | DOWN | 11 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 1:59:48 PM | GOLD | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:59:48 PM | PALLADIUM | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:59:16 PM | ETH | UP | 43 sec | -0.081% | 0¢ | ❌ Lost | $0.00 |
| 10/14 1:59:16 PM | DOGE | UP | 43 sec | -0.066% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:59:16 PM | ZEC | DOWN | 43 sec | +0.114% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:59:16 PM | GBPUSD | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:58:28 PM | EURUSD | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:58:28 PM | COPPER | UP | 1.5 min | — | 9¢ | ❌ Lost | -$0.15 |
| 10/14 1:57:33 PM | NEAR | DOWN | 2.4 min | +0.427% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 1:57:33 PM | AUDUSD | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:57:33 PM | SOL | UP | 2.4 min | -0.207% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 1:57:33 PM | XRP | UP | 2.4 min | -0.226% | 2¢ | ❌ Lost | -$0.15 |
| 10/14 1:57:17 PM | USDCAD | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:56:29 PM | HYPE | DOWN | 3.5 min | +0.472% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 1:54:19 PM | NATGAS | DOWN | 5.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 1:44:52 PM | NATGAS | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:44:52 PM | ZEC | UP | 7 sec | -0.123% | 0¢ | ❌ Lost | $0.00 |
| 10/14 1:44:52 PM | WTI | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:44:52 PM | USDJPY | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:44:52 PM | GOLD | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:44:36 PM | SILVER | UP | 24 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/14 1:44:36 PM | HYPE | UP | 24 sec | -0.118% | 0¢ | ❌ Lost | $0.00 |
| 10/14 1:44:36 PM | PALLADIUM | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:44:36 PM | EURUSD | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:44:36 PM | BNB | UP | 24 sec | -0.080% | 0¢ | ❌ Lost | $0.00 |
| 10/14 1:44:19 PM | USDCAD | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:44:19 PM | GBPUSD | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:44:03 PM | BTC | UP | 56 sec | -0.067% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
