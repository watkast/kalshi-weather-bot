# 15-Minute 1¢ Study

*Updated Tue Oct 6, 11:30 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 713 finished bets | 1% | $35.50 | +46% | +4.98¢ | -$10.55 / $46.05 |

*Expect about **80 buys a day** (~$11.95/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 711 | $22.70 | +30% |
| 5+ min left, hold to the close | 262 | $17.15 | +44% |
| Mean-reversion model ≥ 5%, hold to the close | 1558 | $14.25 | +7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 10317 | 10304 | 46 (0%) | 1.07% | -$600.40 (-48%) | Hold to the close: -$600.40 (-48%) |

*In play or awaiting result: 13. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 6697 | 4.2% | 0.5% (33) | -565% | ❌ Worse |
| Momentum model | 6697 | 4.2% | 0.5% (33) | -594% | ❌ Worse |
| Mean-reversion model | 6697 | 6.8% | 0.5% (33) | -652% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6697 | 33 | -38% | -86% | -86% | -84% |
| Volatility model ≥ 2% | 1307 | 12 | +7% | -73% | -73% | -68% |
| Volatility model ≥ 5% | 713 | 8 | +46% | -62% | -61% | -57% |
| Volatility model ≥ 10% | 447 | 6 | +99% | -45% | -46% | -41% |
| Momentum model ≥ 2% | 1164 | 10 | +4% | -73% | -75% | -73% |
| Momentum model ≥ 5% | 711 | 7 | +30% | -66% | -68% | -65% |
| Momentum model ≥ 10% | 494 | 6 | +76% | -55% | -56% | -53% |
| Mean-reversion model ≥ 2% | 2293 | 19 | -10% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1558 | 15 | +7% | -81% | -81% | -74% |
| Mean-reversion model ≥ 10% | 1033 | 11 | +23% | -79% | -79% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6894 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2577 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 833 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 10304 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 46 | 0% | -$600.40 | -48% | — |
| Sell at 2¢ | 366 | 4% | -$1,121.24 | -90% | 34 sec |
| Sell at 3¢ | 242 | 2% | -$1,122.02 | -90% | 47 sec |
| Sell at 5¢ | 181 | 2% | -$1,098.75 | -88% | 50 sec |
| Sell at 10¢ | 122 | 1% | -$1,042.58 | -84% | 64 sec |
| Sell at 25¢ | 70 | 1% | -$942.70 | -76% | 82 sec |
| Sell at 50¢ | 46 | 0% | -$821.90 | -66% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 259 | 4 | 10% | 3% | +46% | -82% | -88% |
| 2–5 min | 3306 | 24 | 7% | 3% | -29% | -88% | -88% |
| 1–2 min | 2702 | 11 | 3% | 2% | -56% | -94% | -94% |
| Under 1 min | 4034 | 7 | 1% | 0% | -74% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 779 | 6 | 5% | 3% | -8% | -90% | -89% |
| HYPE | 771 | 3 | 5% | 3% | -52% | -88% | -87% |
| DOGE | 769 | 2 | 3% | 1% | -67% | -92% | -92% |
| ETH | 767 | 7 | 5% | 3% | +15% | -88% | -87% |
| BNB | 765 | 3 | 4% | 2% | -53% | -91% | -93% |
| NEAR | 763 | 5 | 6% | 3% | -14% | -68% | -69% |
| SOL | 761 | 0 | 3% | 1% | -100% | -93% | -92% |
| XRP | 760 | 5 | 2% | 1% | -17% | -80% | -80% |
| BTC | 759 | 4 | 5% | 3% | -31% | -87% | -89% |
| GOLD | 430 | 0 | 3% | 1% | -100% | -92% | -95% |
| SILVER | 420 | 0 | 2% | 1% | -100% | -95% | -95% |
| WTI | 398 | 2 | 3% | 1% | -45% | -95% | -97% |
| COPPER | 369 | 0 | 1% | 1% | -100% | -99% | -99% |
| PLATINUM | 330 | 0 | 0% | 0% | -100% | -99% | -99% |
| PALLADIUM | 316 | 1 | 2% | 1% | -70% | -97% | -98% |
| NATGAS | 314 | 3 | 3% | 2% | -11% | -94% | -93% |
| EURUSD | 302 | 1 | 4% | 2% | -69% | -94% | -92% |
| GBPUSD | 286 | 1 | 3% | 2% | -67% | -95% | -95% |
| USDJPY | 245 | 3 | 2% | 1% | +14% | -97% | -96% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5216 | 24 | 4% | 2% | -46% | -90% | -89% |
| DOWN (bought NO) | 5088 | 22 | 3% | 2% | -50% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1146 | 8 | 2% | 1% | +19% | -65% | -64% |
| 0.05–0.1% | 1197 | 4 | 3% | 1% | -51% | -92% | -92% |
| 0.1–0.2% | 1740 | 6 | 4% | 2% | -56% | -91% | -92% |
| 0.2–0.5% | 2007 | 12 | 6% | 3% | -34% | -88% | -87% |
| Over 0.5% | 802 | 5 | 6% | 3% | -36% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2570 | 15 | 4% | 2% | -32% | -87% | -88% |
| Morning (6am–12pm) | 2536 | 17 | 5% | 3% | -24% | -90% | -89% |
| Afternoon (12–6pm) | 2244 | 7 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 2954 | 7 | 3% | 1% | -73% | -95% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,058 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/6 11:29:57 PM | WTI | DOWN | 2 sec | — | 0¢ | In play | — |
| 10/6 11:29:57 PM | GOLD | UP | 2 sec | — | 1¢ | In play | — |
| 10/6 11:29:42 PM | NATGAS | UP | 18 sec | — | 0¢ | In play | — |
| 10/6 11:28:54 PM | BTC | DOWN | 66 sec | +0.049% | 1¢ | In play | — |
| 10/6 11:28:21 PM | ETH | DOWN | 1.6 min | +0.070% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 11:28:06 PM | XRP | DOWN | 1.9 min | +0.157% | 0¢ | In play | — |
| 10/6 11:27:50 PM | NEAR | DOWN | 2.2 min | +0.409% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 11:27:33 PM | DOGE | DOWN | 2.5 min | +0.223% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 11:27:01 PM | SOL | DOWN | 3.0 min | +0.212% | 1¢ | In play | — |
| 10/6 11:27:01 PM | BNB | DOWN | 3.0 min | +0.094% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 11:25:43 PM | HYPE | DOWN | 4.3 min | +0.319% | 1¢ | In play | — |
| 10/6 11:14:56 PM | PALLADIUM | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 11:14:56 PM | SILVER | UP | 4 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/6 11:14:40 PM | NATGAS | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 11:14:40 PM | WTI | DOWN | 19 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 11:14:24 PM | PLATINUM | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 11:13:52 PM | BTC | DOWN | 67 sec | +0.084% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 11:13:37 PM | COPPER | DOWN | 83 sec | — | 6¢ | ❌ Lost | -$0.15 |
| 10/6 11:13:21 PM | NEAR | DOWN | 1.6 min | +0.429% | 0¢ | ❌ Lost | $0.00 |
| 10/6 11:12:01 PM | ZEC | DOWN | 3.0 min | +0.526% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 11:11:29 PM | XRP | DOWN | 3.5 min | +0.397% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 11:11:29 PM | BNB | DOWN | 3.5 min | +0.166% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 11:11:13 PM | DOGE | DOWN | 3.8 min | +0.323% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 11:11:13 PM | ETH | DOWN | 3.8 min | +0.156% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 11:10:57 PM | SOL | DOWN | 4.0 min | +0.300% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 11:10:26 PM | HYPE | DOWN | 4.6 min | +0.333% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 10:59:48 PM | ZEC | DOWN | 11 sec | +0.027% | 0¢ | ❌ Lost | $0.00 |
| 10/6 10:59:48 PM | SILVER | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 10:59:48 PM | GOLD | UP | 11 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/6 10:59:32 PM | PALLADIUM | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
