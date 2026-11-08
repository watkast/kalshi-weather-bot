# 15-Minute 1¢ Study

*Updated Sun Nov 8, 2:31 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4010 finished bets | 1% | $142.05 | +32% | +3.54¢ | $97.60 / $44.45 |

*Expect about **96 buys a day** (~$14.45/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3724 | $72.80 | +18% |
| Volatility model ≥ 2%, hold to the close | 7349 | $25.45 | +3% |
| Momentum model ≥ 2%, hold to the close | 6071 | -$39.50 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 49767 | 49750 | 180 (0%) | 1.07% | -$3,528.30 (-58%) | Hold to the close: -$3,528.30 (-58%) |

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
| Volatility model | 30507 | 4.8% | 0.4% (116) | -709% | ❌ Worse |
| Momentum model | 30507 | 4.6% | 0.4% (116) | -735% | ❌ Worse |
| Mean-reversion model | 30507 | 8.1% | 0.4% (116) | -857% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 30507 | 116 | -51% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 7349 | 65 | +3% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4010 | 42 | +32% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2317 | 27 | +67% | -61% | -59% | -56% |
| Momentum model ≥ 2% | 6071 | 47 | -6% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 3724 | 34 | +18% | -73% | -73% | -69% |
| Momentum model ≥ 10% | 2445 | 23 | +32% | -65% | -64% | -60% |
| Mean-reversion model ≥ 2% | 12587 | 84 | -27% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 8828 | 73 | -8% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 5909 | 53 | +2% | -76% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 30712 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11670 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7368 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 49750 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 180 | 0% | -$3,528.30 | -58% | — |
| Sell at 2¢ | 1948 | 4% | -$5,261.82 | -87% | 47 sec |
| Sell at 3¢ | 1324 | 3% | -$5,251.94 | -87% | 48 sec |
| Sell at 5¢ | 920 | 2% | -$5,142.30 | -85% | 63 sec |
| Sell at 10¢ | 555 | 1% | -$4,929.25 | -81% | 65 sec |
| Sell at 25¢ | 289 | 1% | -$4,587.71 | -76% | 83 sec |
| Sell at 50¢ | 184 | 0% | -$4,204.30 | -70% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2468 | 11 | 11% | 4% | -58% | -81% | -82% |
| 2–5 min | 16025 | 84 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 12565 | 40 | 3% | 2% | -65% | -92% | -92% |
| Under 1 min | 18680 | 45 | 1% | 0% | -65% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3444 | 13 | 5% | 2% | -51% | -88% | -88% |
| SOL | 3435 | 14 | 4% | 2% | -48% | -87% | -87% |
| HYPE | 3428 | 11 | 5% | 2% | -60% | -89% | -88% |
| BNB | 3419 | 17 | 5% | 2% | -37% | -86% | -85% |
| DOGE | 3418 | 6 | 4% | 2% | -78% | -91% | -90% |
| ETH | 3410 | 13 | 7% | 3% | -53% | -81% | -81% |
| NEAR | 3392 | 16 | 5% | 2% | -39% | -85% | -85% |
| BTC | 3388 | 16 | 5% | 2% | -35% | -88% | -89% |
| XRP | 3378 | 12 | 3% | 1% | -56% | -90% | -89% |
| GOLD | 1783 | 5 | 5% | 2% | -66% | -81% | -83% |
| WTI | 1751 | 6 | 4% | 1% | -59% | -92% | -92% |
| SILVER | 1733 | 8 | 5% | 2% | -45% | -82% | -81% |
| PLATINUM | 1567 | 4 | 2% | 1% | -76% | -96% | -96% |
| EURUSD | 1503 | 4 | 2% | 1% | -75% | -90% | -89% |
| COPPER | 1471 | 6 | 2% | 1% | -62% | -72% | -71% |
| NATGAS | 1433 | 8 | 2% | 1% | -48% | -77% | -76% |
| GBPUSD | 1426 | 4 | 2% | 1% | -74% | -96% | -96% |
| PALLADIUM | 1408 | 3 | 1% | 0% | -80% | -91% | -92% |
| USDJPY | 1406 | 5 | 2% | 1% | -67% | -97% | -96% |
| AUDUSD | 960 | 4 | 2% | 1% | -61% | -87% | -87% |
| USDCAD | 929 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 524 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 303 | 1 | 4% | 1% | -69% | -62% | -60% |
| 2YRRATE | 287 | 3 | 4% | 1% | -2% | -28% | -27% |
| 30YRRATE | 285 | 0 | 2% | 1% | -100% | -96% | -95% |
| 5YRRATE | 262 | 1 | 4% | 2% | -64% | -93% | -95% |
| INX | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 25233 | 95 | 4% | 2% | -57% | -88% | -87% |
| DOWN (bought NO) | 24517 | 85 | 4% | 2% | -60% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5031 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5291 | 19 | 3% | 2% | -45% | -91% | -91% |
| 0.1–0.2% | 7934 | 26 | 4% | 2% | -59% | -90% | -90% |
| 0.2–0.5% | 9068 | 35 | 6% | 3% | -57% | -87% | -87% |
| Over 0.5% | 3380 | 13 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12179 | 42 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12223 | 54 | 4% | 2% | -50% | -84% | -84% |
| Afternoon (12–6pm) | 11985 | 43 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 13363 | 41 | 3% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,936 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/8 2:29:32 PM | SOL | UP | 28 sec | -0.058% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 2:29:17 PM | BTC | UP | 42 sec | -0.040% | 0¢ | ❌ Lost | $0.00 |
| 11/8 2:28:59 PM | ETH | UP | 61 sec | -0.055% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 2:28:43 PM | BNB | UP | 77 sec | -0.146% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 2:27:37 PM | HYPE | UP | 2.4 min | -0.328% | 0¢ | ❌ Lost | $0.00 |
| 11/8 2:27:06 PM | NEAR | UP | 2.9 min | -0.487% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 2:26:48 PM | XRP | UP | 3.2 min | -0.392% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 2:26:32 PM | DOGE | UP | 3.5 min | -0.256% | 2¢ | ❌ Lost | -$0.15 |
| 11/8 2:26:32 PM | ZEC | UP | 3.5 min | -0.752% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 2:14:14 PM | BTC | UP | 46 sec | -0.020% | 0¢ | ❌ Lost | $0.00 |
| 11/8 2:13:58 PM | ETH | UP | 62 sec | -0.072% | 0¢ | ❌ Lost | $0.00 |
| 11/8 2:13:42 PM | DOGE | UP | 78 sec | -0.138% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 2:13:42 PM | ZEC | UP | 78 sec | -0.305% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 2:13:09 PM | XRP | UP | 1.9 min | -0.191% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 2:12:37 PM | NEAR | UP | 2.4 min | -0.504% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 2:12:04 PM | HYPE | UP | 2.9 min | -0.276% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 1:59:31 PM | NEAR | UP | 28 sec | -0.113% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 1:58:09 PM | ETH | UP | 1.8 min | -0.112% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 1:58:09 PM | DOGE | UP | 1.8 min | -0.108% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 1:57:37 PM | XRP | DOWN | 2.4 min | +0.209% | 3¢ | ❌ Lost | -$0.15 |
| 11/8 1:57:21 PM | HYPE | UP | 2.6 min | -0.257% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 1:57:21 PM | BNB | UP | 2.6 min | -0.098% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 1:55:43 PM | BTC | UP | 4.3 min | -0.111% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 1:55:43 PM | SOL | UP | 4.3 min | -0.296% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 1:55:11 PM | ZEC | UP | 4.8 min | -0.742% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 1:44:13 PM | NEAR | UP | 47 sec | -0.129% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 1:41:53 PM | BTC | UP | 3.1 min | -0.115% | 6¢ | ❌ Lost | -$0.15 |
| 11/8 1:41:08 PM | XRP | UP | 3.9 min | -0.321% | 3¢ | ❌ Lost | -$0.15 |
| 11/8 1:39:38 PM | DOGE | UP | 5.3 min | -0.197% | 31¢ | ❌ Lost | -$0.15 |
| 11/8 1:39:38 PM | SOL | UP | 5.3 min | -0.329% | 8¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
