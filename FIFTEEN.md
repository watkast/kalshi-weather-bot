# 15-Minute 1¢ Study

*Updated Tue Oct 13, 10:23 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1328 finished bets | 1% | $36.95 | +25% | +2.78¢ | $26.90 / $10.05 |

*Expect about **84 buys a day** (~$12.53/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1257 | $19.30 | +14% |
| 5+ min left, hold to the close | 512 | -$19.30 | -26% |
| Volatility model ≥ 5%, sell at 50¢ | 1328 | -$22.05 | -15% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 17289 | 17282 | 65 (0%) | 1.07% | -$1,179.65 (-56%) | Hold to the close: -$1,179.65 (-56%) |

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
| Volatility model | 11368 | 4.5% | 0.4% (46) | -671% | ❌ Worse |
| Momentum model | 11368 | 4.4% | 0.4% (46) | -697% | ❌ Worse |
| Mean-reversion model | 11368 | 7.3% | 0.4% (46) | -792% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 11368 | 46 | -49% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2356 | 18 | -11% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 1328 | 13 | +25% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 815 | 9 | +59% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 2069 | 15 | -12% | -79% | -80% | -77% |
| Momentum model ≥ 5% | 1257 | 11 | +14% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 858 | 8 | +33% | -69% | -69% | -64% |
| Mean-reversion model ≥ 2% | 4095 | 27 | -28% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2799 | 20 | -21% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1844 | 14 | -12% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 11566 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4183 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1533 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 17282 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 65 | 0% | -$1,179.65 | -56% | — |
| Sell at 2¢ | 595 | 3% | -$1,892.95 | -91% | 33 sec |
| Sell at 3¢ | 397 | 2% | -$1,892.82 | -91% | 46 sec |
| Sell at 5¢ | 287 | 2% | -$1,861.10 | -89% | 48 sec |
| Sell at 10¢ | 182 | 1% | -$1,781.23 | -85% | 63 sec |
| Sell at 25¢ | 101 | 1% | -$1,657.34 | -79% | 77 sec |
| Sell at 50¢ | 65 | 0% | -$1,482.90 | -71% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 508 | 4 | 10% | 3% | -25% | -82% | -87% |
| 2–5 min | 5567 | 32 | 6% | 3% | -43% | -88% | -88% |
| 1–2 min | 4539 | 17 | 3% | 2% | -59% | -94% | -93% |
| Under 1 min | 6664 | 12 | 1% | 0% | -74% | -92% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1297 | 7 | 4% | 2% | -33% | -90% | -90% |
| HYPE | 1293 | 4 | 4% | 2% | -62% | -90% | -89% |
| ETH | 1289 | 8 | 5% | 3% | -24% | -89% | -88% |
| BNB | 1289 | 5 | 4% | 2% | -53% | -90% | -91% |
| DOGE | 1288 | 2 | 4% | 2% | -81% | -91% | -90% |
| SOL | 1284 | 2 | 3% | 1% | -81% | -93% | -92% |
| BTC | 1278 | 6 | 5% | 2% | -38% | -88% | -91% |
| NEAR | 1274 | 7 | 5% | 2% | -28% | -77% | -78% |
| XRP | 1274 | 7 | 2% | 1% | -32% | -85% | -86% |
| GOLD | 684 | 1 | 4% | 1% | -83% | -92% | -93% |
| SILVER | 671 | 2 | 3% | 1% | -66% | -94% | -93% |
| WTI | 641 | 3 | 3% | 1% | -46% | -94% | -96% |
| COPPER | 590 | 0 | 2% | 1% | -100% | -97% | -96% |
| PLATINUM | 562 | 0 | 1% | 0% | -100% | -99% | -99% |
| PALLADIUM | 519 | 1 | 1% | 0% | -82% | -98% | -98% |
| NATGAS | 516 | 3 | 3% | 2% | -46% | -96% | -94% |
| EURUSD | 499 | 3 | 3% | 2% | -44% | -77% | -76% |
| GBPUSD | 471 | 1 | 2% | 1% | -80% | -96% | -96% |
| USDJPY | 428 | 3 | 1% | 1% | -35% | -98% | -98% |
| AUDUSD | 72 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 63 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8689 | 35 | 3% | 2% | -53% | -90% | -89% |
| DOWN (bought NO) | 8593 | 30 | 3% | 2% | -60% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2025 | 10 | 2% | 1% | -17% | -77% | -77% |
| 0.05–0.1% | 2057 | 6 | 3% | 1% | -58% | -92% | -91% |
| 0.1–0.2% | 2955 | 9 | 4% | 2% | -62% | -91% | -91% |
| 0.2–0.5% | 3262 | 18 | 5% | 3% | -39% | -89% | -88% |
| Over 0.5% | 1264 | 5 | 6% | 2% | -59% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4344 | 20 | 4% | 2% | -47% | -87% | -87% |
| Morning (6am–12pm) | 3923 | 20 | 4% | 2% | -41% | -91% | -91% |
| Afternoon (12–6pm) | 4113 | 10 | 3% | 1% | -71% | -91% | -91% |
| Evening (6pm–12am) | 4902 | 15 | 3% | 2% | -65% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,545 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/13 10:14:54 PM | GBPUSD | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:14:38 PM | PLATINUM | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:14:38 PM | NATGAS | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:14:38 PM | BNB | UP | 21 sec | -0.021% | 0¢ | ❌ Lost | $0.00 |
| 10/13 10:14:38 PM | WTI | UP | 21 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/13 10:14:21 PM | ZEC | UP | 38 sec | -0.225% | 0¢ | ❌ Lost | $0.00 |
| 10/13 10:14:21 PM | HYPE | UP | 38 sec | -0.159% | 0¢ | ❌ Lost | $0.00 |
| 10/13 10:14:21 PM | BTC | DOWN | 38 sec | +0.009% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:14:04 PM | ETH | UP | 55 sec | -0.052% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:14:04 PM | DOGE | UP | 55 sec | -0.157% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:13:48 PM | SILVER | UP | 71 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/13 10:13:48 PM | SOL | UP | 71 sec | -0.118% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:13:15 PM | COPPER | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:12:40 PM | EURUSD | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:12:24 PM | XRP | UP | 2.6 min | -0.182% | 2¢ | ❌ Lost | -$0.15 |
| 10/13 10:12:10 PM | GOLD | UP | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 9:59:13 PM | EURUSD | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 9:58:54 PM | COPPER | UP | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 9:58:22 PM | SOL | UP | 1.6 min | -0.188% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 9:58:22 PM | NATGAS | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 9:58:22 PM | BTC | UP | 1.6 min | -0.113% | 0¢ | ❌ Lost | $0.00 |
| 10/13 9:57:03 PM | XRP | UP | 2.9 min | -0.182% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 9:56:44 PM | HYPE | UP | 3.2 min | -0.232% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 9:56:44 PM | BNB | UP | 3.2 min | -0.174% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 9:56:28 PM | ETH | UP | 3.5 min | -0.151% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 9:56:28 PM | NEAR | UP | 3.5 min | -0.592% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 9:56:28 PM | DOGE | UP | 3.5 min | -0.247% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 9:44:49 PM | EURUSD | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 9:44:49 PM | ZEC | DOWN | 11 sec | +0.059% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 9:44:49 PM | USDJPY | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
