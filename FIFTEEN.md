# 15-Minute 1¢ Study

*Updated Fri Oct 16, 11:43 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1635 finished bets | 1% | $84.65 | +47% | +5.18¢ | $37.50 / $47.15 |

*Expect about **89 buys a day** (~$13.29/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1513 | $46.35 | +28% |
| Momentum model ≥ 2%, hold to the close | 2561 | -$2.40 | -1% |
| Volatility model ≥ 5%, sell at 50¢ | 1635 | -$17.85 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 21070 | 21049 | 80 (0%) | 1.07% | -$1,445.60 (-56%) | Hold to the close: -$1,445.60 (-56%) |

*In play or awaiting result: 20. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 13429 | 4.4% | 0.4% (54) | -638% | ❌ Worse |
| Momentum model | 13429 | 4.4% | 0.4% (54) | -661% | ❌ Worse |
| Mean-reversion model | 13429 | 7.4% | 0.4% (54) | -769% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13429 | 54 | -50% | -88% | -88% | -85% |
| Volatility model ≥ 2% | 2985 | 24 | -7% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1635 | 19 | +47% | -74% | -72% | -68% |
| Volatility model ≥ 10% | 953 | 11 | +65% | -65% | -64% | -61% |
| Momentum model ≥ 2% | 2561 | 21 | -1% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1513 | 15 | +28% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1008 | 10 | +40% | -71% | -71% | -66% |
| Mean-reversion model ≥ 2% | 5068 | 34 | -27% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3489 | 27 | -15% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2289 | 16 | -20% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13627 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5237 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2185 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 21049 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 80 | 0% | -$1,445.60 | -56% | — |
| Sell at 2¢ | 749 | 4% | -$2,272.86 | -89% | 42 sec |
| Sell at 3¢ | 505 | 2% | -$2,270.65 | -89% | 47 sec |
| Sell at 5¢ | 365 | 2% | -$2,230.35 | -87% | 50 sec |
| Sell at 10¢ | 220 | 1% | -$2,151.40 | -84% | 63 sec |
| Sell at 25¢ | 126 | 1% | -$1,980.54 | -77% | 80 sec |
| Sell at 50¢ | 83 | 0% | -$1,767.35 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 704 | 5 | 10% | 3% | -32% | -82% | -85% |
| 2–5 min | 6842 | 37 | 7% | 3% | -47% | -88% | -88% |
| 1–2 min | 5469 | 20 | 3% | 2% | -60% | -92% | -92% |
| Under 1 min | 8030 | 18 | 1% | 0% | -68% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1530 | 11 | 5% | 3% | -11% | -89% | -89% |
| HYPE | 1525 | 5 | 4% | 2% | -60% | -90% | -89% |
| ETH | 1520 | 8 | 5% | 3% | -36% | -88% | -87% |
| DOGE | 1516 | 2 | 4% | 2% | -83% | -90% | -90% |
| BNB | 1516 | 6 | 5% | 2% | -51% | -89% | -89% |
| SOL | 1513 | 2 | 3% | 2% | -84% | -92% | -91% |
| XRP | 1504 | 7 | 2% | 1% | -42% | -86% | -87% |
| BTC | 1503 | 7 | 5% | 2% | -38% | -88% | -91% |
| NEAR | 1500 | 8 | 6% | 3% | -30% | -78% | -78% |
| GOLD | 855 | 1 | 4% | 1% | -86% | -92% | -94% |
| SILVER | 830 | 4 | 3% | 1% | -45% | -79% | -80% |
| WTI | 799 | 3 | 3% | 1% | -56% | -94% | -95% |
| COPPER | 730 | 2 | 2% | 1% | -74% | -84% | -84% |
| PLATINUM | 713 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 656 | 5 | 2% | 2% | -29% | -82% | -81% |
| PALLADIUM | 654 | 2 | 1% | 0% | -71% | -84% | -84% |
| EURUSD | 649 | 3 | 3% | 1% | -57% | -81% | -81% |
| GBPUSD | 609 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 570 | 3 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 193 | 0 | 1% | 0% | -100% | -99% | -99% |
| USDCAD | 164 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10630 | 40 | 4% | 2% | -57% | -89% | -89% |
| DOWN (bought NO) | 10419 | 40 | 4% | 2% | -56% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2241 | 11 | 2% | 1% | -17% | -79% | -79% |
| 0.05–0.1% | 2338 | 7 | 3% | 1% | -56% | -92% | -92% |
| 0.1–0.2% | 3445 | 11 | 4% | 2% | -60% | -90% | -90% |
| 0.2–0.5% | 4012 | 21 | 6% | 3% | -42% | -88% | -88% |
| Over 0.5% | 1588 | 6 | 6% | 3% | -61% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5359 | 20 | 4% | 2% | -58% | -87% | -88% |
| Morning (6am–12pm) | 5066 | 27 | 4% | 2% | -39% | -87% | -86% |
| Afternoon (12–6pm) | 4822 | 16 | 3% | 1% | -61% | -88% | -89% |
| Evening (6pm–12am) | 5802 | 17 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,425 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/16 11:43:16 AM | NATGAS | UP | 1.7 min | — | — | In play | — |
| 10/16 11:43:16 AM | GBPUSD | DOWN | 1.7 min | — | — | In play | — |
| 10/16 11:43:00 AM | GOLD | DOWN | 2.0 min | — | — | In play | — |
| 10/16 11:42:12 AM | EURUSD | DOWN | 2.8 min | — | — | In play | — |
| 10/16 11:41:40 AM | AUDUSD | DOWN | 3.3 min | — | — | In play | — |
| 10/16 11:41:24 AM | HYPE | DOWN | 3.6 min | +0.766% | — | In play | — |
| 10/16 11:40:35 AM | DOGE | DOWN | 4.4 min | +0.520% | — | In play | — |
| 10/16 11:39:47 AM | NEAR | DOWN | 5.2 min | +1.766% | — | In play | — |
| 10/16 11:39:31 AM | ZEC | DOWN | 5.5 min | +1.596% | — | In play | — |
| 10/16 11:39:15 AM | BTC | DOWN | 5.7 min | +0.643% | — | In play | — |
| 10/16 11:39:15 AM | BNB | DOWN | 5.7 min | +0.494% | — | In play | — |
| 10/16 11:39:15 AM | XRP | DOWN | 5.7 min | +0.802% | — | In play | — |
| 10/16 11:37:23 AM | SOL | DOWN | 7.6 min | +1.107% | — | In play | — |
| 10/16 11:36:20 AM | ETH | DOWN | 8.7 min | +0.799% | — | In play | — |
| 10/16 11:29:58 AM | EURUSD | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 11:29:58 AM | NATGAS | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 11:29:42 AM | SILVER | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 11:29:26 AM | COPPER | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 11:29:26 AM | AUDUSD | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 11:29:26 AM | PLATINUM | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 11:29:10 AM | GOLD | DOWN | 50 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 11:26:11 AM | HYPE | UP | 3.8 min | -0.480% | 11¢ | ❌ Lost | -$0.15 |
| 10/16 11:25:56 AM | SOL | UP | 4.0 min | -0.677% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 11:25:40 AM | BTC | UP | 4.3 min | -0.363% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 11:25:24 AM | ZEC | UP | 4.6 min | -1.025% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 11:25:08 AM | BNB | UP | 4.8 min | -0.380% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 11:25:08 AM | XRP | UP | 4.8 min | -0.600% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 11:24:52 AM | NEAR | UP | 5.1 min | -1.196% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 11:24:52 AM | DOGE | UP | 5.1 min | -0.866% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 11:24:34 AM | ETH | UP | 5.4 min | -0.710% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
