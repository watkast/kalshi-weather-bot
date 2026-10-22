# 15-Minute 1¢ Study

*Updated Wed Oct 21, 11:39 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2322 finished bets | 1% | $73.95 | +28% | +3.18¢ | $42.00 / $31.95 |

*Expect about **97 buys a day** (~$14.54/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2151 | $55.20 | +23% |
| Volatility model ≥ 2%, hold to the close | 4275 | -$19.05 | -4% |
| Momentum model ≥ 2%, hold to the close | 3592 | -$45.30 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 27692 | 27682 | 102 (0%) | 1.07% | -$1,944.90 (-58%) | Hold to the close: -$1,944.90 (-58%) |

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
| Volatility model | 17828 | 4.6% | 0.4% (72) | -662% | ❌ Worse |
| Momentum model | 17828 | 4.6% | 0.4% (72) | -685% | ❌ Worse |
| Mean-reversion model | 17828 | 7.8% | 0.4% (72) | -800% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17828 | 72 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4275 | 36 | -4% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2322 | 24 | +28% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 1327 | 16 | +69% | -62% | -61% | -58% |
| Momentum model ≥ 2% | 3592 | 27 | -11% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2151 | 21 | +23% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1412 | 14 | +36% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 7087 | 47 | -28% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4945 | 39 | -13% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3296 | 27 | -7% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 18026 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6625 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 3031 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 27682 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 102 | 0% | -$1,944.90 | -58% | — |
| Sell at 2¢ | 1009 | 4% | -$2,970.56 | -88% | 46 sec |
| Sell at 3¢ | 686 | 2% | -$2,965.36 | -88% | 48 sec |
| Sell at 5¢ | 484 | 2% | -$2,918.30 | -87% | 59 sec |
| Sell at 10¢ | 296 | 1% | -$2,817.14 | -84% | 64 sec |
| Sell at 25¢ | 161 | 1% | -$2,601.99 | -77% | 82 sec |
| Sell at 50¢ | 104 | 0% | -$2,362.90 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1137 | 6 | 11% | 4% | -50% | -81% | -84% |
| 2–5 min | 8919 | 46 | 7% | 3% | -49% | -87% | -87% |
| 1–2 min | 7041 | 27 | 3% | 1% | -58% | -93% | -93% |
| Under 1 min | 10581 | 23 | 1% | 0% | -69% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2021 | 11 | 5% | 2% | -32% | -89% | -89% |
| BNB | 2016 | 11 | 5% | 2% | -33% | -83% | -82% |
| HYPE | 2013 | 7 | 5% | 3% | -57% | -89% | -87% |
| ETH | 2003 | 10 | 6% | 3% | -40% | -86% | -86% |
| SOL | 2002 | 3 | 3% | 1% | -81% | -92% | -92% |
| DOGE | 2000 | 3 | 4% | 2% | -81% | -91% | -90% |
| XRP | 1994 | 7 | 3% | 1% | -57% | -88% | -88% |
| NEAR | 1989 | 11 | 6% | 3% | -28% | -80% | -80% |
| BTC | 1988 | 11 | 5% | 2% | -26% | -88% | -90% |
| GOLD | 1084 | 3 | 4% | 1% | -67% | -81% | -83% |
| SILVER | 1048 | 4 | 3% | 1% | -56% | -82% | -82% |
| WTI | 1022 | 3 | 3% | 1% | -65% | -94% | -95% |
| PLATINUM | 912 | 0 | 1% | 0% | -100% | -99% | -99% |
| COPPER | 898 | 3 | 1% | 1% | -69% | -77% | -76% |
| NATGAS | 839 | 5 | 2% | 1% | -44% | -85% | -85% |
| EURUSD | 835 | 3 | 2% | 1% | -66% | -85% | -85% |
| PALLADIUM | 817 | 2 | 1% | 0% | -77% | -87% | -87% |
| GBPUSD | 783 | 1 | 2% | 1% | -88% | -97% | -97% |
| USDJPY | 752 | 4 | 1% | 1% | -50% | -99% | -98% |
| AUDUSD | 345 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 300 | 0 | 1% | 0% | -100% | -99% | -99% |
| 10YRRATE | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 5 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 5 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 4 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 13957 | 52 | 4% | 2% | -57% | -88% | -87% |
| DOWN (bought NO) | 13725 | 50 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3002 | 15 | 2% | 1% | -16% | -78% | -78% |
| 0.05–0.1% | 3111 | 11 | 3% | 2% | -48% | -92% | -91% |
| 0.1–0.2% | 4609 | 16 | 5% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 5259 | 25 | 6% | 3% | -48% | -88% | -87% |
| Over 0.5% | 2042 | 7 | 7% | 3% | -65% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6844 | 28 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6595 | 31 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6540 | 20 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 7703 | 23 | 3% | 1% | -66% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,742 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/21 11:39:47 PM | NEAR | UP | 5.2 min | -0.653% | — | In play | — |
| 10/21 11:39:14 PM | BNB | UP | 5.8 min | -0.195% | — | In play | — |
| 10/21 11:38:09 PM | ZEC | UP | 6.8 min | -0.869% | — | In play | — |
| 10/21 11:29:46 PM | GBPUSD | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 11:29:46 PM | SILVER | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 11:29:46 PM | WTI | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 11:29:20 PM | NATGAS | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 11:28:47 PM | USDJPY | UP | 73 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 11:28:31 PM | SOL | DOWN | 89 sec | +0.246% | 0¢ | ❌ Lost | $0.00 |
| 10/21 11:28:16 PM | BNB | DOWN | 1.7 min | +0.091% | 0¢ | ❌ Lost | $0.00 |
| 10/21 11:28:16 PM | DOGE | DOWN | 1.7 min | +0.138% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 11:28:00 PM | ZEC | DOWN | 2.0 min | +0.320% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 11:28:00 PM | ETH | DOWN | 2.0 min | +0.126% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 11:28:00 PM | HYPE | DOWN | 2.0 min | +0.214% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 11:27:44 PM | XRP | DOWN | 2.3 min | +0.164% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 11:27:11 PM | COPPER | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 11:27:11 PM | NEAR | DOWN | 2.8 min | +0.412% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 11:26:07 PM | BTC | DOWN | 3.9 min | +0.172% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 11:14:12 PM | GOLD | UP | 48 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 11:14:12 PM | USDCAD | UP | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 11:14:12 PM | SILVER | UP | 48 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/21 11:13:56 PM | HYPE | UP | 64 sec | -0.149% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 11:13:40 PM | AUDUSD | UP | 80 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 11:13:24 PM | BNB | UP | 1.6 min | -0.111% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 11:12:51 PM | XRP | UP | 2.1 min | -0.260% | 0¢ | ❌ Lost | $0.00 |
| 10/21 11:12:35 PM | DOGE | UP | 2.4 min | -0.162% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 11:12:19 PM | ETH | UP | 2.7 min | -0.152% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 11:12:19 PM | NEAR | UP | 2.7 min | -0.394% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 11:12:19 PM | SOL | UP | 2.7 min | -0.216% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 11:12:03 PM | BTC | UP | 3.0 min | -0.117% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
