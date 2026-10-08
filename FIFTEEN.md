# 15-Minute 1¢ Study

*Updated Thu Oct 8, 11:26 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 788 finished bets | 1% | $26.95 | +32% | +3.42¢ | -$13.85 / $40.80 |

*Expect about **75 buys a day** (~$11.31/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 788 | $13.70 | +16% |
| 5+ min left, hold to the close | 335 | $6.50 | +13% |
| Volatility model ≥ 5%, sell at 50¢ | 788 | -$3.05 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 11906 | 11892 | 49 (0%) | 1.07% | -$759.10 (-53%) | Hold to the close: -$759.10 (-53%) |

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
| Volatility model | 7619 | 4.0% | 0.4% (33) | -567% | ❌ Worse |
| Momentum model | 7619 | 4.1% | 0.4% (33) | -599% | ❌ Worse |
| Mean-reversion model | 7619 | 6.7% | 0.4% (33) | -664% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7619 | 33 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 1456 | 12 | -4% | -74% | -74% | -70% |
| Volatility model ≥ 5% | 788 | 8 | +32% | -64% | -63% | -60% |
| Volatility model ≥ 10% | 489 | 6 | +81% | -47% | -48% | -43% |
| Momentum model ≥ 2% | 1291 | 10 | -7% | -75% | -76% | -74% |
| Momentum model ≥ 5% | 788 | 7 | +16% | -68% | -70% | -67% |
| Momentum model ≥ 10% | 539 | 6 | +60% | -57% | -58% | -55% |
| Mean-reversion model ≥ 2% | 2624 | 19 | -21% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1771 | 15 | -6% | -82% | -82% | -76% |
| Mean-reversion model ≥ 10% | 1169 | 11 | +9% | -80% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7816 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3034 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1042 | 2% | 2% | 2% | 1% | 1% | 0% |
| **All** | 11892 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 49 | 0% | -$759.10 | -53% | — |
| Sell at 2¢ | 411 | 3% | -$1,296.24 | -90% | 33 sec |
| Sell at 3¢ | 272 | 2% | -$1,297.02 | -90% | 47 sec |
| Sell at 5¢ | 201 | 2% | -$1,272.45 | -88% | 50 sec |
| Sell at 10¢ | 131 | 1% | -$1,217.49 | -84% | 64 sec |
| Sell at 25¢ | 75 | 1% | -$1,112.85 | -77% | 82 sec |
| Sell at 50¢ | 49 | 0% | -$988.35 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 331 | 4 | 11% | 4% | +15% | -81% | -84% |
| 2–5 min | 3883 | 25 | 6% | 3% | -37% | -88% | -89% |
| 1–2 min | 3118 | 12 | 3% | 2% | -58% | -94% | -94% |
| Under 1 min | 4556 | 8 | 1% | 0% | -74% | -89% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 876 | 6 | 5% | 3% | -18% | -90% | -90% |
| HYPE | 875 | 3 | 5% | 3% | -58% | -89% | -87% |
| DOGE | 871 | 2 | 3% | 1% | -71% | -92% | -91% |
| BNB | 870 | 3 | 4% | 2% | -59% | -91% | -92% |
| ETH | 869 | 7 | 5% | 3% | -0% | -89% | -88% |
| NEAR | 865 | 5 | 6% | 3% | -25% | -71% | -73% |
| SOL | 865 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 864 | 4 | 5% | 2% | -39% | -88% | -90% |
| XRP | 861 | 5 | 2% | 1% | -27% | -81% | -81% |
| GOLD | 507 | 0 | 4% | 1% | -100% | -91% | -94% |
| SILVER | 493 | 0 | 3% | 1% | -100% | -94% | -94% |
| WTI | 466 | 3 | 3% | 1% | -29% | -95% | -97% |
| COPPER | 434 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 396 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 373 | 3 | 3% | 2% | -25% | -95% | -93% |
| PALLADIUM | 365 | 1 | 1% | 1% | -74% | -98% | -99% |
| EURUSD | 362 | 3 | 3% | 2% | -23% | -68% | -67% |
| GBPUSD | 344 | 1 | 3% | 2% | -73% | -95% | -95% |
| USDJPY | 310 | 3 | 1% | 1% | -10% | -98% | -97% |
| AUDUSD | 14 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 12 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6069 | 26 | 4% | 2% | -50% | -89% | -88% |
| DOWN (bought NO) | 5823 | 23 | 3% | 2% | -55% | -91% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1268 | 8 | 2% | 1% | +9% | -67% | -66% |
| 0.05–0.1% | 1315 | 4 | 3% | 1% | -55% | -91% | -92% |
| 0.1–0.2% | 1973 | 6 | 3% | 2% | -62% | -92% | -92% |
| 0.2–0.5% | 2304 | 12 | 5% | 3% | -43% | -89% | -88% |
| Over 0.5% | 954 | 5 | 6% | 2% | -46% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3090 | 17 | 4% | 2% | -37% | -85% | -85% |
| Morning (6am–12pm) | 2975 | 17 | 4% | 2% | -35% | -91% | -90% |
| Afternoon (12–6pm) | 2560 | 7 | 3% | 1% | -68% | -88% | -89% |
| Evening (6pm–12am) | 3267 | 8 | 3% | 1% | -72% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,054 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/8 11:25:45 AM | BTC | UP | 4.2 min | -0.541% | — | In play | — |
| 10/8 11:25:14 AM | XRP | UP | 4.8 min | -1.565% | — | In play | — |
| 10/8 11:24:58 AM | SOL | UP | 5.0 min | -1.309% | — | In play | — |
| 10/8 11:24:42 AM | DOGE | UP | 5.3 min | -1.172% | — | In play | — |
| 10/8 11:24:42 AM | HYPE | UP | 5.3 min | -1.212% | — | In play | — |
| 10/8 11:24:25 AM | BNB | UP | 5.6 min | -0.750% | — | In play | — |
| 10/8 11:22:50 AM | NEAR | UP | 7.2 min | -3.334% | — | In play | — |
| 10/8 11:14:56 AM | BTC | UP | 4 sec | -0.010% | 0¢ | ❌ Lost | $0.00 |
| 10/8 11:14:56 AM | NEAR | UP | 4 sec | -0.032% | 0¢ | ❌ Lost | $0.00 |
| 10/8 11:14:56 AM | USDCAD | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:14:56 AM | SOL | DOWN | 4 sec | +0.035% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 11:14:56 AM | AUDUSD | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:14:41 AM | BNB | DOWN | 19 sec | +0.059% | 0¢ | ❌ Lost | $0.00 |
| 10/8 11:14:41 AM | DOGE | DOWN | 19 sec | +0.146% | 0¢ | ❌ Lost | $0.00 |
| 10/8 11:14:25 AM | XRP | UP | 35 sec | -0.097% | 0¢ | ❌ Lost | $0.00 |
| 10/8 11:13:53 AM | HYPE | DOWN | 67 sec | +0.245% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:13:37 AM | COPPER | DOWN | 82 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:13:21 AM | ZEC | DOWN | 1.6 min | +0.900% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:13:21 AM | ETH | DOWN | 1.6 min | +0.365% | 0¢ | ❌ Lost | $0.00 |
| 10/8 11:13:21 AM | NATGAS | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:12:49 AM | GBPUSD | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:12:18 AM | PALLADIUM | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:12:18 AM | SILVER | DOWN | 2.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 11:11:31 AM | PLATINUM | DOWN | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:11:15 AM | GOLD | DOWN | 3.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 11:10:43 AM | EURUSD | DOWN | 4.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:08:21 AM | USDJPY | UP | 6.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 10:58:43 AM | GOLD | DOWN | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 10:58:27 AM | USDCAD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 10:58:11 AM | HYPE | UP | 1.8 min | -0.568% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
