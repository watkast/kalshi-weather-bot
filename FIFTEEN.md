# 15-Minute 1¢ Study

*Updated Tue Oct 20, 6:47 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2117 finished bets | 1% | $84.10 | +35% | +3.97¢ | $23.90 / $60.20 |

*Expect about **95 buys a day** (~$14.27/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1949 | $65.35 | +30% |
| Momentum model ≥ 2%, hold to the close | 3247 | -$17.30 | -5% |
| Volatility model ≥ 5%, sell at 50¢ | 2117 | -$32.90 | -14% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 25093 | 25086 | 92 (0%) | 1.07% | -$1,761.95 (-58%) | Hold to the close: -$1,761.95 (-58%) |

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
| Volatility model | 16402 | 4.6% | 0.4% (65) | -673% | ❌ Worse |
| Momentum model | 16402 | 4.5% | 0.4% (65) | -696% | ❌ Worse |
| Mean-reversion model | 16402 | 7.7% | 0.4% (65) | -811% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16402 | 65 | -51% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3837 | 31 | -7% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2117 | 23 | +35% | -71% | -70% | -67% |
| Volatility model ≥ 10% | 1231 | 15 | +71% | -60% | -59% | -56% |
| Momentum model ≥ 2% | 3247 | 26 | -5% | -78% | -78% | -75% |
| Momentum model ≥ 5% | 1949 | 20 | +30% | -74% | -74% | -69% |
| Momentum model ≥ 10% | 1291 | 13 | +38% | -67% | -66% | -61% |
| Mean-reversion model ≥ 2% | 6406 | 42 | -29% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 4456 | 34 | -16% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2946 | 22 | -15% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16600 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5909 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2577 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 25086 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 92 | 0% | -$1,761.95 | -58% | — |
| Sell at 2¢ | 903 | 4% | -$2,689.17 | -88% | 46 sec |
| Sell at 3¢ | 614 | 2% | -$2,684.49 | -88% | 48 sec |
| Sell at 5¢ | 436 | 2% | -$2,640.55 | -87% | 51 sec |
| Sell at 10¢ | 266 | 1% | -$2,547.49 | -84% | 64 sec |
| Sell at 25¢ | 146 | 1% | -$2,356.69 | -77% | 80 sec |
| Sell at 50¢ | 95 | 0% | -$2,128.70 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 983 | 5 | 10% | 3% | -51% | -82% | -84% |
| 2–5 min | 8131 | 41 | 7% | 3% | -50% | -88% | -87% |
| 1–2 min | 6406 | 24 | 3% | 2% | -59% | -93% | -92% |
| Under 1 min | 9562 | 22 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1866 | 11 | 4% | 2% | -27% | -90% | -90% |
| HYPE | 1855 | 6 | 5% | 2% | -60% | -89% | -88% |
| BNB | 1854 | 9 | 5% | 2% | -41% | -83% | -82% |
| ETH | 1845 | 9 | 6% | 3% | -41% | -87% | -86% |
| DOGE | 1844 | 3 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1841 | 2 | 3% | 2% | -87% | -92% | -92% |
| XRP | 1835 | 7 | 3% | 1% | -53% | -87% | -88% |
| NEAR | 1830 | 10 | 6% | 3% | -30% | -79% | -79% |
| BTC | 1830 | 10 | 5% | 2% | -27% | -88% | -90% |
| GOLD | 970 | 1 | 3% | 1% | -88% | -93% | -95% |
| SILVER | 935 | 4 | 3% | 1% | -50% | -81% | -81% |
| WTI | 912 | 3 | 3% | 1% | -61% | -94% | -95% |
| COPPER | 811 | 3 | 2% | 1% | -65% | -74% | -74% |
| PLATINUM | 804 | 0 | 0% | 0% | -100% | -99% | -99% |
| NATGAS | 745 | 5 | 2% | 1% | -37% | -84% | -83% |
| EURUSD | 741 | 3 | 2% | 1% | -62% | -83% | -83% |
| PALLADIUM | 732 | 2 | 1% | 0% | -74% | -85% | -85% |
| GBPUSD | 698 | 1 | 2% | 1% | -87% | -97% | -97% |
| USDJPY | 649 | 3 | 1% | 1% | -57% | -99% | -98% |
| AUDUSD | 270 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 219 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12659 | 45 | 4% | 2% | -59% | -88% | -87% |
| DOWN (bought NO) | 12427 | 47 | 3% | 1% | -56% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2804 | 15 | 2% | 1% | -11% | -77% | -76% |
| 0.05–0.1% | 2889 | 10 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 4199 | 13 | 5% | 2% | -62% | -90% | -89% |
| 0.2–0.5% | 4838 | 23 | 6% | 3% | -48% | -88% | -87% |
| Over 0.5% | 1867 | 6 | 6% | 3% | -67% | -88% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6450 | 26 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 5867 | 29 | 4% | 2% | -43% | -87% | -86% |
| Afternoon (12–6pm) | 5807 | 19 | 3% | 1% | -61% | -89% | -89% |
| Evening (6pm–12am) | 6962 | 18 | 3% | 2% | -70% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,790 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/20 6:44:58 AM | EURUSD | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:44:42 AM | USDCAD | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:44:27 AM | USDJPY | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:44:27 AM | ZEC | UP | 33 sec | -0.060% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:44:27 AM | XRP | DOWN | 33 sec | +0.046% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:44:27 AM | SOL | DOWN | 33 sec | +0.096% | 0¢ | ❌ Lost | $0.00 |
| 10/20 6:44:27 AM | PALLADIUM | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:44:12 AM | GOLD | DOWN | 47 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:43:40 AM | BTC | DOWN | 79 sec | +0.128% | 0¢ | ❌ Lost | $0.00 |
| 10/20 6:43:40 AM | COPPER | DOWN | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:43:24 AM | SILVER | DOWN | 1.6 min | — | 1¢ | ❌ Lost | $0.00 |
| 10/20 6:43:24 AM | HYPE | DOWN | 1.6 min | +0.191% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:43:24 AM | DOGE | DOWN | 1.6 min | +0.153% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:43:09 AM | WTI | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:42:53 AM | BNB | DOWN | 2.1 min | +0.086% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:42:37 AM | PLATINUM | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:42:37 AM | ETH | DOWN | 2.4 min | +0.219% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:39:11 AM | NEAR | UP | 5.8 min | -0.934% | 11¢ | ❌ Lost | $0.00 |
| 10/20 6:29:58 AM | NATGAS | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:29:42 AM | PLATINUM | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:29:26 AM | AUDUSD | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:29:09 AM | PALLADIUM | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:28:53 AM | GBPUSD | DOWN | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:28:53 AM | EURUSD | DOWN | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:28:37 AM | USDJPY | UP | 82 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:26:28 AM | GOLD | DOWN | 3.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:25:38 AM | WTI | UP | 4.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:25:22 AM | NEAR | DOWN | 4.6 min | +0.547% | 2¢ | ❌ Lost | -$0.15 |
| 10/20 6:24:51 AM | SOL | DOWN | 5.1 min | +0.448% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:24:33 AM | XRP | DOWN | 5.5 min | +0.363% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
