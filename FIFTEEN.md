# 15-Minute 1¢ Study

*Updated Wed Oct 14, 6:13 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1438 finished bets | 1% | $93.00 | +58% | +6.47¢ | $34.75 / $58.25 |

*Expect about **86 buys a day** (~$12.89/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1350 | $64.20 | +44% |
| Momentum model ≥ 2%, hold to the close | 2235 | $21.10 | +8% |
| Volatility model ≥ 2%, hold to the close | 2576 | $10.75 | +3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 18549 | 18532 | 74 (0%) | 1.07% | -$1,209.80 (-54%) | Hold to the close: -$1,209.80 (-54%) |

*In play or awaiting result: 16. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 12060 | 4.5% | 0.4% (52) | -636% | ❌ Worse |
| Momentum model | 12060 | 4.5% | 0.4% (52) | -662% | ❌ Worse |
| Mean-reversion model | 12060 | 7.3% | 0.4% (52) | -755% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12060 | 52 | -46% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2576 | 23 | +3% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1438 | 18 | +58% | -73% | -71% | -66% |
| Volatility model ≥ 10% | 864 | 11 | +81% | -64% | -62% | -58% |
| Momentum model ≥ 2% | 2235 | 20 | +8% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1350 | 15 | +44% | -77% | -76% | -73% |
| Momentum model ≥ 10% | 911 | 10 | +55% | -70% | -70% | -65% |
| Mean-reversion model ≥ 2% | 4435 | 32 | -21% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3039 | 25 | -9% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1997 | 14 | -19% | -80% | -80% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12258 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4531 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 1743 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 18532 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 74 | 0% | -$1,209.80 | -54% | — |
| Sell at 2¢ | 651 | 4% | -$2,020.54 | -90% | 34 sec |
| Sell at 3¢ | 438 | 2% | -$2,018.98 | -90% | 46 sec |
| Sell at 5¢ | 320 | 2% | -$1,981.80 | -88% | 49 sec |
| Sell at 10¢ | 202 | 1% | -$1,897.18 | -84% | 63 sec |
| Sell at 25¢ | 117 | 1% | -$1,732.53 | -77% | 79 sec |
| Sell at 50¢ | 78 | 0% | -$1,523.30 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 579 | 5 | 10% | 3% | -18% | -82% | -87% |
| 2–5 min | 5974 | 35 | 7% | 3% | -42% | -88% | -88% |
| 1–2 min | 4842 | 18 | 3% | 2% | -60% | -94% | -93% |
| Under 1 min | 7133 | 16 | 1% | 0% | -68% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1375 | 11 | 5% | 3% | -0% | -89% | -89% |
| HYPE | 1369 | 4 | 4% | 2% | -64% | -90% | -89% |
| ETH | 1366 | 8 | 5% | 3% | -28% | -88% | -87% |
| DOGE | 1366 | 2 | 4% | 2% | -82% | -91% | -90% |
| BNB | 1365 | 5 | 4% | 2% | -55% | -90% | -90% |
| SOL | 1362 | 2 | 3% | 1% | -82% | -93% | -92% |
| BTC | 1353 | 7 | 5% | 2% | -31% | -88% | -91% |
| XRP | 1352 | 7 | 2% | 1% | -36% | -86% | -86% |
| NEAR | 1350 | 8 | 5% | 3% | -23% | -77% | -78% |
| GOLD | 737 | 1 | 4% | 1% | -84% | -91% | -93% |
| SILVER | 722 | 4 | 3% | 1% | -36% | -78% | -77% |
| WTI | 693 | 3 | 3% | 1% | -50% | -94% | -96% |
| COPPER | 638 | 1 | 2% | 2% | -85% | -97% | -96% |
| PLATINUM | 612 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 565 | 1 | 1% | 0% | -83% | -98% | -98% |
| NATGAS | 564 | 3 | 2% | 2% | -50% | -96% | -95% |
| EURUSD | 549 | 3 | 3% | 1% | -49% | -79% | -78% |
| GBPUSD | 516 | 1 | 2% | 1% | -82% | -97% | -96% |
| USDJPY | 469 | 3 | 1% | 1% | -40% | -99% | -98% |
| AUDUSD | 108 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 101 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9353 | 38 | 3% | 2% | -53% | -89% | -88% |
| DOWN (bought NO) | 9179 | 36 | 4% | 2% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2108 | 11 | 2% | 1% | -13% | -78% | -78% |
| 0.05–0.1% | 2160 | 7 | 3% | 1% | -53% | -92% | -91% |
| 0.1–0.2% | 3112 | 10 | 4% | 2% | -60% | -91% | -90% |
| 0.2–0.5% | 3520 | 20 | 6% | 3% | -38% | -88% | -88% |
| Over 0.5% | 1355 | 6 | 6% | 2% | -54% | -89% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4717 | 20 | 4% | 2% | -52% | -87% | -88% |
| Morning (6am–12pm) | 4329 | 23 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 4482 | 16 | 3% | 1% | -58% | -87% | -88% |
| Evening (6pm–12am) | 5004 | 15 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,496 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/14 6:13:50 PM | BTC | DOWN | 69 sec | +0.163% | — | In play | — |
| 10/14 6:13:50 PM | USDJPY | UP | 69 sec | — | — | In play | — |
| 10/14 6:13:34 PM | DOGE | DOWN | 86 sec | +0.106% | — | In play | — |
| 10/14 6:13:34 PM | PALLADIUM | DOWN | 86 sec | — | — | In play | — |
| 10/14 6:13:15 PM | SOL | DOWN | 1.8 min | +0.162% | — | In play | — |
| 10/14 6:12:43 PM | ZEC | DOWN | 2.3 min | +0.376% | — | In play | — |
| 10/14 6:12:43 PM | XRP | DOWN | 2.3 min | +0.196% | — | In play | — |
| 10/14 6:12:26 PM | ETH | DOWN | 2.5 min | +0.236% | — | In play | — |
| 10/14 6:11:35 PM | GOLD | DOWN | 3.4 min | — | — | In play | — |
| 10/14 6:10:28 PM | HYPE | DOWN | 4.5 min | +0.404% | — | In play | — |
| 10/14 5:59:44 PM | ETH | DOWN | 16 sec | +0.001% | 0¢ | ❌ Lost | $0.00 |
| 10/14 5:59:44 PM | XRP | UP | 16 sec | -0.053% | 0¢ | ❌ Lost | $0.00 |
| 10/14 5:59:24 PM | SOL | UP | 35 sec | -0.076% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:59:08 PM | ZEC | DOWN | 51 sec | +0.187% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 5:59:08 PM | BNB | DOWN | 51 sec | -0.026% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:59:08 PM | GBPUSD | DOWN | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:58:52 PM | BTC | DOWN | 67 sec | +0.104% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:58:52 PM | EURUSD | DOWN | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:58:52 PM | HYPE | UP | 67 sec | -0.097% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 5:58:19 PM | NATGAS | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:57:47 PM | SILVER | DOWN | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 5:57:31 PM | GOLD | DOWN | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 5:55:32 PM | DOGE | UP | 4.5 min | -0.428% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 5:44:45 PM | BTC | DOWN | 15 sec | +0.037% | 0¢ | ❌ Lost | $0.00 |
| 10/14 5:44:45 PM | USDJPY | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:44:45 PM | DOGE | DOWN | 15 sec | +0.052% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:44:45 PM | XRP | UP | 15 sec | -0.022% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:44:23 PM | ETH | DOWN | 36 sec | +0.044% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:44:23 PM | ZEC | DOWN | 36 sec | +0.176% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:44:23 PM | GOLD | DOWN | 36 sec | — | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
