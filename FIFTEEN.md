# 15-Minute 1¢ Study

*Updated Mon Oct 5, 7:48 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 622 finished bets | 1% | $31.10 | +46% | +5.00¢ | -$6.20 / $37.30 |

*Expect about **80 buys a day** (~$11.97/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 623 | $17.55 | +26% |
| Volatility model ≥ 2%, hold to the close | 1157 | $14.65 | +11% |
| Mean-reversion model ≥ 5%, hold to the close | 1375 | $9.20 | +5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 9039 | 9033 | 39 (0%) | 1.07% | -$540.90 (-50%) | Hold to the close: -$540.90 (-50%) |

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
| Volatility model | 5931 | 4.1% | 0.5% (27) | -577% | ❌ Worse |
| Momentum model | 5931 | 4.1% | 0.5% (27) | -602% | ❌ Worse |
| Mean-reversion model | 5931 | 6.7% | 0.5% (27) | -676% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5931 | 27 | -42% | -85% | -85% | -83% |
| Volatility model ≥ 2% | 1157 | 11 | +11% | -70% | -70% | -66% |
| Volatility model ≥ 5% | 622 | 7 | +46% | -57% | -56% | -53% |
| Volatility model ≥ 10% | 383 | 5 | +94% | -38% | -39% | -34% |
| Momentum model ≥ 2% | 1024 | 9 | +6% | -71% | -73% | -71% |
| Momentum model ≥ 5% | 623 | 6 | +26% | -62% | -65% | -62% |
| Momentum model ≥ 10% | 429 | 5 | +67% | -50% | -51% | -48% |
| Mean-reversion model ≥ 2% | 2045 | 15 | -20% | -83% | -83% | -78% |
| Mean-reversion model ≥ 5% | 1375 | 13 | +5% | -79% | -79% | -73% |
| Mean-reversion model ≥ 10% | 905 | 9 | +15% | -78% | -78% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6128 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 2202 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 703 | 3% | 3% | 2% | 2% | 1% | 0% |
| **All** | 9033 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 39 | 0% | -$540.90 | -50% | — |
| Sell at 2¢ | 342 | 4% | -$969.98 | -89% | 33 sec |
| Sell at 3¢ | 224 | 2% | -$971.54 | -89% | 47 sec |
| Sell at 5¢ | 165 | 2% | -$951.65 | -88% | 61 sec |
| Sell at 10¢ | 111 | 1% | -$899.49 | -83% | 66 sec |
| Sell at 25¢ | 61 | 1% | -$814.99 | -75% | 83 sec |
| Sell at 50¢ | 38 | 0% | -$718.40 | -66% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 226 | 3 | 11% | 3% | +26% | -81% | -88% |
| 2–5 min | 2926 | 21 | 7% | 3% | -30% | -87% | -87% |
| 1–2 min | 2381 | 10 | 3% | 2% | -54% | -93% | -93% |
| Under 1 min | 3497 | 5 | 1% | 0% | -79% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 693 | 5 | 5% | 3% | -14% | -89% | -89% |
| DOGE | 684 | 2 | 4% | 1% | -62% | -91% | -91% |
| HYPE | 684 | 3 | 5% | 3% | -46% | -88% | -86% |
| ETH | 683 | 6 | 6% | 3% | +10% | -87% | -86% |
| BNB | 680 | 2 | 4% | 2% | -65% | -90% | -92% |
| BTC | 677 | 3 | 5% | 2% | -42% | -87% | -90% |
| XRP | 677 | 4 | 1% | 1% | -25% | -78% | -78% |
| SOL | 676 | 0 | 3% | 1% | -100% | -93% | -92% |
| NEAR | 674 | 4 | 6% | 3% | -23% | -65% | -66% |
| GOLD | 370 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 355 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 336 | 2 | 3% | 1% | -36% | -95% | -96% |
| COPPER | 314 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 282 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 275 | 2 | 3% | 2% | -32% | -94% | -92% |
| PALLADIUM | 270 | 1 | 2% | 1% | -65% | -97% | -98% |
| EURUSD | 253 | 1 | 4% | 3% | -63% | -92% | -91% |
| GBPUSD | 241 | 1 | 4% | 2% | -61% | -94% | -94% |
| USDJPY | 209 | 3 | 2% | 1% | +34% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4571 | 21 | 4% | 2% | -46% | -89% | -88% |
| DOWN (bought NO) | 4462 | 18 | 4% | 2% | -53% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1011 | 7 | 2% | 1% | +18% | -60% | -60% |
| 0.05–0.1% | 1039 | 3 | 3% | 1% | -57% | -91% | -92% |
| 0.1–0.2% | 1536 | 6 | 4% | 2% | -50% | -91% | -91% |
| 0.2–0.5% | 1798 | 9 | 6% | 3% | -45% | -88% | -87% |
| Over 0.5% | 742 | 4 | 7% | 3% | -45% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2228 | 9 | 4% | 2% | -53% | -86% | -87% |
| Morning (6am–12pm) | 2361 | 17 | 5% | 3% | -18% | -90% | -88% |
| Afternoon (12–6pm) | 1943 | 6 | 3% | 1% | -63% | -86% | -88% |
| Evening (6pm–12am) | 2501 | 7 | 3% | 1% | -68% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,130 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/5 7:44:49 PM | NATGAS | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:44:33 PM | WTI | UP | 27 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:44:17 PM | HYPE | UP | 43 sec | -0.157% | 0¢ | ❌ Lost | $0.00 |
| 10/5 7:44:17 PM | SILVER | UP | 43 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:44:00 PM | PLATINUM | UP | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:44:00 PM | GOLD | UP | 59 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/5 7:43:27 PM | COPPER | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:42:38 PM | NEAR | UP | 2.4 min | -0.487% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:42:22 PM | BNB | UP | 2.6 min | -0.189% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:41:35 PM | ZEC | UP | 3.4 min | -0.450% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:41:35 PM | DOGE | UP | 3.4 min | -0.294% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:41:19 PM | XRP | UP | 3.7 min | -0.332% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:41:19 PM | EURUSD | UP | 3.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:41:03 PM | SOL | UP | 4.0 min | -0.304% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:40:48 PM | BTC | UP | 4.2 min | -0.291% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:40:32 PM | ETH | UP | 4.5 min | -0.249% | 0¢ | ❌ Lost | $0.00 |
| 10/5 7:29:17 PM | SOL | UP | 42 sec | -0.059% | 0¢ | ❌ Lost | $0.00 |
| 10/5 7:29:01 PM | NATGAS | DOWN | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:29:01 PM | NEAR | UP | 59 sec | -0.474% | 0¢ | ❌ Lost | $0.00 |
| 10/5 7:28:13 PM | EURUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:27:41 PM | BTC | UP | 2.3 min | -0.155% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:27:25 PM | ZEC | UP | 2.6 min | -0.385% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:27:25 PM | ETH | UP | 2.6 min | -0.141% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:26:37 PM | XRP | UP | 3.4 min | -0.298% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:26:21 PM | COPPER | UP | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:26:21 PM | DOGE | UP | 3.6 min | -0.328% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:26:21 PM | PALLADIUM | UP | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:25:31 PM | BNB | UP | 4.5 min | -0.271% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:25:15 PM | HYPE | UP | 4.8 min | -0.439% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:24:44 PM | GOLD | UP | 5.2 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
