# 15-Minute 1¢ Study

*Updated Fri Oct 16, 10:18 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1703 finished bets | 1% | $76.70 | +41% | +4.50¢ | $33.75 / $42.95 |

*Expect about **90 buys a day** (~$13.52/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1567 | $40.05 | +24% |
| Momentum model ≥ 2%, hold to the close | 2652 | -$13.65 | -4% |
| Volatility model ≥ 5%, sell at 50¢ | 1703 | -$25.80 | -14% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 21535 | 21528 | 80 (0%) | 1.07% | -$1,499.60 (-57%) | Hold to the close: -$1,499.60 (-57%) |

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
| Volatility model | 13804 | 4.5% | 0.4% (54) | -656% | ❌ Worse |
| Momentum model | 13804 | 4.4% | 0.4% (54) | -679% | ❌ Worse |
| Mean-reversion model | 13804 | 7.4% | 0.4% (54) | -790% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13804 | 54 | -51% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 3105 | 24 | -11% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 1703 | 19 | +41% | -74% | -73% | -69% |
| Volatility model ≥ 10% | 989 | 11 | +58% | -66% | -65% | -62% |
| Momentum model ≥ 2% | 2652 | 21 | -4% | -80% | -81% | -77% |
| Momentum model ≥ 5% | 1567 | 15 | +24% | -78% | -77% | -73% |
| Momentum model ≥ 10% | 1043 | 10 | +35% | -73% | -72% | -67% |
| Mean-reversion model ≥ 2% | 5250 | 34 | -29% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3625 | 27 | -18% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2382 | 16 | -23% | -80% | -80% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 14002 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5309 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 21528 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 80 | 0% | -$1,499.60 | -57% | — |
| Sell at 2¢ | 770 | 4% | -$2,321.40 | -89% | 39 sec |
| Sell at 3¢ | 516 | 2% | -$2,320.36 | -89% | 47 sec |
| Sell at 5¢ | 371 | 2% | -$2,280.45 | -87% | 50 sec |
| Sell at 10¢ | 223 | 1% | -$2,201.47 | -84% | 63 sec |
| Sell at 25¢ | 126 | 1% | -$2,034.54 | -78% | 80 sec |
| Sell at 50¢ | 83 | 0% | -$1,821.35 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 738 | 5 | 10% | 3% | -36% | -82% | -85% |
| 2–5 min | 6972 | 37 | 7% | 3% | -48% | -88% | -88% |
| 1–2 min | 5586 | 20 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 8228 | 18 | 1% | 0% | -69% | -88% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1573 | 11 | 5% | 3% | -13% | -89% | -90% |
| HYPE | 1568 | 5 | 4% | 2% | -61% | -90% | -88% |
| ETH | 1560 | 8 | 6% | 3% | -38% | -87% | -87% |
| BNB | 1558 | 6 | 5% | 2% | -53% | -89% | -89% |
| DOGE | 1557 | 2 | 4% | 2% | -84% | -91% | -90% |
| SOL | 1555 | 2 | 3% | 2% | -84% | -92% | -92% |
| XRP | 1547 | 7 | 3% | 1% | -44% | -86% | -87% |
| NEAR | 1543 | 8 | 6% | 3% | -32% | -78% | -78% |
| BTC | 1541 | 7 | 5% | 2% | -39% | -88% | -91% |
| GOLD | 864 | 1 | 3% | 1% | -86% | -92% | -94% |
| SILVER | 841 | 4 | 3% | 1% | -45% | -80% | -80% |
| WTI | 821 | 3 | 3% | 1% | -57% | -94% | -95% |
| COPPER | 735 | 2 | 2% | 1% | -75% | -84% | -84% |
| PLATINUM | 722 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 667 | 5 | 2% | 2% | -30% | -82% | -81% |
| PALLADIUM | 659 | 2 | 1% | 0% | -72% | -84% | -84% |
| EURUSD | 659 | 3 | 3% | 1% | -58% | -81% | -81% |
| GBPUSD | 615 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 574 | 3 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 200 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 169 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10860 | 40 | 4% | 2% | -58% | -89% | -89% |
| DOWN (bought NO) | 10668 | 40 | 4% | 2% | -57% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2324 | 11 | 2% | 1% | -20% | -80% | -79% |
| 0.05–0.1% | 2398 | 7 | 3% | 1% | -58% | -92% | -92% |
| 0.1–0.2% | 3534 | 11 | 4% | 2% | -61% | -90% | -90% |
| 0.2–0.5% | 4112 | 21 | 6% | 3% | -44% | -88% | -88% |
| Over 0.5% | 1631 | 6 | 6% | 3% | -62% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5359 | 20 | 4% | 2% | -58% | -87% | -88% |
| Morning (6am–12pm) | 5104 | 27 | 4% | 2% | -39% | -87% | -86% |
| Afternoon (12–6pm) | 5104 | 16 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 5961 | 17 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,466 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/16 10:14:37 PM | ETH | UP | 23 sec | -0.024% | 0¢ | ❌ Lost | $0.00 |
| 10/16 10:14:21 PM | XRP | UP | 39 sec | -0.061% | 0¢ | ❌ Lost | $0.00 |
| 10/16 10:14:21 PM | BTC | UP | 39 sec | -0.028% | 0¢ | ❌ Lost | $0.00 |
| 10/16 10:14:05 PM | ZEC | UP | 55 sec | -0.149% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:13:34 PM | BNB | DOWN | 86 sec | +0.024% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 10:12:14 PM | NEAR | DOWN | 2.8 min | +0.586% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:11:11 PM | SOL | UP | 3.8 min | -0.205% | 2¢ | ❌ Lost | -$0.15 |
| 10/16 10:10:24 PM | HYPE | UP | 4.6 min | -0.307% | 0¢ | ❌ Lost | $0.00 |
| 10/16 9:59:28 PM | BNB | UP | 31 sec | -0.036% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 9:59:28 PM | HYPE | UP | 31 sec | -0.026% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 9:59:12 PM | BTC | UP | 47 sec | -0.039% | 0¢ | ❌ Lost | $0.00 |
| 10/16 9:58:41 PM | ETH | UP | 79 sec | -0.035% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 9:58:41 PM | ZEC | UP | 79 sec | -0.239% | 0¢ | ❌ Lost | $0.00 |
| 10/16 9:58:25 PM | DOGE | UP | 1.6 min | -0.118% | 0¢ | ❌ Lost | $0.00 |
| 10/16 9:57:12 PM | SOL | UP | 2.8 min | -0.165% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 9:54:04 PM | XRP | UP | 5.9 min | -0.168% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 9:53:17 PM | NEAR | UP | 6.7 min | -1.005% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 9:44:53 PM | WTI | DOWN | 6 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/16 9:44:38 PM | BTC | DOWN | 21 sec | +0.012% | 0¢ | ❌ Lost | $0.00 |
| 10/16 9:44:22 PM | HYPE | DOWN | 37 sec | +0.035% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 9:44:06 PM | NATGAS | UP | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 9:43:35 PM | ETH | DOWN | 85 sec | +0.070% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 9:42:14 PM | BNB | DOWN | 2.8 min | +0.040% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 9:42:14 PM | SOL | DOWN | 2.8 min | +0.182% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 9:41:43 PM | NEAR | DOWN | 3.3 min | +0.553% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 9:41:12 PM | ZEC | DOWN | 3.8 min | +0.480% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 9:40:56 PM | XRP | DOWN | 4.0 min | +0.145% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 9:39:53 PM | DOGE | DOWN | 5.1 min | +0.254% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 9:29:54 PM | WTI | UP | 5 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 9:27:17 PM | BNB | DOWN | 2.7 min | +0.047% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
