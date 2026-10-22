# 15-Minute 1¢ Study

*Updated Wed Oct 21, 10:28 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2319 finished bets | 1% | $74.25 | +28% | +3.20¢ | $42.30 / $31.95 |

*Expect about **97 buys a day** (~$14.55/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2149 | $55.35 | +23% |
| Volatility model ≥ 2%, hold to the close | 4267 | -$18.15 | -3% |
| Momentum model ≥ 2%, hold to the close | 3589 | -$45.00 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 27619 | 27611 | 102 (0%) | 1.07% | -$1,936.50 (-58%) | Hold to the close: -$1,936.50 (-58%) |

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
| Volatility model | 17784 | 4.6% | 0.4% (72) | -661% | ❌ Worse |
| Momentum model | 17784 | 4.6% | 0.4% (72) | -684% | ❌ Worse |
| Mean-reversion model | 17784 | 7.8% | 0.4% (72) | -798% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17784 | 72 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4267 | 36 | -3% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2319 | 24 | +28% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 1326 | 16 | +69% | -62% | -61% | -58% |
| Momentum model ≥ 2% | 3589 | 27 | -11% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2149 | 21 | +23% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1411 | 14 | +36% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 7061 | 47 | -27% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4929 | 39 | -13% | -80% | -80% | -76% |
| Mean-reversion model ≥ 10% | 3285 | 27 | -6% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 17982 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6607 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 3022 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 27611 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 102 | 0% | -$1,936.50 | -58% | — |
| Sell at 2¢ | 1007 | 4% | -$2,962.68 | -88% | 46 sec |
| Sell at 3¢ | 684 | 2% | -$2,957.74 | -88% | 48 sec |
| Sell at 5¢ | 484 | 2% | -$2,909.90 | -86% | 59 sec |
| Sell at 10¢ | 296 | 1% | -$2,808.74 | -83% | 64 sec |
| Sell at 25¢ | 161 | 1% | -$2,593.59 | -77% | 82 sec |
| Sell at 50¢ | 104 | 0% | -$2,354.50 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1132 | 6 | 11% | 4% | -49% | -81% | -84% |
| 2–5 min | 8891 | 46 | 7% | 3% | -49% | -87% | -87% |
| 1–2 min | 7030 | 27 | 3% | 1% | -58% | -93% | -92% |
| Under 1 min | 10554 | 23 | 1% | 0% | -69% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2016 | 11 | 5% | 2% | -32% | -89% | -89% |
| BNB | 2011 | 11 | 5% | 2% | -33% | -83% | -82% |
| HYPE | 2008 | 7 | 5% | 3% | -57% | -89% | -87% |
| ETH | 1998 | 10 | 6% | 3% | -40% | -86% | -86% |
| SOL | 1997 | 3 | 3% | 2% | -81% | -92% | -92% |
| DOGE | 1996 | 3 | 4% | 2% | -81% | -91% | -90% |
| XRP | 1989 | 7 | 3% | 1% | -57% | -88% | -88% |
| NEAR | 1984 | 11 | 6% | 3% | -28% | -80% | -80% |
| BTC | 1983 | 11 | 5% | 2% | -26% | -88% | -90% |
| GOLD | 1081 | 3 | 4% | 1% | -67% | -81% | -83% |
| SILVER | 1044 | 4 | 3% | 1% | -56% | -82% | -83% |
| WTI | 1018 | 3 | 3% | 1% | -65% | -94% | -95% |
| PLATINUM | 910 | 0 | 1% | 0% | -100% | -99% | -99% |
| COPPER | 897 | 3 | 1% | 1% | -69% | -77% | -76% |
| NATGAS | 835 | 5 | 2% | 1% | -44% | -85% | -84% |
| EURUSD | 835 | 3 | 2% | 1% | -66% | -85% | -85% |
| PALLADIUM | 817 | 2 | 1% | 0% | -77% | -87% | -87% |
| GBPUSD | 782 | 1 | 2% | 1% | -88% | -97% | -97% |
| USDJPY | 748 | 4 | 1% | 1% | -50% | -99% | -98% |
| AUDUSD | 343 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 298 | 0 | 1% | 0% | -100% | -99% | -99% |
| 10YRRATE | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 5 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 5 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 4 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 13920 | 52 | 4% | 2% | -57% | -88% | -87% |
| DOWN (bought NO) | 13691 | 50 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3000 | 15 | 2% | 1% | -16% | -78% | -78% |
| 0.05–0.1% | 3105 | 11 | 3% | 2% | -48% | -92% | -91% |
| 0.1–0.2% | 4589 | 16 | 5% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 5246 | 25 | 6% | 3% | -48% | -87% | -87% |
| Over 0.5% | 2039 | 7 | 7% | 3% | -65% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6844 | 28 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6595 | 31 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6540 | 20 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 7632 | 23 | 3% | 1% | -66% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,736 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/21 10:27:35 PM | BNB | UP | 2.4 min | -0.115% | — | In play | — |
| 10/21 10:14:55 PM | ETH | UP | 4 sec | -0.018% | 0¢ | ❌ Lost | $0.00 |
| 10/21 10:14:55 PM | PALLADIUM | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:14:55 PM | COPPER | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:14:39 PM | DOGE | UP | 20 sec | -0.080% | 0¢ | ❌ Lost | $0.00 |
| 10/21 10:14:39 PM | PLATINUM | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:14:39 PM | SOL | UP | 20 sec | -0.092% | 0¢ | ❌ Lost | $0.00 |
| 10/21 10:14:23 PM | BNB | DOWN | 36 sec | -0.003% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:14:23 PM | BTC | UP | 36 sec | -0.030% | 0¢ | ❌ Lost | $0.00 |
| 10/21 10:14:23 PM | ZEC | UP | 36 sec | -0.158% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:14:07 PM | USDJPY | UP | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:14:07 PM | XRP | DOWN | 52 sec | +0.045% | 0¢ | ❌ Lost | $0.00 |
| 10/21 10:13:51 PM | EURUSD | DOWN | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:13:51 PM | GBPUSD | DOWN | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 10:13:35 PM | HYPE | DOWN | 84 sec | +0.138% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 10:13:19 PM | SILVER | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 10:13:19 PM | NEAR | UP | 1.7 min | -0.346% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 9:59:52 PM | DOGE | DOWN | 8 sec | +0.040% | 0¢ | ❌ Lost | $0.00 |
| 10/21 9:59:52 PM | AUDUSD | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 9:59:52 PM | BNB | DOWN | 8 sec | -0.028% | 0¢ | ❌ Lost | $0.00 |
| 10/21 9:59:52 PM | SOL | DOWN | 8 sec | -0.009% | 0¢ | ❌ Lost | $0.00 |
| 10/21 9:59:05 PM | ETH | DOWN | 54 sec | +0.057% | 0¢ | ❌ Lost | $0.00 |
| 10/21 9:59:05 PM | XRP | DOWN | 54 sec | +0.082% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 9:59:05 PM | COPPER | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 9:58:49 PM | SILVER | UP | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 9:58:33 PM | GOLD | UP | 87 sec | — | 1¢ | ❌ Lost | $0.00 |
| 10/21 9:58:17 PM | WTI | DOWN | 1.7 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/21 9:58:17 PM | NATGAS | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 9:58:17 PM | ZEC | UP | 1.7 min | -0.316% | 1¢ | ❌ Lost | $0.00 |
| 10/21 9:57:42 PM | EURUSD | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
