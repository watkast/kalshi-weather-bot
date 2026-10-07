# 15-Minute 1¢ Study

*Updated Wed Oct 7, 1:57 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 740 finished bets | 1% | $32.65 | +41% | +4.41¢ | -$11.75 / $44.40 |

*Expect about **77 buys a day** (~$11.62/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 738 | $19.70 | +25% |
| 5+ min left, hold to the close | 285 | $13.70 | +32% |
| Volatility model ≥ 2%, hold to the close | 1358 | $4.95 | +3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 10931 | 10922 | 49 (0%) | 1.07% | -$636.25 (-48%) | Hold to the close: -$636.25 (-48%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 7065 | 4.1% | 0.5% (33) | -560% | ❌ Worse |
| Momentum model | 7065 | 4.1% | 0.5% (33) | -589% | ❌ Worse |
| Mean-reversion model | 7065 | 6.8% | 0.5% (33) | -653% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7065 | 33 | -41% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 1358 | 12 | +3% | -73% | -73% | -69% |
| Volatility model ≥ 5% | 740 | 8 | +41% | -62% | -60% | -57% |
| Volatility model ≥ 10% | 461 | 6 | +93% | -45% | -45% | -39% |
| Momentum model ≥ 2% | 1206 | 10 | +0% | -74% | -75% | -72% |
| Momentum model ≥ 5% | 738 | 7 | +25% | -66% | -68% | -65% |
| Momentum model ≥ 10% | 509 | 6 | +71% | -55% | -56% | -52% |
| Mean-reversion model ≥ 2% | 2418 | 19 | -15% | -84% | -84% | -80% |
| Mean-reversion model ≥ 5% | 1641 | 15 | +1% | -81% | -81% | -75% |
| Mean-reversion model ≥ 10% | 1090 | 11 | +16% | -79% | -79% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7262 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2755 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 905 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 10922 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 49 | 0% | -$636.25 | -48% | — |
| Sell at 2¢ | 385 | 4% | -$1,180.15 | -89% | 34 sec |
| Sell at 3¢ | 258 | 2% | -$1,179.63 | -89% | 47 sec |
| Sell at 5¢ | 192 | 2% | -$1,155.45 | -87% | 56 sec |
| Sell at 10¢ | 129 | 1% | -$1,097.26 | -83% | 64 sec |
| Sell at 25¢ | 74 | 1% | -$993.31 | -75% | 82 sec |
| Sell at 50¢ | 49 | 0% | -$865.50 | -65% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 282 | 4 | 11% | 4% | +34% | -81% | -86% |
| 2–5 min | 3518 | 25 | 7% | 3% | -31% | -88% | -88% |
| 1–2 min | 2892 | 12 | 3% | 2% | -55% | -94% | -93% |
| Under 1 min | 4227 | 8 | 1% | 0% | -72% | -88% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 815 | 6 | 5% | 3% | -12% | -90% | -89% |
| HYPE | 814 | 3 | 5% | 3% | -55% | -89% | -87% |
| DOGE | 809 | 2 | 3% | 1% | -69% | -92% | -92% |
| ETH | 808 | 7 | 5% | 3% | +8% | -88% | -88% |
| BNB | 807 | 3 | 4% | 2% | -55% | -91% | -92% |
| NEAR | 804 | 5 | 6% | 3% | -18% | -69% | -70% |
| SOL | 803 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 802 | 4 | 5% | 2% | -34% | -88% | -90% |
| XRP | 800 | 5 | 2% | 1% | -22% | -81% | -80% |
| GOLD | 459 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 449 | 0 | 2% | 1% | -100% | -95% | -94% |
| WTI | 425 | 3 | 3% | 1% | -22% | -95% | -96% |
| COPPER | 393 | 0 | 1% | 1% | -100% | -99% | -99% |
| PLATINUM | 352 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 342 | 3 | 3% | 2% | -18% | -94% | -92% |
| PALLADIUM | 335 | 1 | 1% | 1% | -72% | -97% | -98% |
| EURUSD | 329 | 3 | 4% | 2% | -15% | -65% | -64% |
| GBPUSD | 309 | 1 | 3% | 2% | -70% | -95% | -95% |
| USDJPY | 267 | 3 | 1% | 1% | +5% | -97% | -96% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5559 | 26 | 4% | 2% | -46% | -88% | -87% |
| DOWN (bought NO) | 5363 | 23 | 3% | 2% | -51% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1197 | 8 | 2% | 1% | +16% | -65% | -64% |
| 0.05–0.1% | 1247 | 4 | 3% | 1% | -53% | -92% | -92% |
| 0.1–0.2% | 1845 | 6 | 3% | 2% | -59% | -92% | -92% |
| 0.2–0.5% | 2123 | 12 | 6% | 3% | -38% | -88% | -87% |
| Over 0.5% | 848 | 5 | 6% | 3% | -39% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2890 | 17 | 4% | 2% | -32% | -84% | -84% |
| Morning (6am–12pm) | 2706 | 17 | 4% | 2% | -28% | -91% | -90% |
| Afternoon (12–6pm) | 2336 | 7 | 3% | 1% | -64% | -88% | -88% |
| Evening (6pm–12am) | 2990 | 8 | 3% | 1% | -69% | -95% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,042 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/7 1:56:44 PM | XRP | UP | 3.2 min | -0.330% | — | In play | — |
| 10/7 1:56:13 PM | ZEC | UP | 3.8 min | -0.631% | — | In play | — |
| 10/7 1:54:38 PM | HYPE | UP | 5.4 min | -0.644% | — | In play | — |
| 10/7 1:44:54 PM | WTI | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 1:44:54 PM | COPPER | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 1:44:54 PM | BTC | UP | 5 sec | -0.018% | 0¢ | ❌ Lost | $0.00 |
| 10/7 1:44:39 PM | BNB | UP | 20 sec | -0.031% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 1:44:23 PM | PLATINUM | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 1:44:23 PM | SILVER | UP | 36 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/7 1:44:23 PM | GOLD | UP | 36 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/7 1:43:51 PM | ETH | DOWN | 69 sec | +0.113% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 1:43:51 PM | NEAR | DOWN | 69 sec | +0.581% | 0¢ | ❌ Lost | $0.00 |
| 10/7 1:43:36 PM | USDJPY | DOWN | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 1:43:36 PM | SOL | UP | 83 sec | -0.133% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 1:43:36 PM | NATGAS | DOWN | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 1:43:36 PM | XRP | UP | 83 sec | -0.098% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 1:43:36 PM | GBPUSD | UP | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 1:43:20 PM | DOGE | UP | 1.6 min | -0.130% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 1:43:20 PM | EURUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 1:42:16 PM | HYPE | UP | 2.7 min | -0.238% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 1:42:16 PM | ZEC | UP | 2.7 min | -0.481% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 1:29:51 PM | COPPER | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 1:29:51 PM | XRP | UP | 8 sec | -0.021% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 1:29:19 PM | SOL | DOWN | 41 sec | +0.059% | 0¢ | ❌ Lost | $0.00 |
| 10/7 1:27:45 PM | NEAR | DOWN | 2.2 min | +0.632% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 1:26:40 PM | BTC | DOWN | 3.3 min | +0.134% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 1:26:09 PM | ZEC | DOWN | 3.9 min | +0.615% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 1:25:08 PM | DOGE | DOWN | 4.9 min | +0.251% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 1:25:08 PM | ETH | DOWN | 4.9 min | +0.198% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 1:25:08 PM | HYPE | DOWN | 4.9 min | +0.317% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
