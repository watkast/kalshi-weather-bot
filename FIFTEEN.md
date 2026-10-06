# 15-Minute 1¢ Study

*Updated Tue Oct 6, 1:15 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 633 finished bets | 1% | $30.05 | +44% | +4.75¢ | -$6.65 / $36.70 |

*Expect about **79 buys a day** (~$11.83/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 633 | $16.50 | +24% |
| Volatility model ≥ 2%, hold to the close | 1177 | $12.25 | +9% |
| Mean-reversion model ≥ 5%, hold to the close | 1392 | $7.25 | +4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 9248 | 9231 | 40 (0%) | 1.07% | -$550.90 (-50%) | Hold to the close: -$550.90 (-50%) |

*In play or awaiting result: 17. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 6047 | 4.0% | 0.5% (28) | -570% | ❌ Worse |
| Momentum model | 6047 | 4.1% | 0.5% (28) | -594% | ❌ Worse |
| Mean-reversion model | 6047 | 6.7% | 0.5% (28) | -667% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6047 | 28 | -41% | -85% | -86% | -83% |
| Volatility model ≥ 2% | 1177 | 11 | +9% | -71% | -71% | -66% |
| Volatility model ≥ 5% | 633 | 7 | +44% | -58% | -57% | -54% |
| Volatility model ≥ 10% | 389 | 5 | +92% | -39% | -40% | -35% |
| Momentum model ≥ 2% | 1042 | 9 | +4% | -71% | -73% | -71% |
| Momentum model ≥ 5% | 633 | 6 | +24% | -63% | -65% | -63% |
| Momentum model ≥ 10% | 437 | 5 | +64% | -51% | -52% | -49% |
| Mean-reversion model ≥ 2% | 2072 | 15 | -21% | -83% | -83% | -79% |
| Mean-reversion model ≥ 5% | 1392 | 13 | +4% | -80% | -79% | -73% |
| Mean-reversion model ≥ 10% | 919 | 9 | +13% | -78% | -78% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6244 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 2258 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 729 | 3% | 3% | 2% | 2% | 1% | 0% |
| **All** | 9231 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 40 | 0% | -$550.90 | -50% | — |
| Sell at 2¢ | 344 | 4% | -$993.46 | -89% | 33 sec |
| Sell at 3¢ | 225 | 2% | -$995.15 | -90% | 47 sec |
| Sell at 5¢ | 166 | 2% | -$975.00 | -88% | 56 sec |
| Sell at 10¢ | 112 | 1% | -$922.18 | -83% | 66 sec |
| Sell at 25¢ | 62 | 1% | -$835.68 | -75% | 82 sec |
| Sell at 50¢ | 39 | 0% | -$735.65 | -66% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 236 | 3 | 10% | 3% | +20% | -82% | -89% |
| 2–5 min | 2973 | 21 | 7% | 3% | -31% | -87% | -87% |
| 1–2 min | 2433 | 11 | 3% | 2% | -51% | -93% | -93% |
| Under 1 min | 3586 | 5 | 1% | 0% | -79% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 706 | 5 | 5% | 3% | -15% | -89% | -89% |
| ETH | 697 | 7 | 6% | 3% | +26% | -87% | -86% |
| HYPE | 697 | 3 | 5% | 3% | -47% | -89% | -86% |
| DOGE | 696 | 2 | 4% | 1% | -63% | -91% | -91% |
| BNB | 692 | 2 | 4% | 2% | -65% | -91% | -92% |
| XRP | 690 | 4 | 1% | 1% | -26% | -78% | -78% |
| SOL | 690 | 0 | 3% | 1% | -100% | -93% | -92% |
| NEAR | 688 | 4 | 6% | 3% | -24% | -66% | -67% |
| BTC | 688 | 3 | 5% | 2% | -43% | -87% | -90% |
| GOLD | 379 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 363 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 346 | 2 | 3% | 1% | -38% | -95% | -97% |
| COPPER | 322 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 289 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 282 | 2 | 3% | 2% | -34% | -94% | -93% |
| PALLADIUM | 277 | 1 | 2% | 1% | -66% | -97% | -98% |
| EURUSD | 263 | 1 | 4% | 3% | -65% | -93% | -91% |
| GBPUSD | 250 | 1 | 4% | 2% | -63% | -94% | -94% |
| USDJPY | 216 | 3 | 2% | 1% | +30% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4685 | 22 | 4% | 2% | -45% | -89% | -88% |
| DOWN (bought NO) | 4546 | 18 | 4% | 2% | -54% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1028 | 7 | 2% | 1% | +16% | -61% | -60% |
| 0.05–0.1% | 1072 | 4 | 3% | 1% | -45% | -91% | -92% |
| 0.1–0.2% | 1562 | 6 | 4% | 2% | -51% | -91% | -91% |
| 0.2–0.5% | 1829 | 9 | 6% | 3% | -46% | -88% | -87% |
| Over 0.5% | 751 | 4 | 7% | 3% | -45% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2291 | 10 | 4% | 2% | -49% | -86% | -87% |
| Morning (6am–12pm) | 2361 | 17 | 5% | 3% | -18% | -90% | -88% |
| Afternoon (12–6pm) | 1943 | 6 | 3% | 1% | -63% | -86% | -88% |
| Evening (6pm–12am) | 2636 | 7 | 3% | 1% | -69% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,112 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/6 1:14:48 AM | SOL | UP | 12 sec | -0.006% | 0¢ | ❌ Lost | $0.00 |
| 10/6 1:14:48 AM | NATGAS | UP | 12 sec | — | 0¢ | In play | — |
| 10/6 1:14:32 AM | GOLD | DOWN | 28 sec | — | 0¢ | In play | — |
| 10/6 1:14:16 AM | SILVER | DOWN | 44 sec | — | 1¢ | In play | — |
| 10/6 1:14:16 AM | BTC | DOWN | 44 sec | +0.046% | 0¢ | In play | — |
| 10/6 1:14:16 AM | ZEC | DOWN | 44 sec | +0.124% | 1¢ | In play | — |
| 10/6 1:14:16 AM | COPPER | DOWN | 44 sec | — | 0¢ | In play | — |
| 10/6 1:13:28 AM | ETH | UP | 1.5 min | -0.067% | 84¢ | ✅ Won | $13.85 |
| 10/6 1:13:28 AM | DOGE | UP | 1.5 min | -0.121% | 2¢ | In play | — |
| 10/6 1:13:12 AM | HYPE | UP | 1.8 min | -0.213% | 0¢ | In play | — |
| 10/6 1:12:56 AM | WTI | UP | 2.1 min | — | 1¢ | In play | — |
| 10/6 1:12:56 AM | XRP | UP | 2.1 min | -0.187% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 1:12:24 AM | BNB | UP | 2.6 min | -0.113% | 1¢ | In play | — |
| 10/6 1:11:35 AM | USDJPY | DOWN | 3.4 min | — | 1¢ | In play | — |
| 10/6 1:11:35 AM | NEAR | UP | 3.4 min | -0.541% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 12:59:45 AM | NEAR | UP | 14 sec | -0.102% | 0¢ | ❌ Lost | $0.00 |
| 10/6 12:59:13 AM | BNB | UP | 46 sec | -0.048% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 12:59:13 AM | ZEC | UP | 46 sec | -0.086% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 12:58:42 AM | SOL | DOWN | 78 sec | +0.076% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 12:58:42 AM | HYPE | DOWN | 78 sec | +0.070% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 12:58:42 AM | ETH | DOWN | 78 sec | +0.037% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 12:58:42 AM | EURUSD | DOWN | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 12:58:26 AM | XRP | DOWN | 1.6 min | +0.053% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 12:58:10 AM | PALLADIUM | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 12:57:55 AM | GBPUSD | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 12:44:32 AM | BNB | DOWN | 28 sec | +0.005% | 0¢ | ❌ Lost | $0.00 |
| 10/6 12:44:16 AM | SILVER | UP | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 12:44:00 AM | GOLD | UP | 60 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 12:43:44 AM | PLATINUM | UP | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 12:43:28 AM | BTC | DOWN | 1.5 min | +0.067% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
