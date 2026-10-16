# 15-Minute 1¢ Study

*Updated Fri Oct 16, 7:39 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1619 finished bets | 1% | $72.45 | +40% | +4.47¢ | $38.55 / $33.90 |

*Expect about **89 buys a day** (~$13.28/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1504 | $47.25 | +29% |
| Momentum model ≥ 2%, hold to the close | 2536 | -$13.85 | -5% |
| Volatility model ≥ 5%, sell at 50¢ | 1619 | -$22.80 | -13% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 20787 | 20779 | 79 (0%) | 1.07% | -$1,424.35 (-56%) | Hold to the close: -$1,424.35 (-56%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 13289 | 4.4% | 0.4% (53) | -646% | ❌ Worse |
| Momentum model | 13289 | 4.4% | 0.4% (53) | -669% | ❌ Worse |
| Mean-reversion model | 13289 | 7.4% | 0.4% (53) | -774% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13289 | 53 | -50% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2954 | 23 | -10% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 1619 | 18 | +40% | -74% | -72% | -68% |
| Volatility model ≥ 10% | 949 | 11 | +65% | -65% | -64% | -61% |
| Momentum model ≥ 2% | 2536 | 20 | -5% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1504 | 15 | +29% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1003 | 10 | +40% | -72% | -71% | -66% |
| Mean-reversion model ≥ 2% | 4997 | 33 | -28% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3437 | 26 | -16% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2257 | 15 | -24% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13487 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5160 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2132 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 20779 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 79 | 0% | -$1,424.35 | -56% | — |
| Sell at 2¢ | 737 | 4% | -$2,240.73 | -89% | 42 sec |
| Sell at 3¢ | 494 | 2% | -$2,239.69 | -89% | 47 sec |
| Sell at 5¢ | 358 | 2% | -$2,199.65 | -87% | 50 sec |
| Sell at 10¢ | 218 | 1% | -$2,118.77 | -84% | 63 sec |
| Sell at 25¢ | 125 | 1% | -$1,948.60 | -77% | 80 sec |
| Sell at 50¢ | 82 | 0% | -$1,738.85 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 681 | 5 | 10% | 3% | -30% | -82% | -86% |
| 2–5 min | 6741 | 36 | 7% | 3% | -47% | -88% | -88% |
| 1–2 min | 5413 | 20 | 3% | 2% | -60% | -92% | -92% |
| Under 1 min | 7940 | 18 | 1% | 0% | -67% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1514 | 11 | 5% | 3% | -10% | -89% | -89% |
| HYPE | 1510 | 5 | 4% | 2% | -59% | -90% | -89% |
| ETH | 1504 | 8 | 5% | 3% | -36% | -88% | -87% |
| DOGE | 1500 | 2 | 4% | 2% | -83% | -90% | -89% |
| BNB | 1500 | 5 | 4% | 2% | -59% | -90% | -90% |
| SOL | 1497 | 2 | 3% | 2% | -84% | -92% | -91% |
| XRP | 1491 | 7 | 2% | 1% | -42% | -86% | -87% |
| BTC | 1487 | 7 | 5% | 2% | -37% | -88% | -91% |
| NEAR | 1484 | 8 | 6% | 3% | -29% | -78% | -78% |
| GOLD | 843 | 1 | 4% | 1% | -86% | -92% | -94% |
| SILVER | 819 | 4 | 3% | 1% | -44% | -79% | -80% |
| WTI | 786 | 3 | 3% | 1% | -56% | -94% | -95% |
| COPPER | 718 | 2 | 2% | 1% | -74% | -84% | -83% |
| PLATINUM | 702 | 0 | 1% | 0% | -100% | -99% | -99% |
| PALLADIUM | 647 | 2 | 1% | 0% | -71% | -84% | -84% |
| NATGAS | 645 | 5 | 2% | 2% | -28% | -81% | -80% |
| EURUSD | 638 | 3 | 3% | 1% | -56% | -81% | -80% |
| GBPUSD | 598 | 1 | 2% | 1% | -84% | -97% | -97% |
| USDJPY | 559 | 3 | 1% | 1% | -50% | -99% | -98% |
| AUDUSD | 181 | 0 | 1% | 0% | -100% | -99% | -99% |
| USDCAD | 156 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10477 | 39 | 4% | 2% | -57% | -89% | -89% |
| DOWN (bought NO) | 10302 | 40 | 4% | 2% | -55% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2232 | 11 | 2% | 1% | -17% | -79% | -79% |
| 0.05–0.1% | 2331 | 7 | 3% | 1% | -56% | -92% | -91% |
| 0.1–0.2% | 3417 | 10 | 4% | 2% | -64% | -90% | -90% |
| 0.2–0.5% | 3955 | 21 | 6% | 3% | -42% | -88% | -88% |
| Over 0.5% | 1549 | 6 | 6% | 3% | -60% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5359 | 20 | 4% | 2% | -58% | -87% | -88% |
| Morning (6am–12pm) | 4796 | 26 | 4% | 2% | -37% | -87% | -86% |
| Afternoon (12–6pm) | 4822 | 16 | 3% | 1% | -61% | -88% | -89% |
| Evening (6pm–12am) | 5802 | 17 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,425 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/16 7:39:18 AM | GOLD | DOWN | 5.7 min | — | — | In play | — |
| 10/16 7:29:54 AM | COPPER | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 7:29:54 AM | PLATINUM | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 7:29:54 AM | XRP | DOWN | 5 sec | -0.037% | 0¢ | ❌ Lost | $0.00 |
| 10/16 7:29:38 AM | SOL | UP | 21 sec | -0.076% | 0¢ | ❌ Lost | $0.00 |
| 10/16 7:29:38 AM | WTI | DOWN | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 7:29:38 AM | ZEC | DOWN | 21 sec | +0.106% | 0¢ | ❌ Lost | $0.00 |
| 10/16 7:29:07 AM | HYPE | UP | 53 sec | -0.111% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 7:29:07 AM | BNB | UP | 53 sec | -0.095% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 7:28:51 AM | BTC | UP | 69 sec | -0.069% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 7:28:51 AM | PALLADIUM | DOWN | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 7:28:19 AM | ETH | UP | 1.7 min | -0.188% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 7:27:46 AM | DOGE | UP | 2.2 min | -0.296% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 7:27:14 AM | SILVER | UP | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 7:26:10 AM | NEAR | DOWN | 3.8 min | +0.664% | 2¢ | ❌ Lost | -$0.15 |
| 10/16 7:24:32 AM | GOLD | UP | 5.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 7:14:58 AM | BTC | UP | 2 sec | -0.007% | 0¢ | ❌ Lost | $0.00 |
| 10/16 7:14:58 AM | GBPUSD | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 7:14:58 AM | SOL | DOWN | 2 sec | +0.046% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 7:14:42 AM | NATGAS | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 7:14:42 AM | NEAR | UP | 18 sec | -0.159% | 0¢ | ❌ Lost | $0.00 |
| 10/16 7:14:11 AM | ETH | DOWN | 49 sec | +0.045% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 7:14:11 AM | SILVER | UP | 49 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 7:14:11 AM | BNB | UP | 49 sec | -0.080% | 0¢ | ❌ Lost | $0.00 |
| 10/16 7:14:11 AM | DOGE | DOWN | 49 sec | +0.012% | 0¢ | ❌ Lost | $0.00 |
| 10/16 7:13:38 AM | XRP | UP | 81 sec | -0.142% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 7:13:22 AM | PLATINUM | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 7:12:50 AM | WTI | DOWN | 2.2 min | — | 4¢ | ❌ Lost | -$0.15 |
| 10/16 7:12:34 AM | AUDUSD | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 7:10:57 AM | HYPE | UP | 4.0 min | -0.305% | 6¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
