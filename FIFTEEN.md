# 15-Minute 1¢ Study

*Updated Wed Oct 21, 5:26 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2300 finished bets | 1% | $76.20 | +29% | +3.31¢ | $43.20 / $33.00 |

*Expect about **97 buys a day** (~$14.56/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2131 | $57.30 | +24% |
| Volatility model ≥ 2%, hold to the close | 4226 | -$13.65 | -3% |
| Momentum model ≥ 2%, hold to the close | 3563 | -$42.45 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 27268 | 27260 | 100 (0%) | 1.07% | -$1,922.65 (-58%) | Hold to the close: -$1,922.65 (-58%) |

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
| Volatility model | 17613 | 4.6% | 0.4% (72) | -657% | ❌ Worse |
| Momentum model | 17613 | 4.6% | 0.4% (72) | -680% | ❌ Worse |
| Mean-reversion model | 17613 | 7.8% | 0.4% (72) | -795% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17613 | 72 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4226 | 36 | -3% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2300 | 24 | +29% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 1316 | 16 | +70% | -62% | -60% | -57% |
| Momentum model ≥ 2% | 3563 | 27 | -10% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2131 | 21 | +24% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1403 | 14 | +36% | -68% | -67% | -62% |
| Mean-reversion model ≥ 2% | 6981 | 47 | -27% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4875 | 39 | -12% | -80% | -79% | -76% |
| Mean-reversion model ≥ 10% | 3249 | 27 | -5% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 17811 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6507 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2942 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 27260 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 100 | 0% | -$1,922.65 | -58% | — |
| Sell at 2¢ | 998 | 4% | -$2,923.17 | -88% | 46 sec |
| Sell at 3¢ | 677 | 2% | -$2,918.62 | -88% | 48 sec |
| Sell at 5¢ | 480 | 2% | -$2,870.65 | -86% | 56 sec |
| Sell at 10¢ | 294 | 1% | -$2,769.51 | -83% | 64 sec |
| Sell at 25¢ | 160 | 1% | -$2,569.05 | -77% | 82 sec |
| Sell at 50¢ | 103 | 0% | -$2,333.40 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1105 | 6 | 11% | 4% | -48% | -81% | -84% |
| 2–5 min | 8790 | 45 | 7% | 3% | -49% | -87% | -87% |
| 1–2 min | 6935 | 26 | 3% | 1% | -59% | -93% | -92% |
| Under 1 min | 10426 | 23 | 1% | 0% | -68% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1998 | 11 | 5% | 2% | -31% | -89% | -90% |
| BNB | 1991 | 11 | 5% | 2% | -32% | -83% | -82% |
| HYPE | 1990 | 7 | 5% | 3% | -57% | -88% | -87% |
| ETH | 1978 | 10 | 6% | 3% | -40% | -86% | -86% |
| SOL | 1978 | 3 | 3% | 2% | -81% | -92% | -92% |
| DOGE | 1977 | 3 | 4% | 2% | -81% | -91% | -90% |
| XRP | 1970 | 7 | 3% | 1% | -56% | -88% | -88% |
| BTC | 1965 | 11 | 5% | 2% | -25% | -88% | -90% |
| NEAR | 1964 | 11 | 6% | 3% | -27% | -80% | -79% |
| GOLD | 1065 | 2 | 3% | 1% | -78% | -81% | -84% |
| SILVER | 1027 | 4 | 3% | 1% | -55% | -82% | -82% |
| WTI | 1006 | 3 | 3% | 1% | -65% | -94% | -95% |
| PLATINUM | 893 | 0 | 1% | 0% | -100% | -99% | -99% |
| COPPER | 884 | 3 | 1% | 1% | -68% | -76% | -76% |
| NATGAS | 824 | 5 | 2% | 1% | -43% | -85% | -84% |
| EURUSD | 818 | 3 | 2% | 1% | -66% | -84% | -84% |
| PALLADIUM | 805 | 2 | 1% | 0% | -77% | -87% | -87% |
| GBPUSD | 765 | 1 | 2% | 1% | -88% | -97% | -97% |
| USDJPY | 732 | 3 | 1% | 1% | -62% | -99% | -98% |
| AUDUSD | 326 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 285 | 0 | 0% | 0% | -100% | -99% | -99% |
| 10YRRATE | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 5 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 4 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 3 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 13704 | 50 | 4% | 2% | -58% | -88% | -87% |
| DOWN (bought NO) | 13556 | 50 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2975 | 15 | 2% | 1% | -16% | -78% | -77% |
| 0.05–0.1% | 3077 | 11 | 3% | 2% | -48% | -92% | -91% |
| 0.1–0.2% | 4541 | 16 | 5% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 5197 | 25 | 6% | 3% | -47% | -87% | -87% |
| Over 0.5% | 2018 | 7 | 7% | 3% | -64% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6844 | 28 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6595 | 31 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6489 | 20 | 4% | 2% | -64% | -88% | -89% |
| Evening (6pm–12am) | 7332 | 21 | 3% | 2% | -67% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,744 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/21 5:25:54 PM | ZEC | UP | 4.1 min | -0.456% | — | In play | — |
| 10/21 5:14:44 PM | EURUSD | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:14:28 PM | NEAR | DOWN | 31 sec | +0.023% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:14:28 PM | NATGAS | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:14:12 PM | HYPE | UP | 48 sec | -0.085% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 5:13:55 PM | ZEC | UP | 64 sec | -0.249% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 5:13:55 PM | GBPUSD | DOWN | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:13:39 PM | PLATINUM | UP | 80 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 5:12:50 PM | WTI | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:12:02 PM | USDJPY | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 5:11:45 PM | XRP | UP | 3.2 min | -0.248% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 5:11:45 PM | BNB | UP | 3.2 min | -0.172% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 5:11:13 PM | ETH | UP | 3.8 min | -0.230% | 2¢ | ❌ Lost | -$0.15 |
| 10/21 5:10:56 PM | SOL | UP | 4.0 min | -0.327% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 5:10:56 PM | BTC | UP | 4.0 min | -0.228% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 5:10:56 PM | SILVER | UP | 4.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 5:10:06 PM | DOGE | UP | 4.9 min | -0.362% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 5:08:47 PM | GOLD | UP | 6.2 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/21 4:59:44 PM | SOL | UP | 16 sec | -0.034% | 0¢ | ❌ Lost | $0.00 |
| 10/21 4:59:44 PM | NEAR | UP | 16 sec | -0.128% | 0¢ | ❌ Lost | $0.00 |
| 10/21 4:59:44 PM | SILVER | UP | 16 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 4:59:28 PM | ZEC | DOWN | 32 sec | +0.112% | 0¢ | ❌ Lost | $0.00 |
| 10/21 4:59:28 PM | NATGAS | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:59:13 PM | BTC | UP | 47 sec | -0.052% | 0¢ | ❌ Lost | $0.00 |
| 10/21 4:59:13 PM | XRP | UP | 47 sec | -0.087% | 0¢ | ❌ Lost | $0.00 |
| 10/21 4:58:56 PM | ETH | UP | 63 sec | -0.050% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 4:58:56 PM | HYPE | UP | 63 sec | -0.122% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:57:51 PM | PLATINUM | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:57:03 PM | BNB | UP | 3.0 min | -0.104% | 0¢ | ❌ Lost | $0.00 |
| 10/21 4:55:25 PM | GOLD | UP | 4.6 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
