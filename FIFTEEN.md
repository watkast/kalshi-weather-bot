# 15-Minute 1¢ Study

*Updated Thu Oct 8, 11:34 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 836 finished bets | 1% | $35.25 | +39% | +4.22¢ | -$16.70 / $51.95 |

*Expect about **76 buys a day** (~$11.45/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 819 | $23.95 | +27% |
| 5+ min left, hold to the close | 358 | $3.20 | +6% |
| Volatility model ≥ 5%, sell at 50¢ | 836 | -$2.00 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 12560 | 12553 | 51 (0%) | 1.07% | -$811.80 (-53%) | Hold to the close: -$811.80 (-53%) |

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
| Volatility model | 8013 | 4.0% | 0.4% (35) | -567% | ❌ Worse |
| Momentum model | 8013 | 4.0% | 0.4% (35) | -599% | ❌ Worse |
| Mean-reversion model | 8013 | 6.7% | 0.4% (35) | -664% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 8013 | 35 | -45% | -87% | -88% | -85% |
| Volatility model ≥ 2% | 1532 | 13 | -2% | -74% | -75% | -71% |
| Volatility model ≥ 5% | 836 | 9 | +39% | -66% | -64% | -61% |
| Volatility model ≥ 10% | 512 | 7 | +101% | -49% | -50% | -45% |
| Momentum model ≥ 2% | 1359 | 11 | -3% | -76% | -77% | -74% |
| Momentum model ≥ 5% | 819 | 8 | +27% | -69% | -70% | -67% |
| Momentum model ≥ 10% | 557 | 6 | +55% | -59% | -60% | -56% |
| Mean-reversion model ≥ 2% | 2782 | 20 | -22% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1878 | 16 | -6% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1238 | 12 | +11% | -81% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 8210 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3211 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1132 | 2% | 2% | 2% | 1% | 1% | 0% |
| **All** | 12553 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 51 | 0% | -$811.80 | -53% | — |
| Sell at 2¢ | 428 | 3% | -$1,372.52 | -90% | 33 sec |
| Sell at 3¢ | 282 | 2% | -$1,373.82 | -90% | 47 sec |
| Sell at 5¢ | 207 | 2% | -$1,349.25 | -88% | 51 sec |
| Sell at 10¢ | 136 | 1% | -$1,291.64 | -85% | 64 sec |
| Sell at 25¢ | 78 | 1% | -$1,183.62 | -78% | 82 sec |
| Sell at 50¢ | 51 | 0% | -$1,055.55 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 354 | 4 | 11% | 3% | +7% | -81% | -85% |
| 2–5 min | 4085 | 26 | 6% | 3% | -38% | -88% | -89% |
| 1–2 min | 3293 | 13 | 3% | 2% | -57% | -94% | -94% |
| Under 1 min | 4817 | 8 | 1% | 0% | -76% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 919 | 6 | 4% | 3% | -21% | -90% | -90% |
| HYPE | 918 | 3 | 5% | 3% | -60% | -89% | -88% |
| DOGE | 915 | 2 | 3% | 2% | -72% | -92% | -91% |
| BNB | 915 | 4 | 4% | 2% | -47% | -91% | -92% |
| ETH | 913 | 7 | 5% | 3% | -6% | -89% | -88% |
| NEAR | 909 | 5 | 6% | 2% | -28% | -72% | -74% |
| SOL | 908 | 0 | 3% | 1% | -100% | -94% | -93% |
| BTC | 907 | 4 | 5% | 2% | -42% | -87% | -90% |
| XRP | 906 | 6 | 2% | 1% | -17% | -82% | -82% |
| GOLD | 538 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 522 | 0 | 3% | 1% | -100% | -94% | -94% |
| WTI | 496 | 3 | 3% | 1% | -32% | -95% | -96% |
| COPPER | 459 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 416 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 395 | 3 | 3% | 2% | -29% | -95% | -93% |
| EURUSD | 390 | 3 | 3% | 2% | -28% | -71% | -69% |
| PALLADIUM | 385 | 1 | 1% | 1% | -76% | -98% | -99% |
| GBPUSD | 368 | 1 | 3% | 2% | -75% | -95% | -95% |
| USDJPY | 329 | 3 | 1% | 1% | -15% | -98% | -97% |
| AUDUSD | 23 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 22 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6336 | 27 | 3% | 2% | -51% | -89% | -88% |
| DOWN (bought NO) | 6217 | 24 | 3% | 1% | -56% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1318 | 8 | 2% | 1% | +5% | -68% | -67% |
| 0.05–0.1% | 1377 | 4 | 3% | 1% | -57% | -92% | -92% |
| 0.1–0.2% | 2098 | 7 | 4% | 2% | -58% | -92% | -92% |
| 0.2–0.5% | 2405 | 13 | 5% | 3% | -41% | -89% | -88% |
| Over 0.5% | 1010 | 5 | 6% | 2% | -49% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3090 | 17 | 4% | 2% | -37% | -85% | -85% |
| Morning (6am–12pm) | 3025 | 17 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 2853 | 8 | 3% | 1% | -67% | -89% | -90% |
| Evening (6pm–12am) | 3585 | 9 | 3% | 1% | -71% | -95% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,101 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/8 11:29:33 PM | WTI | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:29:33 PM | ZEC | DOWN | 27 sec | +0.096% | 0¢ | ❌ Lost | $0.00 |
| 10/8 11:29:17 PM | PLATINUM | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:29:17 PM | EURUSD | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:29:01 PM | COPPER | DOWN | 59 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 11:28:15 PM | GOLD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/8 11:27:43 PM | SILVER | DOWN | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 11:27:28 PM | ETH | DOWN | 2.5 min | +0.191% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:27:28 PM | HYPE | DOWN | 2.5 min | +0.193% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:26:56 PM | SOL | DOWN | 3.0 min | +0.193% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 11:26:56 PM | BTC | DOWN | 3.0 min | +0.138% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 11:26:40 PM | XRP | DOWN | 3.3 min | +0.230% | 2¢ | ❌ Lost | -$0.15 |
| 10/8 11:26:25 PM | DOGE | DOWN | 3.6 min | +0.307% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 11:26:09 PM | BNB | DOWN | 3.9 min | +0.171% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 11:25:20 PM | NEAR | DOWN | 4.7 min | +1.003% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 11:14:36 PM | PALLADIUM | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:14:20 PM | COPPER | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:14:04 PM | ZEC | DOWN | 56 sec | +0.137% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:13:48 PM | WTI | DOWN | 72 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 11:13:48 PM | PLATINUM | DOWN | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:13:15 PM | GOLD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:12:13 PM | XRP | DOWN | 2.8 min | +0.201% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 11:11:41 PM | BTC | DOWN | 3.3 min | +0.136% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 11:11:41 PM | ETH | DOWN | 3.3 min | +0.168% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 11:11:26 PM | SOL | DOWN | 3.6 min | +0.412% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 11:11:26 PM | DOGE | DOWN | 3.6 min | +0.237% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:11:10 PM | BNB | DOWN | 3.8 min | +0.104% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 11:11:10 PM | HYPE | DOWN | 3.8 min | +0.335% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:10:05 PM | NEAR | DOWN | 4.9 min | +0.799% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 10:59:49 PM | NEAR | UP | 10 sec | -0.114% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
